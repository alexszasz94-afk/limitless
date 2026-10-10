import { NextResponse } from "next/server";
import { getDb } from "@/lib/db";
import { keyPoolAgeSeconds, refreshKeyPool } from "@/lib/keypool";
import { apiSignedIn, unauthorized } from "@/lib/apiAuth";

export const dynamic = "force-dynamic";
export const maxDuration = 120;

let inFlight: Promise<void> | null = null;

/** "Check now" on the Keys page: checks every Apify key live (free calls, ~10 s). */
export async function POST() {
  if (!(await apiSignedIn())) return unauthorized();
  const db = getDb();
  if (keyPoolAgeSeconds(db) < 15) return NextResponse.json({ ok: true, message: "Just checked." });
  try {
    inFlight ??= refreshKeyPool(db).finally(() => {
      inFlight = null;
    });
    await inFlight;
    return NextResponse.json({ ok: true, message: "Checked every key." });
  } catch (e) {
    return NextResponse.json({ ok: false, message: e instanceof Error ? e.message : "Check failed." }, { status: 500 });
  }
}
