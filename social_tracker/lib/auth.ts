import crypto from "node:crypto";

/**
 * One passphrase (TRACKER_PASSPHRASE in .env), no accounts. Signing in sets an
 * httpOnly cookie holding an HMAC of the passphrase, so changing the
 * passphrase signs every session out. HTTP Basic auth with the passphrase
 * (any user name) also works, for curl and health checks.
 */
export const SESSION_COOKIE = "st_session";
export const SESSION_MAX_AGE = 60 * 60 * 24 * 30;

function passphrase(): string | null {
  const p = process.env.TRACKER_PASSPHRASE;
  return p && p !== "change-me" ? p : null;
}

function hmac(value: string): string {
  return crypto.createHmac("sha256", "social-tracker-v1").update(value).digest("hex");
}

function safeEqual(a: string, b: string): boolean {
  const ha = crypto.createHash("sha256").update(a).digest();
  const hb = crypto.createHash("sha256").update(b).digest();
  return crypto.timingSafeEqual(ha, hb);
}

export function authConfigured(): boolean {
  return passphrase() !== null;
}

/** Cookie value for a correct passphrase, null otherwise. */
export function sessionFor(attempt: string): string | null {
  const p = passphrase();
  if (!p || !safeEqual(attempt, p)) return null;
  return hmac(p);
}

export function isValidSession(cookieValue: string | undefined | null): boolean {
  const p = passphrase();
  return !!p && !!cookieValue && safeEqual(cookieValue, hmac(p));
}

export function isValidBasicAuth(header: string | null): boolean {
  const p = passphrase();
  if (!p || !header?.startsWith("Basic ")) return false;
  try {
    const decoded = Buffer.from(header.slice(6), "base64").toString("utf-8");
    return safeEqual(decoded.slice(decoded.indexOf(":") + 1), p);
  } catch {
    return false;
  }
}
