# Video 15 — Genjutsu recast of @thevareny reel DdhBZveIPNK (rank 30)

**Current status (2026-10-05):** CLIP FOR DANIEL'S REVIEW: `clips/v15_c01_g4.mp4` — generated 2026-10-05 after Daniel's "Now transform them into videos". 3 Genjutsu runs, one per bra colour, cut back together in reel order with the reel's own sound. All three runs passed first time.

## Source reel

- **Reel:** https://www.instagram.com/reel/DdhBZveIPNK/ · @thevareny
- **Views:** 181,212 · 20.8 s · rank 30 of 82 in `competition/all_competitors_ranked/data.md` (scraped 2026-10-05); one of the next five in `competition/selected` by views after the first ten
- **File:** `competition/selected/rank_30_thevareny_DdhBZveIPNK.mp4` · md5 `323b52f8fee5bd2456ec7ba75213a60f` · copied byte-identical to `references/v15_c01_r1.mp4`
- **On-screen text in the reel:** "POV: I found the only thing that can save my posture 😮‍💨" (burned in, top centre)
- **Original look:** Young Black woman with long box braids; taupe trousers with leopard and nude, white pleated skirt with black; bright room with white walls, a window and plants. Try-on edit, colours switch on the cuts.

### Shot analysis

Cuts found with ffmpeg scene detection and checked frame by frame (frame numbers at 30 fps):

- **0.00–0.80 s** (frames 0–23) — leopard, hands on an old strapless bra at her chest — **cut out**
- **0.80–2.50 s** (frames 24–74) — leopard, front, over the head
- **2.50–4.30 s** (frames 75–128) — nude, front, over the head
- **4.30–6.67 s** (frames 129–199) — black, front, over the head
- **6.67–7.73 s** (frames 200–231) — leopard, back view, pulling it over her head
- **7.73–10.33 s** (frames 232–309) — leopard, back view, pulling the long straps
- **10.33–12.97 s** (frames 310–388) — black, back view, straps
- **12.97–15.87 s** (frames 389–475) — nude, back view, straps, turns to look over her shoulder
- **15.87–17.50 s** (frames 476–524) — leopard, front, fastening the hook band
- **17.50–19.27 s** (frames 525–577) — leopard, close-up of the bust, hands on the cups — **cut out**
- **19.27–20.63 s** (frames 578–618) — leopard, back view, hands on her shoulders

**Cut out before generating:** 0.00–0.80 s (hands on an old strapless bra at her chest) and 17.50–19.27 s (close-up of the bust, hands on the cups).

## New character and room (picked 2026-10-05, for review)

- **Woman (second pick, 2026-10-05):** `references/v15_c01_r7.png` · Pinterest pin https://www.pinterest.com/pin/1106055989768659353/ · casual photo at home on a sofa, 784×1373. Prompt description: "Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure". Why: Slim like the original, about 30, with a short natural afro instead of long box braids. Casual at-home photo in a grey T-shirt and jeans — very natural, nothing posed.
- **Room:** `references/v15_c01_r3.png` · Pinterest pin https://www.pinterest.com/pin/1104578246139816018/ · prompt description: "a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug". Why: Bright and lived-in like the original room with plants, but a warmer city living room with a big window.
- **Lower body in every shot:** high-waisted blue jeans
- **First pick, rejected by Daniel 2026-10-05:** `references/v15_c01_r2.png` — "The characters used for video 11 to 15 are not good. I want hyper realistic characters. Use terms like 30 years old women, don't look for specifically ai generated". The first picks had been limited to images with AI evidence; the second search used "30 year old woman" style terms and any Pinterest image.

## C01 — plan (DRAFT, not submitted)

Genjutsu motion transfer (`hf_mult_motion_control`), 720p, one run per bra colour: each driving video holds only that colour's shots, joined, padded with a throw-away filler shot to whole seconds (Genjutsu rounds its output to whole seconds); the runs are cut back together in reel order with the reel's own sound — the method that fixed v9, v2 and v10. The driving videos are already cut (local work, no credits); nothing is submitted until Daniel approves the woman and the room.

### Run 1 — leopard — driving video `references/v15_c01_r4.mp4` (built, not submitted)

