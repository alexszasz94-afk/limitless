import type { Platform } from "../config";
import type { Metrics } from "../db";

/**
 * Scrapers and parsers. Every actor and field below was checked live on
 * 2026-10-06 against new accounts with no posts yet and public accounts
 * with posts.
 *
 *   TikTok    discovery  clockworks~tiktok-profile-scraper
 *             refresh    clockworks~tiktok-video-scraper           (postURLs)
 *             followers  authorMeta.fans on every item; an empty profile
 *                        returns one item {authorMeta, note} instead of videos
 *   Instagram discovery  instagram-scraper~instagram-profile-reels-scraper
 *             fallback   data-slayer~instagram-profile-reels
 *             refresh    the same profile-reels scraper, crawling the profile
 *                        newest-first down to the deepest due post. It is the
 *                        only one with live counts: the data-slayer and
 *                        patient_discovery scrapers return cached numbers that
 *                        lag by hours (live 2026-10-06: 374 for over an hour
 *                        while the reel was at 828, then 890).
 *             deep posts data-slayer~instagram-post-details by URL (beyond
 *                        the crawl cap), fallback
 *                        patient_discovery~instagram-reel-analytics-by-url
 *             followers  apify~instagram-profile-scraper (followersCount),
 *                        also user.follower_count on discovery items
 *   Facebook  posts      apify~facebook-posts-scraper (page crawl, both
 *                        discovery and refresh: post URLs carry no views)
 *             followers  apify~facebook-pages-scraper (followers)
 *
 * Instagram views = ig_play_count, else play_count. Some scrapers' play_count
 * ADDS the Facebook plays of a reel shared to Facebook (seen live: 2396 =
 * 1561 IG + 835 FB) while others report the IG number only; ig_play_count is
 * the Instagram number everywhere it exists. view_count is never used (a
 * different, much smaller metric that once poisoned the old tracker).
 * TikTok views = playCount. Facebook views = viewsCount (the number on the
 * reel). Only videos are tracked: Facebook photo posts (profile picture,
 * cover) and Instagram photos carry no views and are skipped, not failed.
 */

export const ACTORS = {
  tiktokDiscovery: "clockworks~tiktok-profile-scraper",
  tiktokRefresh: "clockworks~tiktok-video-scraper",
  instagramDiscovery: "instagram-scraper~instagram-profile-reels-scraper",
  instagramDiscoveryAlt: "data-slayer~instagram-profile-reels",
  instagramRefresh: "data-slayer~instagram-post-details",
  instagramRefreshAlt: "patient_discovery~instagram-reel-analytics-by-url",
  instagramProfiles: "apify~instagram-profile-scraper",
  facebookPosts: "apify~facebook-posts-scraper",
  facebookPages: "apify~facebook-pages-scraper",
} as const;

/** Upper-bound price per item (USD), for the budget pre-check. Real cost is read back from Apify. */
export const PRICE_PER_ITEM: Record<Platform, number> = {
  tiktok: 0.004,
  instagram: 0.003,
  facebook: 0.006,
};
export const PRICE_PER_PROFILE = 0.005;

export interface ParsedPost {
  platformPostId: string;
  url: string;
  caption: string | null;
  postedAt: string | null;
  metrics: Metrics;
}

export interface Author {
  handle: string | null;
  followers: number | null;
}

export type Parsed =
  | { kind: "post"; post: ParsedPost; author: Author | null }
  | { kind: "profile"; author: Author } // an account-level record, no post (empty TikTok profile)
  | { kind: "skip"; reason: string } // a real item that is not a video post
  | { kind: "error"; reason: string };

type Obj = Record<string, unknown>;

const num = (v: unknown): number | null => (typeof v === "number" && Number.isFinite(v) ? v : null);
const str = (v: unknown): string | null => (typeof v === "string" && v.length > 0 ? v : null);
const obj = (v: unknown): Obj | null => (v && typeof v === "object" && !Array.isArray(v) ? (v as Obj) : null);

