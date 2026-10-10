import Database from "better-sqlite3";
import fs from "node:fs";
import path from "node:path";
import zlib from "node:zlib";
import type { Platform } from "./config";

/**
 * SQLite store. Raw snapshots are the source of truth: every derived number
 * (daily views, latest values, views 24 h / 7 d after posting) can be rebuilt
 * from them at any time. Two processes use this file (the web app and the
 * scraper), so it runs in WAL mode with a busy timeout.
 */

export const SCHEMA_VERSION = 3;

const SCHEMA_V1 = `
CREATE TABLE IF NOT EXISTS products (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  active INTEGER NOT NULL DEFAULT 1,
  avatar TEXT,
  sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS accounts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id TEXT NOT NULL REFERENCES products(id),
  platform TEXT NOT NULL CHECK (platform IN ('instagram','tiktok','facebook')),
  handle TEXT NOT NULL,
  url TEXT NOT NULL,
  active INTEGER NOT NULL DEFAULT 1,
  added_at TEXT NOT NULL,
  UNIQUE (platform, handle COLLATE NOCASE)
);
CREATE INDEX IF NOT EXISTS idx_accounts_product ON accounts(product_id);

CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_id INTEGER NOT NULL REFERENCES accounts(id),
  platform TEXT NOT NULL,
  platform_post_id TEXT NOT NULL,
  url TEXT NOT NULL,
  caption TEXT,
  posted_at TEXT,
  first_seen_at TEXT NOT NULL,
  last_refreshed_at TEXT,
  surge_until TEXT,
  active INTEGER NOT NULL DEFAULT 1,
  consecutive_failures INTEGER NOT NULL DEFAULT 0,
  latest_views INTEGER,
  latest_likes INTEGER,
  latest_comments INTEGER,
  latest_shares INTEGER,
  latest_saves INTEGER,
  latest_at TEXT,
  views_24h INTEGER,
  views_7d INTEGER,
  UNIQUE (platform, platform_post_id)
);
CREATE INDEX IF NOT EXISTS idx_posts_account ON posts(account_id);

-- Never derived. NULL metric = the platform does not expose it. A failed
-- scrape writes NO row: zeros from failures must never enter history.
-- raw_gz = the scraper's item, slimmed to its scalar fields and gzipped.
CREATE TABLE IF NOT EXISTS snapshots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  post_id INTEGER NOT NULL REFERENCES posts(id),
  run_id INTEGER,
  observed_at TEXT NOT NULL,
  views INTEGER,
  likes INTEGER,
  comments INTEGER,
  shares INTEGER,
  saves INTEGER,
  raw_gz BLOB
);
CREATE INDEX IF NOT EXISTS idx_snapshots_post ON snapshots(post_id, observed_at);
CREATE INDEX IF NOT EXISTS idx_snapshots_observed ON snapshots(observed_at);

CREATE TABLE IF NOT EXISTS follower_snapshots (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  account_id INTEGER NOT NULL REFERENCES accounts(id),
  run_id INTEGER,
  observed_at TEXT NOT NULL,
  followers INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_followers_account ON follower_snapshots(account_id, observed_at);

-- Daily deltas per post, in local days. quality 'observed' = the snapshot
-- pair spanned <= 36 h; 'spread' = a longer gap spread over the days it
-- covers. Negative values are real platform revisions and are kept. The
-- first snapshot of a post is a baseline and produces no row.
CREATE TABLE IF NOT EXISTS post_daily (
  post_id INTEGER NOT NULL REFERENCES posts(id),
  date TEXT NOT NULL,
  views REAL NOT NULL DEFAULT 0,
  likes REAL,
  comments REAL,
  shares REAL,
  saves REAL,
  quality TEXT NOT NULL CHECK (quality IN ('observed','spread')),
  PRIMARY KEY (post_id, date)
);
CREATE INDEX IF NOT EXISTS idx_post_daily_date ON post_daily(date);

CREATE TABLE IF NOT EXISTS scrape_runs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  kind TEXT NOT NULL,            -- discovery | refresh | profiles
  trigger_source TEXT NOT NULL,  -- schedule | manual
  platform TEXT,
  actor TEXT,
  key_label TEXT,
  apify_run_id TEXT,
  input_json TEXT,
  items_ok INTEGER NOT NULL DEFAULT 0,
  items_failed INTEGER NOT NULL DEFAULT 0,
  cost_usd REAL NOT NULL DEFAULT 0,
  cost_final INTEGER NOT NULL DEFAULT 0,
  status TEXT NOT NULL,          -- running | ok | partial | error | budget_stop
  error TEXT
);
CREATE INDEX IF NOT EXISTS idx_runs_started ON scrape_runs(started_at);

CREATE TABLE IF NOT EXISTS anomalies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  post_id INTEGER NOT NULL,
  run_id INTEGER,
  kind TEXT NOT NULL,            -- rejected_drop | accepted_drop | swept
  detail TEXT,
  created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_anomalies_post ON anomalies(post_id, kind);
CREATE INDEX IF NOT EXISTS idx_anomalies_created ON anomalies(created_at);

CREATE TABLE IF NOT EXISTS meta (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
`;

