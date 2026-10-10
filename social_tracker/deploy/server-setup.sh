#!/usr/bin/env bash
# One-time setup of the Social Tracker on the server that already runs the
# Distribution portal (run distribution/deploy/server-setup.sh FIRST: it
# installs Docker, the shared Caddy and the GitHub deploy key used here too).
# Run as root:
#   bash server-setup.sh <repo-ssh-url> <site-address>
#     <repo-ssh-url>   the same private repo, e.g. git@github.com:you/your-repo.git
#     <site-address>   e.g. tracker.1-2-3-4.nip.io (your server IP with dashes), later a real domain
# Safe to run again: every step checks before it changes anything.
#
# Layout: the repo is cloned to /srv/social_tracker/src and /srv/social_tracker/app
# points at its social_tracker/ folder, so every other script uses /srv/social_tracker/app.
set -euo pipefail
USAGE="usage: server-setup.sh <repo-ssh-url> <site-address>"
REPO="${1:?$USAGE}"
SITE="${2:?$USAGE}"
BASE=/srv/social_tracker

command -v docker >/dev/null || { echo "Docker missing: run distribution/deploy/server-setup.sh first"; exit 1; }
git ls-remote "$REPO" >/dev/null 2>&1 || { echo "Cannot read $REPO: run distribution/deploy/server-setup.sh first (it sets up the deploy key)"; exit 1; }

echo "== shared Caddy plumbing (network + site folder)"
docker network inspect edge >/dev/null 2>&1 || docker network create edge
mkdir -p /srv/caddy-sites

echo "== folders"
mkdir -p "$BASE/db/backups" /etc/social_tracker
chown -R 1000:1000 "$BASE/db"
printf '%s\n' "$SITE" >/etc/social_tracker/site_address

echo "== code"
[[ -d "$BASE/src/.git" ]] || git clone --quiet "$REPO" "$BASE/src"
ln -sfn "$BASE/src/social_tracker" "$BASE/app"
cd "$BASE/app"
if [[ ! -f .env && -f /etc/social_tracker/app.env ]]; then
  # prepared beforehand (passphrase + APIFY_TOKENS), see deploy/README.md
  install -m 600 /etc/social_tracker/app.env .env
fi
if [[ ! -f .env ]]; then
  PASS=$(openssl rand -base64 24 | tr -d '/+=' | cut -c1-24)
  printf 'TRACKER_PASSPHRASE=%s\nAPIFY_TOKENS=\n' "$PASS" >.env
  chmod 600 .env
  echo "Dashboard passphrase (also in $BASE/app/.env): $PASS"
fi
grep -q '^APIFY_TOKENS=.\+' .env || echo "NOTE: APIFY_TOKENS in $BASE/app/.env is empty - put the Apify key there, then: cd $BASE/app && docker compose up -d"

echo "== services"
cp deploy/social-tracker-*.service deploy/social-tracker-*.timer /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now social-tracker-deploy.timer social-tracker-backup.timer

echo "== first start"
rm -f /srv/caddy-sites/social_tracker.caddy # forces the site file + Caddy reload on this deploy
./deploy/pull-deploy.sh --force
docker compose ps
echo "Done: https://$SITE"
