# social_tracker/: Social Tracker

Next.js dashboard + Apify scraper: products -> accounts (Instagram, TikTok, Facebook) -> posts ->
snapshots. Every post is its own video (one per platform).
**`README.md` is the maintained doc** (what each number means, the schedule, config, keys).
Server: `deploy/README.md`. First-time setup: `../SETUP.md`.

## Rules

- Which accounts are tracked: `config/products.json` is the only answer.
- **Every push to `main` is a production deploy** (the server pulls it within about 2 minutes).
  HTTPS comes from the portal's Caddy (`../distribution`) over the Docker network `edge`.
- Apify keys live only in `.env` (`APIFY_TOKENS`). Never print a key and never commit one.
- Before calling a change done: `npx tsc --noEmit` and `npx next build` with no warnings, and
  look at the pages at 390 px and desktop width.
- The look comes from the palette tokens in `app/globals.css` (the same as the portal's).
  Platform colours (IG #D95926, TikTok #199E8C, FB #4D8DFF) are a colour-blind-safe set; always
  pair them with the platform name. Format dates and numbers in client components by hand, not
  with `Intl` (server and browser ICU differ and break hydration).
- Never commit `.env` or `data/`.

The block below is managed by `next dev` (Next.js 16). Keeping it here stops `next dev`
from creating its own AGENTS.md/CLAUDE.md in this folder.

<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->
