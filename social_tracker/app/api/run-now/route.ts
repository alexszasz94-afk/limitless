import { NextResponse } from "next/server";
import { getDb, getMeta, nowIso, setMeta } from "@/lib/db";
import { apiSignedIn, unauthorized } from "@/lib/apiAuth";

export const dynamic = "force-dynamic";

/**
 * "Run now": leaves a request in the database; the scraper process picks it
 * up within 10 s. Scraping never runs inside a web request.
 */
export async function POST() {
  if (!(await apiSignedIn())) return unauthorized();
  const db = getDb();
  if (getMeta(db, "cycle_lock")) {
    return NextResponse.json({ ok: false, message: "A scrape is already running." }, { status: 409 });
  }
  const last = getMeta(db, "last_cycle");
  if (last) {
    const at = Date.parse((JSON.parse(last) as { at: string }).at);
    const trigger = (JSON.parse(last) as { trigger?: string }).trigger;
    if (trigger === "manual" && Date.now() - at < 2 * 60 * 1000) {
      return NextResponse.json({ ok: false, message: "A manual scrape just finished. Try again in a minute." }, { status: 429 });
    }
  }
  if (!getMeta(db, "run_requested_at")) setMeta(db, "run_requested_at", nowIso());
  return NextResponse.json({ ok: true, message: "Scrape requested. It starts within 10 seconds." });
}
