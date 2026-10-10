# 12 — What was removed before sharing

This copy was made on 2026-10-07 from the original owner's drive. Everything below was taken
out or blanked on purpose. Don't look for these files, don't try to recover blanked
values, and don't treat a placeholder as a real value.

## Not copied at all

| What | Why / what to do instead |
|---|---|
| `keys.txt`, `notes.txt` (root + every product), `guides.txt`, every `board_notes.txt` | Private files. Every `board_notes.txt` was recreated **empty** so the Notes panels work. Create your own `keys.txt` (`11_accounts_and_keys.md`) |
| `.env` files, `.claude-keys/` (SSH keys, deploy keys, passphrases), `.git/` history of both apps | Credentials. `.env.example` files are kept; generate new keys. Start a fresh git repo for each app |
| `node_modules/`, `__pycache__/`, `*.pyc` | Generated; `npm install` recreates them |
| Accounting folder (bank statements, financial analysis) | Personal finance |
| The original owner's personal tax and legal research | Personal |
| A former partner's folder inside `MERRYGLOWUSA - LED CURTAIN LIGHTS/` (financial records, Shopify support chats) | Third-party financial data. `_tool/check_naming.py` no longer tolerates that folder |
| Supplier conversations, screenshots and videos (`fulfillment/agents/`), the CJ-vs-Zendrop comparison built from them, the fulfillment `status.md` and `fulfillment_tracker.xlsx` | Third-party contacts, staff names and orders. The kit + research stay (`10_fulfillment.md`) |
| The Product Finder's raw link lists from a private online community (Discord) and its Miro boards | Private community content |
| Personal customer-support docs (filled-in `README`/`SETUP`/`REPLYING`/`stores.md`) | Inbox address, store handles, customer threads. The generic kit stays (`09_customer_support.md`) |
| `x_systems_shared/` (what the original owner publishes to other people) | Not part of the working drive |
| The root `CLAUDE.md` / `AGENTS.md` | Rewritten for this copy |
| One icon file named after the original owner's email account | Personal |

## Blanked inside files (placeholder you will see)

| Placeholder | Was |
|---|---|
| `(email removed)` | Any email address: the original owner's, and creators' emails from public Instagram bios and YouTube descriptions |
| `(phone removed)` | Phone numbers from public bios |
| `<server-ip>`, `<server-name>` | The original VPS address and name |
| `<github-account>`, `<old-github-account>` | The original GitHub account names |
| `<store-handle>` | Shopify admin store handles |
| `<user>`, `/sessions/<session>` | Computer user name in file paths |
| `user_REMOVED` | The Higgsfield account id inside `cloudfront.net` result URLs (those URLs no longer resolve; the local files are the copies) |
| `removed` (in `x_systems/product_finder/raw/research/*_run.json` / `*_status.json`) | Apify user, run, dataset, key-value-store and console ids |
| `(miro board link removed)`, `(board id removed)` | Miro board links from a private online community |
| Instagram `?stkn=` / `?igsh=` share parameters | They identify who shared a link; removed from URLs |
| WhatsApp `[time, date] Name:` prefixes | Chat member names in the Product Finder's raw link dumps |
| Product Finder Notes card (`notesCard.initialText`) | The original owner's private checklist (now empty) |
| `(apify url removed)` | Signed Apify storage links (datasets, key-value stores) that could open the original owner's Apify data |
| Comments and tagged users in `x_systems/product_finder/raw/research/*.json` (`latestComments`, `firstComment`, `taggedUsers` removed) | Personal data of members of the public who commented; not needed by any tool |
| `key_index` in old `raw/research/*_run.json` set to 0 | Which of the original owner's API keys ran each job |
| Names of supplier staff, partnership terms with a former partner, the private WhatsApp group's name, the original owner's country | Personal / third-party details |

## Also left out on purpose

- `x_assets/songs/` (commercial songs): use music you have the rights to.
- The two deep supplier research reports for the TheXmasGlow projector, and the raw dumps of links shared in a private WhatsApp group (`whatsapp_viral_products.txt`, `pasted_chunk.txt`).
- Store-specific notes about past listings and order backlogs.
| `od-` in two code constants, "Organic Dropshipping" as the apps' display name, "blue palette" | The original owner's business name |
| `Poster 1` | The original poster's device name |

## Kept on purpose

- **Business numbers** (revenue, orders, prices, product costs, supplier quotes) in
  `x_context/`, the research reports and the docs.
- The **first name "Daniel"** (the original owner) in docs and on boards. Read it as your user.
- **Brand and store names** (TheXmasGlow, MerryGlowUSA, Swanlift) and their **public social
  handles**: the product folders, boards, generated media and box art carry them.
- **Higgsfield job and media ids**: history only; they work only in the original account.
- Public competitor data (handles, view counts, public reels) in the Product Finder and the
  `competition/` folders.
