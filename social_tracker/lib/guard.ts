import { type Db, type Metrics, deleteSnapshot, insertAnomaly, insertSnapshot, latestSnapshot } from "./db";
import { recomputePostById } from "./rollup";

/**
 * Snapshot plausibility guard + auto-repair (learned the hard way on an
 * earlier tracker, where an Instagram scraper once returned a ~6x smaller metric for
 * every item and the bad snapshots sank the totals by 530K).
 *
 * Layer 1, guardedInsertSnapshot: a views value more than 30% below the
 * previous snapshot (previous >= 200) is refused and logged as an anomaly.
 * If the same low value (+-10%) is seen 3 times over >= 24 h it is accepted
 * as a real platform revision: a real drop is delayed about a day, never lost.
 *
 * Layer 2, sweepPoisonedSnapshots: a snapshot more than 30% below BOTH its
 * neighbours (each >= 200) is garbage (views never dip and recover). It is
 * deleted, the post is recomputed, and an anomaly is logged.
 */

const DROP_RATIO = 0.7;
const MIN_REF_VIEWS = 200;
const ACCEPT_MIN_OBSERVATIONS = 3;
const ACCEPT_MIN_SPAN_MS = 24 * 3600 * 1000;
const ACCEPT_TOLERANCE = 0.1;
const SWEEP_LOOKBACK_DAYS = 14;

export function guardedInsertSnapshot(
  db: Db,
  s: { postId: number; runId: number | null; observedAt: string; metrics: Metrics; raw: unknown },
): boolean {
  const prev = latestSnapshot(db, s.postId);
  const v = s.metrics.views;
  if (prev && prev.views !== null && v !== null && prev.views >= MIN_REF_VIEWS && v < prev.views * DROP_RATIO) {
    const sightings = db
      .prepare(
        `SELECT CAST(json_extract(detail, '$.views') AS REAL) AS v,
                COALESCE(json_extract(detail, '$.observedAt'), created_at) AS at
         FROM anomalies WHERE post_id=? AND kind='rejected_drop' ORDER BY id DESC LIMIT 10`,
      )
      .all(s.postId) as Array<{ v: number; at: string }>;
    const similar = sightings.filter((r) => Math.abs(r.v - v) <= Math.max(v, 1) * ACCEPT_TOLERANCE);
    const spanMs = similar.length ? Date.parse(s.observedAt) - Math.min(...similar.map((r) => Date.parse(r.at))) : 0;
    const accepted = similar.length + 1 >= ACCEPT_MIN_OBSERVATIONS && spanMs >= ACCEPT_MIN_SPAN_MS;
    insertAnomaly(db, {
      postId: s.postId,
      runId: s.runId,
      kind: accepted ? "accepted_drop" : "rejected_drop",
      detail: { views: v, prevViews: prev.views, observedAt: s.observedAt },
    });
    if (!accepted) {
      console.warn(`[guard] post ${s.postId}: refused implausible views drop ${prev.views} -> ${v}`);
      return false;
    }
    console.warn(`[guard] post ${s.postId}: accepted views drop ${prev.views} -> ${v} (seen ${similar.length + 1}x)`);
  }
  insertSnapshot(db, s);
  return true;
}

export function sweepPoisonedSnapshots(db: Db): number {
  const since = new Date(Date.now() - SWEEP_LOOKBACK_DAYS * 86_400_000).toISOString();
  const rows = db
    .prepare(
      `SELECT s.id, s.post_id, s.views,
         (SELECT views FROM snapshots WHERE post_id=s.post_id
            AND (observed_at<s.observed_at OR (observed_at=s.observed_at AND id<s.id))
            ORDER BY observed_at DESC, id DESC LIMIT 1) AS pv,
         (SELECT views FROM snapshots WHERE post_id=s.post_id
            AND (observed_at>s.observed_at OR (observed_at=s.observed_at AND id>s.id))
            ORDER BY observed_at ASC, id ASC LIMIT 1) AS nv
       FROM snapshots s WHERE s.observed_at>=? AND s.views IS NOT NULL`,
    )
    .all(since) as Array<{ id: number; post_id: number; views: number; pv: number | null; nv: number | null }>;
  const bad = rows.filter(
    (r) =>
      r.pv !== null &&
      r.nv !== null &&
      r.pv >= MIN_REF_VIEWS &&
      r.nv >= MIN_REF_VIEWS &&
      r.views < r.pv * DROP_RATIO &&
      r.views < r.nv * DROP_RATIO,
  );
  for (const r of bad) {
    deleteSnapshot(db, r.id);
    insertAnomaly(db, {
      postId: r.post_id,
      runId: null,
      kind: "swept",
      detail: { snapshotId: r.id, views: r.views, prevViews: r.pv, nextViews: r.nv },
    });
    recomputePostById(db, r.post_id);
    console.warn(`[sweeper] post ${r.post_id}: deleted poisoned snapshot ${r.id} (${r.views} between ${r.pv} and ${r.nv})`);
  }
  return bad.length;
}
