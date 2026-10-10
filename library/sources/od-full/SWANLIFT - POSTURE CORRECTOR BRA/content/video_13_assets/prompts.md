# Video 13 — Genjutsu recast of @gercekform reel DdWgodhFPg5 (rank 24)

**Current status (2026-10-06, put back):** CLIP FOR DANIEL'S REVIEW AGAIN: `clips/v13_c01_g2.mp4` (the cut 14.2 s version) was put back from `to_delete/` at Daniel's request (2026-10-06: "Add back v2 and v13 so I can review them one more time"). Same file, md5 `42881ef76faaaaad1b4807a877f8f2d7`. The full 23.9 s reel was refused by Higgsfield twice (nsfw).

_Previous status (2026-10-06):_ NO CLIP. The cut 14.2 s version `clips/v13_c01_g2.mp4` was removed at Daniel's request (2026-10-06: "remove the final video for video 13 since the length it's not good") - moved to `to_delete/` at the drive root and listed in `content/lost_takes.txt`. The full 23.9 s reel was refused by Higgsfield twice (nsfw). `clips/v13_c01_g1.mp4` (the raw 15 s run of the cut driving video) stays on disk as a record.

_Previous status (2026-10-05):_ CLIP FOR DANIEL'S REVIEW: `clips/v13_c01_g2.mp4` — generated 2026-10-05 after Daniel's "Now transform them into videos". One Genjutsu run. Plan A (the whole 23.8 s reel) was refused (nsfw, no credits); plan B — without the bust close-ups (10.30–18.03 s) and the hand on the chest (19.60–21.57 s) — passed.

## Source reel

- **Reel:** https://www.instagram.com/reel/DdWgodhFPg5/ · @gercekform
- **Views:** 196,438 · 23.9 s · rank 24 of 82 in `competition/all_competitors_ranked/data.md` (scraped 2026-10-05); one of the next five in `competition/selected` by views after the first ten
- **File:** `competition/selected/rank_24_gercekform_DdWgodhFPg5.mp4` · md5 `904286d15a9c6b329f51d632b4a43f89` · copied byte-identical to `references/v13_c01_r1.mp4`
- **On-screen text in the reel:** Turkish captions burned in, lower third, changing every few seconds ("SAATLERCE BÖYLE DURDUĞUNUZU FARK ETMİYORSUNUZ!" …)
- **Original look:** Young woman with a full bust, dark hair in a messy bun, a tattoo on her shoulder; black trousers; living room with sheer curtains and warm afternoon light. Nude bra only, mostly close framing; she talks to camera.

### Shot analysis

Cuts found with ffmpeg scene detection and checked frame by frame (frame numbers at 30 fps):

- **0.00–3.67 s** (frames 0–109) — nude, side view at a laptop, rubbing her shoulder
- **3.67–5.73 s** (frames 110–171) — nude, front, pulls it over her head
- **5.73–10.30 s** (frames 172–308) — nude, back view adjusting, turns side-on, poses
- **10.30–15.83 s** (frames 309–474) — nude, close-up of the bust, straps forward, fastening the hook band — **cut out**
- **15.83–18.03 s** (frames 475–540) — nude, close, adjusting the shoulder straps — **cut out**
- **18.03–19.60 s** (frames 541–587) — nude, back view, crossing the straps
- **19.60–21.57 s** (frames 588–646) — nude, side, talking, hand on her chest — **cut out**
- **21.57–22.57 s** (frames 647–676) — nude, front, OK gestures
- **22.57–23.17 s** (frames 677–694) — nude, front, gesture
- **23.17–23.80 s** (frames 695–713) — nude, hands to her hair

**Cut out before generating:** the close-ups of the bust (10.30–18.03 s) and the hand on the chest (19.60–21.57 s). Plan A sends the whole reel first (a refusal costs nothing); plan B, below, is the cut version if it is refused.

