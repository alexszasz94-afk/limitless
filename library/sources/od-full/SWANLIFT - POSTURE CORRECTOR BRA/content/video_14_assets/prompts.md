# Video 14 — Genjutsu recast of @thevareny reel DdlrbzqoVcW (rank 29)

**Current status (2026-10-05):** CLIP FOR DANIEL'S REVIEW: `clips/v14_c01_g4.mp4` — generated 2026-10-05 after Daniel's "Now transform them into videos". 3 Genjutsu runs, one per bra colour, cut back together in reel order with the reel's own sound. The leopard and nude runs with front shots were refused (nsfw, no credits). Re-run with back views only — passed. So v14 now has no front leopard/nude shots: it starts on the black front shot (the original 6.93 s) and ends on the leopard turn.

## Source reel

- **Reel:** https://www.instagram.com/reel/DdlrbzqoVcW/ · @thevareny
- **Views:** 181,727 · 19.6 s · rank 29 of 82 in `competition/all_competitors_ranked/data.md` (scraped 2026-10-05); one of the next five in `competition/selected` by views after the first ten
- **File:** `competition/selected/rank_29_thevareny_DdlrbzqoVcW.mp4` · md5 `85116a3da0c6c01bfa6cc2fd16c5b858` · copied byte-identical to `references/v14_c01_r1.mp4`
- **On-screen text in the reel:** none (post text: "if you have a bigger chest this specific feeling needs no further explanation..")
- **Original look:** Plus-size woman with a very large bust, long light-brown hair, back tattoo; leopard trousers with leopard, burgundy shorts with nude and black; plain grey wall. Talks and pulls faces to camera; colours switch on the cuts.

### Shot analysis

Cuts found with ffmpeg scene detection and checked frame by frame (frame numbers at 30 fps):

- **0.00–4.63 s** (frames 0–138) — leopard, starts almost topless taking off an old bra, then pulls the leopard bra over her head, poses
- **4.63–6.93 s** (frames 139–207) — nude, bare shoulders holding the bra, then over the head
- **6.93–9.37 s** (frames 208–280) — black, front, over the head
- **9.37–11.30 s** (frames 281–338) — leopard, back view, pulling it down
- **11.30–12.60 s** (frames 339–377) — leopard, back view, crossing the straps
- **12.60–13.53 s** (frames 378–405) — nude, back view, straps
- **13.53–14.87 s** (frames 406–445) — black, back view, straps
- **14.87–16.20 s** (frames 446–485) — leopard, turns, side and back
- **16.20–17.30 s** (frames 486–518) — leopard, front, pose
- **17.30–19.50 s** (frames 519–584) — leopard, front, adjusting the straps, talking

**Cut out before generating:** 0.00–2.60 s (almost topless, taking off an old bra) and 4.63–5.40 s (bare shoulders holding the nude bra in front of her chest). Even cut, this reel is the riskiest of the five: very large bust and deep cleavage in most front shots.

## New character and room (picked 2026-10-05, for review)

- **Woman (second pick, 2026-10-05):** `references/v14_c01_r7.png` · Pinterest pin https://www.pinterest.com/pin/229050331045363309/ · photo in a bedroom, 1664×2080. Prompt description: "plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust". Why: Plus-size with a large bust like the original (the point of this reel), about 30, with long black hair instead of light brown and no tattoos. Three-quarter photo in a plain white T-shirt and black joggers.
- **Room:** `references/v14_c01_r3.png` · Pinterest pin https://www.pinterest.com/pin/3729612242285338/ · prompt description: "a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor". Why: A real phone photo of an ordinary apartment bedroom in daylight — warmer and more lived-in than the original grey wall.
- **Lower body in every shot:** loose black joggers
- **First pick, rejected by Daniel 2026-10-05:** `references/v14_c01_r2.png` — "The characters used for video 11 to 15 are not good. I want hyper realistic characters. Use terms like 30 years old women, don't look for specifically ai generated". The first picks had been limited to images with AI evidence; the second search used "30 year old woman" style terms and any Pinterest image.

