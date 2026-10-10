# Distribution: posting portal

A private daily checklist for the posting team. Every poster gets one secret link
(`/d/<token>`) that shows **today and nothing else**: which accounts to create, how to
warm them up, and which videos to post with which captions. The owner sees everyone's
progress at `/admin`.

Setting it up on a server: [`../SETUP.md`](../SETUP.md). Server details: [`deploy/README.md`](deploy/README.md).

## Run it on this computer (optional, for testing)

Needs Node.js 20.9 or newer (22 LTS recommended).

```bash
cd distribution
npm install
cp .env.example .env        # then set ADMIN_PASSPHRASE in .env
npm run seed                # DEMO personas + posters (seed-assets/), prints the poster links
npm run dev                 # http://localhost:3000
```

Open a printed `/d/<token>` link for a poster's day, and `http://localhost:3000/admin` for
the dashboard. `npm run build && npm start` runs the production build locally.

## How a day works

- **Day N is personal.** A poster's day only moves on when every task of the previous day
  is done, so a missed day pushes the schedule back and never skips content. The admin page
  shows drift (personal day vs. days since start).
- **Several days in one sitting** (`one_day_per_calendar_day: false` in `schedule.json`, the
  default): a finished day shows "Start day N+1" right away, so a poster with momentum can do
  many days in a row. The admin shows "N days ahead". Set it to `true` to hold every poster to
  one day per calendar day ("Day N+1 opens tomorrow").
- **A day freezes on first open:** its videos and its task list. Refreshing never reshuffles,
  and editing `schedule.json` only changes days nobody has opened yet.
- **Empty queue:** a posting task with no video left shows "No video is ready yet" and can't be
  completed. Once new videos are added, it picks one up on the next open ("Check again").
- **Clip spacing:** two items cut from the same clip are never given out on the same day, and
  are avoided on consecutive days.
- **Nothing a poster taps is lost.** Ticks are saved on the phone first and sent in order. They
  are retried while offline (the "Offline, will sync" pill) and sent on the next open.
- **Home-screen install** from a poster's page opens straight on that poster's day.
- When a day is finished, its tasks collapse and a finish screen shows.
- A "day" starts at midnight in the posters' timezone (`TIMEZONE` in `.env`).

## What a non-developer edits: `config/`

The app reads these files on every request, so changes need no rebuild and no restart.

| File | What it holds |
|---|---|
| `schedule.json` | The day templates (fixed days + `repeat_from`), warm-up behaviours and minutes, per-persona `overrides`. Default: day 1 accounts + warm-up, day 2 warm-up + profiles, days 3-4 warm-up + 3 reels, from day 5 on 3 reels. |
| `platforms.json` | The platforms and their tab order (Instagram, TikTok, Facebook), the profile steps per platform, and which tab shows the pinned comment. |
| `personas.json` | The brands (personas): handles per platform, bio, competitor accounts and keywords for the warm-up, pinned comment. Loaded with `npm run manage -- import <persona>`. |
| `create_accounts.json` | The account-creation steps per platform. |
| `privacy_lockdown.json` | The privacy checklist. Update `verified_on` when an item is re-checked in the live app. |

Task types available for `schedule.json`: `create_accounts`, `privacy_lockdown`, `warmup`,
`profile_setup`, `post_reel`, `post_story`, `add_highlight`.

## Personas and their videos: `npm run manage`

`content-manifests/<persona>.json` lists a persona's videos in posting order with their
captions (one string = the same caption on every platform), plus its profile picture and
cover. The files sit in `content/<persona>/` (on the server `/srv/distribution/content/<persona>/`).

```bash
npm run manage -- import <persona>             # persona + videos, checks every file first
npm run manage -- add-poster <persona> "Name"  # prints the poster's link
npm run manage -- list                         # personas, posters, links, queues
npm run manage -- remove-persona <persona>     # refuses while it has progress (--force)
npm run manage -- reset-poster <token>         # back to day 1, same link, videos re-queued
```

On the server, each of these runs as `docker compose exec -T app npm run manage -- ...` in
`/srv/distribution/app`. `import` never deletes anything and never touches progress: run it
again after adding videos to the manifest. The demo personas used by `npm run seed` live in
`seed-assets/demo_personas.json`.

## Video quality: the one rule

Masters are **never transcoded or modified**. Storage is a byte bucket: the save button
downloads the original file, and the in-page player only ever uses the small proxy file.
You can prove it any time:

```bash
npm run verify-integrity -- content/<persona>/reels/video_1.mp4 --url "https://<portal address>/api/media/<token>/master/<contentId>"
```

Use a content item that has already been handed to that poster (a poster link only serves
its own assigned videos; anything else answers 404).

Proxies are made outside the app, small and in H.264 so every browser plays them:
`ffmpeg -i master.mp4 -vf "scale=540:-2,format=yuv420p" -c:v libx264 -crf 28 -maxrate 1500k
-bufsize 3000k -c:a aac -b:a 64k -movflags +faststart master_proxy.mp4`.
A content item can carry a different file per platform (`variants_json`, e.g. a Facebook cut
with another final call to action): `{"facebook": {"master_path": "...", "proxy_path": "..."}}`.

## Safety

- `npm run seed` **wipes the database** (demo data only). It refuses once there is any poster
  progress or a real persona; only `npm run seed -- --force` overrides that. Never run it on
  the live portal: real data goes in with `npm run manage`.
- The server only accepts ticks for a day the poster has opened and reached, and "posted"
  marks only for videos actually handed to that poster.
- Admin: passphrase from `.env`, timing-safe check, slowed wrong attempts, httpOnly cookie,
  log-out button. Poster links are 96-bit random tokens; pages send `no-referrer`,
  `noindex` and `X-Frame-Options: DENY`.
- `.env`, `data/` (the database) and `content/` (the videos) are never committed.

## Folder map

```
app/            pages: /d/[token] (poster day), /admin, API routes (progress, postlog, media)
components/     DayView + one card per task type (components/cards/)
lib/            db.ts (SQLite), storage.ts (files), config.ts, day.ts (day logic), outbox.ts (offline sync)
config/         everything above that a non-developer changes
content-manifests/  per persona: its videos in posting order + captions (npm run manage)
scripts/        manage.ts (real data, no wipe), seed.ts (demo), verify-integrity.ts
seed-assets/    demo personas + placeholder videos and images used by the seed
public/icons/   app icons (home-screen install)
data/           portal.db - created on first run (not in git)
content/        the videos and images served to posters (not in git)
Dockerfile      production image
docker-compose.yml  production stack on the server: portal + Caddy (HTTPS)
deploy/         server setup, auto-deploy, backups: deploy/README.md
```

Not built yet: adding/removing posters from `/admin` (use `npm run manage` for now).
