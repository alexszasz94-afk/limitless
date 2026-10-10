import { apifyTokens, keyLabel, loadBudget } from "../config";
import { ApifyError, getLimits } from "./client";

/**
 * Key rotation over every configured Apify key (APIFY_TOKENS, one or more).
 * Keys are tried in order; a key is used only
 * when its own monthly headroom (checked through /users/me/limits, cached for
 * 10 min) covers the run's estimate plus keyMinHeadroomUsd. A dead key (401)
 * is skipped for the life of the process, an exhausted one until its cache
 * expires. The same keys may also serve other tools, so live headroom (not
 * a local count) is what decides.
 */

interface KeyState {
  token: string;
  label: string;
  dead: boolean;
  exhausted: boolean;
  checkedAt: number;
  headroomUsd: number;
}

const CACHE_TTL_MS = 10 * 60 * 1000;
let states: KeyState[] | null = null;
let signature = "";

function initStates(): KeyState[] {
  const tokens = apifyTokens();
  const sig = tokens.join(",");
  if (!states || sig !== signature) {
    signature = sig;
    states = tokens.map((token) => ({
      token,
      label: keyLabel(token),
      dead: false,
      exhausted: false,
      checkedAt: 0,
      headroomUsd: 0,
    }));
  }
  return states;
}

export interface UsableKey {
  token: string;
  label: string;
}

/** The first key whose headroom covers `estimatedUsd`, or null. */
export async function getUsableKey(estimatedUsd: number, skip: Set<string> = new Set()): Promise<UsableKey | null> {
  const need = estimatedUsd + loadBudget().keyMinHeadroomUsd;
  for (const s of initStates()) {
    if (s.dead || skip.has(s.label)) continue;
    const fresh = Date.now() - s.checkedAt < CACHE_TTL_MS;
    if (s.exhausted && fresh) continue;
    if (!fresh) {
      try {
        const l = await getLimits(s.token);
        s.headroomUsd = l.maxMonthlyUsageUsd - l.monthlyUsageUsd;
        s.exhausted = s.headroomUsd <= 0;
        s.checkedAt = Date.now();
      } catch (e) {
        if (e instanceof ApifyError && (e.httpStatus === 401 || e.httpStatus === 403 || e.httpStatus === 404)) {
          s.dead = true;
        } else {
          s.checkedAt = Date.now() - CACHE_TTL_MS + 60_000; // transient: retry this key in a minute
        }
        continue;
      }
    }
    if (!s.exhausted && s.headroomUsd >= need) return { token: s.token, label: s.label };
  }
  return null;
}

/** A run failed on a payment/limit error: move on to the next key. */
export function markKeyExhausted(label: string): void {
  for (const s of initStates()) {
    if (s.label === label) {
      s.exhausted = true;
      s.checkedAt = Date.now();
    }
  }
}

/** After a run: shrink the cached headroom so the same near-empty key is not picked again. */
export function noteKeySpend(label: string, usd: number): void {
  for (const s of initStates()) {
    if (s.label === label) {
      s.headroomUsd = Math.max(0, s.headroomUsd - usd);
      if (s.headroomUsd <= 0) s.exhausted = true;
    }
  }
}

export function tokenForLabel(label: string | null): string | null {
  if (!label) return null;
  return initStates().find((s) => s.label === label)?.token ?? null;
}

export interface KeyStatus {
  /** Position of the key in the list (1 = first key in APIFY_TOKENS). */
  n: number;
  label: string;
  /** "not reached" = Apify did not answer for this key (twice); its numbers are unknown this time. */
  status: "ok" | "used up" | "invalid" | "not reached";
  usedUsd: number | null;
  capUsd: number | null;
  cycleStart: string | null;
  cycleEnd: string | null;
  runningNow: number;
}

export interface KeyPoolSummary {
  checkedAt: string;
  total: number;
  ok: number;
  overCap: number;
  invalid: number;
  /** Keys Apify did not answer for this time (network); left out of the money totals. */
  notReached?: number;
  usedUsd: number;
  capUsd: number;
  /** Credit left, key by key: a key that ran a little past its cap counts 0, not minus. */
  leftUsd?: number;
  runningNow: number;
}

const round2 = (n: number) => Math.round(n * 100) / 100;

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

/** 401/403/404 = the key itself is refused; anything else (timeout, 5xx, 429) is the network. */
const isRefused = (e: unknown) =>
  e instanceof ApifyError && (e.httpStatus === 401 || e.httpStatus === 403 || e.httpStatus === 404);

/**
 * Live status of every key, 10 at a time (153 calls, ~4 s; free on Apify's
 * side). Usage covers everything that key ran - this tracker and anything
 * else the keys are used for. A key is "invalid" only
 * when Apify refuses it; a call that fails for any other reason is tried once
 * more and then shown as "not reached", so a network blip never looks like a
 * dead key or silently shrinks the totals.
 */
export async function checkAllKeys(
  tokens: string[] = apifyTokens(),
  fetchLimits: typeof getLimits = getLimits,
  retryDelayMs = 1500,
): Promise<{ summary: KeyPoolSummary; keys: KeyStatus[] }> {
  const keys: KeyStatus[] = [];
  const one = async (t: string, n: number): Promise<KeyStatus> => {
    const base = { n, label: keyLabel(t) };
    const empty = { usedUsd: null, capUsd: null, cycleStart: null, cycleEnd: null, runningNow: 0 };
    for (let attempt = 0; ; attempt++) {
      try {
        const l = await fetchLimits(t);
        return {
          ...base,
          status: l.monthlyUsageUsd >= l.maxMonthlyUsageUsd ? "used up" : "ok",
          usedUsd: round2(l.monthlyUsageUsd),
          capUsd: round2(l.maxMonthlyUsageUsd),
          cycleStart: l.cycleStart,
          cycleEnd: l.cycleEnd,
          runningNow: l.runningNow,
        };
      } catch (e) {
        if (isRefused(e)) return { ...base, status: "invalid", ...empty };
        if (attempt >= 1) return { ...base, status: "not reached", ...empty };
        await sleep(retryDelayMs);
      }
    }
  };
  for (let i = 0; i < tokens.length; i += 10) {
    keys.push(...(await Promise.all(tokens.slice(i, i + 10).map((t, j) => one(t, i + j + 1)))));
  }
  const live = keys.filter((k) => k.usedUsd !== null && k.capUsd !== null);
  const summary: KeyPoolSummary = {
    checkedAt: new Date().toISOString(),
    total: keys.length,
    ok: keys.filter((k) => k.status === "ok").length,
    overCap: keys.filter((k) => k.status === "used up").length,
    invalid: keys.filter((k) => k.status === "invalid").length,
    notReached: keys.filter((k) => k.status === "not reached").length,
    usedUsd: round2(live.reduce((s, k) => s + (k.usedUsd ?? 0), 0)),
    capUsd: round2(live.reduce((s, k) => s + (k.capUsd ?? 0), 0)),
    leftUsd: round2(live.reduce((s, k) => s + Math.max(0, (k.capUsd ?? 0) - (k.usedUsd ?? 0)), 0)),
    runningNow: keys.reduce((s, k) => s + k.runningNow, 0),
  };
  return { summary, keys };
}

/** Credit left from a stored summary (older summaries have no leftUsd). */
export function poolLeftUsd(s: Pick<KeyPoolSummary, "capUsd" | "usedUsd" | "leftUsd">): number {
  return s.leftUsd ?? Math.max(0, s.capUsd - s.usedUsd);
}
