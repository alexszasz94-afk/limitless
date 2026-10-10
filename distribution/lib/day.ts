/**
 * Day resolution: personal day computation, assignment freezing, manifest.
 *
 * "Day N" is personal, not calendar-based: the current day is the first day
 * whose tasks aren't all complete. Missing a calendar day slips the schedule;
 * it never skips content. Elapsed calendar days are tracked separately so
 * the admin can see drift.
 *
 * Assignments FREEZE on first open: content is picked once inside a
 * transaction and written to `assignments` + `day_opens`. Refreshing re-reads
 * the same rows. A day that has been opened is never reshuffled.
 */
import {
  db,
  getPersona,
  getQueuedContent,
  getAssignments,
  getProgress,
  getCompletedCountByDay,
  getContentItem,
  getPostedPlatforms,
  setContentStatus,
  getOpenedDays,
  dayCompletedAt,
  dayOpenedAt,
} from "./db";
import {
  tasksForDay,
  getPrivacyConfig,
  getCreateAccountsConfig,
  getPlatforms,
  oneDayPerCalendarDay,
} from "./config";
import { generateWarmup } from "./warmup";
import { statFile } from "./storage";
import type { Poster, DayManifest, DayTask, ResolvedTask, ContentKind } from "./types";

export const CONTENT_TASK_KIND: Record<string, ContentKind> = {
  post_reel: "reel",
  post_story: "story",
  add_highlight: "highlight_cover",
};

/** YYYY-MM-DD of a moment in the poster's timezone. */
function localDate(when: Date, timeZone: string): string {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: timeZone || "UTC",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(when);
}

/**
 * The task list of a day. A day that has been opened keeps the list it was
 * frozen with, so editing schedule.json never reshuffles a day in progress;
 * days not opened yet follow the current schedule.
 */
export function dayTasks(
  poster: Poster,
  day: number,
  opened: Map<number, string | null> = getOpenedDays(poster.id),
): DayTask[] {
  const frozen = opened.get(day);
  if (frozen) {
    try {
      return JSON.parse(frozen) as DayTask[];
    } catch {
      /* fall through to the live schedule */
    }
  }
  return tasksForDay(day, poster.persona_id);
}

export interface DayPosition {
  /** The day the poster is on. */
  day: number;
  /** Every task of `day` is done and the next day opens tomorrow. */
  waitForTomorrow: boolean;
}

/**
 * The poster's current day: the first day whose tasks aren't all complete.
 * With one_day_per_calendar_day (default) a day finished today keeps the
 * poster on it until the next calendar day in their timezone.
 */
export function dayPosition(poster: Poster): DayPosition {
  const completed = getCompletedCountByDay(poster.id);
  const opened = getOpenedDays(poster.id);
  const gate = oneDayPerCalendarDay();
  const today = localDate(new Date(), poster.timezone);
  let d = 1;
  for (; d < 10000; d++) {
    const n = dayTasks(poster, d, opened).length;
    if (n === 0) break;
    if ((completed.get(d) ?? 0) < n) break;
    // Day d is complete. Hold here if it was finished today and the next
    // day hasn't been opened yet.
    if (gate && !opened.has(d + 1)) {
      const at = dayCompletedAt(poster.id, d);
      if (at && localDate(new Date(at), poster.timezone) === today) {
        return { day: d, waitForTomorrow: true };
      }
    }
  }
  return { day: d, waitForTomorrow: false };
}

export function currentDay(poster: Poster): number {
  return dayPosition(poster).day;
}

/** Calendar days since start_date in the poster's timezone (0 = start day). */
export function elapsedDays(poster: Poster): number {
  const t = localDate(new Date(), poster.timezone);
  const today = Date.UTC(+t.slice(0, 4), +t.slice(5, 7) - 1, +t.slice(8, 10));
  const s = poster.start_date;
  const start = Date.UTC(+s.slice(0, 4), +s.slice(5, 7) - 1, +s.slice(8, 10));
  return Math.max(0, Math.round((today - start) / 86400000));
}

/** Pick the next item of a queue, keeping clips apart (see freezeDay). */
function pickItem(posterId: string, personaId: string, kind: ContentKind, day: number, todayClips: Set<string>) {
  const d = db();
  const prevClips = new Set<string>(
    (
      d
        .prepare(
          `SELECT ci.source_clip_id AS c FROM assignments a
           JOIN content_items ci ON ci.id = a.content_item_id
           WHERE a.poster_id = ? AND a.day = ? AND ci.source_clip_id IS NOT NULL`,
        )
        .all(posterId, day - 1) as Array<{ c: string }>
    ).map((r) => r.c),
  );
  const queue = getQueuedContent(personaId, kind);
  // Prefer clips not used today or yesterday; a same-day repeat is worse
  // than a next-day repeat, so degrade in that order.
  const clean = queue.find(
    (c) => !c.source_clip_id || (!todayClips.has(c.source_clip_id) && !prevClips.has(c.source_clip_id)),
  );
  const okToday = queue.find((c) => !c.source_clip_id || !todayClips.has(c.source_clip_id));
  return clean ?? okToday ?? queue[0] ?? null;
}

