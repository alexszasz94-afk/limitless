# Video 11 — Genjutsu recast of @thevareny reel DdrfZrYogDl (rank 21)

**Current status (2026-10-05):** CLIP FOR DANIEL'S REVIEW: `clips/v11_c01_g4.mp4` — generated 2026-10-05 after Daniel's "Now transform them into videos". 3 Genjutsu runs, one per bra colour, cut back together in reel order with the reel's own sound. Known problem: in the black run she wears a white long-sleeved top under the bra (Genjutsu took it from somewhere in her picture's styling); the nude and leopard shots show bare skin.

## Source reel

- **Reel:** https://www.instagram.com/reel/DdrfZrYogDl/ · @thevareny
- **Views:** 208,524 · 13.4 s · rank 21 of 82 in `competition/all_competitors_ranked/data.md` (scraped 2026-10-05); one of the next five in `competition/selected` by views after the first ten
- **File:** `competition/selected/rank_21_thevareny_DdrfZrYogDl.mp4` · md5 `fd925f75755d038e7b1e1a82df07b2a9` · copied byte-identical to `references/v11_c01_r1.mp4`
- **On-screen text in the reel:** "The perfect modest gym bra doesn't exist.." (burned in, top centre)
- **Original look:** Young slim woman with tanned skin and a slicked-back bun; a different bottom per colour (grey leggings with nude, leopard trousers with leopard, jeans with black); bedroom with bookshelves and a desk lamp. Fast try-on edit, colour switches on the cuts.

### Shot analysis

Cuts found with ffmpeg scene detection and checked frame by frame (frame numbers at 30 fps):

- **0.00–1.07 s** (frames 0–31) — nude, front, pulls it over her head
- **1.07–2.57 s** (frames 32–76) — leopard, front, pulls it over her head
- **2.57–3.30 s** (frames 77–98) — black, front, over the head
- **3.30–5.97 s** (frames 99–178) — black, arms up, side, then back view pulling it down
- **5.97–7.30 s** (frames 179–218) — leopard, back view, pulling the long straps
- **7.30–8.37 s** (frames 219–250) — black, back view, straps
- **8.37–9.27 s** (frames 251–277) — nude, back view, straps
- **9.27–10.17 s** (frames 278–304) — nude, front, bringing the straps forward
- **10.17–11.80 s** (frames 305–353) — leopard, close-up of the bust, fastening the hook band — **cut out**
- **11.80–13.30 s** (frames 354–398) — nude, front, talking, hands gesturing, touches the cups at the end

**Cut out before generating:** the leopard close-up of the bust while she fastens the hook band (10.17–11.80 s) — the kind of shot that made Higgsfield refuse v1, v2 and v10.

## New character and room (picked 2026-10-05, for review)

- **Woman (second pick, 2026-10-05):** `references/v11_c01_r7.png` · Pinterest pin https://www.pinterest.com/pin/1082904672936262751/ · photorealistic full-body photo in a living room, 1536×2752. Prompt description: "woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure". Why: Slim like the original, about 30, but a wavy bob instead of a slicked-back bun. Full-body photo in a fitted cream top and dark jeans, so her build and height are clear.
- **Room:** `references/v11_c01_r3.png` · Pinterest pin https://www.pinterest.com/pin/354236326965499520/ · prompt description: "a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug". Why: An ordinary, real-looking bedroom with open floor and daylight from one window — the original is a lived-in bedroom too, but this one is calmer and brighter; no mirror.
- **Lower body in every shot:** high-waisted dark blue jeans
- **First pick, rejected by Daniel 2026-10-05:** `references/v11_c01_r2.png` — "The characters used for video 11 to 15 are not good. I want hyper realistic characters. Use terms like 30 years old women, don't look for specifically ai generated". The first picks had been limited to images with AI evidence; the second search used "30 year old woman" style terms and any Pinterest image.

## C01 — plan (DRAFT, not submitted)

Genjutsu motion transfer (`hf_mult_motion_control`), 720p, one run per bra colour: each driving video holds only that colour's shots, joined, padded with a throw-away filler shot to whole seconds (Genjutsu rounds its output to whole seconds); the runs are cut back together in reel order with the reel's own sound — the method that fixed v9, v2 and v10. The driving videos are already cut (local work, no credits); nothing is submitted until Daniel approves the woman and the room.

### Run 1 — nude — driving video `references/v11_c01_r4.mp4` (built, not submitted)

