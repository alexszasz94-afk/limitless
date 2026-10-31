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
| snoopy_detail | refs/detail.jpg | B-roll (Image 7) + close-ups of the fabric (bag shots) |
| snoopy_box | refs/box.jpg | the gift box (cream linen box, camel velvet ribbon, round seal) |
| snoopy_box_display | refs/box-display-camel.jpg (Alex chose the CAMEL one, 28 Oct; remade with GPT Image 2.5 as a twin of the HeatGrump box) | NEW 28 Oct (Alex: "the Snoopy box like the HeatGrump one"): tall display box with a window, the robe inside with the hood on top, "HEATPUP" at the bottom — use it for every box/unboxing hook. Lettering on packaging: make/fix it ONLY with `gpt_image_2_5` (quality high). |
| snoopy_v4 | ../../motion/snoopy-v4.mp4 (video) | input of B-roll v4 |
| snoopy_v5 | ../../motion/snoopy-v5.mp4 (video) | input of B-roll v5 |
`refs/pouch.jpg` (`snoopy_pouch`) shows ANOTHER robe — never upload or use it (rule 31 Oct, Alex).

## Fixed clips — connector + remote (rule 31 Oct, Alex: ALWAYS these, never generated)
`tools.py next-set snoopy` prints which ones; log them with `connector=<file> remote=<file>`. They are used as they are — no Kling, no upscale, no edits. The B-roll v4/v5 has NO connector or remote inside (its prompt says so).
- **Default, every video:** `fixed/connector-fabric-1.mp4` (1.7 s, grey connector slides COMPLETELY in on the camel corduroy) — use **0 → 1.7**; `fixed/remote-fabric-1.mp4` (5 s, white remote, lights off, then ONE green light climbs up to 5) — use **0.3 → 3.0**.
- **Alternates, only if a fabric clip fails the check:** `fixed/connector-tree-1.mp4`, `-2` (use 1.2 → 4.0, fully joined at ~3.0 s) and `fixed/remote-tree-1.mp4` (use 0 → 1.9).
- Frozen recipe they were made with (once): `recipes/connector-remote-fabric.md` in Alex's repo. Never make a new one.

## Music — rotating Christmas pool (rule 30 Oct, Alex)
The songs live in ONE shared pool, `music/xmas/` (both robes). `tools.py next-set snoopy` picks the song (never the same as the last 2 videos) and prints the edit.json lines; log it with `song=<file>`.
- `music/xmas/mariah-all-i-want.mp3` — drop at **53.4 s**.
- `music/xmas/buble-beginning.mp3` — drop at **35.35 s**.
- `music/xmas/wham-last-christmas.mp3` — no clear drop (steady from the start): `"music_start": 0`.
- `music/xmas/let-it-go.mp3` — chorus at **58.5 s** (mostly for Princess, but in the rotation).
ONE rule for the drop (rule 31 Oct, Alex): the drop/chorus ALWAYS lands exactly on the hook → B-roll cut: `"music_start": <drop> - <hook end>`, `"music_duck": <hook end>` (quiet under the hook, full from the cut; montage.py evens out the loudness).

## B-roll (rule 31 Oct, Alex) — ONLY v4 and v5, rotating
The B-roll is made from OUR finished, approved silent B-roll (method C): Kling keeps its shots, cuts, movements and seconds, and the prompt replaces the person, the room and the robe. `tools.py next-set snoopy` says which variant (v4 / v5, never the same twice in a row); log it with `motion=v4` or `motion=v5`. The prompts below are FROZEN: copy them word for word; fill ONLY `<OUTFIT>`, `<SOFA>` and `<COZY_BG>`. Never add, remove or "improve" a sentence.
- `<OUTFIT>` = long pajamas or long lounge pants under the robe, e.g. `red buffalo-plaid long pajamas` (the same in the hook).
- `<SOFA>` = the real sofa you SEE in the room photo, where it stands, e.g. `the cream sofa under the black window on the left side of Image 2`.
- `<COZY_BG>` = what is really behind that sofa in the room photo, e.g. `the black window and the Christmas tree next to it`.
- Room: must show a SOFA clearly (the cozy shot is filmed WIDE on that real sofa). Room without a sofa → `tools.py reject` it and run next-set again. Character: real photo, light skin only (rule 31 Oct). If the photo shows legs (skirt, shorts, dress), use a head + shoulders crop as Image 1 (`tools.py crop`, see princess PRODUCT.md) so the filter does not refuse it.

