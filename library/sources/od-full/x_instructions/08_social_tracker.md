# 08 — Social Tracker

**What it is:** a dashboard plus an hourly scraper (Next.js + SQLite). For every product, it
tracks its accounts on Instagram, TikTok and Facebook: total views, views gained per day,
followers, every post (with its views 24 h and 7 days after going live), and which
**Distribution video** performs best. Posts are matched to videos by caption, using
`x_systems/distribution/content-manifests/<persona>.json`. It uses **public data only**,
through Apify scrapers, and never logs in to the accounts.

**Folder:** `x_systems/social_tracker/`. Read its `README.md` (pages, how numbers are made,
scrape cadence, config), `CLAUDE.md` (rules for an AI) and `deploy/README.md` (hosting).

## Config (read live, no code change)

| File | Holds |
|---|---|
| `config/products.json` | The products and their accounts (`platform`, `handle`, `url`, `active`), `distributionPersona`, `videoOverrides` for fixing a post→video match by hand. The Swanlift entry is the original owner's real setup: replace it with your user's accounts |
| `config/cadence.json` | When new and old posts and followers are scraped |
| `config/budget.json` | Hard monthly ceiling for the tracker's own Apify spend (was $400), per-run caps |

## Keys

The scraper needs Apify API tokens:

- locally: `APIFY_KEYS_FILE` in `.env` points at a text file holding `apify_api_…` tokens
  (default `../../keys.txt`, the drive root's `keys.txt`, shared with the Product Finder);
- on the server: `APIFY_TOKENS=` (comma-separated) in the server's `.env`;
- plus `TRACKER_PASSPHRASE` for signing in to the dashboard.

Copy `.env.example` to `.env` and fill it. The Keys page shows each key's credit, spend and
reset day. Use keys from Apify account(s) your user owns, within Apify's terms.

## Run / host

Locally: `npm install`, set `.env`, then follow README.md. In production it ran on the
**same server as Distribution**, behind Distribution's Caddy (through `/srv/caddy-sites/*.caddy`
and the Docker network `edge`), deployed by push to its own private GitHub repo.
`deploy/server-setup.sh` + `deploy/README.md` cover it. Set up Distribution's server first.
The original addresses, repo and keys were removed (`<server-ip>`, `<github-account>`).

Shopify sales stats were planned but not built (README "Later").
