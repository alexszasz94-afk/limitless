"use client";

import { useRouter } from "next/navigation";
import { useCallback, useEffect, useRef, useState } from "react";

type State = "idle" | "requested" | "running";

/** Asks the scraper for a cycle now, then follows it until it is done and refreshes the page. */
export default function RunNowButton({ initial }: { initial: State }) {
  const router = useRouter();
  const [state, setState] = useState<State>(initial);
  const [msg, setMsg] = useState<string | null>(null);
  const seenBusy = useRef(initial !== "idle");
  const requestedAt = useRef<number | null>(initial === "requested" ? Date.now() : null);

  const poll = useCallback(async () => {
    try {
      const r = await fetch("/api/status", { cache: "no-store" });
      if (!r.ok) return;
      const s = (await r.json()) as { requested: boolean; running: boolean; heartbeat: string | null };
      const next: State = s.running ? "running" : s.requested ? "requested" : "idle";
      const scraperDown = !s.heartbeat || Date.now() - Date.parse(s.heartbeat) > 60_000;
      if (next === "requested" && scraperDown && requestedAt.current && Date.now() - requestedAt.current > 30_000) {
        // Nobody is picking the request up: say so instead of spinning forever.
        seenBusy.current = false;
        setState("idle");
        setMsg("The scraper is not running, so nothing started. See Health.");
        return;
      }
      if (next !== "idle") seenBusy.current = true;
      setState(next);
      if (next === "idle" && seenBusy.current) {
        seenBusy.current = false;
        setMsg("Done - numbers updated.");
        router.refresh();
      }
    } catch {
      // offline for a moment: keep polling
    }
  }, [router]);

  useEffect(() => {
    if (state === "idle") return;
    const t = setInterval(poll, 3000);
    return () => clearInterval(t);
  }, [state, poll]);

  async function run() {
    setMsg(null);
    const r = await fetch("/api/run-now", { method: "POST" });
    const body = (await r.json().catch(() => ({}))) as { ok?: boolean; message?: string };
    if (r.ok) {
      seenBusy.current = true;
      requestedAt.current = Date.now();
      setState("requested");
    } else {
      setMsg(body.message ?? "Could not start a scrape.");
      void poll();
    }
  }

  const busy = state !== "idle";
  return (
    <div className="flex flex-col items-start gap-1.5 sm:items-end">
      <button
        type="button"
        onClick={run}
        disabled={busy}
        className="btn-primary inline-flex items-center gap-2 rounded-xl px-4 py-2.5 text-sm"
      >
        {busy ? (
          <svg
            className="spin"
            width="15"
            height="15"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.6"
            strokeLinecap="round"
            aria-hidden="true"
          >
            <path d="M21 12a9 9 0 1 1-6.2-8.56" />
          </svg>
        ) : (
          <svg
            width="15"
            height="15"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.4"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden="true"
          >
            <path d="M21 12a9 9 0 1 1-3-6.7L21 8" />
            <path d="M21 3v5h-5" />
          </svg>
        )}
        {state === "running" ? "Scraping…" : state === "requested" ? "Starting…" : "Run now"}
      </button>
      <p className="min-h-4 text-xs text-ink-dim" aria-live="polite">
        {msg ?? ""}
      </p>
    </div>
  );
}
