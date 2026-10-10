# CLAUDE.md — ORGANIC DROPSHIPPING (full shared copy)

Read this before touching anything in this folder. `AGENTS.md` is the same file for AIs
that look for that name. Then read `x_instructions/README.md`: it explains every system
here, in order.

This is not a codebase. It is an organic dropshipping drive: viral short-form videos made
with AI, posted organically (no paid ads) on Instagram, TikTok and Facebook, sending
traffic to Shopify stores. It holds one ALL-CAPS `BRAND - PRODUCT` folder per product,
each with a pipeline of short ad videos, plus the systems around them: the video board kit,
the Product Finder, the Hooks Board, the Distribution posting portal, the Social Tracker,
customer support and fulfillment kits.

Every ad is built the same way: a still **starting frame** is generated, then **animated**
into a clip, then cut in CapCut and posted. The board (`video_board.html`) is the record of
what was picked. The `prompts.md` files are the record of how it was made. Boards are built
by the board kit in `x_systems/video_boards/`. Start at its `README.md`.

## Whose drive this is

This folder is a full copy of the original owner's drive, given to a partner. It was
cleaned before sharing: no passwords, API keys, tokens, email addresses, server addresses,
account ids or private notes are in it (`x_instructions/12_what_was_removed.md` lists what
was removed and what you will find blanked out).

- **"Daniel"** in docs, on boards, in tool messages and in `prompts.md` is the original
  owner. In this copy read it as **the person you work for, your user**. Approvals,
  rejections and "only when Daniel says so" now mean *your* user's say-so.
- **"the drive" / `ORGANIC DROPSHIPPING/`** means this folder, the one holding this file.
  Run every command from here.
- Text like `(email removed)`, `(phone removed)`, `<server-ip>`, `<server-name>`,
  `<github-account>`, `<store-handle>`, `<user>`, `user_REMOVED`, `removed` and
  `(miro board link removed)` marks something that was scrubbed. Never try to recover
  it, and never treat it as a real value.
- The Higgsfield ids in the archive (`job …`, `media …`, `cloudfront.net` result URLs)
  belong to the original owner's account. Your user's account cannot fetch them. To reuse
  an attachment, upload **the local file named next to it** and attach that.
- Snapshot taken 2026-10-07. Counts in docs are dated. The boards and `videos_to_post/`
  are the live numbers, so count from disk when it matters.

Products in this copy: `MERRYGLOWUSA - LED CURTAIN LIGHTS` (35 videos),
`MERRYGLOWUSA - CHRISTMAS PROJECTOR` (8; generated media still shows the old UBU box art),
`THEXMASGLOW - CHRISTMAS PROJECTOR` (30), `SWANLIFT - POSTURE CORRECTOR BRA`
(motion-transfer board). A product called `RETROMYPHONE - RETRO HANDSET` was a deleted
test. Never recreate it.

Archive completeness is a requirement: every take must be in its `prompts.md`, including
failures. Check each `prompts.md` file's dated traceability section for known gaps. Never
reconstruct a missing prompt from a neighbouring take. PNG and MP4 shot references are
both allowed under `_tool/NAMING.md` and share one `r<K>` sequence.

---

## The three rules

They outrank convenience. They outrank your own judgement about what would be nicer. They
are not negotiable mid-task.

### 1. Never invent a filename. The law is `_tool/NAMING.md`.

Read it before writing a single file into a product folder. Do not re-derive the convention
from what is on disk, and do not copy a neighbouring file's pattern. A wrong name that
already exists is a bug, not a precedent.

The short version, which does not replace reading the file:

```
v<N>_c<NN>_<kind><K>.<ext>      v1, v17, v33  ·  c01, c03, c17 (always 2 digits)
                                g = generation, r = reference
                                K starts at 1, never padded, never reused
```

- A generation is **never overwritten.** If you don't like `g1`, the next one is `g2`.
- No letter suffixes (`g1b`, `g3c`), no descriptive names, no `_2k`, no `_upscaled`, no
  `final`, no `best`. An upscale keeps its source's exact name and lives in
  `clips/upscaled/`: the folder is the suffix.
- Everything inside a product folder is lowercase with underscores.

