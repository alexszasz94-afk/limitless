# Video 12 — Genjutsu recast of @the_vitalys reel DdZPCKsKaNv (rank 22)

**Current status (2026-10-05):** CLIP FOR DANIEL'S REVIEW: `clips/v12_c01_g3.mp4` — generated 2026-10-05 after Daniel's "Now transform them into videos". 2 Genjutsu runs, one per bra colour, cut back together in reel order with the reel's own sound. Known problem: in the nude run she keeps the black T-shirt from her photo under the bra; the black run shows bare skin. So the T-shirt appears and disappears on the colour cuts.

## Source reel

- **Reel:** https://www.instagram.com/reel/DdZPCKsKaNv/ · @the_vitalys
- **Views:** 206,140 · 8.2 s · rank 22 of 82 in `competition/all_competitors_ranked/data.md` (scraped 2026-10-05); one of the next five in `competition/selected` by views after the first ten
- **File:** `competition/selected/rank_22_the_vitalys_DdZPCKsKaNv.mp4` · md5 `6fc5883539366474975878d5720ec931` · copied byte-identical to `references/v12_c01_r1.mp4`
- **On-screen text in the reel:** none
- **Original look:** Young slim toned brunette with a slicked ponytail; black denim shorts with the nude bra, light denim shorts with the black one; grey-blue and white walls. Silent step-by-step demo, nude and black alternating on the cuts (29.83 fps file).

### Shot analysis

Cuts found with ffmpeg scene detection and checked frame by frame (frame numbers at 30 fps, the file runs at 29.83 fps):

- **0.00–0.83 s** (frames 0–24) — nude, front, holds it up, then over the head
- **0.83–1.77 s** (frames 25–52) — black, front, over the head
- **1.77–2.37 s** (frames 53–70) — nude, front, over the head
- **2.37–3.03 s** (frames 71–90) — black, front, over the head
- **3.03–4.40 s** (frames 91–131) — nude, back view, pulling and crossing the long straps
- **4.40–5.47 s** (frames 132–163) — black, back view, straps
- **5.47–6.07 s** (frames 164–181) — nude, back view, straps
- **6.07–7.33 s** (frames 182–219) — nude, front, pulls the straps forward, thumbs up
- **7.33–8.10 s** (frames 220–242) — black, front, flexes both arms, smiles

**Cut out before generating:** nothing — this reel is the same kind as v4, which passed Higgsfield once it was re-encoded. If it is refused, the first 0.3 s (holding the bra against her chest) is the part to cut.

## New character and room (picked 2026-10-05, for review)

- **Woman (second pick, 2026-10-05):** `references/v12_c01_r6.png` · Pinterest pin https://www.pinterest.com/pin/654359020906501602/ · phone selfie at home, 1122×1402. Prompt description: "woman around thirty with long, wavy, caramel-highlighted brown hair, light olive skin, a calm natural smile and a slim figure". Why: Slim like the original, about 30, with long loose highlighted hair instead of a slicked ponytail. Real-looking phone selfie in a plain black T-shirt.
- **Room:** `references/v12_c01_r3.png` · Pinterest pin https://www.pinterest.com/pin/1091067447267466362/ · prompt description: "a bright Scandinavian-style living room in ordinary daylight: a glass balcony door with trees outside, a rattan pendant lamp, a grey sofa with a knitted throw, a round light-wood coffee table, a jute rug, plants on wall shelves and framed prints". Why: Bright, airy apartment like the original, but a styled living room with a balcony door instead of bare grey walls; open floor in front of the camera.
- **Lower body in every shot:** high-waisted mid-blue jeans
- **First pick, rejected by Daniel 2026-10-05:** `references/v12_c01_r2.png` — "The characters used for video 11 to 15 are not good. I want hyper realistic characters. Use terms like 30 years old women, don't look for specifically ai generated". The first picks had been limited to images with AI evidence; the second search used "30 year old woman" style terms and any Pinterest image.

## C01 — plan (DRAFT, not submitted)

Genjutsu motion transfer (`hf_mult_motion_control`), 720p, one run per bra colour: each driving video holds only that colour's shots, joined, padded with a throw-away filler shot to whole seconds (Genjutsu rounds its output to whole seconds); the runs are cut back together in reel order with the reel's own sound — the method that fixed v9, v2 and v10. The driving videos are already cut (local work, no credits); nothing is submitted until Daniel approves the woman and the room.

### Run 1 — nude — driving video `references/v12_c01_r4.mp4` (built, not submitted)

