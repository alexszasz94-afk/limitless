import type { Metadata } from "next";
import { getPosterByToken } from "@/lib/db";
import { openDay, cardConfigs } from "@/lib/day";
import DayView from "@/components/DayView";
import Mark from "@/components/Mark";

export const dynamic = "force-dynamic";

export async function generateMetadata({ params }: { params: Promise<{ token: string }> }): Promise<Metadata> {
  const { token } = await params;
  return {
    title: "Today",
    // Installing from this page opens this poster's day, not the home page.
    manifest: getPosterByToken(token) ? `/d/${token}/manifest.webmanifest` : undefined,
  };
}

export default async function PosterDay({ params }: { params: Promise<{ token: string }> }) {
  const { token } = await params;
  const poster = getPosterByToken(token);

  if (!poster) {
    return (
      <main className="flex min-h-dvh flex-col items-center justify-center gap-5 px-8">
        <Mark size={56} />
        <p className="text-center text-sm text-ink-dim">This link isn&apos;t active. Check with your manager.</p>
      </main>
    );
  }

  return <DayView token={token} manifest={openDay(poster)} configs={cardConfigs()} />;
}
