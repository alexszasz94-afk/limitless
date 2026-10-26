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
- `fixed/connector.mp4` — lilac connector clicking in. Use **1.0–2.6**.
- `fixed/remote.mp4` — pink crystal remote, lights go up. Use **0–3.1**.

## Music
- `music/let-it-go.mp3` — the chorus ("Let it go…") hits at ≈ 58.5 s. Put it on the reveal moment: `"music_start": 58.5 - <time of the reveal in the final video>` (e.g. reveal at 1.9 s → `56.6`). `"music_vol": 0.75`, `"orig_vol": 1.0`.
- `music/princess-trend.mp3` — 15 s trending sound, `"music_start": 0`. Video can be max ~14.5 s with it.

## ⚠️ Content filter (important)
Kling sometimes refuses the princess B-roll with status `nsfw`. It does NOT cost credits (refunded). Causes: long prompts that mention bare legs, feet, toes, satin shorts, AND a character photo that shows legs (skirt, shorts, dress) — the motion clip already shows legs, the two together trigger the filter. So, EVERY time:
- **Crop the character photo to head + shoulders** before uploading it for the B-roll: look at the photo, then `python3 engine/tools.py crop library/characters/<x>.jpg output/<name>/char-face.jpg <left> <top> <right> <bottom>` (e.g. `0.15 0 0.85 0.45` — face and shoulders only, nothing below the chest). Upload that crop and use it as Image 1 in the B-roll (the full photo is still fine for hook start frames).
- Long pajama PANTS set under the robe (never shorts/skirt), and never write "bare", "legs", "toes", "satin", "skin".
- Use EXACTLY the short prompt below.
If it still says `nsfw`: (1) send the same call again once (it is random sometimes); (2) replace `wearing a <colour> long pajama set under the robe` with `wearing a <colour> long-sleeve pajama top and long pajama pants`; (3) remove Image 6 (pouch-feet) from the medias and from the prompt (keep Image 5). Never more than 5 tries — then tell the creator.

## B-roll motion clip — ONLY the classic one (rule 26 Oct)
Use only `motion` (`motion/broll-motion.mp4`, shared with Snoopy): it is tested and comes out well. Variety comes from the new person, room, outfit, hook and the custom cozy — not from other motion clips.
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

Prompt (fill the `<...>`):
```
Edit the input video. Keep exactly the same shots, cuts, framing, movements and timing. Change only the person to the woman of Image 1 (same face, wearing a <colour> long pajama set under the robe), the room to the <living room / bedroom> of Image 2, and the robe to the hooded robe of Image 3 (front) and Image 4 (back) reproduced one to one: royal-blue top with puffed red and light-blue striped shoulders, red belt with bow, long yellow lower part with gold crown border, white sherpa trim, white sherpa lining inside, blue hood with gold tiara. The foot pockets of the robe are exactly like Image 5 and Image 6: two yellow pockets with a white fluffy band on top, sewn inside at the hem, joined in the middle, open only at the top; when she opens the robe she steps into them one after the other exactly like in the input video, and then they look exactly like Image 6. UGC style, real iPhone video, soft natural light, true colours. No text. Silent.
```
After it finishes: `cuts` → ≈ 0.96, 3.58, 4.92. `cozy` from last cut + 0.15.


**Foot pockets — ALWAYS add this sentence to every B-roll prompt (rule 26 Oct):** `FOOT POCKETS, step by step: when she opens the robe, BOTH her feet are still OUTSIDE the pockets, standing on the floor in front of the hem, the two pockets are empty and flat; then she lifts one foot from the outside, over the white fluffy band, and puts it INTO one pocket; then she lifts the other foot from the outside and puts it into the other pocket. No foot is ever inside a pocket before she puts it in.`

## Standard edit order (ALWAYS this order: hook → puts it on → foot pockets → connector → remote → cozy)
1. hook clip(s) `"audio": true`
2. broll.mp4 `0.15 → ~3.5`
3. fixed/connector.mp4 `1.0 → 2.6`
4. fixed/remote.mp4 `0 → 3.1`
5. broll.mp4 lying shot `~3.62 → ~4.9`
6. cozy-zoom.mp4 `0 → 2.05`

Texts `"size": 76, "y": 0.08`. Examples: `Princess girlies, pls\ndon't hate...🥺👑` + `Comment "PRINCESS" if\nyou want one! 👑` · `Don't show this to a\nPrincess lover...🥺🌹` · `H&M X DISNEY 🤩🔔`.
