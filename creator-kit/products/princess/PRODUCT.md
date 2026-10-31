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
| princess_v4 | ../../motion/princess-v4.mp4 (video) | input of B-roll v4 |
| princess_v5 | ../../motion/princess-v5.mp4 (video) | input of B-roll v5 |

## Fixed clips — connector + remote (rule 31 Oct, Alex: ALWAYS these, never generated)
`tools.py next-set princess` prints which ones; log them with `connector=<file> remote=<file>`. They are used as they are — no Kling, no upscale, no edits. The B-roll v4/v5 has NO connector or remote inside (its prompt says so).
- **Default, every video:** `fixed/connector-fabric-1.mp4` (1.7 s, lilac connector slides COMPLETELY in on the robe's blue velvet) — use **0 → 1.7**; `fixed/remote-fabric-1.mp4` (5 s, pink crown remote, all 5 crystal lights off, then ONE light climbs 1 → 5) — use **0.3 → 3.0**.
- **Alternates, only if a fabric clip fails the check:** `fixed/connector-tree-1.mp4`, `-2` (use 1.2 → 4.0, fully joined at ~3.0 s) and `fixed/remote-tree-1.mp4`, `-2` (use 0 → 2.95).
- Frozen recipe they were made with (once): `recipes/connector-remote-fabric.md` in Alex's repo. Never make a new one.

## Music — rotating Christmas pool (rule 30 Oct, Alex)
The songs live in ONE shared pool, `music/xmas/` (both robes). `tools.py next-set princess` picks the song (never the same as the last 2 videos) and prints the edit.json lines; log it with `song=<file>`.
- `music/xmas/let-it-go.mp3` — chorus at **58.5 s** (fits the Princess robe best).
- `music/xmas/mariah-all-i-want.mp3` — drop at **53.4 s**.
- `music/xmas/buble-beginning.mp3` — drop at **35.35 s**.
- `music/xmas/wham-last-christmas.mp3` — steady from the start: `"music_start": 0`.
ONE rule for the drop (rule 31 Oct, Alex): the drop/chorus ALWAYS lands exactly on the hook → B-roll cut: `"music_start": <drop> - <hook end>`, `"music_duck": <hook end>` (quiet under the hook, full from the cut; montage.py evens out the loudness).
- `products/princess/music/princess-trend.mp3` — 15 s trending sound, `"music_start": 0`, video max ~14.5 s; only when the creator asks for it.

## Content filter (`nsfw`, refunded, costs nothing)
Kling sometimes refuses a princess B-roll with `nsfw`. Causes: a character photo that shows legs (skirt, shorts, dress) together with the motion clip. So, EVERY time:
- If the character photo shows legs, **crop it to head + shoulders** before uploading it for the B-roll: `python3 engine/tools.py crop library/characters/<x>.jpg output/<name>/char-face.jpg <left> <top> <right> <bottom>` (e.g. `0.15 0 0.85 0.45`) and use that crop as Image 1 (the full photo is still fine for the hook).
- `<OUTFIT>` = a long pajama set (never shorts/skirt), e.g. `a red and green plaid long pajama set`.
If it still says `nsfw`: (1) send the same call again once; (2) write `<OUTFIT>` as `a <colour> long-sleeve pajama top and long pajama pants`. Never change anything else in the prompt; after 3 refusals tell the creator.

## B-roll (rule 31 Oct, Alex) — ONLY v4 and v5, rotating
The B-roll is made from OUR finished, approved silent B-roll (method C): Kling keeps its shots, cuts, movements and seconds, and the prompt replaces the person, the room and the robe. `tools.py next-set princess` says which variant (v4 / v5, never the same twice in a row); log it with `motion=v4` or `motion=v5`. The prompts below are FROZEN: copy them word for word; fill ONLY `<OUTFIT>`, `<SOFA>` and `<COZY_BG>`. Never add, remove or "improve" a sentence.
- `<OUTFIT>` = the long pajamas/lounge set under the robe (the same in the hook).
- `<SOFA>` = the real sofa you SEE in the room photo, where it stands, e.g. `the light-grey sectional sofa under the window on the right side of Image 2`.
- `<COZY_BG>` = what is really behind that sofa in the room photo, e.g. `the window with white curtains and the Christmas tree in the corner`.
- Room: must show a SOFA clearly (the cozy shot is filmed WIDE on that real sofa). Room without a sofa → `tools.py reject` it and run next-set again. Character: real photo, light skin only (rule 31 Oct).

**Settings (both variants):** `generate_video` with `model: "kling4_0"`, `mode: "video-edit"`, `resolution: "1080p"`, `aspect_ratio: "9:16"`, `duration`: 8 (v4) / 6 (v5) — the exact length of the motion clip, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"` (if the tool says another preset was recommended, retry with the id it gives you). No sound needed (the prompt ends with "Silent").
**`medias` in THIS order (both variants):**
1. `princess_v4` (or `princess_v5`) — role `video_references`
2. character photo (`characters[<file>]`, or the head + shoulders crop) — role `image_references` = Image 1
3. room photo with the sofa visible (`rooms[<file>]`) — role `image_references` = Image 2
4. `princess_front` = Image 3
5. `princess_back` = Image 4
6. `princess_pouch_open` = Image 5
7. `princess_pouch_feet` = Image 6
(all images with role `image_references`)

### B-roll v4 (motion `motion/princess-v4.mp4`, duration 8)
Shots in the generated clip: back view, she lifts the hood 0–0.8 · hood up from behind 0.8–~1.7 (hard cut at ~1.67–1.79) · full body facing the camera: one foot slides into a pocket, robe held wide open, other foot, she wraps it closed ~1.7–5.8 · cozy: sitting WIDE on the real sofa, hood up, collar to her face 5.8–8.0 (still from 7.8).
```
Edit the input video. Keep exactly the same four shots, the same cuts, the same camera position and framing (except the last shot, which is filmed WIDE from about 3 metres away), the same body movements and the same timing as the input video, second by second; the output has exactly the same length as the input. Change only the person, the room and the robe. PERSON: exactly the woman of Image 1, same face and hair; under the robe she wears <OUTFIT>, the same in every shot. ROOM: exactly the living room of Image 2, only what is in Image 2; the last shot is on its sofa. THE SOFA: <SOFA>. Never add, move or invent furniture: she uses only the sofa that is already in Image 2, in its real place, seen from a camera angle where that sofa really is; the background behind her in the cozy shot is the part of Image 2 that is really behind that sofa: <COZY_BG>. ROBE: the hooded robe of Image 3 (front) and Image 4 (back): REPRODUCE IT ONE TO ONE from Images 3-4 in every frame, every colour, every trim, the white sherpa lining and the hood with its tiara. The foot pockets are exactly like Image 5 and Image 6.
SHOT 1 (0 to 0.8 s): close, seen from behind, the robe is already on her shoulders, the hood down on her back, she lifts the hood with both hands; her face is not seen.
SHOT 2 (0.8 to 1.7 s): hard cut at exactly 1.67 s, never later; the back shot never lasts longer than in the input. Seen from behind, the hood is pulled up over her head, we see the back of the hood up on her head exactly like Image 4; her face is not seen.
SHOT 3 (1.7 to 5.8 s): full body, she stands on the floor in the FOREGROUND facing the camera, nothing between her and the camera, the hood DOWN on her back in this shot, her whole face visible. Exactly like the input: the robe is open, she holds one side out and slides one foot down behind the hem into a foot pocket, then she holds the robe wide open with both arms showing the white sherpa lining, she slides the other foot down behind the hem into the other foot pocket, then she wraps the robe closed and stands wrapped in it. THE HEM COVERS HER FEET AT ALL TIMES: the robe is extra long, its white hem lies flat on the floor all around her and touches the floor, there is NO gap between the hem and the floor, so her feet are always hidden behind the hem and inside the pockets - never visible on the floor, before, during and after she steps in, also when the robe is still closed. She slides each foot from behind the hem straight down into its pocket, so the pocket fills up and rests full on the floor; only the yellow fabric and the white fluffy band are seen on the floor, never a sock, a foot or a heel. FEET STAY IN THE POCKETS UNTIL THE END: once both feet are inside the foot pockets they never come out again.
SHOT 4 (5.8 s to the end): In the final shot she is SITTING DOWN on the sofa of Image 2 - her bottom on the seat cushion, her back against the backrest, knees bent, wrapped in the robe, hood up; she is NEVER standing, never standing in front of the sofa, never between armchairs. Wide framing, about 3 metres away: the whole sofa and her full seated body, face small. The room of Image 2 around the sofa. She sits on the sofa of Image 2, wrapped in the closed robe, the hood UP on her head (the blue hood with its gold tiara exactly like Images 3-4), and pulls the white sherpa collar up to her face with both hands and closes her eyes, smiling; her legs are completely covered by the closed robe down to the feet, the hem closed over them; no pajama pants, no knee and no foot visible. From 7.8 s to the end she holds still.
LOOK: UGC style, a real unedited iPhone 16 video of a real person in a real home, Full HD, completely realistic; warm, very soft, very natural light, diffuse daylight and the warm glow of real lamps, gentle low contrast, true slightly warm colours; no HDR, no glow, no orange cast, no CGI look. Natural real movements with real weight and gravity, no morphing, no flicker. Correct hands with five fingers. NO TEXT: the caption text of the input video is removed completely; no captions, no emoji, no subtitles, no watermark, no other logos. No cable connector and no remote anywhere. Silent.
```
**After generating — ALWAYS (rule 31 Oct, Alex):** `python3 engine/tools.py cutjerk output/<name>/broll.mp4 output/<name>/broll-cut.mp4` — cuts 3.10–3.40 s out (the robe-opening jerk) and gives one clean cut from the half-open to the fully open robe; everything after 3.40 s comes 0.30 s earlier. Check 2.7–3.5 s at 15 fps (no jerk frame). Use ONLY `broll-cut.mp4` in the edit.
**Edit times (in broll-cut.mp4, ±0.1 s — take the real cuts from `tools.py cuts`):** puts it on (back + hood) 0.10 → ~1.7 · foot pockets ~1.7 → ~5.4 (cozy cut − 0.12) · cozy ~5.6 (cozy cut + 0.12) → ~7.5.
**Check (skill `check`):** her face in every front shot; the back shot cut not later than ~1.8 s; in the cozy shot she SITS on the real sofa of the room (never stands). Any of these fails → regenerate ONCE with the SAME prompt. Feet, socks or pajama legs are NOT a fail (rule 31 Oct, Alex): only obvious long bare feet on the floor > 0.5 s → cut those frames if the cut stays clean, otherwise deliver.

### B-roll v5 (motion `motion/princess-v5.mp4`, duration 6)
Shots in the generated clip: sleeves, she slides her arm in 0–1.8 (small jump cut at 1.0) · from behind, she pulls the hood up 1.8–2.4 · lying on her back on the sofa, hood up 2.4–3.5 · cozy: curled up on her side WIDE on the real sofa 3.5–6.0 (still from 5.5). No foot-pocket shot.
```
Edit the input video. Keep exactly the same four shots, the same cuts, the same camera position and framing, the same body movements and the same timing as the input video, second by second; the output has exactly the same length as the input. Change only the person, the room and the robe. PERSON: exactly the woman of Image 1, same face and hair; under the robe she wears <OUTFIT>, the same in every shot. ROOM: exactly the living room of Image 2, only what is in Image 2; the lying shots are on its sofa. THE SOFA: <SOFA>. Never add, move or invent furniture: she uses only the sofa that is already in Image 2, in its real place, seen from a camera angle where that sofa really is; the background behind her in the cozy shot is the part of Image 2 that is really behind that sofa: <COZY_BG>. ROBE: the hooded robe of Image 3 (front) and Image 4 (back): REPRODUCE IT ONE TO ONE from Images 3-4 in every frame, every colour, every trim, the white sherpa lining and the hood with its tiara. The foot pockets are exactly like Image 5 and Image 6.
SHOT 1 (0 to 1.8 s, with the same small jump cut at 1.0 s): close, from the side, she slides her arm into the long sleeve of the robe and pulls the robe onto her shoulder; her face is mostly out of the frame.
SHOT 2 (1.8 to 2.4 s): close, seen from behind, the robe is on her shoulders and she pulls the hood up over her head, the back of the hood exactly like Image 4; her face is not seen.
SHOT 3 (2.4 to 3.5 s): she lies stretched out on her back on the sofa of Image 2, her head on a cushion, the hood UP on her head (the blue hood with its gold tiara exactly like Images 3-4), relaxed, pulling the robe over herself like a blanket, her face visible; her legs are completely covered by the closed robe down to the feet, the hem closed over them; no pajama pants, no knee and no foot visible.
SHOT 4 (3.5 s to the end, a SEPARATE shot with a hard cut at 3.5 s - never skip or merge this shot): THE COZY SHOT, A WIDE SHOT exactly as framed in the input: we see the whole sofa of Image 2 and her full body lying on it, her face small in the frame; the room of Image 2 around the sofa. She lies curled up on her side on the sofa of Image 2, completely wrapped in the closed robe, the hood UP on her head (the blue hood with its gold tiara exactly like Images 3-4), eyes closed, cozy; her legs are completely covered by the closed robe down to the feet, the hem closed over them; no pajama pants, no knee and no foot visible. From 5.5 s to the end she holds still.
LOOK: UGC style, a real unedited iPhone 16 video of a real person in a real home, Full HD, completely realistic; warm, very soft, very natural light, diffuse daylight and the warm glow of real lamps, gentle low contrast, true slightly warm colours; no HDR, no glow, no orange cast, no CGI look. Natural real movements with real weight and gravity, no morphing, no flicker. Correct hands with five fingers. NO TEXT: the caption text of the input video is removed completely; no captions, no emoji, no subtitles, no watermark, no other logos. No cable connector and no remote anywhere. Silent.
```
**Edit times (±0.1 s, take the real cuts from `tools.py cuts`):** puts it on (sleeves + hood) 0.10 → ~2.3 and lying ~2.5 → ~3.4 (play 0.10 → 3.38 as ONE segment) · cozy ~3.62 → ~5.9.
**Check (skill `check`):** the SAME woman (face and hair colour) in every shot; the real sofa of the room. Any fail → regenerate ONCE with the SAME prompt (feet/legs showing are not a fail, rule 31 Oct, Alex).

## Standard edit order (rule 31 Oct, Alex — ALWAYS: hook → B-roll → connector → remote → cozy)
1. hook clip(s) `"audio": true` — exactly as long as the original's hook (ends on the original's hook end)
2. B-roll part 1: v4 `broll-cut.mp4 0.10 → ~5.4` (puts it on + foot pockets) / v5 `broll.mp4 0.10 → ~3.38` (puts it on + lying)
3. `fixed/connector-fabric-1.mp4 0 → 1.7`
4. `fixed/remote-fabric-1.mp4 0.3 → 3.0`
5. B-roll cozy: v4 `broll-cut.mp4 ~5.62 → ~7.5` / v5 `broll.mp4 ~3.62 → ~5.9`
`"texts": []` — the suggested text goes in text.txt (CLAUDE.md rule 9). Text examples: `Princess girlies, pls\ndon't hate...🥺👑` · `Don't show this to a\nPrincess lover...🥺🌹` · `H&M X DISNEY 🤩🔔`.
