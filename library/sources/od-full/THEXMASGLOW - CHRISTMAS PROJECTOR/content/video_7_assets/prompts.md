# Video 7 - prompts archive

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_7.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

*Product:* THEXMASGLOW - CHRISTMAS PROJECTOR
*Round:* 2026-09-20
*Scope:* B-roll generated 2026-09-20 in a round Daniel asked for "only for the broll". The **C01 hook was added later the same day** in the v7/v8/v9/v10 hook round - see the C01 section below.

## Planned cut

| card | section | shot |
|---|---|---|
| C01 | Hook | the store end-cap, our carton faced wall to wall |
| C02 | B-roll 1 - the unbox | hands on the closed carton |
| C03 | B-roll 1 - the unbox | the dome lifted onto the counter |
| C04 | B-roll 1 - the unbox | the cable going in |
| C05 | B-roll 2 - the reveal | F1 the closed door, F2 the room behind it |
| C06 | B-roll 2 - the reveal | the child in bed under the running ceiling |
| C07 | B-roll 2 - the reveal | the two children in the middle of the great room |

## Brief as given

> Now I want you to create me the images for the next 2 videos, only for the broll
> (just without the hook). The same style as you did for the last videos. Different
> tables, backgrounds, houses, kids and animations. Try to make the animation even
> more insane and wow. Don't ask me how. All the images must be extremly high
> quality, perfect light, iphone shots, nothing blurish. Use gpt image 2.5 Sunburst,
> 2k, mid quality settings, 9x16.

## Look pack chosen

Modern rustic. Camel, travertine, white oak, terracotta and copper. Distinct from v2-v6 in every slot Daniel named.

| slot | v7 |
|---|---|
| sleeve | camel wool |
| C02 table | weathered reclaimed elm plank, pale grey-brown, dead-matte hardwax oil, softly eased square edge |
| C02 background | limewashed oat plaster living room, lime plaster fireplace with a chunky reclaimed oak beam mantel, cream knitted stockings, slim black picture light over a dark abstract canvas |
| C03/C04 counter | polished dark green Verde marble, white and pale jade veining, square mitred edge, high polish |
| C03/C04 kitchen | natural white oak slab fronts with slim black recessed finger pulls, full-height travertine slab backsplash in warm oatmeal, matte black range - LEFT in C03, RIGHT in C04 |
| C05 F1 door | classic American two-panel door, deep forest green eggshell, antique brass knob and escutcheon |
| knitwear | rust-orange and cream fair-isle with a band of little pine trees across the chest, oatmeal knitted lounge trousers, thick cream socks |
| C06 child | girl, about 7, shoulder-length light brown hair |
| C07 children | girl about 8 with long wavy light brown hair, boy about 5 with short sandy brown hair |
| ornaments | terracotta and antique copper |
| ribbon / bow | terracotta |
| C06 quilt | rust-orange wool |

**Projection signature** - the one thing in v7's projection that is in no other ad:

```text
and turning slowly above the rooftops one enormous glowing gold fairground carousel of prancing reindeer, its scalloped canopy strung with tiny bells and its centre pole a bright column of light, and on the frozen pond below it a wide ring of glowing gold ice skaters circling one behind another, each one trailing a long bright curved arc of light across the ice
```

## The escalation clause

Daniel asked for the animation to be "even more insane and wow". The v4/v5/v6 escalation clause was kept **byte-identical** and a second clause was appended to it by replacing its trailing period. This is the appended half:

```text
; and beyond even that, great slow-turning glowing gold snow globes the size of a car drifting across the upper wall, each one holding its own tiny lit village inside it, a long glowing gold paper-chain garland of angels linked hand to hand curving right across the ceiling from one corner to the other, whole flights of glowing gold robins and doves crossing in loose Vs at three different depths, glowing gold ribbons of ivy and holly with bright red berries winding up every corner of the room, and a slow steady rise of glowing gold sparks lifting off the village chimneys and climbing the full height of the wall to join the star field, so every surface is so full that the eye cannot rest on any single thing.
```

## Settings

`gpt_image_2_5 - variant sunburst - quality medium - resolution 2k - aspect_ratio 9:16 - count 1 - use_unlim false` - output 1520 x 2688. Workspace Oneofone1.

## Lineage

- C02, C03, C04, C05 F1 - from **v6**
- C05 F2, C06 - from **v4** (take 2 of each)
- C07 - from **v5** (take 2), plus one coherence edit naming the great room as the same house seen through the door earlier in the ad

Per CLAUDE.md rule 3 every source was pasted byte-identically and only the nouns that physically differ were changed. The builder asserted a single match on every substitution, so untouched text is verified identical, not assumed identical.

---

## C01 - The store end-cap

*Section:* Hook
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW
*What it is:* seen from a couple of steps behind her, a woman in an oatmeal knit and American-flag Christmas pyjama bottoms standing in front of a retail end-cap faced wall-to-wall with our carton, blue basket in hand.

- frames: `v7_c01_g1.png` (current)
- clips: none yet

*Reused from* MERRYGLOWUSA - LED CURTAIN LIGHTS v9 C01 - changed: (a) every box on the shelves and stacked on top, now the THEXMASGLOW carton; (b) the tall right-edge display banner, now the THEXMASGLOW banner; (c) the woman, now late 20s with long dark brown hair, an oatmeal cream knit and American-flag Christmas pyjama bottoms. The camera position, the eye level, the distance, the three-quarters-from-behind pose, the blue basket, the gondola angle, the shelf count, the concrete floor and the store ceiling are held to the reference.

*Note on the source:* the LED v9 C01 has **no image prompt** in its `prompts.md` - only a video prompt. Per CLAUDE.md rule 3 nothing was reconstructed from memory: the frame itself was attached as the geometry reference and the geometry was restated in prose, the same pattern v6 C01 used.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `references/v7_c01_r1.png` | owns the geometry - camera position, eye level, distance, her pose and scale, the basket, the gondola angle, the banner position |
| @Image 2 | `references/v7_c01_r2.png` | owns the carton artwork |

media ids `1d8b4b34-7ef9-4002-ae4c-7d0d88cbf71e`, `2597b25d-60d1-4060-9602-32b0ee26c2f7`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `330ade78-cfcc-4202-ac66-cb7809310383`

```text
Copy the FIRST attached reference photo EXACTLY as a photograph: the same camera position standing a couple of steps behind and slightly to the left of the woman, the same eye-level height, the same distance, the same vertical 9:16 framing, the same three-quarters-from-behind view of her with her head and shoulders cropped at the upper left of the frame, the same blue plastic shopping basket hanging from her hand low at the bottom left, the same white retail gondola shelving unit running across the right two thirds of the frame at the same oblique angle, the same four loaded shelves, the same tall narrow printed display banner standing at the right edge, the same polished grey concrete store floor, the same bright overhead store lighting and the same ceiling with its light fixtures across the top. Same composition, same scale of everything. Change only the three things below.

FIRST - THE PRODUCT BOXES. Every box on the shelves and every box stacked on top of the shelving unit is now OUR carton, exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, proportions about 1 to 1.6, forest green body, a dark red band across the top carrying a gold THEXMASGLOW wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR under it, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector standing on a separate white four-legged splayed stand base, a slim red remote printed beside it, a gold village skyline along the bottom edge, a thin gold foil border framing the panel, and no transparent window anywhere. The cartons stand upright side by side, front panels facing the camera, filling every shelf from end to end, four full shelves of them, perfectly aligned in neat rows the way a retail end-cap is faced, identical to each other. They keep the same footprint and the same rhythm on the shelf as the boxes in the FIRST reference.

SECOND - THE TALL DISPLAY BANNER at the right edge. It is now our banner: a tall narrow vertical printed panel in the same forest green as the carton with a gold foil border, a gold star at the top, the gold wordmark THEXMASGLOW, a cream serif headline CHRISTMAS LIGHT PROJECTOR, a large printed photograph of the white dome projector throwing warm gold trees and snowflakes across a dark living-room wall, and a column of small feature icons with the lines 16 Patterns, Remote Control, Timer and Indoor and Outdoor down the lower half. Same position, same width, same height, same angle as in the FIRST reference.

THIRD - THE WOMAN. A different woman from the reference: late 20s, long dark brown hair falling loose down her back, an oversized oatmeal cream knitted sweater, and matching American-flag Christmas pyjama bottoms - soft brushed cotton pyjama trousers with bold red and white horizontal stripes and small white five-pointed stars printed across the navy blue waistband panel, slightly loose the way real pyjamas fit - with white ribbed socks in white trainers. She stands in exactly the same place, the same three-quarters-from-behind pose, the same shoulders, the same head turn toward the shelf, the same arm down holding the same blue plastic shopping basket. Same scale in the frame.

FRAMING: leave a clean band of plain store ceiling across the very top of the image - roughly the top eighth of the frame - free of boxes, banners, signage and lettering, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room; she stays exactly the size she is in the FIRST reference.

The wordmark printed on the cartons and on the banner must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere in the picture.

LIGHTING AND QUALITY: bright, clean, evenly lit big-box store interior, neutral white balance with no orange and no colour cast, no dark corners. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp legible printing on every carton, realistic fabric and skin texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own cartons and banner.
```

*Result:* the shelf wall, the banner and the pyjama bottoms all landed. Her head is cropped at the top left exactly as in the source frame - that crop is inherited from the reference, not a defect of this take. Video 9 C01 is the corrected-angle version of this same shot.

---

### Video prompt - `clips/v7_c01_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 1080p - 9:16 - 5s - count 1 - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c01_g1.png` - Higgsfield media `7bf2c68b-42b7-4596-8ad4-5156a3493834`
**Extra references** - none
**Job** - `a5da6166-0752-4ab3-95ec-b01a817f070b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_171604_a5da6166-0752-4ab3-95ec-b01a817f070b.mp4

**Lineage** - Reused from MERRYGLOWUSA - LED CURTAIN LIGHTS v9 C01 - changed: only the five product/wardrobe nouns (winter coat -> cream knit sweater and American-flag pajama pants, LED CURTAIN LIGHTS box -> THEXMASGLOW CHRISTMAS LIGHT PROJECTOR box). Every word describing motion, camera, pacing, framing, audio and the hard rules is byte-identical to the source, and the duration stays 5s as in the source Settings line.

Built by exact-string replacement with `assert s.count(old) == 1` guards on each of the five swaps plus negative post-asserts (`"LED CURTAIN" not in s`, `"coat" not in s`), so a silently missed match was impossible.

```
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by a friend standing a few steps behind the woman — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in; all distance changes happen because the woman physically moves, never the lens.

Start frame: a young woman in a cream knit sweater and American-flag pajama pants stands in a bright store aisle holding a blue shopping basket, facing the shelf stacked with the green THEXMASGLOW CHRISTMAS LIGHT PROJECTOR product boxes.

ACTION TIMELINE:
0.0–1.0s — She spots the boxes on the shelf, freezes for a split second, then screams with real excitement: "No way — they actually have it!" Her whole body reacts, shoulders jumping.
1.0–2.0s — She lets the blue shopping basket drop straight out of her hand — it hits the store floor with a loud plastic clatter and tips over — as she spins around to the friend filming, one hand flying to her mouth, eyes huge, pure disbelief on her face.
2.0–3.5s — She whips back around and runs the few steps to the shelf, sweater flapping, shoes squeaking on the store floor, the camera staying put and letting her get smaller toward the shelf.
3.5–5.0s — She grabs one THEXMASGLOW CHRISTMAS LIGHT PROJECTOR box off the shelf with both hands, hugs it to her chest, and bounces on her feet laughing, extremely happy, turning halfway back toward the camera to show it. End frame: her hugging the box, beaming.

AUDIO: her real voice, lip-synced — the excited scream and line, then breathless laughing; the loud clatter of the dropped basket; running footsteps; bright store ambience with distant murmur and faint checkout beeps. NO music, no narration.

REALISM — HARD RULES: she keeps exactly the same face, hair, sweater and outfit as the start frame the whole clip. The shelf and every product box stay pixel-faithful to the start frame — same artwork, logo, colors, spelling, text rigid and never warping. The store background stays identical. Real phone-camera look, slight sensor noise, mild motion blur on the run, no cinematic bokeh, no text overlays, no watermark.
```

### Image prompt - `starting_frames/v7_c01_g2.png` (take 2)

Daniel on take 1: *"the boxes are too big, they must have the size of our boxe. Remake the starting frame and wait for me to review it."*

**Lineage** - Reused from v7 C01 take 1 - changed: ONLY the product-boxes paragraph. The sentence *"They keep the same footprint and the same rhythm on the shelf as the boxes in the FIRST reference."* was the defect - it handed the carton footprint to the LED curtain reference frame, whose boxes are much larger, and the prompt never stated a real-world size. It is deleted and replaced with the true carton size from `product_images/box_spec.md` (~15 x 15 x 24 cm, ~1 : 1.6), a human-scale anchor (forearm / half the shelf gap), an explicit instruction to ignore the first reference's box size, and a denser facing count (9-10 per shelf). Every other block - camera and geometry, banner, woman, FRAMING headroom, spelling lock, lighting and quality, no-captions - is byte-identical to take 1.

```text
Copy the FIRST attached reference photo EXACTLY as a photograph: the same camera position standing a couple of steps behind and slightly to the left of the woman, the same eye-level height, the same distance, the same vertical 9:16 framing, the same three-quarters-from-behind view of her with her head and shoulders cropped at the upper left of the frame, the same blue plastic shopping basket hanging from her hand low at the bottom left, the same white retail gondola shelving unit running across the right two thirds of the frame at the same oblique angle, the same four loaded shelves, the same tall narrow printed display banner standing at the right edge, the same polished grey concrete store floor, the same bright overhead store lighting and the same ceiling with its light fixtures across the top. Same composition, same scale of everything. Change only the three things below.

FIRST - THE PRODUCT BOXES. Every box on the shelves and every box stacked on top of the shelving unit is now OUR carton, exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, proportions about 1 to 1.6, forest green body, a dark red band across the top carrying a gold THEXMASGLOW wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR under it, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector standing on a separate white four-legged splayed stand base, a slim red remote printed beside it, a gold village skyline along the bottom edge, a thin gold foil border framing the panel, and no transparent window anywhere. SIZE IS CRITICAL: our carton is a SMALL package - roughly 15 cm wide by 15 cm deep by 24 cm tall, about the size of a shoebox stood upright on its end, no taller than the woman's forearm from wrist to elbow, and reaching only about half way up the gap between one shelf and the shelf above it, leaving a clear band of empty shelf air over every row. Do NOT copy the size of the boxes in the FIRST reference - those are much larger packages and their footprint must be ignored completely. Because our carton is small, MANY more of them fit: the cartons stand upright side by side, front panels facing the camera, packed tightly from one end of every shelf to the other with at least nine or ten of them across each shelf, four full shelves of them, perfectly aligned in dense neat rows the way a retail end-cap is faced, every carton identical to every other in size, proportion and printing.

SECOND - THE TALL DISPLAY BANNER at the right edge. It is now our banner: a tall narrow vertical printed panel in the same forest green as the carton with a gold foil border, a gold star at the top, the gold wordmark THEXMASGLOW, a cream serif headline CHRISTMAS LIGHT PROJECTOR, a large printed photograph of the white dome projector throwing warm gold trees and snowflakes across a dark living-room wall, and a column of small feature icons with the lines 16 Patterns, Remote Control, Timer and Indoor and Outdoor down the lower half. Same position, same width, same height, same angle as in the FIRST reference.

THIRD - THE WOMAN. A different woman from the reference: late 20s, long dark brown hair falling loose down her back, an oversized oatmeal cream knitted sweater, and matching American-flag Christmas pyjama bottoms - soft brushed cotton pyjama trousers with bold red and white horizontal stripes and small white five-pointed stars printed across the navy blue waistband panel, slightly loose the way real pyjamas fit - with white ribbed socks in white trainers. She stands in exactly the same place, the same three-quarters-from-behind pose, the same shoulders, the same head turn toward the shelf, the same arm down holding the same blue plastic shopping basket. Same scale in the frame.

FRAMING: leave a clean band of plain store ceiling across the very top of the image - roughly the top eighth of the frame - free of boxes, banners, signage and lettering, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room; she stays exactly the size she is in the FIRST reference.

The wordmark printed on the cartons and on the banner must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere in the picture.

LIGHTING AND QUALITY: bright, clean, evenly lit big-box store interior, neutral white balance with no orange and no colour cast, no dark corners. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp legible printing on every carton, realistic fabric and skin texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own cartons and banner.
```

**References** - unchanged from take 1.

| slot | file | why | media id |
|---|---|---|---|
| @Image 1 | `references/v7_c01_r1.png` | owns the geometry - camera position, eye level, distance, her pose and scale, the basket, the gondola angle, the banner position | `1d8b4b34-7ef9-4002-ae4c-7d0d88cbf71e` |
| @Image 2 | `references/v7_c01_r2.png` | owns the carton artwork | `2597b25d-60d1-4060-9602-32b0ee26c2f7` |

**Settings** - `gpt_image_2_5 - variant sunburst - quality medium - resolution 2k - aspect_ratio 9:16 - count 1 - use_unlim false`. Workspace Oneofone1. Job `f97d7572-0d90-4688-af6e-2555fe14ddb7`. md5 `c2590b897ca9048934b11089f43cbd0b`.

**Verdict** - approved by Daniel: *"The starting frame for video 7 now it's looking perfect, animate it in the same way"*.

### Video prompt - `clips/v7_c01_g2.mp4` (take 2)

**Lineage** - Reused from v7 C01 take 1 - changed: NOTHING. Daniel asked for the approved frame to be animated "in the same way", and nothing in the new frame physically differs except the carton size, so the prompt text is byte-identical to take 1. Only the start image changed, from `v7_c01_g1.png` to `v7_c01_g2.png`.

```text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by a friend standing a few steps behind the woman — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in; all distance changes happen because the woman physically moves, never the lens.