## C01 — plan (DRAFT, not submitted)

Genjutsu motion transfer (`hf_mult_motion_control`), 720p, one run per bra colour: each driving video holds only that colour's shots, joined, padded with a throw-away filler shot to whole seconds (Genjutsu rounds its output to whole seconds); the runs are cut back together in reel order with the reel's own sound — the method that fixed v9, v2 and v10. The driving videos are already cut (local work, no credits); nothing is submitted until Daniel approves the woman and the room.

### Run 1 — leopard — driving video `references/v14_c01_r4.mp4` (built, not submitted)

Frames 78–138 (2.60–4.63 s) + 281–377 (9.37–12.60 s) + 446–584 (14.87–19.50 s) + filler 208–210 (6.93–7.03 s) of `references/v14_c01_r1.mp4` · 10.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `d1e06d8ccb45beda3915f548f58b2233`. Attachments in order: @Video1 this driving video, @Image1 `references/v14_c01_r7.png`, @Image2 `references/v14_c01_r3.png`, @Image3 `references/bra_leopard_front.png` (product folder), @Image4 `references/bra_back_leopard.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head and settles it; then, seen from behind, she pulls it down and crosses the long straps behind her back; then she turns side-on; at the end, facing the camera, she poses and adjusts the shoulder straps while she talks.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Run 2 — nude — driving video `references/v14_c01_r5.mp4` (built, not submitted)

Frames 162–207 (5.40–6.93 s) + 378–405 (12.60–13.53 s) + filler 208–253 (6.93–8.47 s) of `references/v14_c01_r1.mp4` · 4.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `814e012c6c6dde1201103610bd2b25e9`. Attachments in order: @Video1 this driving video, @Image1 `references/v14_c01_r7.png`, @Image2 `references/v14_c01_r3.png`, @Image3 `references/bra_nude_flat.png` (product folder), @Image4 `references/bra_back_nude.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Run 3 — black — driving video `references/v14_c01_r6.mp4` (built, not submitted)

Frames 208–280 (6.93–9.37 s) + 406–445 (13.53–14.87 s) + filler 446–452 (14.87–15.10 s) of `references/v14_c01_r1.mp4` · 4.00 s · re-encoded H.264 CRF 14 + AAC 192k · md5 `d249467c33ec05290766e27660c10400`. Attachments in order: @Video1 this driving video, @Image1 `references/v14_c01_r7.png`, @Image2 `references/v14_c01_r3.png`, @Image3 `references/bra_black_flat.png` (product folder), @Image4 `references/bra_back_black.png` (product folder).

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head and settles it; then, seen from behind, she pulls and crosses the long straps.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

**Reel order after the runs:** 2.60–4.63 s leopard · 5.40–6.93 s nude · 6.93–9.37 s black · 9.37–12.60 s leopard · 12.60–13.53 s nude · 13.53–14.87 s black · 14.87–19.50 s leopard.

### Take history

- leopard run · driving video `references/v14_c01_r4.mp4` · job `89fb8b96-71dd-41f6-869d-3c45af1a832b` · status **nsfw** — refused, no file, no credits charged.
- nude run · driving video `references/v14_c01_r5.mp4` · job `fa8ba68d-04a8-4221-8331-45146cd1515d` · status **nsfw** — refused, no file, no credits charged.
- `clips/v14_c01_g3.mp4` · black run · driving video `references/v14_c01_r6.mp4` · job `5993d31c-5b70-4bc7-9c5c-98b6c04ffe23` · md5 `fd843e4c0cc1d4aa5d34e553ef32ab05` · 4.04 s · part of the assembly
- `clips/v14_c01_g1.mp4` · leopard run · driving video `references/v14_c01_r8.mp4` · job `8759bbd3-dd24-476c-ab99-965807c128c7` · md5 `c074b056ec8f637af4d10d290620109e` · 5.04 s · part of the assembly
- `clips/v14_c01_g2.mp4` · nude run · driving video `references/v14_c01_r9.mp4` · job `f4269ae6-8f44-4188-9032-315667ec8211` · md5 `3f4e70c48175284812a6aed38e13bbb8` · 4.04 s · part of the assembly
- `clips/v14_c01_g4.mp4` · assembled · md5 `5de067f316a1aa33b2664d31d4fbf63c` · 222 frames, 9.25 s · **waiting for Daniel's review**

