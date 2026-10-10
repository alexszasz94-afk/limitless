/**
 * Platform ids come from config/platforms.json (instagram, tiktok, facebook
 * today). They are plain strings so a platform can be added or
 * dropped in config without touching code.
 */
export type Platform = string;

export type ProfileStep = "picture" | "cover" | "bio";

export interface PlatformInfo {
  id: Platform;
  /** Full name, used in headings ("Facebook Page"). */
  label: string;
  /** Short name for the caption tabs ("Facebook"). */
  tab_label: string;
  /** Profile sub-steps for the profile_setup card. */
  profile_steps: ProfileStep[];
  /** Shows the persona's pinned comment on this platform's tab. */
  pinned_comment?: boolean;
}

export interface Competitor {
  platform: Platform;
  handle: string;
  note?: string;
}

export interface Persona {
  id: string;
  name: string;
  handles: Record<Platform, string>;
  bio: string;
  profile_image_path: string;
  cover_image_path: string;
  competitors: Competitor[];
  keywords: string[];
  voice_notes: string;
  pinned_comment: string;
}

export interface Poster {
  id: string;
  name: string;
  token: string;
  persona_id: string;
  start_date: string; // YYYY-MM-DD
  timezone: string;
}

export type ContentKind = "reel" | "story" | "highlight_cover";
export type ContentStatus = "queued" | "assigned" | "posted" | "retired";

/** Per-platform file override (e.g. Facebook gets the same video with a different final CTA). */
export interface ContentVariant {
  master_path: string;
  proxy_path: string;
}

export interface ContentItem {
  id: string;
  persona_id: string;
  kind: ContentKind;
  master_path: string;
  proxy_path: string;
  source_clip_id: string | null;
  duration_seconds: number | null;
  captions: Record<Platform, string>;
  queue_order: number;
  status: ContentStatus;
  /** Platform → file override. Empty for single-video personas. */
  variants: Partial<Record<Platform, ContentVariant>>;
  /** Hide the persona's pinned comment for this item (e.g. no product placement). */
  suppress_pinned_comment: boolean;
}

export type TaskType =
  | "create_accounts"
  | "privacy_lockdown"
  | "warmup"
  | "profile_setup"
  | "post_reel"
  | "post_story"
  | "add_highlight";

export interface DayTask {
  type: TaskType;
  params?: Record<string, unknown>;
}

export interface WarmupPlan {
  perAccountMinutes: number;
  behaviors: string[];
  accounts: Competitor[];
  keywords: string[];
}

/** One resolved task as sent to the poster UI. */
export interface ResolvedTask {
  index: number;
  type: TaskType;
  params: Record<string, unknown>;
  completed: boolean;
  content?: {
    id: string;
    kind: ContentKind;
    duration_seconds: number | null;
    captions: Record<Platform, string>;
    posted_platforms: Platform[];
    /** Platforms that have their OWN video/proxy file (e.g. a Facebook cut with a different CTA). */
    variant_platforms: Platform[];
    /** True when this item's card should NOT show the pinned-comment box. */
    suppress_pinned_comment: boolean;
    /** Size of the original file in bytes (shown next to the save button). */
    size_bytes: number | null;
  } | null;
  warmup?: WarmupPlan;
}

export interface DayManifest {
  posterName: string;
  personaName: string;
  handles: Record<Platform, string>;
  bio: string;
  pinnedComment: string;
  personaId: string;
  day: number;
  elapsedDays: number;
  tasks: ResolvedTask[];
  allDone: boolean;
  /** All of today's tasks are done and the next day opens tomorrow. */
  waitForTomorrow: boolean;
  /** Schedule setting: the next day opens on the next calendar day at the earliest. */
  oneDayPerCalendarDay: boolean;
  /** When this day was first opened. Part of the phone's local checklist key, so a day
   *  that is reset and opened again starts with clean ticks. */
  openedAt: string;
}
