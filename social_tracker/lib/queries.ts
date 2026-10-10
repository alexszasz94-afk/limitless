import { type Platform, PLATFORMS, isPlatform, loadBudget, loadCadence } from "./config";
import { type Db, type RunRow, getDb, getMeta, monthCostUsd } from "./db";
import { addDays, dateRange, startOfLocalDay, todayLocal } from "./time";
import type { KeyPoolSummary, KeyStatus } from "./apify/keys";

/**
 * Read models for the pages. Everything reads pre-computed tables (posts'
 * latest_* columns, post_daily) - nothing is recomputed from raw snapshots
 * on a page load.
 *
 * Two kinds of numbers, labelled in the UI:
 *  - Total views = the latest count of every post, summed (what the
 *    platforms show today).
 *  - Views in a period (today, 7 days, the chart) = views GAINED in those
 *    local days, from the day-by-day deltas. A post's first observation is a
 *    baseline, so views it had before the tracker first saw it are not
 *    "gained" in any day.
 */

export type Period = "7d" | "30d" | "90d" | "all";
export const PERIODS: Period[] = ["7d", "30d", "90d", "all"];
export const PERIOD_LABEL: Record<Period, string> = { "7d": "7 days", "30d": "30 days", "90d": "90 days", all: "All time" };

export function parsePeriod(v: unknown): Period {
  return PERIODS.includes(v as Period) ? (v as Period) : "30d";
}

export interface Window {
  from: string;
  to: string;
  days: number;
  prevFrom: string | null;
  prevTo: string | null;
}

export function windowFor(db: Db, period: Period, productId: string | null): Window {
  const to = todayLocal();
  if (period === "all") {
    const first = scopeFirstDate(db, productId);
    const from = first && first < to ? first : addDays(to, -6);
    return { from, to, days: dateRange(from, to).length, prevFrom: null, prevTo: null };
  }
  const n = period === "7d" ? 7 : period === "30d" ? 30 : 90;
  const from = addDays(to, -(n - 1));
  const prevFrom = addDays(from, -n);
  // Compare only against a fully tracked previous period (a half-tracked one would show +400%).
  const first = scopeFirstDate(db, productId);
  const prevComplete = !!first && first <= prevFrom;
  return { from, to, days: n, prevFrom: prevComplete ? prevFrom : null, prevTo: prevComplete ? addDays(from, -1) : null };
}

function scopeFirstDate(db: Db, productId: string | null): string | null {
  const r = db
    .prepare(
      `SELECT MIN(pd.date) AS d FROM post_daily pd JOIN posts p ON p.id=pd.post_id JOIN accounts a ON a.id=p.account_id
       WHERE (? IS NULL OR a.product_id=?)`,
    )
    .get(productId, productId) as { d: string | null };
  return r.d;
}

// ---------------------------------------------------------------- scope helpers

export interface ProductInfo {
  id: string;
  name: string;
  avatar: string | null;
  active: boolean;
}

export function listProducts(db: Db = getDb()): ProductInfo[] {
  return (
    db.prepare(`SELECT id, name, avatar, active FROM products ORDER BY active DESC, sort_order, name`).all() as Array<{
      id: string;
      name: string;
      avatar: string | null;
      active: number;
    }>
  ).map((p) => ({ ...p, active: !!p.active }));
}

export function parseProduct(db: Db, v: unknown): string | null {
  return typeof v === "string" && listProducts(db).some((p) => p.id === v) ? v : null;
}

function viewsGained(db: Db, from: string, to: string, productId: string | null, platform: Platform | null = null): number {
  const r = db
    .prepare(
      `SELECT COALESCE(SUM(pd.views),0) AS v FROM post_daily pd
       JOIN posts p ON p.id=pd.post_id JOIN accounts a ON a.id=p.account_id
       WHERE pd.date>=? AND pd.date<=? AND (? IS NULL OR a.product_id=?) AND (? IS NULL OR p.platform=?)`,
    )
    .get(from, to, productId, productId, platform, platform) as { v: number };
  return Math.round(r.v);
}