/**
 * v2 (2026-10-06) matched posts to Distribution videos by caption: a caption
 * history table and posts.video_id / video_match. v3 (2026-10-08) dropped the
 * matching - captions repeat and change across platforms, so every post is
 * tracked as its own video - and removes the table and both columns.
 * Idempotent.
 */
function dropVideoMatching(db: Db): void {
  db.exec(`DROP INDEX IF EXISTS idx_posts_video; DROP TABLE IF EXISTS video_captions;`);
  const cols = new Set((db.pragma("table_info(posts)") as Array<{ name: string }>).map((c) => c.name));
  for (const c of ["video_id", "video_match"]) if (cols.has(c)) db.exec(`ALTER TABLE posts DROP COLUMN ${c}`);
}

/**
 * Bring the file up to SCHEMA_VERSION in one write transaction: the web app
 * and the scraper may open it at the same moment, and the second one waits,
 * then finds the work done.
 */
function migrate(db: Db): void {
  db.transaction(() => {
    const version = db.pragma("user_version", { simple: true }) as number;
    if (version >= SCHEMA_VERSION) return;
    if (version < 1) db.exec(SCHEMA_V1);
    if (version < 3) dropVideoMatching(db);
    db.pragma(`user_version = ${SCHEMA_VERSION}`);
  }).immediate();
}

export type Db = Database.Database;

export function dataDir(): string {
  return process.env.DATA_DIR || path.join(/*turbopackIgnore: true*/ process.cwd(), "data");
}

/** Open (and migrate) a tracker database file. The app uses getDb(). */
export function openDb(file: string): Db {
  fs.mkdirSync(/*turbopackIgnore: true*/ path.dirname(file), { recursive: true });
  const db = new Database(file);
  db.pragma("journal_mode = WAL");
  db.pragma("synchronous = NORMAL");
  db.pragma("foreign_keys = ON");
  db.pragma("busy_timeout = 10000");
  if ((db.pragma("user_version", { simple: true }) as number) < SCHEMA_VERSION) migrate(db);
  return db;
}

const g = globalThis as unknown as { __trackerDb?: Db };

/** One connection per process (kept across Next.js dev reloads). */
export function getDb(): Db {
  if (!g.__trackerDb) g.__trackerDb = openDb(path.join(dataDir(), "tracker.db"));
  return g.__trackerDb;
}

// ---------------------------------------------------------------- rows

export interface ProductRow {
  id: string;
  name: string;
  active: number;
  avatar: string | null;
  sort_order: number;
}

export interface AccountRow {
  id: number;
  product_id: string;
  platform: Platform;
  handle: string;
  url: string;
  active: number;
  added_at: string;
}

export interface PostRow {
  id: number;
  account_id: number;
  platform: Platform;
  platform_post_id: string;
  url: string;
  caption: string | null;
  posted_at: string | null;
  first_seen_at: string;
  last_refreshed_at: string | null;
  surge_until: string | null;
  active: number;
  consecutive_failures: number;
  latest_views: number | null;
  latest_likes: number | null;
  latest_comments: number | null;
  latest_shares: number | null;
  latest_saves: number | null;
  latest_at: string | null;
  views_24h: number | null;
  views_7d: number | null;
}

export interface Metrics {
  views: number | null;
  likes: number | null;
  comments: number | null;
  shares: number | null;
  saves: number | null;
}

export interface SnapshotRow extends Metrics {
  id: number;
  post_id: number;
  run_id: number | null;
  observed_at: string;
}

export interface DailyRow {
  post_id: number;
  date: string;
  views: number;
  likes: number | null;
  comments: number | null;
  shares: number | null;
  saves: number | null;
  quality: "observed" | "spread";
}

export interface RunRow {
  id: number;
  started_at: string;
  finished_at: string | null;
  kind: string;
  trigger_source: string;
  platform: string | null;
  actor: string | null;
  key_label: string | null;
  apify_run_id: string | null;
  input_json: string | null;
  items_ok: number;
  items_failed: number;
  cost_usd: number;
  cost_final: number;
  status: string;
  error: string | null;
}

