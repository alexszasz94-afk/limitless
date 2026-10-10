/**
 * Database adapter: SQLite on local disk.
 *
 * SWAP POINT: to move to hosted Postgres later, reimplement the exported
 * functions in this file. Nothing outside this file touches SQL, except
 * lib/day.ts which uses the exported `db` transaction helper.
 */
import Database from "better-sqlite3";
import fs from "node:fs";
import path from "node:path";
import type { Persona, Poster, ContentItem, Platform } from "./types";

const DATA_DIR = process.env.DATA_DIR ?? path.join(/*turbopackIgnore: true*/ process.cwd(), "data");
const DB_PATH = path.join(DATA_DIR, "portal.db");

// One connection per server process. Kept on globalThis so dev-mode hot
// reloads don't open a new handle on every edit.
const g = globalThis as unknown as { __distDb?: Database.Database };

export function db(): Database.Database {
  if (g.__distDb) return g.__distDb;
  fs.mkdirSync(DATA_DIR, { recursive: true });
  const d = new Database(DB_PATH);
  d.pragma("journal_mode = WAL");
  d.pragma("synchronous = NORMAL");
  d.pragma("foreign_keys = ON");
  d.pragma("busy_timeout = 5000");
  migrate(d);
  g.__distDb = d;
  return d;
}

function migrate(d: Database.Database) {
  d.exec(`
    CREATE TABLE IF NOT EXISTS personas (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      handles_json TEXT NOT NULL,
      bio TEXT NOT NULL DEFAULT '',
      profile_image_path TEXT NOT NULL DEFAULT '',
      cover_image_path TEXT NOT NULL DEFAULT '',
      competitors_json TEXT NOT NULL DEFAULT '[]',
      keywords_json TEXT NOT NULL DEFAULT '[]',
      voice_notes TEXT NOT NULL DEFAULT '',
      pinned_comment TEXT NOT NULL DEFAULT ''
    );

    CREATE TABLE IF NOT EXISTS posters (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      token TEXT NOT NULL UNIQUE,
      persona_id TEXT NOT NULL REFERENCES personas(id),
      start_date TEXT NOT NULL,
      timezone TEXT NOT NULL DEFAULT 'UTC'
    );

    CREATE TABLE IF NOT EXISTS content_items (
      id TEXT PRIMARY KEY,
      persona_id TEXT NOT NULL REFERENCES personas(id),
      kind TEXT NOT NULL CHECK (kind IN ('reel','story','highlight_cover')),
      master_path TEXT NOT NULL,
      proxy_path TEXT NOT NULL,
      source_clip_id TEXT,
      duration_seconds REAL,
      captions_json TEXT NOT NULL DEFAULT '{}',
      queue_order INTEGER NOT NULL DEFAULT 0,
      status TEXT NOT NULL DEFAULT 'queued'
        CHECK (status IN ('queued','assigned','posted','retired')),
      variants_json TEXT NOT NULL DEFAULT '{}',
      suppress_pinned_comment INTEGER NOT NULL DEFAULT 0
    );
    CREATE INDEX IF NOT EXISTS idx_content_queue
      ON content_items (persona_id, kind, status, queue_order);

    CREATE TABLE IF NOT EXISTS assignments (
      poster_id TEXT NOT NULL REFERENCES posters(id),
      day INTEGER NOT NULL,
      task_index INTEGER NOT NULL,
      content_item_id TEXT REFERENCES content_items(id),
      PRIMARY KEY (poster_id, day, task_index)
    );

    CREATE TABLE IF NOT EXISTS progress (
      poster_id TEXT NOT NULL REFERENCES posters(id),
      day INTEGER NOT NULL,
      task_index INTEGER NOT NULL,
      completed_at TEXT NOT NULL,
      PRIMARY KEY (poster_id, day, task_index)
    );

    -- platform ids are validated against config/platforms.json in the API,
    -- not here, so a new platform never needs a schema change.
    CREATE TABLE IF NOT EXISTS post_log (
      poster_id TEXT NOT NULL REFERENCES posters(id),
      content_item_id TEXT NOT NULL REFERENCES content_items(id),
      platform TEXT NOT NULL,
      marked_at TEXT NOT NULL,
      PRIMARY KEY (poster_id, content_item_id, platform)
    );

    -- tasks_json: the day's task list as it was when the day first opened.
    -- Editing schedule.json later never changes a day that is already open.
    CREATE TABLE IF NOT EXISTS day_opens (
      poster_id TEXT NOT NULL REFERENCES posters(id),
      day INTEGER NOT NULL,
      opened_at TEXT NOT NULL,
      tasks_json TEXT,
      PRIMARY KEY (poster_id, day)
    );
  `);

  // Columns added after the first local build: bring existing databases up without losing rows.
  const cols = d.prepare("PRAGMA table_info(day_opens)").all() as Array<{ name: string }>;
  if (!cols.some((c) => c.name === "tasks_json")) {
    d.exec("ALTER TABLE day_opens ADD COLUMN tasks_json TEXT");
  }
}