## New character and room (picked 2026-10-05, for review)

- **Woman (second pick, 2026-10-05):** `references/v13_c01_r5.png` · Pinterest pin https://www.pinterest.com/pin/112308584465152422/ · phone selfie, 1080×1920. Prompt description: "woman around thirty with a messy, textured dark brown bob, warm brown eyes, a big natural smile and a curvy figure with a full bust". Why: Natural, unretouched-looking phone selfie of a woman about 30 in a knitted sweater — a dark bob and a big smile instead of the original's bun and tattoo.
- **Room:** `references/v13_c01_r3.png` · Pinterest pin https://www.pinterest.com/pin/578853358402615627/ · prompt description: "a cosy bedroom in soft daylight: a double bed with white bedding and a cream knitted throw, a wooden bench with a wicker basket at the foot of the bed, a window with sheer curtains and trees outside, a large plant and a framed landscape print". Why: Soft daylight and sheer curtains keep the original mood, in a bedroom instead of a living room.
- **Lower body in every shot:** loose black trousers
- **First pick, rejected by Daniel 2026-10-05:** `references/v13_c01_r2.png` — "The characters used for video 11 to 15 are not good. I want hyper realistic characters. Use terms like 30 years old women, don't look for specifically ai generated". The first picks had been limited to images with AI evidence; the second search used "30 year old woman" style terms and any Pinterest image.

## C01 — plan (DRAFT, not submitted)

Genjutsu motion transfer (`hf_mult_motion_control`), 720p, one run over the whole reel (one colour). The driving videos are already cut (local work, no credits); nothing is submitted until Daniel approves the woman and the room.

### Run 1 — nude — driving video `references/v13_c01_r4.mp4` (built, not submitted)

