# Snoopy heated robe (HeatPup) — everything Claude needs

## What it is
Long hooded heated robe. Outside: light camel-brown ribbed (corduroy-like) plush with embroidered dog, little yellow birds and Christmas lights. Inside: white fluffy sherpa. White fluffy trim on front edges, cuffs, pockets and hem. Hood front = white fluffy dog face, black nose, closed-eye line, smile line, two long black floppy ears, red Santa hat with white pom-pom. Inside the hem: one wide foot pocket across the whole width (camel outside, white trim on top), open only at the top. Comes with a white 5-light heating remote and a grey cable connector.

## Reference images (upload once, IDs go to state/media.json)
| key | file | use |
|---|---|---|
| snoopy_front_closed | refs/front-closed.jpg | every robe shot |
| snoopy_front_open | refs/front-open.jpg | every robe shot |
| snoopy_back | refs/back.jpg | every robe shot |
| snoopy_hood | refs/hood.jpg | every robe shot |
| snoopy_pouch | refs/pouch.jpg | B-roll only (the foot pocket) |
| snoopy_detail | refs/detail.jpg | close-ups of the fabric (connector/remote shots, bag shots) |
| snoopy_box | refs/box.jpg | the gift box (cream linen box, camel velvet ribbon, round seal) |

## Fixed clips (already made — never generate again)
- `fixed/connector-and-remote.mp4` — 0.00–1.375 s = connector clicks in; after that = remote close-up. Use **0–1.375** for the connector.
- `fixed/remote-tree-1.mp4`, `-2`, `-3` — white remote close-up next to the Christmas tree with the Snoopy sleeve (3 different trees/nails), 1.9 s, lights go up. ROTATION (Alex 28 Oct): `tools.py next-set snoopy` says which one; use the whole clip 0–1.9. Never generate a new remote. (`fixed/remote-closeup.mp4` = old one, not used.)

## Music
- `music/linus-and-lucy.mp3` — `"music_start": 0.8`, `"music_vol": 0.75`, `"orig_vol": 1.0`.

## B-roll (always new person + new room) — Kling 4.0 video-edit
Call `generate_video_batch` (or `generate_video`) with:
- `model: "kling4_0"`, `mode: "video-edit"`, `resolution: "1080p"`, `aspect_ratio: "9:16"`, `duration: 7`, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"` (if the tool answers that a preset was recommended, retry with the id it gives you).
- `medias` in THIS order:
  1. `motion` (role `video_references`)
  2. character photo (role `image_references`) = Image 1 — if she wears a skirt/shorts/dress in the photo, crop it to head + shoulders first (`tools.py crop`, see princess PRODUCT.md) so the filter does not refuse it
  3. room photo (role `image_references`) = Image 2
  4. snoopy_front_closed (role `image_references`) = Image 3
  5. snoopy_front_open (role `image_references`) = Image 4
  6. snoopy_back (role `image_references`) = Image 5
  7. snoopy_hood (role `image_references`) = Image 6
  8. snoopy_pouch (role `image_references`) = Image 7

