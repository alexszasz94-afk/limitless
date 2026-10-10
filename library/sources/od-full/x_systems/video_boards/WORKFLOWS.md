# Video board — workflows

Commands run from the drive root (`ORGANIC DROPSHIPPING/`). `PRODUCT` is the
product folder name or any piece of it that matches only that folder (`THEX`,
`LED`, `"MERRYGLOWUSA - CHRISTMAS"`).
Read `CLAUDE.md` and `_tool/NAMING.md` first — they outrank this file.

```
python3 x_systems/video_boards/tools/build_board.py PRODUCT        # rebuild one board
python3 x_systems/video_boards/tools/build_board.py                # rebuild every board
python3 x_systems/video_boards/tools/add_card.py PRODUCT ...       # add / update a shot from Higgsfield job records
python3 x_systems/video_boards/tools/decide.py PRODUCT "APPROVE …"  # apply Daniel's review lines
python3 x_systems/video_boards/tools/new_board.py "BRAND - PRODUCT" "Brand"   # new product
```

## 1. A new product

1. Create the product folder by `_tool/NAMING.md` §1–§3 (ALL CAPS `BRAND - PRODUCT`,
   `content/`, `product_images/`, `videos_to_post/` …).
2. `python3 x_systems/video_boards/tools/new_board.py "BRAND - PRODUCT" "Brand"` —
   writes `content/_board_thumbs/board_data.json` (no videos yet), an empty
   `board_notes.txt`, and the board.
3. Fill the product's panels in `board_data.json` as they are learned: a `spec`
   panel for the product box (the canonical packshot and its dimensions), then
   Frame rules / Clip rules lists after each round (SYSTEM.md §2.1).
4. Tell Daniel to open the board once in Chrome and click **Connect
   board_notes.txt (once)**, picking `content/_board_thumbs/board_notes.txt`.

## 2. Plan a video

Decide the hook and the shots before generating anything. Shot ids: C01 the
hook, C02–C04 B-roll 1 (the product), C05–C07 B-roll 2 (the payoff) — adapt
the count per product, but keep one fixed slot list per product. To repeat a
shot from an earlier video, follow CLAUDE.md rule 3: paste its prompt verbatim
from `prompts.md § Verified record`, change only the nouns that must change,
same model and settings.

## 3. Round 1 — frames, then Daniel reviews

For every shot of the video:

1. Generate the start frame on Higgsfield (one generation per shot, then stop).
2. Download the result into `content/video_N_assets/starting_frames/vN_cNN_gK.png`
   — next free take number, never overwrite (NAMING.md §4).
3. Save the job record as JSON: the generation object Higgsfield returns
   (`show_generation_by_ids` / `job_display` for that job id) → a scratch file
   (the session's own workspace; it is needed only for the next command — the
   card keeps everything that matters, so later calls can leave `--frame` out).
4. Add the card:

   ```
   python3 x_systems/video_boards/tools/add_card.py PRODUCT --video N --shot cNN \
       --group "B-roll 1" --title "Hands on the box" --desc "<one line: what happens>" \
       --frame content/video_N_assets/starting_frames/vN_cNN_g1.png=<scratch>/job.json \
       --media <media id>=<file you attached, e.g. product_images/box_g1.png> \
       [--lane-title "<hook name>" --caption "<on-screen text>"]      (first card of a video)
   ```

   The card is `FRAME FOR REVIEW`. Its drawer holds the attachments in the order
   they were sent and the job's exact prompt.
5. Append the take to `content/video_N_assets/prompts.md` (NAMING.md §5): file,
   job id, settings, attachments, prompt, and later Daniel's verdict.
6. Run the checks (§7), then tell Daniel: "Video N — 7 frames waiting for review."

Daniel opens the board, presses **Review**, clicks Approve / Reject on each card,
then **Copy decisions** and pastes the lines into the chat.

## 4. Applying Daniel's decisions

```
python3 x_systems/video_boards/tools/decide.py PRODUCT "APPROVE v18_c02_g1.png" "REJECT v18_c03_g1.png — hands too big"
```

(Or save the pasted lines in a scratch file and pass its path.)
Approved cards turn `FRAME APPROVED` (or `APPROVED` for clips). Rejected cards
turn `REJECTED` and carry Daniel's reason in their notes.

For each rejection: re-roll that one shot — same start conditions, fix only what
the reason names (CLAUDE.md "A fix is a prompt edit") — save it as the next take
(`g2`), then:

