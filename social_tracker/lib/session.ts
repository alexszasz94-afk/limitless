import { cookies, headers } from "next/headers";
import { redirect } from "next/navigation";
import { SESSION_COOKIE, isValidBasicAuth, isValidSession } from "./auth";

/** True when the current request is signed in (cookie or Basic auth). */
export async function isSignedIn(): Promise<boolean> {
  const c = (await cookies()).get(SESSION_COOKIE)?.value;
  if (isValidSession(c)) return true;
  return isValidBasicAuth((await headers()).get("authorization"));
}

/** Every page and server action calls this; the proxy is only the first line. */
export async function requireSignIn(): Promise<void> {
  if (!(await isSignedIn())) redirect("/login");
}
