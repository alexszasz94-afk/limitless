---
name: new-video
description: Makes one finished, ready-to-post robe video (Snoopy or Princess) from an Instagram/TikTok link or a hook idea — hook start frames, hook clips, new B-roll with a new person and room, fixed connector/remote clips, trimming, edit with text and music. Run when the creator types "new video ...".
---
Work alone from start to finish. Keep the creator updated with one short line at each stage ("making the start frames…", "animating…", "editing…").

0. If `state/media.json` lacks the robe keys → run the `setup` skill first. Robe not given → ask "Snoopy or Princess?". Check `balance` (≥ 80 credits).
1. **Name**: short folder name, e.g. `snoopy-castle`, `princess-hm`. Work in `output/<name>/`.
2. **Reference**: link → `python3 engine/tools.py download <url> output/<name>/ref` and `sheet` it (1.5 fps); Read the sheet. Idea only → pick the closest proven concept in `HOOKS.md` and adapt it. Decide: hook shots (1–4), each 1.5–3.5 s in the final video, total hook 3–7 s; the on-screen text (copy the reference wording, swap the product); whether it's a "whole clip" format (no B-roll, like "It's just a robe") or the standard hook + robe part.
3. **Set**: `python3 engine/tools.py next-set` → character + room. Upload both (save ids in state/media.json). Pick an under-robe outfit (Christmas pajamas, cozy sweater set, college sweatshirt — always long pants) and describe the room from what you see in the photo.
4. **Start B-roll now** (it takes longest): exactly the B-roll recipe in `products/<robe>/PRODUCT.md`. (Skip for whole-clip formats.)
5. **Start frames**: one per hook shot, recipe in `HOOKS.md`, all in one `generate_image_batch`. Download each with `python3 engine/tools.py fetch <url> output/<name>/start-<n>.jpg`, Read and check them (rules 6 in CLAUDE.md). Redo bad ones.
6. **Animate** every good start frame (one `generate_video_batch`), recipe in `HOOKS.md`. Fetch each to `output/<name>/hook-<n>.mp4`, `sheet` at 4 fps, `safe-end`, decide start/end of the usable part. Redo bad ones (max 3 tries).
7. **B-roll**: fetch to `output/<name>/broll.mp4`, `sheet` at 2.5 fps and check robe/hood/pouch/face. `cuts` → then `cozy` from the last cut + 0.15.
8. **Edit**: write `output/<name>/edit.json` (format at the top of `engine/montage.py`) with the edit order from PRODUCT.md; hook texts end where the call-to-action starts (the lying shot), or one text for the whole video. Music from `products/<robe>/music/` (cue in PRODUCT.md; for Let It Go put the chorus on the reveal). Run `python3 engine/montage.py output/<name>/edit.json`. Whole-clip formats with ceiling-fan cuts: after montage run `python3 engine/tools.py fanwipe <final> <final-2> <cut times…>` and keep the wiped one as FINAL.
9. **Check the final**: `sheet` at 1 fps and `cuts`; text never over a face, text switches exactly on the cut, no leftover reference-photo flash, no black frames, ends cleanly. Fix and re-run if needed.
10. **Deliver** as described in CLAUDE.md (FINAL.mp4 + caption.txt + short summary).