export const nowIso = () => new Date().toISOString();

// ---------------------------------------------------------------- meta

export function getMeta(db: Db, key: string): string | null {
  const r = db.prepare(`SELECT value FROM meta WHERE key=?`).get(key) as { value: string } | undefined;
  return r && r.value !== "" ? r.value : null;
}

export function setMeta(db: Db, key: string, value: string | null): void {
  if (value === null) db.prepare(`DELETE FROM meta WHERE key=?`).run(key);
  else
    db.prepare(`INSERT INTO meta (key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value`).run(key, value);
}

// ---------------------------------------------------------------- products & accounts

export function upsertProduct(db: Db, p: { id: string; name: string; active: boolean; avatar: string | null; sort: number }) {
  db.prepare(
    `INSERT INTO products (id, name, active, avatar, sort_order) VALUES (?, ?, ?, ?, ?)
     ON CONFLICT(id) DO UPDATE SET name=excluded.name, active=excluded.active, avatar=excluded.avatar, sort_order=excluded.sort_order`,
  ).run(p.id, p.name, p.active ? 1 : 0, p.avatar, p.sort);
}

export function upsertAccount(
  db: Db,
  a: { productId: string; platform: Platform; handle: string; url: string; active: boolean },
): number {
  const existing = db
    .prepare(`SELECT id FROM accounts WHERE platform=? AND handle=? COLLATE NOCASE`)
    .get(a.platform, a.handle) as { id: number } | undefined;
  if (existing) {
    db.prepare(`UPDATE accounts SET product_id=?, handle=?, url=?, active=? WHERE id=?`).run(
      a.productId,
      a.handle,
      a.url,
      a.active ? 1 : 0,
      existing.id,
    );
    return existing.id;
  }
  const r = db
    .prepare(`INSERT INTO accounts (product_id, platform, handle, url, active, added_at) VALUES (?, ?, ?, ?, ?, ?)`)
    .run(a.productId, a.platform, a.handle, a.url, a.active ? 1 : 0, nowIso());
  return Number(r.lastInsertRowid);
}

export function listAccounts(db: Db, activeOnly = false): AccountRow[] {
  return db
    .prepare(`SELECT * FROM accounts ${activeOnly ? "WHERE active=1" : ""} ORDER BY product_id, platform, id`)
    .all() as AccountRow[];
}

export function getAccount(db: Db, id: number): AccountRow | undefined {
  return db.prepare(`SELECT * FROM accounts WHERE id=?`).get(id) as AccountRow | undefined;
}

// ---------------------------------------------------------------- posts

export function getPostByPlatformId(db: Db, platform: Platform, platformPostId: string): PostRow | undefined {
  return db.prepare(`SELECT * FROM posts WHERE platform=? AND platform_post_id=?`).get(platform, platformPostId) as
    PostRow | undefined;
}

export function upsertPost(
  db: Db,
  p: {
    accountId: number;
    platform: Platform;
    platformPostId: string;
    url: string;
    caption: string | null;
    postedAt: string | null;
    seenAt: string;
  },
): { id: number; isNew: boolean } {
  const existing = getPostByPlatformId(db, p.platform, p.platformPostId);
  if (existing) {
    // A post whose owning account is paused (e.g. its handle was renamed in
    // products.json, which creates a new account row) moves to the account
    // that sees it now, so its history keeps being refreshed and counted.
    db.prepare(
      `UPDATE posts SET url=?, caption=COALESCE(?, caption), posted_at=COALESCE(posted_at, ?),
         account_id=CASE WHEN account_id<>? AND (SELECT active FROM accounts WHERE id=posts.account_id)=0 THEN ? ELSE account_id END
       WHERE id=?`,
    ).run(p.url, p.caption, p.postedAt, p.accountId, p.accountId, existing.id);
    return { id: existing.id, isNew: false };
  }
  const r = db
    .prepare(
      `INSERT INTO posts (account_id, platform, platform_post_id, url, caption, posted_at, first_seen_at)
       VALUES (?, ?, ?, ?, ?, ?, ?)`,
    )
    .run(p.accountId, p.platform, p.platformPostId, p.url, p.caption, p.postedAt, p.seenAt);
  return { id: Number(r.lastInsertRowid), isNew: true };
}