Start frame: a young woman in a cream knit sweater and American-flag pajama pants stands in a bright store aisle holding a blue shopping basket, facing the shelf stacked with the green THEXMASGLOW CHRISTMAS LIGHT PROJECTOR product boxes.

ACTION TIMELINE:
0.0–1.0s — She spots the boxes on the shelf, freezes for a split second, then screams with real excitement: "No way — they actually have it!" Her whole body reacts, shoulders jumping.
1.0–2.0s — She lets the blue shopping basket drop straight out of her hand — it hits the store floor with a loud plastic clatter and tips over — as she spins around to the friend filming, one hand flying to her mouth, eyes huge, pure disbelief on her face.
2.0–3.5s — She whips back around and runs the few steps to the shelf, sweater flapping, shoes squeaking on the store floor, the camera staying put and letting her get smaller toward the shelf.
3.5–5.0s — She grabs one THEXMASGLOW CHRISTMAS LIGHT PROJECTOR box off the shelf with both hands, hugs it to her chest, and bounces on her feet laughing, extremely happy, turning halfway back toward the camera to show it. End frame: her hugging the box, beaming.

AUDIO: her real voice, lip-synced — the excited scream and line, then breathless laughing; the loud clatter of the dropped basket; running footsteps; bright store ambience with distant murmur and faint checkout beeps. NO music, no narration.

REALISM — HARD RULES: she keeps exactly the same face, hair, sweater and outfit as the start frame the whole clip. The shelf and every product box stay pixel-faithful to the start frame — same artwork, logo, colors, spelling, text rigid and never warping. The store background stays identical. Real phone-camera look, slight sensor noise, mild motion blur on the run, no cinematic bokeh, no text overlays, no watermark.
```

**Start image** - `starting_frames/v7_c01_g2.png` (passed as job id `f97d7572-0d90-4688-af6e-2555fe14ddb7`). No other media attached.

**Settings** - seedance_2_5 - mode omni_reference - 1080p - 9:16 - 5s - count 1 - credits (use_unlim false) - workspace Oneofone1. Submitted with `declined_preset_id = 24bae836-2c4a-48e0-89b6-49fcc0b21612` after the backend recommended the preset "IN THE DARK" instead of submitting; the payload was otherwise identical. Job `44dc2c9f-0650-4913-b26c-5ebe446a2c4f`. Output 5.05s, md5 `ae8d672411bb0accee5fa4a1c2680a57`.

---

## C02 - Hands on the box

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW Animated 2026-09-20 as `clips/v7_c02_g1.mp4`, FOR REVIEW.
*What it is:* two hands resting on the closed carton on the weathered elm table, the beat before it opens.

- frames: `v7_c02_g1.png` (current)
- clips: `v7_c02_g1.mp4` (current)

*Reused from* v6 C02 - changed: (a) the sleeve, now camel wool; (b) `SECOND - THE TABLE`, now weathered reclaimed elm plank, pale grey-brown, dead-matte hardwax oil, softly eased square edge; (c) `THIRD - THE BACKGROUND`, now the limewashed oat plaster living room with the lime plaster fireplace and reclaimed oak beam mantel; (d) the table dressing baubles, now terracotta and antique copper. The carton description, the hands clause, the quality tail and the wordmark spelling clause are byte-identical to v6.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c02_g1.png` | owns the geometry - camera position, top-down-ish angle, distance, the table plane, the hands' position and grip, the box's position, scale and angle |
| @Image 2 | `../../product_images/box_festive_green_g2.png` | owns the carton artwork |

media ids `1cdfcc53-e771-4bba-9eab-b1788346098b`, `2597b25d-60d1-4060-9602-32b0ee26c2f7`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `a8fbe9ef-5b65-42e3-973c-28e6bd5dc031`

```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a camel wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a weathered reclaimed elm plank table top: a pale grey-brown timber with wide open grain, small sound knots and fine saw marks left in the surface, finished in a dead-matte hardwax oil with no shine at all, and a softly eased square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused modern rustic American Christmas living room: walls in limewashed oat plaster with a soft chalky mottle, a plain lime plaster fireplace with a chunky reclaimed oak beam mantel and cream knitted stockings hanging from it, a decorated Christmas tree with warm white fairy lights and terracotta and antique copper ornaments standing off to one side, a slim black picture light glowing over a large dark abstract canvas, all well out of focus so the box stays the clear subject.

Dress the reclaimed elm table more festively: a sprig of fir and a few red berries, two or three small terracotta and antique copper baubles, a short cream candle, a soft warm string light trailing across the matte elm, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.
```

*Flag, not fixed:* the THEXMASGLOW wordmark has printed **twice** on this take - once on the green top face above the red band and again on the red band itself. Spelling is correct (eleven letters) in both. Same defect as v4/v5/v6 C02. Not re-rolled - Daniel decides.

### Video prompt - `clips/v7_c02_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c02_g1.png` - Higgsfield media `a8fbe9ef-5b65-42e3-973c-28e6bd5dc031`
**Extra references** - `@Video 1` - the v6 C02 unboxing-mechanics clip, Higgsfield media `1d2e8a8d-1e49-422a-8b04-d1a1230096a4` (mechanics only, silent - see the AUDIO RULE at the top of the prompt). Coerced by the backend to `video_references`.
**Job** - `43637e2f-a6e6-4430-b415-caed7b64d0d7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175626_43637e2f-a6e6-4430-b415-caed7b64d0d7.mp4

**Lineage** - Reused from v6 C02 - changed: the sleeve colour (deep plum wool -> camel wool, both mentions) and the table (French-polished deep mahogany -> weathered reclaimed elm plank), and `[5] LOCATION` rewritten to the v7 limewashed-oat room with its lime-plaster fireplace, reclaimed oak beam mantel, slim black picture light and terracotta/antique-copper baubles. The four priority rules (AUDIO, BOTH HANDS, EXIT, SPEED), every beat with its time range, `[9]` camera and the whole ban list are v6's words unchanged.

```
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a weathered reclaimed elm plank table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a camel wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a weathered reclaimed elm plank table fills the frame: pale grey-brown timber with wide open grain, small sound knots and fine saw marks, a dead-matte hardwax oil finish and a softly eased square edge. A short cream candle sits at the left, a sprig of fir with red berries and two or three small terracotta and antique copper baubles beside it, a soft warm string light trailing across the matte elm, and behind it limewashed oat plaster walls with a soft chalky mottle, a plain lime plaster fireplace with a chunky reclaimed oak beam mantel and hanging cream knitted stockings, a slim black picture light glowing over a large dark abstract canvas, and a decorated Christmas tree with warm white lights softly out of focus. The candle, the fir, the berries, the baubles, the string light, the defocused fireplace and the defocused tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the weathered reclaimed elm plank table, lid flaps folded back, with the candle, the fir, the berries, the defocused fireplace and the defocused tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
```

---

## C03 - The dome lifted out

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW Animated 2026-09-20 as `clips/v7_c03_g1.mp4`, FOR REVIEW.
*What it is:* the dome set down on the green marble counter, hand still on it.

- frames: `v7_c03_g1.png` (current)
- clips: `v7_c03_g1.mp4` (current)

*Reused from* v6 C03 - changed: (a) the sleeve, now camel wool; (b) the counter, now polished dark green Verde marble with white and pale jade veining, square mitred edge, high polish; (c) the kitchen behind it, now natural white oak slab fronts with slim black recessed finger pulls, a full-height travertine slab backsplash in warm oatmeal, and the matte black range on the LEFT. The dome description including the BLACK mesh lens disc, the hand clause, the camera clause and the quality tail are byte-identical to v6.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c03_g1.png` | owns the geometry - camera height, the counter plane, the dome's position and scale, the hand's approach |

media ids `7ccdd557-bfee-45b0-a067-0652320f537b`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `40b992eb-b4e3-4718-99c0-5e66ecf7c362`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a camel wool sweater sleeve pushed back; right forearm enters from the right in the same camel sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a polished dark green Verde marble counter: a deep forest green stone shot through with fine bright white and pale jade veining that branches across the surface, a square mitred edge, and a high polish that holds soft warm reflections. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A modern rustic American Christmas kitchen, softly defocused: natural white oak slab-front cabinets with slim black recessed finger pulls, a full-height travertine slab backsplash in warm oatmeal with its fine horizontal bedding lines running across it, a matte black range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

### Video prompt - `clips/v7_c03_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c03_g1.png` - Higgsfield media `40b992eb-b4e3-4718-99c0-5e66ecf7c362`
**Extra references** - none
**Job** - `bb8bfafb-46f2-49a1-ae03-2630f7bce07f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175626_bb8bfafb-46f2-49a1-ae03-2630f7bce07f.mp4

**Lineage** - Reused from v6 C03 - changed: the sleeve colour (deep plum -> camel) and the counter (honed cream limestone -> polished dark green Verde marble, including the `[11] PHYSICS` line, which becomes "The polished marble is hard"), plus the kitchen nouns to white oak slab fronts, slim black recessed finger pulls, a matte black range on the LEFT and a travertine slab backsplash. AUDIO RULE, NATURALNESS RULE and all five beats are v6's words unchanged.

```
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a polished dark green Verde marble kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in camel wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a polished dark green Verde marble countertop fills the lower half of frame and stays there for the whole clip - a deep forest green stone shot through with fine bright white and pale jade veining, a square mitred edge and a high polish; behind it a warm Christmas kitchen with natural white oak slab-front cabinets with slim black recessed finger pulls, a matte black range built into the tall cabinet run on the left, a full-height travertine slab backsplash in warm oatmeal, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the Verde marble counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The polished marble is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
```

---

## C04 - The cable going in

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW Animated 2026-09-20 as `clips/v7_c04_g1.mp4`, FOR REVIEW.
*What it is:* the plug pushed into the back of the dome on the same counter, seen from the other side.

- frames: `v7_c04_g1.png` (current)
- clips: `v7_c04_g1.mp4` (current)

*Reused from* v6 C04 - changed the same three nouns as C03, with the matte black range moved to the RIGHT so C03 and C04 read as two angles on one kitchen rather than two kitchens. The cable clause, the socket geometry, the dome description and the quality tail are byte-identical to v6.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c04_g1.png` | owns the geometry - camera height, the counter plane, the dome's position and scale, the cable and the hand |

media ids `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `1d282e66-6e60-4ac5-8519-d9e4ead9364d`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a camel wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a polished dark green Verde marble counter: a deep forest green stone shot through with fine bright white and pale jade veining that branches across the surface, a square mitred edge, and a high polish that holds soft warm reflections. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A modern rustic American Christmas kitchen, softly defocused across the top third of the frame: natural white oak slab-front cabinets with slim black recessed finger pulls, a full-height travertine slab backsplash in warm oatmeal with its fine horizontal bedding lines running across it, a matte black range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

*Why the range moves:* C03 and C04 are shot from opposite sides of the same counter. If the range stays on the same side in both, the room flips. This mirror is deliberate and carried from v3 onward.

### Video prompt - `clips/v7_c04_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c04_g1.png` - Higgsfield media `1d282e66-6e60-4ac5-8519-d9e4ead9364d`
**Extra references** - none
**Job** - `04967f82-13f3-467a-8d50-c67b3c676e08`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175626_04967f82-13f3-467a-8d50-c67b3c676e08.mp4

**Lineage** - Reused from v6 C04 - changed: the sleeve colour (deep plum -> camel), the counter (limestone -> Verde marble, including "the marble immediately around it") and the range moved to the RIGHT. FREEZE MEANS FREEZE, the RED-only lock, the black mesh disc starfield beat and the ban list are v6's words unchanged.

```
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a camel wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same camel sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a polished dark green Verde marble countertop fills the lower two thirds of frame and stays there for the whole clip - a deep forest green stone shot through with fine bright white and pale jade veining, a square mitred edge and a high polish; behind it a warm Christmas kitchen with natural white oak slab-front cabinets with slim black recessed finger pulls, a matte black range built into the tall cabinet run on the right, a full-height travertine slab backsplash in warm oatmeal, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the marble immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
```

---

## C05 - The door, then the room

*Section:* B-roll 2 - the reveal
*Status:* BOTH FRAMES GENERATED - TAKE 1 FOR REVIEW Animated 2026-09-20 as `clips/v7_c05_g1.mp4`, FOR REVIEW.
*What it is:* two frames. F1 is the closed door with the wreath, the beat before the push. F2 is what is behind it - the whole room already running.

- frames: `v7_c05_g1.png` (F1, current) - `references/v7_c05_r1.png` (F2, current)
- clips: `v7_c05_g1.mp4`, `v7_c05_g2.mp4`, `v7_c05_g3.mp4` (current)

F2 is filed in `references/` and not in `starting_frames/` because it is the *destination* of the C05 move, not a start frame in its own right. This follows the v6 precedent exactly.

### FRAME 1 - the closed door

*Reused from* v6 C05 FRAME 1 - changed: the door itself. v6's door was a flat slab; this one is a classic American **two-panel** door painted deep forest green eggshell with an antique brass knob and escutcheon. The exposure line was retargeted to `the forest green paint reads clearly as a deep green rather than black`. The wreath clause, the hallway clause, the camera clause, the ban list and the quality tail are byte-identical to v6.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c05_g2.png` | owns the geometry - the closed door filling the frame, the wreath's position and scale, the camera distance and the hallway light |

media ids `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0`

```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American two-panel door painted a deep forest green in a soft eggshell finish: crisp raised mouldings around two tall flat recessed panels, clean painted surfaces with the faintest brush texture, an antique brass knob and a matching antique brass escutcheon plate, set in a plain painted cream frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest green paint reads clearly as a deep green rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### FRAME 2 - the room behind it

*Reused from* v4 C05 FRAME 2 take 2 - changed: (a) the house, now `house_great_room_beams`; (b) the Christmas dressing, now terracotta and antique copper; (c) the knitwear on the two figures; (d) the projection signature, now the carousel of prancing reindeer and the ring of skaters on the frozen pond; (e) the escalation clause, which keeps the v4/v5/v6 text byte-identical and appends a second clause after it. Everything describing the camera, the doorway geometry, the real-architecture rule, the projector's position and the no-falling-snow ban is byte-identical to v4.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/references/v1_c05_r1.png` | owns the geometry - the open doorway, the camera standing in the hall looking through, the door leaf swung inward on the left, the room beyond |
| @Image 2 | `../../references/house_great_room_beams.png` | owns the architecture - a real photograph of a real great room. The projection is painted onto these surfaces; nothing about the room is invented |

media ids `f3a8c329-4152-4a22-9469-d89578812e09`, `e402f616-c876-4e01-bb5a-60774babf36a`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `fdb431f8-16b9-46f4-a377-05dad939cb2e`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its beams, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height living space whose ceiling is flat smooth cream plaster crossed by four heavy square-sawn pale oak beams running left to right at even spacing, each one a real chunky timber with square corners and visible grain where it lands on the wall, and one large rectangular flush skylight set into the plaster between the first two beams; a first-floor gallery landing crossing the left and centre of the room at mid height, its railing made of slim black metal balusters under a black top rail with a plain cream fascia below it; a straight run of stairs on the right coming down towards the camera with pale oak treads and the same slim black baluster railing; tall black-framed windows filling the right-hand wall to full height; pale limewashed plaster walls; and underneath the gallery an open kitchen with a white marble waterfall island, open shelving with pottery and a full-height pale oak cabinet run. Terracotta saltillo tile floor laid in a square pattern, a large faded Persian rug in rust, cream and terracotta, a big cream linen sectional sofa, a chunky rustic reclaimed-wood low coffee table, and a large olive tree in a terracotta pot in the right foreground. Copy the proportions, the beam spacing, the skylight, the railings and the stair from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall windows show a dark blue snow-covered night outside, there is no daylight and no sunlight anywhere in the room, every lamp, pendant and downlight in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing in front of the tall windows with warm white lights and terracotta and antique copper baubles and wrapped gifts underneath, a thick evergreen garland with pine cones and terracotta ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a bowl of terracotta and antique copper baubles on the coffee table. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every plaster wall, the whole flat plaster ceiling and its four heavy square oak beams, and the fascia and railing of the gallery landing, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and turning slowly above the rooftops one enormous glowing gold fairground carousel of prancing reindeer, its scalloped canopy strung with tiny bells and its centre pole a bright column of light, and on the frozen pond below it a wide ring of glowing gold ice skaters circling one behind another, each one trailing a long bright curved arc of light across the ice; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling plane and run with the direction of the oak beams instead of hanging as vertical curtains, and visibly break and step where each heavy beam crosses them; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the ceiling plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the wall above the gallery landing; one big brilliant north star high beside the skylight with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across the whole ceiling; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth; and beyond even that, great slow-turning glowing gold snow globes the size of a car drifting across the upper wall, each one holding its own tiny lit village inside it, a long glowing gold paper-chain garland of angels linked hand to hand curving right across the ceiling from one corner to the other, whole flights of glowing gold robins and doves crossing in loose Vs at three different depths, glowing gold ribbons of ivy and holly with bright red berries winding up every corner of the room, and a slow steady rise of glowing gold sparks lifting off the village chimneys and climbing the full height of the wall to join the star field, so every surface is so full that the eye cannot rest on any single thing. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the oak beams. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every heavy square oak beam with its grain and its square corners, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each beam breaks the light with its own hard shadow line where it stands proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the ceiling plane and stepping where it crosses each beam. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling crossed by four heavy oak beams with a skylight set between them, never as a backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The terracotta tile floor, the Persian rug, the cream sectional sofa, the olive tree, the Christmas tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

*Flag, not fixed:* `house_great_room_beams` was last used in **v5 C07**. Only four house photographs exist and v7 plus v8 need six room slots, so a collision was unavoidable - see the round summary.

