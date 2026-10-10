/**
 * The long-running scraper (its own container on the server, `npm run
 * scraper` locally). A cycle starts at minute 0 of every hour; the cadence
 * config decides what is actually due. "Run now" on the Runs page leaves a
 * request in the database, picked up here within 10 seconds. A heartbeat in
 * the database lets the web app and the container healthcheck see that this
 * process is alive.
 */
import { loadEnv } from "./env";
loadEnv();

import { getDb, getMeta, setMeta, nowIso } from "../lib/db";
import { runCycle, type Trigger } from "./engine";

const db = getDb();
let running = false;
let lastHourKey = "";

async function cycle(trigger: Trigger) {
  if (running) return;
  running = true;
  try {
    await runCycle(trigger);
  } catch (e) {
    console.error("[scheduler] cycle failed:", e);
  } finally {
    running = false;
  }
}

function tick() {
  setMeta(db, "scheduler_heartbeat", nowIso());
  if (running) return;
  const requested = getMeta(db, "run_requested_at");
  if (requested) {
    setMeta(db, "run_requested_at", null);
    void cycle("manual");
    return;
  }
  // First idle tick of each new hour (a cycle still running at :00 just delays it).
  const hourKey = new Date().toISOString().slice(0, 13);
  if (hourKey !== lastHourKey) {
    lastHourKey = hourKey;
    void cycle("schedule");
  }
}

console.log(`[scheduler] started ${nowIso()} - hourly cycles, run-now requests every 10 s`);
// A freshly started scheduler catches up straight away (new accounts get backfilled).
lastHourKey = new Date().toISOString().slice(0, 13);
void cycle("schedule");
setInterval(tick, 10_000);

for (const sig of ["SIGTERM", "SIGINT"] as const) {
  process.on(sig, () => {
    console.log(`[scheduler] ${sig} - exiting${running ? " (a cycle was running; its runs are closed on next start)" : ""}`);
    try {
      if (running) setMeta(db, "cycle_lock", null);
    } finally {
      process.exit(0);
    }
  });
}