## C01 — generated 2026-10-05

- Extra driving video `references/v14_c01_r8.mp4` · leopard back views: frames 281–377 + 446–485 + filler 208–220 · 5.00 s · md5 `e99f4c11e1dc06bf2bc074ff282fc234` (cut from `references/v14_c01_r1.mp4`, H.264 CRF 14 + AAC 192k)
- Extra driving video `references/v14_c01_r9.mp4` · nude back view: frames 378–405 + filler 406–445, 339–377, 281–293 · 4.00 s · md5 `929382710e0341589e5abc731703ca5a` (cut from `references/v14_c01_r1.mp4`, H.264 CRF 14 + AAC 192k)

**Assembly of `clips/v14_c01_g4.mp4`** (24 fps, reel order):

| # | colour | source frames | reel sound (s) |
|---|---|---|---|
| 1 | black | `v14_c01_g3.mp4` 0–58 | 6.933–9.392 |
| 2 | leopard | `v14_c01_g1.mp4` 0–76 | 9.367–12.575 |
| 3 | nude | `v14_c01_g2.mp4` 0–20 | 12.600–13.475 |
| 4 | black | `v14_c01_g3.mp4` 59–91 | 13.533–14.908 |
| 5 | leopard | `v14_c01_g1.mp4` 77–108 | 14.867–16.200 |

Every join checked frame by frame.

### Video prompt — leopard run · job `89fb8b96` (refused) (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head and settles it; then, seen from behind, she pulls it down and crosses the long straps behind her back; then she turns side-on; at the end, facing the camera, she poses and adjusts the shoulder straps while she talks.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Video prompt — nude run · job `fa8ba68d` (refused) (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Video prompt — black run · job `5993d31c` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head and settles it; then, seen from behind, she pulls and crosses the long straps.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Video prompt — leopard run · job `8759bbd3` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: seen from behind, she pulls the leopard bra down and crosses the long straps behind her back; then she turns side-on and back again.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### Video prompt — nude run · job `f4269ae6` (exact text sent to Higgsfield)

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1. Every shot shows her from behind: she pulls the long straps of the nude bra and crosses them behind her back.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

## Note on the product references

`product_images/` is empty, so the bra references come from Pinterest (AliExpress listing photos of this same bra, a curvy-faja.com leopard front, an inspireuplift.com black flat-lay); the per-colour back views are crops of `references/bra_back_three_colours.png`.

## Verified record — Higgsfield

### C01 — assembled clip (in review) — no single job

- `clips/v14_c01_g4.mp4` · md5 `5de067f316a1aa33b2664d31d4fbf63c` · built from the runs below (cut list in § C01 — generated)


