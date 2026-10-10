import { appTimezone } from "./config";

/**
 * Local-time helpers. Every "day" in the tracker (today, last 7 days, the
 * chart's columns) is a calendar day in the configured timezone, never a UTC
 * day, and day boundaries follow daylight saving correctly (a 23 h or 25 h
 * day is still one day).
 */

const DAY_MS = 86_400_000;
const formatters = new Map<string, Intl.DateTimeFormat>();

function fmt(tz: string): Intl.DateTimeFormat {
  let f = formatters.get(tz);
  if (!f) {
    f = new Intl.DateTimeFormat("en-US", {
      timeZone: tz,
      hourCycle: "h23",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
    formatters.set(tz, f);
  }
  return f;
}

interface Parts {
  y: number;
  m: number;
  d: number;
  h: number;
  min: number;
  s: number;
}

export function localParts(ms: number, tz = appTimezone()): Parts {
  const p: Record<string, number> = {};
  for (const part of fmt(tz).formatToParts(new Date(ms))) {
    if (part.type !== "literal") p[part.type] = Number(part.value);
  }
  return { y: p.year, m: p.month, d: p.day, h: p.hour === 24 ? 0 : p.hour, min: p.minute, s: p.second };
}

/** Offset of the timezone from UTC at instant `ms`, in ms (e.g. Europe/Berlin in summer: +2 h). */
function offsetMs(ms: number, tz: string): number {
  const p = localParts(ms, tz);
  const asUtc = Date.UTC(p.y, p.m - 1, p.d, p.h, p.min, p.s);
  return asUtc - Math.floor(ms / 1000) * 1000;
}

const pad = (n: number) => String(n).padStart(2, "0");

/** YYYY-MM-DD of instant `ms` in the tracker's timezone. */
export function localDate(ms: number, tz = appTimezone()): string {
  const p = localParts(ms, tz);
  return `${p.y}-${pad(p.m)}-${pad(p.d)}`;
}

export function localHour(ms: number, tz = appTimezone()): number {
  return localParts(ms, tz).h;
}

/** YYYY-MM-DD shifted by n calendar days. */
export function addDays(date: string, n: number): string {
  const [y, m, d] = date.split("-").map(Number);
  const t = new Date(Date.UTC(y, m - 1, d) + n * DAY_MS);
  return `${t.getUTCFullYear()}-${pad(t.getUTCMonth() + 1)}-${pad(t.getUTCDate())}`;
}

/** The instant local midnight starts `date` (YYYY-MM-DD). */
export function startOfLocalDay(date: string, tz = appTimezone()): number {
  const [y, m, d] = date.split("-").map(Number);
  const naive = Date.UTC(y, m - 1, d);
  // Two passes settle the offset even on a daylight-saving switch day.
  let t = naive - offsetMs(naive, tz);
  t = naive - offsetMs(t, tz);
  return t;
}

/** The first local midnight strictly after instant `ms`. */
export function nextLocalMidnight(ms: number, tz = appTimezone()): number {
  return startOfLocalDay(addDays(localDate(ms, tz), 1), tz);
}

export function todayLocal(now = Date.now()): string {
  return localDate(now);
}

/** Every date from `from` to `to`, inclusive. */
export function dateRange(from: string, to: string): string[] {
  const out: string[] = [];
  for (let d = from; d <= to; d = addDays(d, 1)) out.push(d);
  return out;
}
