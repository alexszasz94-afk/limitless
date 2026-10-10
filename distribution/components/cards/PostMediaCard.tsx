"use client";

import { useEffect, useRef, useState } from "react";
import type { Platform, PlatformInfo, ResolvedTask } from "@/lib/types";
import { send } from "@/lib/outbox";
import { Check, CopyButton, Note, PrimaryButton, TapToSave, fmtSize, saveToGallery, useCanShareFiles } from "../ui";

/**
 * The core card: proxy preview, save-to-gallery, per-platform captions and a
 * single "posted" toggle per video (logs every platform at once). Used by
 * post_reel, post_story and add_highlight: same shape, different queue.
 */
export default function PostMediaCard({
  token,
  content,
  platforms,
  onComplete,
  done,
  pinnedComment,
}: {
  token: string;
  content: NonNullable<ResolvedTask["content"]> | null;
  platforms: PlatformInfo[];
  pinnedComment?: string;
  onComplete: () => void;
  done: boolean;
}) {
  const ids = platforms.map((p) => p.id);
  const [tab, setTab] = useState<Platform>(ids[0] ?? "");
  const [posted, setPosted] = useState<Set<Platform>>(new Set(content?.posted_platforms ?? []));
  const [ready, setReady] = useState(false);
  const [saving, setSaving] = useState(false);
  const [progress, setProgress] = useState<number | null>(null);
  const [readyFile, setReadyFile] = useState<File | null>(null);
  const isImage = content?.kind === "highlight_cover";
  const canShare = useCanShareFiles(isImage ? "image/jpeg" : "video/mp4", isImage ? "probe.jpg" : "probe.mp4");
  const readyTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const allPosted = ids.length > 0 && ids.every((p) => posted.has(p));

  // Marking the video posted completes the task.
  useEffect(() => {
    if (allPosted && !done) onComplete();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [allPosted]);

  // Per-platform file override: preview and save follow the selected tab.
  const tabHasVariant = !!content?.variant_platforms?.includes(tab);
  const qs = tabHasVariant ? `?platform=${encodeURIComponent(tab)}` : "";
  const proxyUrl = content ? `/api/media/${token}/proxy/${content.id}${qs}` : "";
  const masterUrl = content ? `/api/media/${token}/master/${content.id}${qs}` : "";

  // Show the skeleton while a (new) file loads, but never forever: some
  // browsers don't fire loadeddata with preload="metadata", so also reveal
  // on metadata/canplay and after 2.5 s at the latest.
  useEffect(() => {
    setReady(false);
    setReadyFile(null);
    if (readyTimer.current) clearTimeout(readyTimer.current);
    readyTimer.current = setTimeout(() => setReady(true), 2500);
    return () => {
      if (readyTimer.current) clearTimeout(readyTimer.current);
    };
  }, [proxyUrl]);

  if (!content) {
    return (
      <div className="flex flex-col gap-3">
        <Note>No video is ready for this task yet. Tell your manager, then check again once they say it&apos;s added.</Note>
        <button type="button" onClick={() => location.reload()} className="btn-quiet rounded-xl py-3 text-sm font-medium">
          Check again
        </button>
      </div>
    );
  }

  const hasAnyVariant = content.variant_platforms.length > 0;
  const tabInfo = platforms.find((p) => p.id === tab);
  const labelOf = (id: string) => platforms.find((p) => p.id === id)?.tab_label ?? id;
  const reveal = () => setReady(true);

  // Pinned comment in two parts: the text is posted and pinned first, then
  // the link goes in as a reply (links in comments get cut otherwise). The
  // link is the last URL in the string.
  const showPin = !!pinnedComment && !!tabInfo?.pinned_comment;
  const pinLink = (pinnedComment?.match(/https?:\/\/\S+/g) ?? []).pop() ?? null;
  const pinText = pinnedComment ? (pinLink ? pinnedComment.replace(pinLink, "").trim() : pinnedComment) : "";

  const save = async () => {
    if (saving) return;
    setSaving(true);
    setProgress(null);
    const pending = await saveToGallery({
      url: masterUrl,
      basename: `${content.id}${tabHasVariant ? `_${tab}` : ""}`,
      fallbackType: isImage ? "image/jpeg" : "video/mp4",
      fallbackExt: isImage ? "jpg" : "mp4",
      canShare,
      onProgress: (f) => setProgress(Math.floor(f * 100)),
    });
    setReadyFile(pending);
    setSaving(false);
    setProgress(null);
  };

  // One tap per video: posted everywhere (post_log still gets a row per platform).
  const togglePostedAll = () => {
    const target = !allPosted;
    setPosted(target ? new Set(ids) : new Set());
    send(`/api/poster/${token}/postlog`, { contentItemId: content.id, platforms: ids, posted: target });
  };

  // Same caption, same file and no pinned comment on every platform: one
  // caption box with one copy button instead of tabs that all show the same.
  const anyPin = !!pinnedComment && platforms.some((p) => p.pinned_comment);
  const sameEverywhere =
    !hasAnyVariant && !anyPin && ids.every((p) => (content.captions[p] ?? "") === (content.captions[ids[0]] ?? ""));
  const caption = content.captions[sameEverywhere ? ids[0] : tab] ?? "";

  return (
    <div className="flex flex-col gap-4">
      {/* Preview: PROXY ONLY. The master is never streamed for preview. */}
      <div
        className="relative mx-auto w-full overflow-hidden rounded-xl border border-line bg-black"
        style={{ aspectRatio: "9/16", maxHeight: 440, maxWidth: 248 }}
      >
        {!ready && <div className="skeleton pointer-events-none absolute inset-0" />}
        {isImage ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img key={proxyUrl} src={proxyUrl} alt="Preview" className="h-full w-full object-contain" onLoad={reveal} onError={reveal} />
        ) : (
          <video
            key={proxyUrl}
            // #t=0.001 makes iOS Safari paint the first frame instead of a blank player.
            src={`${proxyUrl}#t=0.001`}
            controls
            playsInline
            preload="metadata"
            className="h-full w-full object-contain"
            onLoadedMetadata={reveal}
            onLoadedData={reveal}
            onCanPlay={reveal}
            onError={reveal}
          />
        )}
      </div>

      {readyFile ? (
        <TapToSave file={readyFile} onDone={() => setReadyFile(null)} />
      ) : (
      <PrimaryButton onClick={save} disabled={saving} big>
        <span className="inline-flex items-center justify-center gap-2">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
            <path d="M12 4v11M7 10l5 5 5-5M5 20h14" />
          </svg>
          {saving
            ? progress !== null
              ? `Loading video… ${progress}%`
              : "Preparing…"
            : `Save ${isImage ? "image" : "video"}${hasAnyVariant ? ` for ${labelOf(tab)}` : ""} to gallery`}
        </span>
      </PrimaryButton>
      )}
      <p className="-mt-1 text-center text-xs text-ink-faint">
        {!tabHasVariant && content.size_bytes ? `Original · ${fmtSize(content.size_bytes)} · ` : ""}
        Never post a screen recording.
      </p>

      {hasAnyVariant && (
        <p className="rounded-xl border border-accent/25 bg-accent/10 p-3 text-center text-xs leading-relaxed text-accent-pale">
          {content.variant_platforms.map(labelOf).join(" and ")} {content.variant_platforms.length > 1 ? "get" : "gets"} its
          own version of this video. The preview and the save button follow the tab you pick below, so save each
          platform&apos;s own file.
        </p>
      )}

      {/* Platform tabs: captions (and variant files) differ per platform */}
      {!sameEverywhere && (
      <div role="tablist" className="flex gap-1 rounded-xl border border-line bg-surface-2/70 p-1">
        {platforms.map((p) => (
          <button
            key={p.id}
            role="tab"
            aria-selected={tab === p.id}
            onClick={() => setTab(p.id)}
            className={`min-w-0 flex-1 truncate rounded-lg px-1 py-2 text-[13px] font-medium transition-colors ${
              tab === p.id ? "bg-surface-3 text-ink shadow-[inset_0_1px_0_rgba(255,255,255,0.05)]" : "text-ink-dim"
            }`}
          >
            {p.tab_label}
          </button>
        ))}
      </div>
      )}

      <div className="rounded-xl border border-line bg-surface-2/60 p-4">
        <p className="eyebrow mb-2">
          Caption · {sameEverywhere ? (ids.length > 1 ? "same on every platform" : labelOf(ids[0])) : labelOf(tab)}
        </p>
        <p className="whitespace-pre-wrap text-[15px] leading-relaxed">
          {caption || <span className="text-ink-faint">No caption for this platform.</span>}
        </p>
        {caption && (
          <div className="mt-3">
            <CopyButton text={caption} label="Copy caption" />
          </div>
        )}
      </div>

      {showPin && (
        <div className="rounded-xl border border-line bg-surface-2/60 p-4">
          <p className="eyebrow mb-2">Pinned comment · {labelOf(tab)}</p>
          <ol className="mb-3 ml-4 list-decimal space-y-1 text-sm leading-relaxed text-ink-dim">
            <li>
              Post <span className="text-ink">comment 1</span> (no link) under your video.
            </li>
            <li>
              <span className="text-ink">Press and hold</span> it, then tap <span className="text-ink">Pin</span>.
            </li>
            {pinLink && (
              <li>
                <span className="text-ink">Reply</span> to the pinned comment with <span className="text-ink">comment 2</span> (the link).
              </li>
            )}
          </ol>
          <div className="rounded-lg bg-bg/70 p-3">
            <p className="mb-1 text-xs font-medium text-ink-faint">1 · The comment</p>
            <p className="whitespace-pre-wrap text-sm leading-relaxed">{pinText}</p>
            <div className="mt-2">
              <CopyButton text={pinText} label="Copy comment" />
            </div>
          </div>
          {pinLink && (
            <div className="mt-3 rounded-lg bg-bg/70 p-3">
              <p className="mb-1 text-xs font-medium text-ink-faint">2 · The link (reply to the pinned comment)</p>
              <p className="break-all text-sm leading-relaxed">{pinLink}</p>
              <div className="mt-2">
                <CopyButton text={pinLink} label="Copy link" />
              </div>
            </div>
          )}
        </div>
      )}

      <div
        className={`flex items-center gap-3 rounded-xl border px-4 py-3.5 transition-colors ${
          allPosted ? "border-accent/50 bg-accent/10" : "border-line-strong"
        }`}
      >
        <Check checked={allPosted} onToggle={togglePostedAll} size={26} label="Posted on every platform" />
        <button type="button" onClick={togglePostedAll} className="flex-1 text-left text-[15px] font-medium">
          Posted on {platforms.length === 1 ? platforms[0].tab_label : `all ${platforms.length} platforms`}
          <span className="block text-xs font-normal text-ink-faint">
            {platforms.map((p) => p.tab_label).join(" · ")}
          </span>
        </button>
      </div>
    </div>
  );
}