Frames 0–713 (0.00–23.80 s) of `references/v13_c01_r1.mp4` · 23.80 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `9c864a78f3154a37187fe7cbe934b011`. Attachments in order: @Video1 this driving video, @Image1 `references/v13_c01_r5.png`, @Image2 `references/v13_c01_r3.png`, @Image3 `references/bra_nude_flat.png` (product folder), @Image4 `references/bra_back_nude.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with a messy, textured dark brown bob, warm brown eyes, a big natural smile and a curvy figure with a full bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black trousers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. She already wears the nude posture bra at the start. Keep every cut of @Video1: first, seen from the side, she rubs her shoulder; then, facing the camera, she pulls the bra down over her head; then, seen from behind and from the side, she settles it and poses; then, facing the camera close up, she brings the long straps forward, fastens the hook band under her bust and adjusts the shoulder straps; then, seen from behind, she crosses the long straps; at the end she talks to the camera, gestures and touches her hair.

Every shot takes place in the room from @Image2: a cosy bedroom in soft daylight: a double bed with white bedding and a cream knitted throw, a wooden bench with a wicker basket at the foot of the bed, a window with sheer curtains and trees outside, a large plant and a framed landscape print. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

**Plan B if the whole reel is refused:** driving video frames 0–308 (0.00–10.30 s) + 541–587 (18.03–19.60 s) + 647–713 (21.57–23.80 s) (14.10 s), same prompt with the close-up sentence taken out.

### Take history

- nude run · driving video `references/v13_c01_r4.mp4` · job `40b04d25-6cbd-4698-a01c-32bfa8363a2b` · status **nsfw** — refused, no file, no credits charged.
- **Whole reel again, one run (Daniel 2026-10-05: "I want you to generate the entire video in one run")** · driving video `references/v13_c01_r4.mp4` (whole reel, 23.8 s) · prompt and attachments identical to the first whole-reel run · job `8187c9b3-9198-48a7-8d5d-6a8969b4bc59` · status **nsfw** — refused again, no file, no credits charged.
- `clips/v13_c01_g1.mp4` · nude run · driving video `references/v13_c01_r6.mp4` · job `cb5b862b-8e89-4c63-9ecd-c2b81583b6d3` · md5 `56edfd6773c193d786d7085474076750` · 15.04 s · trimmed to make the clip in review
- `clips/v13_c01_g2.mp4` · assembled · md5 `42881ef76faaaaad1b4807a877f8f2d7` · 340 frames, 14.17 s · **waiting for Daniel's review**

## C01 — generated 2026-10-05

- Extra driving video `references/v13_c01_r6.mp4` · frames 0–308 + 541–587 + 647–713 + filler 0–26 · 15.00 s · md5 `29dac0781c00f8a130365ae84a046156` (cut from `references/v13_c01_r1.mp4`, H.264 CRF 14 + AAC 192k)

**Assembly of `clips/v13_c01_g2.mp4`** (24 fps, reel order):

| # | colour | source frames | reel sound (s) |
|---|---|---|---|
| 1 | nude | `v13_c01_g1.mp4` 0–339 | the run's own sound, 0.000–14.167 |

The last 0.87 s of the run (the throw-away filler shot that pads the driving video to 15 s) is cut off. The clip jumps at 12.33 s (7.4 s of bust close-ups removed) and at 13.5 s (the hand-on-chest shot removed).

### Video prompt — nude run · job `40b04d25` (refused) (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with a messy, textured dark brown bob, warm brown eyes, a big natural smile and a curvy figure with a full bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black trousers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. She already wears the nude posture bra at the start. Keep every cut of @Video1: first, seen from the side, she rubs her shoulder; then, facing the camera, she pulls the bra down over her head; then, seen from behind and from the side, she settles it and poses; then, facing the camera close up, she brings the long straps forward, fastens the hook band under her bust and adjusts the shoulder straps; then, seen from behind, she crosses the long straps; at the end she talks to the camera, gestures and touches her hair.

Every shot takes place in the room from @Image2: a cosy bedroom in soft daylight: a double bed with white bedding and a cream knitted throw, a wooden bench with a wicker basket at the foot of the bed, a window with sheer curtains and trees outside, a large plant and a framed landscape print. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Video prompt — nude run · job `cb5b862b` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with a messy, textured dark brown bob, warm brown eyes, a big natural smile and a curvy figure with a full bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black trousers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. She already wears the nude posture bra at the start. Keep every cut of @Video1: first, seen from the side, she rubs her shoulder; then, facing the camera, she pulls the bra down over her head; then, seen from behind and from the side, she settles it and poses; then, seen from behind, she crosses the long straps; at the end she talks to the camera, gestures and touches her hair.

Every shot takes place in the room from @Image2: a cosy bedroom in soft daylight: a double bed with white bedding and a cream knitted throw, a wooden bench with a wicker basket at the foot of the bed, a window with sheer curtains and trees outside, a large plant and a framed landscape print. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

## Note on the product references

`product_images/` is empty, so the bra references come from Pinterest (AliExpress listing photos of this same bra, a curvy-faja.com leopard front, an inspireuplift.com black flat-lay); the per-colour back views are crops of `references/bra_back_three_colours.png`.

## Verified record — Higgsfield

### C01 — assembled clip (in review) — no single job

- `clips/v13_c01_g2.mp4` · md5 `42881ef76faaaaad1b4807a877f8f2d7` · built from the runs below (cut list in § C01 — generated)


### C01 — nude run — job `cb5b862b-8e89-4c63-9ecd-c2b81583b6d3`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_184731_cb5b862b-8e89-4c63-9ecd-c2b81583b6d3.mp4
- **On disk:** `clips/v13_c01_g1.mp4` · md5 `56edfd6773c193d786d7085474076750` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `b135f171-08fb-4492-9318-c11a4d936bdf` · `references/v13_c01_r6.mp4`
  - image · media `4e52458f-10a2-44d4-b9bc-a7abc2d8bf5d` · `references/v13_c01_r5.png`
  - image · media `0eff9fc2-8eed-4b86-ae05-54cc3855b696` · `references/v13_c01_r3.png`
  - image · media `b7938776-24d0-4faa-a5ab-49a2c29965aa` · `references/bra_nude_flat.png` (product folder)
  - image · media `0585d4e5-d4e4-44f0-87a5-16d7921f9e59` · `references/bra_back_nude.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with a messy, textured dark brown bob, warm brown eyes, a big natural smile and a curvy figure with a full bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black trousers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. She already wears the nude posture bra at the start. Keep every cut of @Video1: first, seen from the side, she rubs her shoulder; then, facing the camera, she pulls the bra down over her head; then, seen from behind and from the side, she settles it and poses; then, seen from behind, she crosses the long straps; at the end she talks to the camera, gestures and touches her hair.