After adding **anything** to a product folder, run all five:

```
python3 x_systems/video_boards/tools/build_board.py   # rebuild the boards from their data
python3 _tool/check_naming.py     # are the files named right?
python3 _tool/make_thumbs.py      # build missing board thumbnails
python3 _tool/mark_lost.py        # does any board still point at a file that is gone?
python3 _tool/check_board.py      # do board paths resolve, are cards uniform?
```

All five must exit 0, or the job is not done. Report the exit codes; don't just say they
passed. None of the checkers edits anything. The boards are generated, so a wrong board is
fixed in its data and rebuilt. A product filter that matches nothing exits 2: that means
"nothing was checked", not "all clear". (On Windows the command may be `python` or `py`.)

### 2. Do not build anything your user did not ask for.

Especially not HTML.

The HTML on this drive is: the four video boards (generated), `x_systems/hooks/hooks_board.html`,
`x_systems/product_finder/product_board.html` (generated), and the board kit's templates and
example page. Every video board is **generated**: its content lives in
`<PRODUCT>/content/_board_thumbs/board_data.json`, and `build_board.py` turns it into
`video_board.html`. A board is drawn as lanes (one per video) or, with `"layout": "columns"`,
one column per motion-transfer run (Swanlift; `x_systems/video_boards/SYSTEM.md` §2.6).
"Add this to the board" means change the data (`add_card.py`, `decide.py`, or by hand) and
rebuild. The Product Finder's data is `x_systems/product_finder/board_data.json`, built by
`x_systems/video_boards/tools/product_finder.py`. **Never hand-edit a generated `.html`**:
the next build overwrites it. The look and behaviour live only in the kit's `template/`.
Change it there and rebuild every board.

Do not create a new board, a dashboard, an index page, a summary page, a preview page, a
README, a comparison page, a "here's what I did" page or a tracker unless asked. If
something feels like it would help, **say so in one line and wait.**

The same goes for scripts. `_tool/` holds four checkers and `x_systems/video_boards/tools/`
holds the board tools. That is enough. Propose a new one; don't write it.

The deliverables on this drive are generated images, generated clips, `prompts.md` entries
and board cards. That is the complete list.

### 3. "Animate it the same way" means copy the prompt, not the idea.

When your user says *animate this like that other one*, the motion must come out identical.
It won't if you rebuild the prompt from memory or describe the motion in fresh words.
**Two prompts that mean the same thing to a human produce different videos.** Rewording is
the bug.

The protocol, every time:

1. **Get the source shot id** (`v20_c02`). If they pointed at a picture, lane or card, read
   the id off the board first. Do not guess which shot they meant: ask.
2. **Open the archive**: `content/video_<N>_assets/prompts.md`, section
   `## Verified record — Higgsfield` → `### C<NN>` → the `— IN THE CUT` entry. That text
   is exactly what Higgsfield ran, and it outranks anything earlier in the file.
3. **Paste it verbatim**: the whole thing, including the CAMERA block, the beat timings
   with their time ranges, the ban list and the phrasing. Byte-identical.
4. **Change only the nouns that physically differ** in the new frame: the room, the
   product, the person, the colour. Everything about *motion, camera, pacing and framing*
   stays exactly as written.
5. **Reuse the settings** from that section's `**Settings**` line. A different model is a
   different animation: seedance 2.5 at 720p/5s stays seedance 2.5 at 720p/5s.
6. **Record the lineage** in the new `prompts.md` entry:
   `Reused from v20 C02 — changed: <the one line that changed, and why>`.

If the source prompt is not in `prompts.md`, say so and stop. Do not reconstruct a prompt by
watching the old clip. The same rule covers stills: *another one like that* means reopen
that shot's `### Image prompt` and change only the one thing they named.

---

## How a generation round runs

- **Two approvals per video, always in this order:** frames first (all start frames go on
  the board as FRAME FOR REVIEW, and your user approves or rejects them), then clips
  (animate only approved frames → CLIP FOR REVIEW → approve or reject). Never animate a
  frame that is not approved. The approval belongs to the exact frame file: a new frame
  needs a new approval, and `add_card.py` refuses a clip on any other frame. Step by step,
  with the commands: `x_systems/video_boards/WORKFLOWS.md` §3–§5.
