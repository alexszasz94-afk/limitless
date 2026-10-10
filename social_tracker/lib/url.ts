/** Build a link that keeps the current filters and changes some of them. */
export function hrefWith(
  path: string,
  current: Record<string, string | undefined>,
  changes: Record<string, string | null | undefined>,
): string {
  const p = new URLSearchParams();
  const merged: Record<string, string | null | undefined> = { ...current, ...changes };
  for (const [k, v] of Object.entries(merged)) if (v) p.set(k, v);
  const qs = p.toString();
  return qs ? `${path}?${qs}` : path;
}

/** Search params (Next passes string | string[] | undefined) -> plain strings. */
export function flatParams(sp: Record<string, string | string[] | undefined>): Record<string, string | undefined> {
  const out: Record<string, string | undefined> = {};
  for (const [k, v] of Object.entries(sp)) out[k] = Array.isArray(v) ? v[0] : v;
  return out;
}

/** A return address after sign-in: only a path on this site, never another site. */
export function safeNext(v: unknown): string {
  if (typeof v !== "string" || !/^\/(?![\/\\])[^\x00-\x20\\]*$/.test(v)) return "/";
  try {
    // Belt and braces: the path must stay on this site once a browser resolves it.
    return new URL(v, "http://tracker.local").origin === "http://tracker.local" ? v : "/";
  } catch {
    return "/";
  }
}
