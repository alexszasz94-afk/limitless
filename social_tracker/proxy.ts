import { NextResponse, type NextRequest } from "next/server";
import { SESSION_COOKIE, isValidBasicAuth, isValidSession } from "@/lib/auth";

/**
 * The whole tracker is private. Signed-out page requests go to /login; API
 * requests get 401. Pages, route handlers and server actions check the
 * session again themselves (lib/session.ts), so a matcher change can never
 * open anything up.
 */
export function proxy(req: NextRequest) {
  const { pathname } = req.nextUrl;
  if (pathname === "/login") return NextResponse.next();
  if (isValidSession(req.cookies.get(SESSION_COOKIE)?.value)) return NextResponse.next();
  if (isValidBasicAuth(req.headers.get("authorization"))) return NextResponse.next();
  if (pathname.startsWith("/api/")) {
    return new NextResponse("Sign in required", {
      status: 401,
      headers: { "WWW-Authenticate": 'Basic realm="social-tracker"' },
    });
  }
  const url = req.nextUrl.clone();
  url.pathname = "/login";
  url.search = pathname === "/" ? "" : `?next=${encodeURIComponent(pathname + req.nextUrl.search)}`;
  return NextResponse.redirect(url);
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|icons/|icon.svg|apple-icon.png|manifest.webmanifest|robots.txt|favicon.ico).*)"],
};
