import Link from "next/link";
import { Suspense } from "react";
import Mark from "./Mark";
import NavLinks from "./NavLinks";
import { signOut } from "@/lib/actions";
import { freshness } from "@/lib/queries";
import { fmtAge, timeAgo } from "@/lib/format";

export default function Shell({ children }: { children: React.ReactNode }) {
  const f = freshness();
  return (
    <>
      <header className="sticky top-0 z-30 border-b border-line bg-bg/80 backdrop-blur-md">
        <div className="mx-auto max-w-6xl px-4 sm:px-6">
          <div className="flex items-center justify-between gap-3 pt-3">
            <Link href="/" className="flex min-w-0 items-center gap-2.5">
              <Mark size={32} />
              <span className="min-w-0 leading-tight">
                <span className="block text-[10px] font-bold uppercase tracking-[0.14em] text-ink-faint">Analytics</span>
                <span className="block truncate text-[15px] font-semibold tracking-tight">Social Tracker</span>
              </span>
            </Link>
            <div className="flex shrink-0 items-center gap-2">
              <Link
                href="/runs"
                className="flex items-center gap-2 rounded-full border border-line bg-surface px-3 py-1.5 text-xs text-ink-dim transition-colors hover:text-ink"
                title={f.ok ? "Scraper healthy" : "Something needs attention - see Runs"}
              >
                {f.running ? (
                  <span className="dot pulse-dot bg-accent" />
                ) : (
                  <span className="dot" style={{ background: f.ok ? "var(--color-accent)" : "var(--color-warn)" }} />
                )}
                <span className="hidden sm:inline">
                  {f.running ? "Scraping now" : f.lastSuccess ? `Updated ${timeAgo(f.lastSuccess)}` : "Not scraped yet"}
                </span>
                <span className="sm:hidden">{f.running ? "Now" : f.lastSuccess ? fmtAge(f.lastSuccess) : "–"}</span>
                {!f.ok && <span className="font-medium text-warn">Check</span>}
              </Link>
              <form action={signOut}>
                <button type="submit" className="btn-quiet rounded-full px-3 py-1.5 text-xs text-ink-dim">
                  Sign out
                </button>
              </form>
            </div>
          </div>
          <div className="mt-2 pb-2">
            <Suspense fallback={<div className="h-9" />}>
              <NavLinks />
            </Suspense>
          </div>
        </div>
      </header>
      <main className="mx-auto max-w-6xl px-4 pb-24 pt-6 sm:px-6 sm:pt-8">{children}</main>
    </>
  );
}
