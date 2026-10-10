# Deploy: the tracker on the server

First-time setup is in [`../../SETUP.md`](../../SETUP.md) (Step 8). The tracker runs on the same
server as the posting portal and adds two small containers.

## How it runs

```
GitHub (your private copy of the repo, branch main)
   │  every 2 min the server checks for new commits (the same read-only deploy key as the portal)
   ▼
/srv/social_tracker/src        git clone of the whole repo
/srv/social_tracker/app  ->    src/social_tracker (symlink) ── deploy/pull-deploy.sh rebuilds + restarts
   ├─ web      container       the dashboard, port 3100 on the Docker networks only
   └─ scraper  container       the hourly scheduler (Apify); healthcheck = its heartbeat
/srv/social_tracker/db         tracker.db + backups/ (nightly safe copies, gzipped, 14 kept)
/srv/social_tracker/app/.env   TRACKER_PASSPHRASE + APIFY_TOKENS (server only, never in git)
/etc/social_tracker/site_address   the public address

HTTPS: the portal's Caddy (container in /srv/distribution/app) imports /srv/caddy-sites/*.caddy
and sits on the shared Docker network "edge"; the tracker's web container joins "edge" as
social-tracker:3100. pull-deploy.sh writes /srv/caddy-sites/social_tracker.caddy from
deploy/social_tracker.caddy and reloads Caddy when it changes.
```

- **Deploy = push to `main`.** Within about 2 minutes the server pulls, rebuilds and restarts
  both containers. It takes a few seconds, and Caddy holds requests meanwhile. A scrape cut off
  mid-run is closed as "interrupted" and redone in the next cycle. To deploy right away:
  `/srv/social_tracker/app/deploy/pull-deploy.sh --force`. Logs: `journalctl -u social-tracker-deploy -n 50`.
- **Config edits** (`config/*.json`) arrive by push and are read live.
- **Backups:** `deploy/backup.sh` runs at 03:40 UTC (`journalctl -u social-tracker-backup`).
  For an off-site copy, create `/etc/social_tracker/restic.env` (a restic repository and its password).
- **A real domain:** point its DNS at the server's IP and write the domain into
  `/etc/social_tracker/site_address`, then run `/srv/social_tracker/app/deploy/pull-deploy.sh --force`.
  The Caddy site file is regenerated, Caddy reloads, and the certificate is fetched automatically.

## Useful commands (on the server)

```
cd /srv/social_tracker/app
docker compose ps                       # web + scraper up and healthy?
docker compose logs -f scraper          # what the scraper is doing
docker compose logs -f web
docker compose exec scraper node --import tsx scraper/once.ts   # one full pass now (same as Run now)
```

To change the Apify keys, rewrite `APIFY_TOKENS=` in `.env` (comma-separated), then run
`docker compose up -d` (both containers restart with the new list).

Health check for monitoring: `curl -u x:<passphrase> https://<address>/api/health` returns
`{"status":"ok"|"alert",...}`.