function followersAt(db: Db, accountId: number, beforeIso: string | null): number | null {
  const r = (
    beforeIso
      ? db
          .prepare(
            `SELECT followers FROM follower_snapshots WHERE account_id=? AND observed_at<? ORDER BY observed_at DESC, id DESC LIMIT 1`,
          )
          .get(accountId, beforeIso)
      : db
          .prepare(`SELECT followers FROM follower_snapshots WHERE account_id=? ORDER BY observed_at DESC, id DESC LIMIT 1`)
          .get(accountId)
  ) as { followers: number } | undefined;
  return r ? r.followers : null;
}

/** The earliest follower count observed on/after a moment (for "change since"). */
function followersFirstAfter(db: Db, accountId: number, iso: string): number | null {
  const r = db
    .prepare(
      `SELECT followers FROM follower_snapshots WHERE account_id=? AND observed_at>=? ORDER BY observed_at ASC, id ASC LIMIT 1`,
    )
    .get(accountId, iso) as { followers: number } | undefined;
  return r ? r.followers : null;
}

// ---------------------------------------------------------------- overview

export interface AccountStat {
  id: number;
  productId: string;
  platform: Platform;
  handle: string;
  url: string;
  active: boolean;
  followers: number | null;
  followersChange: number | null;
  /** true when the first follower count is newer than the period start (change = since tracking began) */
  followersSinceStart: boolean;
  posts: number;
  periodViews: number;
  totalViews: number;
  lastChecked: string | null;
}

export interface ProductStat extends ProductInfo {
  totalViews: number;
  periodViews: number;
  prevPeriodViews: number | null;
  posts: number;
  postsInPeriod: number;
  followers: number | null;
  followersChange: number | null;
  accounts: AccountStat[];
}

export interface DayPoint {
  date: string;
  values: Record<Platform, number>;
}

export interface TopPost {
  id: number;
  platform: Platform;
  handle: string;
  productName: string;
  url: string;
  caption: string | null;
  /** When it went live (first seen when the platform gives no date). */
  postedAt: string;
  views: number | null;
  periodViews: number;
  views24h: number | null;
}

export interface Overview {
  window: Window;
  totals: {
    totalViews: number;
    periodViews: number;
    prevPeriodViews: number | null;
    today: number;
    yesterday: number;
    posts: number;
    postsInPeriod: number;
    followers: number | null;
    followersChange: number | null;
    followersSinceStart: boolean;
    accounts: number;
  };
  series: DayPoint[];
  products: ProductStat[];
  /** Most views gained in the period. */
  topPosts: TopPost[];
  /** Most views 24 h after going live, among the videos posted in the period (fair across ages). */
  bestStarts: TopPost[];
}

