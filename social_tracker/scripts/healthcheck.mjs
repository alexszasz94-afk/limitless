// Container healthcheck for the scraper: healthy while its heartbeat (written
// every 10 s) is less than 3 minutes old.
import Database from "better-sqlite3";
import path from "node:path";

try {
  const db = new Database(path.join(process.env.DATA_DIR || "data", "tracker.db"), { readonly: true, fileMustExist: true });
  db.pragma("busy_timeout = 5000");
  const row = db.prepare("SELECT value FROM meta WHERE key='scheduler_heartbeat'").get();
  db.close();
  process.exit(row && Date.now() - Date.parse(row.value) < 180_000 ? 0 : 1);
} catch {
  process.exit(1);
}