```
python3 x_systems/video_boards/tools/add_card.py PRODUCT --video N --shot cNN --group ... --title ... --desc ... \
    --frame content/video_N_assets/starting_frames/vN_cNN_g2.png=<new job.json> --replaced "Daniel: hands too big"
```

The old take moves to "Other takes on disk" with the reason; the card is back
to FOR REVIEW. Record the verdict in `prompts.md`.

## 5. Round 2 — clips, then Daniel reviews

Only when **every** frame of the video is approved:

1. Animate each approved frame (the frame is the start image). Reuse the proven
   clip prompt of the same slot (rule 3) and its model and settings.
2. Download to `content/video_N_assets/clips/vN_cNN_gK.mp4` (next free take).
3. Save the video job record JSON, then:

   ```
   python3 x_systems/video_boards/tools/add_card.py PRODUCT --video N --shot cNN --group ... --title ... --desc ... \
       --clip content/video_N_assets/clips/vN_cNN_g1.mp4=<video job.json> --media <start image id>=vN_cNN_g2.png
   ```

   Without `--frame` the card keeps its approved frame and its prompt, and every
   detail added by hand (`variant`, `tip`, `count_note`, extra tags). The tool
   refuses a clip unless the card's frame files are exactly the ones Daniel
   approved - a new `--frame` together with `--clip` is refused, because the
   approval belongs to the frame file, not to the shot. The card is `CLIP FOR REVIEW`.
4. Daniel reviews; apply with `decide.py` as in §4. A rejected clip is re-rolled
   on the **same approved frame** — only the prompt changes — then `add_card.py
   … --clip <g2>=… --replaced "<reason>"`.
   **Motion transfer (Genjutsu `hf_mult_motion_control` and the like)** makes the
   clip straight from a driving video — there is no start frame, so the shot has one
   approval: the clip. Put the driving video in `references/vN_cNN_rK.mp4` first, then

   ```
   python3 x_systems/video_boards/tools/add_card.py PRODUCT --video N --shot cNN --group Hook --title ... --desc ... \
       --clip content/video_N_assets/clips/vN_cNN_g1.mp4=<video job.json> \
       --driver content/video_N_assets/references/vN_cNN_r1.mp4 \
       --media <video id>=content/video_N_assets/references/vN_cNN_r1.mp4 --media <image id>=<image file>
   ```

   **Columns layout** (SYSTEM.md §2.6 - one column per run: reference / new woman + room / final
   video): before generating, each run is a card at stage `refs` with its `driver` and `looks`
   (the r2 woman, the r3 room, ...) and the planned prompt in its drawer. Daniel approves or rejects
   the pictures (`APPROVE vN_cNN_r2.png`, applied with `decide.py`); only approved runs are generated,
   then `add_card.py ... --clip ... --driver ...` turns the card into stage `clip` (it keeps `looks`;
   it refuses while the refs are not approved, unless Daniel said `--force`).
   The card is `CLIP FOR REVIEW`. Only our generated clip is shown: where a generated
   start frame normally sits (`GENERATED CLIP`) and again in the clip strip underneath.
   The driving video is never shown on the card - only in the Prompts drawer's
   attachments. This works the same on every board. A re-roll
   is `--clip <g2>=… --replaced "<reason>"`, `--driver` carries over.
5. When a clip is approved and upscaled, the upscale keeps the exact name in
   `clips/upscaled/`; re-run `add_card.py` with the same `--clip` and
   `--status approved`: the card plays the upscale and its info line gains
   `· 2K <w>×<h>`.

## 6. After the edit — the finished video

1. Export lands in `videos_to_post/video_N.mp4`.
2. In `board_data.json`, lane N: `"final": "videos_to_post/video_N.mp4"`, the
   `caption` (the on-screen text, read off the export), and meta rows Status
   `Exported · Mon DD` (→ `Posted · Mon DD` only when Daniel says it is posted),
   Hook, Song, Runtime and Resolution (`ffprobe` the export).
3. Every card of the video is `clip` / `approved`; give each shot's `take` its
   `info` line with the 2K size if upscaled.
4. `prompts.md`: add the `## Verified record` for the video (NAMING.md §5).
5. `build_board.py PRODUCT`, then the checks.

## 7. Finishing checks — every time something changed

```
python3 x_systems/video_boards/tools/build_board.py PRODUCT   # exit 0 = data valid, board written
python3 _tool/check_naming.py
python3 _tool/make_thumbs.py
python3 _tool/mark_lost.py
python3 _tool/check_board.py
```