export function overview(productId: string | null, period: Period): Overview {
  const db = getDb();
  const w = windowFor(db, period, productId);
  const today = todayLocal();
  const windowStartIso = new Date(startOfLocalDay(w.from)).toISOString();

  const accounts = db
    .prepare(
      `SELECT a.id, a.product_id, a.platform, a.handle, a.url, a.active,
         (SELECT COUNT(*) FROM posts p WHERE p.account_id=a.id) AS posts,
         (SELECT COALESCE(SUM(p.latest_views),0) FROM posts p WHERE p.account_id=a.id) AS total_views,
         (SELECT COALESCE(SUM(pd.views),0) FROM post_daily pd JOIN posts p ON p.id=pd.post_id
            WHERE p.account_id=a.id AND pd.date>=? AND pd.date<=?) AS period_views,
         (SELECT value FROM meta m WHERE m.key='last_discovery_' || a.id) AS last_checked
       FROM accounts a JOIN products pr ON pr.id=a.product_id
       WHERE (? IS NULL OR a.product_id=?) AND (a.active=1 OR EXISTS (SELECT 1 FROM posts p WHERE p.account_id=a.id))
       ORDER BY pr.sort_order, a.id`,
    )
    .all(w.from, w.to, productId, productId) as Array<{
    id: number;
    product_id: string;
    platform: Platform;
    handle: string;
    url: string;
    active: number;
    posts: number;
    total_views: number;
    period_views: number;
    last_checked: string | null;
  }>;

  const accountStats: AccountStat[] = accounts
    .map((a) => {
      const followers = followersAt(db, a.id, null);
      const before = followersAt(db, a.id, windowStartIso);
      const base = before ?? followersFirstAfter(db, a.id, windowStartIso);
      return {
        followersSinceStart: before === null && base !== null,
        id: a.id,
        productId: a.product_id,
        platform: a.platform,
        handle: a.handle,
        url: a.url,
        active: !!a.active,
        followers,
        followersChange: followers !== null && base !== null ? followers - base : null,
        posts: a.posts,
        periodViews: Math.round(a.period_views),
        totalViews: a.total_views,
        lastChecked: a.last_checked,
      };
    })
    .sort((x, y) => PLATFORMS.indexOf(x.platform) - PLATFORMS.indexOf(y.platform));

  const windowEndIso = new Date(startOfLocalDay(addDays(w.to, 1))).toISOString();
  const postsInPeriodBy = new Map<string, number>();
  for (const r of db
    .prepare(
      `SELECT a.product_id AS pid, COUNT(*) AS n FROM posts p JOIN accounts a ON a.id=p.account_id
       WHERE (? IS NULL OR a.product_id=?) AND COALESCE(p.posted_at, p.first_seen_at)>=? AND COALESCE(p.posted_at, p.first_seen_at)<?
       GROUP BY a.product_id`,
    )
    .all(productId, productId, windowStartIso, windowEndIso) as Array<{ pid: string; n: number }>)
    postsInPeriodBy.set(r.pid, r.n);

  const sumNullable = (vals: Array<number | null>) =>
    vals.some((v) => v !== null) ? vals.reduce<number>((s, v) => s + (v ?? 0), 0) : null;

  const products: ProductStat[] = listProducts(db)
    .filter((p) => (productId ? p.id === productId : p.active || accountStats.some((a) => a.productId === p.id)))
    .map((p) => {
      const accs = accountStats.filter((a) => a.productId === p.id);
      return {
        ...p,
        accounts: accs,
        totalViews: accs.reduce((s, a) => s + a.totalViews, 0),
        periodViews: accs.reduce((s, a) => s + a.periodViews, 0),
        prevPeriodViews: w.prevFrom && w.prevTo ? viewsGained(db, w.prevFrom, w.prevTo, p.id) : null,
        posts: accs.reduce((s, a) => s + a.posts, 0),
        postsInPeriod: postsInPeriodBy.get(p.id) ?? 0,
        // Followers: live accounts only (a paused or renamed account's last count is history).
        followers: sumNullable(accs.filter((a) => a.active).map((a) => a.followers)),
        followersChange: sumNullable(accs.filter((a) => a.active).map((a) => a.followersChange)),
      };
    });

  // chart: views gained per local day per platform
  const rows = db
    .prepare(
      `SELECT pd.date, p.platform, SUM(pd.views) AS v
       FROM post_daily pd JOIN posts p ON p.id=pd.post_id JOIN accounts a ON a.id=p.account_id
       WHERE pd.date>=? AND pd.date<=? AND (? IS NULL OR a.product_id=?)
       GROUP BY pd.date, p.platform`,
    )
    .all(w.from, w.to, productId, productId) as Array<{ date: string; platform: Platform; v: number }>;
  const byDate = new Map<string, DayPoint>();
  for (const d of dateRange(w.from, w.to)) {
    byDate.set(d, { date: d, values: { instagram: 0, tiktok: 0, facebook: 0 } });
  }
  for (const r of rows) {
    const pt = byDate.get(r.date);
    if (!pt || !isPlatform(r.platform)) continue;
    pt.values[r.platform] += Math.round(r.v);
  }

  // Rankings: every post is one video on one platform.
  const ranked = (extraWhere: string, order: string, extraParams: unknown[]): TopPost[] =>
    (
      db
        .prepare(
          `SELECT p.id, p.platform, a.handle, pr.name AS product_name, p.url, p.caption,
           COALESCE(p.posted_at, p.first_seen_at) AS live_at, p.latest_views, p.views_24h,
           (SELECT COALESCE(SUM(pd.views),0) FROM post_daily pd WHERE pd.post_id=p.id AND pd.date>=? AND pd.date<=?) AS period_views
         FROM posts p JOIN accounts a ON a.id=p.account_id JOIN products pr ON pr.id=a.product_id
         WHERE (? IS NULL OR a.product_id=?) ${extraWhere}
         ORDER BY ${order}, p.id DESC LIMIT 5`,
        )
        .all(w.from, w.to, productId, productId, ...extraParams) as Array<{
        id: number;
        platform: Platform;
        handle: string;
        product_name: string;
        url: string;
        caption: string | null;
        live_at: string;
        latest_views: number | null;
        views_24h: number | null;
        period_views: number;
      }>
    ).map((r) => ({
      id: r.id,
      platform: r.platform,
      handle: r.handle,
      productName: r.product_name,
      url: r.url,
      caption: r.caption,
      postedAt: r.live_at,
      views: r.latest_views,
      periodViews: Math.round(r.period_views),
      views24h: r.views_24h,
    }));
  const topPosts = ranked("", "period_views DESC, p.latest_views DESC", []);
  const bestStarts =
    period === "all"
      ? ranked("AND p.views_24h IS NOT NULL", "p.views_24h DESC, p.latest_views DESC", [])
      : ranked(
          "AND p.views_24h IS NOT NULL AND COALESCE(p.posted_at, p.first_seen_at)>=? AND COALESCE(p.posted_at, p.first_seen_at)<?",
          "p.views_24h DESC, p.latest_views DESC",
          [windowStartIso, windowEndIso],
        );

  const liveAccounts = accountStats.filter((a) => a.active);
  const followersAll = sumNullable(liveAccounts.map((a) => a.followers));
  return {
    window: w,
    totals: {
      totalViews: accountStats.reduce((s, a) => s + a.totalViews, 0),
      periodViews: accountStats.reduce((s, a) => s + a.periodViews, 0),
      prevPeriodViews: w.prevFrom && w.prevTo ? viewsGained(db, w.prevFrom, w.prevTo, productId) : null,
      today: viewsGained(db, today, today, productId),
      yesterday: viewsGained(db, addDays(today, -1), addDays(today, -1), productId),
      posts: accountStats.reduce((s, a) => s + a.posts, 0),
      postsInPeriod: [...postsInPeriodBy.values()].reduce((s, n) => s + n, 0),
      followers: followersAll,
      followersChange: sumNullable(liveAccounts.map((a) => a.followersChange)),
      followersSinceStart: liveAccounts.some((a) => a.followersSinceStart),
      accounts: accountStats.filter((a) => a.active).length,
    },
    series: [...byDate.values()],
    products,
    topPosts,
    bestStarts,
  };
}

