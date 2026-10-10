# distribution/: posting portal

Next.js app: one private daily checklist per poster (`/d/<token>`), and `/admin` for the owner.
**`README.md` is the maintained doc**: how to run it, how days work, what lives in `config/`.
Server: `deploy/README.md`. First-time setup: `../SETUP.md`.

## Rules

- Built for iPhone first: check every change at 390-402 px wide.
- Real data goes in with `npm run manage` (never the seed). `npm run seed` wipes the database
  (demo data). It refuses once there is poster progress or a real persona; never use
  `--force` on a portal that real posters use.
- **Every push to `main` is a production deploy** (the server pulls it within about 2 minutes).
- The server's Caddy is shared with the Social Tracker (`../social_tracker`): it imports
  `/srv/caddy-sites/*.caddy` and joins the Docker network `edge`. Keep both when changing
  `docker-compose.yml` or `deploy/Caddyfile`.
- Masters are never transcoded or modified; the player uses proxies only.
  `npm run verify-integrity` proves it.
- Never commit `.env`, `data/` or `content/` (see `.gitignore`).
- Before calling a change done: `npx tsc --noEmit` and `npx next build` with no warnings,
  then click through a day on a 390 px wide screen.
- The look comes from the palette tokens in `app/globals.css`: tile #0E1014, glow #4D8DFF,
  glyph #79ADFF, highlight #A8C8FF. One accent, no extra colours.

The block below is managed by `next dev` (Next.js 16). Keeping it here stops `next dev`
from creating its own AGENTS.md/CLAUDE.md in this folder.

<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->
