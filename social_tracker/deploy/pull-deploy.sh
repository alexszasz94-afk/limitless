#!/usr/bin/env bash
# Auto-deploy: runs every 2 minutes (social-tracker-deploy.timer). If GitHub's
# main branch has a new commit, update the code, rebuild and restart both
# containers. The server holds only a READ-ONLY deploy key.
set -euo pipefail
APP_DIR=/srv/social_tracker/app
SITE_FILE=/srv/caddy-sites/social_tracker.caddy
exec 9>/run/social-tracker-deploy.lock
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
docker compose build --pull web
docker compose up -d --remove-orphans
docker image prune -f >/dev/null

# Keep the Caddy site file in step with deploy/social_tracker.caddy.
if [[ -f /etc/social_tracker/site_address ]]; then
  SITE=$(tr -d '[:space:]' </etc/social_tracker/site_address)
  NEW=$(sed "s|__SITE_ADDRESS__|$SITE|" deploy/social_tracker.caddy)
  if [[ ! -f "$SITE_FILE" || "$NEW" != "$(cat "$SITE_FILE")" ]]; then
    printf '%s\n' "$NEW" >"$SITE_FILE"
    CADDY=$(docker ps -q --filter volume=/etc/caddy/sites | head -n1)
    if [[ -n "$CADDY" ]]; then
      docker exec "$CADDY" caddy reload --config /etc/caddy/Caddyfile && echo "deploy: caddy reloaded"
    else
      echo "deploy: WARNING no Caddy container mounts /etc/caddy/sites - the dashboard is not reachable from outside"
    fi
  fi
fi
echo "deploy: done $(git log -1 --format='%h %s')"
