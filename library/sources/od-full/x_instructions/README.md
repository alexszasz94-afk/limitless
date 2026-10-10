# x_instructions — how everything on this drive works

Written for an AI assistant (Claude, Codex, …) working in this folder for a new owner. A
human can read it too, but `START_HERE.md` at the root is the human version.

Read `../CLAUDE.md` first (the rules). Then read the files below in order. Each one says
what a system is for, where its files are, how to run it, and what you must set up yourself
because the original owner's accounts and keys were removed.

| # | File | What it covers |
|---|---|---|
| 01 | `01_business_and_model.md` | The business model, the products, what worked (numbers), how decisions were made |
| 02 | `02_drive_layout.md` | Every folder and what lives in it |
| 03 | `03_video_pipeline.md` | How one ad is made: hook → frames → review → clips → review → cut → post |
| 04 | `04_video_boards.md` | The video boards: opening, reviewing, notes, rebuilding, the five checks |
| 05 | `05_product_finder.md` | The competitor-research board and how new accounts are imported |
| 06 | `06_hooks_board.md` | The 14 proven hooks and the on-screen text list |
| 07 | `07_distribution_portal.md` | The posting portal for a team of posters (Next.js, self-hosted) |
| 08 | `08_social_tracker.md` | The views / followers tracker (Next.js + Apify, self-hosted) |
| 09 | `09_customer_support.md` | The support-email system (kit) |
| 10 | `10_fulfillment.md` | The supplier / fulfillment tracking system (kit) and the sourcing research |
| 11 | `11_accounts_and_keys.md` | Every account and key the new owner needs, and where each one plugs in |
| 12 | `12_what_was_removed.md` | What was taken out before sharing, so you don't look for it |
| — | `skills/` | Three step-by-step procedures the original owner ran as Claude skills |

## The short version

1. Products live in `BRAND - PRODUCT/` folders. Each has a **video board**
   (`video_board.html`, open in Chrome or Edge) that shows every video, shot and prompt.
2. Ads are AI-generated: still frame in Higgsfield (`gpt_image_2` / `gpt_image_2_5`),
   animated with `seedance_2_5` (or Genjutsu motion transfer for Swanlift), upscaled, cut
   in CapCut with on-screen text and a song, posted organically.
3. Every prompt that ever ran is archived in `content/video_N_assets/prompts.md`. Reuse a
   proven prompt **verbatim** (CLAUDE.md rule 3).
4. New products come from the **Product Finder** (`x_systems/product_finder/product_board.html`):
   competitor accounts ranked by real views.
5. Videos are posted by a team through the **Distribution** portal and measured by the
   **Social Tracker**. Both are web apps the new owner must host himself.
6. Stores get a support inbox (customer support kit) and a supplier tracker (fulfillment
   kit). Both kits use `<placeholders>` you fill with the new owner's own values.

## Working style the boards and tools expect

- Use Python 3 (standard library only) for the board tools. Install `ffmpeg`/`ffprobe` for
  thumbnails and clip checks. Use Node.js 20.9+ for the two web apps.
- Run every command from the drive root (the folder holding `CLAUDE.md`).
- Generate once per shot, then wait for your user's review.
- Report exit codes of the checks; never claim a check passed without running it.