/** Unix seconds, unix ms or an ISO string -> ISO string. */
function toIso(v: unknown): string | null {
  if (typeof v === "number" && Number.isFinite(v) && v > 0) {
    const d = new Date(v > 1e12 ? v : v * 1000);
    return Number.isNaN(d.getTime()) ? null : d.toISOString();
  }
  const s = str(v);
  if (!s) return null;
  const t = Date.parse(s);
  return Number.isNaN(t) ? null : new Date(t).toISOString();
}

function errorOf(item: Obj): string | null {
  if (item.error) return typeof item.error === "string" ? item.error : JSON.stringify(item.error);
  if (item.noResults === true) return "noResults";
  if (item.errorDescription) return String(item.errorDescription);
  return null;
}

// ---------------------------------------------------------------- inputs

const TT_NO_DOWNLOADS = {
  shouldDownloadVideos: false,
  shouldDownloadCovers: false,
  shouldDownloadSubtitles: false,
  shouldDownloadSlideshowImages: false,
};

export const inputs = {
  tiktokDiscovery: (handle: string, n: number) => ({
    profiles: [handle],
    resultsPerPage: n,
    profileScrapeSections: ["videos"],
    profileSorting: "latest",
    ...TT_NO_DOWNLOADS,
  }),
  tiktokRefresh: (urls: string[]) => ({ postURLs: urls, ...TT_NO_DOWNLOADS }),
  instagramDiscovery: (handle: string, n: number) => ({ instagramUsernames: [handle], postsPerProfile: Math.max(5, n) }),
  instagramDiscoveryAlt: (handle: string, n: number) => ({ username: handle, maxResults: Math.max(5, n) }),
  instagramRefresh: (urls: string[]) => ({ postUrls: urls }),
  /**
   * patient_discovery's input schema has a DEFAULT postCode pointing at a
   * demo reel, and Apify merges defaults into every run: left empty, each
   * call also returns (and bills) that unrelated reel. The only way to
   * suppress it is to put a real shortcode there: the first URL's code goes
   * into postCode, the rest into postUrls.
   */
  instagramRefreshAlt: (urls: string[]) => {
    const [first, ...rest] = urls;
    const input: { postCode: string; postUrls?: string[] } = { postCode: instagramShortcode(first) ?? first };
    if (rest.length) input.postUrls = rest;
    return input;
  },
  instagramProfiles: (handles: string[]) => ({ usernames: handles }),
  facebookPosts: (pageUrl: string, n: number) => ({ startUrls: [{ url: pageUrl }], resultsLimit: n }),
  facebookPages: (pageUrls: string[]) => ({ startUrls: pageUrls.map((url) => ({ url })) }),
};

export function instagramShortcode(url: string): string | null {
  return url.match(/instagram\.com\/(?:[^/]+\/)?(?:p|reel|reels|tv)\/([A-Za-z0-9_-]+)/)?.[1] ?? null;
}

// ---------------------------------------------------------------- parsers

export function parseTiktok(raw: unknown): Parsed {
  const item = obj(raw);
  if (!item) return { kind: "error", reason: "not an object" };
  const err = errorOf(item);
  if (err) return { kind: "error", reason: err };
  const am = obj(item.authorMeta);
  const author: Author | null = am ? { handle: str(am.name), followers: num(am.fans) } : null;
  const id = str(item.id);
  const url = str(item.webVideoUrl);
  if (!id || !url) {
    // Profile with no videos: one {authorMeta, note} record.
    if (author && (item.note || !item.id)) return { kind: "profile", author };
    return { kind: "error", reason: "unparseable" };
  }
  const views = num(item.playCount);
  if (views === null) return { kind: "error", reason: "missing playCount" };
  return {
    kind: "post",
    post: {
      platformPostId: id,
      url,
      caption: str(item.text),
      postedAt: toIso(item.createTimeISO) ?? toIso(item.createTime),
      metrics: {
        views,
        likes: num(item.diggCount),
        comments: num(item.commentCount),
        shares: num(item.shareCount),
        saves: num(item.collectCount),
      },
    },
    author,
  };
}

