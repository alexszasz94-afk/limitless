import { NextResponse } from "next/server";
import { health } from "@/lib/queries";
import { getDb, monthCostUsd } from "@/lib/db";
import { loadBudget } from "@/lib/config";
import { apiSignedIn, unauthorized } from "@/lib/apiAuth";

export const dynamic = "force-dynamic";

/** For monitoring (Basic auth with the passphrase): status "ok" or "alert" + reasons. */
export async function GET() {
  if (!(await apiSignedIn())) return unauthorized();
  const h = health();
  return NextResponse.json(
    {
      status: h.ok ? "ok" : "alert",
      reasons: h.items.map((i) => `${i.level}: ${i.text}`),
      monthCostUsd: Math.round(monthCostUsd(getDb(), new Date().toISOString().slice(0, 7)) * 1000) / 1000,
      monthlyBudgetUsd: loadBudget().monthlyBudgetUsd,
    },
    { headers: { "Cache-Control": "no-store" } },
  );
}
