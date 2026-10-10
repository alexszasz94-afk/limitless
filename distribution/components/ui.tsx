"use client";

import { useCallback, useEffect, useRef, useState } from "react";

/** The round check used everywhere. */
export function Check({
  checked,
  onToggle,
  size = 26,
  label,
}: {
  checked: boolean;
  onToggle?: () => void;
  size?: number;
  label?: string;
}) {
  return (
    <button
      type="button"
      onClick={onToggle}
      aria-pressed={checked}
      aria-label={label}
      className="relative shrink-0 transition-transform active:scale-90"
      style={{ width: size, height: size }}
    >
      {/* bigger invisible hit area for thumbs */}
      <span className="absolute -inset-2" aria-hidden="true" />
      <span
        className={`flex h-full w-full items-center justify-center rounded-full border-2 transition-all duration-200 ${
          checked
            ? "border-accent bg-accent shadow-[0_0_14px_rgba(77,141,255,0.45)]"
            : "border-line-strong bg-transparent"
        }`}
      >
        {checked && (
          <svg
            className="animate-pop"
            width={size * 0.55}
            height={size * 0.55}
            viewBox="0 0 24 24"
            fill="none"
            stroke="#0e1014"
            strokeWidth="3.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M20 6L9 17l-5-5" />
          </svg>
        )}
      </span>
    </button>
  );
}

/** A checklist row: check + text, the whole row is tappable. */
export function CheckRow({
  checked,
  onToggle,
  children,
}: {
  checked: boolean;
  onToggle: () => void;
  children: React.ReactNode;
}) {
  return (
    <li className="flex items-start gap-3">
      <Check checked={checked} onToggle={onToggle} size={24} />
      <button
        type="button"
        onClick={onToggle}
        className={`min-w-0 flex-1 pt-0.5 text-left text-[15px] leading-snug transition-colors ${
          checked ? "text-ink-faint line-through decoration-ink-faint" : "text-ink"
        }`}
      >
        {children}
      </button>
    </li>
  );
}

/** One-tap copy button with feedback. */
export function CopyButton({ text, label }: { text: string; label?: string }) {
  const [copied, setCopied] = useState(false);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  useEffect(() => () => {
    if (timer.current) clearTimeout(timer.current);
  }, []);
  const copy = useCallback(async () => {
    try {
      await navigator.clipboard.writeText(text);
    } catch {
      const ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      document.execCommand("copy");
      ta.remove();
    }
    setCopied(true);
    if (timer.current) clearTimeout(timer.current);
    timer.current = setTimeout(() => setCopied(false), 1600);
  }, [text]);
  return (
    <button
      type="button"
      onClick={copy}
      className={`inline-flex min-h-10 shrink-0 items-center gap-1.5 rounded-lg px-3 py-2 text-sm font-medium transition-colors ${
        copied ? "bg-accent text-white" : "btn-quiet"
      }`}
    >
      {copied ? (
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <path d="M20 6L9 17l-5-5" />
        </svg>
      ) : (
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" className="opacity-70">
          <rect x="9" y="9" width="12" height="12" rx="2.5" />
          <path d="M5 15V5a2 2 0 0 1 2-2h10" />
        </svg>
      )}
      {copied ? "Copied" : (label ?? "Copy")}
    </button>
  );
}

/** 98 MB / 740 KB, for showing how big a download is. */
export function fmtSize(bytes: number): string {
  if (bytes >= 1e6) return `${Math.round(bytes / 1e6)} MB`;
  return `${Math.max(1, Math.round(bytes / 1e3))} KB`;
}

/** "@handle" for usernames; names with spaces (a Facebook Page name) stay as they are. */
export function fmtHandle(h: string): string {
  return /\s/.test(h) ? h : `@${h}`;
}

/** Primary full-width action button. */
export function PrimaryButton({
  children,
  onClick,
  disabled,
  big,
}: {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  big?: boolean;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={`btn-primary w-full rounded-xl ${big ? "py-4 text-[17px]" : "py-3.5 text-[15px]"}`}
    >
      {children}
    </button>
  );
}

/** A soft info panel. */
export function Note({ children }: { children: React.ReactNode }) {
  return (
    <div className="rounded-xl border border-line bg-surface-2/70 p-4 text-sm leading-relaxed text-ink-dim">
      {children}
    </div>
  );
}

