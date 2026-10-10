import type { Metadata } from "next";
import { cookies, headers } from "next/headers";
import { redirect } from "next/navigation";
import Mark from "@/components/Mark";
import { SESSION_COOKIE, SESSION_MAX_AGE, authConfigured, sessionFor } from "@/lib/auth";
import { isSignedIn } from "@/lib/session";
import { safeNext } from "@/lib/url";

export const dynamic = "force-dynamic";
export const metadata: Metadata = { title: "Sign in" };

async function signIn(formData: FormData) {
  "use server";
  const next = safeNext(formData.get("next"));
  const value = sessionFor(String(formData.get("passphrase") ?? ""));
  if (!value) {
    await new Promise((r) => setTimeout(r, 800)); // slow down guessing
    redirect(`/login?e=1${next !== "/" ? `&next=${encodeURIComponent(next)}` : ""}`);
  }
  // Secure cookie only over HTTPS, so signing in also works over plain http locally.
  const https = (await headers()).get("x-forwarded-proto") === "https";
  (await cookies()).set(SESSION_COOKIE, value, {
    httpOnly: true,
    sameSite: "lax",
    secure: https,
    maxAge: SESSION_MAX_AGE,
    path: "/",
  });
  redirect(next);
}

export default async function LoginPage({ searchParams }: { searchParams: Promise<{ e?: string; next?: string }> }) {
  const { e, next } = await searchParams;
  if (await isSignedIn()) redirect(safeNext(next));
  return (
    <main className="mx-auto flex min-h-dvh max-w-sm flex-col justify-center px-6">
      <div className="mb-8 flex items-center gap-3">
        <Mark size={48} />
        <div>
          <p className="eyebrow">Analytics</p>
          <h1 className="text-2xl font-semibold tracking-tight">Social Tracker</h1>
        </div>
      </div>
      <form action={signIn} className="flex flex-col gap-3">
        <input type="hidden" name="next" value={safeNext(next)} />
        <input
          type="password"
          name="passphrase"
          placeholder="Passphrase"
          aria-label="Passphrase"
          autoComplete="current-password"
          autoFocus
          required
          className="rounded-xl border border-line bg-surface px-4 py-3.5 text-base text-ink outline-none transition-colors placeholder:text-ink-faint focus:border-accent"
        />
        <button type="submit" className="btn-primary rounded-xl py-3.5">
          Sign in
        </button>
      </form>
      {e && (
        <p className="mt-4 text-sm text-warn" role="alert">
          Wrong passphrase.
        </p>
      )}
      {!authConfigured() && (
        <p className="mt-4 text-sm text-ink-faint">
          TRACKER_PASSPHRASE is not set (or still &quot;change-me&quot;). Set it in .env and restart.
        </p>
      )}
    </main>
  );
}