Frames 24–74 (0.80–2.50 s) + 200–309 (6.67–10.33 s) + 476–524 (15.87–17.50 s) + 578–618 (19.27–20.63 s) + filler 75–93 (2.50–3.13 s) of `references/v15_c01_r1.mp4` · 9.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `8ff3a0a18b73fab941b64f8cfa4beb01`. Attachments in order: @Video1 this driving video, @Image1 `references/v15_c01_r7.png`, @Image2 `references/v15_c01_r3.png`, @Image3 `references/bra_leopard_front.png` (product folder), @Image4 `references/bra_back_leopard.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head; then, seen from behind, she pulls it over her head and pulls and crosses the long straps; then, facing the camera, she fastens the hook band under her bust; in the last shot, seen from behind, she rests her hands on her shoulders.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Run 2 — nude — driving video `references/v15_c01_r5.mp4` (built, not submitted)

Frames 75–128 (2.50–4.30 s) + 389–475 (12.97–15.87 s) + filler 129–137 (4.30–4.60 s) of `references/v15_c01_r1.mp4` · 5.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `05e8e05d04ead0d10e9c2c364e826968`. Attachments in order: @Video1 this driving video, @Image1 `references/v15_c01_r7.png`, @Image2 `references/v15_c01_r3.png`, @Image3 `references/bra_nude_flat.png` (product folder), @Image4 `references/bra_back_nude.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps and turns to look over her shoulder.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Run 3 — black — driving video `references/v15_c01_r6.mp4` (built, not submitted)

Frames 129–199 (4.30–6.67 s) + 310–388 (10.33–12.97 s) of `references/v15_c01_r1.mp4` · 5.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `f2b1394ad77995282b3f21c695f7339e`. Attachments in order: @Video1 this driving video, @Image1 `references/v15_c01_r7.png`, @Image2 `references/v15_c01_r3.png`, @Image3 `references/bra_black_flat.png` (product folder), @Image4 `references/bra_back_black.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head; then, seen from behind, she pulls and crosses the long straps.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

**Reel order after the runs:** 0.80–2.50 s leopard · 2.50–4.30 s nude · 4.30–6.67 s black · 6.67–10.33 s leopard · 10.33–12.97 s black · 12.97–15.87 s nude · 15.87–17.50 s leopard · 19.27–20.63 s leopard.

### Take history

- `clips/v15_c01_g1.mp4` · leopard run · driving video `references/v15_c01_r4.mp4` · job `f5c9e195-ae1d-4f2d-b4d2-41d72e46d08b` · md5 `0cb533182ad1455bde055e3dc27cdd51` · 9.04 s · part of the assembly
- `clips/v15_c01_g2.mp4` · nude run · driving video `references/v15_c01_r5.mp4` · job `0170c80b-3ece-44d4-8d6d-c72c51cd3eab` · md5 `616f5580d78deb6a1210cf774ccbb6ab` · 5.04 s · part of the assembly
- `clips/v15_c01_g3.mp4` · black run · driving video `references/v15_c01_r6.mp4` · job `7d02cb84-2084-422b-bed5-96666f77bd70` · md5 `ce6b30c088372aaa014e26665234321b` · 5.04 s · part of the assembly
- `clips/v15_c01_g4.mp4` · assembled · md5 `821014256f9908d1467db93c6476c426` · 436 frames, 18.17 s · **waiting for Daniel's review**

## C01 — generated 2026-10-05


**Assembly of `clips/v15_c01_g4.mp4`** (24 fps, reel order):

| # | colour | source frames | reel sound (s) |
|---|---|---|---|
| 1 | leopard | `v15_c01_g1.mp4` 0–41 | 0.800–2.550 |
| 2 | nude | `v15_c01_g2.mp4` 0–43 | 2.500–4.333 |
| 3 | black | `v15_c01_g3.mp4` 0–56 | 4.300–6.675 |
| 4 | leopard | `v15_c01_g1.mp4` 42–128 | 6.667–10.292 |
| 5 | black | `v15_c01_g3.mp4` 57–119 | 10.333–12.958 |
| 6 | nude | `v15_c01_g2.mp4` 44–112 | 12.967–15.842 |
| 7 | leopard | `v15_c01_g1.mp4` 129–168 | 15.867–17.533 |
| 8 | leopard | `v15_c01_g1.mp4` 169–202 | 19.267–20.683 |

Every join checked frame by frame.

### Video prompt — leopard run · job `f5c9e195` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head; then, seen from behind, she pulls it over her head and pulls and crosses the long straps; then, facing the camera, she fastens the hook band under her bust; in the last shot, seen from behind, she rests her hands on her shoulders.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Video prompt — nude run · job `0170c80b` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps and turns to look over her shoulder.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Video prompt — black run · job `7d02cb84` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head; then, seen from behind, she pulls and crosses the long straps.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

## Note on the product references

`product_images/` is empty, so the bra references come from Pinterest (AliExpress listing photos of this same bra, a curvy-faja.com leopard front, an inspireuplift.com black flat-lay); the per-colour back views are crops of `references/bra_back_three_colours.png`.

## Verified record — Higgsfield

### C01 — assembled clip (in review) — no single job

- `clips/v15_c01_g4.mp4` · md5 `821014256f9908d1467db93c6476c426` · built from the runs below (cut list in § C01 — generated)


### C01 — leopard run — job `f5c9e195-ae1d-4f2d-b4d2-41d72e46d08b`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183556_f5c9e195-ae1d-4f2d-b4d2-41d72e46d08b.mp4
- **On disk:** `clips/v15_c01_g1.mp4` · md5 `0cb533182ad1455bde055e3dc27cdd51` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `7cabe4f4-f4f6-4aea-a4d8-3621da5e9fa6` · `references/v15_c01_r4.mp4`
  - image · media `82a6c769-c383-49b6-a29f-4a8270236495` · `references/v15_c01_r7.png`
  - image · media `8c5aeaae-3682-407e-822c-de65fe46ab48` · `references/v15_c01_r3.png`
  - image · media `edef02a5-72c0-4b25-896f-3e38f77c9da1` · `references/bra_leopard_front.png` (product folder)
  - image · media `ca6e7a8c-80bc-47e1-8a86-3695200d1b38` · `references/bra_back_leopard.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head; then, seen from behind, she pulls it over her head and pulls and crosses the long straps; then, facing the camera, she fastens the hook band under her bust; in the last shot, seen from behind, she rests her hands on her shoulders.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### C01 — nude run — job `0170c80b-3ece-44d4-8d6d-c72c51cd3eab`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183556_0170c80b-3ece-44d4-8d6d-c72c51cd3eab.mp4
