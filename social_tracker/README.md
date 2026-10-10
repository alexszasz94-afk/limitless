# Social Tracker

The dashboard for your brands. For every product it shows the accounts on Instagram, TikTok
and Facebook, every video they post, its views over time, the followers, and which videos
perform best. It uses public data only, through Apify scrapers, and never logs in to the accounts.

Setting it up on a server: [`../SETUP.md`](../SETUP.md). Server details: [`deploy/README.md`](deploy/README.md).

## Pages

| Page | What it answers |
|---|---|
| **Overview** | Total views, views gained per day by platform, followers, each product and its account on each platform. **Top videos** (most views gained in the period) and **Best first 24 hours** (most views 24 h after going live, among the videos posted in the period). Filters: product, 7 / 30 / 90 days / all. |
| **Videos** | Every video (one post on one platform): views gained in the period, total, **views 24 h and 7 days after it went live** (the fair way to compare a new video with an old one), likes, comments, shares, saves, engagement. Filter by platform and product, and sort by any column. |
| **Runs** | Health, this month's spend against the budget, the Apify key pool, the schedule, every scraper run with its cost, and a **Run now** button. |
| **Keys** | Every Apify key in `APIFY_TOKENS`: credit left and spent (everything the key ran, this tracker or anything else), each key's spend, cap and reset day, and a **Check now** button. It checks automatically every hour. *Invalid* = Apify refuses the key; *not reached* = Apify didn't answer twice (network problem), so the numbers are unknown until the next check. |

## How the numbers are made

- **Total views** = the latest count of every post, added up (what the platforms show now).
- **Gained** (today, a period, the chart) = views added during those **local days** (the
  `timezone` in `config/cadence.json`), worked out from the difference between consecutive
  snapshots of each post. A post's first snapshot is its starting point. A gap between two
  snapshots is spread over the days it covers.
- **Instagram views** = Instagram plays only. If a reel is shared to Facebook, its Facebook
  plays are never added here (the Facebook post is tracked on its own). Facebook views = the
  number shown on the reel. TikTok views = play count.
- Only **videos** are tracked: Facebook photo posts (profile picture, cover) are ignored.
- **Every post is its own video.** The same clip posted on Instagram, TikTok and Facebook counts
  as three videos, one per platform.
- Safety rails:
  - A failed scrape writes nothing, so zeros never enter the history.
  - A views drop of more than 30% is refused until it's confirmed 3 times over 24 h.
  - A snapshot that dips and then recovers is deleted automatically.
  - A post missing from 2 refreshes in a row is marked gone (its history stays).
  - A platform that returns nothing backs off from 1 h to 12 h, instead of being paid for every hour.

## When it scrapes (`config/cadence.json`)

- **New posts:** every account at 00:00, 06:00, 12:00 and 18:00 (its newest 12 posts, which also
  refreshes their numbers). A newly added account is scraped right away.
- **Older posts:** re-checked by age: every 12 h for 2 days, then daily at 09:00 until 14 days,
  weekly until 60 days, then monthly. A post whose daily views beat 2x its account's median is
  checked every 6 h for 48 h.
- **Followers:** Instagram and Facebook daily at 09:00, TikTok with every check.
- **Run now** (Runs page) does a full pass straight away.

## Config (no code changes, read live)

| File | What it holds |
|---|---|
| `config/products.json` | The products and their accounts. Add a product or account and push. `active: false` (or removing it) pauses it, and its history is kept. |
| `config/cadence.json` | The schedule above, and the `timezone` all days are counted in. |
| `config/budget.json` | A hard monthly ceiling for this tracker's Apify spend (`monthlyBudgetUsd`). Over it, runs are skipped and logged as `budget stop`. |

## Apify keys

`APIFY_TOKENS` in `.env`: one key, or several separated by commas. Keys are tried in order. A
key is used while its own monthly credit covers the run. When it's out of credit, busy (free
accounts allow 5 runs at a time) or invalid, the next key is used. With one key, that key does
everything. The Runs and Keys pages show the pool. For local runs only, `APIFY_KEYS_FILE` can
point at a text file instead: every `apify_api_...` token in it is used, and nothing else in
the file is read.

## Run it on this computer (optional, for testing)

Needs Node.js 20.9+.

```bash
cd social_tracker
npm install
cp .env.example .env      # set TRACKER_PASSPHRASE and APIFY_TOKENS
npm run dev               # dashboard on http://localhost:3100
npm run scraper           # the scheduler, in a second terminal (scrapes for real, spends credit)
npm run scrape:once       # one full pass now
```

Local data goes to `data/tracker.db` (gitignored), separate from the server's.

## Server

See `deploy/README.md`. In short: `/srv/social_tracker/app` is the `social_tracker/` folder of
a clone of the repo. A push to `main` deploys itself within about 2 minutes (two containers:
`web` and `scraper`). The database is `/srv/social_tracker/db/tracker.db` with nightly backups.
HTTPS goes through the portal's Caddy.