Prompt (fill the three `<...>`; for a living room without a bed replace "bed" with "sofa" in SHOT 3 and 4):
```
Edit the input video. Keep EXACTLY the same four shots, the same cuts, the same camera position and framing, the same body movements and the same timing as the input video. Change only the person, the room and the robe.

REPLACEMENTS IN EVERY FRAME:
- PERSON: exactly the woman of Image 1 — same face, same <hair: e.g. long straight light-brown hair>, same build. Under the robe she wears <outfit: e.g. red-and-green plaid flannel Christmas pajamas>, the same in every shot. Never the woman or the clothes of the input video.
- ROOM: exactly the room of Image 2 — <describe what you SEE in the room photo: walls, windows, tree, sofa/bed, rug, lights>, soft daylight. Only what is in Image 2: do not add any furniture that is not in Image 2. Nothing stands between the camera and her in shot 2: her whole body down to the floor is visible.
- ROBE: exactly the robe of Images 3-6, reproduced one to one in every frame. Outside: light camel-brown ribbed (corduroy-like) plush with the same embroidered motifs in the same places. Inside: white fluffy sherpa lining. White fluffy trim on the front edges, cuffs, pockets and hem. Long, down to the ankles. Never the dark red robe of the input video.
- HOOD: exactly Image 6 (front) and Image 5 (back). FRONT of the hood = white fluffy face with a black nose, a closed-eye line and one smile line, two long black floppy ears on the sides, and a red Santa hat with a white fur brim and a white pom-pom sewn on top. BACK of the hood = light camel ribbed fabric like the robe, the two black ears hanging on its sides, the red Santa hat on top. The hood is a real 3D sewn hood, never a flat print, never inside-out, never upside down.

SHOT 1 (0.0-0.9 s, seen from behind): the robe is already on her shoulders and she raises both arms and pulls the hood up over her head. From behind we only ever see the OUTSIDE of the hood: the camel ribbed back of the hood with the black ears on both sides — the white lining of the hood is never visible from behind. When she pulls it up, the hood sits upright on her head: from behind we see the camel back of the hood, the black ears on both sides and the red Santa hat on top.

SHOT 2 (0.9-3.6 s, facing the camera, full body): the hood is up on her head (front face of the hood, hat, ears visible exactly as Image 6). She holds the front edges of the robe and opens it wide with both arms at shoulder height, showing the white sherpa lining. THE FOOT POCKET, exactly as in Image 7: at the bottom of the robe, on the inside, one wide deep pouch across the whole width, about 30 cm high, sewn to the hem, OPEN ONLY AT THE TOP and CLOSED AT THE BOTTOM and on both sides; outside of the pouch = light camel ribbed fabric, top edge = white fluffy trim. STEP-IN ORDER, exactly like the input video: (a) 0.9-1.9 s: she first opens only the RIGHT front panel of the robe (camera right); only the right half of the pouch is visible, lying at the hem on the floor. Her right foot lifts OVER the white top edge and goes down INTO the right half of the pouch. During this time her LEFT foot stays OUTSIDE the robe, standing on the floor clearly to the LEFT of the robe and of the pouch, fully visible next to it, never under it, never behind it. (b) 1.9-2.3 s: she opens the LEFT front panel too, so the whole pouch across the full width is visible on the floor, then lifts her left foot OVER the top edge and puts it down INTO the left half of the pouch. (c) From then on both feet are inside the pouch: the pouch shows two soft bulges where the feet are, no toes or ankles are visible anywhere below, through or behind the pouch, and the closed bottom seam of the pouch lies FLAT ON THE FLOOR with no gap. Legs and feet only ever go in over the top edge of the pouch — never through the fabric of the pouch or of the robe. Then she closes the robe around her.

SHOT 3 (3.6-4.95 s): she lies on the bed wrapped in the closed robe, hood up, the same relaxed pose as the input video.

SHOT 4 (4.95-7.3 s): she sits on the bed leaning against the pillows, wrapped in the robe, hood up, the same pose as the input video.

QUALITY: UGC style, natural, real iPhone 17 Pro Max video. LIGHT: very soft, very natural daylight from the windows plus the warm Christmas tree lights, low contrast, soft shadows, true colours; no harsh light, no HDR, no glow, no CGI look. MOTION: smooth natural movements with real weight and gravity of thick plush fabric, no morphing, no flicker, no objects changing shape between frames. Correct hands with five fingers. No text, no logos. Silent video, no sound.
```
After it finishes: `python3 engine/tools.py cuts output/<name>/broll.mp4` → you get 3 cuts (≈0.9, 3.5, 4.8). Then `python3 engine/tools.py cozy output/<name>/broll.mp4 output/<name>/cozy-zoom.mp4 <last cut + 0.15>`.


**Foot pouch — ALWAYS add this sentence to every B-roll prompt (rule 26 Oct):** `THE FOOT POUCH (one wide pouch across the whole width, open only at the top): both her feet start OUTSIDE the pouch on the floor; then she lifts her right foot over the white top edge into the right half of the pouch, then her left foot over the top edge into the left half; no foot is ever inside before she puts it in.`

## Standard edit order (ALWAYS this order: hook → puts it on → foot pockets → connector → remote → cozy) (edit.json segments)
1. hook clip(s) with `"audio": true`
2. broll.mp4 `0.15 → first cut of shot 3` (≈ 0.15–3.46) — robe on + pouch
3. fixed/connector-and-remote.mp4 `0 → 1.375`
4. fixed/remote-tree-N.mp4 whole clip (N from next-set, rotation)
5. broll.mp4 shot 3 (lying) `cut2 + 0.05 → cut3 - 0.05` (≈ 3.54–4.79)
6. cozy-zoom.mp4 `0 → 2.1`

Texts: `"size": 76, "y": 0.08` (high, so it never covers the face), 2–3 lines with `\n`. Second text (call to action) starts at the lying shot.
Proven text examples: `DONT Show this to a\nSNOOPY LOVER...🎄🐶` · `Snoopy girlies, pls\ndon't hate... 🥺🐶` + `Comment "SNOOPY" if\nyou want one! 🐶` · `Burger King\nX\nSNOOPY 🐶🎄` + `Jk, we make them 🤭\n(Link in bio)` · `H&M X SNOOPY\n🤩🐶`.
