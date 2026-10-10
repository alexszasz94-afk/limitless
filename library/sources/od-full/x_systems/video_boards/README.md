# Video boards — start here

Every product on this drive has one **video board**: `<PRODUCT>/video_board.html`.
It is an infinite canvas (pan, zoom) with one lane per video and one card per
shot - or, in the **columns layout** (`"layout": "columns"`, SYSTEM.md §2.6), one column per
motion-transfer run with three rows that line up: reference reel, new woman + room, final video. It has two jobs:

1. **For Claude** — hold every prompt that worked, exactly as it was sent to
   Higgsfield, with its settings and attachments, so any shot can be remade
   the same way on the first try.
2. **For Daniel** — review new frames and clips fast (Approve / Reject), keep
   notes, and see every video of a product in one place.

All boards are built from **one template** by **one tool**. Nobody edits a
`video_board.html` by hand any more.

```
<PRODUCT>/content/_board_thumbs/board_data.json   ← the board's content (edit this)
                 │
                 ▼  python3 x_systems/video_boards/tools/build_board.py <PRODUCT>
<PRODUCT>/video_board.html                        ← generated page (never edit)
```

## What is in this folder

```
x_systems/video_boards/
  README.md            this page
  SYSTEM.md            how a board is built: the data file field by field, the
                       card anatomy, the statuses, the design rules
  WORKFLOWS.md         step-by-step: new product, new video round (frames →
                       review → clips → review), applying Daniel's decisions,
                       Higgsfield checks, rebuilding a broken board, final checks
  template/
    page.html          the page skeleton
    board.css          the stylesheet (the look of every board)
    board.js           canvas engine, notes panel, review buttons
    favicon.txt        default tab icon (a product can set its own)
    example_board_data.json   a made-up product showing every card state
    example_board.html        what that example looks like (open it)
  tools/
    build_board.py     board_data.json → video_board.html (validates first)
    add_card.py        add / update one shot from its Higgsfield job records
    decide.py          apply Daniel's APPROVE / REJECT lines
    new_board.py       start the board of a new product
    extract_board.py   rescue: video_board.html → board_data.json
    match_media.py     audit: which Higgsfield job made which file
    make_dark_css.py   regenerate the dark theme after a colour change in board.css
```

Standard library Python only, except `match_media.py --media` (Pillow + numpy).
The drive-wide rules still apply: file names follow `_tool/NAMING.md`, and the
build plus the four checks in `_tool/` must all exit 0 after every change
(WORKFLOWS.md §7).

## The boards today

| product | videos | cards | data file |
|---|---|---|---|
| SWANLIFT - POSTURE CORRECTOR BRA (columns layout) | 10 | 12 runs | `content/_board_thumbs/board_data.json` |
| THEXMASGLOW - CHRISTMAS PROJECTOR | 30 | 210 | `content/_board_thumbs/board_data.json` |
| MERRYGLOWUSA - LED CURTAIN LIGHTS | 35 | 265 | `content/_board_thumbs/board_data.json` |
| MERRYGLOWUSA - CHRISTMAS PROJECTOR | 8 | 40 | `content/_board_thumbs/board_data.json` |

(Counts as of 2026-09-30, Swanlift 2026-10-05 - the boards themselves are the live number.)

`content/_board_thumbs/` also holds the thumbnails (rebuilt by
`_tool/make_thumbs.py`) and `board_notes.txt` (Daniel's notes). **Never delete
that folder**: `board_data.json` and `board_notes.txt` are not regenerable.

## The five things to remember

1. Change `board_data.json`, then run `build_board.py`. Never edit the HTML.
2. Every prompt on a board is the exact text stored on the Higgsfield job that
   made the file shown — pasted, never rewritten.
3. Two approvals per video: frames first, then clips (WORKFLOWS.md §3–§5).
   A motion-transfer clip has no frame: its references (woman, room) are approved first when the
   card starts at stage `refs`, then the clip (§5).
   Only Claude changes a card's status, in the data file.
4. Nothing is overwritten on disk; re-rolls take the next take number.
5. The design lives in `template/`. Change it there and rebuild every board —
   all boards must stay identical in look and behaviour.
