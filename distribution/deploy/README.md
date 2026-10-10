# Deploy: the portal on the server

First-time setup is in [`../../SETUP.md`](../../SETUP.md) (Step 7). This file explains how the
running server is put together.

## How it runs

```
GitHub (your private copy of the repo, branch main)
   │  every 2 min the server checks for new commits (read-only deploy key on the server)
   ▼
/srv/distribution/src        git clone of the whole repo
/srv/distribution/app  ->    src/distribution  (symlink) ── deploy/pull-deploy.sh rebuilds + restarts
   ├─ app   container        Next.js portal on the private Docker network (port 3000)
   └─ caddy container        HTTPS on 80/443, certificates automatic, no compression
/srv/distribution/db         portal.db + backups/ (nightly safe copies, 14 kept)
/srv/distribution/content    the videos and images served to posters
/srv/distribution/app/.env   ADMIN_PASSPHRASE + SITE_ADDRESS + TIMEZONE (server only, never in git)
```

**Shared with the Social Tracker:** this Caddy also serves the tracker. The Caddyfile imports
`/srv/caddy-sites/*.caddy` (the tracker writes its own site file there), and the caddy
container joins the external Docker network `edge`, where the tracker's dashboard answers as
`social-tracker:3100`. Both are created by `deploy/server-setup.sh`. Restarting Caddy here
briefly interrupts the tracker's dashboard too (its scraper keeps running).

- **Deploy = push to `main`.** Within about 2 minutes the server pulls, rebuilds and restarts
  (a few seconds of restart; Caddy holds requests meanwhile). To deploy right away:
  `/srv/distribution/app/deploy/pull-deploy.sh`. Logs: `journalctl -u distribution-deploy -n 50`.
  If a build fails, the previous version keeps running. Fix the problem and push again, or run
  `pull-deploy.sh --force`.
- **Config edits** (`config/*.json`) also arrive by push, and the app reads them live.
  Content manifests are built into the image, so they're live once the deploy has finished.
- **Backups:** `deploy/backup.sh` runs at 03:30 UTC (`journalctl -u distribution-backup`).
  For an off-site copy of the database and the videos, create `/etc/distribution/restic.env`
  (a restic repository and its password, e.g. on a Hetzner Storage Box). Hetzner's own server
  backups, if switched on, copy everything daily.
- **Videos never pass through compression:** the Caddyfile has no `encode`, and the portal
  streams the original bytes.

## Useful commands (on the server)

```
cd /srv/distribution/app
docker compose ps                    # both containers up?
docker compose logs -f app           # portal logs
docker compose up -d caddy           # after changing SITE_ADDRESS in .env
docker compose exec -T app npm run manage -- list   # personas, posters + their links, queues
```

## Adding a persona's videos (no wipe, safe on the live portal)

1. Repo: the persona in `config/personas.json`, and its videos and captions in
   `content-manifests/<persona>.json`. Push (it deploys itself).
2. Upload the files to `/srv/distribution/content/<persona>/` exactly as the manifest names
   them (the masters byte-for-byte as exported, plus the small H.264 proxies), then
   `chown -R 1000:1000 /srv/distribution/content/<persona>`.
3. `docker compose exec -T app npm run manage -- import <persona>` checks every file first, then
   adds the new items to the end of the queue and updates the captions of existing ones. It never
   deletes anything and never touches progress.
4. A poster: `docker compose exec -T app npm run manage -- add-poster <persona> "<name>"`
   prints their link. To start someone over with the same link: `npm run manage -- reset-poster <token>`.

Never run `npm run seed` here: it wipes the database (it refuses while real personas or
progress exist).