- **Generate once, then stop.** One generation per shot, then your user reviews. Never
  self-review and re-roll unprompted. If something looks wrong, flag it in a line and let
  them decide.
- **Attach the frame that owns the geometry.** Use two references per regen: one that fixes
  the layout, one that fixes the look. Restate the geometry in the prompt text too, or a
  bug you already fixed comes back.
- **A fix is a prompt edit, not a new frame.** If the note is about motion, timing or
  count, edit that line and re-roll on the same starting frame.
- **Anything that must move has to exist in the starting frame.** A prop that appears only
  in the video prompt pops in and looks fake.
- Nothing is ever overwritten. Re-rolls continue the take numbers.

Product-specific creative law (the black curtain wire, the windowless box, the canonical
C02 framing, the green character, the projector's mesh lens) lives in each product's
`prompts.md` and board panels. Check there before generating, not after.

---

## Private files and keys

- `notes.txt` (root and every product folder), `guides.txt` and `board_notes.txt` are
  your user's private files if they create them. Never open, read, search, quote, edit,
  move or delete them, and leave them out of every grep or crawl. The board's Notes panel
  writes `board_notes.txt` by itself; that is the only thing that touches it. In this copy
  every `board_notes.txt` starts empty.
- `keys.txt` at the root (create it yourself, see `x_instructions/11_accounts_and_keys.md`)
  holds your user's keys. Its `apify_api_` tokens may be used only through
  `x_systems/video_boards/tools/product_finder.py` and the Social Tracker, which read them
  and never print them. Never print, quote or copy any line of `keys.txt` anywhere else.

## Where things live

```
ORGANIC DROPSHIPPING/            (this folder)
  START_HERE.md               for your user (a human): open, unzip, first steps
  CLAUDE.md / AGENTS.md       this file
  x_instructions/             how every system works, for an AI. Read README.md first
  BRAND - PRODUCT/
    video_board.html          generated from board_data.json. Never edit
    content/
      video_N_assets/         starting_frames/ clips/ references/ prompts.md
      _board_thumbs/          thumbnails (generated) + board_data.json (the board's content)
                              + board_notes.txt (the Notes panel's file). Never delete
      lost_takes.txt          files that are genuinely gone
      stories/                story / hero stills for posts (optional)
      upscaled_videos/        Swanlift only: one upscale per finished video
    product_images/  competition/  videos_to_post/  references/ (optional)
                              nothing else belongs in a product folder (NAMING.md §2)
  _tool/                      NAMING.md + the four checkers
  x_assets/                   images/ (board icons). Songs are not included: use music you have the rights to
  x_context/                  business.md, priorities.md, decisions.md: the original
                              owner's business context and decision log (history; see
                              x_instructions/01_business_and_model.md)
  x_research/                 prompting guides (gpt image 2 / 2.5, nano banana 2, seedance 2.5),
                              upscaler research, Genjutsu motion-transfer research, sourcing playbook
  x_systems/
    video_boards/             the board kit: README, SYSTEM, WORKFLOWS, template/, tools/
    product_finder/           competitor-account research board + its data and raw evidence
    hooks/                    Hooks Board: the 14 proven hooks + the "Text on screen" list
    distribution/             posting portal (Next.js app) for a team of posters
    social_tracker/           views/followers tracker (Next.js app + Apify scraper)
    customer_support/         the support-email system as a generic kit (kit/)
    fulfillment/              the supplier-tracking system as a generic kit (kit/) + supplier research
```

## Two facts that will bite

- **Some synced or network drives truncate writes** made through an AI's file tools (the
  original drive did: a file write was cut off at the old file's length). Safe pattern:
  write to a temp file, check the byte count, copy it into place, then compare `md5sum` of
  both. Verify after every write.
- **Two sessions, one board.** The board tools write through an exclusive `<file>.building`
  temp file and refuse to save `board_data.json` if it changed since they read it. A second
  session editing the same board is stopped with a message, never silently overwritten. A
  leftover `.building` file (from an interrupted run) is deleted, then rerun.