export function listActivePosts(db: Db, platform?: Platform): PostRow[] {
  return (
    platform
      ? db
          .prepare(
            `SELECT p.* FROM posts p JOIN accounts a ON a.id=p.account_id WHERE p.active=1 AND a.active=1 AND p.platform=?`,
          )
          .all(platform)
      : db.prepare(`SELECT p.* FROM posts p JOIN accounts a ON a.id=p.account_id WHERE p.active=1 AND a.active=1`).all()
  ) as PostRow[];
}

export function accountHasPosts(db: Db, accountId: number): boolean {
  return !!db.prepare(`SELECT 1 FROM posts WHERE account_id=? LIMIT 1`).get(accountId);
}

export function markPostRefreshed(db: Db, postId: number, at: string) {
  db.prepare(`UPDATE posts SET last_refreshed_at=? WHERE id=?`).run(at, postId);
}

export function clearPostFailures(db: Db, postId: number) {
  db.prepare(`UPDATE posts SET consecutive_failures=0, active=1 WHERE id=?`).run(postId);
}

export function recordPostFailure(db: Db, postId: number): number {
  db.prepare(`UPDATE posts SET consecutive_failures=consecutive_failures+1 WHERE id=?`).run(postId);
  return (db.prepare(`SELECT consecutive_failures AS n FROM posts WHERE id=?`).get(postId) as { n: number }).n;
}

export function deactivatePost(db: Db, postId: number) {
  db.prepare(`UPDATE posts SET active=0 WHERE id=?`).run(postId);
}

export function setPostSurge(db: Db, postId: number, until: string | null) {
  db.prepare(`UPDATE posts SET surge_until=? WHERE id=?`).run(until, postId);
}

// ---------------------------------------------------------------- snapshots

/** Keep only an item's scalar fields (and those of a few small nested objects). */
export function slimRaw(raw: unknown): unknown {
  if (!raw || typeof raw !== "object") return raw;
  const KEEP_NESTED = new Set(["metrics", "metrics_availability", "authorMeta", "user", "owner", "videoMeta"]);
  const scalars = (o: Record<string, unknown>) => {
    const out: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(o)) {
      if (v === null || typeof v === "number" || typeof v === "boolean") out[k] = v;
      else if (typeof v === "string") out[k] = v.length > 400 ? v.slice(0, 400) + "…" : v;
    }
    return out;
  };
  const src = raw as Record<string, unknown>;
  const out = scalars(src);
  for (const k of KEEP_NESTED) {
    const v = src[k];
    if (v && typeof v === "object" && !Array.isArray(v)) out[k] = scalars(v as Record<string, unknown>);
  }
  return out;
}

export function gzJson(v: unknown): Buffer {
  return zlib.gzipSync(Buffer.from(JSON.stringify(v)));
}

export function latestSnapshot(db: Db, postId: number): SnapshotRow | undefined {
  return db
    .prepare(
      `SELECT id, post_id, run_id, observed_at, views, likes, comments, shares, saves
       FROM snapshots WHERE post_id=? ORDER BY observed_at DESC, id DESC LIMIT 1`,
    )
    .get(postId) as SnapshotRow | undefined;
}

export function listSnapshots(db: Db, postId: number): SnapshotRow[] {
  return db
    .prepare(
      `SELECT id, post_id, run_id, observed_at, views, likes, comments, shares, saves
       FROM snapshots WHERE post_id=? ORDER BY observed_at ASC, id ASC`,
    )
    .all(postId) as SnapshotRow[];
}

export function insertSnapshot(
  db: Db,
  s: { postId: number; runId: number | null; observedAt: string; metrics: Metrics; raw: unknown },
) {
  db.prepare(
    `INSERT INTO snapshots (post_id, run_id, observed_at, views, likes, comments, shares, saves, raw_gz)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
  ).run(
    s.postId,
    s.runId,
    s.observedAt,
    s.metrics.views,
    s.metrics.likes,
    s.metrics.comments,
    s.metrics.shares,
    s.metrics.saves,
    gzJson(slimRaw(s.raw)),
  );
}

export function deleteSnapshot(db: Db, id: number) {
  db.prepare(`DELETE FROM snapshots WHERE id=?`).run(id);
}

export function replacePostDaily(db: Db, postId: number, rows: DailyRow[]) {
  const del = db.prepare(`DELETE FROM post_daily WHERE post_id=?`);
  const ins = db.prepare(
    `INSERT INTO post_daily (post_id, date, views, likes, comments, shares, saves, quality) VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
  );
  db.transaction(() => {
    del.run(postId);
    for (const r of rows) ins.run(r.post_id, r.date, r.views, r.likes, r.comments, r.shares, r.saves, r.quality);
  })();
}