// ---------------------------------------------------------------- posts

export type PostSort = "views" | "period" | "v24" | "v7d" | "newest" | "er";
export const POST_SORTS: Array<{ id: PostSort; label: string }> = [
  { id: "period", label: "Views in period" },
  { id: "views", label: "Total views" },
  { id: "v24", label: "Views after 24 h" },
  { id: "v7d", label: "Views after 7 days" },
  { id: "er", label: "Engagement rate" },
  { id: "newest", label: "Newest" },
];

export interface PostRowView {
  id: number;
  productId: string;
  productName: string;
  platform: Platform;
  handle: string;
  url: string;
  caption: string | null;
  postedAt: string | null;
  firstSeenAt: string;
  active: boolean;
  views: number | null;
  likes: number | null;
  comments: number | null;
  shares: number | null;
  saves: number | null;
  latestAt: string | null;
  views24h: number | null;
  views7d: number | null;
  periodViews: number;
  engagement: number | null;
}

export interface PostsQuery {
  productId: string | null;
  platform: Platform | null;
  sort: PostSort;
  period: Period;
  page: number;
}

export const PAGE_SIZE = 50;

export function posts(q: PostsQuery): { rows: PostRowView[]; total: number; window: Window } {
  const db = getDb();
  const w = windowFor(db, q.period, q.productId);
  const order: Record<PostSort, string> = {
    views: "p.latest_views IS NULL, p.latest_views DESC",
    period: "period_views DESC, p.latest_views DESC",
    v24: "p.views_24h IS NULL, p.views_24h DESC",
    v7d: "p.views_7d IS NULL, p.views_7d DESC",
    newest: "COALESCE(p.posted_at, p.first_seen_at) DESC",
    er: "engagement IS NULL, engagement DESC",
  };
  const clauses: string[] = [];
  const params: unknown[] = [];
  if (q.productId) {
    clauses.push("a.product_id=?");
    params.push(q.productId);
  }
  if (q.platform) {
    clauses.push("p.platform=?");
    params.push(q.platform);
  }
  const where = clauses.length ? `WHERE ${clauses.join(" AND ")}` : "";
  const total = (
    db.prepare(`SELECT COUNT(*) AS n FROM posts p JOIN accounts a ON a.id=p.account_id ${where}`).get(...params) as { n: number }
  ).n;
  const rows = db
    .prepare(
      `SELECT p.*, a.product_id, a.handle, pr.name AS product_name,
         (SELECT COALESCE(SUM(pd.views),0) FROM post_daily pd WHERE pd.post_id=p.id AND pd.date>=? AND pd.date<=?) AS period_views,
         CASE WHEN p.latest_views > 0 THEN
           (COALESCE(p.latest_likes,0)+COALESCE(p.latest_comments,0)+COALESCE(p.latest_shares,0)+COALESCE(p.latest_saves,0))*1.0/p.latest_views
         END AS engagement
       FROM posts p JOIN accounts a ON a.id=p.account_id JOIN products pr ON pr.id=a.product_id
       ${where}
       ORDER BY ${order[q.sort]}, p.id DESC
       LIMIT ? OFFSET ?`,
    )
    .all(w.from, w.to, ...params, PAGE_SIZE, (q.page - 1) * PAGE_SIZE) as Array<Record<string, unknown>>;
  return {
    total,
    window: w,
    rows: rows.map((r) => ({
      id: r.id as number,
      productId: r.product_id as string,
      productName: r.product_name as string,
      platform: r.platform as Platform,
      handle: r.handle as string,
      url: r.url as string,
      caption: (r.caption as string | null) ?? null,
      postedAt: (r.posted_at as string | null) ?? null,
      firstSeenAt: r.first_seen_at as string,
      active: !!r.active,
      views: r.latest_views as number | null,
      likes: r.latest_likes as number | null,
      comments: r.latest_comments as number | null,
      shares: r.latest_shares as number | null,
      saves: r.latest_saves as number | null,
      latestAt: r.latest_at as string | null,
      views24h: r.views_24h as number | null,
      views7d: r.views_7d as number | null,
      periodViews: Math.round(r.period_views as number),
      engagement: (r.engagement as number | null) ?? null,
    })),
  };
}

