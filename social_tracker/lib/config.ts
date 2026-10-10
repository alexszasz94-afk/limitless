import fs from "node:fs";
import path from "node:path";

/**
 * Config files in config/ are read on every use (they are tiny), so an edit
 * that arrives with a push is live on the next request or scrape cycle, with
 * no rebuild and no restart.
 */

export type Platform = "instagram" | "tiktok" | "facebook";

/** Display order everywhere (same as the Distribution portal's tabs). */
export const PLATFORMS: Platform[] = ["instagram", "tiktok", "facebook"];

export const PLATFORM_LABEL: Record<Platform, string> = {
  instagram: "Instagram",
  tiktok: "TikTok",
  facebook: "Facebook",
};

export function isPlatform(v: unknown): v is Platform {
  return v === "instagram" || v === "tiktok" || v === "facebook";
}

export interface AccountConfig {
  platform: Platform;
  handle: string;
  url: string;
  active: boolean;
}

export interface ProductConfig {
  id: string;
  name: string;
  active: boolean;
  avatar?: string;
  accounts: AccountConfig[];
}

export interface RefreshTier {
  maxAgeDays: number | null;
  everyHours: number;
}

export interface CadenceFile {
  timezone: string;
  anchorHourLocal: number;
  discovery: { atHours: number[]; resultsPerProfile: number };
  profiles: { atHours: number[] };
  refreshTiers: RefreshTier[];
  platformOverrides: Partial<Record<Platform, { maxEveryHours: number }>>;
  /** How deep a refresh crawl of a profile/page may go (Instagram, Facebook). */
  crawlDepthCap?: Partial<Record<"instagram" | "facebook", number>>;
  surge: {
    enabled: boolean;
    deltaMultiple: number;
    promoteEveryHours: number;
    durationHours: number;
  };
}

export interface BudgetFile {
  monthlyBudgetUsd: number;
  perRunMaxItems: number;
  keyMinHeadroomUsd: number;
}

export function configDir(): string {
  return process.env.CONFIG_DIR || path.join(/*turbopackIgnore: true*/ process.cwd(), "config");
}

function readJson<T>(file: string): T {
  // turbopackIgnore: config/ is read at run time, never bundled.
  const p = path.join(/*turbopackIgnore: true*/ configDir(), file);
  // Strip a BOM and NUL padding (Windows editors and synced drives add both).
  const raw = fs.readFileSync(/*turbopackIgnore: true*/ p, "utf-8").replace(/^﻿/, "").replace(/\0+/g, "");
  return JSON.parse(raw) as T;
}

export function loadProducts(): ProductConfig[] {
  const file = readJson<{ products: ProductConfig[] }>("products.json");
  const products = file.products ?? [];
  const ids = new Set<string>();
  const handles = new Set<string>();
  for (const p of products) {
    if (!/^[a-z0-9_-]+$/.test(p.id)) throw new Error(`products.json: bad product id "${p.id}"`);
    if (ids.has(p.id)) throw new Error(`products.json: duplicate product id "${p.id}"`);
    ids.add(p.id);
    for (const a of p.accounts ?? []) {
      if (!isPlatform(a.platform)) {
        throw new Error(`products.json: ${p.id} has an unknown platform "${a.platform}"`);
      }
      const key = `${a.platform}:${a.handle.toLowerCase()}`;
      if (handles.has(key)) throw new Error(`products.json: account ${key} is listed twice`);
      handles.add(key);
    }
  }
  return products;
}

export function loadCadence(): CadenceFile {
  return readJson<CadenceFile>("cadence.json");
}

export function loadBudget(): BudgetFile {
  return readJson<BudgetFile>("budget.json");
}

/** The tracker's timezone: all "days" (charts, today, 7 days) are local days here. */
let tzCache: { tz: string; at: number } | null = null;
export function appTimezone(): string {
  // Called for every date conversion: re-read cadence.json at most once a minute.
  if (tzCache && Date.now() - tzCache.at < 60_000) return tzCache.tz;
  let tz = "UTC";
  try {
    tz = loadCadence().timezone || tz;
  } catch {
    // keep the default
  }
  tzCache = { tz, at: Date.now() };
  return tz;
}

/**
 * Apify keys, tried in order. On the server they sit in APIFY_TOKENS
 * (comma-separated, .env). Locally APIFY_KEYS_FILE can point at a text file
 * (a plain text file): only its apify_api_ tokens are read, nothing else in
 * the file is touched, and no token is ever printed.
 */
export function apifyTokens(): string[] {
  const out: string[] = [];
  const add = (t: string) => {
    const v = t.trim();
    if (v && !out.includes(v)) out.push(v);
  };
  (process.env.APIFY_TOKENS || "").split(",").forEach(add);
  const file = process.env.APIFY_KEYS_FILE;
  if (file) {
    try {
      const text = fs.readFileSync(path.resolve(/*turbopackIgnore: true*/ process.cwd(), file), "utf-8");
      for (const m of text.matchAll(/apify_api_[A-Za-z0-9]+/g)) add(m[0]);
    } catch {
      // unreadable file = no extra keys; the runs page shows "no keys"
    }
  }
  return out;
}

/** Short label for a key, safe to log and show: the last 6 characters only. */
export function keyLabel(token: string): string {
  return "…" + token.slice(-6);
}
