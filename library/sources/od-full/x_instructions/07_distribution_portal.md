# 07 — Distribution (the posting portal)

**What it is:** a small web app (Next.js) for a **team of posters**. Each poster gets one
secret link (`/d/<token>`) that shows **today's tasks and nothing else**: which accounts to
create, how to warm them up, and which videos to post with which captions. Videos are saved
to the phone byte-for-byte, never re-compressed. The owner sees everyone's progress at
`/admin`. It was built because posting ~50 videos a day needs a team, plus one system that
tells each poster exactly what to do.

**Folder:** `x_systems/distribution/`. Its own docs are complete; read them in this order:
`README.md` (how it works, config, commands) → `CLAUDE.md` (rules for an AI working on it)
→ `deploy/README.md` (hosting).

## Run it locally (try it first)

```
cd x_systems/distribution
npm install
copy .env.example .env      # set ADMIN_PASSPHRASE (macOS/Linux: cp)
npm run seed                # DEMO personas + posters, prints poster links
npm run dev                 # http://localhost:3000  (/admin for the dashboard)
```

Requires Node.js 20.9+. `npm run seed` **wipes the database** and is for demo data only.

## Make it yours

1. **Personas** (one per product/brand identity): `config/personas.json` holds the handles
   per platform, bio, the competitor accounts posters visit during warm-up, and keywords.
   The Swanlift persona is the original owner's real setup. Keep it as an example or
   replace it.
2. **Content:** `content-manifests/<persona>.json` lists the videos in posting order with
   their caption and file paths. The files go in `content/<persona>/` (masters exactly as
   exported from `videos_to_post/`, plus small H.264 proxies; the ffmpeg line is in
   README.md). This copy has no `content/` folder: build it from `videos_to_post/`.
3. **Schedule:** `config/schedule.json` (day 1 accounts + warm-up, day 2 warm-up +
   profiles, then 3 reels a day; tune it). Platforms: `config/platforms.json`.
4. Load real data with `npm run manage -- import <persona>` and
   `npm run manage -- add-poster <persona> "Name"` (prints the poster's link). Never use
   `seed` on real data.

## Host it (needed for real posters)

The original ran on a small Ubuntu VPS (Hetzner CX23, about $10/month) with Docker Compose +
Caddy (automatic HTTPS). The server pulls new commits from a **private GitHub repo** every
2 minutes, so a push to `main` deploys itself. `deploy/README.md` and
`deploy/server-setup.sh` set up a fresh server end to end. Your user needs their own:

- a GitHub account + private repo for this folder (set `REPO=` in `deploy/server-setup.sh`),
- a VPS (any Ubuntu 24.04 host works; Hetzner is what was used),
- an SSH key for the server and a read-only deploy key for the repo (the setup script
  prints it),
- a domain or a free `nip.io` name for the server's IP (`SITE_ADDRESS` in the server's `.env`),
- `ADMIN_PASSPHRASE` in the server's `.env`.

The original server address, repo name and keys were removed from this copy (`<server-ip>`,
`<server-name>`, `<github-account>` in the docs). The Social Tracker shares this server's
Caddy (`08_social_tracker.md`).