### Video prompt - `clips/v7_c05_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c05_g1.png` - Higgsfield media `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0`
**Extra references** - `@Image 1` - `references/v7_c05_r1.png`, the room the projection is read from, Higgsfield media `fdb431f8-16b9-46f4-a377-05dad939cb2e`. Coerced by the backend to `image_references`.
**Job** - `1cab2e97-fe1b-4492-a374-2705b79607c8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175814_1cab2e97-fe1b-4492-a374-2705b79607c8.mp4

**Lineage** - Reused from v6 C05 take 5 - changed: at Daniel's instruction the Holding layer and the "ADD NOTHING. No smoke and no chimney plumes of any kind." paragraph were DELETED and replaced with eleven per-element motion paragraphs (CHIMNEY SMOKE, RISING SPARKS, AURORA, SLEIGH AND REINDEER, CAROUSEL, ICE SKATERS, SHOOTING STARS, SNOWFLAKES, SMALL TRAVELLERS, STAR FIELD, MOON AND NORTH STAR) built on the architecture already proven in v6 C06/C07; and beat 1.7-3.2s re-blocked so the boy runs and launches onto the sofa instead of standing still facing camera - that static child is the thing Daniel called out on v6. Duration stays 5s, camera still makes exactly two moves.

```
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s: a closed forest green two-panel door with a wreath, a hand on the antique brass knob.

THE PICTURE ON THE WALLS IS A CLOSED SET
The start image does not show the room, so read the room ONLY from @Image 1. Everything thrown onto the walls and the ceiling is already drawn in @Image 1. You are not designing a projection - you are making the one in @Image 1 move. Invent nothing. If a thing is not in the list below, it does not exist in this clip.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and the oak beams and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. @Image 1 is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element, and every one of these is moving at the same time:
- THE CHIMNEY SMOKE - every cottage chimney in the village is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - the glowing gold sparks lift off the village chimneys continuously and climb the full height of the wall to join the star field, drifting a little sideways as they rise and fading out near the top, with fresh ones leaving the pots for the whole clip.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the walls and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from where it sits in @Image 1, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail of light streams behind the runners, and the whole team rises and dips a little as it goes. The team is never parked.
- THE CAROUSEL - the great glowing gold fairground carousel above the rooftops TURNS, about a quarter of a full turn every second, its prancing reindeer swinging round with it and rising and falling on their poles as they pass, its scalloped canopy turning with them and its centre pole pulsing brighter and dimmer.
- THE ICE SKATERS - the ring of glowing gold skaters circles the frozen pond one behind another, covering about a third of the ring every second, each one leaning into the curve and laying down a long bright curved arc of light behind it that slowly fades off the ice as a fresh one is drawn.
- THE SHOOTING STARS - they streak across at their different angles, the tail thinning out behind them, and fade; fresh ones set off elsewhere for the whole clip.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the beams, so the density holds even.
- THE CANDY CANES, THE BUNTING, THE ICE CRYSTALS, THE SNOW GLOBES, THE ANGEL GARLAND AND THE BIRDS - all of them travel slowly across the surfaces they are painted on, the candy canes and the big faceted ice crystals turning end over end as they go, the snow globes turning slowly on their own centres, the birds beating their wings as their loose Vs cross.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON AND THE NORTH STAR - these two are the ONLY elements that hold their positions. They stay exactly where they are for the whole clip and only brighten and dim very slightly. Nothing else in the picture is allowed to hold still.
Because the walls and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the timber.

EVERY PROJECTED SHAPE IS PAINT, NOT AN OBJECT. All of it is flat light lying on whatever surface it lands on. It skews and stretches with the slope of that surface, it bends over the beams, it breaks where a wall meets the ceiling. Nothing ever floats free of a surface into the air of the room. There is no snow in the air of the room, none between the camera and the walls, none in front of the children, the sofa, the staircase or the tree, and none landing on the floor or on anyone.

WHAT ELSE HOLDS: the real room. The limewashed plaster walls, the flat cream plaster ceiling and its four heavy square-sawn pale oak beams, the flush skylight, the gallery landing and its slim black balusters, the straight stair on the right, the terracotta saltillo tile floor, the faded Persian rug in rust, cream and terracotta, the cream linen sectional sofa, the chunky reclaimed-wood coffee table, the olive tree in its terracotta pot, the real Christmas tree and its lights, the framing, the colours. The projected picture's outer edge stays put - it never rotates, spins, swings or slides across the room as one sheet. Only the things inside it travel.

@Image 1 is the authority on the room and on every projected shape: its layout, its beams, its stair, its furniture, its two children, and the exact set, style and colour of the projected shapes. It is a photograph - copy its look, never its stillness.

BEATS
0.0-0.7s - The hand turns the antique brass knob and pushes the door away from camera. Behind it the room is ALREADY running: smoke already climbing, snow already falling, the aurora already swelling, the carousel already turning, the reindeer already crossing. The widening gap simply uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on, spreads or grows as the door opens, and nothing glows along the door edge, frame or gap.
0.7-1.7s - The door swings wide and the camera walks through. The snow keeps falling at the same steady rate it already had, down the face of the far wall. It stays on that wall - it does not cross the open air of the room and it does not drift toward the camera.
1.7-3.2s - Inside. THE BOY, the child who is facing the camera at 0.0s, does NOT stay standing there: he turns on the spot away from the lens, runs three or four quick real steps across the rug and LAUNCHES HIMSELF UP ONTO THE CREAM LINEN SECTIONAL SOFA, landing on his knees on the cushions with both arms flying up, laughing. The cushions compress under him and spring back. THE GIRL stays where she is, still seen from behind, still looking up at the wall, shifting her weight and turning her head as she watches.
3.2-5.0s - Without a break THE BOY keeps bouncing on the cushions, pushing up and dropping back with his arms above his head, while the camera keeps walking and TILTS UP until the oak beams fill the top of frame. The ceiling is the busiest surface in the clip: snow pouring across it, the swell running along every aurora ribbon, the sleigh team crossing it, the ice crystals turning, the specks twinkling.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the walk from 0.7s, the tilt up from 3.2s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes - no phone, screen, hand or device in frame after 0.7s.

THE CHILDREN - exactly two, both visible from 1.7s on, no adults, no third child, no pets. Warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks, as in @Image 1. They never stand still and never pose. THE BOY is in continuous motion from 1.7s to the last frame.

SHARPNESS - hold the sharpness, exposure and fine detail of the start image: the panel edges and eggshell sheen of the forest green door, the antique brass knob and its escutcheon plate, the skin of the forearm and the thin gold bangle, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet on tile and rug, a body landing on sofa cushions, children laughing, quiet room tone. (no BGM). No music, no song, no score, no instruments, no bells used as music. No subtitles.

BANNED - a frozen or still picture; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a carousel that does not turn; skaters that do not circle; flakes that only twinkle without travelling; a still ceiling above moving walls; a shape that stays in the same place on the plaster when the list says it travels; a projection that appears to move only because the camera moves; the boy still standing front-on in the same spot at the end; children standing still or posed; snow, snowflakes or any particles falling through the open air of the room; volumetric or three-dimensional snow; anything drifting between the camera and the walls; snow passing in front of the children, the sofa, the staircase, the rug or the real tree; snow settling on the floor, the furniture or anyone's hair or shoulders; any projected shape that appears to leave the surface it is painted on; any projected shape that is not on the list above; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; any music; slow motion; blur or soft focus; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
```

### Video prompt - `clips/v7_c05_g2.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c05_g1.png` - Higgsfield media `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0` - unchanged, a fix is a prompt edit not a new frame
**Extra references** - `@Image 1` - `references/v7_c05_r1.png`, the room the projection is read from, Higgsfield media `fdb431f8-16b9-46f4-a377-05dad939cb2e`. Coerced by the backend to `image_references`. No video reference - banned on C05/C06/C07.
**Job** - `f26b8654-efa2-4ad2-ab57-b7cc1b6d2a15`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_184130_f26b8654-efa2-4ad2-ab57-b7cc1b6d2a15.mp4

**Lineage** - Rewritten from scratch off `v7_c05_g1` - changed: Daniel rejected g1 because the projection was effectively motionless. The g1 text was 10,938 characters and repeated the motion demand in the header, in eleven per-element paragraphs, in every beat, in POSITIVE LOCKS and in fifteen BANNED entries - which `feedback_projection_motion.md` says degrades the demand rather than reinforcing it, and which spent the 5-second budget on inventory instead of movement. g2 is 6,997 characters: the three elements Daniel named by hand (SMOKE, THE AURORA, THE SLEIGH) plus THE SNOW are hoisted into four short named-subject blocks at the top, each stated ONCE with a real-world feel and a rate; the other seven elements collapse into a single trailing sentence; the BANNED list is cut to the essentials. Same start frame, same references, same settings, camera unchanged at two moves.

```
TASK: image-to-video, 5 seconds, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed forest green two-panel door with a wreath, a hand on the antique brass knob. @Image 1 is the room behind that door and the authority on its layout, beams, stair, furniture, two children, colours, and on the exact set and style of every projected shape.

THE MOVING PICTURE IS THE SUBJECT OF THIS CLIP. The walls and the ceiling are a cinema screen with a film playing on them. The plaster and the pale oak beams hold perfectly still; the picture lying on them is running for all five seconds. @Image 1 is one paused frame of that film, and at 0.0s it un-pauses.

Four things carry the motion, and all four are running from the first frame to the last:

SMOKE. Every cottage chimney in the little village is smoking hard enough to see plainly. Each plume boils up out of its pot, leans to the right, climbs a full cottage-roof height every second and widens and thins away, while the next plume is already forming behind it.

THE AURORA. Each ribbon behaves like a long silk curtain hung in a slow draught: a swell travels along the ribbon from one end to the other, about a third of its length every second, brightening and thinning the ribbon as it passes and combing its lower fringe into new folds. The ribbon's arc stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its team of reindeer are FLYING. They travel across the ceiling, about a fifth of the ceiling's width every second, so that by 5.0s the team has crossed most of the way. Legs gallop, heads nod, the sleigh rocks behind them, the long tapering trail of light streams off the runners, and the whole team rises and dips as it goes. The team is never parked.

THE SNOW. Every snowflake and point of light drifts downward and slightly sideways, about a quarter of the wall's height every second, the way snow falls past a window at night, each one turning slowly on its own centre and breathing brighter and dimmer on its own timing. One that reaches the floor line fades out there as a fresh one fades in high near the beams, so the density never thins.

Everything else in the picture travels as well: the gold sparks lifting off the chimneys and climbing to the star field, the great fairground carousel turning with its reindeer rising and falling on their poles, the skaters circling the frozen pond and laying bright arcs behind them, the shooting stars streaking and fading, the candy canes and faceted ice crystals tumbling end over end, the snow globes turning, the birds beating across in loose Vs. Only the moon and the north star hold their positions; those two simply breathe brighter and dimmer.

The walls and the ceiling are lit by ONE projector and are therefore ONE picture: whatever the wall is doing, the ceiling is doing at the same instant and at the same speed. The picture's outer boundary is anchored — it never rotates, spins, swings or slides across the room as one sheet; only the things inside it travel. All of it is flat light lying on the surfaces: it skews with their slope, bends over the beams and breaks where wall meets ceiling. Nothing ever leaves a surface — no snow in the open air of the room, none between camera and wall, none in front of the children, the sofa, the stair or the real tree, none settling on the floor or on anyone.

BEATS
0.0-0.7s — The hand turns the brass knob and pushes the door away from camera. The room behind it is already running; the widening gap only uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on or spreads as the door opens. The door edge and frame stay plain painted wood — no glowing strip, no coloured fringe, no bright seam in the gap.
0.7-3.2s — The camera walks through and on across the rug. THE BOY, the child facing the camera at 0.0s, turns on the spot away from the lens, runs three or four quick real steps and LAUNCHES HIMSELF UP ONTO the cream linen sectional sofa, landing on his knees on the cushions with both arms flying up, laughing; the cushions compress under him and spring back. THE GIRL stays where she is, seen from behind, shifting her weight and turning her head to watch him.
3.2-5.0s — The boy keeps bouncing on the cushions, pushing up and dropping back with his arms above his head, while the camera tilts up to the oak beams. The ceiling is the busiest surface in the frame: snow pouring across it, the swell running along every aurora ribbon, the sleigh team crossing it, the specks twinkling.

CAMERA — eye height, normal wide-angle phone lens, natural handheld bounce. Two moves only: the walk from 0.7s, the tilt up from 3.2s. The camera is the person's eyes; no phone, screen, hand or device in frame after 0.7s.

THE CHILDREN — exactly two, both visible from 1.7s on, no adults, no third child, no pets. Rust-orange and cream fair-isle knitted jumpers with a band of little pine trees across the chest, oatmeal knitted lounge trousers, thick cream knitted socks, as in @Image 1.

SHARPNESS — hold the sharpness, exposure and fine detail of the start image: the panel edges and eggshell sheen of the forest green door, the brass knob and its escutcheon, the skin of the forearm and its thin gold bangle, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO — dry documentary sound only: the handle, the door swinging, running feet on tile and rug, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS — real-time motion at normal speed throughout. One continuous take. The picture is visibly in motion in every single frame — at the start, in the middle and in the last second. The boy ends the clip on the sofa, not standing where he began. Sharp focus to the final frame.

BANNED — a still or frozen picture; chimneys without smoke; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that twinkle but never travel; a still ceiling above a moving wall; a projection that appears to move only because the camera moves; light that moves for a moment and then stops; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric or three-dimensional snow; snow in front of the children, the sofa, the stair, the rug or the real tree; snow settling on anyone; any projected shape that leaves the surface it lies on; the boy still standing front-on at the end; children posed or standing still; jellyfish, fish, coral, bubbles or underwater imagery; a room lit entirely blue; the projector unit visible; slow motion; blur or soft focus; any music; a cut; a third child; an adult; subtitles; on-screen text.
```


---

### Video prompt - `clips/v7_c05_g3.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c05_g1.png` - Higgsfield media `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0` - unchanged, a fix is a prompt edit not a new frame
**Extra references** - `@Image 1` - `references/v7_c05_r1.png`, the room the projection is read from, Higgsfield media `fdb431f8-16b9-46f4-a377-05dad939cb2e`. Coerced by the backend to `image_references`. No video reference - banned on C05/C06/C07.
**Job** - `7cf7c73e-a010-45e6-abc2-4f98caf88ee9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_205021_7cf7c73e-a010-45e6-abc2-4f98caf88ee9.mp4

**Lineage** - Reused from `v7_c05_g2` - changed: the children's entrance only. Daniel: *"when the door open the kids look like they are stunned and they are not muving and than they start to move. When the door open the kids should already be moving."* g2 contained the line `THE GIRL stays where she is, seen from behind, shifting her weight and turning her head to watch him.` - that sentence is the literal instruction to freeze her, and it is the defect. Three surgical edits, nothing else touched: (a) beat 0.0-0.7s now says the room is running AND BOTH CHILDREN ARE ALREADY IN MOTION, so the door uncovers a run already under way; (b) the girl's `stays where she is` sentence is replaced with her own run - already mid-stride as the door opens, crossing the rug without breaking step, head back, one arm up pointing at the sleigh, still going on the last frame; (c) BANNED's weak `children posed or standing still;` is replaced with the explicit set: stunned, startled, waiting, hesitating, rooted to one spot, only turning her head while her feet stay planted, beginning motionless and starting later, stopping before 5.0s. The four hero motion blocks (SMOKE, THE AURORA, THE SLEIGH, THE SNOW), the two-move camera (walk from 0.7s, tilt up from 3.2s), the settings, the start frame and the reference are byte-identical to g2 - Daniel confirmed the projection motion in g2 was right.