/**
 * Freeze the day for (poster, day) on first open: store its task list and
 * pick its content. Content slots that found an empty queue are retried on
 * every later open, so refilling a queue unblocks the poster.
 */
function freezeDay(poster: Poster, day: number): void {
  const d = db();
  const opened = d.prepare("SELECT 1 FROM day_opens WHERE poster_id = ? AND day = ?");

  const tx = d.transaction(() => {
    const isNew = !opened.get(poster.id, day);
    const tasks = isNew ? tasksForDay(day, poster.persona_id) : dayTasks(poster, day);
    const existing = getAssignments(poster.id, day);
    const todayClips = new Set<string>();
    for (const id of existing.values()) {
      const c = id ? getContentItem(id) : null;
      if (c?.source_clip_id) todayClips.add(c.source_clip_id);
    }
    const upsert = d.prepare(
      `INSERT INTO assignments (poster_id, day, task_index, content_item_id) VALUES (?, ?, ?, ?)
       ON CONFLICT (poster_id, day, task_index) DO UPDATE SET content_item_id = excluded.content_item_id`,
    );

    tasks.forEach((task, index) => {
      const kind = CONTENT_TASK_KIND[task.type];
      if (existing.has(index) && (existing.get(index) || !kind)) return; // already settled
      if (!kind) {
        upsert.run(poster.id, day, index, null);
        return;
      }
      const item = pickItem(poster.id, poster.persona_id, kind, day, todayClips);
      if (item) {
        if (item.source_clip_id) todayClips.add(item.source_clip_id);
        setContentStatus(item.id, "assigned");
      }
      upsert.run(poster.id, day, index, item?.id ?? null); // null: queue empty, the card says so
    });

    if (isNew) {
      d.prepare("INSERT INTO day_opens (poster_id, day, opened_at, tasks_json) VALUES (?, ?, ?, ?)").run(
        poster.id,
        day,
        new Date().toISOString(),
        JSON.stringify(tasks),
      );
    }
  });
  tx();
}

/** Build the full manifest the poster UI renders. Freezes the day if needed. */
export function openDay(poster: Poster): DayManifest {
  const { day, waitForTomorrow } = dayPosition(poster);
  freezeDay(poster, day);

  const persona = getPersona(poster.persona_id);
  if (!persona) throw new Error("Persona missing for poster");

  const tasks = dayTasks(poster, day);
  const assignments = getAssignments(poster.id, day);
  const progress = getProgress(poster.id, day);

  const resolved: ResolvedTask[] = tasks.map((task, index) => {
    const base: ResolvedTask = {
      index,
      type: task.type,
      params: task.params ?? {},
      completed: progress.has(index),
      content: null,
    };
    if (task.type === "warmup") {
      base.warmup = generateWarmup(poster.id, persona, day);
    }
    if (CONTENT_TASK_KIND[task.type]) {
      const contentId = assignments.get(index) ?? null;
      const item = contentId ? getContentItem(contentId) : null;
      if (item) {
        base.content = {
          id: item.id,
          kind: item.kind,
          duration_seconds: item.duration_seconds,
          captions: item.captions,
          posted_platforms: getPostedPlatforms(poster.id, item.id),
          variant_platforms: Object.keys(item.variants ?? {}),
          suppress_pinned_comment: item.suppress_pinned_comment,
          size_bytes: statFile(item.master_path)?.size ?? null,
        };
      }
    }
    return base;
  });

  return {
    posterName: poster.name,
    personaName: persona.name,
    handles: persona.handles,
    bio: persona.bio,
    pinnedComment: persona.pinned_comment,
    personaId: persona.id,
    day,
    elapsedDays: elapsedDays(poster),
    tasks: resolved,
    allDone: resolved.length > 0 && resolved.every((t) => t.completed),
    waitForTomorrow,
    oneDayPerCalendarDay: oneDayPerCalendarDay(),
    openedAt: dayOpenedAt(poster.id, day) ?? "",
  };
}

/** Static config content the cards need. */
export function cardConfigs() {
  return {
    privacy: getPrivacyConfig(),
    createAccounts: getCreateAccountsConfig(),
    platforms: getPlatforms(),
  };
}