Frames 0–31 (0.00–1.07 s) + 251–304 (8.37–10.17 s) + 354–398 (11.80–13.30 s) + filler 32–50 (1.07–1.70 s) of `references/v11_c01_r1.mp4` · 5.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `ab32aab76c85fdcb1559dca830a56f7e`. Attachments in order: @Video1 this driving video, @Image1 `references/v11_c01_r7.png`, @Image2 `references/v11_c01_r3.png`, @Image3 `references/bra_nude_flat.png` (product folder), @Image4 `references/bra_back_nude.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps down; then, facing the camera, she brings the long straps forward; in the last shot, facing the camera, she talks and smooths the bra with her hands.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Run 2 — leopard — driving video `references/v11_c01_r5.mp4` (built, not submitted)

Frames 32–76 (1.07–2.57 s) + 179–218 (5.97–7.30 s) + filler 77–111 (2.57–3.73 s) of `references/v11_c01_r1.mp4` · 4.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `8de1b2aeb292f9c23ab8654be7a67739`. Attachments in order: @Video1 this driving video, @Image1 `references/v11_c01_r7.png`, @Image2 `references/v11_c01_r3.png`, @Image3 `references/bra_leopard_front.png` (product folder), @Image4 `references/bra_back_leopard.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head; then, seen from behind, she pulls the long straps and crosses them behind her back.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Run 3 — black — driving video `references/v11_c01_r6.mp4` (built, not submitted)

Frames 77–178 (2.57–5.97 s) + 219–250 (7.30–8.37 s) + filler 251–266 (8.37–8.90 s) of `references/v11_c01_r1.mp4` · 5.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `1b72b964b09fd0287d06cc95ca980571`. Attachments in order: @Video1 this driving video, @Image1 `references/v11_c01_r7.png`, @Image2 `references/v11_c01_r3.png`, @Image3 `references/bra_black_flat.png` (product folder), @Image4 `references/bra_back_black.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the black bra down over her head; then, turned sideways and then with her back to the camera, she pulls it down and settles it; then, seen from behind, she pulls the long straps.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

**Reel order after the runs:** 0.00–1.07 s nude · 1.07–2.57 s leopard · 2.57–5.97 s black · 5.97–7.30 s leopard · 7.30–8.37 s black · 8.37–10.17 s nude · 11.80–13.30 s nude.

### Take history

- `clips/v11_c01_g1.mp4` · nude run · driving video `references/v11_c01_r4.mp4` · job `e6870484-b0fb-4f41-9ff2-ba31114e1ac0` · md5 `543a3033647a1bcb877880cd945e644f` · 5.04 s · part of the assembly
- `clips/v11_c01_g2.mp4` · leopard run · driving video `references/v11_c01_r5.mp4` · job `9646ea5a-5c8e-4350-bed2-617305cee9eb` · md5 `999cacb2ae4195faa21f709ed7e0cd96` · 4.04 s · part of the assembly
- `clips/v11_c01_g3.mp4` · black run · driving video `references/v11_c01_r6.mp4` · job `5e27d806-9f59-4ab5-a625-9a7bcb88cf80` · md5 `4851106709cde787d1a1a80d72db7afb` · 5.04 s · part of the assembly
- `clips/v11_c01_g4.mp4` · assembled · md5 `09d46e67b4bbffd156bd5e3ce99c3731` · 280 frames, 11.67 s · **waiting for Daniel's review**

## C01 — generated 2026-10-05


**Assembly of `clips/v11_c01_g4.mp4`** (24 fps, reel order):

| # | colour | source frames | reel sound (s) |
|---|---|---|---|
| 1 | nude | `v11_c01_g1.mp4` 0–24 | 0.000–1.042 |
| 2 | leopard | `v11_c01_g2.mp4` 0–35 | 1.067–2.567 |
| 3 | black | `v11_c01_g3.mp4` 0–81 | 2.567–5.983 |
| 4 | leopard | `v11_c01_g2.mp4` 36–66 | 5.967–7.258 |
| 5 | black | `v11_c01_g3.mp4` 82–107 | 7.300–8.383 |
| 6 | nude | `v11_c01_g1.mp4` 25–68 | 8.367–10.200 |
| 7 | nude | `v11_c01_g1.mp4` 69–104 | 11.800–13.300 |

Every join checked frame by frame.

### Video prompt — nude run · job `e6870484` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps down; then, facing the camera, she brings the long straps forward; in the last shot, facing the camera, she talks and smooths the bra with her hands.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Video prompt — leopard run · job `9646ea5a` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head; then, seen from behind, she pulls the long straps and crosses them behind her back.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### Video prompt — black run · job `5e27d806` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the black bra down over her head; then, turned sideways and then with her back to the camera, she pulls it down and settles it; then, seen from behind, she pulls the long straps.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

## Note on the product references

`product_images/` is empty, so the bra references come from Pinterest (AliExpress listing photos of this same bra, a curvy-faja.com leopard front, an inspireuplift.com black flat-lay); the per-colour back views are crops of `references/bra_back_three_colours.png`.

## Verified record — Higgsfield

### C01 — assembled clip (in review) — no single job

- `clips/v11_c01_g4.mp4` · md5 `09d46e67b4bbffd156bd5e3ce99c3731` · built from the runs below (cut list in § C01 — generated)


### C01 — nude run — job `e6870484-b0fb-4f41-9ff2-ba31114e1ac0`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183405_e6870484-b0fb-4f41-9ff2-ba31114e1ac0.mp4
- **On disk:** `clips/v11_c01_g1.mp4` · md5 `543a3033647a1bcb877880cd945e644f` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `284ea5e1-b592-466e-aeb2-e1c58e7c23cb` · `references/v11_c01_r4.mp4`
  - image · media `8ab559f4-acec-4ab1-9d23-4b010016c517` · `references/v11_c01_r7.png`
  - image · media `fd56f237-c7a0-4b32-a918-bf4a27842cf7` · `references/v11_c01_r3.png`
  - image · media `b7938776-24d0-4faa-a5ab-49a2c29965aa` · `references/bra_nude_flat.png` (product folder)
  - image · media `0585d4e5-d4e4-44f0-87a5-16d7921f9e59` · `references/bra_back_nude.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps down; then, facing the camera, she brings the long straps forward; in the last shot, facing the camera, she talks and smooths the bra with her hands.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### C01 — leopard run — job `9646ea5a-5c8e-4350-bed2-617305cee9eb`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183405_9646ea5a-5c8e-4350-bed2-617305cee9eb.mp4