```
TASK: image-to-video, 5 seconds, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed forest green two-panel door with a wreath, a hand on the antique brass knob. @Image 1 is the room behind that door and the authority on its layout, beams, stair, furniture, two children, colours, and on the exact set and style of every projected shape.

THE MOVING PICTURE IS THE SUBJECT OF THIS CLIP. The walls and the ceiling are a cinema screen with a film playing on them. The plaster and the pale oak beams hold perfectly still; the picture lying on them is running for all five seconds. @Image 1 is one paused frame of that film, and at 0.0s it un-pauses.

Four things carry the motion, and all four are running from the first frame to the last:

SMOKE. Every cottage chimney in the little village is smoking hard enough to see plainly. Each plume boils up out of its pot, leans to the right, climbs a full cottage-roof height every second and widens and thins away, while the next plume is already forming behind it.

THE AURORA. Each ribbon behaves like a long silk curtain hung in a slow draught: a swell travels along the ribbon from one end to the other, about a third of its length every second, brightening and thinning the ribbon as it passes and combing its lower fringe into new folds. The ribbon's arc stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its team of reindeer are FLYING. They travel across the ceiling, about a fifth of the ceiling's width every second, so that by 5.0s the team has crossed most of the way. Legs gallop, heads nod, the sleigh rocks behind them, the long tapering trail of light streams off the runners, and the whole team rises and dips as it goes. The team is never parked.

THE SNOW. Every snowflake and point of light drifts downward and slightly sideways, about a quarter of the wall's height every second, the way snow falls past a window at night, each one turning slowly on its own centre and breathing brighter and dimmer on its own timing. One that reaches the floor line fades out there as a fresh one fades in high near the beams, so the density never thins.

Everything else in the picture travels as well: the gold sparks lifting off the chimneys and climbing to the star field, the great fairground carousel turning with its reindeer rising and falling on their poles, the skaters circling the frozen pond and laying bright arcs behind them, the shooting stars streaking and fading, the candy canes and faceted ice crystals tumbling end over end, the snow globes turning, the birds beating across in loose Vs. Only the moon and the north star hold their positions; those two simply breathe brighter and dimmer.

The walls and the ceiling are lit by ONE projector and are therefore ONE picture: whatever the wall is doing, the ceiling is doing at the same instant and at the same speed. The picture's outer boundary is anchored — it never rotates, spins, swings or slides across the room as one sheet; only the things inside it travel. All of it is flat light lying on the surfaces: it skews with their slope, bends over the beams and breaks where wall meets ceiling. Nothing ever leaves a surface — no snow in the open air of the room, none between camera and wall, none in front of the children, the sofa, the stair or the real tree, none settling on the floor or on anyone.

BEATS
0.0-0.7s — The hand turns the brass knob and pushes the door away from camera. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION; the widening gap only uncovers more of something that was already going — a film that was already playing and two kids who were already running before the door opened. Nothing ignites, switches on or spreads as the door opens. The door edge and frame stay plain painted wood — no glowing strip, no coloured fringe, no bright seam in the gap.
0.7-3.2s — The camera walks through and on across the rug. BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. The door does not open on two kids standing stunned, frozen or waiting to be filmed who then start to move; it opens on two kids already in the middle of doing something, and neither of them is ever still. THE BOY, the child nearer the camera, is already turning away from the lens and pushing off his front foot as the gap widens; he runs three or four quick real steps and LAUNCHES HIMSELF UP ONTO the cream linen sectional sofa, landing on his knees on the cushions with both arms flying up, laughing; the cushions compress under him and spring back. THE GIRL is already mid-stride as well; she runs on across the rug without breaking step, tips her head right back to look straight up at the beams and throws one arm up pointing at the flying sleigh overhead, mouth open, delighted. Both runs are ordinary excited-kid running at real speed and real weight: feet landing, knees bending, arms swinging, hair and jumpers moving with them.
3.2-5.0s — The boy keeps bouncing on the cushions, pushing up and dropping back with his arms above his head, while THE GIRL keeps moving across the room and keeps her arm up pointing at the ceiling, still going on the last frame, and the camera tilts up to the oak beams. The ceiling is the busiest surface in the frame: snow pouring across it, the swell running along every aurora ribbon, the sleigh team crossing it, the specks twinkling.

CAMERA — eye height, normal wide-angle phone lens, natural handheld bounce. Two moves only: the walk from 0.7s, the tilt up from 3.2s. The camera is the person's eyes; no phone, screen, hand or device in frame after 0.7s.

THE CHILDREN — exactly two, both visible from 1.7s on, no adults, no third child, no pets. Rust-orange and cream fair-isle knitted jumpers with a band of little pine trees across the chest, oatmeal knitted lounge trousers, thick cream knitted socks, as in @Image 1.

SHARPNESS — hold the sharpness, exposure and fine detail of the start image: the panel edges and eggshell sheen of the forest green door, the brass knob and its escutcheon, the skin of the forearm and its thin gold bangle, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO — dry documentary sound only: the handle, the door swinging, running feet on tile and rug, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS — real-time motion at normal speed throughout. One continuous take. The picture is visibly in motion in every single frame — at the start, in the middle and in the last second. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to 5.0s: the boy ends the clip bouncing on the sofa, not standing where he began, and the girl ends it still moving and still pointing up at the beams. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED — a still or frozen picture; chimneys without smoke; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that twinkle but never travel; a still ceiling above a moving wall; a projection that appears to move only because the camera moves; light that moves for a moment and then stops; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric or three-dimensional snow; snow in front of the children, the sofa, the stair, the rug or the real tree; snow settling on anyone; any projected shape that leaves the surface it lies on; the boy still standing front-on at the end; either child standing still, frozen, stunned, startled, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head or shifts her weight while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before 5.0s; jellyfish, fish, coral, bubbles or underwater imagery; a room lit entirely blue; the projector unit visible; slow motion; blur or soft focus; any music; a cut; a third child; an adult; subtitles; on-screen text.
```

## C06 - The child in bed

*Section:* B-roll 2 - the reveal
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW Animated 2026-09-20 as `clips/v7_c06_g1.mp4`, FOR REVIEW.
*What it is:* a girl of about seven lying in bed looking up at the ceiling, the whole ceiling running.

- frames: `v7_c06_g1.png` (current)
- clips: `v7_c06_g1.mp4` (current)

*Reused from* v4 C06 take 2 - changed: (a) the house, now `house_bedroom_rafters`; (b) the child, now a girl of about seven with shoulder-length light brown hair; (c) the quilt, now rust-orange wool; (d) the projection signature, now the carousel and the skaters; (e) the escalation clause, with the second half appended. The camera clause, the bed geometry, the real-architecture rule, the projector's position on the nightstand and the no-falling-snow ban are byte-identical to v4.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c06_g1.png` | owns the geometry - camera height at the foot of the bed, the child's position in frame, how much ceiling is visible |
| @Image 2 | `../../references/house_bedroom_rafters.png` | owns the architecture - a real photograph of a real bedroom, rafters included |

media ids `0a845da6-2607-46cc-a595-4fee4b17d6a9`, `c1ea3b08-e710-4bda-9d33-4dd99b0e3012`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `6effc3a5-7218-453b-a756-9e97c76cf9ef`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with her family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its truss, its walls, its window and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a girl of about seven with shoulder-length light brown hair, fully dressed for winter in a warm rust-orange and cream fair-isle knitted Christmas jumper with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. She is standing up on top of the bed, knees bent and both arms raised out to her sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge. Wholesome family Christmas scene, a child at home with her family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom under a high vaulted roof, the ceiling two sloping planes of smooth cream plaster meeting at a ridge that runs away from the camera, crossed by heavy reclaimed oak rafters - a king-post truss near the front, its two rafters meeting at the ridge above a horizontal collar, and four or five more rafters marching down the right-hand slope onto a horizontal oak wall plate - with small recessed downlights set into the plaster between them, and a big black wrought-iron ring chandelier of two concentric rings carrying a row of plain candle bulbs hanging on a black rod from the ridge; a tall gable end wall on the left with a triangular-headed window above a pair of dark-framed glazed doors with side lights and long taupe linen curtains; a horizontal grey-brown plank accent wall behind the bed with three small framed prints in thin dark frames and a black wall sconce beside them; a low reclaimed-wood platform bed with a wide plank headboard, two nightstands with table lamps, wide pale oak plank floorboards and a large flat-weave oat rug. Copy the proportions, the rafter spacing, the king-post truss, the ridge, the ring chandelier and the gable window from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the gable window and the glazed doors show a dark blue snow-covered night outside, there is no daylight anywhere in the room, the ring chandelier and every downlight and table lamp are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a rust-orange wool quilt, a cream cable-knit throw and ticking-stripe pillows, a cream knitted stocking hangs from the rafter above the headboard, a warm fairy-light garland is strung around the gable window, a small lit Christmas tree stands on the floor beside the bed, and a small evergreen wreath with a terracotta bow hangs on the plank wall. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both sloping plaster ceiling planes, the heavy oak rafters and the king-post truss, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and turning slowly above the rooftops one enormous glowing gold fairground carousel of prancing reindeer, its scalloped canopy strung with tiny bells and its centre pole a bright column of light, and on the frozen pond below it a wide ring of glowing gold ice skaters circling one behind another, each one trailing a long bright curved arc of light across the ice; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the gable window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth; and beyond even that, great slow-turning glowing gold snow globes the size of a car drifting across the upper wall, each one holding its own tiny lit village inside it, a long glowing gold paper-chain garland of angels linked hand to hand curving right across the ceiling from one corner to the other, whole flights of glowing gold robins and doves crossing in loose Vs at three different depths, glowing gold ribbons of ivy and holly with bright red berries winding up every corner of the room, and a slow steady rise of glowing gold sparks lifting off the village chimneys and climbing the full height of the wall to join the star field, so every surface is so full that the eye cannot rest on any single thing. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the cream plaster and the oak rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, and every heavy reclaimed oak rafter, the king-post truss and the ridge, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the truss break the light with their own hard shadow lines where they stand proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as two sloping plaster planes meeting at a ridge and crossed by heavy oak rafters, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the flat-weave rug, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Her knitted jumper catches that spill so the jumper and the mid-bounce pose read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

*Flag, not fixed:* `house_bedroom_rafters` was last used in **v4 C06**. Three ads apart, which is the widest gap available.

### Video prompt - `clips/v7_c06_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c06_g1.png` - Higgsfield media `6effc3a5-7218-453b-a756-9e97c76cf9ef`
**Extra references** - none
**Job** - `ab635356-a3f3-4bd2-88e7-c7f20da772ad`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175814_ab635356-a3f3-4bd2-88e7-c7f20da772ad.mp4

**Lineage** - Reused from v6 C06 - changed: the camera inverted at Daniel's request so the shot starts high on the wall and TILTS DOWN 0.0-2.2s, then PULLS BACK in a small gentle zoom out 2.2-5.0s, instead of holding twice then tilting up; duration raised 4s -> 5s because two camera moves plus three bounces will not fit in four seconds (a deliberate departure from v6, recorded here); room, child, quilt and ornament nouns to v7; the trackable flake re-timed to pass mid-wall at 2.5s and fade at 5.0s; DO NOT INCLUDE gains "a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom". Every per-element motion paragraph is v6's words unchanged.

```
SUMMARY: a girl bounces on her bed in a vaulted rafter Christmas bedroom at night while a projected snow-village picture is PLAYING across the wall behind the bed and both sloping plaster ceiling planes, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, its ceiling of two sloping planes of smooth cream plaster meeting at a ridge that runs away from the camera crossed by heavy reclaimed oak rafters with a king-post truss near the front, the big black wrought-iron ring chandelier of two concentric rings, the tall gable end wall on the left with its triangular-headed window above a pair of dark-framed glazed doors, the horizontal grey-brown plank accent wall behind the bed, the low reclaimed-wood platform bed with its wide plank headboard and its rust-orange wool quilt, the wide pale oak plank floorboards, the large flat-weave oat rug, the Christmas dressing, THE GIRL and the colour.

SUBJECTS:
THE GIRL - exactly one child, a girl of about seven with shoulder-length light brown hair, in a warm rust-orange and cream fair-isle knitted Christmas jumper with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks, standing on the bed with her arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall and both sloping plaster ceiling planes. Everything glowing on the plaster and the oak is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a snow village low along the wall with gabled cottages with lit windows, a church steeple, snow-laden pine trees and a frozen pond, plumes above the chimneys, an enormous glowing gold fairground carousel of prancing reindeer turning above the rooftops, a ring of glowing gold ice skaters circling the frozen pond below it, wide aurora ribbons in warm gold, emerald green and deep rose lying along both ceiling slopes and kinking at the ridge, Santa's sleigh drawn by a team of eight flying reindeer keystoned across the slope, a big soft ivory moon high on the slope above the gable window, one big brilliant north star near the ridge, a dense field of warm gold stars of many sizes, long-tailed shooting stars, glowing gold candy canes, bunting, big faceted ice crystals, slow-turning snow globes, a paper-chain garland of angels, loose Vs of gold robins and doves, and a heavy fall of small glowing gold and cream six-point snowflakes and points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and the oak and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE GIRL and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element, and every one of these is moving at the same time:
- THE CHIMNEY SMOKE - every cottage chimney in the village is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - the glowing gold sparks lift off the village chimneys continuously and climb the full height of the wall to join the star field, drifting a little sideways as they rise and fading out near the top, with fresh ones leaving the pots for the whole clip.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on both ceiling slopes is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from where it sits in the start image, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail of light streams behind the runners, and the whole team rises and dips a little as it goes. The team is never parked.
- THE CAROUSEL - the great glowing gold fairground carousel above the rooftops TURNS, about a quarter of a full turn every second, its prancing reindeer swinging round with it and rising and falling on their poles as they pass, its scalloped canopy turning with them and its centre pole pulsing brighter and dimmer.
- THE ICE SKATERS - the ring of glowing gold skaters circles the frozen pond one behind another, covering about a third of the ring every second, each one leaning into the curve and laying down a long bright curved arc of light behind it that slowly fades off the ice as a fresh one is drawn.
- THE SHOOTING STARS - they streak across at their different angles, the tail thinning out behind them, and fade; fresh ones set off elsewhere for the whole clip.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts, breathes brighter and dimmer on its own timing, and cycles slowly through gold, cream and soft rose. One that reaches the skirting board fades out there while a fresh one fades in high near the ridge, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE CANDY CANES, THE BUNTING, THE ICE CRYSTALS, THE SNOW GLOBES, THE ANGEL GARLAND AND THE BIRDS - all of them travel slowly across the surfaces they are painted on, the candy canes and the big faceted ice crystals turning end over end as they go, the snow globes turning slowly on their own centres, the birds beating their wings as their loose Vs cross.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON AND THE NORTH STAR - these two are the ONLY elements that hold their positions. They stay exactly where they are for the whole clip and only brighten and dim very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and both ceiling slopes are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the oak.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the wall and the sloping plaster ceiling so the projected picture fills most of the frame and THE GIRL is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the rafters and the ridge sliding up out of the top of frame, until the bed and THE GIRL fill the lower half. THE GIRL bends her knees and pushes off the mattress; both feet leave the quilt, arms swinging up over her head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE GIRL lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; she is bouncing continuously and never stops. The wall and both ceiling slopes stay in frame throughout, the aurora rippling along them and the sleigh still flying across.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a girl laughing. (no BGM). No music, no song, no score, no instruments, no bells used as music. No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real girl jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN from the top of the wall, then a small slow pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a carousel that does not turn; skaters that do not circle; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; a projection that appears to move only because the camera moves; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
```

---

## C07 - The two children in the room

*Section:* B-roll 2 - the reveal
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW Animated 2026-09-20 as `clips/v7_c07_g1.mp4`, FOR REVIEW.
*What it is:* two children standing in the middle of the great room with the whole room running around them.

- frames: `v7_c07_g1.png` (current)
- clips: `v7_c07_g1.mp4` (current)

*Reused from* v5 C07 take 2 - changed: (a) the house, now `house_great_room_beams`; (b) the two children, now a girl of about eight with long wavy light brown hair and a boy of about five with short sandy brown hair; (c) the knitwear; (d) the Christmas dressing, now terracotta and antique copper; (e) the projection signature; (f) the escalation clause, with the second half appended; (g) one coherence edit - the room is now named as "the same house seen earlier in this ad, now from the middle of the great room", because C05 F2 opens onto it. The camera clause, the children's placement, the real-architecture rule and the no-falling-snow ban are byte-identical to v5.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c07_g1.png` | owns the geometry - camera height, the children's position and scale in frame, how much of the room and ceiling is in shot |
| @Image 2 | `../../references/house_great_room_beams.png` | owns the architecture - the same real great room C05 F2 opens onto |

media ids `c9a6740d-383b-4829-a7b9-f7a3c079c03f`, `e402f616-c876-4e01-bb5a-60774babf36a`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `49a02dae-3ad9-4cfa-9387-baeeb98bab32`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its beams, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long wavy light brown hair, the boy is about five with short sandy brown hair. Both are fully dressed for winter in warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height living space whose ceiling is flat smooth cream plaster crossed by four heavy square-sawn pale oak beams running left to right at even spacing, each one a real chunky timber with square corners and visible grain where it lands on the wall, and one large rectangular flush skylight set into the plaster between the first two beams; a first-floor gallery landing crossing the left and centre of the room at mid height, its railing made of slim black metal balusters under a black top rail with a plain cream fascia below it; a straight run of stairs on the right coming down towards the camera with pale oak treads and the same slim black baluster railing; tall black-framed windows filling the right-hand wall to full height; pale limewashed plaster walls; and underneath the gallery an open kitchen with a white marble waterfall island, open shelving with pottery and a full-height pale oak cabinet run. Terracotta saltillo tile floor laid in a square pattern, a large faded Persian rug in rust, cream and terracotta, a big cream linen sectional sofa, a chunky rustic reclaimed-wood low coffee table, and a large olive tree in a terracotta pot in the right foreground. The ceiling of this room is FLAT - there is no vault, no ridge and no sloping ceiling plane anywhere in it. Copy the proportions, the beam spacing, the skylight, the railings and the stair from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall windows show a dark blue snow-covered night outside, there is no daylight and no sunlight anywhere in the room, every lamp, pendant and downlight in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall slim real Christmas tree standing in front of the tall windows with warm white lights and terracotta and antique copper ornaments and wrapped gifts underneath, a thick evergreen garland with pine cones and terracotta ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a bowl of terracotta and antique copper ornaments on the coffee table. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every limewashed plaster wall, the whole flat plaster ceiling and its four heavy square oak beams, and the fascia and railing of the gallery landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and turning slowly above the rooftops one enormous glowing gold fairground carousel of prancing reindeer, its scalloped canopy strung with tiny bells and its centre pole a bright column of light, and on the frozen pond below it a wide ring of glowing gold ice skaters circling one behind another, each one trailing a long bright curved arc of light across the ice; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling plane and run with the direction of the oak beams instead of hanging as vertical curtains, and visibly break and step where each heavy beam crosses them; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the ceiling plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the wall above the gallery landing; one big brilliant north star high beside the skylight with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth; and beyond even that, great slow-turning glowing gold snow globes the size of a car drifting across the upper wall, each one holding its own tiny lit village inside it, a long glowing gold paper-chain garland of angels linked hand to hand curving right across the ceiling from one corner to the other, whole flights of glowing gold robins and doves crossing in loose Vs at three different depths, glowing gold ribbons of ivy and holly with bright red berries winding up every corner of the room, and a slow steady rise of glowing gold sparks lifting off the village chimneys and climbing the full height of the wall to join the star field, so every surface is so full that the eye cannot rest on any single thing. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the oak beams. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every heavy square oak beam with its grain and its square corners, all stay clearly visible THROUGH the coloured light, and each beam breaks the light with its own hard shadow line where it stands proud of the plaster. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the ceiling plane and stepping where it crosses each beam. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling crossed by four heavy oak beams with a skylight set between them, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The terracotta tile floor, the Persian rug, the cream sectional sofa, the olive tree, the Christmas tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

*Refusal note:* v4, v5 and v6 all hit `ip_detected` on C07 and needed a reword. This take passed **first submission**. The two additive edits baked into the v5 take-2 source - the "Wholesome family Christmas scene, children at home with their family at Christmas." opener and the "...so their knitted jumpers read clearly." ending - appear to clear the trigger preemptively. Keep both in any future C07.