### C01 — black run — job `5993d31c-5b70-4bc7-9c5c-98b6c04ffe23`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_183556_5993d31c-5b70-4bc7-9c5c-98b6c04ffe23.mp4
- **On disk:** `clips/v14_c01_g3.mp4` · md5 `fd843e4c0cc1d4aa5d34e553ef32ab05` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `455fe1d7-379a-406c-87e8-452983f41602` · `references/v14_c01_r6.mp4`
  - image · media `a1afc5d6-2ee5-4a27-b3cc-5b7d0ea63991` · `references/v14_c01_r7.png`
  - image · media `f184665b-d334-4f47-9769-6cf66c439462` · `references/v14_c01_r3.png`
  - image · media `cd6c941a-bcaf-47a3-9592-6499e4497d0c` · `references/bra_black_flat.png` (product folder)
  - image · media `78454e62-a5a0-421c-b8db-205026282d19` · `references/bra_back_black.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the black bra laid flat. @Image4 shows the back of the black bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is black and only black: plain matte black, with black shoulder straps, black long straps and a black hook band. It is the same black bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the black bra down over her head and settles it; then, seen from behind, she pulls and crosses the long straps.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### C01 — leopard run — job `8759bbd3-dd24-476c-ab99-965807c128c7`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_184410_8759bbd3-dd24-476c-ab99-965807c128c7.mp4
- **On disk:** `clips/v14_c01_g1.mp4` · md5 `c074b056ec8f637af4d10d290620109e` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `32a618dd-06ae-4a4c-a5a8-51695d755a77` · `references/v14_c01_r8.mp4`
  - image · media `a1afc5d6-2ee5-4a27-b3cc-5b7d0ea63991` · `references/v14_c01_r7.png`
  - image · media `f184665b-d334-4f47-9769-6cf66c439462` · `references/v14_c01_r3.png`
  - image · media `edef02a5-72c0-4b25-896f-3e38f77c9da1` · `references/bra_leopard_front.png` (product folder)
  - image · media `ca6e7a8c-80bc-47e1-8a86-3695200d1b38` · `references/bra_back_leopard.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: seen from behind, she pulls the leopard bra down and crosses the long straps behind her back; then she turns side-on and back again.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### C01 — nude run — job `f4269ae6-8f44-4188-9032-315667ec8211`

- **Status:** completed
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261005_184412_f4269ae6-8f44-4188-9032-315667ec8211.mp4
- **On disk:** `clips/v14_c01_g2.mp4` · md5 `3f4e70c48175284812a6aed38e13bbb8` (same md5 as the file at the result URL)
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `b511250b-90eb-485b-92d8-5dbf2069e19d` · `references/v14_c01_r9.mp4`
  - image · media `a1afc5d6-2ee5-4a27-b3cc-5b7d0ea63991` · `references/v14_c01_r7.png`
  - image · media `f184665b-d334-4f47-9769-6cf66c439462` · `references/v14_c01_r3.png`
  - image · media `b7938776-24d0-4faa-a5ab-49a2c29965aa` · `references/bra_nude_flat.png` (product folder)
  - image · media `0585d4e5-d4e4-44f0-87a5-16d7921f9e59` · `references/bra_back_nude.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1. Every shot shows her from behind: she pulls the long straps of the nude bra and crosses them behind her back.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### C01 — leopard run — job `89fb8b96-71dd-41f6-869d-3c45af1a832b`

- **Status:** nsfw (refused by Higgsfield; no video, no credits charged)
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `7aef4c01-a913-49ad-9661-53ab7da713a9` · `references/v14_c01_r4.mp4`
  - image · media `a1afc5d6-2ee5-4a27-b3cc-5b7d0ea63991` · `references/v14_c01_r7.png`
  - image · media `f184665b-d334-4f47-9769-6cf66c439462` · `references/v14_c01_r3.png`
  - image · media `edef02a5-72c0-4b25-896f-3e38f77c9da1` · `references/bra_leopard_front.png` (product folder)
  - image · media `ca6e7a8c-80bc-47e1-8a86-3695200d1b38` · `references/bra_back_leopard.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the leopard bra from the front. @Image4 shows the back of the leopard bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is leopard and only leopard: brown leopard print with black spots, with the same leopard print on the shoulder straps, the back panel, the long straps and the hook band. It is the same leopard bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: first, facing the camera, she pulls the leopard bra down over her head and settles it; then, seen from behind, she pulls it down and crosses the long straps behind her back; then she turns side-on; at the end, facing the camera, she poses and adjusts the shoulder straps while she talks.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

### C01 — nude run — job `fa8ba68d-04a8-4221-8331-45146cd1515d`

