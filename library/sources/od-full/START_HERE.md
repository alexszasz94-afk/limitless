# Start here — Organic Dropshipping (full copy)

This is the complete working drive of an organic dropshipping business: AI-made short videos
posted on Instagram, TikTok and Facebook (no paid ads), sending traffic to Shopify stores. It
contains every product folder (every frame, clip, prompt and finished video), the video
boards, the Product Finder, the Hooks Board, and the tools and kits that run the business.

Passwords, API keys, email addresses, server addresses, account ids and private notes were
removed before sharing. `x_instructions/12_what_was_removed.md` lists exactly what.

## 1. Unzip

Unzip to a **short path**, e.g. `C:\OD\` or your Desktop, not deep inside other folders
(Windows has a 260-character path limit and some paths here are long). Keep every folder
name exactly as it is: the boards find each picture and video by its place in the folder.

## 2. Open the boards (Chrome or Edge)

| Board | File |
|---|---|
| Video board per product | `<PRODUCT>/video_board.html`, e.g. `THEXMASGLOW - CHRISTMAS PROJECTOR/video_board.html` |
| Product Finder (competitor research) | `x_systems/product_finder/product_board.html` |
| Hooks Board (the 14 proven hooks + on-screen texts) | `x_systems/hooks/hooks_board.html` |

- Drag to move, mouse wheel or pinch to zoom. Video boards: `0` fit all · `1` home ·
  `2` newest video · `E` open every card · `D` dark / light.
- Click a clip to play it and a picture to see it full size. **Prompts** on a card shows the
  exact prompts that made it, with a Copy button.
- **Notes** panel: click **Connect board_notes.txt (once)** and pick that board's
  `board_notes.txt` (for a product: `content/_board_thumbs/board_notes.txt`). Your notes
  then save into that file. All of them start empty.

## 3. Products

| Folder | What | Finished videos |
|---|---|---|
| `THEXMASGLOW - CHRISTMAS PROJECTOR` | Christmas dome projector | `videos_to_post/` (30) |
| `MERRYGLOWUSA - LED CURTAIN LIGHTS` | LED curtain lights | `videos_to_post/` (35) |
| `MERRYGLOWUSA - CHRISTMAS PROJECTOR` | Christmas projector (other store) | `videos_to_post/` (8) |
| `SWANLIFT - POSTURE CORRECTOR BRA` | Posture bra, motion-transfer videos | `videos_to_post/` |

Inside each: `content/video_N_assets/` (frames, clips, `prompts.md` = full history of every
take), `product_images/` (box art, packshots, profile picture), `competition/` (competitor
reels + notes), `references/`.

## 4. Working with your AI (Claude, Codex …)

Open this whole folder as your AI assistant's working folder. It reads `CLAUDE.md` /
`AGENTS.md` first (the rules), then `x_instructions/` (how every system works). Tell it:
*"Read CLAUDE.md and x_instructions/README.md, then help me with …"*.

Install on your computer:

- **Python 3** (python.org; on Windows tick "Add python.exe to PATH")
- **ffmpeg** (includes ffprobe), on the PATH
- **Node.js 22 LTS**, only for the posting portal and the tracker
- Accounts of your own: **Higgsfield** (frames and clips), **Apify** (research and tracking),
  Shopify, Gmail. See `x_instructions/11_accounts_and_keys.md`. Your Apify key goes in a
  file `keys.txt` you create at the root of this folder. Keep it to yourself.

A video round: your AI generates the start frames → they appear on the board as FRAME FOR
REVIEW → you press **Review**, Approve / Reject each card, **Copy decisions**, paste them into
the chat → the AI animates only the approved frames → you review the clips the same way.

## 5. Check that everything works

From this folder, in a terminal (use `python` or `py` instead of `python3` on Windows if
needed):

```
python3 x_systems/video_boards/tools/build_board.py
python3 _tool/check_naming.py
python3 _tool/make_thumbs.py
python3 _tool/mark_lost.py
python3 _tool/check_board.py
python3 x_systems/video_boards/tools/product_finder.py check
```

Every command should end with exit code 0. If a board page ever breaks, the first command
rebuilds it from its `board_data.json`.

## Notes

- The generated videos and box art show the original brand names (TheXmasGlow,
  MerryGlowUSA, Swanlift). Selling under your own brand means new packshots and new frames.
- Higgsfield job ids in the records belong to the original account. Your AI re-uploads the
  local files instead.
- The posting portal (`x_systems/distribution/`) and the tracker (`x_systems/social_tracker/`)
  are web apps you'd host on your own server: `x_instructions/07_*` and `08_*`.
