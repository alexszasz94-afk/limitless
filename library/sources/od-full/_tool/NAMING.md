# Naming and folder rules

This file is the law. `check_naming.py` enforces it. If a rule here and a file on
disk disagree, the file is wrong.

## 1. Product folders

One folder per product at the root of `ORGANIC DROPSHIPPING`, named:

```
BRAND - PRODUCT
```

ALL CAPS, spaces around the dash. Examples:

```
MERRYGLOWUSA - LED CURTAIN LIGHTS
THEXMASGLOW - CHRISTMAS PROJECTOR
```

Everything *inside* a product folder is lowercase with underscores. No spaces,
no capitals, no dates in folder names, no `round1/` `round2/` `final/` `new/`
`old/` folders — ever.

## 2. Product folder layout

```
BRAND - PRODUCT/
  video_board.html          <- generated from content/_board_thumbs/board_data.json, see §6
  notes.txt                 <- Daniel's private notes (never opened by Claude)
  references/               <- product-level anchors, stable names (optional)
  product_images/
  competition/
  content/
    _board_thumbs/          <- board_data.json, board_notes.txt, thumbnails (§6)
    lost_takes.txt          <- files that are gone for good
    stories/                <- story / hero stills for posts (descriptive lowercase names allowed)
    upscaled_videos/        <- one 2K upscale per finished video, video_N.mp4 (Daniel 2026-10-06; source + job in that video's prompts.md)
    video_1_assets/
    video_2_assets/
    ...
  videos_to_post/
```

Nothing else goes in a product folder or in `content/` - `check_naming.py` reports
any other entry. Business files (spreadsheets, screenshots, status notes) live
outside the product folders.

## 3. Asset folder layout

Every `video_N_assets/` contains exactly four things and nothing else (all
three folders exist even when empty - `check_naming.py` reports a missing one):

```
video_N_assets/
  starting_frames/
  clips/
  references/
  prompts.md
```

`clips/upscaled/` is the one permitted sub-folder, inside `clips/`.

If a folder appears that is not on this list, it is junk. Move it to the
`to_delete/` folder at the root of `ORGANIC DROPSHIPPING` — one staging area
for the whole drive, not one per product — and say so, so it actually gets
emptied. Never leave junk inside a product folder.

## 4. File names

```
v<N>_c<NN>_<kind><K>.<ext>
```

| part | meaning | rule |
|---|---|---|
| `v<N>` | video number | no padding: `v1`, `v17`, `v33` |
| `c<NN>` | clip / shot number within that video | **always two digits**: `c01`, `c03`, `c17` |
| `<kind>` | `g` = generation, `r` = reference | one letter |
| `<K>` | take number | starts at 1, no padding, never reused |

Examples:

```
starting_frames/v33_c03_g1.png     first frame generated for video 33, shot 3
starting_frames/v33_c03_g2.png     second attempt, first one is KEPT
clips/v33_c03_g1.mp4               first clip animated off that frame
clips/upscaled/v33_c03_g1.mp4      the 2K upscale of that exact clip
references/v33_c03_r1.png          a reference image made for this shot
references/v33_c03_r2.mp4          a video motion reference for the same shot
```

### Rules that follow from this

- **A generation is never overwritten.** Don't like `g1`? The next one is `g2`.
  `g1` stays on disk. This is how we compare takes and how we learn what failed.
- **Take numbers are per shot, per kind.** Frames and clips number
  independently: `v33_c03_g4.png` and `v33_c03_g1.mp4` can coexist, and normally
  do — a clip is animated off whichever frame was picked.
- **The upscale carries its source's exact name**, in `clips/upscaled/`. No
  `_2k`, no `_upscaled`, no suffix of any kind. The folder is the suffix.
- **No letter suffixes.** `g1b`, `g1c`, `g3c` are banned. A re-roll with a
  tweaked prompt is a new number, not a letter. So is a re-roll with a different
  reference.
- **No descriptive names.** `ref_store_walk.png`, `final_v2.png`,
  `best_one.png`, `v1_c01_anim.png` are all banned. What the file *is* goes in
  `prompts.md`, not in the filename.
- Extensions: `.png` for starting frames, `.mp4` for clips, and `.png` or
  `.mp4` for references. Lowercase. Daniel approved MP4 shot references on
  2026-09-21. Image and video references share a single `r<K>` sequence per
  shot: never reuse r1 for a second reference of a different format.
- Archive a video reference's original name, current path, hash, duration and
  audio status in `prompts.md`. A silent derivative is a separate reference;
  do not call an original with audio silent.

### Product-level references

Cross-video brand anchors live in `<PRODUCT>/references/` and keep stable,
descriptive, lowercase names, because they are referred to by name for months:

```
references/box_front.png
references/pfp_style.png
references/product_anchor.png
```

These are the one exception to "no descriptive names". They are not takes and
they never get a version number — if the anchor changes, it is a different
product decision and gets a different name.

## 5. prompts.md

One per `video_N_assets/`. It must archive **every** prompt and every
take, including the ones that failed. The board carries only the prompts of
the takes in the cut (§6); everything else belongs here. The inline template below is the
authoritative format; the old `PROMPTS_TEMPLATE.md` pointer was broken.
Historical gaps must be labelled explicitly, not treated as complete. The shape is:

