# Princess heated robe — everything Claude needs

## What it is
Long hooded heated robe in classic fairy-tale princess colours. Royal-blue plush top and long sleeves, puffed shoulders with red and light-blue stripes, white fluffy cuffs with a gold embroidered band, red velvet belt with a bow and two tassels, long bright-yellow plush lower part down to the floor with a gold crown-and-heart border at the hem, small gold crown emblem on the chest, white fluffy sherpa trim and white sherpa lining inside, royal-blue pointed hood with a gold embroidered tiara. Inside the hem: two yellow foot pockets with a white fluffy band on top, joined in the middle, open only at the top. Comes with a pink crystal remote (5 lights) and a lilac cable connector.

## Reference images (upload once, IDs go to state/media.json)
| key | file | use |
|---|---|---|
| princess_front | refs/front.jpg | every robe shot |
| princess_back | refs/back.jpg | every robe shot |
| princess_pouch_open | refs/pouch-open.jpg | B-roll (robe held open, foot pockets) |
| princess_pouch_feet | refs/pouch-feet.jpg | B-roll (both feet in the pockets) |

## Fixed clips (already made — never generate again)
- `fixed/connector-tree-1.mp4`, `-2` — lilac connector pushed fully in, close-up next to the Christmas tree, woman's hands + princess sleeve, 4K, 4 s. ROTATION (Alex 28 Oct): `tools.py next-set princess` says which one; use **1.2–4.0** (fully joined at ~3.0 s, then held — never cut before). Never generate a new connector. (`fixed/connector.mp4` = old one, not used.)
- `fixed/remote-tree-1.mp4`, `-2` — pink crystal remote close-up next to the Christmas tree (2 different trees/nails), 4K, lights go up. ROTATION (Alex 28 Oct): `tools.py next-set princess` says which one; use the whole clip **0–2.95**. Never generate a new remote. (`fixed/remote.mp4` = old one, not used.)

## Music — rotating Christmas pool (rule 30 Oct, Alex)
The songs live in ONE shared pool, `music/xmas/` (both robes). `tools.py next-set princess` picks the song (never the same as the last 2 videos) and prints the edit.json lines; log it with `song=<file>`.
- `music/xmas/let-it-go.mp3` — chorus at **58.5 s** (fits the Princess robe best; put the chorus on the reveal/drop).
- `music/xmas/mariah-all-i-want.mp3` — drop at **53.4 s**.
- `music/xmas/buble-beginning.mp3` — drop at **35.35 s**.
- `music/xmas/wham-last-christmas.mp3` — steady from the start: `"music_start": 0`.
Rule 28 Oct still applies: quiet under the hook (`music_duck` = hook end, `music_hook_vol` 0.2), louder from the drop at the hook → B-roll cut (`music_start = drop - hook end`).
- `music/princess-trend.mp3` (in products/princess/music/) — 15 s trending sound, `"music_start": 0`, video max ~14.5 s; only when the creator asks for it.

## ⚠️ Content filter (important)
Kling sometimes refuses the princess B-roll with status `nsfw`. It does NOT cost credits (refunded). Causes: long prompts that mention bare legs, feet, toes, satin shorts, AND a character photo that shows legs (skirt, shorts, dress) — the motion clip already shows legs, the two together trigger the filter. So, EVERY time:
- **Crop the character photo to head + shoulders** before uploading it for the B-roll: look at the photo, then `python3 engine/tools.py crop library/characters/<x>.jpg output/<name>/char-face.jpg <left> <top> <right> <bottom>` (e.g. `0.15 0 0.85 0.45` — face and shoulders only, nothing below the chest). Upload that crop and use it as Image 1 in the B-roll (the full photo is still fine for hook start frames).
- Long pajama PANTS set under the robe (never shorts/skirt), and never write "bare", "legs", "toes", "satin", "skin".
- Use EXACTLY the short prompt below.
If it still says `nsfw`: (1) send the same call again once (it is random sometimes); (2) replace `wearing a <colour> long pajama set under the robe` with `wearing a <colour> long-sleeve pajama top and long pajama pants`; (3) remove Image 6 (pouch-feet) from the medias and from the prompt (keep Image 5). Never more than 5 tries — then tell the creator.