export function parseInstagram(raw: unknown): Parsed {
  const item = obj(raw);
  if (!item) return { kind: "error", reason: "not an object" };
  const err = errorOf(item);
  if (err) return { kind: "error", reason: err };
  const m = obj(item.metrics) ?? item;
  // pk is the plain numeric media id; id may be "<pk>_<ownerid>".
  const rawId = str(item.pk) ?? (num(item.pk) !== null ? String(item.pk) : null) ?? str(item.id);
  const id = rawId ? rawId.split("_")[0] : null;
  const code = str(item.code) ?? str(item.shortcode) ?? str(item.shortCode);
  if (!id || !code) return { kind: "error", reason: "unparseable" };
  const views = num(m.ig_play_count) ?? num(m.play_count);
  if (views === null) {
    if (num(item.media_type) !== null && item.media_type !== 2) return { kind: "skip", reason: "not a video" };
    return { kind: "error", reason: "missing play count" };
  }
  const cap = item.caption;
  const caption = typeof cap === "string" ? cap : str(obj(cap)?.text);
  const user = obj(item.user) ?? obj(item.owner);
  return {
    kind: "post",
    post: {
      platformPostId: id,
      url: `https://www.instagram.com/p/${code}/`,
      caption: caption && caption.length ? caption : null,
      postedAt: toIso(item.taken_at) ?? toIso(item.taken_at_timestamp) ?? toIso(item.timestamp),
      metrics: {
        views,
        likes: num(m.like_count),
        comments: num(m.comment_count),
        shares: num(m.share_count) ?? num(m.reshare_count),
        saves: num(m.save_count),
      },
    },
    author: user ? { handle: str(user.username), followers: num(user.follower_count) } : null,
  };
}

export function parseFacebook(raw: unknown): Parsed {
  const item = obj(raw);
  if (!item) return { kind: "error", reason: "not an object" };
  // The posts scraper appends {"error":"no_items"} when one of its internal
  // page queries finds nothing more - routine on a page with few posts (seen
  // on new pages). Not a post and not a failure.
  if (item.error === "no_items") return { kind: "skip", reason: "no_items record" };
  const err = errorOf(item);
  if (err) return { kind: "error", reason: err };
  const id = str(item.postId) ?? str(item.id);
  const url = str(item.url) ?? str(item.topLevelUrl);
  if (!id || !url) return { kind: "error", reason: "unparseable" };
  const views = num(item.viewsCount);
  const media = Array.isArray(item.media) ? (item.media as unknown[]).map(obj) : [];
  const isVideo = item.isVideo === true || views !== null || media.some((x) => x?.__typename === "Video");
  if (!isVideo) return { kind: "skip", reason: "not a video" };
  if (views === null) return { kind: "error", reason: "missing viewsCount" };
  return {
    kind: "post",
    post: {
      platformPostId: id,
      url,
      caption: str(item.text),
      postedAt: toIso(item.time) ?? toIso(item.timestamp),
      metrics: {
        views,
        likes: num(item.likes) ?? num(item.topReactionsCount),
        comments: num(item.comments),
        shares: num(item.shares),
        saves: null, // Facebook does not expose saves
      },
    },
    author: null,
  };
}

export function parserFor(platform: Platform): (raw: unknown) => Parsed {
  if (platform === "tiktok") return parseTiktok;
  if (platform === "instagram") return parseInstagram;
  return parseFacebook;
}

/** apify~instagram-profile-scraper item -> handle + followers. */
export function parseInstagramProfile(raw: unknown): Author | null {
  const item = obj(raw);
  if (!item || errorOf(item)) return null;
  const handle = str(item.username);
  const followers = num(item.followersCount);
  return handle && followers !== null ? { handle, followers } : null;
}

/** apify~facebook-pages-scraper item -> page url/name + followers. */
export function parseFacebookPage(raw: unknown): { urls: string[]; name: string | null; followers: number } | null {
  const item = obj(raw);
  if (!item || errorOf(item)) return null;
  const followers = num(item.followers) ?? num(item.likes);
  if (followers === null) return null;
  const urls = [str(item.pageUrl), str(item.facebookUrl), str(item.inputUrl)].filter((u): u is string => !!u);
  return { urls, name: str(item.pageName), followers };
}
