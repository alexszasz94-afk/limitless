# 04 — The video boards

Full docs: `x_systems/video_boards/README.md` → `SYSTEM.md` (the data file field by field,
card anatomy, statuses, design rules) → `WORKFLOWS.md` (step by step). This page is the
summary.

## What a board is

`<PRODUCT>/video_board.html` is an infinite canvas with one lane per video and one card per
shot. Swanlift uses the columns layout instead: one column per motion-transfer run. Each
card shows the chosen frame or clip, its status, and a **Prompts** drawer with the exact
image prompt, clip prompt, settings, attachments and other takes, each with a Copy button.
The board has two jobs:

1. For the AI: hold every prompt that worked, exactly as sent, so any shot can be remade
   the same way first time.
2. For your user: review new frames and clips fast (Approve / Reject), keep notes, and see
   every video of a product in one place.

## Using it (human)

- Open in **Chrome or Edge** (double-click the file). Keep the folder structure intact:
  the board finds every picture and video by its relative path.
- Drag to pan, wheel or pinch to zoom. Keys: `0` fit all · `1` home · `2` newest video ·
  `E` open every card · `D` dark / light.
- **Review mode:** press **Review**, click Approve / Reject on each card under review, then
  **Copy decisions** and paste the lines to the AI.
- **Notes panel** (left): click **Connect board_notes.txt (once)** and pick
  `<PRODUCT>/content/_board_thumbs/board_notes.txt`. Notes then save into that file. This
  works in Chrome / Edge only; in other browsers notes stay in the browser.

## Changing it (AI)

```
<PRODUCT>/content/_board_thumbs/board_data.json   ← the content (edit this)
        │  python3 x_systems/video_boards/tools/build_board.py [<PRODUCT>]
        ▼
<PRODUCT>/video_board.html                        ← generated (never edit)
```

| Tool (`x_systems/video_boards/tools/`) | What it does |
|---|---|
| `new_board.py "BRAND - PRODUCT" "Brand"` | Start a board for a new product folder |
| `add_card.py` | Add a frame / clip / reference card (refuses a clip on an unapproved frame) |
| `decide.py` | Apply the pasted Approve / Reject decisions |
| `build_board.py` | Rebuild one or all boards from their data |
| `extract_board.py`, `match_media.py`, `make_dark_css.py` | Maintenance helpers used by the kit (see SYSTEM.md) |
| `product_finder.py` | The Product Finder's builder (see `05_product_finder.md`) |

The look and behaviour live only in `x_systems/video_boards/template/` (`page.html`,
`board.css`, `board.js`). Change the template, then rebuild **every** board. The
`example_board.html` / `example_board_data.json` pair shows every feature.

## The five checks, after every change

```
python3 x_systems/video_boards/tools/build_board.py
python3 _tool/check_naming.py
python3 _tool/make_thumbs.py
python3 _tool/mark_lost.py
python3 _tool/check_board.py
```

All five exit 0 or the job is not done. `make_thumbs.py` needs `ffmpeg` on the PATH.
`lost_takes.txt` lists takes whose files are genuinely gone; `mark_lost.py` checks that
the board doesn't point at missing files.