Frames 0–24 (0.00–0.83 s) + 53–70 (1.77–2.37 s) + 91–131 (3.03–4.40 s) + 164–219 (5.47–7.33 s) + filler 25–34 (0.83–1.17 s) of `references/v12_c01_r1.mp4` · 5.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `95418269bbd5bf2b88068c92f933a98d` (the file runs at 29.83 fps; the driving video is written at 30 fps with the same frames, so it is 0.6 % faster — 151/121 frames). Attachments in order: @Video1 this driving video, @Image1 `references/v12_c01_r6.png`, @Image2 `references/v12_c01_r3.png`, @Image3 `references/bra_nude_flat.png` (product folder), @Image4 `references/bra_back_nude.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with long, wavy, caramel-highlighted brown hair, light olive skin, a calm natural smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted mid-blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she holds the nude bra up and pulls it down over her head; after the cut she pulls it over her head again; then, seen from behind, she pulls the long straps down and crosses them behind her back; at the end, facing the camera, she pulls the long straps forward and gives a thumbs-up.

Every shot takes place in the room from @Image2: a bright Scandinavian-style living room in ordinary daylight: a glass balcony door with trees outside, a rattan pendant lamp, a grey sofa with a knitted throw, a round light-wood coffee table, a jute rug, plants on wall shelves and framed prints. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Run 2 — black — driving video `references/v12_c01_r5.mp4` (built, not submitted)

Frames 25–52 (0.83–1.77 s) + 71–90 (2.37–3.03 s) + 132–163 (4.40–5.47 s) + 220–242 (7.33–8.10 s) + filler 91–107 (3.03–3.60 s) of `references/v12_c01_r1.mp4` · 4.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `3e2e7f9d8dd074c85a191cf016ed402a` (the file runs at 29.83 fps; the driving video is written at 30 fps with the same frames, so it is 0.6 % faster — 151/121 frames). Attachments in order: @Video1 this driving video, @Image1 `references/v12_c01_r6.png`, @Image2 `references/v12_c01_r3.png`, @Image3 `references/bra_black_flat.png` (product folder), @Image4 `references/bra_back_black.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with long, wavy, caramel-highlighted brown hair, light olive skin, a calm natural smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted mid-blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head; after the cut she does it again; then, seen from behind, she pulls the long straps down and crosses them; in the last shot, facing the camera, she flexes both arms and smiles.

Every shot takes place in the room from @Image2: a bright Scandinavian-style living room in ordinary daylight: a glass balcony door with trees outside, a rattan pendant lamp, a grey sofa with a knitted throw, a round light-wood coffee table, a jute rug, plants on wall shelves and framed prints. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

**Reel order after the runs:** 0.00–0.83 s nude · 0.83–1.77 s black · 1.77–2.37 s nude · 2.37–3.03 s black · 3.03–4.40 s nude · 4.40–5.47 s black · 5.47–7.33 s nude · 7.33–8.10 s black.

### Take history

- `clips/v12_c01_g1.mp4` · nude run · driving video `references/v12_c01_r4.mp4` · job `8c2dc422-4ec8-461c-8622-8d0f85e1fb02` · md5 `e2cf18aece41b8e801cbabe131f6a76b` · 5.04 s · part of the assembly
- `clips/v12_c01_g2.mp4` · black run · driving video `references/v12_c01_r5.mp4` · job `b6f027f3-0f1b-44f4-b4c1-a2e8a87d73fe` · md5 `53189241b1d7e7c156d6604c611d3c69` · 4.04 s · part of the assembly
- `clips/v12_c01_g3.mp4` · assembled · md5 `4b9f0503b8da55d1e738100ce5b6407b` · 195 frames, 8.12 s · **waiting for Daniel's review**

## C01 — generated 2026-10-05


**Assembly of `clips/v12_c01_g3.mp4`** (24 fps, reel order):

| # | colour | source frames | reel sound (s) |
|---|---|---|---|
| 1 | nude | `v12_c01_g1.mp4` 0–19 | 0.000–0.833 |
| 2 | black | `v12_c01_g2.mp4` 0–21 | 0.838–1.755 |
| 3 | nude | `v12_c01_g1.mp4` 20–35 | 1.777–2.443 |
| 4 | black | `v12_c01_g2.mp4` 22–36 | 2.380–3.005 |
| 5 | nude | `v12_c01_g1.mp4` 36–67 | 3.050–4.384 |
| 6 | black | `v12_c01_g2.mp4` 37–63 | 4.425–5.550 |
| 7 | nude | `v12_c01_g1.mp4` 68–111 | 5.497–7.331 |
| 8 | black | `v12_c01_g2.mp4` 64–82 | 7.374–8.166 |

Every join checked frame by frame.

### Video prompt — nude run · job `8c2dc422` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with long, wavy, caramel-highlighted brown hair, light olive skin, a calm natural smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted mid-blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she holds the nude bra up and pulls it down over her head; after the cut she pulls it over her head again; then, seen from behind, she pulls the long straps down and crosses them behind her back; at the end, facing the camera, she pulls the long straps forward and gives a thumbs-up.

Every shot takes place in the room from @Image2: a bright Scandinavian-style living room in ordinary daylight: a glass balcony door with trees outside, a rattan pendant lamp, a grey sofa with a knitted throw, a round light-wood coffee table, a jute rug, plants on wall shelves and framed prints. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Video prompt — black run · job `b6f027f3` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with long, wavy, caramel-highlighted brown hair, light olive skin, a calm natural smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted mid-blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head; after the cut she does it again; then, seen from behind, she pulls the long straps down and crosses them; in the last shot, facing the camera, she flexes both arms and smiles.

