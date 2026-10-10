import { NextRequest, NextResponse } from "next/server";
import { getPosterByToken, markProgress, unmarkProgress, isDayOpened, dayOpenedAt, getAssignments } from "@/lib/db";
import { currentDay, dayTasks, CONTENT_TASK_KIND } from "@/lib/day";

/**
 * Mark / unmark one task of a day. Only a day the poster has actually opened
 * and is on (or already finished) can be written, and only a task index that
 * exists on that day, so a stray or replayed request can never skip ahead.
 */
export async function POST(req: NextRequest, { params }: { params: Promise<{ token: string }> }) {
  const { token } = await params;
  const poster = getPosterByToken(token);
  if (!poster) return NextResponse.json({ error: "not found" }, { status: 404 });

  let body: { day?: unknown; taskIndex?: unknown; completed?: unknown; at?: unknown };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "bad request" }, { status: 400 });
  }
  const day = Number(body.day);
  const taskIndex = Number(body.taskIndex);
  if (!Number.isInteger(day) || !Number.isInteger(taskIndex) || day < 1 || taskIndex < 0) {
    return NextResponse.json({ error: "bad request" }, { status: 400 });
  }
  if (
    !isDayOpened(poster.id, day) ||
    taskIndex >= dayTasks(poster, day).length ||
    day > currentDay(poster)
  ) {
    return NextResponse.json({ error: "not allowed" }, { status: 409 });
  }

  // A posting task can't be completed while no video has been handed out for it.
  const task = dayTasks(poster, day)[taskIndex];
  if (body.completed !== false && CONTENT_TASK_KIND[task.type] && !getAssignments(poster.id, day).get(taskIndex)) {
    return NextResponse.json({ error: "no content yet" }, { status: 409 });
  }

  if (body.completed === false) {
    unmarkProgress(poster.id, day, taskIndex);
  } else {
    // Record the time of the tap (sent by the phone, so an offline tick that
    // syncs after midnight still counts for the evening it was done), clamped
    // between the day's first open and now so it can't be faked forward/back.
    const now = Date.now();
    const opened = Date.parse(dayOpenedAt(poster.id, day) ?? "") || now;
    const tapped = typeof body.at === "string" ? Date.parse(body.at) : NaN;
    const at = Number.isFinite(tapped) ? Math.min(now, Math.max(opened, tapped)) : now;
    markProgress(poster.id, day, taskIndex, new Date(at).toISOString());
  }
  return NextResponse.json({ ok: true });
}