// ---- row mappers -----------------------------------------------------------

/* eslint-disable @typescript-eslint/no-explicit-any */
function rowToPersona(r: any): Persona {
  return {
    id: r.id,
    name: r.name,
    handles: JSON.parse(r.handles_json),
    bio: r.bio,
    profile_image_path: r.profile_image_path,
    cover_image_path: r.cover_image_path,
    competitors: JSON.parse(r.competitors_json),
    keywords: JSON.parse(r.keywords_json),
    voice_notes: r.voice_notes,
    pinned_comment: r.pinned_comment ?? "",
  };
}

function rowToContent(r: any): ContentItem {
  return {
    id: r.id,
    persona_id: r.persona_id,
    kind: r.kind,
    master_path: r.master_path,
    proxy_path: r.proxy_path,
    source_clip_id: r.source_clip_id,
    duration_seconds: r.duration_seconds,
    captions: JSON.parse(r.captions_json),
    queue_order: r.queue_order,
    status: r.status,
    variants: JSON.parse(r.variants_json ?? "{}"),
    suppress_pinned_comment: !!r.suppress_pinned_comment,
  };
}

// ---- queries ---------------------------------------------------------------

export function getPosterByToken(token: string): Poster | null {
  if (!/^[a-zA-Z0-9_-]{6,64}$/.test(token)) return null;
  const r = db().prepare("SELECT * FROM posters WHERE token = ?").get(token) as any;
  return r ? { ...r } : null;
}

export function getAllPosters(): Poster[] {
  return db().prepare("SELECT * FROM posters ORDER BY name").all() as Poster[];
}

export function getPersona(id: string): Persona | null {
  const r = db().prepare("SELECT * FROM personas WHERE id = ?").get(id) as any;
  return r ? rowToPersona(r) : null;
}

export function getContentItem(id: string): ContentItem | null {
  const r = db().prepare("SELECT * FROM content_items WHERE id = ?").get(id) as any;
  return r ? rowToContent(r) : null;
}

export function getQueuedContent(personaId: string, kind: string): ContentItem[] {
  const rows = db()
    .prepare(
      `SELECT * FROM content_items
       WHERE persona_id = ? AND kind = ? AND status = 'queued'
       ORDER BY queue_order`,
    )
    .all(personaId, kind) as any[];
  return rows.map(rowToContent);
}

export function getAssignments(posterId: string, day: number): Map<number, string | null> {
  const rows = db()
    .prepare("SELECT task_index, content_item_id FROM assignments WHERE poster_id = ? AND day = ?")
    .all(posterId, day) as any[];
  return new Map(rows.map((r) => [r.task_index, r.content_item_id]));
}

/** Frozen task lists of every day this poster has opened (day -> tasks JSON or null). */
export function getOpenedDays(posterId: string): Map<number, string | null> {
  const rows = db()
    .prepare("SELECT day, tasks_json FROM day_opens WHERE poster_id = ?")
    .all(posterId) as any[];
  return new Map(rows.map((r) => [r.day, r.tasks_json ?? null]));
}

/** When the last task of a day was ticked (ISO string), or null. */
export function dayCompletedAt(posterId: string, day: number): string | null {
  const r = db()
    .prepare("SELECT MAX(completed_at) AS t FROM progress WHERE poster_id = ? AND day = ?")
    .get(posterId, day) as any;
  return r?.t ?? null;
}

export function isDayOpened(posterId: string, day: number): boolean {
  return !!db().prepare("SELECT 1 FROM day_opens WHERE poster_id = ? AND day = ?").get(posterId, day);
}

