#!/usr/bin/env bash
# One-time setup of a fresh Ubuntu 24.04 server for the portal (run it FIRST:
# it also installs Docker and the shared Caddy that the Social Tracker uses).
# Run as root:
#   bash server-setup.sh <repo-ssh-url> <site-address> <timezone> [volume-mount-path]
#     <repo-ssh-url>   your PRIVATE copy of this repo, e.g. git@github.com:you/your-repo.git
#     <site-address>   e.g. portal.1-2-3-4.nip.io (your server IP with dashes), later a real domain
#     <timezone>       the posters' timezone, e.g. Europe/London (decides when a "day" starts)
#     [volume-mount]   where an extra disk for videos is mounted (e.g. /mnt/HC_Volume_123456);
#                      omit to keep videos on the main disk
# Safe to run again: every step checks before it changes anything.
#
# Layout: the repo is cloned to /srv/distribution/src and /srv/distribution/app
# points at its distribution/ folder, so every other script uses /srv/distribution/app.
set -euo pipefail
USAGE="usage: server-setup.sh <repo-ssh-url> <site-address> <timezone> [volume-mount-path]"
REPO="${1:?$USAGE}"
SITE="${2:?$USAGE}"
TZONE="${3:?$USAGE}"
VOLUME="${4:-}"
BASE=/srv/distribution

[[ -e "/usr/share/zoneinfo/$TZONE" ]] || { echo "Unknown timezone: $TZONE (example: Europe/London)"; exit 1; }

echo "== packages, automatic security updates"
export DEBIAN_FRONTEND=noninteractive
apt-get update -q
apt-get install -y -q ca-certificates curl git unattended-upgrades restic sqlite3 ffmpeg
dpkg-reconfigure -f noninteractive unattended-upgrades
cat >/etc/apt/apt.conf.d/52distribution-reboot <<'CONF'
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-Time "04:30";
CONF

echo "== docker"
if ! command -v docker >/dev/null; then
  curl -fsSL https://get.docker.com | sh
fi
systemctl enable --now docker
# keep container logs small
mkdir -p /etc/docker
[[ -f /etc/docker/daemon.json ]] || cat >/etc/docker/daemon.json <<'CONF'
{ "log-driver": "local", "log-opts": { "max-size": "20m", "max-file": "3" } }
CONF
systemctl restart docker

echo "== swap (2 GB) so builds never run out of memory"
if ! swapon --show | grep -q /swapfile; then
  fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
  grep -q '^/swapfile' /etc/fstab || echo '/swapfile none swap sw 0 0' >>/etc/fstab
fi

echo "== SSH: keys only"
cat >/etc/ssh/sshd_config.d/10-distribution.conf <<'CONF'
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin prohibit-password
CONF
systemctl reload ssh || systemctl reload sshd

echo "== shared Caddy plumbing for other apps on this server (Social Tracker)"
docker network inspect edge >/dev/null 2>&1 || docker network create edge
mkdir -p /srv/caddy-sites

echo "== folders"
mkdir -p "$BASE/db/backups" /etc/distribution
if [[ -n "$VOLUME" ]]; then
  mkdir -p "$VOLUME/content"
  ln -sfn "$VOLUME/content" "$BASE/content"
else
  mkdir -p "$BASE/content"
fi
chown -R 1000:1000 "$BASE/db" "$VOLUME${VOLUME:+/content}" "$BASE/content" 2>/dev/null || true

echo "== read-only GitHub deploy key for this server (used by both apps)"
mkdir -p /root/.ssh && chmod 700 /root/.ssh
if [[ ! -f /root/.ssh/repo_pull ]]; then
  ssh-keygen -t ed25519 -N "" -C "server-pull@$(hostname)" -f /root/.ssh/repo_pull -q
fi
cat >/root/.ssh/config <<'CONF'
Host github.com
  IdentityFile /root/.ssh/repo_pull
  IdentitiesOnly yes
CONF
ssh-keyscan -t ed25519 github.com >>/root/.ssh/known_hosts 2>/dev/null
sort -u -o /root/.ssh/known_hosts /root/.ssh/known_hosts

if ! git ls-remote "$REPO" >/dev/null 2>&1; then
  echo
  echo "ADD THIS READ-ONLY DEPLOY KEY TO GitHub (your repo > Settings > Deploy keys > Add deploy key,"
  echo "'Allow write access' OFF). It is also saved in /root/.ssh/repo_pull.pub:"
  cat /root/.ssh/repo_pull.pub
  echo "Then run this script again with the same arguments."
  exit 2
fi

echo "== code"
if [[ ! -d "$BASE/src/.git" ]]; then
  git clone --quiet "$REPO" "$BASE/src"
fi
ln -sfn "$BASE/src/distribution" "$BASE/app"
cd "$BASE/app"
if [[ ! -f .env ]]; then
  PASS=$(openssl rand -base64 24 | tr -d '/+=' | cut -c1-24)
  printf 'ADMIN_PASSPHRASE=%s\nSITE_ADDRESS=%s\nTIMEZONE=%s\n' "$PASS" "$SITE" "$TZONE" >.env
  chmod 600 .env
  echo "Admin passphrase (also in $BASE/app/.env): $PASS"
else
  sed -i "s|^SITE_ADDRESS=.*|SITE_ADDRESS=$SITE|" .env
  if grep -q '^TIMEZONE=' .env; then
    sed -i "s|^TIMEZONE=.*|TIMEZONE=$TZONE|" .env
  else
    echo "TIMEZONE=$TZONE" >>.env
  fi
fi

echo "== services"
cp deploy/distribution-*.service deploy/distribution-*.timer /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now distribution-deploy.timer distribution-backup.timer

echo "== first start"
./deploy/pull-deploy.sh --force
docker compose ps
echo "Done: https://$SITE  (admin page: https://$SITE/admin)"