### Video prompt - `clips/v7_c07_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v7_c07_g1.png` - Higgsfield media `49a02dae-3ad9-4cfa-9387-baeeb98bab32`
**Extra references** - none
**Job** - `705e9998-0bd0-4b0a-8d81-4cf223d9f99f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175814_705e9998-0bd0-4b0a-8d81-4cf223d9f99f.mp4

**Lineage** - Reused from v6 C07 - changed: only the room, children and wardrobe nouns to v7 (beamed great room; boy ~5 sandy brown on the rug, girl ~8 long wavy light brown on the sofa). The timeline (0.0-1.0 one step forward, 1.0-2.0 hold, 2.0-4.0 tilt up past the tree), the per-element motion block, the POSITIVE LOCKS and the ban list are v6's words unchanged, including the ip_detected-clearing opener and the "their knitted jumpers read clearly" lock carried from the v6 take that cleared.

```
Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected snow-village picture is PLAYING across the walls and the whole flat cream plaster ceiling and its four heavy square oak beams, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the flat cream plaster ceiling crossed by four heavy square-sawn pale oak beams with a flush rectangular skylight set between them, the first-floor gallery landing with its slim black metal balusters under a black top rail, the straight run of pale oak stairs on the right, the tall black-framed windows filling the right-hand wall with snow outside, the pale limewashed plaster walls, the open kitchen with its white marble waterfall island, the terracotta saltillo tile floor, the large faded Persian rug in rust, cream and terracotta, the big cream linen sectional sofa, the chunky rustic reclaimed-wood low coffee table, the large olive tree in its terracotta pot, the lit Christmas tree with its presents, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with short sandy brown hair, on the rug at the front left, back to camera, facing the wall, turning on the spot with his arms out.
THE OTHER CHILD - a girl of about eight with long wavy light brown hair, standing up on the cream linen sofa cushions, back to camera, with both arms raised toward the wall, bouncing on the spot.
Both in warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the walls and the whole ceiling. Everything glowing on the plaster and the oak is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a snow village low along the walls with gabled cottages with lit windows, a church steeple, snow-laden pine trees and a frozen pond, plumes above the chimneys, an enormous glowing gold fairground carousel of prancing reindeer turning above the rooftops, a ring of glowing gold ice skaters circling the frozen pond below it, wide aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls and lying along the ceiling with the direction of the oak beams, Santa's sleigh drawn by a team of eight flying reindeer keystoned across the ceiling, a big soft ivory moon high on the wall above the gallery landing, one big brilliant north star beside the skylight, a dense field of warm gold stars of many sizes, long-tailed shooting stars, glowing gold candy canes, bunting, big faceted ice crystals, slow-turning snow globes, a paper-chain garland of angels, loose Vs of gold robins and doves, and a heavy fall of small glowing gold and cream six-point snowflakes and points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and the oak and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element, and every one of these is moving at the same time:
- THE CHIMNEY SMOKE - every cottage chimney in the village is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - the glowing gold sparks lift off the village chimneys continuously and climb the full height of the wall to join the star field, drifting a little sideways as they rise and fading out near the top, with fresh ones leaving the pots for the whole clip.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the walls and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from where it sits in the start image, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail of light streams behind the runners, and the whole team rises and dips a little as it goes. The team is never parked.
- THE CAROUSEL - the great glowing gold fairground carousel above the rooftops TURNS, about a quarter of a full turn every second, its prancing reindeer swinging round with it and rising and falling on their poles as they pass, its scalloped canopy turning with them and its centre pole pulsing brighter and dimmer.
- THE ICE SKATERS - the ring of glowing gold skaters circles the frozen pond one behind another, covering about a third of the ring every second, each one leaning into the curve and laying down a long bright curved arc of light behind it that slowly fades off the ice as a fresh one is drawn.
- THE SHOOTING STARS - they streak across at their different angles, the tail thinning out behind them, and fade; fresh ones set off elsewhere for the whole clip.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the beams, so the density holds even.
- THE CANDY CANES, THE BUNTING, THE ICE CRYSTALS, THE SNOW GLOBES, THE ANGEL GARLAND AND THE BIRDS - all of them travel slowly across the surfaces they are painted on, the candy canes and the big faceted ice crystals turning end over end as they go, the snow globes turning slowly on their own centres, the birds beating their wings as their loose Vs cross.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON AND THE NORTH STAR - these two are the ONLY elements that hold their positions. They stay exactly where they are for the whole clip and only brighten and dim very slightly. Nothing else in the picture is allowed to hold still.
Because the walls and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the oak.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the beamed ceiling fills the upper half of the frame, the aurora rippling along it and the sleigh team still flying across it. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, socked feet on a rug. (no BGM). No music, no song, no score, no instruments, no bells used as music. No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a carousel that does not turn; skaters that do not circle; flakes that only twinkle without travelling; a still ceiling above moving walls; the whole picture rotating, spinning, sweeping or sliding as one sheet; a projection that appears to move only because the camera moves; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.
```

---

## Round summary

| card | frame | job | result |
|---|---|---|---|
| C01 | `v7_c01_g1.png` | `330ade78` | ok |
| C02 | `v7_c02_g1.png` | `a8fbe9ef` | ok - wordmark doubled, flagged |
| C03 | `v7_c03_g1.png` | `40b992eb` | ok |
| C04 | `v7_c04_g1.png` | `1d282e66` | ok |
| C05 F1 | `v7_c05_g1.png` | `ff4a3535` | ok |
| C05 F2 | `references/v7_c05_r1.png` | `fdb431f8` | ok |
| C06 | `v7_c06_g1.png` | `6effc3a5` | ok |
| C07 | `v7_c07_g1.png` | `49a02dae` | ok - no refusal, first try |

Eight frames, eight jobs, zero failures, zero refusals, zero re-rolls. All 1520 x 2688 PNG. C02-C07 ran in the B-roll round; C01 was added in the later hook round the same day.

## The house collision

Four house photographs exist. v7 and v8 together need six room slots - four great-room, two bedroom. A collision is forced. The rule carried from v6 is: within one ad C05 F2 and C07 must be the *same* house, because the door opens onto the room the next shot is inside; and when a reuse is forced, place it as many ads apart as possible and change the children, the knitwear and the Christmas dressing.

| slot | v7 house | last previous use |
|---|---|---|
| C05 F2 + C07 | `house_great_room_beams` | v5 C07 |
| C06 | `house_bedroom_rafters` | v4 C06 |

No new architecture was invented to avoid this. Per the standing rule, B-roll 2 geometry always comes off a photograph of a real house.

## Result URLs

CDN base `https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/`

```
v7_c02_g1.png              ->  hf_20260920_131859_a8fbe9ef-5b65-42e3-973c-28e6bd5dc031.png
v7_c03_g1.png              ->  hf_20260920_131859_40b992eb-b4e3-4718-99c0-5e66ecf7c362.png
v7_c04_g1.png              ->  hf_20260920_131859_1d282e66-6e60-4ac5-8519-d9e4ead9364d.png
v7_c05_g1.png              ->  hf_20260920_131859_ff4a3535-a332-4cc2-96b3-03b0dabb3cd0.png
references/v7_c05_r1.png   ->  hf_20260920_132004_fdb431f8-16b9-46f4-a377-05dad939cb2e.png
v7_c06_g1.png              ->  hf_20260920_132005_6effc3a5-7218-453b-a756-9e97c76cf9ef.png
v7_c07_g1.png              ->  hf_20260920_132315_49a02dae-3ad9-4cfa-9387-baeeb98bab32.png
```

Every file was downloaded from the CDN, copied onto the drive and md5-verified against the download. 14 of 14 matched.

## Next

1. Daniel reviews the seven frames on the board.
2. Nothing is animated until he picks. Video prompts go in this file under a `### Video prompt` subsection per card, with the reuse lineage recorded.
3. The doubled wordmark on C02 is a decision for him, not a self-initiated re-roll.

---

## Upscale run — 2026-09-20

All seven picked takes upscaled with **ByteDance Upscale · Model version Pro · 2K · 30fps**.
Preset **AIGC** on the hook (C01), **Common** on C02–C07 — the split Daniel specified.

"Picked take" here means the **last take** of each shot, which is what he asked for: C01 → g2,
C05 → g2, everything else single-take g1.

Results are saved in `clips/upscaled/` under the **source's exact filename** (the folder is the
suffix — no `_2k`, no `_upscaled`). All seven come back **1440×2560 @ 30fps**.

**Model version Pro is not reachable from the MCP.** `upscale_video`'s bytedance branch accepts
only `provider`, `video_id`, `width`, `height`, `resolution`, `fps`, `preset`, with
`additionalProperties: false`; passing `model_version` returns `Unrecognized key: "model_version"`.
Standard/Pro is **UI-only**, so this run was driven through `https://higgsfield.ai/upscale` in the
browser with the Chrome extension, exactly like the v33/v34/v35 runs on the LED curtain drive.

| Shot | Source clip | Src bytes | Preset | Upscale job | Result bytes | Result md5 |
|---|---|---|---|---|---|---|
| C01 | `v7_c01_g2.mp4` | 7295236 | **AIGC** | `a7bb8af0-53e8-43b7-87c9-bac5afe6db8b` | 10650648 | `103c71977f6fd867f4939669a1ca9a75` |
| C02 | `v7_c02_g1.mp4` | 1871637 | Common | `b846d07e-2f84-419c-911e-3528e5dcbe1a` | 8766952 | `2b33700400c0cb90f86aa232f104d7c2` |
| C03 | `v7_c03_g1.mp4` | 1609736 | Common | `8b5b7592-f54f-48bc-b88b-3c3e703d0c58` | 8658123 | `38f604d3e2f68b00c2ca712ac0c80472` |
| C04 | `v7_c04_g1.mp4` | 1061260 | Common | `cab656c2-ed03-42ad-b89b-1a17b854fd6a` | 6121553 | `8aef2579d3550d5a0bf65d206de1e10d` |
| C05 | `v7_c05_g2.mp4` | 3683333 | Common | `e139b170-0ddb-4f43-a0ab-ff10922e20da` | 11042862 | `d98a1b631bb862f5e557e64689e2d90e` |
| C06 | `v7_c06_g1.mp4` | 3674792 | Common | `e0ecab8c-cbaa-4fe0-8016-8a3e55b29c2e` | 10593327 | `f1ff0f4acfc7998eaed0e5a779da26ca` |
| C07 | `v7_c07_g1.mp4` | 2797633 | Common | `0ee06745-85dd-4a00-ac2a-69227dbbe0b2` | 9050116 | `7b07c90cb32b2a3bb5f4ddd6c51d39fa` |

**How the source clip gets into the page.** `file_upload` no longer accepts host filesystem paths.
Each clip was fetched back from Higgsfield's own CDN inside the page and injected through a
`DataTransfer` into `input[type=file]`. The fetched blob's byte count was checked against the local
file **before** every submit — a mistyped character in a job id silently 403s, and a
wrong-but-valid id would upscale the wrong clip at full price.

**Every submit was verified.** Clicking the green Upscale button can silently no-op: the page
blanks for a few seconds and re-renders the same form with no job created. The check is
`location.href` flipping from `?media=video--<id>` to `?media=video-job--<id>`; a re-click on the
same media URL works, because the upload and the preset both persist.

**The sticky-preset trap.** Preset persists across navigations, so after the AIGC hook submit a
freshly loaded panel still read AIGC. Every submit re-read the panel state first
(`aria-checked` on the version/resolution/fps toggles plus the preset label) and aborted rather
than submit anything that was not `Pro/2K/30fps` on the intended preset.

**Pulling results down.** Upscale jobs are invisible to `show_generation_by_ids` (`lookup_failed`),
so each result URL was read off `video.currentSrc` on
`https://higgsfield.ai/upscale/desktop?media=video-job--<id>` — the done test is the hostname
flipping from `d2ol7oe51mr4n9` (source, still rendering) to `d8j0ntlcm91z4` (result). The sandbox
curls `d8j0ntlcm91z4` directly, so nothing was downloaded through the browser. Every file was
md5-verified against its download after landing on the drive; 7 of 7 matched.


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v7_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v7_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v7_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v7_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v7_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v7_c05_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v7_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v7_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c05_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v7_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v7_c01_r1.png` | Embedded PNG `hf-job-id`: `37184f6d-1741-4903-9d59-7b26566313eb`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v7_c01_r2.png` | Embedded PNG `hf-job-id`: `d3bc5bcc-0d95-4fd9-9003-9e9360aba0fd`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v7_c05_r1.png` | Embedded PNG `hf-job-id`: `fdb431f8-16b9-46f4-a377-05dad939cb2e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c01_g1.png` | Embedded PNG `hf-job-id`: `330ade78-cfcc-4202-ac66-cb7809310383`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c01_g2.png` | Embedded PNG `hf-job-id`: `f97d7572-0d90-4688-af6e-2555fe14ddb7`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c02_g1.png` | Embedded PNG `hf-job-id`: `a8fbe9ef-5b65-42e3-973c-28e6bd5dc031`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c03_g1.png` | Embedded PNG `hf-job-id`: `40b992eb-b4e3-4718-99c0-5e66ecf7c362`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c04_g1.png` | Embedded PNG `hf-job-id`: `1d282e66-6e60-4ac5-8519-d9e4ead9364d`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c05_g1.png` | Embedded PNG `hf-job-id`: `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c06_g1.png` | Embedded PNG `hf-job-id`: `6effc3a5-7218-453b-a756-9e97c76cf9ef`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v7_c07_g1.png` | Embedded PNG `hf-job-id`: `49a02dae-3ad9-4cfa-9387-baeeb98bab32`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C01: the board did not show the exact clip prompt of `v7_c01_g2.mp4`; it now does (text above).
- C01: the board did not show the exact image prompt of `v7_c01_g2.png`; it now does.
- C02: the board did not show the exact clip prompt of `v7_c02_g1.mp4`; it now does (text above).
- C03: the board did not show the exact clip prompt of `v7_c03_g1.mp4`; it now does (text above).
- C04: the board did not show the exact clip prompt of `v7_c04_g1.mp4`; it now does (text above).
- C05: the board did not show the exact clip prompt of `v7_c05_g2.mp4`; it now does (text above).
- C06: the board did not show the exact clip prompt of `v7_c06_g1.mp4`; it now does (text above).
- C07: the board did not show the exact clip prompt of `v7_c07_g1.mp4`; it now does (text above).

### C01 — Store end-cap reaction

**In the cut:** `starting_frames/v7_c01_g2.png` → `clips/v7_c01_g2.mp4`

#### Image prompt — `starting_frames/v7_c01_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `f97d7572-0d90-4688-af6e-2555fe14ddb7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_173926_f97d7572-0d90-4688-af6e-2555fe14ddb7.png
**References, in submission order**
- @Image 1: `content/video_7_assets/references/v7_c01_r1.png` · Higgsfield media `1d8b4b34-7ef9-4002-ae4c-7d0d88cbf71e`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY as a photograph: the same camera position standing a couple of steps behind and slightly to the left of the woman, the same eye-level height, the same distance, the same vertical 9:16 framing, the same three-quarters-from-behind view of her with her head and shoulders cropped at the upper left of the frame, the same blue plastic shopping basket hanging from her hand low at the bottom left, the same white retail gondola shelving unit running across the right two thirds of the frame at the same oblique angle, the same four loaded shelves, the same tall narrow printed display banner standing at the right edge, the same polished grey concrete store floor, the same bright overhead store lighting and the same ceiling with its light fixtures across the top. Same composition, same scale of everything. Change only the three things below.

FIRST - THE PRODUCT BOXES. Every box on the shelves and every box stacked on top of the shelving unit is now OUR carton, exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, proportions about 1 to 1.6, forest green body, a dark red band across the top carrying a gold THEXMASGLOW wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR under it, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector standing on a separate white four-legged splayed stand base, a slim red remote printed beside it, a gold village skyline along the bottom edge, a thin gold foil border framing the panel, and no transparent window anywhere. SIZE IS CRITICAL: our carton is a SMALL package - roughly 15 cm wide by 15 cm deep by 24 cm tall, about the size of a shoebox stood upright on its end, no taller than the woman's forearm from wrist to elbow, and reaching only about half way up the gap between one shelf and the shelf above it, leaving a clear band of empty shelf air over every row. Do NOT copy the size of the boxes in the FIRST reference - those are much larger packages and their footprint must be ignored completely. Because our carton is small, MANY more of them fit: the cartons stand upright side by side, front panels facing the camera, packed tightly from one end of every shelf to the other with at least nine or ten of them across each shelf, four full shelves of them, perfectly aligned in dense neat rows the way a retail end-cap is faced, every carton identical to every other in size, proportion and printing.

SECOND - THE TALL DISPLAY BANNER at the right edge. It is now our banner: a tall narrow vertical printed panel in the same forest green as the carton with a gold foil border, a gold star at the top, the gold wordmark THEXMASGLOW, a cream serif headline CHRISTMAS LIGHT PROJECTOR, a large printed photograph of the white dome projector throwing warm gold trees and snowflakes across a dark living-room wall, and a column of small feature icons with the lines 16 Patterns, Remote Control, Timer and Indoor and Outdoor down the lower half. Same position, same width, same height, same angle as in the FIRST reference.

THIRD - THE WOMAN. A different woman from the reference: late 20s, long dark brown hair falling loose down her back, an oversized oatmeal cream knitted sweater, and matching American-flag Christmas pyjama bottoms - soft brushed cotton pyjama trousers with bold red and white horizontal stripes and small white five-pointed stars printed across the navy blue waistband panel, slightly loose the way real pyjamas fit - with white ribbed socks in white trainers. She stands in exactly the same place, the same three-quarters-from-behind pose, the same shoulders, the same head turn toward the shelf, the same arm down holding the same blue plastic shopping basket. Same scale in the frame.

FRAMING: leave a clean band of plain store ceiling across the very top of the image - roughly the top eighth of the frame - free of boxes, banners, signage and lettering, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room; she stays exactly the size she is in the FIRST reference.

The wordmark printed on the cartons and on the banner must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere in the picture.

LIGHTING AND QUALITY: bright, clean, evenly lit big-box store interior, neutral white balance with no orange and no colour cast, no dark corners. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp legible printing on every carton, realistic fabric and skin texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own cartons and banner.
````

#### Video prompt — `clips/v7_c01_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `44dc2c9f-0650-4913-b26c-5ebe446a2c4f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_174134_44dc2c9f-0650-4913-b26c-5ebe446a2c4f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c01_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c01_g2.png` · Higgsfield media `f97d7572-0d90-4688-af6e-2555fe14ddb7`

