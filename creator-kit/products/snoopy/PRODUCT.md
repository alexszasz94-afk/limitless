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
| snoopy_box_display | refs/box-display-camel.jpg (Alex chose the CAMEL one, 28 Oct; the red one is not used) | NEW 28 Oct (Alex: "the Snoopy box like the HeatGrump one"): tall display box with a window, the robe inside with the hood on top, "HEATPUP" at the bottom — use it for every box/unboxing hook. Lettering on packaging: make/fix it with `gpt_image_2_5` (quality high) — nano_banana misspells it (HEATTPUP/HEATGPUP). |

## Fixed clips (already made — never generate again)
- `fixed/connector-tree-1.mp4`, `-2` — grey connector pushed fully in, close-up next to the Christmas tree, woman's hands + Snoopy sleeve, 4K, 4 s. ROTATION (Alex 28 Oct): `tools.py next-set snoopy` says which one; use **1.2–4.0** (fully joined at ~3.0 s, then held — never cut before). Never generate a new connector. (`fixed/connector-and-remote.mp4` = old one, not used.)
- `fixed/remote-tree-1.mp4` — THE ONLY Snoopy remote (Alex 28 Oct: "la snoopy folosim doar a doua telecomanda"): white remote close-up next to the silver Christmas tree with the Snoopy sleeve, 4K, 1.9 s, lights go up. ROTATION (Alex 28 Oct): `tools.py next-set snoopy` says which one; use the whole clip 0–1.9. Never generate a new remote. (`fixed/remote-closeup.mp4` = old one, not used.)

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

Prompt — THE PROVEN ONE (rule 28 Oct, Alex: "no mistakes on the Snoopy B-roll"). It made all 7 Snoopy B-rolls of lot28 right on the first try. Copy it WORD FOR WORD; fill ONLY `<outfit>`. NEVER add, remove or "improve" a sentence (no hem/feet/knees sentences, no extra room description, rule 3b sentences do NOT go here) — every addition so far made it worse (28 Oct test: added sentences → pants/knees showing, 3 B-rolls paid).
```
Edit the input video. Keep EXACTLY the same four shots, the same cuts, the same camera position and framing, the same body movements and the same timing as the input video. Change only the person, the room and the robe. PERSON: exactly the woman of Image 1, same face; under the robe she wears <outfit, long pajamas or long lounge pants, e.g. red buffalo-plaid long pajamas>, the same in every shot. ROOM: exactly the living room of Image 2, only what is in Image 2, soft daylight; shots 3 and 4 happen on its sofa; nothing stands between the camera and her in shot 2, her whole body down to the floor is visible. ROBE: exactly the robe of Images 3-6, reproduced one to one in every frame: light camel-brown ribbed plush outside with the same embroidered motifs, white fluffy sherpa lining, white fluffy trim on the front edges, cuffs, pockets and hem, long to the ankles. HOOD: exactly Image 6 (front) and Image 5 (back): white fluffy dog face with black nose, closed-eye line and smile line, two long black floppy ears, red Santa hat with white brim and pom-pom; from behind only the camel back of the hood with the ears and the hat; a real 3D sewn hood. SHOT 1: seen from behind, she pulls the hood up. SHOT 2: facing the camera, hood up, she opens the robe wide showing the white lining. THE FOOT POUCH exactly as Image 7: one wide pouch across the whole width at the inside of the hem, open only at the top, camel outside, white fluffy trim on top. Both her feet start OUTSIDE the pouch on the floor; then she lifts her right foot over the white top edge into the right half of the pouch, then her left foot over the top edge into the left half; no foot is ever inside before she puts it in; then she closes the robe. SHOT 3: she lies on the sofa wrapped in the closed robe, hood up. SHOT 4: she sits on the sofa leaning back, wrapped in the robe, hood up. UGC style, natural, real iPhone 17 Pro Max video, very soft natural daylight plus warm tree lights, low contrast, true colours, no HDR, no glow, no CGI look. Smooth natural movements with real weight, no morphing, no flicker. Correct hands with five fingers. No text, no logos. Silent.
```
(Room is a bedroom with no sofa → replace "its sofa" and "the sofa" with "its bed" / "the bed", nothing else.)

CHECK (skill `check`, every frame at 5 fps) — what is RIGHT and what is WRONG for Snoopy:
- RIGHT (approved, keep it): in shot 2 she steps into the pouch over its top edge and her feet are visible while she does it — that is the action Alex approved on every video.
- WRONG → regenerate once with the SAME prompt (Kling varies; never change the words): wrong face/robe/hood, a different room, a foot going in THROUGH the fabric, a foot outside the pouch AFTER it went in, empty pouch at the end of shot 2, pants/knees/legs visible in shot 3 or 4.
- If shot 4 shows pants/knees: end the edit on the lying shot (shot 3) instead of the cozy-zoom — never regenerate for it more than once.

After it finishes: `python3 engine/tools.py cuts output/<name>/broll.mp4` → you get 3 cuts (≈0.9, 3.5, 4.8). Then `python3 engine/tools.py cozy output/<name>/broll.mp4 output/<name>/cozy-zoom.mp4 <last cut + 0.15>`.


**Foot pouch:** already inside the proven prompt above — nothing to add.

## Standard edit order (ALWAYS this order: hook → puts it on → foot pockets → connector → remote → cozy) (edit.json segments)
1. hook clip(s) with `"audio": true`
2. broll.mp4 `0.15 → first cut of shot 3` (≈ 0.15–3.46) — robe on + pouch
3. fixed/connector-tree-N.mp4 `1.2 → 4.0` (N from next-set, rotation)
4. fixed/remote-tree-N.mp4 whole clip (N from next-set, rotation)
5. broll.mp4 shot 3 (lying) `cut2 + 0.05 → cut3 - 0.05` (≈ 3.54–4.79)
6. cozy-zoom.mp4 `0 → 2.1`

Texts: `"size": 76, "y": 0.08` (high, so it never covers the face), 2–3 lines with `\n`. Second text (call to action) starts at the lying shot.
Proven text examples: `DONT Show this to a\nSNOOPY LOVER...🎄🐶` · `Snoopy girlies, pls\ndon't hate... 🥺🐶` + `Comment "SNOOPY" if\nyou want one! 🐶` · `Burger King\nX\nSNOOPY 🐶🎄` + `Jk, we make them 🤭\n(Link in bio)` · `H&M X SNOOPY\n🤩🐶`.
