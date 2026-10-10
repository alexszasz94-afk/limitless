#!/usr/bin/env bash
# Nightly backup (distribution-backup.timer):
#  1. a consistent copy of the SQLite database (safe while the app runs:
#     SQLite's online backup, never a plain file copy of a WAL database);
#  2. if /etc/distribution/restic.env exists, the database copies and all
#     videos go to the off-site restic repository (e.g. a Hetzner Storage Box).
set -euo pipefail
APP_DIR=/srv/distribution/app
DB_DIR=/srv/distribution/db
KEEP_LOCAL=14
STAMP=$(date -u +%Y-%m-%d_%H%M)

mkdir -p "$DB_DIR/backups"
cd "$APP_DIR"
docker compose exec -T app node -e "
  const Database = require('better-sqlite3');
  const db = new Database('/data/db/portal.db', { readonly: true });
  db.backup('/data/db/backups/portal_$STAMP.db')
    .then(() => { console.log('db backup ok: portal_$STAMP.db'); db.close(); })
    .catch((e) => { console.error(e); process.exit(1); });
"
# keep the newest $KEEP_LOCAL local copies
ls -1t "$DB_DIR"/backups/portal_*.db 2>/dev/null | tail -n +$((KEEP_LOCAL + 1)) | xargs -r rm -f

if [[ -f /etc/distribution/restic.env ]]; then
  set -a; source /etc/distribution/restic.env; set +a
  restic backup --quiet --tag nightly "$DB_DIR/backups" /srv/distribution/content
  restic forget --quiet --prune --keep-daily 14 --keep-weekly 8 --keep-monthly 6
  echo "off-site backup ok"
else
  echo "off-site backup skipped (no /etc/distribution/restic.env yet)"
fi
