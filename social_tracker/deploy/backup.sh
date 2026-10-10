#!/usr/bin/env bash
# Nightly backup (social-tracker-backup.timer):
#  1. a consistent copy of the SQLite database (SQLite's online backup, safe
#     while both containers run; never a plain copy of a WAL database), gzipped;
#  2. if /etc/social_tracker/restic.env exists, the copies also go to the
#     off-site restic repository (e.g. a Hetzner Storage Box).
set -euo pipefail
APP_DIR=/srv/social_tracker/app
DB_DIR=/srv/social_tracker/db
KEEP_LOCAL=14
STAMP=$(date -u +%Y-%m-%d_%H%M)

mkdir -p "$DB_DIR/backups"
chown 1000:1000 "$DB_DIR/backups"
cd "$APP_DIR"
docker compose exec -T web node -e "
  const Database = require('better-sqlite3');
  const db = new Database('/data/db/tracker.db', { readonly: true });
  db.backup('/data/db/backups/tracker_$STAMP.db')
    .then(() => { console.log('db backup ok: tracker_$STAMP.db'); db.close(); })
    .catch((e) => { console.error(e); process.exit(1); });
"
# compressed (snapshots compress ~5x), then keep the newest $KEEP_LOCAL
gzip -f "$DB_DIR/backups/tracker_$STAMP.db"
ls -1t "$DB_DIR"/backups/tracker_*.db.gz 2>/dev/null | tail -n +$((KEEP_LOCAL + 1)) | xargs -r rm -f

if [[ -f /etc/social_tracker/restic.env ]]; then
  set -a; source /etc/social_tracker/restic.env; set +a
  restic backup --quiet --tag social-tracker "$DB_DIR/backups"
  restic forget --quiet --prune --tag social-tracker --keep-daily 14 --keep-weekly 8 --keep-monthly 6
  echo "off-site backup ok"
else
  echo "off-site backup skipped (no /etc/social_tracker/restic.env yet)"
fi