// ---------------------------------------------------------------- runs & health

export interface HealthItem {
  level: "alert" | "info";
  text: string;
}

export function health(dbIn?: Db): { ok: boolean; items: HealthItem[] } {
  const db = dbIn ?? getDb();
  const now = Date.now();
  const H = 3600_000;
  const items: HealthItem[] = [];
  const alert = (text: string) => items.push({ level: "alert", text });
  const info = (text: string) => items.push({ level: "info", text });

  const hb = getMeta(db, "scheduler_heartbeat");
  if (!hb || now - Date.parse(hb) > 5 * 60_000) alert("The scraper process is not running (no heartbeat in 5 min).");

  const activeAccounts = (db.prepare(`SELECT COUNT(*) AS n FROM accounts WHERE active=1`).get() as { n: number }).n;
  if (activeAccounts > 0) {
    const last = db.prepare(`SELECT started_at FROM scrape_runs ORDER BY id DESC LIMIT 1`).get() as
      { started_at: string } | undefined;
    if (!last || now - Date.parse(last.started_at) > 8 * H) alert("No scrape attempted in the last 8 hours.");
    const lastOk = db
      .prepare(
        `SELECT finished_at FROM scrape_runs WHERE status IN ('ok','partial') AND finished_at IS NOT NULL ORDER BY id DESC LIMIT 1`,
      )
      .get() as { finished_at: string } | undefined;
    if (last && (!lastOk || now - Date.parse(lastOk.finished_at) > 24 * H)) alert("No successful scrape in the last 24 hours.");
  }

  const dayAgo = new Date(now - 24 * H).toISOString();
  const counts: Record<string, number> = {};
  for (const r of db
    .prepare(`SELECT status, COUNT(*) AS n FROM scrape_runs WHERE started_at>=? GROUP BY status`)
    .all(dayAgo) as Array<{
    status: string;
    n: number;
  }>)
    counts[r.status] = r.n;
  const errors = counts.error ?? 0;
  const oks = (counts.ok ?? 0) + (counts.partial ?? 0);
  if (errors > 0 && errors >= oks) alert(`High error rate: ${errors} failed vs ${oks} good runs in 24 h.`);
  else if (errors > 0) info(`${errors} failed run${errors === 1 ? "" : "s"} in 24 h (retried or covered by a fallback).`);
  if (counts.budget_stop) alert(`Monthly budget reached: ${counts.budget_stop} run(s) skipped in 24 h.`);

  for (const p of PLATFORMS) {
    const raw = getMeta(db, `zero_yield_backoff_${p}`);
    if (!raw) continue;
    try {
      const b = JSON.parse(raw) as { level: number; until: string };
      if (Date.parse(b.until) > now)
        alert(`${p} refresh is paused after returning nothing (retry after ${b.until.slice(11, 16)} UTC).`);
    } catch {
      // ignore
    }
  }

  for (const r of db
    .prepare(
      `SELECT p.platform, MAX(p.latest_at) AS last FROM posts p JOIN accounts a ON a.id=p.account_id
       WHERE p.active=1 AND a.active=1 GROUP BY p.platform`,
    )
    .all() as Array<{ platform: string; last: string | null }>) {
    if (!r.last || now - Date.parse(r.last) > 26 * H) alert(`${r.platform}: no new numbers for over 26 hours.`);
  }

  const an: Record<string, number> = {};
  for (const r of db.prepare(`SELECT kind, COUNT(*) AS n FROM anomalies WHERE created_at>=? GROUP BY kind`).all(dayAgo) as Array<{
    kind: string;
    n: number;
  }>)
    an[r.kind] = r.n;
  if (an.rejected_drop) info(`${an.rejected_drop} implausible view drop(s) refused in 24 h (a scraper may be glitching).`);
  if (an.swept) info(`${an.swept} bad snapshot(s) auto-repaired in 24 h.`);
  if (an.accepted_drop) info(`${an.accepted_drop} view drop(s) accepted as real after 24 h of confirmation.`);

  const failing = (
    db.prepare(`SELECT COUNT(*) AS n FROM posts WHERE consecutive_failures>=1 AND active=1`).get() as { n: number }
  ).n;
  if (failing) info(`${failing} post(s) missed their last refresh (marked gone after 2 misses).`);

  const budget = loadBudget().monthlyBudgetUsd;
  const spent = monthCostUsd(db, new Date().toISOString().slice(0, 7));
  if (budget > 0 && spent >= 0.9 * budget)
    alert(`This month's spend $${spent.toFixed(2)} is at ${Math.round((spent / budget) * 100)}% of the $${budget} budget.`);

  const pool = getMeta(db, "key_pool");
  if (pool) {
    const p = JSON.parse(pool) as { ok: number; total: number; notReached?: number };
    if (p.total > 0 && p.ok === 0) alert("No Apify key has credit left this month.");
    if (p.notReached) info(`${p.notReached} Apify key(s) did not answer at the last key check (network) - Check now on the Keys page retries.`);
  } else if (activeAccounts > 0 && hb) info("Apify keys not checked yet.");

  return { ok: !items.some((i) => i.level === "alert"), items };
}

