import { type Platform, PLATFORM_LABEL } from "@/lib/config";

export const PLATFORM_COLOR: Record<Platform, string> = {
  instagram: "var(--color-ig)",
  tiktok: "var(--color-tt)",
  facebook: "var(--color-fb)",
};

export function PlatformDot({ platform, size = 8 }: { platform: Platform; size?: number }) {
  return <span className="dot" style={{ background: PLATFORM_COLOR[platform], width: size, height: size }} aria-hidden="true" />;
}

/** Colour dot + name: identity never rests on colour alone. */
export function PlatformTag({ platform, short = false }: { platform: Platform; short?: boolean }) {
  const label = PLATFORM_LABEL[platform];
  return (
    <span className="inline-flex items-center gap-1.5 whitespace-nowrap text-ink-dim">
      <PlatformDot platform={platform} />
      <span>{short ? { instagram: "IG", tiktok: "TT", facebook: "FB" }[platform] : label}</span>
    </span>
  );
}
