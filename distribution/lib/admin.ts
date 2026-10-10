import crypto from "node:crypto";

/**
 * Admin session: a cookie carrying an HMAC of the passphrase. No accounts,
 * no user table; the passphrase lives in the ADMIN_PASSPHRASE env var.
 * Changing the passphrase logs every admin session out.
 */
const COOKIE_NAME = "dist_admin";

function hmac(value: string): string {
  return crypto.createHmac("sha256", "distribution-admin-v1").update(value).digest("hex");
}

function safeEqual(a: string, b: string): boolean {
  const ha = crypto.createHash("sha256").update(a).digest();
  const hb = crypto.createHash("sha256").update(b).digest();
  return crypto.timingSafeEqual(ha, hb);
}

function expected(): string | null {
  const pass = process.env.ADMIN_PASSPHRASE;
  if (!pass || pass === "change-me") return null;
  return hmac(pass);
}

export function adminConfigured(): boolean {
  return expected() !== null;
}

export function adminCookieName(): string {
  return COOKIE_NAME;
}

/** Cookie value for a correct passphrase, null otherwise. */
export function adminCookieValue(passphrase: string): string | null {
  const pass = process.env.ADMIN_PASSPHRASE;
  if (!pass || pass === "change-me" || !safeEqual(passphrase, pass)) return null;
  return hmac(pass);
}

export function isAdminSession(cookieStore: {
  get: (name: string) => { value: string } | undefined;
}): boolean {
  const exp = expected();
  if (!exp) return false;
  const c = cookieStore.get(COOKIE_NAME);
  return !!c && safeEqual(c.value, exp);
}
