import { appTimezone } from "./config";

/** 999 · 1.2K · 12K · 1.2M (one decimal only below 10). */
export function fmtCompact(n: number | null | undefined): string {
  if (n === null || n === undefined || Number.isNaN(n)) return "–";
  const a = Math.abs(n);
  const sign = n < 0 ? "−" : "";
  const unit = (v: number, s: string) => {
    const r = v < 10 ? Math.round(v * 10) / 10 : Math.round(v);
    if (r >= 1000 && s === "K") return unit(v / 1000, "M");
    return `${sign}${r}${s}`;
  };
  if (a >= 1e9) return unit(a / 1e9, "B");
  if (a >= 1e6) return unit(a / 1e6, "M");
  if (a >= 1e3) return unit(a / 1e3, "K");
  return `${sign}${Math.round(a)}`;
}

export function fmtFull(n: number | null | undefined): string {
  if (n === null || n === undefined || Number.isNaN(n)) return "–";
  return Math.round(n).toLocaleString("en-US");
}

/** +12% / −4% / null when there is nothing to compare with. */
export function pctChange(cur: number, prev: number | null): number | null {
  if (prev === null || prev <= 0) return null;
  return ((cur - prev) / prev) * 100;
}

/** +12% · −4.5% (one decimal below 10%). */
export function fmtPct(p: number | null): string {
  if (p === null || !Number.isFinite(p)) return "–";
  const a = Math.abs(p);
  const v = a < 10 ? a.toFixed(1).replace(/\.0$/, "") : Math.round(a).toString();
  return `${p > 0 ? "+" : p < 0 ? "−" : ""}${v}%`;
}

export function fmtSigned(n: number | null): string {
  if (n === null) return "–";
  if (n === 0) return "±0";
  return `${n > 0 ? "+" : "−"}${fmtCompact(Math.abs(n))}`;
}

export function fmtUsd(n: number, digits = 2): string {
  return `$${n.toFixed(digits)}`;
}

export function timeAgo(iso: string | null | undefined, now = Date.now()): string {
  if (!iso) return "never";
  const s = Math.max(0, (now - Date.parse(iso)) / 1000);
  if (s < 60) return "just now";
  if (s < 3600) return `${Math.round(s / 60)} min ago`;
  if (s < 86400) return `${Math.round(s / 3600)} h ago`;
  const d = Math.round(s / 86400);
  return d === 1 ? "yesterday" : `${d} days ago`;
}

/** Age of a post: 5h · 3d · 6w · 4mo. */
export function fmtAge(iso: string | null | undefined, now = Date.now()): string {
  if (!iso) return "–";
  const h = Math.max(0, (now - Date.parse(iso)) / 3600_000);
  if (h < 1) return `${Math.max(1, Math.round(h * 60))}m`;
  if (h < 48) return `${Math.round(h)}h`;
  const d = h / 24;
  if (d < 21) return `${Math.round(d)}d`;
  if (d < 90) return `${Math.round(d / 7)}w`;
  return `${Math.round(d / 30)}mo`;
}

const dtCache = new Map<string, Intl.DateTimeFormat>();
function dt(opts: Intl.DateTimeFormatOptions): Intl.DateTimeFormat {
  const tz = appTimezone();
  const key = tz + JSON.stringify(opts);
  let f = dtCache.get(key);
  if (!f) {
    f = new Intl.DateTimeFormat("en-GB", { timeZone: tz, ...opts });
    dtCache.set(key, f);
  }
  return f;
}

/** "6 Oct, 14:32" in the tracker's timezone. */
export function fmtDateTime(iso: string | null | undefined): string {
  if (!iso) return "–";
  return dt({ day: "numeric", month: "short", hour: "2-digit", minute: "2-digit", hourCycle: "h23" }).format(new Date(iso));
}

export function fmtHandle(platform: string, handle: string): string {
  return platform === "facebook" ? handle : `@${handle}`;
}