export interface RunsPage {
  runs: RunRow[];
  monthSpend: number;
  lastMonthSpend: number;
  budget: number;
  keyPool: {
    checkedAt: string;
    total: number;
    ok: number;
    overCap: number;
    invalid: number;
    notReached?: number;
    usedUsd: number;
    capUsd: number;
    leftUsd?: number;
  } | null;
  health: { ok: boolean; items: HealthItem[] };
  lastCycle: { at: string; trigger: string; seconds: number; notes?: string[] } | null;
  heartbeat: string | null;
  runningSince: string | null;
  requestedAt: string | null;
  schedule: { discovery: number[]; profiles: number[]; anchor: number; timezone: string };
  postsTracked: number;
  snapshots: number;
}

export function runsPage(limit = 150): RunsPage {
  const db = getDb();
  const month = new Date().toISOString().slice(0, 7);
  const d = new Date();
  const lastMonth = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() - 1, 1)).toISOString().slice(0, 7);
  const cad = loadCadence();
  const lock = getMeta(db, "cycle_lock");
  const lc = getMeta(db, "last_cycle");
  const kp = getMeta(db, "key_pool");
  return {
    runs: db.prepare(`SELECT * FROM scrape_runs ORDER BY id DESC LIMIT ?`).all(limit) as RunRow[],
    monthSpend: monthCostUsd(db, month),
    lastMonthSpend: monthCostUsd(db, lastMonth),
    budget: loadBudget().monthlyBudgetUsd,
    keyPool: kp ? JSON.parse(kp) : null,
    health: health(db),
    lastCycle: lc ? JSON.parse(lc) : null,
    heartbeat: getMeta(db, "scheduler_heartbeat"),
    runningSince: lock ? (JSON.parse(lock) as { since: string }).since : null,
    requestedAt: getMeta(db, "run_requested_at"),
    schedule: {
      discovery: cad.discovery.atHours,
      profiles: cad.profiles.atHours,
      anchor: cad.anchorHourLocal,
      timezone: cad.timezone,
    },
    postsTracked: (db.prepare(`SELECT COUNT(*) AS n FROM posts`).get() as { n: number }).n,
    snapshots: (db.prepare(`SELECT COUNT(*) AS n FROM snapshots`).get() as { n: number }).n,
  };
}