/** Section heading inside a card. */
export function SubHead({ children, aside }: { children: React.ReactNode; aside?: React.ReactNode }) {
  return (
    <div className="mb-2.5 flex items-center justify-between gap-3">
      <h3 className="eyebrow">{children}</h3>
      {aside}
    </div>
  );
}

/** localStorage-backed set of checked sub-step ids, scoped per poster+day+task. */
export function useLocalChecks(scopeKey: string) {
  const [checks, setChecks] = useState<Set<string>>(new Set());

  useEffect(() => {
    try {
      const raw = localStorage.getItem(scopeKey);
      setChecks(raw ? new Set(JSON.parse(raw)) : new Set());
    } catch {}
  }, [scopeKey]);

  const toggle = useCallback(
    (id: string) => {
      setChecks((prev) => {
        const next = new Set(prev);
        if (next.has(id)) next.delete(id);
        else next.add(id);
        try {
          localStorage.setItem(scopeKey, JSON.stringify([...next]));
        } catch {}
        return next;
      });
    },
    [scopeKey],
  );

  return { checks, toggle };
}

/** Feature-detect "share files" (iOS Safari / Android Chrome over HTTPS). */
export function useCanShareFiles(type = "video/mp4", name = "probe.mp4") {
  const [canShare, setCanShare] = useState(false);
  useEffect(() => {
    try {
      const probe = new File([new Uint8Array(1)], name, { type });
      setCanShare(!!navigator.canShare && navigator.canShare({ files: [probe] }));
    } catch {
      setCanShare(false);
    }
  }, [type, name]);
  return canShare;
}

/**
 * Save a file to the phone's gallery: fetch it and open the native share
 * sheet ("Save Video" / "Save Image"). Where the share sheet isn't supported
 * it falls back to a plain download of the same bytes.
 *
 * Phones only allow the share sheet for a few seconds after a tap. When a big
 * file takes longer to fetch, the browser refuses the share; the fetched file
 * is then returned so the card can show a "tap to save" button, which opens
 * the sheet instantly with a fresh tap. Returns null otherwise.
 */
export async function saveToGallery(opts: {
  url: string;
  downloadUrl?: string;
  basename: string;
  fallbackType: string;
  fallbackExt: string;
  canShare: boolean;
  /** 0..1 while the file loads (big videos take a while on mobile data). */
  onProgress?: (fraction: number) => void;
}): Promise<File | null> {
  const download = () => {
    const a = document.createElement("a");
    a.href = opts.downloadUrl ?? opts.url;
    a.download = "";
    document.body.appendChild(a);
    a.click();
    a.remove();
  };
  if (!opts.canShare) {
    download();
    return null;
  }
  let file: File;
  try {
    const res = await fetch(opts.url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const total = Number(res.headers.get("content-length")) || 0;
    let blob: Blob;
    if (res.body && total && opts.onProgress) {
      // Read in chunks to show progress; the bytes are kept exactly as sent.
      const reader = res.body.getReader();
      const chunks: Uint8Array[] = [];
      let got = 0;
      for (;;) {
        const { done, value } = await reader.read();
        if (done) break;
        chunks.push(value);
        got += value.length;
        opts.onProgress(Math.min(1, got / total));
      }
      blob = new Blob(chunks as BlobPart[], { type: res.headers.get("content-type") ?? "" });
    } else {
      blob = await res.blob();
    }
    const type = blob.type || opts.fallbackType;
    file = new File([blob], `${opts.basename}.${extFor(type, opts.fallbackExt)}`, { type });
  } catch {
    download(); // fetch failed: let the browser download it directly instead
    return null;
  }
  try {
    await navigator.share({ files: [file] });
    return null;
  } catch (e) {
    // NotAllowedError: the tap "expired" while the file loaded; ask for one more tap.
    if (e instanceof DOMException && e.name === "NotAllowedError") return file;
    return null; // AbortError = the poster closed the sheet
  }
}

/** Second step of saveToGallery when the first tap expired: share the already-fetched file. */
export function TapToSave({ file, onDone }: { file: File; onDone: () => void }) {
  return (
    <PrimaryButton
      big
      onClick={async () => {
        try {
          await navigator.share({ files: [file] });
        } catch {}
        onDone();
      }}
    >
      Ready, tap to save
    </PrimaryButton>
  );
}

export function extFor(type: string, fallback: string): string {
  if (type === "image/png") return "png";
  if (type === "image/webp") return "webp";
  if (type === "image/jpeg") return "jpg";
  if (type === "video/quicktime") return "mov";
  return fallback;
}