1. **Reusable blocks** — the paragraphs pasted into every prompt for this video
   (geometry block, product realism block, ban list). Quoted verbatim so they
   can be copied.
2. **Per shot** — for each `cNN`, every take that was generated, its full
   prompt, which references were attached, the model and settings, the job id,
   and whether it worked. **Bad takes are recorded, not deleted** — the reason a
   take failed is the most valuable thing in the file.
3. **What changed and why** — when a take is a re-roll of the previous one, the
   line that changed and the reason.

If you can't re-create a shot from its prompts.md alone, the prompts.md is
incomplete.

### Verified record

Every `prompts.md` ends with `## Verified record — Higgsfield`: one `### CNN`
per shot, the take in the cut first, then every other take on disk, each with
the exact Higgsfield prompt, settings, job id, result URL and attachments. It is
built by matching each local file to its Higgsfield job (clips byte-identical).
When anything earlier in the file disagrees, the verified record wins. Every new
take is added there the same way.

### Inline archive template

Repeat the take block for every frame, clip and reference. Keep earlier blocks
unchanged, including rejected takes. Put current status above historical notes.

````markdown
# Video N — title

**Current status (YYYY-MM-DD):** verified local export path, or current stage.

## Reusable blocks
Exact reusable text; no paraphrasing.

## C01 — shot name
**Frame:** `starting_frames/vN_c01_g1.png`
**Clip:** `clips/vN_c01_g1.mp4`
**Settings:** exact model, mode, resolution, quality, duration and other submitted parameters.
**Job ID:** full service job UUID; explicitly unknown if not recorded.
**References:** exact local paths plus attached media IDs/URLs and roles in order.

### Image prompt
```text
Exact submitted image prompt.
```

### Video prompt
```text
Exact submitted motion prompt.
```

### Take history
Exact filename/path; result; selected/rejected/unreviewed; reason if recorded.
Reused from vX CYY — changed: exact line and reason, or no change.
Upscaled derivative: exact source path and upscale job/settings, or explicitly unknown.
````

A file inventory proves accounting, not prompt completeness. Recovered service
records are evidence; a filename mention alone is not. Do not reuse an unresolved
take until its exact prompt and settings have been retrieved. Never mistake C2PA
manifest/instance UUIDs embedded in MP4s for generation job IDs.

## 6. video_board.html

Every product has one board, and every board is **generated** by the board kit
in `x_systems/video_boards/` (Daniel's request, 2026-09-23). The kit is the
complete specification — this section only fixes the names:

```
<PRODUCT>/content/_board_thumbs/board_data.json   the board's content (source of truth)
<PRODUCT>/content/_board_thumbs/board_notes.txt   Daniel's notes, written by the page
<PRODUCT>/content/_board_thumbs/**/*.webp         thumbnails (make_thumbs.py)
<PRODUCT>/video_board.html                        built by build_board.py - never edit
```

- `x_systems/video_boards/SYSTEM.md` — the data file field by field, the card
  anatomy (`data-clip`, `data-shot` = `v<N>_c<NN>`, `data-stage` frame|clip,
  `data-status` review|approved|rejected, `data-file` = the file under review),
  the status chips, the design constants (card 372 px, two-frame card 724 px,
  frame column 342 px).
- `x_systems/video_boards/WORKFLOWS.md` — new product, the two-step review
  (frames → Daniel → clips → Daniel), applying decision lines, after the export,
  Higgsfield checks, repairs.

Card titles are short so they never truncate; one fixed slot list per product
(TheXmasGlow: C01 the short hook name, C02 Hands on the box, C03 The projector
lifted, C04 The cable going in, C05 The door opens on the room, C06 The bed
bounce, C07 The whole Christmas room).

**Every prompt on a board is the exact text stored on the Higgsfield job** that
made the file shown. Rejected takes never disappear: they stay in the card's
"Other takes on disk" with Daniel's reason, and in `prompts.md`.

## 7. Enforcement

After adding anything to a product folder, run:

```
python3 x_systems/video_boards/tools/build_board.py   # 0. rebuild the boards from their data
python3 _tool/check_naming.py     # 1. are the files named right?
python3 _tool/make_thumbs.py      # 2. build any missing board thumbnails
python3 _tool/mark_lost.py        # 3. no board points at a file that is gone
python3 _tool/check_board.py      # 4. does the board point at real files,
                                  #    and is every card the same shape?
```

Each takes an optional product filter:

```
python3 _tool/check_naming.py "MERRY*"
python3 _tool/check_board.py XMAS
```

Exit code 0 means clean. All five must exit 0 before a job is done.

`mark_lost.py` never edits a board (boards are generated): it fails when a board
still points at a file that is gone - listed in `lost_takes.txt` → rebuild the
board (the builder greys it out); not listed → restore the file or record it with
Daniel. `build_board.py` applies the same rule: a missing file that is not listed
stops the build. `check_naming.py` also cross-checks the archive: every take named
in a video's `prompts.md` and every path on the board must be on disk or in
`lost_takes.txt` - that is what catches a deleted latest take, which leaves no
numbering hole. A product filter that matches nothing exits 2, never 0.