- **On disk:** `clips/v15_c01_g2.mp4` · md5 `616f5580d78deb6a1210cf774ccbb6ab` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `fa09435b-72f2-4a48-ac49-b7dec889fe9f` · `references/v15_c01_r5.mp4`
  - image · media `82a6c769-c383-49b6-a29f-4a8270236495` · `references/v15_c01_r7.png`
  - image · media `8c5aeaae-3682-407e-822c-de65fe46ab48` · `references/v15_c01_r3.png`
  - image · media `b7938776-24d0-4faa-a5ab-49a2c29965aa` · `references/bra_nude_flat.png` (product folder)
  - image · media `0585d4e5-d4e4-44f0-87a5-16d7921f9e59` · `references/bra_back_nude.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps and turns to look over her shoulder.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### C01 — black run — job `7d02cb84-2084-422b-bed5-96666f77bd70`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183557_7d02cb84-2084-422b-bed5-96666f77bd70.mp4
- **On disk:** `clips/v15_c01_g3.mp4` · md5 `ce6b30c088372aaa014e26665234321b` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `035ba1fb-1f99-4e1c-9b81-e1512129209a` · `references/v15_c01_r6.mp4`
  - image · media `82a6c769-c383-49b6-a29f-4a8270236495` · `references/v15_c01_r7.png`
  - image · media `8c5aeaae-3682-407e-822c-de65fe46ab48` · `references/v15_c01_r3.png`
  - image · media `cd6c941a-bcaf-47a3-9592-6499e4497d0c` · `references/bra_black_flat.png` (product folder)
  - image · media `78454e62-a5a0-421c-b8db-205026282d19` · `references/bra_back_black.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a Black woman around thirty with short natural afro hair, warm dark-brown skin, a gentle smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head; then, seen from behind, she pulls and crosses the long straps.

Every shot takes place in the room from @Image2: a cosy, lived-in city apartment living room in daylight: a big window looking onto red-brick buildings, a cream sofa with a knitted throw, a round wooden coffee table with books and flowers, a record player on a wooden cabinet, a hanging plant and a jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

## Upscale (2026-10-06)

Daniel 2026-10-06: "upscale all the 13 final videos using bytedance settings". On higgsfield.ai/upscale (Chrome), settings checked on the page before submitting: ByteDance Upscale · model version Pro · resolution 2K · 30fps · preset AIGC.

- Source: `clips/v15_c01_g4.mp4` · md5 `821014256f9908d1467db93c6476c426` · uploaded as media `061aa320-a585-45a2-a604-d185e7279338`.
- Job `707c6509-ddee-4a8d-9ef0-1f2fdbabf59c` · result https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261006_000715_a804f96a-af96-480d-b706-4cb9d34af834.mp4
- On disk: `content/upscaled_videos/video_15.mp4` · md5 `63e837a346b0a7ead8dac3ce84c2f12f` (same as the result URL) · 1440×2560 · 30 fps · reel sound kept
