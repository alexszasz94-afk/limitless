#!/usr/bin/env bash
# Auto-deploy: runs every 2 minutes (distribution-deploy.timer). If GitHub's
# main branch has a new commit, update the code and rebuild/restart the app.
# The server only holds a READ-ONLY deploy key; nothing on GitHub can reach it.
set -euo pipefail
APP_DIR=/srv/distribution/app
exec 9>/run/distribution-deploy.lock
flock -n 9 || exit 0 # a deploy is already running

cd "$APP_DIR"
git fetch --quiet origin main
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)
if [[ "$LOCAL" == "$REMOTE" && "${1:-}" != "--force" ]]; then
  exit 0
fi

echo "deploy: $LOCAL -> $REMOTE"
git reset --hard --quiet origin/main
docker compose build --pull app
docker compose up -d --remove-orphans
docker image prune -f >/dev/null
echo "deploy: done $(git log -1 --format='%h %s')"
