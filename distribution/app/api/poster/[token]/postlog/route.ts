import { NextRequest, NextResponse } from "next/server";
import {
  getPosterByToken,
  getContentItem,
  logPost,
  unlogPost,
  getPostedPlatforms,
  setContentStatus,
  isAssignedTo,
} from "@/lib/db";
import { platformIds } from "@/lib/config";

/**
 * Mark a content item posted / not posted on one or more platforms.
 * Body: { contentItemId, platforms: string[] , posted?: boolean }
 * (a single { platform } is accepted too). The item must be one that was
 * assigned to this poster. When every platform is logged the item is
 * marked 'posted'.
 */
export async function POST(req: NextRequest, { params }: { params: Promise<{ token: string }> }) {
  const { token } = await params;
  const poster = getPosterByToken(token);
  if (!poster) return NextResponse.json({ error: "not found" }, { status: 404 });

  let body: { contentItemId?: unknown; platform?: unknown; platforms?: unknown; posted?: unknown };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "bad request" }, { status: 400 });
  }

  const all = platformIds();
  const requested = Array.isArray(body.platforms) ? body.platforms : [body.platform];
  const platforms = requested.filter((p): p is string => typeof p === "string" && all.includes(p));
  const contentItemId = typeof body.contentItemId === "string" ? body.contentItemId : "";
  const item = contentItemId ? getContentItem(contentItemId) : null;

  if (!platforms.length || platforms.length !== requested.length || !item) {
    return NextResponse.json({ error: "bad request" }, { status: 400 });
  }
  if (item.persona_id !== poster.persona_id || !isAssignedTo(poster.id, item.id)) {
    return NextResponse.json({ error: "not found" }, { status: 404 });
  }

  for (const p of platforms) {
    if (body.posted === false) unlogPost(poster.id, item.id, p);
    else logPost(poster.id, item.id, p);
  }

  const posted = getPostedPlatforms(poster.id, item.id);
  const complete = all.every((p) => posted.includes(p));
  if (complete && item.status !== "posted") setContentStatus(item.id, "posted");
  if (!complete && item.status === "posted") setContentStatus(item.id, "assigned");
  return NextResponse.json({ ok: true, posted });
}