## B-roll motion clips
`motion` (classic, `motion/broll-motion.mp4`, shared with Snoopy) and `motion2` alternate (see below).
**Second motion (28 Oct, Alex): `motion2` = `motion/broll-motion-2.mp4` (6 s, from instagram.com/p/De-wL1DSEhY): back shot putting the hood on → front, opens the robe and steps into the pockets → sitting cozy on the sofa. ROTATION (Alex 28 Oct: "il facem prin rotatie"): `motion` and `motion2` alternate video by video — `tools.py next-set princess` says which one; log it with `motion=<key>`. Same medias and prompt, `duration: 6`, BUT replace the FOOT POCKETS sentence with: `THE HEM COVERS HER FEET AT ALL TIMES: the robe is extra long, its white hem lies flat on the floor all around her and touches the rug, there is NO gap between the hem and the floor, so her feet are always hidden behind the hem and inside the pockets - never visible on the floor, before, during and after she steps in, also when the robe is still closed. She slides each foot from behind the hem straight down into its pocket, so the pocket fills up; only the yellow fabric and the white band are seen on the floor, never a sock, a foot, a heel or a toe.` (with motion2 the old sentence "feet OUTSIDE ... standing on the floor" made socks show before they went in — Alex 28 Oct). Cuts ≈ 1.29 (back→front), 2.46, 4.42 (→ sofa); edit: broll 0.15→1.2 + 1.35→4.35, cozy 4.55→5.9. Check the pocket shot at 15 fps: no sock/foot under the hem.**
**Room check (sofa or bed)** — see "Room check" in CLAUDE.md: the last cozy shot must match the room.

## B-roll (always new person + new room) — Kling 4.0 video-edit
`model: "kling4_0"`, `mode: "video-edit"`, `resolution: "1080p"`, `aspect_ratio: "9:16"`, `duration: 7`, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"` (if the tool says another preset was recommended, retry with the id it gives you).
`medias` in THIS order:
1. `motion` (role `video_references`)
2. character photo CROPPED to head + shoulders (role `image_references`) = Image 1
3. room photo (role `image_references`) = Image 2
4. princess_front (role `image_references`) = Image 3
5. princess_back (role `image_references`) = Image 4
6. princess_pouch_open (role `image_references`) = Image 5
7. princess_pouch_feet (role `image_references`) = Image 6

Prompt — THE PROVEN ONE for the classic `motion` (tested 28 Oct, first try right: same face, real room, robe one to one, both feet go in and stay in, legs covered in the lying and sitting shots, no nsfw). Copy it WORD FOR WORD; fill ONLY `<colour>` and `<living room / bedroom>`. Never add sentences (no "bare", "toe", "legs", "skin"). Her stepping into the pockets with her feet visible is the RIGHT action (like Snoopy).
```
Edit the input video. Keep exactly the same shots, cuts, framing, movements and timing. Change only the person to the woman of Image 1 (same face, wearing a <colour> long pajama set under the robe), the room to the <living room / bedroom> of Image 2, and the robe to the hooded robe of Image 3 (front) and Image 4 (back) reproduced one to one: royal-blue top with puffed red and light-blue striped shoulders, red belt with bow, long yellow lower part with gold crown border, white sherpa trim, white sherpa lining inside, blue hood with gold tiara. The foot pockets of the robe are exactly like Image 5 and Image 6: two yellow pockets with a white fluffy band on top, sewn inside at the hem, joined in the middle, open only at the top; when she opens the robe she steps into them one after the other exactly like in the input video, and then they look exactly like Image 6. FOOT POCKETS, step by step: when she opens the robe, BOTH her feet are still OUTSIDE the pockets, standing on the floor in front of the hem, the two pockets are empty and flat; then she lifts one foot from the outside, over the white fluffy band, and puts it INTO one pocket; then she lifts the other foot from the outside and puts it into the other pocket. No foot is ever inside a pocket before she puts it in. FEET STAY IN THE POCKETS UNTIL THE END: once both feet are inside the foot pockets they never come out again; in the lying shot and in the sitting shot her legs are completely covered by the closed robe from the hips down to the feet, the hem closed over them; no pajama pants and no knee is ever visible outside the robe. UGC style, real iPhone video, soft natural light, true colours. No text. Silent.
```
After it finishes: `cuts` → ≈ 0.96, 3.58, 4.92. `cozy` from last cut + 0.15.