/** For the header: when numbers last moved, and whether a cycle is running. */
export function freshness(): { lastSuccess: string | null; running: boolean; ok: boolean } {
  const db = getDb();
  const r = db.prepare(`SELECT MAX(finished_at) AS t FROM scrape_runs WHERE status IN ('ok','partial')`).get() as {
    t: string | null;
  };
  return { lastSuccess: r.t, running: !!getMeta(db, "cycle_lock"), ok: health(db).ok };
}

// ---------------------------------------------------------------- Apify keys

export interface KeysPage {
  summary: KeyPoolSummary | null;
  keys: KeyStatus[];
  trackerMonthSpend: number;
  resets: Array<{ date: string; keys: number; freedUsd: number }>;
}

/** The Keys page: every key's credit, spend and reset date (as last checked). */
export function keysPage(): KeysPage {
  const db = getDb();
  const s = getMeta(db, "key_pool");
  const k = getMeta(db, "key_pool_keys");
  const keys = k ? (JSON.parse(k) as KeyStatus[]) : [];
  // Each key resets on its own day: group the coming resets and what they give back.
  const byDate = new Map<string, { keys: number; freedUsd: number }>();
  for (const key of keys) {
    if (!key.cycleEnd || key.usedUsd === null) continue;
    const resetAt = Date.parse(key.cycleEnd) + 1; // endAt is the last millisecond of the cycle
    if (resetAt < Date.now()) continue;
    const date = new Date(resetAt).toISOString().slice(0, 10);
    const cur = byDate.get(date) ?? { keys: 0, freedUsd: 0 };
    cur.keys++;
    cur.freedUsd += key.capUsd === null ? key.usedUsd : Math.min(key.usedUsd, key.capUsd); // a reset gives back at most the cap
    byDate.set(date, cur);
  }
  return {
    summary: s ? (JSON.parse(s) as KeyPoolSummary) : null,
    keys,
    trackerMonthSpend: monthCostUsd(db, new Date().toISOString().slice(0, 7)),
    resets: [...byDate.entries()]
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([date, v]) => ({ date, keys: v.keys, freedUsd: Math.round(v.freedUsd * 100) / 100 })),
  };
}