Every shot takes place in the room from @Image2: a bright Scandinavian-style living room in ordinary daylight: a glass balcony door with trees outside, a rattan pendant lamp, a grey sofa with a knitted throw, a round light-wood coffee table, a jute rug, plants on wall shelves and framed prints. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

## Note on the product references

`product_images/` is empty, so the bra references come from Pinterest (AliExpress listing photos of this same bra, a curvy-faja.com leopard front, an inspireuplift.com black flat-lay); the per-colour back views are crops of `references/bra_back_three_colours.png`.

## Verified record — Higgsfield

### C01 — assembled clip (in review) — no single job

- `clips/v12_c01_g3.mp4` · md5 `4b9f0503b8da55d1e738100ce5b6407b` · built from the runs below (cut list in § C01 — generated)


### C01 — nude run — job `8c2dc422-4ec8-461c-8622-8d0f85e1fb02`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183405_8c2dc422-4ec8-461c-8622-8d0f85e1fb02.mp4
- **On disk:** `clips/v12_c01_g1.mp4` · md5 `e2cf18aece41b8e801cbabe131f6a76b` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `af7e0bea-a4fc-4ec4-8ddc-12207d51b09a` · `references/v12_c01_r4.mp4`
  - image · media `238594b8-0fe0-4e49-8b1a-ca0b90079d75` · `references/v12_c01_r6.png`
  - image · media `f76a2a01-2838-49dd-80c5-fa695f500126` · `references/v12_c01_r3.png`
  - image · media `b7938776-24d0-4faa-a5ab-49a2c29965aa` · `references/bra_nude_flat.png` (product folder)
  - image · media `0585d4e5-d4e4-44f0-87a5-16d7921f9e59` · `references/bra_back_nude.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with long, wavy, caramel-highlighted brown hair, light olive skin, a calm natural smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted mid-blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she holds the nude bra up and pulls it down over her head; after the cut she pulls it over her head again; then, seen from behind, she pulls the long straps down and crosses them behind her back; at the end, facing the camera, she pulls the long straps forward and gives a thumbs-up.

Every shot takes place in the room from @Image2: a bright Scandinavian-style living room in ordinary daylight: a glass balcony door with trees outside, a rattan pendant lamp, a grey sofa with a knitted throw, a round light-wood coffee table, a jute rug, plants on wall shelves and framed prints. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### C01 — black run — job `b6f027f3-0f1b-44f4-b4c1-a2e8a87d73fe`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183457_b6f027f3-0f1b-44f4-b4c1-a2e8a87d73fe.mp4
- **On disk:** `clips/v12_c01_g2.mp4` · md5 `53189241b1d7e7c156d6604c611d3c69` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `89ed8040-6c24-4b8d-94a9-f65d329b01a5` · `references/v12_c01_r5.mp4`
  - image · media `238594b8-0fe0-4e49-8b1a-ca0b90079d75` · `references/v12_c01_r6.png`
  - image · media `f76a2a01-2838-49dd-80c5-fa695f500126` · `references/v12_c01_r3.png`
  - image · media `cd6c941a-bcaf-47a3-9592-6499e4497d0c` · `references/bra_black_flat.png` (product folder)
  - image · media `78454e62-a5a0-421c-b8db-205026282d19` · `references/bra_back_black.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a woman around thirty with long, wavy, caramel-highlighted brown hair, light olive skin, a calm natural smile and a slim figure. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears high-waisted mid-blue jeans on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head; after the cut she does it again; then, seen from behind, she pulls the long straps down and crosses them; in the last shot, facing the camera, she flexes both arms and smiles.

Every shot takes place in the room from @Image2: a bright Scandinavian-style living room in ordinary daylight: a glass balcony door with trees outside, a rattan pendant lamp, a grey sofa with a knitted throw, a round light-wood coffee table, a jute rug, plants on wall shelves and framed prints. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

## Upscale (2026-10-06)

Daniel 2026-10-06: "upscale all the 13 final videos using bytedance settings". On higgsfield.ai/upscale (Chrome), settings checked on the page before submitting: ByteDance Upscale · model version Pro · resolution 2K · 30fps · preset AIGC.

- Source: `clips/v12_c01_g3.mp4` · md5 `4b9f0503b8da55d1e738100ce5b6407b` · uploaded as media `dd9e289f-38fd-4ff7-8447-2546aa636b74`.
- Job `970b5a71-2d3b-4e96-8d85-6a9e465b882e` · result https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261006_000630_526aa2f3-5ec3-4242-bc51-cc6059a3484c.mp4
- On disk: `content/upscaled_videos/video_12.mp4` · md5 `ed42c70e5642edc59e04e56c64e2e52f` (same as the result URL) · 1440×2560 · 30 fps · reel sound kept