**Foot pockets:** already inside the proven prompt above — nothing to add (for `motion2` use the HEM sentence from the motion2 paragraph instead).

## B-roll variants 3-5 (rule 30 Oct, Alex: 4 rotating B-roll variants so the videos are not all the same)
The B-roll now ROTATES over the variants (`tools.py next-set princess` says which one; log `motion=<key>`): classic `motion`, `motion2`, and the three NEW variants below, copied from reference reels. **The prompts are FROZEN in `recipes/` (repo root) — copy them word for word, fill only the `<...>` parts; PRODUCT.md does not duplicate them.**
- **Variant 3** — `motion/broll-motion-3.mp4` (12 s, from instagram.com/p/DdZxYkctpt1). Recipe: `recipes/broll-princess-v3.md`. Segments in the generated clip: back 0-1.0, put-on + foot pockets 1.0-6.7, CONNECTOR close-up 6.7-7.5, REMOTE close-up 7.5-10.0, cozy sitting 10.0-12.0.
- **Variant 4** — `motion/broll-motion-4.mp4` (12 s, from instagram.com/p/Dc3sRnKtTw0). Recipe: `recipes/broll-princess-v4.md`. Segments: back + hood up 0-1.7, put-on + pockets 1.7-5.8, CONNECTOR 5.8-7.3, REMOTE 7.3-9.3, cozy 9.3-12.0.
- **Variant 5** — `motion/broll-motion-5.mp4` (11 s, from instagram.com/p/Dco0N-Ctps-). Recipe: `recipes/broll-princess-v5.md`. Segments: sleeves 0-1.8, back 1.8-2.5, lying 2.5-4.2, CONNECTOR 4.2-5.0, REMOTE 5.0-7.1, lying hood up 7.1-9.1, cozy sitting 9.1-11.0. No foot-pocket shot (the reference has none).
With variants 3-5 the CONNECTOR and REMOTE close-ups are generated INSIDE the B-roll itself (our lilac connector + pink crown remote as image refs, rule 30 Oct) - do NOT add the fixed tree clips to the edit. With the old `motion`/`motion2` variants they still come from `fixed/connector-tree-N.mp4` / `remote-tree-N.mp4` as before. Edit order stays hook -> put on -> pockets -> connector -> remote -> cozy, all inside the one B-roll clip (trim 0.12 s around its cuts; check the end for a flash).

## Standard edit order (ALWAYS this order: hook → puts it on → foot pockets → connector → remote → cozy)
1. hook clip(s) `"audio": true`
2. broll.mp4 `0.15 → ~3.5`
3. fixed/connector-tree-N.mp4 `1.2 → 4.0` (N from next-set, rotation)
4. fixed/remote-tree-N.mp4 `0 → 2.95` (N from next-set, rotation)
5. broll.mp4 lying shot `~3.62 → ~4.9`
6. cozy-zoom.mp4 `0 → 2.05`

Texts `"size": 76, "y": 0.08`. Examples: `Princess girlies, pls\ndon't hate...🥺👑` + `Comment "PRINCESS" if\nyou want one! 👑` · `Don't show this to a\nPrincess lover...🥺🌹` · `H&M X DISNEY 🤩🔔`.