**Settings (both variants):** `generate_video` with `model: "kling4_0"`, `mode: "video-edit"`, `resolution: "1080p"`, `aspect_ratio: "9:16"`, `duration`: 8 (v4) / 7 (v5) — the exact length of the motion clip, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"` (if the tool says another preset was recommended, retry with the id it gives you). No sound needed (the prompt ends with "Silent").
**`medias` in THIS order (both variants):**
1. `snoopy_v4` (or `snoopy_v5`) — role `video_references`
2. character photo (`characters[<file>]`, or the head + shoulders crop) — role `image_references` = Image 1
3. room photo with the sofa visible (`rooms[<file>]`) — role `image_references` = Image 2
4. `snoopy_front_closed` = Image 3
5. `snoopy_front_open` = Image 4
6. `snoopy_back` = Image 5
7. `snoopy_hood` = Image 6
8. `snoopy_detail` = Image 7
(all images with role `image_references`; NEVER `snoopy_pouch`)

### B-roll v4 (motion `motion/snoopy-v4.mp4`, duration 8)
Shots in the generated clip: from behind, she reaches for the hood 0–0.6 · close-up of the hood lifted 0.6–1.1 · hood up from behind (camel back with ears + Santa hat, never the dog face) 1.1–~1.7 · full body facing the camera, hood up: one foot into the pouch, robe held wide open, other foot, she wraps it closed ~1.7–5.8 · cozy: sitting WIDE on the real sofa, arms crossed holding the collar 5.8–8.0 (still from 7.8).
```
Edit the input video. Keep EXACTLY the same five shots, the same cuts, the same camera position and framing (except the last shot, which is filmed WIDE from about 3 metres away), the same body movements and the same timing as the input video, second by second; the output has exactly the same length as the input. Change only the person, the room and the robe. PERSON: exactly the woman of Image 1, same face and hair; under the robe she wears <OUTFIT>, the same in every shot. ROOM: exactly the living room of Image 2, only what is in Image 2, soft daylight; the last shot is on its sofa. THE SOFA: <SOFA>. Never add, move or invent furniture: she uses only the sofa that is already in Image 2, in its real place, seen from a camera angle where that sofa really is; the background behind her in the cozy shot is the part of Image 2 that is really behind that sofa: <COZY_BG>. ROBE: exactly the robe of Images 3-7, REPRODUCE IT ONE TO ONE in every frame: the same fabric, colours, embroidered motifs, white fluffy sherpa lining and white fluffy trims as Images 3-7. HOOD: exactly Image 6 (front) and Image 5 (back), a real 3D sewn hood.
SHOT 1 (0 to 0.6 s): close, seen from behind, the robe is already on her shoulders, the hood down on her back, she reaches up for the hood with both hands; her face is not seen.
SHOT 2 (0.6 to 1.1 s): close-up from behind of the hood being lifted up over her head.
SHOT 3 (1.1 to 1.7 s): hard cut at exactly 1.7 s, never later; the back shot never lasts longer than in the input. Seen from behind, the hood is up on her head exactly like Image 5: from behind ONLY the camel corduroy back of the hood with the two black floppy ears and the red Santa hat; the dog's face stays on the FRONT of the hood and is NEVER seen from behind; her face is not seen.
SHOT 4 (1.7 to 5.8 s): full body, she stands on the floor in the FOREGROUND facing the camera, nothing between her and the camera, the hood UP on her head (the dog-face hood exactly like Image 6), her whole face visible. Exactly like the input: the robe is open, she holds one side out and lifts one foot into the foot pouch, then she holds the robe wide open with both arms showing the white lining, she lifts the other foot into the pouch, then she wraps the robe closed and stands wrapped in it. THE FOOT POUCH: one wide pouch across the whole width at the inside of the hem, open only at the top, the robe fabric outside, white fluffy trim on top. Both her feet start OUTSIDE the pouch on the floor; she lifts her right foot over the white top edge into the right half of the pouch, then her left foot over the top edge into the left half; no foot is ever inside before she puts it in, and once a foot is in it never comes out again; the filled pouch rests on the floor with her feet inside it.
SHOT 5 (5.8 s to the end): In the final shot she is SITTING DOWN on the sofa of Image 2 - her bottom on the seat cushion, her back against the backrest, knees bent, wrapped in the robe, hood up; she is NEVER standing, never standing in front of the sofa, never between armchairs. Wide framing, about 3 metres away: the whole sofa and her full seated body, face small. The room of Image 2 around the sofa. She sits on the sofa of Image 2, wrapped in the closed robe, the hood UP on her head (the dog-face hood exactly like Image 6), and her arms crossed holding the white fluffy collar closed, smiling; her legs are completely covered by the closed robe down to the feet; no pajama pants, no knee and no foot visible. From 7.8 s to the end she holds still.
LOOK: UGC style, a real unedited iPhone 16 video of a real person in a real home, Full HD, completely realistic; warm, very soft, very natural light, diffuse daylight and the warm glow of real lamps, gentle low contrast, true slightly warm colours; no HDR, no glow, no orange cast, no CGI look. Natural real movements with real weight and gravity, no morphing, no flicker. Correct hands with five fingers. NO TEXT: the caption text of the input video is removed completely; no captions, no emoji, no subtitles, no watermark, no other logos. No cable connector and no remote anywhere. Silent.
```
**After generating — ALWAYS (rule 31 Oct, Alex):** `python3 engine/tools.py cutjerk output/<name>/broll.mp4 output/<name>/broll-cut.mp4` — cuts 3.10–3.40 s out (the robe-opening jerk) and gives one clean cut from the half-open to the fully open robe; everything after 3.40 s comes 0.30 s earlier. Check 2.7–3.5 s at 15 fps (no jerk frame). Use ONLY `broll-cut.mp4` in the edit.
**Edit times (in broll-cut.mp4, ±0.1 s — take the real cuts from `tools.py cuts`):** puts it on (back + hood) 0.10 → ~1.7 · foot pouch ~1.7 → ~5.4 (cozy cut − 0.12) · cozy ~5.6 (cozy cut + 0.12) → ~7.5.
**Check (skill `check`):** her face in every front shot; from behind never the dog face; the back shot cut not later than ~1.8 s; stepping into the pouch over its top edge with the feet visible is the APPROVED action, wrong is only a foot outside AFTER it went in; in the cozy shot she SITS on the real sofa of the room (never stands), and no pajama legs show between the robe flaps. Any fail → regenerate ONCE with the SAME prompt.

