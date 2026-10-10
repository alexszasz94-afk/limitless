/**
 * One scrape cycle:
 *   1. sync config -> DB, close runs a crashed process left "running"
 *   2. reconcile the cost of recent runs (Apify billing lags 1-2 min)
 *   3. discovery per account when its slot is due (new posts + fresh numbers
 *      for the newest ones + TikTok followers)
 *   4. follower counts (Instagram, Facebook) once a day
 *   5. refresh every post that is due, one batched run per platform
 *   6. rebuild derived numbers for touched posts, surge rules, auto-repair
 *      sweep, every Apify key checked for the Keys page
 *
 * Failure discipline: a failed or empty scrape writes NO snapshot (zeros never
 * enter history); a post missing from 2 refreshes in a row is marked gone
 * (history kept); a platform whose refresh yields nothing backs off
 * exponentially instead of billing every hour. Budget discipline: every
 * Apify run is pre-checked against config/budget.json.
 */
import { type Platform, PLATFORMS, loadBudget, loadCadence } from "../lib/config";
import {
  type AccountRow,
  type Db,
  type PostRow,
  accountHasPosts,
  clearPostFailures,
  closeStaleRuns,
  deactivatePost,
  finishRun,
  getAccount,
  getDb,
  getMeta,
  getPostByPlatformId,
  insertFollowers,
  listAccounts,
  listActivePosts,
  listUnreconciledRuns,
  markPostRefreshed,
  monthCostUsd,
  nowIso,
  recordPostFailure,
  setMeta,
  setRunCost,
  startRun,
  upsertPost,
} from "../lib/db";
import { syncConfigToDb } from "../lib/sync";
import { ApifyError, abortRun, getRun, runActorAndWait } from "../lib/apify/client";
import { getUsableKey, markKeyExhausted, noteKeySpend, tokenForLabel } from "../lib/apify/keys";
import { refreshKeyPool } from "../lib/keypool";
import {
  ACTORS,
  PRICE_PER_ITEM,
  PRICE_PER_PROFILE,
  type Parsed,
  type ParsedPost,
  inputs,
  parseFacebookPage,
  parseInstagramProfile,
  parserFor,
} from "../lib/apify/actors";
import { guardedInsertSnapshot, sweepPoisonedSnapshots } from "../lib/guard";
import { recomputePostById } from "../lib/rollup";
import { applySurgeRules, duePosts } from "../lib/cadence";
import { localHour } from "../lib/time";

const MAX_CONSECUTIVE_FAILURES = 2;
const BACKOFF_HOURS = [1, 2, 4, 8, 12];
const LOCK_KEY = "cycle_lock";
const LOCK_STALE_MS = 45 * 60 * 1000;
const H = 3600 * 1000;

export type Trigger = "schedule" | "manual";

export interface CycleResult {
  skippedBecauseLocked?: boolean;
  discoveryRuns: number;
  profileRuns: number;
  refreshRuns: number;
  postsRefreshed: number;
  newPosts: number;
  failures: number;
  notes: string[];
}

// ---------------------------------------------------------------- lock

/** One cycle at a time across processes (scheduler + a manual CLI run). */
// The lock records when it was last renewed ("since") and who holds it. Every
// actor run renews it, so a long cycle is never mistaken for a dead one, and a
// cycle only ever releases its own lock.
let lockOwner: string | null = null;

