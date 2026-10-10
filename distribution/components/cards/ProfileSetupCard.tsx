"use client";

import { useState } from "react";
import type { Platform, PlatformInfo, ProfileStep } from "@/lib/types";
import { CheckRow, CopyButton, PrimaryButton, SubHead, TapToSave, fmtHandle, saveToGallery, useCanShareFiles, useLocalChecks } from "../ui";

const STEP_LABEL: Record<ProfileStep, string> = {
  picture: "Set the profile picture",
  cover: "Set the cover image",
  bio: "Paste the bio",
};

export default function ProfileSetupCard({
  token,
  personaId,
  bio,
  handles,
  platforms,
  scopeKey,
  onComplete,
  done,
}: {
  token: string;
  personaId: string;
  bio: string;
  handles: Record<Platform, string>;
  platforms: PlatformInfo[];
  scopeKey: string;
  onComplete: () => void;
  done: boolean;
}) {
  const { checks, toggle } = useLocalChecks(scopeKey);
  const canShare = useCanShareFiles("image/jpeg", "probe.jpg");
  const [saving, setSaving] = useState<"profile" | "cover" | null>(null);
  const [readyFile, setReadyFile] = useState<File | null>(null);
  const coverOn = platforms.filter((p) => p.profile_steps.includes("cover")).map((p) => p.tab_label);

  const save = async (kind: "profile" | "cover") => {
    if (saving) return;
    setSaving(kind);
    const url = `/api/media/${token}/${kind}/${personaId}`;
    const pending = await saveToGallery({
      url,
      downloadUrl: `${url}?download=1`,
      basename: `${personaId}_${kind}`,
      fallbackType: "image/jpeg",
      fallbackExt: "jpg",
      canShare,
    });
    setReadyFile(pending);
    setSaving(null);
  };

  return (
    <div className="flex flex-col gap-6">
      {readyFile && <TapToSave file={readyFile} onDone={() => setReadyFile(null)} />}
      <div className={`grid gap-3 ${coverOn.length ? "grid-cols-2" : "grid-cols-1"}`}>
        <button
          type="button"
          onClick={() => save("profile")}
          disabled={saving !== null}
          className="btn-quiet flex flex-col items-center gap-3 rounded-xl p-4 disabled:opacity-60"
        >
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src={`/api/media/${token}/profile/${personaId}?preview=1`}
            alt="Profile picture"
            width={80}
            height={80}
            className="h-20 w-20 rounded-full object-cover ring-2 ring-accent/40"
            decoding="async"
          />
          <span className="text-sm font-medium text-accent-soft">
            {saving === "profile" ? "Preparing…" : "Save picture to gallery"}
          </span>
        </button>
        {coverOn.length > 0 && (
          <button
            type="button"
            onClick={() => save("cover")}
            disabled={saving !== null}
            className="btn-quiet flex flex-col items-center gap-3 rounded-xl p-4 disabled:opacity-60"
          >
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img
              src={`/api/media/${token}/cover/${personaId}?preview=1`}
              alt="Cover image"
              className="h-20 w-full rounded-lg object-cover"
              decoding="async"
            />
            <span className="text-center text-sm font-medium text-accent-soft">
              {saving === "cover" ? "Preparing…" : `Save cover (${coverOn.join(", ")})`}
            </span>
          </button>
        )}
      </div>

      <div className="rounded-xl border border-line bg-surface-2/60 p-4">
        <p className="eyebrow mb-2">Bio</p>
        <p className="mb-3 text-[15px] leading-relaxed">{bio}</p>
        <CopyButton text={bio} label="Copy bio" />
      </div>

      {platforms.map((p) => (
        <div key={p.id}>
          <SubHead
            aside={handles[p.id] ? <span className="truncate text-sm text-accent-soft">{fmtHandle(handles[p.id])}</span> : null}
          >
            {p.label}
          </SubHead>
          <ul className="flex flex-col gap-3">
            {p.profile_steps.map((s) => {
              const id = `${p.id}_${s}`;
              return (
                <CheckRow key={id} checked={checks.has(id)} onToggle={() => toggle(id)}>
                  {STEP_LABEL[s]}
                </CheckRow>
              );
            })}
          </ul>
        </div>
      ))}

      {!done && <PrimaryButton onClick={onComplete}>Done, profiles set</PrimaryButton>}
    </div>
  );
}