- **Status:** nsfw (refused by Higgsfield; no video, no credits charged)
- **Model:** `hf_mult_motion_control` (Genjutsu motion transfer) · resolution `720p` · aspect_ratio 9:16 · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612 · submitted 2026-10-05
- **Attachments, in submission order** (@Video1 is the video; @Image numbers follow the image order):
  - @Video1 · media `ddb1a490-eea7-4b0f-9fae-4d1a115e955e` · `references/v14_c01_r5.mp4`
  - image · media `a1afc5d6-2ee5-4a27-b3cc-5b7d0ea63991` · `references/v14_c01_r7.png`
  - image · media `f184665b-d334-4f47-9769-6cf66c439462` · `references/v14_c01_r3.png`
  - image · media `b7938776-24d0-4faa-a5ab-49a2c29965aa` · `references/bra_nude_flat.png` (product folder)
  - image · media `0585d4e5-d4e4-44f0-87a5-16d7921f9e59` · `references/bra_back_nude.png` (product folder)
- **Exact prompt:**

```text
@Video1 is the motion source. @Image1 is the new woman. @Image2 is the room. @Image3 shows the nude (beige) bra with its two long straps. @Image4 shows the back of the nude bra, showing the keyhole cut-out and the crossed straps.

Use @Video1 only for motion, camera and timing: keep every shot, every cut, every camera move, pose, gesture, hand movement and head turn, with its exact timing, as in @Video1, in the same vertical 9:16 framing, with the woman at the same position, distance and size in frame.

Recast the woman as the woman from @Image1: a plus-size woman around thirty with long, wavy black hair, warm olive skin, a soft smile and a full, curvy figure with a large bust. Take only her face, hair, skin and body from @Image1; her clothes come from this prompt. In every shot she wears loose black joggers on her lower body.

The garment she puts on is the posture corrector bra shown in @Image3 and @Image4. It is seamless and wire-free, with a deep V neckline, wide shoulder straps and smooth moulded cups; the back is open with a large rounded keyhole cut-out under the shoulder blades; two long elastic straps hang from the back panel, cross behind her back and close at the front under the bust with a short hook-and-eye band. In this whole clip the bra is nude and only nude: plain nude beige, with nude shoulder straps, nude long straps and a nude hook band. It is the same nude bra in every shot, from the first frame to the last, and it never changes colour, even where the bra in @Video1 has a different colour or pattern. It moves exactly as the bra moves in @Video1. Keep every cut of @Video1: facing the camera, she pulls the nude bra down over her head; then, seen from behind, she pulls the long straps.

Every shot takes place in the room from @Image2: a bright apartment bedroom in ordinary daylight: white walls, a large white bed with a cream knitted throw, a floor-to-ceiling glass balcony door looking onto city balconies, a large monstera plant and a patterned rug on a wood floor. The camera sees the room from where the phone stands in @Video1, with the woman standing in the open floor space, and the same light direction in every shot.

Hyperrealistic, natural, unedited iPhone video filmed at home in ordinary daylight, like a real person's TikTok: real skin with pores, small imperfections and natural shine; no beauty filter, no skin smoothing, no glow, no cinematic colour grading; real cotton and elastic fabric with creases and folds; natural white balance and true-to-life colours, with the slight softness and sensor noise of a phone camera. No text of any kind anywhere in the frame: no on-screen captions, no subtitles, no emojis, no stickers, no text overlays, no logos, no watermarks.
```

## Upscale (2026-10-06)

Daniel 2026-10-06: "upscale all the 13 final videos using bytedance settings". On higgsfield.ai/upscale (Chrome), settings checked on the page before submitting: ByteDance Upscale · model version Pro · resolution 2K · 30fps · preset AIGC.

- Source: `clips/v14_c01_g4.mp4` · md5 `5de067f316a1aa33b2664d31d4fbf63c` · uploaded as media `1d2cd1c6-57ad-4b3b-8a87-e71507f75f77`.
- Job `ccc78898-64ca-4e7f-9f2e-dabeddf657a8` · result https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20261006_000700_dd53e958-bd2f-4377-bdc1-41bb0705cf78.mp4
- On disk: `content/upscaled_videos/video_14.mp4` · md5 `0b31b4c20711cbbdb903a5c75670a765` (same as the result URL) · 1440×2560 · 30 fps · reel sound kept