function acquireLock(db: Db): boolean {
  const owner = `${process.pid}-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
  const ok = db
    .transaction(() => {
      const cur = getMeta(db, LOCK_KEY);
      if (cur) {
        const since = Date.parse((JSON.parse(cur) as { since: string }).since);
        if (Date.now() - since < LOCK_STALE_MS) return false;
      }
      setMeta(db, LOCK_KEY, JSON.stringify({ since: nowIso(), owner }));
      return true;
    })
    .immediate();
  if (ok) lockOwner = owner;
  return ok;
}

function renewLock(db: Db) {
  if (!lockOwner) return;
  db.transaction(() => {
    const cur = getMeta(db, LOCK_KEY);
    if (cur && (JSON.parse(cur) as { owner?: string }).owner === lockOwner) {
      setMeta(db, LOCK_KEY, JSON.stringify({ since: nowIso(), owner: lockOwner }));
    }
  }).immediate();
}

function releaseLock(db: Db) {
  db.transaction(() => {
    const cur = getMeta(db, LOCK_KEY);
    if (cur && (JSON.parse(cur) as { owner?: string }).owner === lockOwner) setMeta(db, LOCK_KEY, null);
  }).immediate();
  lockOwner = null;
}

// ---------------------------------------------------------------- helpers

const statusFor = (ok: number, failed: number) => (ok === 0 && failed > 0 ? "error" : ok > 0 && failed > 0 ? "partial" : "ok");

const sameHandle = (a: string | null | undefined, b: string) =>
  !!a && a.replace(/^@/, "").toLowerCase() === b.replace(/^@/, "").toLowerCase();

function budgetRemaining(db: Db): number {
  return loadBudget().monthlyBudgetUsd - monthCostUsd(db, new Date().toISOString().slice(0, 7));
}

interface RunOutcome {
  runId: number;
  items: unknown[] | null; // null = the run failed (its row is already finished as error/budget_stop)
}

/**
 * Start one actor run with budget check and key rotation. A key refused at
 * start (out of credit, or its 5-concurrent-runs limit) is skipped and the
 * next key is tried, up to 4 keys. The run row is finished "ok" on success;
 * callers then rewrite its status from what the items actually contained.
 */
async function executeActorRun(
  db: Db,
  o: {
    kind: string;
    trigger: Trigger;
    platform: Platform | null;
    actor: string;
    input: unknown;
    estimatedUsd: number;
    timeoutMs?: number;
  },
): Promise<RunOutcome> {
  renewLock(db);
  const runId = startRun(db, { kind: o.kind, trigger: o.trigger, platform: o.platform, actor: o.actor, input: o.input });
  const remaining = budgetRemaining(db);
  if (o.estimatedUsd > remaining) {
    finishRun(db, runId, {
      status: "budget_stop",
      error: `monthly budget reached (estimate $${o.estimatedUsd.toFixed(3)}, left $${Math.max(0, remaining).toFixed(3)})`,
    });
    console.error(`[budget] stop: ${o.kind}/${o.platform ?? "-"} skipped`);
    return { runId, items: null };
  }
  const skip = new Set<string>();
  let lastError = "no usable Apify key (all invalid, over their cap, or busy)";
  for (let attempt = 0; attempt < 4; attempt++) {
    const key = await getUsableKey(o.estimatedUsd, skip);
    if (!key) break;
    db.prepare(`UPDATE scrape_runs SET key_label=? WHERE id=?`).run(key.label, runId);
    try {
      const { run, items } = await runActorAndWait(key.token, o.actor, o.input, o.timeoutMs, (apifyRunId) =>
        // Recorded the moment the run exists, with the estimate as provisional cost:
        // a crash, restart or failure later still has its real cost read back.
        db.prepare(`UPDATE scrape_runs SET apify_run_id=?, cost_usd=? WHERE id=?`).run(apifyRunId, o.estimatedUsd, runId),
      );
      const cost = run.usageTotalUsd ?? o.estimatedUsd;
      finishRun(db, runId, { status: "ok", apifyRunId: run.id, costUsd: cost, itemsOk: items.length });
      noteKeySpend(key.label, cost);
      return { runId, items };
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      lastError = msg;
      if (e instanceof ApifyError && e.runId) {
        // It ran (and billed): keep the run id and provisional cost, stop here.
        noteKeySpend(key.label, o.estimatedUsd);
        break;
      }
      const refusedAtStart =
        e instanceof ApifyError &&
        (e.httpStatus === 402 ||
          e.httpStatus === 403 ||
          /concurrent|limit|credit|payment|usage|exceed/i.test(`${e.apifyType ?? ""} ${msg}`));
      if (refusedAtStart) {
        if (!/concurrent/i.test(`${(e as ApifyError).apifyType ?? ""} ${msg}`)) markKeyExhausted(key.label);
        skip.add(key.label);
        continue; // try the next key
      }
      break; // the actor itself failed: not a key problem
    }
  }
  finishRun(db, runId, { status: "error", error: lastError.slice(0, 500) });
  console.error(`[run] ${o.kind}/${o.platform ?? "-"} ${o.actor} failed: ${lastError}`);
  return { runId, items: null };
}

async function reconcileCosts(db: Db): Promise<void> {
  const since = new Date(Date.now() - 48 * 3600 * 1000).toISOString();
  for (const run of listUnreconciledRuns(db, since)) {
    const token = tokenForLabel(run.key_label);
    const old = Date.now() - Date.parse(run.started_at) > 10 * 60 * 1000;
    if (!token || !run.apify_run_id) {
      if (old) setRunCost(db, run.id, run.cost_usd, true);
      continue;
    }
    try {
      const info = await getRun(token, run.apify_run_id);
      if (info.usageTotalUsd !== null) setRunCost(db, run.id, info.usageTotalUsd, old);
    } catch {
      // try again next cycle
    }
  }
}

/** Store one post observation. Returns false when the guard refused it. */
function ingestPost(
  db: Db,
  account: AccountRow,
  p: ParsedPost,
  runId: number,
  observedAt: string,
  raw: unknown,
): { postId: number; isNew: boolean; written: boolean } {
  const { id, isNew } = upsertPost(db, {
    accountId: account.id,
    platform: account.platform,
    platformPostId: p.platformPostId,
    url: p.url,
    caption: p.caption,
    postedAt: p.postedAt,
    seenAt: observedAt,
  });
  const written = guardedInsertSnapshot(db, { postId: id, runId, observedAt, metrics: p.metrics, raw });
  markPostRefreshed(db, id, observedAt);
  if (written) clearPostFailures(db, id);
  return { postId: id, isNew, written };
}

function recordFollowersFrom(db: Db, account: AccountRow, parsed: Parsed[], runId: number, at: string): boolean {
  for (const p of parsed) {
    const author = p.kind === "post" ? p.author : p.kind === "profile" ? p.author : null;
    if (author && author.followers !== null && sameHandle(author.handle, account.handle)) {
      insertFollowers(db, account.id, runId, at, author.followers);
      return true;
    }
  }
  return false;
}

// ---------------------------------------------------------------- discovery

async function discoverAccount(
  db: Db,
  trigger: Trigger,
  account: AccountRow,
): Promise<{ ok: boolean; newPosts: number; touched: number[] }> {
  const n = loadCadence().discovery.resultsPerProfile;
  const attempts: Array<{ actor: string; input: unknown; items: number }> =
    account.platform === "tiktok"
      ? [{ actor: ACTORS.tiktokDiscovery, input: inputs.tiktokDiscovery(account.handle, n), items: n }]
      : account.platform === "instagram"
        ? [
            { actor: ACTORS.instagramDiscovery, input: inputs.instagramDiscovery(account.handle, n), items: Math.max(5, n) },
            {
              actor: ACTORS.instagramDiscoveryAlt,
              input: inputs.instagramDiscoveryAlt(account.handle, n),
              items: Math.max(5, n),
            },
          ]
        : [{ actor: ACTORS.facebookPosts, input: inputs.facebookPosts(account.url, n), items: n }];
  const expectEmpty = !accountHasPosts(db, account.id);
  const parse = parserFor(account.platform);

  for (let i = 0; i < attempts.length; i++) {
    const a = attempts[i];
    const res = await executeActorRun(db, {
      kind: "discovery",
      trigger,
      platform: account.platform,
      actor: a.actor,
      input: a.input,
      estimatedUsd: a.items * PRICE_PER_ITEM[account.platform] + 0.002,
    });
    if (!res.items) continue;
    const parsed = res.items.map(parse);
    const posts = parsed.filter((p): p is Extract<Parsed, { kind: "post" }> => p.kind === "post");
    const errors = parsed.filter((p) => p.kind === "error");
    const validEmpty = posts.length === 0 && errors.length === 0 && (res.items.length > 0 || expectEmpty);
    if (posts.length === 0 && !validEmpty) {
      const next = attempts[i + 1];
      finishRun(db, res.runId, {
        status: "error",
        itemsOk: 0,
        itemsFailed: Math.max(1, errors.length),
        error:
          (res.items.length === 0 ? "returned nothing" : `returned no usable posts (${errors.length} error items)`) +
          (next ? ` - trying ${next.actor}` : ""),
      });
      continue;
    }

    const observedAt = nowIso();
    let ok = 0;
    let failed = 0;
    let newPosts = 0;
    const touched: number[] = [];
    db.transaction(() => {
      parsed.forEach((p, idx) => {
        if (p.kind !== "post") return;
        const r = ingestPost(db, account, p.post, res.runId, observedAt, res.items![idx]);
        if (r.isNew) newPosts++;
        if (r.written) {
          ok++;
          touched.push(r.postId);
        } else failed++;
      });
      recordFollowersFrom(db, account, parsed, res.runId, observedAt);
    })();
    finishRun(db, res.runId, {
      status: statusFor(ok, failed),
      itemsOk: ok,
      itemsFailed: failed,
      error: validEmpty ? "no posts yet" : null,
    });
    return { ok: true, newPosts, touched };
  }
  return { ok: false, newPosts: 0, touched: [] };
}

// ---------------------------------------------------------------- follower counts

async function refreshProfiles(db: Db, trigger: Trigger, accounts: AccountRow[]): Promise<{ runs: number; ok: boolean }> {
  let runs = 0;
  let allOk = true;
  const ig = accounts.filter((a) => a.platform === "instagram");
  if (ig.length) {
    runs++;
    const res = await executeActorRun(db, {
      kind: "profiles",
      trigger,
      platform: "instagram",
      actor: ACTORS.instagramProfiles,
      input: inputs.instagramProfiles(ig.map((a) => a.handle)),
      estimatedUsd: ig.length * PRICE_PER_PROFILE + 0.002,
    });
    if (res.items) {
      const at = nowIso();
      let ok = 0;
      for (const raw of res.items) {
        const p = parseInstagramProfile(raw);
        const acc = p && ig.find((a) => sameHandle(p.handle, a.handle));
        if (p && acc && p.followers !== null) {
          insertFollowers(db, acc.id, res.runId, at, p.followers);
          ok++;
        }
      }
      finishRun(db, res.runId, { status: statusFor(ok, ig.length - ok), itemsOk: ok, itemsFailed: ig.length - ok });
    } else allOk = false;
  }
  const fb = accounts.filter((a) => a.platform === "facebook");
  if (fb.length) {
    runs++;
    const res = await executeActorRun(db, {
      kind: "profiles",
      trigger,
      platform: "facebook",
      actor: ACTORS.facebookPages,
      input: inputs.facebookPages(fb.map((a) => a.url)),
      estimatedUsd: fb.length * PRICE_PER_PROFILE + 0.002,
    });
    if (res.items) {
      const at = nowIso();
      const norm = (u: string) =>
        u
          .replace(/^https?:\/\/(www\.|m\.)?/, "")
          .replace(/[?#].*$/, "")
          .replace(/\/+$/, "")
          .toLowerCase();
      let ok = 0;
      const done = new Set<number>();
      for (const raw of res.items) {
        const p = parseFacebookPage(raw);
        if (!p) continue;
        const acc = fb.find(
          (a) => !done.has(a.id) && (p.urls.some((u) => norm(u) === norm(a.url)) || sameHandle(p.name, a.handle)),
        );
        if (acc) {
          insertFollowers(db, acc.id, res.runId, at, p.followers);
          done.add(acc.id);
          ok++;
        }
      }
      finishRun(db, res.runId, { status: statusFor(ok, fb.length - ok), itemsOk: ok, itemsFailed: fb.length - ok });
    } else allOk = false;
  }
  return { runs, ok: allOk };
}

// ---------------------------------------------------------------- refresh

function backoffKey(p: Platform) {
  return `zero_yield_backoff_${p}`;
}

function activeBackoff(db: Db, p: Platform, now: number): { level: number; until: string } | null {
  const raw = getMeta(db, backoffKey(p));
  if (!raw) return null;
  try {
    const b = JSON.parse(raw) as { level: number; until: string };
    return Date.parse(b.until) > now ? b : null;
  } catch {
    return null;
  }
}

function escalateBackoff(db: Db, p: Platform) {
  let level = 0;
  try {
    level = (JSON.parse(getMeta(db, backoffKey(p)) ?? "{}") as { level?: number }).level ?? 0;
  } catch {
    level = 0;
  }
  const next = Math.min(level + 1, BACKOFF_HOURS.length);
  const hours = BACKOFF_HOURS[next - 1];
  setMeta(db, backoffKey(p), JSON.stringify({ level: next, until: new Date(Date.now() + hours * 3600_000).toISOString() }));
  console.warn(`[backoff] ${p}: nothing came back, holding off ${hours} h (level ${next})`);
}

function clearBackoff(db: Db, p: Platform) {
  setMeta(db, backoffKey(p), null);
}

function penalise(db: Db, post: PostRow, at: string) {
  const fails = recordPostFailure(db, post.id);
  markPostRefreshed(db, post.id, at); // don't hammer it every cycle
  if (fails >= MAX_CONSECUTIVE_FAILURES) {
    deactivatePost(db, post.id);
    console.warn(`[refresh] post ${post.id} (${post.url}) marked gone after ${fails} misses`);
  }
}

/** TikTok / Instagram: one run with every due URL; stragglers are re-asked from the next actor. */
async function refreshByUrl(
  db: Db,
  trigger: Trigger,
  platform: "tiktok" | "instagram",
  posts: PostRow[],
): Promise<{ refreshed: number; failures: number; touched: number[]; runs: number }> {
  const batch = posts.slice(0, loadBudget().perRunMaxItems);
  const attempts: Array<{ actor: string; input: (urls: string[]) => unknown }> =
    platform === "tiktok"
      ? [{ actor: ACTORS.tiktokRefresh, input: inputs.tiktokRefresh }]
      : [
          { actor: ACTORS.instagramRefresh, input: inputs.instagramRefresh },
          { actor: ACTORS.instagramRefreshAlt, input: inputs.instagramRefreshAlt },
          { actor: ACTORS.instagramRefresh, input: inputs.instagramRefresh },
        ];
  const parse = parserFor(platform);
  const found = new Map<number, { post: ParsedPost; raw: unknown; runId: number; author: Parsed }>();
  let missing = batch.slice();
  let runs = 0;

  for (let i = 0; i < attempts.length && missing.length; i++) {
    const a = attempts[i];
    const urls = missing.map((p) => p.url);
    runs++;
    const res = await executeActorRun(db, {
      kind: "refresh",
      trigger,
      platform,
      actor: a.actor,
      input: a.input(urls),
      estimatedUsd: urls.length * PRICE_PER_ITEM[platform] + 0.002,
    });
    if (!res.items) continue;
    let gained = 0;
    res.items.forEach((raw) => {
      const p = parse(raw);
      if (p.kind !== "post") return;
      const target = missing.find((m) => m.platform_post_id === p.post.platformPostId || m.url === p.post.url);
      if (!target || found.has(target.id)) return;
      found.set(target.id, { post: p.post, raw, runId: res.runId, author: p });
      gained++;
    });
    missing = missing.filter((m) => !found.has(m.id));
    const next = missing.length && i < attempts.length - 1 ? attempts[i + 1] : null;
    finishRun(db, res.runId, {
      status: statusFor(gained, missing.length),
      itemsOk: gained,
      itemsFailed: missing.length,
      error: missing.length ? `${missing.length}/${urls.length} not returned` + (next ? ` - asking ${next.actor}` : "") : null,
    });
  }

  if (!found.size) {
    // Not one post came back: a platform/scraper problem, not dead posts. No
    // penalties; hold the platform off exponentially instead of billing hourly.
    escalateBackoff(db, platform);
    return { refreshed: 0, failures: batch.length, touched: [], runs };
  }
  clearBackoff(db, platform);

  const at = nowIso();
  let refreshed = 0;
  let failures = 0;
  const touched: number[] = [];
  const followersDone = new Set<number>();
  db.transaction(() => {
    for (const post of batch) {
      const f = found.get(post.id);
      if (!f) {
        penalise(db, post, at);
        failures++;
        continue;
      }
      const written = guardedInsertSnapshot(db, {
        postId: post.id,
        runId: f.runId,
        observedAt: at,
        metrics: f.post.metrics,
        raw: f.raw,
      });
      markPostRefreshed(db, post.id, at);
      if (written) {
        clearPostFailures(db, post.id);
        touched.push(post.id);
        refreshed++;
      } else failures++;
      if (!followersDone.has(post.account_id)) {
        const author = f.author.kind === "post" ? f.author.author : null;
        const acc = getAccount(db, post.account_id)!;
        if (author?.followers != null && sameHandle(author.handle, acc.handle)) {
          insertFollowers(db, acc.id, f.runId, at, author.followers);
          followersDone.add(post.account_id);
        }
      }
    }
  })();
  return { refreshed, failures, touched, runs };
}

/**
 * Refresh by re-crawling each account's profile/page, newest first, just deep
 * enough to reach its deepest due post (+10 for pinned posts and new ones).
 * Used for:
 *  - Facebook: post URLs come back without views, so a page crawl is the
 *    only way to get them.
 *  - Instagram: only the profile-reels scraper reports live counts; the
 *    by-URL scrapers return cached numbers that lag by hours (seen live
 *    2026-10-06: 374 for over an hour while the reel had 828, then 890).
 * Every post in the crawl gets a snapshot (it was paid for), new ones too.
 * Due posts deeper than the crawl cap (cadence.json crawlDepthCap) are
 * returned as `beyond`: Instagram's go to the by-URL scrapers, Facebook's
 * wait for their next slot.
 */
async function refreshByCrawl(
  db: Db,
  trigger: Trigger,
  platform: "instagram" | "facebook",
  posts: PostRow[],
): Promise<{
  refreshed: number;
  failures: number;
  touched: number[];
  runs: number;
  newPosts: number;
  beyond: PostRow[];
  seen: Set<number>;
}> {
  const cap = loadCadence().crawlDepthCap?.[platform] ?? (platform === "instagram" ? 250 : 500);
  const byAccount = new Map<number, PostRow[]>();
  for (const p of posts) byAccount.set(p.account_id, [...(byAccount.get(p.account_id) ?? []), p]);
  let refreshed = 0;
  let failures = 0;
  let runs = 0;
  let newPosts = 0;
  const touched: number[] = [];
  const beyond: PostRow[] = [];
  const seenAll = new Set<number>();
  const parse = parserFor(platform);
  let crawlsOk = 0;

  for (const [accountId, dueAll] of byAccount) {
    const account = getAccount(db, accountId);
    if (!account) continue;
    const all = listActivePosts(db, platform)
      .filter((p) => p.account_id === accountId)
      .sort((a, b) => (b.posted_at ?? b.first_seen_at).localeCompare(a.posted_at ?? a.first_seen_at));
    const rank = new Map(all.map((p, i) => [p.id, i + 1]));
    const due = dueAll.filter((p) => (rank.get(p.id) ?? Infinity) <= cap);
    beyond.push(...dueAll.filter((p) => (rank.get(p.id) ?? Infinity) > cap));
    if (!due.length) continue;
    const deepest = Math.max(...due.map((p) => rank.get(p.id)!));
    const limit = Math.min(Math.max(deepest + 10, 15), cap + 10);
    runs++;
    const res = await executeActorRun(db, {
      kind: "refresh",
      trigger,
      platform,
      actor: platform === "instagram" ? ACTORS.instagramDiscovery : ACTORS.facebookPosts,
      input:
        platform === "instagram" ? inputs.instagramDiscovery(account.handle, limit) : inputs.facebookPosts(account.url, limit),
      estimatedUsd: limit * PRICE_PER_ITEM[platform] + 0.002,
      timeoutMs: Math.min(15 * 60_000, 120_000 + limit * 1500),
    });
    if (!res.items) continue;
    const parsed = res.items.map(parse);
    // Real feed entries only (Facebook's "no_items" filler record is not one).
    const crawled = parsed.filter((p) => p.kind === "post" || (p.kind === "skip" && p.reason !== "no_items record")).length;
    if (parsed.some((p) => p.kind === "post")) crawlsOk++;
    if (!parsed.some((p) => p.kind === "post")) {
      // A crawl with no usable post says nothing about the posts: retry next cycle.
      finishRun(db, res.runId, { status: "error", itemsOk: 0, itemsFailed: due.length, error: "crawl returned no usable posts" });
      continue;
    }
    const at = nowIso();
    let ok = 0;
    let failed = 0;
    db.transaction(() => {
      const seen = new Set<number>();
      parsed.forEach((p, idx) => {
        if (p.kind !== "post") return;
        const before = getPostByPlatformId(db, platform, p.post.platformPostId);
        // Owned by another LIVE account of ours (e.g. a collab post): leave it to that account.
        // A post of a paused account (renamed handle) is taken over by this one in upsertPost.
        if (before && before.account_id !== accountId && getAccount(db, before.account_id)?.active) return;
        const r = ingestPost(db, account, p.post, res.runId, at, res.items![idx]);
        seen.add(r.postId);
        seenAll.add(r.postId);
        if (r.isNew) newPosts++;
        if (r.written) touched.push(r.postId);
      });
      recordFollowersFrom(db, account, parsed, res.runId, at);
      for (const post of due) {
        if (seen.has(post.id)) {
          if (touched.includes(post.id)) {
            ok++;
            refreshed++;
          } else {
            failed++;
            failures++;
          }
        } else if ((rank.get(post.id) ?? 0) > crawled && crawled >= limit) {
          // The crawl stopped at its limit before reaching this post (pinned posts,
          // new posts): no verdict, no penalty, next slot. A crawl that ended short
          // of its limit reached the end of the feed, so a missing post is really gone.
          markPostRefreshed(db, post.id, at);
          console.warn(
            `[refresh ${platform}] post ${post.id} at depth ${rank.get(post.id)} beyond crawl yield ${crawled}: deferred`,
          );
          failed++;
        } else {
          penalise(db, post, at);
          failed++;
          failures++;
        }
      }
    })();
    finishRun(db, res.runId, { status: statusFor(ok, failed), itemsOk: ok, itemsFailed: failed });
  }
  // Every crawl failed: hold the platform off (1 -> 12 h) instead of billing every hour.
  if (runs > 0 && crawlsOk === 0) escalateBackoff(db, platform);
  else if (crawlsOk > 0) clearBackoff(db, platform);
  return { refreshed, failures, touched, runs, newPosts, beyond, seen: seenAll };
}

// ---------------------------------------------------------------- the cycle

export async function runCycle(trigger: Trigger): Promise<CycleResult> {
  const db = getDb();
  const result: CycleResult = {
    discoveryRuns: 0,
    profileRuns: 0,
    refreshRuns: 0,
    postsRefreshed: 0,
    newPosts: 0,
    failures: 0,
    notes: [],
  };
  if (!acquireLock(db)) {
    console.warn("[cycle] another cycle is running - skipped");
    return { ...result, skippedBecauseLocked: true };
  }
  const started = Date.now();
  try {
    // Runs a restart cut off: closed here; still running on Apify -> aborted (their cost is read back below).
    for (const r of closeStaleRuns(db, new Date().toISOString())) {
      const token = tokenForLabel(r.key_label);
      if (token && r.apify_run_id) await abortRun(token, r.apify_run_id).catch(() => undefined);
    }
    syncConfigToDb(db);
    await reconcileCosts(db);

    const now = Date.now();
    const hour = localHour(now);
    const cadence = loadCadence();
    const accounts = listAccounts(db, true);
    const touched = new Set<number>();

    // 1) discovery
    for (const account of accounts) {
      const metaKey = `last_discovery_${account.id}`;
      const failKey = `discovery_fail_${account.id}`;
      const last = getMeta(db, metaKey);
      const since = last ? now - Date.parse(last) : Infinity;
      const fail = JSON.parse(getMeta(db, failKey) ?? "null") as { count: number; at: string } | null;
      // After a failure, retry 1 h, 2 h, 4 h ... (max 24 h) later - not every hour forever
      // (e.g. a mistyped handle). A slot or "Run now" always tries.
      const retryDue = !fail || now - Date.parse(fail.at) >= Math.min(2 ** (fail.count - 1), 24) * H;
      const due =
        trigger === "manual" || // "Run now" = fresh numbers for every account
        (cadence.discovery.atHours.includes(hour) && since >= 2 * H) ||
        (since === Infinity && retryDue) || // a new account: backfill right away
        (since >= 8 * H && retryDue); // missed slots (server was down): catch up
      if (!due) continue;
      result.discoveryRuns++;
      const d = await discoverAccount(db, trigger, account);
      if (d.ok) {
        setMeta(db, metaKey, nowIso());
        setMeta(db, failKey, null);
        result.newPosts += d.newPosts;
        d.touched.forEach((id) => touched.add(id));
      } else {
        setMeta(db, failKey, JSON.stringify({ count: (fail?.count ?? 0) + 1, at: nowIso() }));
        result.failures++;
        result.notes.push(`discovery ${account.platform}/${account.handle} failed`);
      }
    }

    // 2) follower counts (Instagram, Facebook; TikTok's arrive with discovery)
    {
      const last = getMeta(db, "last_profiles");
      const since = last ? now - Date.parse(last) : Infinity;
      const failedAt = getMeta(db, "last_profiles_failed");
      const due =
        (trigger === "manual" && since >= H) ||
        (cadence.profiles.atHours.includes(hour) && since >= 20 * H) ||
        since >= 26 * H || // never done, or the daily slot was missed: catch up
        (!!failedAt && now - Date.parse(failedAt) >= H); // the last attempt failed: retry hourly
      const targets = accounts.filter((a) => a.platform !== "tiktok");
      if (due && targets.length) {
        const pr = await refreshProfiles(db, trigger, targets);
        result.profileRuns += pr.runs;
        if (pr.ok) {
          setMeta(db, "last_profiles", nowIso());
          setMeta(db, "last_profiles_failed", null);
        } else {
          setMeta(db, "last_profiles_failed", nowIso());
          result.notes.push("follower counts failed - retrying in an hour");
        }
      }
    }

    // 3) refresh due posts, per platform
    const byPlatform = new Map<Platform, PostRow[]>();
    for (const p of duePosts(db, now)) {
      if (touched.has(p.id)) continue; // discovery just observed it
      byPlatform.set(p.platform, [...(byPlatform.get(p.platform) ?? []), p]);
    }
    for (const platform of PLATFORMS) {
      const posts = byPlatform.get(platform);
      if (!posts?.length) continue;
      const held = trigger === "manual" ? null : activeBackoff(db, platform, now);
      if (held) {
        result.notes.push(`${platform} refresh held (no data last time) until ${held.until}`);
        continue;
      }
      let rest = posts;
      if (platform !== "tiktok") {
        const c = await refreshByCrawl(db, trigger, platform, posts);
        result.refreshRuns += c.runs;
        result.postsRefreshed += c.refreshed;
        result.failures += c.failures;
        result.newPosts += c.newPosts;
        c.touched.forEach((id) => touched.add(id));
        rest = c.beyond.filter((p) => !c.seen.has(p.id)); // a deep post the crawl happened to cover is done
        if (platform === "facebook") {
          // Deeper than any page crawl goes: no other way to read them; next slot.
          const at = nowIso();
          for (const p of rest) markPostRefreshed(db, p.id, at);
          rest = [];
        }
      }
      if (!rest.length) continue;
      const r = await refreshByUrl(db, trigger, platform as "tiktok" | "instagram", rest);
      result.refreshRuns += r.runs;
      result.postsRefreshed += r.refreshed;
      result.failures += r.failures;
      r.touched.forEach((id) => touched.add(id));
    }

    // 4) derived numbers, surge, repair
    db.transaction(() => {
      for (const id of touched) recomputePostById(db, id);
    })();
    const promoted = applySurgeRules(db, now);
    if (promoted) result.notes.push(`${promoted} post(s) surging (checked every ${cadence.surge.promoteEveryHours} h)`);
    const swept = sweepPoisonedSnapshots(db);
    if (swept) result.notes.push(`auto-repaired ${swept} bad snapshot(s)`);

    // 5) every key's status for the Keys page (free calls; the keys are shared with other tools)
    try {
      await refreshKeyPool(db);
    } catch {
      // shown as "checked x ago" on the Keys page
    }
    return result;
  } finally {
    setMeta(
      db,
      "last_cycle",
      JSON.stringify({ at: nowIso(), trigger, seconds: Math.round((Date.now() - started) / 1000), ...result }),
    );
    releaseLock(db);
    console.log(
      `[cycle ${trigger}] discovery=${result.discoveryRuns} profiles=${result.profileRuns} refresh=${result.refreshRuns} ` +
        `posts=${result.postsRefreshed} new=${result.newPosts} failures=${result.failures}` +
        (result.notes.length ? ` | ${result.notes.join("; ")}` : ""),
    );
  }
}