### B-roll v5 (motion `motion/snoopy-v5.mp4`, duration 7)
Shots in the generated clip: sleeves, she slides her arm in 0–1.7 (small jump cut at 1.0) · from behind, hood hanging on her back 1.7–2.5 · lying on her back on the sofa, hood up 2.5–4.3 · cozy: curled up on her side WIDE on the real sofa 4.3–7.0 (still from 6.2). No foot-pouch shot.
```
Edit the input video. Keep EXACTLY the same four shots, the same cuts, the same camera position and framing, the same body movements and the same timing as the input video, second by second; the output has exactly the same length as the input. Change only the person, the room and the robe. PERSON: exactly the woman of Image 1, same face and hair; under the robe she wears <OUTFIT>, the same in every shot. ROOM: exactly the living room of Image 2, only what is in Image 2, soft daylight; the lying shots are on its sofa. THE SOFA: <SOFA>. Never add, move or invent furniture: she uses only the sofa that is already in Image 2, in its real place, seen from a camera angle where that sofa really is; the background behind her in the cozy shot is the part of Image 2 that is really behind that sofa: <COZY_BG>. ROBE: exactly the robe of Images 3-7, REPRODUCE IT ONE TO ONE in every frame: the same fabric, colours, embroidered motifs, white fluffy sherpa lining and white fluffy trims as Images 3-7. HOOD: exactly Image 6 (front) and Image 5 (back), a real 3D sewn hood.
SHOT 1 (0 to 1.7 s, with the same small jump cut at 1.0 s): close, from the side, she slides her arm into the long sleeve of the robe and pulls the robe onto her shoulder; her face is mostly out of the frame.
SHOT 2 (1.7 to 2.5 s): close, seen from behind, the robe is on her shoulders, the hood hangs down on her back exactly like Image 5: from behind ONLY the camel corduroy back of the hood with the two black floppy ears and the red Santa hat; the dog's face stays on the FRONT of the hood and is NEVER seen from behind.
SHOT 3 (2.5 to 4.3 s): she lies stretched out on her back on the sofa of Image 2, her head on a cushion, the hood UP on her head (the dog-face hood exactly like Image 6), relaxed, pulling the robe over herself like a blanket, her face visible; her legs are completely covered by the closed robe down to the feet; no pajama pants, no knee and no foot visible.
SHOT 4 (4.3 s to the end, a SEPARATE shot with a hard cut at 4.3 s - never skip or merge this shot): THE COZY SHOT, A WIDE SHOT exactly as framed in the input: we see the whole sofa of Image 2 and her full body lying on it, her face small in the frame; the room of Image 2 around the sofa. She lies curled up on her side on the sofa of Image 2, completely wrapped in the closed robe, the hood UP on her head (the dog-face hood exactly like Image 6), eyes closed, cozy; her legs are completely covered by the closed robe down to the feet; no pajama pants, no knee and no foot visible. From 6.2 s to the end she holds still.
LOOK: UGC style, a real unedited iPhone 16 video of a real person in a real home, Full HD, completely realistic; warm, very soft, very natural light, diffuse daylight and the warm glow of real lamps, gentle low contrast, true slightly warm colours; no HDR, no glow, no orange cast, no CGI look. Natural real movements with real weight and gravity, no morphing, no flicker. Correct hands with five fingers. NO TEXT: the caption text of the input video is removed completely; no captions, no emoji, no subtitles, no watermark, no other logos. No cable connector and no remote anywhere. Silent.
```
**Edit times (±0.1 s, take the real cuts from `tools.py cuts`):** puts it on (sleeves + back) 0.10 → ~2.4 and lying ~2.6 → ~4.2 (play 0.10 → 4.18 as ONE segment) · cozy ~4.42 → ~6.9.
**Check (skill `check`):** the SAME woman (face and hair colour) in every shot — hair changing between shots = fail; from behind never the dog face; the real sofa of the room; legs always covered by the robe. Any fail → regenerate ONCE with the SAME prompt.

## Standard edit order (rule 31 Oct, Alex — ALWAYS: hook → B-roll → connector → remote → cozy)
1. hook clip(s) `"audio": true` — exactly as long as the original's hook (ends on the original's hook end)
2. B-roll part 1: v4 `broll-cut.mp4 0.10 → ~5.4` (puts it on + foot pouch) / v5 `broll.mp4 0.10 → ~4.18` (puts it on + lying)
3. `fixed/connector-fabric-1.mp4 0 → 1.7`
4. `fixed/remote-fabric-1.mp4 0.3 → 3.0`
5. B-roll cozy: v4 `broll-cut.mp4 ~5.62 → ~7.5` / v5 `broll.mp4 ~4.42 → ~6.9`
`"texts": []` — the suggested text goes in text.txt (CLAUDE.md rule 9). Proven text examples: `DONT Show this to a\nSNOOPY LOVER...🎄🐶` · `Snoopy girlies, pls\ndon't hate... 🥺🐶` + `Comment "SNOOPY" if\nyou want one! 🐶` · `Burger King\nX\nSNOOPY 🐶🎄` + `Jk, we make them 🤭\n(Link in bio)` · `H&M X SNOOPY\n🤩🐶`.