````text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by a friend standing a few steps behind the woman — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in; all distance changes happen because the woman physically moves, never the lens.

Start frame: a young woman in a cream knit sweater and American-flag pajama pants stands in a bright store aisle holding a blue shopping basket, facing the shelf stacked with the green THEXMASGLOW CHRISTMAS LIGHT PROJECTOR product boxes.

ACTION TIMELINE:
0.0–1.0s — She spots the boxes on the shelf, freezes for a split second, then screams with real excitement: "No way — they actually have it!" Her whole body reacts, shoulders jumping.
1.0–2.0s — She lets the blue shopping basket drop straight out of her hand — it hits the store floor with a loud plastic clatter and tips over — as she spins around to the friend filming, one hand flying to her mouth, eyes huge, pure disbelief on her face.
2.0–3.5s — She whips back around and runs the few steps to the shelf, sweater flapping, shoes squeaking on the store floor, the camera staying put and letting her get smaller toward the shelf.
3.5–5.0s — She grabs one THEXMASGLOW CHRISTMAS LIGHT PROJECTOR box off the shelf with both hands, hugs it to her chest, and bounces on her feet laughing, extremely happy, turning halfway back toward the camera to show it. End frame: her hugging the box, beaming.

AUDIO: her real voice, lip-synced — the excited scream and line, then breathless laughing; the loud clatter of the dropped basket; running footsteps; bright store ambience with distant murmur and faint checkout beeps. NO music, no narration.

REALISM — HARD RULES: she keeps exactly the same face, hair, sweater and outfit as the start frame the whole clip. The shelf and every product box stay pixel-faithful to the start frame — same artwork, logo, colors, spelling, text rigid and never warping. The store background stays identical. Real phone-camera look, slight sensor noise, mild motion blur on the run, no cinematic bokeh, no text overlays, no watermark.
````

**Other takes of C01 on disk (4)**

#### Image prompt — `starting_frames/v7_c01_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `330ade78-cfcc-4202-ac66-cb7809310383`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141118_330ade78-cfcc-4202-ac66-cb7809310383.png
**References, in submission order**
- @Image 1: `content/video_7_assets/references/v7_c01_r1.png` · Higgsfield media `1d8b4b34-7ef9-4002-ae4c-7d0d88cbf71e`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY as a photograph: the same camera position standing a couple of steps behind and slightly to the left of the woman, the same eye-level height, the same distance, the same vertical 9:16 framing, the same three-quarters-from-behind view of her with her head and shoulders cropped at the upper left of the frame, the same blue plastic shopping basket hanging from her hand low at the bottom left, the same white retail gondola shelving unit running across the right two thirds of the frame at the same oblique angle, the same four loaded shelves, the same tall narrow printed display banner standing at the right edge, the same polished grey concrete store floor, the same bright overhead store lighting and the same ceiling with its light fixtures across the top. Same composition, same scale of everything. Change only the three things below.

FIRST - THE PRODUCT BOXES. Every box on the shelves and every box stacked on top of the shelving unit is now OUR carton, exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, proportions about 1 to 1.6, forest green body, a dark red band across the top carrying a gold THEXMASGLOW wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR under it, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector standing on a separate white four-legged splayed stand base, a slim red remote printed beside it, a gold village skyline along the bottom edge, a thin gold foil border framing the panel, and no transparent window anywhere. The cartons stand upright side by side, front panels facing the camera, filling every shelf from end to end, four full shelves of them, perfectly aligned in neat rows the way a retail end-cap is faced, identical to each other. They keep the same footprint and the same rhythm on the shelf as the boxes in the FIRST reference.

SECOND - THE TALL DISPLAY BANNER at the right edge. It is now our banner: a tall narrow vertical printed panel in the same forest green as the carton with a gold foil border, a gold star at the top, the gold wordmark THEXMASGLOW, a cream serif headline CHRISTMAS LIGHT PROJECTOR, a large printed photograph of the white dome projector throwing warm gold trees and snowflakes across a dark living-room wall, and a column of small feature icons with the lines 16 Patterns, Remote Control, Timer and Indoor and Outdoor down the lower half. Same position, same width, same height, same angle as in the FIRST reference.

THIRD - THE WOMAN. A different woman from the reference: late 20s, long dark brown hair falling loose down her back, an oversized oatmeal cream knitted sweater, and matching American-flag Christmas pyjama bottoms - soft brushed cotton pyjama trousers with bold red and white horizontal stripes and small white five-pointed stars printed across the navy blue waistband panel, slightly loose the way real pyjamas fit - with white ribbed socks in white trainers. She stands in exactly the same place, the same three-quarters-from-behind pose, the same shoulders, the same head turn toward the shelf, the same arm down holding the same blue plastic shopping basket. Same scale in the frame.

FRAMING: leave a clean band of plain store ceiling across the very top of the image - roughly the top eighth of the frame - free of boxes, banners, signage and lettering, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room; she stays exactly the size she is in the FIRST reference.

The wordmark printed on the cartons and on the banner must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere in the picture.

LIGHTING AND QUALITY: bright, clean, evenly lit big-box store interior, neutral white balance with no orange and no colour cast, no dark corners. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp legible printing on every carton, realistic fabric and skin texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own cartons and banner.
````

#### Image prompt — `references/v7_c01_r1.png`

Not a Higgsfield generation on record (no matching job in the workspace history) — a supplied reference.

#### Image prompt — `references/v7_c01_r2.png`

**Settings** - gpt_image_2 · 3:4 · 2k · medium · 1744×2336
**Job** - `d3bc5bcc-0d95-4fd9-9003-9e9360aba0fd`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_130008_d3bc5bcc-0d95-4fd9-9003-9e9360aba0fd.png
**Same Higgsfield job as** - `content/video_9_assets/references/v9_c01_r1.png`
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `4f4786eb-3c1b-40f9-b35d-392739e67e89`
- @Image 2: uploaded image, not on the drive · Higgsfield media `ff48b1ad-6883-4b35-8ea5-0bc685278098`

````text
Photorealistic retail packaging packshot. Recreate the box in the first reference image EXACTLY — same festive green artwork, same red top band with THEXMASGLOW in gold serif capitals, same cream serif CHRISTMAS LIGHT PROJECTOR headline, same gold foil border and tonal snowflakes, same gold village skyline along the bottom, same printed projector render and red remote, same '16 Patterns | Remote Control | Timer' caption line, same grey seamless background, same lighting, same slight three-quarter angle, same two hands gripping the sides with wrists cropped.

THE ONLY CHANGE: the carton is a noticeably LARGER package. Scale it up from roughly 12 x 12 x 20 cm to roughly 15 x 15 x 24 cm, keeping the same 1 : 1.6 tall upright proportions and the same square footprint. The hands must stay adult-sized and normal — because the box is bigger, the fingers now wrap a smaller fraction of the side panels and the box reads as a substantial, heavier package. Do not simply crop in closer; the hands must visibly be smaller relative to the box than in the reference.

Keep the tuck-top construction: a separate flat lid panel on top with a visible seam running around the top, closed and sealed, small centred gold THEXMASGLOW wordmark on the lid.

The printed product render stays the projector from the second reference photo: a smooth white dome-topped cylindrical body on a separate white four-legged splayed stand base, light exiting the TOP of the dome, with a slim red handheld remote beside it. Not a camera, no front lens, no swivel head.

Normal wide-angle lens, natural perspective, vertical box edges stay vertical and parallel. All printed text correctly spelled and sharply legible. No fisheye, no barrel distortion, no lens warping, no transparent window.
````

#### Video prompt — `clips/v7_c01_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `a5da6166-0752-4ab3-95ec-b01a817f070b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_171604_a5da6166-0752-4ab3-95ec-b01a817f070b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: uploaded image, not on the drive · Higgsfield media `7bf2c68b-42b7-4596-8ad4-5156a3493834`

````text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by a friend standing a few steps behind the woman — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in; all distance changes happen because the woman physically moves, never the lens.

Start frame: a young woman in a cream knit sweater and American-flag pajama pants stands in a bright store aisle holding a blue shopping basket, facing the shelf stacked with the green THEXMASGLOW CHRISTMAS LIGHT PROJECTOR product boxes.

ACTION TIMELINE:
0.0–1.0s — She spots the boxes on the shelf, freezes for a split second, then screams with real excitement: "No way — they actually have it!" Her whole body reacts, shoulders jumping.
1.0–2.0s — She lets the blue shopping basket drop straight out of her hand — it hits the store floor with a loud plastic clatter and tips over — as she spins around to the friend filming, one hand flying to her mouth, eyes huge, pure disbelief on her face.
2.0–3.5s — She whips back around and runs the few steps to the shelf, sweater flapping, shoes squeaking on the store floor, the camera staying put and letting her get smaller toward the shelf.
3.5–5.0s — She grabs one THEXMASGLOW CHRISTMAS LIGHT PROJECTOR box off the shelf with both hands, hugs it to her chest, and bounces on her feet laughing, extremely happy, turning halfway back toward the camera to show it. End frame: her hugging the box, beaming.

AUDIO: her real voice, lip-synced — the excited scream and line, then breathless laughing; the loud clatter of the dropped basket; running footsteps; bright store ambience with distant murmur and faint checkout beeps. NO music, no narration.

REALISM — HARD RULES: she keeps exactly the same face, hair, sweater and outfit as the start frame the whole clip. The shelf and every product box stay pixel-faithful to the start frame — same artwork, logo, colors, spelling, text rigid and never warping. The store background stays identical. Real phone-camera look, slight sensor noise, mild motion blur on the run, no cinematic bokeh, no text overlays, no watermark.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v7_c02_g1.png` → `clips/v7_c02_g1.mp4`

#### Image prompt — `starting_frames/v7_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a8fbe9ef-5b65-42e3-973c-28e6bd5dc031`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_131859_a8fbe9ef-5b65-42e3-973c-28e6bd5dc031.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `1cdfcc53-e771-4bba-9eab-b1788346098b`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a camel wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a weathered reclaimed elm plank table top: a pale grey-brown timber with wide open grain, small sound knots and fine saw marks left in the surface, finished in a dead-matte hardwax oil with no shine at all, and a softly eased square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused modern rustic American Christmas living room: walls in limewashed oat plaster with a soft chalky mottle, a plain lime plaster fireplace with a chunky reclaimed oak beam mantel and cream knitted stockings hanging from it, a decorated Christmas tree with warm white fairy lights and terracotta and antique copper ornaments standing off to one side, a slim black picture light glowing over a large dark abstract canvas, all well out of focus so the box stays the clear subject.

Dress the reclaimed elm table more festively: a sprig of fir and a few red berries, two or three small terracotta and antique copper baubles, a short cream candle, a soft warm string light trailing across the matte elm, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.
````

#### Video prompt — `clips/v7_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `43637e2f-a6e6-4430-b415-caed7b64d0d7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175626_43637e2f-a6e6-4430-b415-caed7b64d0d7.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c02_g1.png` · Higgsfield media `a8fbe9ef-5b65-42e3-973c-28e6bd5dc031`
- video ref 1: `references/scene_no_audio-2.mp4` — upload · 2.14 s · Higgsfield media `1d2e8a8d-1e49-422a-8b04-d1a1230096a4`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a weathered reclaimed elm plank table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a camel wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a weathered reclaimed elm plank table fills the frame: pale grey-brown timber with wide open grain, small sound knots and fine saw marks, a dead-matte hardwax oil finish and a softly eased square edge. A short cream candle sits at the left, a sprig of fir with red berries and two or three small terracotta and antique copper baubles beside it, a soft warm string light trailing across the matte elm, and behind it limewashed oat plaster walls with a soft chalky mottle, a plain lime plaster fireplace with a chunky reclaimed oak beam mantel and hanging cream knitted stockings, a slim black picture light glowing over a large dark abstract canvas, and a decorated Christmas tree with warm white lights softly out of focus. The candle, the fir, the berries, the baubles, the string light, the defocused fireplace and the defocused tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the weathered reclaimed elm plank table, lid flaps folded back, with the candle, the fir, the berries, the defocused fireplace and the defocused tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v7_c03_g1.png` → `clips/v7_c03_g1.mp4`

#### Image prompt — `starting_frames/v7_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `40b992eb-b4e3-4718-99c0-5e66ecf7c362`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_131859_40b992eb-b4e3-4718-99c0-5e66ecf7c362.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `7ccdd557-bfee-45b0-a067-0652320f537b`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a camel wool sweater sleeve pushed back; right forearm enters from the right in the same camel sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a polished dark green Verde marble counter: a deep forest green stone shot through with fine bright white and pale jade veining that branches across the surface, a square mitred edge, and a high polish that holds soft warm reflections. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A modern rustic American Christmas kitchen, softly defocused: natural white oak slab-front cabinets with slim black recessed finger pulls, a full-height travertine slab backsplash in warm oatmeal with its fine horizontal bedding lines running across it, a matte black range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v7_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `bb8bfafb-46f2-49a1-ae03-2630f7bce07f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175626_bb8bfafb-46f2-49a1-ae03-2630f7bce07f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c03_g1.png` · Higgsfield media `40b992eb-b4e3-4718-99c0-5e66ecf7c362`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a polished dark green Verde marble kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in camel wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a polished dark green Verde marble countertop fills the lower half of frame and stays there for the whole clip - a deep forest green stone shot through with fine bright white and pale jade veining, a square mitred edge and a high polish; behind it a warm Christmas kitchen with natural white oak slab-front cabinets with slim black recessed finger pulls, a matte black range built into the tall cabinet run on the left, a full-height travertine slab backsplash in warm oatmeal, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the Verde marble counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The polished marble is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v7_c04_g1.png` → `clips/v7_c04_g1.mp4`

#### Image prompt — `starting_frames/v7_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `1d282e66-6e60-4ac5-8519-d9e4ead9364d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_131859_1d282e66-6e60-4ac5-8519-d9e4ead9364d.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a camel wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a polished dark green Verde marble counter: a deep forest green stone shot through with fine bright white and pale jade veining that branches across the surface, a square mitred edge, and a high polish that holds soft warm reflections. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A modern rustic American Christmas kitchen, softly defocused across the top third of the frame: natural white oak slab-front cabinets with slim black recessed finger pulls, a full-height travertine slab backsplash in warm oatmeal with its fine horizontal bedding lines running across it, a matte black range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v7_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `04967f82-13f3-467a-8d50-c67b3c676e08`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175626_04967f82-13f3-467a-8d50-c67b3c676e08.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c04_g1.png` · Higgsfield media `1d282e66-6e60-4ac5-8519-d9e4ead9364d`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a camel wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same camel sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a polished dark green Verde marble countertop fills the lower two thirds of frame and stays there for the whole clip - a deep forest green stone shot through with fine bright white and pale jade veining, a square mitred edge and a high polish; behind it a warm Christmas kitchen with natural white oak slab-front cabinets with slim black recessed finger pulls, a matte black range built into the tall cabinet run on the right, a full-height travertine slab backsplash in warm oatmeal, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the marble immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v7_c05_g1.png`, `references/v7_c05_r1.png` → `clips/v7_c05_g2.mp4`

#### Image prompt — `starting_frames/v7_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_131859_ff4a3535-a332-4cc2-96b3-03b0dabb3cd0.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American two-panel door painted a deep forest green in a soft eggshell finish: crisp raised mouldings around two tall flat recessed panels, clean painted surfaces with the faintest brush texture, an antique brass knob and a matching antique brass escutcheon plate, set in a plain painted cream frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest green paint reads clearly as a deep green rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Image prompt — `references/v7_c05_r1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `fdb431f8-16b9-46f4-a377-05dad939cb2e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_132004_fdb431f8-16b9-46f4-a377-05dad939cb2e.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `f3a8c329-4152-4a22-9469-d89578812e09`
- @Image 2: `references/house_great_room_beams.png` · Higgsfield media `e402f616-c876-4e01-bb5a-60774babf36a`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its beams, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height living space whose ceiling is flat smooth cream plaster crossed by four heavy square-sawn pale oak beams running left to right at even spacing, each one a real chunky timber with square corners and visible grain where it lands on the wall, and one large rectangular flush skylight set into the plaster between the first two beams; a first-floor gallery landing crossing the left and centre of the room at mid height, its railing made of slim black metal balusters under a black top rail with a plain cream fascia below it; a straight run of stairs on the right coming down towards the camera with pale oak treads and the same slim black baluster railing; tall black-framed windows filling the right-hand wall to full height; pale limewashed plaster walls; and underneath the gallery an open kitchen with a white marble waterfall island, open shelving with pottery and a full-height pale oak cabinet run. Terracotta saltillo tile floor laid in a square pattern, a large faded Persian rug in rust, cream and terracotta, a big cream linen sectional sofa, a chunky rustic reclaimed-wood low coffee table, and a large olive tree in a terracotta pot in the right foreground. Copy the proportions, the beam spacing, the skylight, the railings and the stair from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall windows show a dark blue snow-covered night outside, there is no daylight and no sunlight anywhere in the room, every lamp, pendant and downlight in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing in front of the tall windows with warm white lights and terracotta and antique copper baubles and wrapped gifts underneath, a thick evergreen garland with pine cones and terracotta ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a bowl of terracotta and antique copper baubles on the coffee table. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every plaster wall, the whole flat plaster ceiling and its four heavy square oak beams, and the fascia and railing of the gallery landing, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and turning slowly above the rooftops one enormous glowing gold fairground carousel of prancing reindeer, its scalloped canopy strung with tiny bells and its centre pole a bright column of light, and on the frozen pond below it a wide ring of glowing gold ice skaters circling one behind another, each one trailing a long bright curved arc of light across the ice; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling plane and run with the direction of the oak beams instead of hanging as vertical curtains, and visibly break and step where each heavy beam crosses them; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the ceiling plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the wall above the gallery landing; one big brilliant north star high beside the skylight with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across the whole ceiling; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth; and beyond even that, great slow-turning glowing gold snow globes the size of a car drifting across the upper wall, each one holding its own tiny lit village inside it, a long glowing gold paper-chain garland of angels linked hand to hand curving right across the ceiling from one corner to the other, whole flights of glowing gold robins and doves crossing in loose Vs at three different depths, glowing gold ribbons of ivy and holly with bright red berries winding up every corner of the room, and a slow steady rise of glowing gold sparks lifting off the village chimneys and climbing the full height of the wall to join the star field, so every surface is so full that the eye cannot rest on any single thing. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the oak beams. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every heavy square oak beam with its grain and its square corners, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each beam breaks the light with its own hard shadow line where it stands proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the ceiling plane and stepping where it crosses each beam. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling crossed by four heavy oak beams with a skylight set between them, never as a backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The terracotta tile floor, the Persian rug, the cream sectional sofa, the olive tree, the Christmas tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v7_c05_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `f26b8654-efa2-4ad2-ab57-b7cc1b6d2a15`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_184130_f26b8654-efa2-4ad2-ab57-b7cc1b6d2a15.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c05_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c05_g1.png` · Higgsfield media `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0`
- image ref 1: `content/video_7_assets/references/v7_c05_r1.png` · Higgsfield media `fdb431f8-16b9-46f4-a377-05dad939cb2e`

````text
TASK: image-to-video, 5 seconds, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed forest green two-panel door with a wreath, a hand on the antique brass knob. @Image 1 is the room behind that door and the authority on its layout, beams, stair, furniture, two children, colours, and on the exact set and style of every projected shape.

THE MOVING PICTURE IS THE SUBJECT OF THIS CLIP. The walls and the ceiling are a cinema screen with a film playing on them. The plaster and the pale oak beams hold perfectly still; the picture lying on them is running for all five seconds. @Image 1 is one paused frame of that film, and at 0.0s it un-pauses.

Four things carry the motion, and all four are running from the first frame to the last:

SMOKE. Every cottage chimney in the little village is smoking hard enough to see plainly. Each plume boils up out of its pot, leans to the right, climbs a full cottage-roof height every second and widens and thins away, while the next plume is already forming behind it.

THE AURORA. Each ribbon behaves like a long silk curtain hung in a slow draught: a swell travels along the ribbon from one end to the other, about a third of its length every second, brightening and thinning the ribbon as it passes and combing its lower fringe into new folds. The ribbon's arc stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its team of reindeer are FLYING. They travel across the ceiling, about a fifth of the ceiling's width every second, so that by 5.0s the team has crossed most of the way. Legs gallop, heads nod, the sleigh rocks behind them, the long tapering trail of light streams off the runners, and the whole team rises and dips as it goes. The team is never parked.

THE SNOW. Every snowflake and point of light drifts downward and slightly sideways, about a quarter of the wall's height every second, the way snow falls past a window at night, each one turning slowly on its own centre and breathing brighter and dimmer on its own timing. One that reaches the floor line fades out there as a fresh one fades in high near the beams, so the density never thins.

Everything else in the picture travels as well: the gold sparks lifting off the chimneys and climbing to the star field, the great fairground carousel turning with its reindeer rising and falling on their poles, the skaters circling the frozen pond and laying bright arcs behind them, the shooting stars streaking and fading, the candy canes and faceted ice crystals tumbling end over end, the snow globes turning, the birds beating across in loose Vs. Only the moon and the north star hold their positions; those two simply breathe brighter and dimmer.

The walls and the ceiling are lit by ONE projector and are therefore ONE picture: whatever the wall is doing, the ceiling is doing at the same instant and at the same speed. The picture's outer boundary is anchored - it never rotates, spins, swings or slides across the room as one sheet; only the things inside it travel. All of it is flat light lying on the surfaces: it skews with their slope, bends over the beams and breaks where wall meets ceiling. Nothing ever leaves a surface - no snow in the open air of the room, none between camera and wall, none in front of the children, the sofa, the stair or the real tree, none settling on the floor or on anyone.

BEATS
0.0-0.7s - The hand turns the brass knob and pushes the door away from camera. The room behind it is already running; the widening gap only uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on or spreads as the door opens. The door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.7-3.2s - The camera walks through and on across the rug. THE BOY, the child facing the camera at 0.0s, turns on the spot away from the lens, runs three or four quick real steps and LAUNCHES HIMSELF UP ONTO the cream linen sectional sofa, landing on his knees on the cushions with both arms flying up, laughing; the cushions compress under him and spring back. THE GIRL stays where she is, seen from behind, shifting her weight and turning her head to watch him.
3.2-5.0s - The boy keeps bouncing on the cushions, pushing up and dropping back with his arms above his head, while the camera tilts up to the oak beams. The ceiling is the busiest surface in the frame: snow pouring across it, the swell running along every aurora ribbon, the sleigh team crossing it, the specks twinkling.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Two moves only: the walk from 0.7s, the tilt up from 3.2s. The camera is the person's eyes; no phone, screen, hand or device in frame after 0.7s.

THE CHILDREN - exactly two, both visible from 1.7s on, no adults, no third child, no pets. Rust-orange and cream fair-isle knitted jumpers with a band of little pine trees across the chest, oatmeal knitted lounge trousers, thick cream knitted socks, as in @Image 1.

SHARPNESS - hold the sharpness, exposure and fine detail of the start image: the panel edges and eggshell sheen of the forest green door, the brass knob and its escutcheon, the skin of the forearm and its thin gold bangle, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet on tile and rug, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed throughout. One continuous take. The picture is visibly in motion in every single frame - at the start, in the middle and in the last second. The boy ends the clip on the sofa, not standing where he began. Sharp focus to the final frame.

BANNED - a still or frozen picture; chimneys without smoke; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that twinkle but never travel; a still ceiling above a moving wall; a projection that appears to move only because the camera moves; light that moves for a moment and then stops; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric or three-dimensional snow; snow in front of the children, the sofa, the stair, the rug or the real tree; snow settling on anyone; any projected shape that leaves the surface it lies on; the boy still standing front-on at the end; children posed or standing still; jellyfish, fish, coral, bubbles or underwater imagery; a room lit entirely blue; the projector unit visible; slow motion; blur or soft focus; any music; a cut; a third child; an adult; subtitles; on-screen text.
````

**Other takes of C05 on disk (2)**

#### Video prompt — `clips/v7_c05_g1.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `1cab2e97-fe1b-4492-a374-2705b79607c8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175814_1cab2e97-fe1b-4492-a374-2705b79607c8.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c05_g1.png` · Higgsfield media `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0`
- image ref 1: `content/video_7_assets/references/v7_c05_r1.png` · Higgsfield media `fdb431f8-16b9-46f4-a377-05dad939cb2e`