- **On disk:** `clips/v11_c01_g2.mp4` · md5 `999cacb2ae4195faa21f709ed7e0cd96` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `5f6bb3d4-c513-46b3-9a29-20ae52aa95d0` · `references/v11_c01_r5.mp4`
  - image · media `8ab559f4-acec-4ab1-9d23-4b010016c517` · `references/v11_c01_r7.png`
  - image · media `fd56f237-c7a0-4b32-a918-bf4a27842cf7` · `references/v11_c01_r3.png`
  - image · media `edef02a5-72c0-4b25-896f-3e38f77c9da1` · `references/bra_leopard_front.png` (product folder)
  - image · media `ca6e7a8c-80bc-47e1-8a86-3695200d1b38` · `references/bra_back_leopard.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head; then, seen from behind, she pulls the long straps and crosses them behind her back.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

### C01 — black run — job `5e27d806-9f59-4ab5-a625-9a7bcb88cf80`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183406_5e27d806-9f59-4ab5-a625-9a7bcb88cf80.mp4
- **On disk:** `clips/v11_c01_g3.mp4` · md5 `4851106709cde787d1a1a80d72db7afb` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `2d8e252f-92e6-4cae-aff0-483108b7cbae` · `references/v11_c01_r6.mp4`
  - image · media `8ab559f4-acec-4ab1-9d23-4b010016c517` · `references/v11_c01_r7.png`
  - image · media `fd56f237-c7a0-4b32-a918-bf4a27842cf7` · `references/v11_c01_r3.png`
  - image · media `cd6c941a-bcaf-47a3-9592-6499e4497d0c` · `references/bra_black_flat.png` (product folder)
  - image · media `78454e62-a5a0-421c-b8db-205026282d19` · `references/bra_back_black.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with shoulder-length wavy dark brown hair, warm brown eyes, a friendly smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted dark blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the black bra down over her head; then, turned sideways and then with her back to the camera, she pulls it down and settles it; then, seen from behind, she pulls the long straps.

Every shot takes place in the room from @Image2: a simple, bright bedroom in ordinary daylight: pale walls, a single wooden bed with grey bedding, a window with white curtains, a tall light-wood wardrobe and a light wood floor with a long jute rug. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks. @Video1 has text burned into the picture; do not copy it: the result shows only the woman and her surroundings, with no letters, words or emojis anywhere.
```

## Upscale (2026-10-06)

Daniel 2026-10-06: "upscale all the 13 final videos using bytedance settings". On higgsfield.ai/upscale (Chrome), settings checked on the page before submitting: ByteDance Upscale · model version Pro · resolution 2K · 30fps · preset AIGC.

- Source: `clips/v11_c01_g4.mp4` · md5 `09d46e67b4bbffd156bd5e3ce99c3731` · uploaded as media `dafeb080-2ec6-41bb-aab7-6dbbf335f36f`.
- Job `be8beb19-40db-4e1b-a7a1-c04b27a64e3a` · result https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_232620_14678002-9066-41aa-a4af-8b3b4d8de54b.mp4
- On disk: `content/upscaled_videos/video_11.mp4` · md5 `578bfef961bb8f117f018f26b5d3cfc1` (same as the result URL) · 1440×2560 · 30 fps · reel sound kept
