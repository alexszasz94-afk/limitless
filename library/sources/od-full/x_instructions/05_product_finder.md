# 05 — Product Finder

**What it is:** a research board of competitor accounts selling viral products on
Instagram, TikTok and Facebook. Open `x_systems/product_finder/product_board.html` in Chrome
or Edge. It is organised as **category → product → variation → accounts**, with one card
per source account. Each card shows that account's best video of the product it sells
**now** (its latest continuous product run), its followers, and the average views of its
newest up to 20 videos of that run. Accounts are ranked on video performance; the 50
weakest are listed separately. A batch picker shows which accounts were added on which day.

## Files (`x_systems/product_finder/`)

| File | What it is |
|---|---|
| `board_data.json` | Source of truth (UTF-8, indent 2, no trailing newline) |
| `product_board.html` | Generated board. Never edit |
| `links.txt` | Generated: one dated section per batch. Never edit |
| `media/` | Each featured video (`.mp4`) + poster (`.jpg`), named `ig_/tt_/fb_<handle>_<videoId>` |
| `raw/reel_owner_map.txt` | Shared reel → owner handle (`CODE=handle`, append only) |
| `raw/research/` | Evidence per import / per Apify run (`<label>_run/_status/_items.json`, `update_<mon><dd>_review.json`) and the removals |
| `board_notes.txt` | The Notes card's file (starts empty) |

## The tool

```
T=x_systems/video_boards/tools/product_finder.py
python3 $T check          # validate everything, write nothing
python3 $T all            # rank + links + build + check (exit 0 or the job is not done)
python3 $T triage FILE    # classify links: present / removed / new / needs_resolution
python3 $T apify-balance  # credit left on every Apify key in keys.txt
python3 $T apify-run ACTOR INPUT.json LABEL --max-usd 1 [--wait 150]
python3 $T apify-fetch LABEL
```

The `apify-*` commands need Apify tokens in `keys.txt` at the drive root
(`11_accounts_and_keys.md`). Everything else works offline.

## Rules that matter

- **Latest product run only.** Accounts change products; old success misleads. Show the
  highest-viewed video inside the newest unbroken run of the same physical product, and
  average its newest up to 20 videos. Mixed or ambiguous accounts are `review` and not
  ranked.
- **Same physical product = same product and variation**, whatever the account name.
  Designs, fandoms, niches and seasons are variations.
- **Footage decides the label**, not the username, bio, caption or store link.
- **Never restore a removed account** (`raw/research/removals.json` and the two audit files).
- **Unknown is unknown, not zero.** Never fill a gap with a guess or another account's video.
- Ranking: equal-weight percentiles of followers and current-run average views (details in
  the tool's docstring).

## Importing new accounts

The full procedure is `skills/product-finder-import.md`. The original owner collected links
from a private WhatsApp group of product hunters. Your user will have their own
source: any list of links works with `triage`.

## Note on scrubbed data

- Creators' emails and phone numbers from public bios became `(email removed)` /
  `(phone removed)`.
- Apify account and storage ids in `raw/research/*_run.json` / `*_status.json` became
  `removed`. The old runs can't be re-fetched, but their `_items.json` evidence is intact.
- The original owner's private checklist was removed from the Notes card.