````text
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s: a closed forest green two-panel door with a wreath, a hand on the antique brass knob.

THE PICTURE ON THE WALLS IS A CLOSED SET
The start image does not show the room, so read the room ONLY from @Image 1. Everything thrown onto the walls and the ceiling is already drawn in @Image 1. You are not designing a projection - you are making the one in @Image 1 move. Invent nothing. If a thing is not in the list below, it does not exist in this clip.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and the oak beams and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. @Image 1 is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element, and every one of these is moving at the same time:
- THE CHIMNEY SMOKE - every cottage chimney in the village is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - the glowing gold sparks lift off the village chimneys continuously and climb the full height of the wall to join the star field, drifting a little sideways as they rise and fading out near the top, with fresh ones leaving the pots for the whole clip.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the walls and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from where it sits in @Image 1, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail of light streams behind the runners, and the whole team rises and dips a little as it goes. The team is never parked.
- THE CAROUSEL - the great glowing gold fairground carousel above the rooftops TURNS, about a quarter of a full turn every second, its prancing reindeer swinging round with it and rising and falling on their poles as they pass, its scalloped canopy turning with them and its centre pole pulsing brighter and dimmer.
- THE ICE SKATERS - the ring of glowing gold skaters circles the frozen pond one behind another, covering about a third of the ring every second, each one leaning into the curve and laying down a long bright curved arc of light behind it that slowly fades off the ice as a fresh one is drawn.
- THE SHOOTING STARS - they streak across at their different angles, the tail thinning out behind them, and fade; fresh ones set off elsewhere for the whole clip.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the beams, so the density holds even.
- THE CANDY CANES, THE BUNTING, THE ICE CRYSTALS, THE SNOW GLOBES, THE ANGEL GARLAND AND THE BIRDS - all of them travel slowly across the surfaces they are painted on, the candy canes and the big faceted ice crystals turning end over end as they go, the snow globes turning slowly on their own centres, the birds beating their wings as their loose Vs cross.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON AND THE NORTH STAR - these two are the ONLY elements that hold their positions. They stay exactly where they are for the whole clip and only brighten and dim very slightly. Nothing else in the picture is allowed to hold still.
Because the walls and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the timber.

EVERY PROJECTED SHAPE IS PAINT, NOT AN OBJECT. All of it is flat light lying on whatever surface it lands on. It skews and stretches with the slope of that surface, it bends over the beams, it breaks where a wall meets the ceiling. Nothing ever floats free of a surface into the air of the room. There is no snow in the air of the room, none between the camera and the walls, none in front of the children, the sofa, the staircase or the tree, and none landing on the floor or on anyone.

WHAT ELSE HOLDS: the real room. The limewashed plaster walls, the flat cream plaster ceiling and its four heavy square-sawn pale oak beams, the flush skylight, the gallery landing and its slim black balusters, the straight stair on the right, the terracotta saltillo tile floor, the faded Persian rug in rust, cream and terracotta, the cream linen sectional sofa, the chunky reclaimed-wood coffee table, the olive tree in its terracotta pot, the real Christmas tree and its lights, the framing, the colours. The projected picture's outer edge stays put - it never rotates, spins, swings or slides across the room as one sheet. Only the things inside it travel.

@Image 1 is the authority on the room and on every projected shape: its layout, its beams, its stair, its furniture, its two children, and the exact set, style and colour of the projected shapes. It is a photograph - copy its look, never its stillness.

BEATS
0.0-0.7s - The hand turns the antique brass knob and pushes the door away from camera. Behind it the room is ALREADY running: smoke already climbing, snow already falling, the aurora already swelling, the carousel already turning, the reindeer already crossing. The widening gap simply uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on, spreads or grows as the door opens, and nothing glows along the door edge, frame or gap.
0.7-1.7s - The door swings wide and the camera walks through. The snow keeps falling at the same steady rate it already had, down the face of the far wall. It stays on that wall - it does not cross the open air of the room and it does not drift toward the camera.
1.7-3.2s - Inside. THE BOY, the child who is facing the camera at 0.0s, does NOT stay standing there: he turns on the spot away from the lens, runs three or four quick real steps across the rug and LAUNCHES HIMSELF UP ONTO THE CREAM LINEN SECTIONAL SOFA, landing on his knees on the cushions with both arms flying up, laughing. The cushions compress under him and spring back. THE GIRL stays where she is, still seen from behind, still looking up at the wall, shifting her weight and turning her head as she watches.
3.2-5.0s - Without a break THE BOY keeps bouncing on the cushions, pushing up and dropping back with his arms above his head, while the camera keeps walking and TILTS UP until the oak beams fill the top of frame. The ceiling is the busiest surface in the clip: snow pouring across it, the swell running along every aurora ribbon, the sleigh team crossing it, the ice crystals turning, the specks twinkling.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the walk from 0.7s, the tilt up from 3.2s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes - no phone, screen, hand or device in frame after 0.7s.

THE CHILDREN - exactly two, both visible from 1.7s on, no adults, no third child, no pets. Warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks, as in @Image 1. They never stand still and never pose. THE BOY is in continuous motion from 1.7s to the last frame.

SHARPNESS - hold the sharpness, exposure and fine detail of the start image: the panel edges and eggshell sheen of the forest green door, the antique brass knob and its escutcheon plate, the skin of the forearm and the thin gold bangle, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet on tile and rug, a body landing on sofa cushions, children laughing, quiet room tone. (no BGM). No music, no song, no score, no instruments, no bells used as music. No subtitles.

BANNED - a frozen or still picture; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a carousel that does not turn; skaters that do not circle; flakes that only twinkle without travelling; a still ceiling above moving walls; a shape that stays in the same place on the plaster when the list says it travels; a projection that appears to move only because the camera moves; the boy still standing front-on in the same spot at the end; children standing still or posed; snow, snowflakes or any particles falling through the open air of the room; volumetric or three-dimensional snow; anything drifting between the camera and the walls; snow passing in front of the children, the sofa, the staircase, the rug or the real tree; snow settling on the floor, the furniture or anyone's hair or shoulders; any projected shape that appears to leave the surface it is painted on; any projected shape that is not on the list above; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; any music; slow motion; blur or soft focus; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v7_c05_g3.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `7cf7c73e-a010-45e6-abc2-4f98caf88ee9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_205021_7cf7c73e-a010-45e6-abc2-4f98caf88ee9.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c05_g3.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c05_g1.png` · Higgsfield media `ff4a3535-a332-4cc2-96b3-03b0dabb3cd0`
- image ref 1: `content/video_7_assets/references/v7_c05_r1.png` · Higgsfield media `fdb431f8-16b9-46f4-a377-05dad939cb2e`

````text
TASK: image-to-video, 5 seconds, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed forest green two-panel door with a wreath, a hand on the antique brass knob. @Image 1 is the room behind that door and the authority on its layout, beams, stair, furniture, two children, colours, and on the exact set and style of every projected shape.

THE MOVING PICTURE IS THE SUBJECT OF THIS CLIP. The walls and the ceiling are a cinema screen with a film playing on them. The plaster and the pale oak beams hold perfectly still; the picture lying on them is running for all five seconds. @Image 1 is one paused frame of that film, and at 0.0s it un-pauses.

Four things carry the motion, and all four are running from the first frame to the last:

SMOKE. Every cottage chimney in the little village is smoking hard enough to see plainly. Each plume boils up out of its pot, leans to the right, climbs a full cottage-roof height every second and widens and thins away, while the next plume is already forming behind it.

THE AURORA. Each ribbon behaves like a long silk curtain hung in a slow draught: a swell travels along the ribbon from one end to the other, about a third of its length every second, brightening and thinning the ribbon as it passes and combing its lower fringe into new folds. The ribbon's arc stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its team of reindeer are FLYING. They travel across the ceiling, about a fifth of the ceiling's width every second, so that by 5.0s the team has crossed most of the way. Legs gallop, heads nod, the sleigh rocks behind them, the long tapering trail of light streams off the runners, and the whole team rises and dips as it goes. The team is never parked.

THE SNOW. Every snowflake and point of light drifts downward and slightly sideways, about a quarter of the wall's height every second, the way snow falls past a window at night, each one turning slowly on its own centre and breathing brighter and dimmer on its own timing. One that reaches the floor line fades out there as a fresh one fades in high near the beams, so the density never thins.

Everything else in the picture travels as well: the gold sparks lifting off the chimneys and climbing to the star field, the great fairground carousel turning with its reindeer rising and falling on their poles, the skaters circling the frozen pond and laying bright arcs behind them, the shooting stars streaking and fading, the candy canes and faceted ice crystals tumbling end over end, the snow globes turning, the birds beating across in loose Vs. Only the moon and the north star hold their positions; those two simply breathe brighter and dimmer.

The walls and the ceiling are lit by ONE projector and are therefore ONE picture: whatever the wall is doing, the ceiling is doing at the same instant and at the same speed. The picture's outer boundary is anchored — it never rotates, spins, swings or slides across the room as one sheet; only the things inside it travel. All of it is flat light lying on the surfaces: it skews with their slope, bends over the beams and breaks where wall meets ceiling. Nothing ever leaves a surface — no snow in the open air of the room, none between camera and wall, none in front of the children, the sofa, the stair or the real tree, none settling on the floor or on anyone.

BEATS
0.0-0.7s — The hand turns the brass knob and pushes the door away from camera. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION; the widening gap only uncovers more of something that was already going — a film that was already playing and two kids who were already running before the door opened. Nothing ignites, switches on or spreads as the door opens. The door edge and frame stay plain painted wood — no glowing strip, no coloured fringe, no bright seam in the gap.
0.7-3.2s — The camera walks through and on across the rug. BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. The door does not open on two kids standing stunned, frozen or waiting to be filmed who then start to move; it opens on two kids already in the middle of doing something, and neither of them is ever still. THE BOY, the child nearer the camera, is already turning away from the lens and pushing off his front foot as the gap widens; he runs three or four quick real steps and LAUNCHES HIMSELF UP ONTO the cream linen sectional sofa, landing on his knees on the cushions with both arms flying up, laughing; the cushions compress under him and spring back. THE GIRL is already mid-stride as well; she runs on across the rug without breaking step, tips her head right back to look straight up at the beams and throws one arm up pointing at the flying sleigh overhead, mouth open, delighted. Both runs are ordinary excited-kid running at real speed and real weight: feet landing, knees bending, arms swinging, hair and jumpers moving with them.
3.2-5.0s — The boy keeps bouncing on the cushions, pushing up and dropping back with his arms above his head, while THE GIRL keeps moving across the room and keeps her arm up pointing at the ceiling, still going on the last frame, and the camera tilts up to the oak beams. The ceiling is the busiest surface in the frame: snow pouring across it, the swell running along every aurora ribbon, the sleigh team crossing it, the specks twinkling.

