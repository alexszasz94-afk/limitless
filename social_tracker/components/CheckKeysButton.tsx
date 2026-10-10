"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

/** Checks every Apify key live, then reloads the page's numbers. */
export default function CheckKeysButton() {
  const router = useRouter();
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState<string | null>(null);
  async function check() {
    setBusy(true);
    setMsg(null);
    try {
      const r = await fetch("/api/keys/check", { method: "POST" });
      const body = (await r.json().catch(() => ({}))) as { message?: string };
      setMsg(r.ok ? "Up to date." : (body.message ?? "Check failed."));
      router.refresh();
    } catch {
      setMsg("Check failed (offline?).");
    } finally {
      setBusy(false);
    }
  }
  return (
    <div className="flex flex-col items-start gap-1.5 sm:items-end">
      <button
        type="button"
        onClick={check}
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
        {busy ? "Checking all keys…" : "Check now"}
      </button>
      <p className="min-h-4 text-xs text-ink-dim" aria-live="polite">
        {msg ?? ""}
      </p>
    </div>
  );
}