All exit 0 or the job is not done. Report the exit codes. `mark_lost.py` only
checks (it never edits a board): it fails when a board still points at a file that
is gone - listed in `lost_takes.txt` → rebuild the board; not listed → restore the
file or record it. A mistyped product filter exits 2 ("nothing was checked") on
every tool, never 0.

Writing on this drive: the tools verify their own writes. To change
`board_data.json` by hand, do it as a read-modify-write script in the drive's
shell (`python3 - <<'EOF' … json.load … json.dump … EOF`), never by pasting the
file's content through a file-writing tool (the mount has truncated such writes),
then run `build_board.py PRODUCT` — it refuses invalid data — and compare md5s
of anything you copied in.

## 8. Higgsfield — finding which job made a file

New work records the job at download time (§3), so this is only for audits and
recovery.

1. Page through the history with `show_generations` (`type` video, then image;
   `size` 100; pass `next_cursor` as `cursor` until the dates are covered). Each
   page is saved as JSON by the chat; the drive's shell must be able to read
   them, so copy them into a temporary `_tmp_claude/` folder at the drive root.
   Remove it when done: ask Daniel for delete permission for the session, or
   move it into `to_delete/` and tell him.
2. `python3 x_systems/video_boards/tools/match_media.py PRODUCT <pages> <out> --md5 --media`
   → `matches.json` (file → job; clips md5-checked), `media.json` (attachment id →
   local file), `report.txt` (what did not match).
3. Evidence rules: a clip is "the same" only when its md5 equals the Higgsfield
   result; an image when its byte size equals the result's; an attachment when its
   bytes match, or its picture matches within 0.10 (40×72 grey). A clip that is a
   re-encoded copy can still be tied to its job when the job's prompt equals the
   recorded prompt **and** its start image is the card's frame — say so on the card
   (`matched by prompt + start frame`). Anything weaker: keep the old text and label
   it `text from the old board · no matching Higgsfield job found`.
4. Where the board and Higgsfield disagree, Higgsfield wins; write each correction
   under "Board corrections" in that video's `prompts.md § Verified record`.

## 9. When something breaks

| symptom | fix |
|---|---|
| `video_board.html` broken, deleted or hand-edited | `build_board.py PRODUCT` — the page is rebuilt from `board_data.json` exactly |
| `board_data.json` damaged or deleted, board still fine | `extract_board.py PRODUCT --write` (add `--force` to replace a damaged one), then `build_board.py PRODUCT` and compare md5: the rebuilt page is byte-identical. (Empty panels are not on the page, so a rescue cannot bring those back — re-add them if needed.) |
| both gone | rebuild the data from the product's `prompts.md § Verified record` files (every card's frames, clip, prompts, settings, attachments are there), using `add_card.py` per shot with job records re-fetched from Higgsfield (§8) |
| the template files are damaged | every built board carries the full stylesheet and script: copy the text between `<style>` and `</style>` into `template/board.css` and between `<script>` and `</script>` into `template/board.js` (take them from the newest board), then rebuild |
| build refuses: "file not found" | the path is wrong or the file really is gone. Wrong → fix the path in the data. Gone → add its name to `content/lost_takes.txt` (with Daniel's knowledge) and rebuild: the card shows it greyed "take lost" |
| a thumbnail is missing or stale | `python3 _tool/make_thumbs.py PRODUCT` (a file renamed or swapped in place keeps its old time: `touch` it first) |
| notes seem lost | they are in the browser (`vb.notes.<key>`) and in `content/_board_thumbs/board_notes.txt`; reconnecting the file merges both, never drops text |
| a tool says `… .building already exists` | another session is writing that file right now, or an interrupted run left it behind: wait, or move the `.building` file to `to_delete/`, then rerun |
| `board_data.json changed since this command read it` | another session saved first; nothing was written - run the command again on the new data |
| a card says `no prompt block for …` | every generated frame and clip on a card needs its prompt (§3 step 4); for a real historical gap add a `notes` block titled "No image prompt on record" / "No clip prompt on record" |
| Daniel's clicks do not appear | decisions are per browser; ask him for the copied lines — the lines are the record |

## 10. Rules that keep boards identical

- Only `build_board.py` writes `video_board.html`. Change content in
  `board_data.json` (by hand or with `add_card.py` / `decide.py`), design in
  `template/`.
- One card per shot per video; take numbers always match the file names.
- Prompts are pasted from the Higgsfield job, never retyped.
- A rejected take is never deleted from disk or from the record — it moves to
  "Other takes on disk".
- After a template change, rebuild **all** boards and the example.
