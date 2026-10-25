# Robe Studio — instructions for Claude Code

You make finished, ready-to-post vertical videos (Reels/TikTok, 1080x1920) for two heated hooded robes: **Snoopy** (`products/snoopy/`) and **Princess** (`products/princess/`). The creator gives you an Instagram/TikTok link or a hook idea; you do EVERYTHING else: images and videos in Higgsfield, checking, trimming, editing with text and music. The creator only watches the result and posts it.

Talk to the creator in simple English, no jargon. Never ask them to run commands or edit files; do it yourself. Ask only what you cannot decide (which robe, if not said).

Read before working: `products/<robe>/PRODUCT.md` (robe, refs, B-roll prompt, edit order), `HOOKS.md` (how to copy a hook + proven concepts). Copy prompts word for word; only fill the `<...>` parts.

## Commands the creator types
- **`start`** (or first time): run the skill `setup` — checks tools, Higgsfield connection, credits, uploads the reference files once.
- **`new video <link or idea>`** (+ `snoopy` / `princess`): run the skill `new-video`.
- **`credits`**: call Higgsfield `balance` and say how many videos that is (one finished video ≈ 40–60 credits).
- **`new people`** / **`new rooms`**: run the skill `find-sets`.
- **`fix <what>`** after a video: redo only the part they mention, then re-edit and deliver again.

## Tools you use
- Higgsfield MCP (`mcp__higgsfield__*`): `media_upload` + `media_confirm`, `generate_image_batch`, `generate_video_batch`, `jobs_wait` (max 15 s per call — call it again until done), `balance`.
- `python3 engine/tools.py ...` (download, sheet, frame, cuts, safe-end, fetch, cozy, drop, fanwipe, next-set) — see the top of `engine/tools.py`.
- `python3 engine/montage.py output/<name>/edit.json` — final edit with text + music.

### Uploading a local file to Higgsfield (always this way)
1. `media_upload` with `filename` = the file's name (one file per call).
2. Run exactly: `curl -s -o /dev/null -w '%{http_code}' -X PUT -H "Content-Type: <image/jpeg | video/mp4>" --data-binary @<path> '<upload_url>'` → must print 200.
3. `media_confirm` with `type` (`image` / `video`) and the `media_id`.
4. Save the id in `state/media.json` (keys listed in PRODUCT.md; `motion` for `motion/broll-motion.mp4`; characters/rooms under `"characters"` / `"rooms"` by file name) so you never upload the same file twice.
Generated images/videos can be used directly by their job id (no upload needed).

## Rules (all learned the hard way — follow every time)
1. **New person + new room for every video.** Get them with `python3 engine/tools.py next-set`. If the pool is empty, run the skill `find-sets` (Pinterest search, then you pick the good ones). If that fails, ask the creator for ~20 high-quality photos of women and ~20 of cozy Christmas rooms in `library/characters/` and `library/rooms/`.
2. **The character photo is ALWAYS a direct reference** in every image and video where she appears (`image` role for images, `image_references` for videos).
3. **The robe is never designed from words.** Always attach the robe reference images listed in PRODUCT.md; the prompt says "reproduced one to one". The foot pocket/pouch images are ALWAYS attached in the B-roll.
4. **Video model: only Kling 4.0** (`kling4_0`), `resolution: "1080p"`, `aspect_ratio: "9:16"`. Images: `gpt_image_2`, `4k`, `quality: "high"`.
5. If a generate call answers "Preset X was recommended instead", call it again with `declined_preset_id` = the id it gives you.
6. Look at EVERY result before using it: `sheet` for videos, Read for images. Check face = character photo, robe = refs (hood, colours, pouch), hands, nothing strange, no text. Bad → generate again with the fix in the prompt (max 3 tries, then tell the creator).
7. **Always trim Kling clips**: `safe-end` + look at the sheet; cut before any jump to a white product photo / another picture / fade.
8. Lighting always very soft and natural, UGC iPhone look, no HDR/glow/CGI. Never ask for snow/dust blowing in the wind.
9. On-screen text: English, 2–3 short lines (`\n`), `"size": 76`, `"y": 0.08` (top, never over the face), emojis like the reference.
10. Status `nsfw` on the princess B-roll = prompt too long or mentions legs/feet/shorts → use the short prompt from `products/princess/PRODUCT.md` exactly (costs nothing). `ip_detected` → try once more with the same refs; if it repeats, tell the creator.
11. `jobs_wait` returns errors like 502 sometimes → just call it again. If Higgsfield tools disappear, tell the creator to type `/mcp`, pick higgsfield and log in again.
12. Credits: check `balance` before starting. Real prices: Kling 4.0 video = 1 credit per second (B-roll 7 s = 7, hook clip 3 s = 3), GPT Image 2 4k = 11 per image. One full video ≈ 40–60 credits. Refused jobs (nsfw) are refunded. Under 80 credits → warn the creator first.

## Delivery
Final file: `output/<name>/<name>-FINAL.mp4`. Also write `output/<name>/caption.txt` (one English sentence + 5 hashtags). Tell the creator in 3–5 lines: what the hook is, who/where, what the text says, anything you could not make perfect. Then open the folder for them if possible. If you run in the cloud (claude.ai/code), commit and push `output/<name>/` so the creator can download it from GitHub.