export function setPostDerived(
  db: Db,
  postId: number,
  d: { latest: SnapshotRow | undefined; views24h: number | null; views7d: number | null },
) {
  const l = d.latest;
  db.prepare(
    `UPDATE posts SET latest_views=?, latest_likes=?, latest_comments=?, latest_shares=?, latest_saves=?, latest_at=?,
       views_24h=?, views_7d=? WHERE id=?`,
  ).run(
    l?.views ?? null,
    l?.likes ?? null,
    l?.comments ?? null,
    l?.shares ?? null,
    l?.saves ?? null,
    l?.observed_at ?? null,
    d.views24h,
    d.views7d,
    postId,
  );
}

// ---------------------------------------------------------------- followers

export function insertFollowers(db: Db, accountId: number, runId: number | null, observedAt: string, followers: number) {
  db.prepare(`INSERT INTO follower_snapshots (account_id, run_id, observed_at, followers) VALUES (?, ?, ?, ?)`).run(
    accountId,
    runId,
    observedAt,
    followers,
  );
}

// ---------------------------------------------------------------- runs

export function startRun(
  db: Db,
  r: { kind: string; trigger: string; platform: string | null; actor: string | null; keyLabel?: string | null; input?: unknown },
): number {
  const res = db
    .prepare(
      `INSERT INTO scrape_runs (started_at, kind, trigger_source, platform, actor, key_label, input_json, status)
       VALUES (?, ?, ?, ?, ?, ?, ?, 'running')`,
    )
    .run(
      nowIso(),
      r.kind,
      r.trigger,
      r.platform,
      r.actor,
      r.keyLabel ?? null,
      r.input === undefined ? null : JSON.stringify(r.input),
    );
  return Number(res.lastInsertRowid);
}

export function finishRun(
  db: Db,
  id: number,
  r: {
    status: string;
    itemsOk?: number;
    itemsFailed?: number;
    costUsd?: number;
    apifyRunId?: string;
    error?: string | null;
  },
) {
  db.prepare(
    `UPDATE scrape_runs SET finished_at=?, status=?,
       items_ok=COALESCE(?, items_ok), items_failed=COALESCE(?, items_failed),
       cost_usd=COALESCE(?, cost_usd), apify_run_id=COALESCE(?, apify_run_id),
       error=? WHERE id=?`,
  ).run(
    nowIso(),
    r.status,
    r.itemsOk ?? null,
    r.itemsFailed ?? null,
    r.costUsd ?? null,
    r.apifyRunId ?? null,
    r.error ?? null,
    id,
  );
}

export function setRunCost(db: Db, id: number, usd: number, final: boolean) {
  db.prepare(`UPDATE scrape_runs SET cost_usd=?, cost_final=? WHERE id=?`).run(usd, final ? 1 : 0, id);
}

export function listUnreconciledRuns(db: Db, sinceIso: string): RunRow[] {
  return db
    .prepare(`SELECT * FROM scrape_runs WHERE cost_final=0 AND apify_run_id IS NOT NULL AND started_at>=? ORDER BY id`)
    .all(sinceIso) as RunRow[];
}

/** This tracker's own spend in a calendar month (UTC, like Apify's billing). */
export function monthCostUsd(db: Db, monthPrefix: string): number {
  const r = db
    .prepare(`SELECT COALESCE(SUM(cost_usd),0) AS c FROM scrape_runs WHERE substr(started_at,1,7)=?`)
    .get(monthPrefix) as { c: number };
  return r.c;
}

/** Runs left "running" by a process that died (restart mid-cycle). Returns them so they can be aborted. */
export function closeStaleRuns(db: Db, olderThanIso: string): RunRow[] {
  const stale = db.prepare(`SELECT * FROM scrape_runs WHERE status='running' AND started_at<?`).all(olderThanIso) as RunRow[];
  db.prepare(
    `UPDATE scrape_runs SET status='error', finished_at=?, error='interrupted (scraper restarted mid-run)'
     WHERE status='running' AND started_at<?`,
  ).run(nowIso(), olderThanIso);
  return stale;
}

// ---------------------------------------------------------------- anomalies

export function insertAnomaly(db: Db, a: { postId: number; runId: number | null; kind: string; detail: unknown }) {
  db.prepare(`INSERT INTO anomalies (post_id, run_id, kind, detail, created_at) VALUES (?, ?, ?, ?, ?)`).run(
    a.postId,
    a.runId,
    a.kind,
    JSON.stringify(a.detail),
    nowIso(),
  );
}