Every shot takes place in the room from @Image2: a cosy bedroom in soft daylight: a double bed with white bedding and a cream knitted throw, a wooden bench with a wicker basket at the foot of the bed, a window with sheer curtains and trees outside, a large plant and a framed landscape print. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### C01 — nude run — job `40b04d25-6cbd-4698-a01c-32bfa8363a2b`

- **Status:** nsfw (refused by Higgsfield; no video, no credits charged)
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `9af4a0c4-fc59-4af5-974e-e5773e72c604` · `references/v13_c01_r4.mp4`
  - image · media `4e52458f-10a2-44d4-b9bc-a7abc2d8bf5d` · `references/v13_c01_r5.png`
  - image · media `0eff9fc2-8eed-4b86-ae05-54cc3855b696` · `references/v13_c01_r3.png`
  - image · media `b7938776-24d0-4faa-a5ab-49a2c29965aa` · `references/bra_nude_flat.png` (product folder)
  - image · media `0585d4e5-d4e4-44f0-87a5-16d7921f9e59` · `references/bra_back_nude.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with a messy, textured dark brown bob, warm brown eyes, a big natural smile and a curvy figure with a full bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black trousers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. She already wears the nude posture bra at the start. Keep every cut of @Video1: first, seen from the side, she rubs her shoulder; then, facing the camera, she pulls the bra down over her head; then, seen from behind and from the side, she settles it and poses; then, facing the camera close up, she brings the long straps forward, fastens the hook band under her bust and adjusts the shoulder straps; then, seen from behind, she crosses the long straps; at the end she talks to the camera, gestures and touches her hair.

Every shot takes place in the room from @Image2: a cosy bedroom in soft daylight: a double bed with white bedding and a cream knitted throw, a wooden bench with a wicker basket at the foot of the bed, a window with sheer curtains and trees outside, a large plant and a framed landscape print. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### C01 — whole reel, second try — job `8187c9b3-9198-48a7-8d5d-6a8969b4bc59`

- **Status:** nsfw (refused by Higgsfield; no video, no credits charged) · submitted 2026-10-05 · prompt and attachments byte-identical to job `40b04d25-6cbd-4698-a01c-32bfa8363a2b` above.

## Upscale (2026-10-06)

Daniel 2026-10-06: "upscale all the 13 final videos using bytedance settings". On higgsfield.ai/upscale (Chrome), settings checked on the page before submitting: ByteDance Upscale · model version Pro · resolution 2K · 30fps · preset AIGC.

- Source: `clips/v13_c01_g2.mp4` · md5 `42881ef76faaaaad1b4807a877f8f2d7` · uploaded as media `e899cdb8-a8da-4a6b-a991-257ad2443a1c`.
- Job `2152573b-25bc-4e65-b2fe-9f3ff29c1add` · result https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261006_000645_32f47bff-405e-4fb3-8d29-4e7e89f5e347.mp4
- On disk: `content/upscaled_videos/video_13.mp4` · md5 `535fb61e8e104ff4cb34df68c651028d` (same as the result URL) · 1440×2560 · 30 fps · reel sound kept