CAMERA — eye height, normal wide-angle phone lens, natural handheld bounce. Two moves only: the walk from 0.7s, the tilt up from 3.2s. The camera is the person's eyes; no phone, screen, hand or device in frame after 0.7s.

THE CHILDREN — exactly two, both visible from 1.7s on, no adults, no third child, no pets. Rust-orange and cream fair-isle knitted jumpers with a band of little pine trees across the chest, oatmeal knitted lounge trousers, thick cream knitted socks, as in @Image 1.

SHARPNESS — hold the sharpness, exposure and fine detail of the start image: the panel edges and eggshell sheen of the forest green door, the brass knob and its escutcheon, the skin of the forearm and its thin gold bangle, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO — dry documentary sound only: the handle, the door swinging, running feet on tile and rug, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS — real-time motion at normal speed throughout. One continuous take. The picture is visibly in motion in every single frame — at the start, in the middle and in the last second. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to 5.0s: the boy ends the clip bouncing on the sofa, not standing where he began, and the girl ends it still moving and still pointing up at the beams. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED — a still or frozen picture; chimneys without smoke; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that twinkle but never travel; a still ceiling above a moving wall; a projection that appears to move only because the camera moves; light that moves for a moment and then stops; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric or three-dimensional snow; snow in front of the children, the sofa, the stair, the rug or the real tree; snow settling on anyone; any projected shape that leaves the surface it lies on; the boy still standing front-on at the end; either child standing still, frozen, stunned, startled, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head or shifts her weight while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before 5.0s; jellyfish, fish, coral, bubbles or underwater imagery; a room lit entirely blue; the projector unit visible; slow motion; blur or soft focus; any music; a cut; a third child; an adult; subtitles; on-screen text.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v7_c06_g1.png` → `clips/v7_c06_g1.mp4`

#### Image prompt — `starting_frames/v7_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `6effc3a5-7218-453b-a756-9e97c76cf9ef`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_132005_6effc3a5-7218-453b-a756-9e97c76cf9ef.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `0a845da6-2607-46cc-a595-4fee4b17d6a9`
- @Image 2: `references/house_bedroom_rafters.png` · Higgsfield media `c1ea3b08-e710-4bda-9d33-4dd99b0e3012`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with her family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its truss, its walls, its window and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a girl of about seven with shoulder-length light brown hair, fully dressed for winter in a warm rust-orange and cream fair-isle knitted Christmas jumper with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. She is standing up on top of the bed, knees bent and both arms raised out to her sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge. Wholesome family Christmas scene, a child at home with her family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom under a high vaulted roof, the ceiling two sloping planes of smooth cream plaster meeting at a ridge that runs away from the camera, crossed by heavy reclaimed oak rafters - a king-post truss near the front, its two rafters meeting at the ridge above a horizontal collar, and four or five more rafters marching down the right-hand slope onto a horizontal oak wall plate - with small recessed downlights set into the plaster between them, and a big black wrought-iron ring chandelier of two concentric rings carrying a row of plain candle bulbs hanging on a black rod from the ridge; a tall gable end wall on the left with a triangular-headed window above a pair of dark-framed glazed doors with side lights and long taupe linen curtains; a horizontal grey-brown plank accent wall behind the bed with three small framed prints in thin dark frames and a black wall sconce beside them; a low reclaimed-wood platform bed with a wide plank headboard, two nightstands with table lamps, wide pale oak plank floorboards and a large flat-weave oat rug. Copy the proportions, the rafter spacing, the king-post truss, the ridge, the ring chandelier and the gable window from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the gable window and the glazed doors show a dark blue snow-covered night outside, there is no daylight anywhere in the room, the ring chandelier and every downlight and table lamp are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a rust-orange wool quilt, a cream cable-knit throw and ticking-stripe pillows, a cream knitted stocking hangs from the rafter above the headboard, a warm fairy-light garland is strung around the gable window, a small lit Christmas tree stands on the floor beside the bed, and a small evergreen wreath with a terracotta bow hangs on the plank wall. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both sloping plaster ceiling planes, the heavy oak rafters and the king-post truss, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and turning slowly above the rooftops one enormous glowing gold fairground carousel of prancing reindeer, its scalloped canopy strung with tiny bells and its centre pole a bright column of light, and on the frozen pond below it a wide ring of glowing gold ice skaters circling one behind another, each one trailing a long bright curved arc of light across the ice; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the gable window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth; and beyond even that, great slow-turning glowing gold snow globes the size of a car drifting across the upper wall, each one holding its own tiny lit village inside it, a long glowing gold paper-chain garland of angels linked hand to hand curving right across the ceiling from one corner to the other, whole flights of glowing gold robins and doves crossing in loose Vs at three different depths, glowing gold ribbons of ivy and holly with bright red berries winding up every corner of the room, and a slow steady rise of glowing gold sparks lifting off the village chimneys and climbing the full height of the wall to join the star field, so every surface is so full that the eye cannot rest on any single thing. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the cream plaster and the oak rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, and every heavy reclaimed oak rafter, the king-post truss and the ridge, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the truss break the light with their own hard shadow lines where they stand proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as two sloping plaster planes meeting at a ridge and crossed by heavy oak rafters, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the flat-weave rug, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Her knitted jumper catches that spill so the jumper and the mid-bounce pose read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v7_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `ab635356-a3f3-4bd2-88e7-c7f20da772ad`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175814_ab635356-a3f3-4bd2-88e7-c7f20da772ad.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c06_g1.png` · Higgsfield media `6effc3a5-7218-453b-a756-9e97c76cf9ef`

````text
SUMMARY: a girl bounces on her bed in a vaulted rafter Christmas bedroom at night while a projected snow-village picture is PLAYING across the wall behind the bed and both sloping plaster ceiling planes, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, its ceiling of two sloping planes of smooth cream plaster meeting at a ridge that runs away from the camera crossed by heavy reclaimed oak rafters with a king-post truss near the front, the big black wrought-iron ring chandelier of two concentric rings, the tall gable end wall on the left with its triangular-headed window above a pair of dark-framed glazed doors, the horizontal grey-brown plank accent wall behind the bed, the low reclaimed-wood platform bed with its wide plank headboard and its rust-orange wool quilt, the wide pale oak plank floorboards, the large flat-weave oat rug, the Christmas dressing, THE GIRL and the colour.

SUBJECTS:
THE GIRL - exactly one child, a girl of about seven with shoulder-length light brown hair, in a warm rust-orange and cream fair-isle knitted Christmas jumper with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks, standing on the bed with her arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall and both sloping plaster ceiling planes. Everything glowing on the plaster and the oak is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a snow village low along the wall with gabled cottages with lit windows, a church steeple, snow-laden pine trees and a frozen pond, plumes above the chimneys, an enormous glowing gold fairground carousel of prancing reindeer turning above the rooftops, a ring of glowing gold ice skaters circling the frozen pond below it, wide aurora ribbons in warm gold, emerald green and deep rose lying along both ceiling slopes and kinking at the ridge, Santa's sleigh drawn by a team of eight flying reindeer keystoned across the slope, a big soft ivory moon high on the slope above the gable window, one big brilliant north star near the ridge, a dense field of warm gold stars of many sizes, long-tailed shooting stars, glowing gold candy canes, bunting, big faceted ice crystals, slow-turning snow globes, a paper-chain garland of angels, loose Vs of gold robins and doves, and a heavy fall of small glowing gold and cream six-point snowflakes and points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and the oak and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE GIRL and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element, and every one of these is moving at the same time:
- THE CHIMNEY SMOKE - every cottage chimney in the village is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - the glowing gold sparks lift off the village chimneys continuously and climb the full height of the wall to join the star field, drifting a little sideways as they rise and fading out near the top, with fresh ones leaving the pots for the whole clip.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on both ceiling slopes is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from where it sits in the start image, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail of light streams behind the runners, and the whole team rises and dips a little as it goes. The team is never parked.
- THE CAROUSEL - the great glowing gold fairground carousel above the rooftops TURNS, about a quarter of a full turn every second, its prancing reindeer swinging round with it and rising and falling on their poles as they pass, its scalloped canopy turning with them and its centre pole pulsing brighter and dimmer.
- THE ICE SKATERS - the ring of glowing gold skaters circles the frozen pond one behind another, covering about a third of the ring every second, each one leaning into the curve and laying down a long bright curved arc of light behind it that slowly fades off the ice as a fresh one is drawn.
- THE SHOOTING STARS - they streak across at their different angles, the tail thinning out behind them, and fade; fresh ones set off elsewhere for the whole clip.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts, breathes brighter and dimmer on its own timing, and cycles slowly through gold, cream and soft rose. One that reaches the skirting board fades out there while a fresh one fades in high near the ridge, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE CANDY CANES, THE BUNTING, THE ICE CRYSTALS, THE SNOW GLOBES, THE ANGEL GARLAND AND THE BIRDS - all of them travel slowly across the surfaces they are painted on, the candy canes and the big faceted ice crystals turning end over end as they go, the snow globes turning slowly on their own centres, the birds beating their wings as their loose Vs cross.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON AND THE NORTH STAR - these two are the ONLY elements that hold their positions. They stay exactly where they are for the whole clip and only brighten and dim very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and both ceiling slopes are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the oak.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the wall and the sloping plaster ceiling so the projected picture fills most of the frame and THE GIRL is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the rafters and the ridge sliding up out of the top of frame, until the bed and THE GIRL fill the lower half. THE GIRL bends her knees and pushes off the mattress; both feet leave the quilt, arms swinging up over her head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE GIRL lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; she is bouncing continuously and never stops. The wall and both ceiling slopes stay in frame throughout, the aurora rippling along them and the sleigh still flying across.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a girl laughing. (no BGM). No music, no song, no score, no instruments, no bells used as music. No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real girl jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN from the top of the wall, then a small slow pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a carousel that does not turn; skaters that do not circle; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; a projection that appears to move only because the camera moves; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v7_c07_g1.png` → `clips/v7_c07_g1.mp4`

#### Image prompt — `starting_frames/v7_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `49a02dae-3ad9-4cfa-9387-baeeb98bab32`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_132315_49a02dae-3ad9-4cfa-9387-baeeb98bab32.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `c9a6740d-383b-4829-a7b9-f7a3c079c03f`
- @Image 2: `references/house_great_room_beams.png` · Higgsfield media `e402f616-c876-4e01-bb5a-60774babf36a`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its beams, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long wavy light brown hair, the boy is about five with short sandy brown hair. Both are fully dressed for winter in warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height living space whose ceiling is flat smooth cream plaster crossed by four heavy square-sawn pale oak beams running left to right at even spacing, each one a real chunky timber with square corners and visible grain where it lands on the wall, and one large rectangular flush skylight set into the plaster between the first two beams; a first-floor gallery landing crossing the left and centre of the room at mid height, its railing made of slim black metal balusters under a black top rail with a plain cream fascia below it; a straight run of stairs on the right coming down towards the camera with pale oak treads and the same slim black baluster railing; tall black-framed windows filling the right-hand wall to full height; pale limewashed plaster walls; and underneath the gallery an open kitchen with a white marble waterfall island, open shelving with pottery and a full-height pale oak cabinet run. Terracotta saltillo tile floor laid in a square pattern, a large faded Persian rug in rust, cream and terracotta, a big cream linen sectional sofa, a chunky rustic reclaimed-wood low coffee table, and a large olive tree in a terracotta pot in the right foreground. The ceiling of this room is FLAT - there is no vault, no ridge and no sloping ceiling plane anywhere in it. Copy the proportions, the beam spacing, the skylight, the railings and the stair from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall windows show a dark blue snow-covered night outside, there is no daylight and no sunlight anywhere in the room, every lamp, pendant and downlight in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall slim real Christmas tree standing in front of the tall windows with warm white lights and terracotta and antique copper ornaments and wrapped gifts underneath, a thick evergreen garland with pine cones and terracotta ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a bowl of terracotta and antique copper ornaments on the coffee table. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every limewashed plaster wall, the whole flat plaster ceiling and its four heavy square oak beams, and the fascia and railing of the gallery landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and turning slowly above the rooftops one enormous glowing gold fairground carousel of prancing reindeer, its scalloped canopy strung with tiny bells and its centre pole a bright column of light, and on the frozen pond below it a wide ring of glowing gold ice skaters circling one behind another, each one trailing a long bright curved arc of light across the ice; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling plane and run with the direction of the oak beams instead of hanging as vertical curtains, and visibly break and step where each heavy beam crosses them; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the ceiling plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the wall above the gallery landing; one big brilliant north star high beside the skylight with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth; and beyond even that, great slow-turning glowing gold snow globes the size of a car drifting across the upper wall, each one holding its own tiny lit village inside it, a long glowing gold paper-chain garland of angels linked hand to hand curving right across the ceiling from one corner to the other, whole flights of glowing gold robins and doves crossing in loose Vs at three different depths, glowing gold ribbons of ivy and holly with bright red berries winding up every corner of the room, and a slow steady rise of glowing gold sparks lifting off the village chimneys and climbing the full height of the wall to join the star field, so every surface is so full that the eye cannot rest on any single thing. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the oak beams. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every heavy square oak beam with its grain and its square corners, all stay clearly visible THROUGH the coloured light, and each beam breaks the light with its own hard shadow line where it stands proud of the plaster. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the ceiling plane and stepping where it crosses each beam. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling crossed by four heavy oak beams with a skylight set between them, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The terracotta tile floor, the Persian rug, the cream sectional sofa, the olive tree, the Christmas tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v7_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `705e9998-0bd0-4b0a-8d81-4cf223d9f99f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_175814_705e9998-0bd0-4b0a-8d81-4cf223d9f99f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v7_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_7_assets/starting_frames/v7_c07_g1.png` · Higgsfield media `49a02dae-3ad9-4cfa-9387-baeeb98bab32`

````text
Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected snow-village picture is PLAYING across the walls and the whole flat cream plaster ceiling and its four heavy square oak beams, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the flat cream plaster ceiling crossed by four heavy square-sawn pale oak beams with a flush rectangular skylight set between them, the first-floor gallery landing with its slim black metal balusters under a black top rail, the straight run of pale oak stairs on the right, the tall black-framed windows filling the right-hand wall with snow outside, the pale limewashed plaster walls, the open kitchen with its white marble waterfall island, the terracotta saltillo tile floor, the large faded Persian rug in rust, cream and terracotta, the big cream linen sectional sofa, the chunky rustic reclaimed-wood low coffee table, the large olive tree in its terracotta pot, the lit Christmas tree with its presents, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with short sandy brown hair, on the rug at the front left, back to camera, facing the wall, turning on the spot with his arms out.
THE OTHER CHILD - a girl of about eight with long wavy light brown hair, standing up on the cream linen sofa cushions, back to camera, with both arms raised toward the wall, bouncing on the spot.
Both in warm rust-orange and cream fair-isle knitted Christmas jumpers with a band of little pine trees across the chest, matching oatmeal knitted lounge trousers and thick cream knitted socks. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the walls and the whole ceiling. Everything glowing on the plaster and the oak is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a snow village low along the walls with gabled cottages with lit windows, a church steeple, snow-laden pine trees and a frozen pond, plumes above the chimneys, an enormous glowing gold fairground carousel of prancing reindeer turning above the rooftops, a ring of glowing gold ice skaters circling the frozen pond below it, wide aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls and lying along the ceiling with the direction of the oak beams, Santa's sleigh drawn by a team of eight flying reindeer keystoned across the ceiling, a big soft ivory moon high on the wall above the gallery landing, one big brilliant north star beside the skylight, a dense field of warm gold stars of many sizes, long-tailed shooting stars, glowing gold candy canes, bunting, big faceted ice crystals, slow-turning snow globes, a paper-chain garland of angels, loose Vs of gold robins and doves, and a heavy fall of small glowing gold and cream six-point snowflakes and points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and the oak and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element, and every one of these is moving at the same time:
- THE CHIMNEY SMOKE - every cottage chimney in the village is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - the glowing gold sparks lift off the village chimneys continuously and climb the full height of the wall to join the star field, drifting a little sideways as they rise and fading out near the top, with fresh ones leaving the pots for the whole clip.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the walls and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from where it sits in the start image, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail of light streams behind the runners, and the whole team rises and dips a little as it goes. The team is never parked.
- THE CAROUSEL - the great glowing gold fairground carousel above the rooftops TURNS, about a quarter of a full turn every second, its prancing reindeer swinging round with it and rising and falling on their poles as they pass, its scalloped canopy turning with them and its centre pole pulsing brighter and dimmer.
- THE ICE SKATERS - the ring of glowing gold skaters circles the frozen pond one behind another, covering about a third of the ring every second, each one leaning into the curve and laying down a long bright curved arc of light behind it that slowly fades off the ice as a fresh one is drawn.
- THE SHOOTING STARS - they streak across at their different angles, the tail thinning out behind them, and fade; fresh ones set off elsewhere for the whole clip.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the beams, so the density holds even.
- THE CANDY CANES, THE BUNTING, THE ICE CRYSTALS, THE SNOW GLOBES, THE ANGEL GARLAND AND THE BIRDS - all of them travel slowly across the surfaces they are painted on, the candy canes and the big faceted ice crystals turning end over end as they go, the snow globes turning slowly on their own centres, the birds beating their wings as their loose Vs cross.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON AND THE NORTH STAR - these two are the ONLY elements that hold their positions. They stay exactly where they are for the whole clip and only brighten and dim very slightly. Nothing else in the picture is allowed to hold still.
Because the walls and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the oak.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the beamed ceiling fills the upper half of the frame, the aurora rippling along it and the sleigh team still flying across it. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, socked feet on a rug. (no BGM). No music, no song, no score, no instruments, no bells used as music. No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a carousel that does not turn; skaters that do not circle; flakes that only twinkle without travelling; a still ceiling above moving walls; the whole picture rotating, spinning, sweeping or sliding as one sheet; a projection that appears to move only because the camera moves; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.
````
