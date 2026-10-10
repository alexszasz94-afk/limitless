import { cookies, headers } from "next/headers";
import { SESSION_COOKIE, isValidBasicAuth, isValidSession } from "./auth";

/** Route handlers check the session themselves (never rely on the proxy alone). */
export async function apiSignedIn(): Promise<boolean> {
  if (isValidSession((await cookies()).get(SESSION_COOKIE)?.value)) return true;
  return isValidBasicAuth((await headers()).get("authorization"));
}

export function unauthorized(): Response {
  return new Response("Sign in required", { status: 401, headers: { "WWW-Authenticate": 'Basic realm="social-tracker"' } });
}
