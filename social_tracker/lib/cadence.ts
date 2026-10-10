import { type CadenceFile, loadCadence } from "./config";
import { type Db, type PostRow, listActivePosts, setPostSurge } from "./db";
import { localDate, localHour } from "./time";

/**
 * Adaptive refresh cadence:
 *  - age tiers from config/cadence.json (12 h -> daily -> weekly -> monthly)
 *  - optional per-platform ceiling (platformOverrides.<platform>.maxEveryHours)
 *  - surge: a post whose latest daily views beat deltaMultiple x its account's
 *    median is re-checked every promoteEveryHours for durationHours
 *  - daily-and-slower tiers fire only at the anchor hour, so every day's pull
 *    happens at the same local time and day-to-day numbers compare fairly
 */

const HOUR_MS = 3600 * 1000;
const DAY_MS = 24 * HOUR_MS;

export function postAgeDays(post: PostRow, now: number): number {
  return (now - Date.parse(post.posted_at ?? post.first_seen_at)) / DAY_MS;
}

export function intervalHoursFor(post: PostRow, cadence: CadenceFile, now: number): number {
  if (cadence.surge.enabled && post.surge_until && Date.parse(post.surge_until) > now) {
    return cadence.surge.promoteEveryHours;
  }
  const age = postAgeDays(post, now);
  let hours = cadence.refreshTiers[cadence.refreshTiers.length - 1].everyHours;
  for (const tier of cadence.refreshTiers) {
    if (tier.maxAgeDays === null || age <= tier.maxAgeDays) {
      hours = tier.everyHours;
      break;
    }
  }
  const cap = cadence.platformOverrides?.[post.platform]?.maxEveryHours;
  if (cap && hours > cap) hours = cap;
  return hours;
}

/**
 * Due now? Sub-daily tiers: as soon as the interval has passed (with 10 min
 * slack so an hourly tick a little early does not skip a slot). Daily and
 * slower: only in the anchor hour, interval passed minus 1 h slack.
 */
export function isDue(post: PostRow, cadence: CadenceFile, now: number): boolean {
  if (!post.last_refreshed_at) return true;
  const hours = intervalHoursFor(post, cadence, now);
  const elapsed = now - Date.parse(post.last_refreshed_at);
  if (hours < 24) return elapsed >= hours * HOUR_MS - 10 * 60 * 1000;
  if (localHour(now) !== cadence.anchorHourLocal) return false;
  return elapsed >= (hours - 1) * HOUR_MS;
}

export function duePosts(db: Db, now: number): PostRow[] {
  const cadence = loadCadence();
  return listActivePosts(db).filter((p) => isDue(p, cadence, now));
}

/** After a cycle: promote surging posts, expire finished surges. */
export function applySurgeRules(db: Db, now: number): number {
  const cadence = loadCadence();
  if (!cadence.surge.enabled) return 0;
  const since = localDate(now - 7 * DAY_MS);
  const rows = db
    .prepare(
      `SELECT pd.post_id, p.account_id, pd.date, pd.views
       FROM post_daily pd JOIN posts p ON p.id=pd.post_id
       WHERE pd.date>=? AND pd.quality='observed' AND p.active=1`,
    )
    .all(since) as Array<{ post_id: number; account_id: number; date: string; views: number }>;

  const latest = new Map<number, { date: string; views: number; accountId: number }>();
  const perAccount = new Map<number, number[]>();
  for (const r of rows) {
    const cur = latest.get(r.post_id);
    if (!cur || r.date > cur.date) latest.set(r.post_id, { date: r.date, views: r.views, accountId: r.account_id });
    const arr = perAccount.get(r.account_id) ?? [];
    arr.push(r.views);
    perAccount.set(r.account_id, arr);
  }

  let promoted = 0;
  const until = new Date(now + cadence.surge.durationHours * HOUR_MS).toISOString();
  for (const [postId, l] of latest) {
    const values = (perAccount.get(l.accountId) ?? []).slice().sort((a, b) => a - b);
    if (values.length < 4) continue; // not enough history to call a surge
    const median = values[Math.floor(values.length / 2)];
    if (median > 0 && l.views > cadence.surge.deltaMultiple * median) {
      setPostSurge(db, postId, until);
      promoted++;
    }
  }
  db.prepare(`UPDATE posts SET surge_until=NULL WHERE surge_until IS NOT NULL AND surge_until<=?`).run(
    new Date(now).toISOString(),
  );
  return promoted;
}
