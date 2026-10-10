/**
 * Config loader for /config/*.json.
 *
 * Files are re-read only when they change on disk (mtime check), so editing
 * the schedule, platforms or checklist copy never needs a rebuild or restart,
 * while a page render that resolves many days (currentDay walks the
 * schedule) still parses each file at most once.
 */
import fs from "node:fs";
import path from "node:path";
import type { DayTask, PlatformInfo } from "./types";

const CONFIG_DIR = process.env.CONFIG_DIR ?? path.join(/*turbopackIgnore: true*/ process.cwd(), "config");

const cache = new Map<string, { mtimeMs: number; size: number; data: unknown }>();

function readJson<T>(name: string): T {
  const file = path.join(CONFIG_DIR, name);
  const st = fs.statSync(file);
  const hit = cache.get(name);
  if (hit && hit.mtimeMs === st.mtimeMs && hit.size === st.size) return hit.data as T;
  const data = JSON.parse(fs.readFileSync(file, "utf8")) as T;
  cache.set(name, { mtimeMs: st.mtimeMs, size: st.size, data });
  return data;
}

// ---- schedule --------------------------------------------------------------

export interface WarmupDefaults {
  per_account_minutes: number;
  behaviors: string[];
}

export interface ScheduleDays {
  days: Array<{
    day: number | "repeat_from";
    repeat_from?: number;
    tasks: DayTask[];
  }>;
}

export interface ScheduleConfig extends ScheduleDays {
  warmup_defaults: WarmupDefaults;
  /** true (default): the next day opens on the next calendar day at the
   *  earliest, so a poster can't run through several days in one sitting. */
  one_day_per_calendar_day?: boolean;
  /** Per-persona schedule overrides, keyed by persona id. A persona listed
   *  here uses its own day template instead of the global one. */
  overrides?: Record<string, ScheduleDays>;
}

export function getScheduleConfig(): ScheduleConfig {
  return readJson<ScheduleConfig>("schedule.json");
}

export function oneDayPerCalendarDay(): boolean {
  return getScheduleConfig().one_day_per_calendar_day !== false;
}

function resolveDay(cfg: ScheduleDays, day: number): DayTask[] {
  const exact = cfg.days.find((d) => d.day === day);
  if (exact) return exact.tasks;
  const repeat = cfg.days.find((d) => d.day === "repeat_from");
  if (repeat && day >= (repeat.repeat_from ?? Infinity)) return repeat.tasks;
  // Past the fixed days but before repeat_from (misconfig): use the last fixed day.
  const fixed = cfg.days.filter((d) => typeof d.day === "number");
  const last = fixed[fixed.length - 1];
  return last ? last.tasks : [];
}

/** Task list for a (1-based) personal day. Pass the persona id so
 *  per-persona overrides apply. */
export function tasksForDay(day: number, personaId?: string): DayTask[] {
  const cfg = getScheduleConfig();
  const override = personaId ? cfg.overrides?.[personaId] : undefined;
  return resolveDay(override ?? cfg, day);
}

// ---- platforms -------------------------------------------------------------

export function getPlatforms(): PlatformInfo[] {
  return readJson<{ platforms: PlatformInfo[] }>("platforms.json").platforms;
}

export function platformIds(): string[] {
  return getPlatforms().map((p) => p.id);
}

// ---- checklist copy ----------------------------------------------------------

export interface PrivacyItem {
  id: string;
  mode: "deny" | "do";
  title: string;
  detail: string;
  needs_verification?: boolean;
  verified_on: string;
}

export interface PrivacyConfig {
  page_note: string;
  items: PrivacyItem[];
}

export function getPrivacyConfig(): PrivacyConfig {
  return readJson("privacy_lockdown.json");
}

export interface CreateAccountsConfig {
  intro: string;
  platforms: Array<{ platform: string; label: string; steps: string[] }>;
}

export function getCreateAccountsConfig(): CreateAccountsConfig {
  return readJson("create_accounts.json");
}

export interface PersonaSeed {
  id: string;
  name: string;
  handles: Record<string, string>;
  bio: string;
  competitors: Array<{ platform: string; handle: string; note?: string }>;
  keywords: string[];
  voice_notes?: string;
  pinned_comment?: string;
}

export function getPersonasConfig(): { personas: PersonaSeed[] } {
  return readJson("personas.json");
}
