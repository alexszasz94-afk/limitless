import { NextResponse } from "next/server";
import { getDb, getMeta } from "@/lib/db";
import { apiSignedIn, unauthorized } from "@/lib/apiAuth";

export const dynamic = "force-dynamic";

/** Scraper state for the Run-now button: requested / running / idle. */
export async function GET() {
  if (!(await apiSignedIn())) return unauthorized();
  const db = getDb();
  const lock = getMeta(db, "cycle_lock");
  const last = getMeta(db, "last_cycle");
  return NextResponse.json(
    {
      requested: !!getMeta(db, "run_requested_at"),
      running: !!lock,
      lastCycleAt: last ? (JSON.parse(last) as { at: string }).at : null,
      heartbeat: getMeta(db, "scheduler_heartbeat"),
    },
    { headers: { "Cache-Control": "no-store" } },
  );
}