export function getProgress(posterId: string, day: number): Set<number> {
  const rows = db()
    .prepare("SELECT task_index FROM progress WHERE poster_id = ? AND day = ?")
    .all(posterId, day) as any[];
  return new Set(rows.map((r) => r.task_index));
}

export function getCompletedCountByDay(posterId: string): Map<number, number> {
  const rows = db()
    .prepare("SELECT day, COUNT(*) AS n FROM progress WHERE poster_id = ? GROUP BY day")
    .all(posterId) as any[];
  return new Map(rows.map((r) => [r.day, r.n]));
}

export function lastActivity(posterId: string): string | null {
  const r = db()
    .prepare(
      `SELECT MAX(t) AS t FROM (
         SELECT MAX(completed_at) AS t FROM progress WHERE poster_id = ?
         UNION ALL SELECT MAX(marked_at) FROM post_log WHERE poster_id = ?
       )`,
    )
    .get(posterId, posterId) as any;
  return r?.t ?? null;
}

/** Tick a task. `at` = when the poster tapped (an offline tap syncs later). */
export function markProgress(posterId: string, day: number, taskIndex: number, at?: string): void {
  db()
    .prepare(
      `INSERT OR IGNORE INTO progress (poster_id, day, task_index, completed_at)
       VALUES (?, ?, ?, ?)`,
    )
    .run(posterId, day, taskIndex, at ?? new Date().toISOString());
}

export function dayOpenedAt(posterId: string, day: number): string | null {
  const r = db()
    .prepare("SELECT opened_at FROM day_opens WHERE poster_id = ? AND day = ?")
    .get(posterId, day) as any;
  return r?.opened_at ?? null;
}

export function unmarkProgress(posterId: string, day: number, taskIndex: number): void {
  db()
    .prepare("DELETE FROM progress WHERE poster_id = ? AND day = ? AND task_index = ?")
    .run(posterId, day, taskIndex);
}

export function logPost(posterId: string, contentItemId: string, platform: Platform): void {
  db()
    .prepare(
      `INSERT OR IGNORE INTO post_log (poster_id, content_item_id, platform, marked_at)
       VALUES (?, ?, ?, ?)`,
    )
    .run(posterId, contentItemId, platform, new Date().toISOString());
}

export function unlogPost(posterId: string, contentItemId: string, platform: Platform): void {
  db()
    .prepare("DELETE FROM post_log WHERE poster_id = ? AND content_item_id = ? AND platform = ?")
    .run(posterId, contentItemId, platform);
}

export function getPostedPlatforms(posterId: string, contentItemId: string): Platform[] {
  const rows = db()
    .prepare("SELECT platform FROM post_log WHERE poster_id = ? AND content_item_id = ?")
    .all(posterId, contentItemId) as any[];
  return rows.map((r) => r.platform);
}

export function setContentStatus(id: string, status: string): void {
  db().prepare("UPDATE content_items SET status = ? WHERE id = ?").run(status, id);
}

/** Is this content item assigned to this poster on some day? */
export function isAssignedTo(posterId: string, contentItemId: string): boolean {
  return !!db()
    .prepare("SELECT 1 FROM assignments WHERE poster_id = ? AND content_item_id = ? LIMIT 1")
    .get(posterId, contentItemId);
}

export function countQueued(personaId: string): Record<string, number> {
  const rows = db()
    .prepare(
      `SELECT kind, COUNT(*) AS n FROM content_items
       WHERE persona_id = ? AND status = 'queued' GROUP BY kind`,
    )
    .all(personaId) as any[];
  const out: Record<string, number> = {};
  for (const r of rows) out[r.kind] = r.n;
  return out;
}

export function countPosted(posterId: string): number {
  const r = db()
    .prepare("SELECT COUNT(DISTINCT content_item_id) AS n FROM post_log WHERE poster_id = ?")
    .get(posterId) as any;
  return r?.n ?? 0;
}

export function hasAnyProgress(): boolean {
  try {
    const r = db()
      .prepare("SELECT (SELECT COUNT(*) FROM progress) + (SELECT COUNT(*) FROM post_log) AS n")
      .get() as any;
    return (r?.n ?? 0) > 0;
  } catch {
    return false;
  }
}
