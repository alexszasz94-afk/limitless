import { type Db, type DailyRow, type PostRow, type SnapshotRow, listSnapshots, replacePostDaily, setPostDerived } from "./db";
import { localDate, nextLocalMidnight } from "./time";

/**
 * Derived numbers, all rebuilt from raw snapshots (idempotent):
 *  - post_daily: views gained per local day. The first snapshot is a
 *    baseline (no row); a gap between two snapshots is spread over the days
 *    it covers in proportion to time and flagged 'spread' when it spans more
 *    than 36 h; negative deltas (platform revisions) are kept.
 *  - views 24 h / 7 d after posting: read off the snapshot curve, with the
 *    post's publish time counting as 0 views. Null until a snapshot past that
 *    moment exists, so a young post is never compared on a partial number.
 */

const OBSERVED_MAX_SPAN_MS = 36 * 3600 * 1000;
const HOUR_MS = 3600 * 1000;

/** Fraction of [t0, t1] falling on each local date. */
export function dateFractions(t0: number, t1: number, tz?: string): Map<string, number> {
  const out = new Map<string, number>();
  const total = t1 - t0;
  if (total <= 0) {
    out.set(localDate(t1, tz), 1);
    return out;
  }
  let cursor = t0;
  while (cursor < t1) {
    let sliceEnd = Math.min(nextLocalMidnight(cursor, tz), t1);
    // Zones whose clocks jump at midnight can make "next midnight" not move: step past it.
    if (sliceEnd <= cursor) sliceEnd = Math.min(cursor + 3600_000, t1);
    const key = localDate(cursor, tz);
    out.set(key, (out.get(key) ?? 0) + (sliceEnd - cursor) / total);
    cursor = sliceEnd;
  }
  return out;
}

const round2 = (n: number) => Math.round(n * 100) / 100;

export function computeDailyRows(snapshots: SnapshotRow[], tz?: string): DailyRow[] {
  if (snapshots.length < 2) return [];
  type Acc = {
    views: number;
    likes: number | null;
    comments: number | null;
    shares: number | null;
    saves: number | null;
    spread: boolean;
  };
  const days = new Map<string, Acc>();
  const add = (cur: number | null, delta: number | null, frac: number) => (delta === null ? cur : (cur ?? 0) + delta * frac);

  for (let i = 1; i < snapshots.length; i++) {
    const prev = snapshots[i - 1];
    const cur = snapshots[i];
    const t0 = Date.parse(prev.observed_at);
    const t1 = Date.parse(cur.observed_at);
    const d = (a: number | null, b: number | null) => (a !== null && b !== null ? b - a : null);
    const delta = {
      views: d(prev.views, cur.views),
      likes: d(prev.likes, cur.likes),
      comments: d(prev.comments, cur.comments),
      shares: d(prev.shares, cur.shares),
      saves: d(prev.saves, cur.saves),
    };
    const spread = t1 - t0 > OBSERVED_MAX_SPAN_MS;
    for (const [date, frac] of dateFractions(t0, t1, tz)) {
      let a = days.get(date);
      if (!a) {
        a = { views: 0, likes: null, comments: null, shares: null, saves: null, spread: false };
        days.set(date, a);
      }
      if (delta.views !== null) a.views += delta.views * frac;
      a.likes = add(a.likes, delta.likes, frac);
      a.comments = add(a.comments, delta.comments, frac);
      a.shares = add(a.shares, delta.shares, frac);
      a.saves = add(a.saves, delta.saves, frac);
      if (spread) a.spread = true;
    }
  }
  const postId = snapshots[0].post_id;
  return [...days.entries()]
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([date, a]) => ({
      post_id: postId,
      date,
      views: round2(a.views),
      likes: a.likes === null ? null : round2(a.likes),
      comments: a.comments === null ? null : round2(a.comments),
      shares: a.shares === null ? null : round2(a.shares),
      saves: a.saves === null ? null : round2(a.saves),
      quality: a.spread ? "spread" : "observed",
    }));
}

/**
 * Views `hours` after publishing, interpolated on the snapshot curve. The
 * publish moment is a known point (0 views). Returns null when no snapshot
 * reaches that moment yet, when the publish time is unknown, or when the two
 * points around that moment are more than `maxSpanHours` apart (a post first
 * seen days after it went up would otherwise get an invented early curve).
 */
export function viewsAfter(
  postedAt: string | null,
  snapshots: SnapshotRow[],
  hours: number,
  maxSpanHours = Math.max(36, hours * 0.6),
): number | null {
  if (!postedAt) return null;
  const t0 = Date.parse(postedAt);
  if (Number.isNaN(t0)) return null;
  const target = t0 + hours * HOUR_MS;
  const pts: Array<[number, number]> = [[t0, 0]];
  for (const s of snapshots) {
    if (s.views === null) continue;
    const t = Date.parse(s.observed_at);
    if (t >= t0) pts.push([t, s.views]);
  }
  if (pts[pts.length - 1][0] < target) return null;
  for (let i = 1; i < pts.length; i++) {
    const [ta, va] = pts[i - 1];
    const [tb, vb] = pts[i];
    if (tb >= target) {
      if (tb === ta) return vb;
      if (tb - ta > maxSpanHours * HOUR_MS) return null;
      return Math.round(va + ((vb - va) * (target - ta)) / (tb - ta));
    }
  }
  return null;
}

/** Rebuild everything derived for one post from its snapshots. */
export function recomputePost(db: Db, post: Pick<PostRow, "id" | "posted_at">): void {
  const snaps = listSnapshots(db, post.id);
  replacePostDaily(db, post.id, computeDailyRows(snaps));
  setPostDerived(db, post.id, {
    latest: snaps[snaps.length - 1],
    views24h: viewsAfter(post.posted_at, snaps, 24),
    views7d: viewsAfter(post.posted_at, snaps, 24 * 7),
  });
}

export function recomputePostById(db: Db, postId: number): void {
  const post = db.prepare(`SELECT id, posted_at FROM posts WHERE id=?`).get(postId) as
    Pick<PostRow, "id" | "posted_at"> | undefined;
  if (post) recomputePost(db, post);
}
