# Video 15 - image archive

**Animation status (2026-09-22):** All seven requested shots, C01-C07, have local video take 1 and board players for review. Hooks use 1080p; B-roll uses 720p; each clip is 4 or 5 seconds as archived below. One generation per shot; image and earlier hook takes retained. Sampled review issues are recorded with each clip.

**Current status (2026-09-22):** C01 hook plus 7 B-roll images saved and on the board for review. All images await Daniel's review.

**Settings:** Higgsfield `gpt_image_2_5`; variant `sunburst`; resolution `2k`; quality `medium`; aspect_ratio `9:16`; count `1` per image. Reference role image is mapped by the backend to image_references.

## Reusable blocks
Exact camera, geometry, product and sharpness wording reopened from video 14. Full submitted prompts below include every reused block verbatim except the documented changes. New house finishes, hands, children, pyjamas, projection story and surface mapping; C03/C04 explicitly enlarged to match the C02 product scale. One generation per image; no self-rerolls.


## C02 - starting frame

**Frame:** `starting_frames/v15_c02_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "bbfc652c-e9eb-4430-9b53-610b56917312"}, {"role": "image", "value": "2597b25d-60d1-4060-9602-32b0ee26c2f7"}]}`
**Job ID:** 87bb29f6-bdc9-4513-9a89-9babf4f67faa
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 7044351 bytes; SHA-256 fb77903b32d54d442a47fc4e70eb5d1f5f37f400f0b05371e61b3fb79d1d340f. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c02_g1.png` - bbfc652c-e9eb-4430-9b53-610b56917312 - role image (backend image_references)
2. `../../product_images/box_festive_green_g2.png` - 2597b25d-60d1-4060-9602-32b0ee26c2f7 - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C02 - starting frame image take 1 - changed: New hands and sleeve, table and house finishes. Theme: French country · Nutcracker Christmas.

### Image prompt
```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 35, with fair skin with light freckles and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a sage-green cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a honey-oak farmhouse dining table with broad straight grain, a satin-matte finish and a substantial square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive French-country dining room with warm ivory plaster walls, pale oak cabinets, an antique brass mirror, a carved limestone fireplace with red stockings and a Christmas tree dressed with burgundy bows and gold glass ornaments. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** One generated take; awaiting Daniel's review.

### Video prompt - take 1
**Clip:** `clips/v15_c02_g1.mp4`
**Job ID:** `90706e24-d8e5-4120-92c7-a2dff79a5d02`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `87bb29f6-bdc9-4513-9a89-9babf4f67faa` = `starting_frames/v15_c02_g1.png`
- image `87bb29f6-bdc9-4513-9a89-9babf4f67faa` = `starting_frames/v15_c02_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 1967151 bytes.
**Upscale:** `clips/upscaled/v15_c02_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a honey-oak farmhouse dining table with broad straight grain, a satin-matte finish and a substantial square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a sage-green cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a honey-oak farmhouse dining table with broad straight grain, a satin-matte finish and a substantial square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive French-country dining room with warm ivory plaster walls, pale oak cabinets, an antique brass mirror, a carved limestone fireplace with red stockings and a Christmas tree dressed with burgundy bows and gold glass ornaments. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the pale cream terrazzo dining table with small terracotta and warm-white stone chips, a satin-matte surface and a square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
```


## C03 - starting frame

**Frame:** `starting_frames/v15_c03_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "4b0ce2fa-f22e-4fdc-a781-0a2f43789130"}, {"role": "image", "value": "87bb29f6-bdc9-4513-9a89-9babf4f67faa"}]}`
**Job ID:** 6521ec22-9695-4f86-82fa-fa33156e0a5d
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 5600372 bytes; SHA-256 1d7f38ba4d8cf9629466b4d8424896369a1903b2c9bf748459af0970e4e6c69b. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c03_g1.png` - 4b0ce2fa-f22e-4fdc-a781-0a2f43789130 - role image (backend image_references)
2. `starting_frames/v15_c02_g1.png` - 87bb29f6-bdc9-4513-9a89-9babf4f67faa - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C03 - starting frame image take 1 - changed: New hand/sleeve, countertop and kitchen finishes; enlarged full projector to approximately 42 percent of frame height and dome to approximately 46 percent of frame width, replacing the older small-product scale wording. Second reference changed to this video C02 for hand, photographic-look and product-scale continuity. Theme: French country · Nutcracker Christmas.

### Image prompt
```text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with fair skin with light freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a sage-green cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same sage-green cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C02 and owns the new woman's hands, sweater, photographic look and full-size carton-to-projector scale; the projector should plausibly fill that carton when unpacked; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** Requested larger product scale to match C02; compare the apparent product size across C02/C03/C04. Black mesh top, separate stand and hand action retained in the prompt. One take, no reroll.

### Video prompt - take 1
**Clip:** `clips/v15_c03_g1.mp4`
**Job ID:** `f7853fb5-540d-4529-9274-ab8549d245d6`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `6521ec22-9695-4f86-82fa-fa33156e0a5d` = `starting_frames/v15_c03_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 1945124 bytes.
**Upscale:** `clips/upscaled/v15_c03_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in sage-green cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy; behind it soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the dark charcoal honed granite counter with very fine silver-grey mineral flecks and a straight eased edge, matte rather than mirror-polished.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
```


## C04 - starting frame

**Frame:** `starting_frames/v15_c04_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "e243effc-2c21-4bed-9551-e592483315ca"}, {"role": "image", "value": "6521ec22-9695-4f86-82fa-fa33156e0a5d"}]}`
**Job ID:** 93ade77e-7356-4b70-afc6-976b87529bde
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 5636874 bytes; SHA-256 64345aa2dbdfa6e4b7d700d0e548052b92b34085fa8d61c0b22469915ffaebf4. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c04_g1.png` - e243effc-2c21-4bed-9551-e592483315ca - role image (backend image_references)
2. `starting_frames/v15_c03_g1.png` - 6521ec22-9695-4f86-82fa-fa33156e0a5d - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C04 - starting frame image take 1 - changed: New hand/sleeve, countertop and kitchen finishes; enlarged full projector to approximately 42 percent of frame height and dome to approximately 46 percent of frame width, replacing the older small-product scale wording. Second reference changed to this video C03 for the enlarged product, hands and kitchen continuity. Theme: French country · Nutcracker Christmas.

### Image prompt
```text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with fair skin with light freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a sage-green cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C03 and owns the enlarged product's physical dimensions relative to the hands, exact product identity, kitchen finishes, hands, sweater and photographic look; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** Requested larger product scale to match C02; compare the apparent product size across C02/C03/C04. Black mesh top, separate stand and hand action retained in the prompt. One take, no reroll.

### Video prompt - take 1
**Clip:** `clips/v15_c04_g1.mp4`
**Job ID:** `28fd0fca-2a1f-48b1-80ca-761e96aed71f`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `93ade77e-7356-4b70-afc6-976b87529bde` = `starting_frames/v15_c04_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 1220413 bytes.
**Upscale:** `clips/upscaled/v15_c04_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand PLUGS a white USB-C connector INTO the small dark socket in the bottom rim of the projector's white dome, and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a sage-green cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same sage-green cable-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy; behind it soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the stone and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the stone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
```


## C05 - starting frame

**Frame:** `starting_frames/v15_c05_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "6a0df249-6245-439e-a380-e9bbdf6dc580"}, {"role": "image", "value": "87bb29f6-bdc9-4513-9a89-9babf4f67faa"}]}`
**Job ID:** b3101160-afff-496e-8980-229304195285
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 5451001 bytes; SHA-256 f52fe080232815da7c98c319d2ab317c21bde4299437994c8b0c315d232cb4bc. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c05_g1.png` - 6a0df249-6245-439e-a380-e9bbdf6dc580 - role image (backend image_references)
2. `starting_frames/v15_c02_g1.png` - 87bb29f6-bdc9-4513-9a89-9babf4f67faa - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C05 - starting frame image take 1 - changed: New door, hand tone and sleeve. Second reference changed to this video C02 for hand and sleeve look. Theme: French country · Nutcracker Christmas.

### Image prompt
```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the sage-green cable-knit wool sleeve and no jewellery, with fair skin with light freckles, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a muted sage-green painted four-panel solid wood door with two tall upper panels and two shorter lower panels, a satin finish and crisp mouldings, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the sage-green paint reads clearly as muted green, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** Continuity note: the generated sleeve is cream rather than the requested sage-green used in C02/C03. Door is closed. One take retained for Daniel's review; no reroll.

### Video prompt - take 1
**Clip:** `clips/v15_c05_g1.mp4`
**Job ID:** `777cba5a-8326-46af-a24e-049df166e251`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 5, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `b3101160-afff-496e-8980-229304195285` = `starting_frames/v15_c05_g1.png`
- image `7a28dda2-126c-456b-b9ba-f29fd781f87a` = `unresolved on this drive`
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; audio stream aac; 3647189 bytes.
**Upscale:** `clips/upscaled/v15_c05_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Video 1. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high coffered ceiling meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

PRIMARY REQUIREMENT: this is a continuously ANIMATED Christmas movie projected on real walls and ceiling. The sleigh travels, reindeer gallop and smoke actively billows from every illustrated house chimney. Most other existing illustrated subjects move too. A static decorative image behind moving children is a failed result. Apply the detailed PROJECTED FILM ACTION below at every instant; retain the existing camera and child choreography.

CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the coffered ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the existing illustrated villagers and toy/train procession travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a muted sage-green painted four-panel solid wood door with two tall upper panels and two shorter lower panels, a satin finish and crisp mouldings fully closed with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, coffered ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED FILM ACTION - THE MAIN SUBJECT IS THE MOVING CHRISTMAS ARTWORK. Animate the existing illustrated objects themselves, not just the camera, children, brightness or glitter. At every moment MOST visible illustrated subjects are visibly changing position or shape independently. Keep the physical room and the projection's overall footprint fixed.
SLEIGH AND REINDEER: the existing sleigh team travels along the plaster ceiling at roughly one fifth of the visible ceiling width per second, crossing architectural seams and passing the fixed central star. Every reindeer continuously cycles its legs in a running gallop; heads bob, harnesses flex and the sleigh rocks behind them. The team must move relative to the stationary beams, star and ceiling corners in every half-second interval. Do not rotate the ceiling picture as a single disc.
CHIMNEYS: each visible illustrated house chimney continuously emits a clearly visible cream-grey animated smoke plume, contained INSIDE the flat wall illustration. New curls emerge every 0.25 second, rise one roof-height per second, expand and deform, then dissolve as more curls follow. Several different plumes must be visibly evolving at once; none may remain a frozen drawn squiggle. These are moving pixels on the wall, never real smoke entering the room.
VILLAGE: the existing illustrated figures walk along the wall, take full alternating steps and swing arms. Gift carriers lift and pass the existing parcels. Existing animal drawings walk with articulating legs, toy processions advance and wheels turn where present. Existing house-window light flickers independently. Buildings stay fixed so the moving figures and chimney smoke read clearly.
RIBBONS, GARLANDS AND BELLS: successive waves visibly deform each existing ribbon along its length while bright gold crests travel from the central star toward the walls, covering half a ribbon length per second. Existing bell drawings swing left-right-left roughly once per second with independently swinging clappers. Existing ornament drawings rotate within the projected picture. Do not leave the wall decorations frozen while only the ceiling sleigh moves.
SNOW AND STARS: existing snowflake drawings translate along the ceiling planes and down the walls continuously, at different speeds. Ceiling snow stays flush to ceiling plaster and follows its slope, never drops into the air. Stars twinkle independently while existing shooting-star streaks traverse the surface. Nothing moves over the boy or children, furniture, floor or in the open room.
All these actions run simultaneously from the first visible projected frame until the final frame, at normal playback speed, without a fade-in, opening pause, final freeze or settling back into the reference image. The supplied visual references fix architecture, identities and artwork appearance ONLY; replace their static or weak artwork motion with the explicit motion above. The original full projection is already on at frame zero or behind the closed door. All animated pixels bend at actual wall and ceiling seams, remain flat on those surfaces and are occluded by real foreground objects.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the actual room surfaces. The broad flat central ceiling and all four smooth ceiling transitions remain visible. The sleigh trail and garlands run across the flat panel then curve and progressively stretch around the rounded coves before continuing vertically down the walls; no invented ridge or angular fold interrupts the coves. At the chimney breast the picture breaks sharply around the two projecting vertical corners, carrying across every brick face with crisp mortar-line texture and tiny mortar shadows. The arched doorway and window reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole coffered ceiling and over every ceiling seam, right into all four corners. No bare un-animated patch of plaster and no bare ceiling detail anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera crosses the single thin doorway threshold directly into the living room, already beside its sectional and rug shown in the reference without passing through any intervening space, while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the existing illustrated villagers and toy/train procession and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl with East Asian features, light warm skin and long straight dark hair  runs a broad curving path across the rug and alongside the sofa; the boy with fair freckled skin and short tousled copper-red hair follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole coffered ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; a ribbon that sits still; a parked sleigh; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, chimney surface and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and ceiling details. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.

ROOM AND IDENTITY - a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about eight with fair freckled skin and wavy auburn hair in two low braids; a boy of about six with fair freckled skin and short tousled copper-red hair. Both fully dressed in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Preserve these identities and architecture from @Video 1.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing toy train rolls steadily through the projected village with its wheels turning; toy-shop elves walk and pass gifts; nutcrackers move their arms and nod. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
```


## C05 F2 - room reference

**Reference:** `references/v15_c05_r1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "dda4701e-8d9d-4351-99f8-60bb9093cf68"}, {"role": "image", "value": "1c500339-2855-45b6-bd9b-4c3633b5a272"}]}`
**Job ID:** b711e297-8ca5-4199-aa1d-dcd291687645
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 7582624 bytes; SHA-256 cd5c0e7b7da3147c42ef544cc1a10e54f30fc9fd4fe3d7dd6d33ed3378b1b2bd. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/references/v11_c05_r1.png` - dda4701e-8d9d-4351-99f8-60bb9093cf68 - role image (backend image_references)
2. `../video_9_assets/references/v9_c05_r4.png` - 1c500339-2855-45b6-bd9b-4c3633b5a272 - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C05 F2 - room reference image take 1 - changed: New children, cotton Christmas pyjamas, house/bedroom architecture, projected Christmas story and geometry-specific surface mapping; remaining camera, pose, projection contrast and sharpness blocks retained. Theme: French country · Nutcracker Christmas.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about six with fair freckled skin and short tousled copper-red hair; the girl is of about eight with fair freckled skin and wavy auburn hair in two low braids. Both children are fully dressed for winter in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. Seen from the doorway; the new a muted sage-green painted four-panel solid wood door with two tall upper panels and two shorter lower panels, a satin finish and crisp mouldings is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The six deep ceiling coffers remain visibly three-dimensional. The sleigh, ribbons and garlands split at every plaster beam edge, continue down the recessed vertical sides and reappear on each separate flat inset panel, foreshortened according to its angle. At the limestone chimney the panorama folds around both projecting corners; joints and fine stone texture remain visible. Window arches and oak doorway reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the burgundy wool rug, the cream linen sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the pale limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
No animation requested or generated in this round.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** New architecture, children, pyjamas and Christmas projection story. Some chimney surfaces remain less covered by projection; review as generated. One take, no reroll.


## C06 - starting frame

**Frame:** `starting_frames/v15_c06_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "a11380c1-3dd8-4a0a-accc-481aec5fa3bf"}, {"role": "image", "value": "b711e297-8ca5-4199-aa1d-dcd291687645"}]}`
**Job ID:** b85e97dc-8031-4a3c-9ff5-6129174c1acd
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 7431791 bytes; SHA-256 7a9727cdcdf0dc7f2c8da09d60f808dca552e3e74ae5ff95edee7b716fce87c6. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c06_g1.png` - a11380c1-3dd8-4a0a-accc-481aec5fa3bf - role image (backend image_references)
2. `references/v15_c05_r1.png` - b711e297-8ca5-4199-aa1d-dcd291687645 - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C06 - starting frame image take 1 - changed: New children, cotton Christmas pyjamas, house/bedroom architecture, projected Christmas story and geometry-specific surface mapping; remaining camera, pose, projection contrast and sharpness blocks retained. Second reference changed to this video C05 room reference for child, pyjama and projection continuity; C06 retains its separate bedroom architecture. Theme: French country · Nutcracker Christmas.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with fair freckled skin and short tousled copper-red hair, fully dressed for winter in a burgundy-and-cream brushed-cotton Christmas pyjama set patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a cosy French-country bedroom with a high BARREL-VAULTED CEILING: one continuous smooth plaster arch curves from the left wall to the right wall without ridges or beams, ending against a vertical flat back wall with two narrow arched windows. An oak bed with a woven-cane headboard is centred on the back wall, cream bedding and a burgundy quilt, oak bedside chests, honey-oak floorboards and a burgundy wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The smooth barrel vault remains one continuous rounded plaster surface. The sleigh and ribbons curve and progressively stretch over the arch, then break cleanly at its junction with the flat back wall. The two arched window reveals interrupt the image at their real edges. No invented ridge or crossing beams interrupt the vault. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his cotton pyjama top catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** One generated take; awaiting Daniel's review.

### Video prompt - take 1
**Clip:** `clips/v15_c06_g1.mp4`
**Job ID:** `7dc73fdd-7a79-4d8c-b2f8-d763ee33d10f`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 5, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `b85e97dc-8031-4a3c-9ff5-6129174c1acd` = `starting_frames/v15_c06_g1.png`
- image `b85e97dc-8031-4a3c-9ff5-6129174c1acd` = `starting_frames/v15_c06_g1.png`
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; audio stream aac; 6537350 bytes.
**Upscale:** `clips/upscaled/v15_c06_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
SURFACE ANIMATION - PRIMARY CORRECTION: all Christmas graphics are an already-playing flat movie projected ONTO walls and ceiling. Increase clearly visible independent animation: sleigh and galloping reindeer traverse the ceiling, deer walk briskly along the wall, elves pass gifts, bells swing and strong bright waves travel along existing ribbons continuously. Both walls and ceiling show changing graphic positions every half-second, independent of camera movement. The room air is completely clear and empty. ZERO airborne snow, floating flakes, glitter, volumetric particles or objects falling from the ceiling. On ceiling planes, flat snowflake drawings slide along the plaster; on wall planes they slide down the wall. Never cross the open space between those surfaces. The child and furniture occlude the projection: no graphic appears over their silhouettes or on the bed or floor. Every moving shape foreshortens, bends and clips at the actual ceiling planes, trim faces and wall corners. The architecture and projection footprint remain stationary, while the picture inside moves strongly. Retain the already-illuminated opening and existing camera/child choreography.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the barrel-vaulted ceiling, including the entire ceiling and its source-facing architectural details. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the wall shown in the starting frame behind the bed and the whole barrel-vaulted ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy French-country bedroom with a high BARREL-VAULTED CEILING: one continuous smooth plaster arch curves from the left wall to the right wall without ridges or beams, ending against a vertical flat back wall with two narrow arched windows. An oak bed with a woven-cane headboard is centred on the back wall, cream bedding and a burgundy quilt, oak bedside chests, honey-oak floorboards and a burgundy wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about six with fair freckled skin and short tousled copper-red hair, fully dressed for winter in a burgundy-and-cream brushed-cotton Christmas pyjama set patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall shown in the starting frame and the whole barrel-vaulted ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE DRAWINGS - animated flat smoke curls rise within the projected cottage drawings on the wall, leaning right and changing shape while new drawn curls form below. These are pixels on plaster, not real smoke or haze in the room.
- THE RISING SPARK DRAWINGS - flat gold pixels climb along the wall from the illustrated village chimneys toward the painted star field at roughly one roof height each half-second. They are part of the projected wall movie, with no real sparks, airborne trails or particles between the camera and the wall.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about half of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a quarter of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE EXISTING VILLAGE FIGURES AND THE ELVES. Existing toy-shop elves walk and pass gifts, nutcrackers nod and lift their arms, and the toy train rolls through the village with turning wheels. They continuously change position at real-time speed.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about half of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE PROJECTED ORNAMENT DRAWINGS - the tiny elves keep passing gifts within the flat wall illustration beside the log-cabin depot. Flat bauble and candy-cane drawings translate and turn along the wall and ceiling planes; they have no depth in the real room. Big gold bell drawings swing visibly side to side within the same projected surface, their clapper drawings moving inside them. All obey surface perspective and architectural occlusion.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - these are strictly flat two-dimensional moving light marks on plaster, never physical flakes. On the ceiling they glide tangentially ALONG each ceiling surface toward its edge or wall seam, following its perspective; they never fall away from the ceiling into the room. On the walls they translate downward along the wall at about one quarter wall-height per second. At a wall-ceiling corner their path bends onto the adjoining surface and remains flush with it; behind the real boy, bed, headboard and beams they are occluded and disappear, never drawn over those objects. Keep their projected scale tied to the surface, with no foreground enlargement, blur, depth or free-space parallax. Every flake stays visibly attached to one architectural plane in every frame.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the wall shown in the starting frame and the barrel-vaulted ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the barrel-vaulted ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The single smooth barrel vault remains continuous. Drawings curve smoothly over its arch without an invented ridge or beam; arched window reveals and the vertical back wall interrupt light at their real boundaries. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing toy train rolls steadily through the projected village with its wheels turning; toy-shop elves walk and pass gifts; nutcrackers move their arms and nod. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
```


## C07 - starting frame

**Frame:** `starting_frames/v15_c07_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "b5910d54-c9bd-4be4-9ae3-3b870ad2e793"}, {"role": "image", "value": "b711e297-8ca5-4199-aa1d-dcd291687645"}]}`
**Job ID:** c3133600-4ea8-4653-9a1c-2783e1959255
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 7521284 bytes; SHA-256 04a33a1d9a353fabfc66a23636bd5858b3f66738c0d0ce6c2f24344c6390eba1. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c07_g1.png` - b5910d54-c9bd-4be4-9ae3-3b870ad2e793 - role image (backend image_references)
2. `references/v15_c05_r1.png` - b711e297-8ca5-4199-aa1d-dcd291687645 - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C07 - starting frame image take 1 - changed: New children, cotton Christmas pyjamas, house/bedroom architecture, projected Christmas story and geometry-specific surface mapping; remaining camera, pose, projection contrast and sharpness blocks retained. Second reference changed to this video C05 room reference for child, pyjama and projection continuity; C06 retains its separate bedroom architecture. Theme: French country · Nutcracker Christmas.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about eight with fair freckled skin and wavy auburn hair in two low braids; a boy of about six with fair freckled skin and short tousled copper-red hair. Both fully dressed in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The six deep ceiling coffers remain visibly three-dimensional. The sleigh, ribbons and garlands split at every plaster beam edge, continue down the recessed vertical sides and reappear on each separate flat inset panel, foreshortened according to its angle. At the limestone chimney the panorama folds around both projecting corners; joints and fine stone texture remain visible. Window arches and oak doorway reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the burgundy wool rug, the cream linen sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the pale limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** New architecture, children, pyjamas and Christmas projection story. Some chimney surfaces remain less covered by projection; review as generated. One take, no reroll.

### Video prompt - take 1
**Clip:** `clips/v15_c07_g1.mp4`
**Job ID:** `7a28dda2-126c-456b-b9ba-f29fd781f87a`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `c3133600-4ea8-4653-9a1c-2783e1959255` = `starting_frames/v15_c07_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 3973166 bytes.
**Upscale:** `clips/upscaled/v15_c07_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, coffered ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire coffered ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about six with fair freckled skin and short tousled copper-red hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with fair freckled skin and wavy auburn hair in two low braids, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole coffered ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, wall material and ceiling details and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE EXISTING VILLAGE FIGURES AND THE ELVES. The illustrated deer travel steadily among the projected fir trees along the lower wall, legs walking and heads nodding, moving about one body length every second. Existing rabbits make small grounded hops within the wall drawing; elves bend, lift existing wrapped gifts and pass them toward the red sleigh at the log-cabin depot. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster ceiling details, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny elves keep passing gifts beside the Christmas gift workshops and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, wall material and ceiling details. NOTHING IS PROJECTED ON THE FLOOR: the floorboards shown in the starting frame, the rug and sectional sofa shown in the starting frame, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the coffered ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their cotton pyjamas read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the coffered ceiling or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The six deep ceiling coffers and broad plaster beams remain stationary. Moving drawings break at each beam edge, continue down recess sides and reappear on inset panels, with narrow real occlusion shadows; the limestone chimney and arched window reveals stay solid. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing toy train rolls steadily through the projected village with its wheels turning; toy-shop elves walk and pass gifts; nutcrackers move their arms and nod. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
```


## C01 - hook starting frame

**Frame:** `starting_frames/v15_c01_g1.png`
**Settings:** `{"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"ff02562a-4709-4fc1-bade-56457b3e7817"},{"role":"image","value":"c3133600-4ea8-4653-9a1c-2783e1959255"}]}`
**Job ID:** eac2a2e1-2de4-47da-98cf-3a07ac625721
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 6301810 bytes; SHA-256 8aef0d6116e3e2a8ca85c99d42b51fe6dfb73658e2201de8f99d0d02652cd2fb. Native dimensions returned for requested 2k / 9:16. Temp-to-destination copy hash verified.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_172612_eac2a2e1-2de4-47da-98cf-3a07ac625721.png
**References, in attached order:**
1. `../video_10_assets/starting_frames/v10_c01_g7.png` - completed generation ff02562a-4709-4fc1-bade-56457b3e7817 - geometry and camera; role image mapped to image_references.
2. `starting_frames/v15_c07_g1.png` - completed generation c3133600-4ea8-4653-9a1c-2783e1959255 - look only as constrained in prompt; role image mapped to image_references.

Reused from v10 C01 image g7 - changed: Room finishes changed to pale sage and honey oak; mother changed to auburn-haired, fair freckled adult; children changed to red-haired siblings. Exact source camera, framing, staircase, poses, left-side child placement and lighting blocks preserved.

### Image prompt
```text
Copy the FIRST attached reference photo EXACTLY as a photograph, changing only the room finishes and people described below: a different two-storey American French-country entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, a honey-oak staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, a heavy honey-oak newel post in the lower right corner, pale sage painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, a honey-oak polished wood floor. Same composition, same perspective, same scale of the tree. Change only the room finishes and the people; retain every object's position.

THE PEOPLE - REMOVE AND REPLACE: the mother who is up on the staircase in the FIRST reference is replaced by a different MOTHER in exactly her position, at exactly her height on the stairs, at exactly her distance from the camera and exactly her size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother about 35 with fair freckled skin and copper-auburn hair in a low ponytail. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom of the frame over to the LEFT side of the frame, on the opposite side of the picture from the staircase and the newel post, well clear of the tree and NOT in front of it - the floor directly in front of the tree's base is left completely empty - with their backs to the camera, small in the frame because they are far below the top of the tree, two children - a boy about 6 with fair freckled skin and short tousled copper-red hair and a girl about 8 with fair freckled skin and wavy auburn hair in two low braids - are seen from behind, standing on the floor with their heads tipped back looking up at their mother and at the top of the tall tree, the boy holding the little girl's hand. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the pale sage wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean pale sage paint, the staircase and floor as natural honey oak, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact camera, framing, person positions, staircase geometry, tree scale and iPhone photograph look. @Image 2 supplies only the French-country house's honey-oak material look and the new children's hair and appearance. Do not import its composition, poses, projected imagery, darkness or lighting. This hook is a brightly and evenly lit daytime hall with plain pale sage walls. Keep the American-flag pyjamas from @Image 1. The children remain on the LEFT, away from the staircase and clear of the tree base. The mother remains leaning over the railing at the same scale and position.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
One generation submitted; no automatic reroll.

### Video prompt - take 1
**Clip:** `clips/v15_c01_g1.mp4`
**Job ID:** `4c07e686-8865-4f3c-97ce-7248fd16ca4c`
**Settings:** {"model": "seedance_2_5", "resolution": "1080p", "duration": 5, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `eac2a2e1-2de4-47da-98cf-3a07ac625721` = `starting_frames/v15_c01_g1.png`
**Output verification:** 1080x1920; 24/1 fps; 121 frames; encoded duration 5.05s; audio stream aac; 7143104 bytes.
**Upscale:** `clips/upscaled/v15_c01_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the hallway floor holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the staircase behind the honey-oak railing, leaning out over it with one arm stretched up to the gold star on top of the tall decorated Christmas tree beside the stairs. Two small children in matching American-flag pajamas stand on the floor at the lower left of the frame with their backs to the camera, watching her. Wrapped presents at the foot of the tree.

ACTION TIMELINE:
0.0–1.0s — Both hands now on the gold star, she works it down onto the top of the tree, stretching further and further out over the railing, more and more of her weight going onto the tree itself.
1.0–1.6s — The tree tips. It leans away from the stairs toward the open floor and keeps going, and she loses her balance and comes over the railing with it, still holding on. At the same instant the two children take three quick steps further to the left, well out of the way, and stop there — the tree never comes near them.
1.6–2.4s — The whole tree swings down diagonally across the frame and crashes flat onto the wooden floor, branches flattening, the gold star snapping off the top and skittering away on its own.
2.4–3.2s — She lands on the floor face-down across the fallen tree, and the impact bursts a wave of ornaments off the branches — dozens of red, gold, pink and white baubles bouncing out low across the wooden floor and rolling toward the camera, spreading right across the bottom of the frame.
3.2–5.0s — The last ornaments wobble to a stop on the floor. She lies still across the fallen tree for a beat, then lifts her head, blows the hair out of her face and starts laughing. The two children stay where they moved to on the left, staring at the mess. End frame: the tree flat on the floor, ornaments scattered everywhere, her looking up laughing.

AUDIO: her real voice, lip-synced, matching her appearance — a short yelp as she goes over, then breathless laughing at the end; the dry rush of the tree branches going over; the heavy thud of the tree hitting the wooden floor; dozens of glass and plastic ornaments clattering, bouncing and rolling on hard wood; one small surprised squeal from a child. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip, and the two children keep exactly the same clothes and size. The hallway stays pixel-faithful to the start frame — same staircase, same honey-oak railing and newel post, same American flag on the wall, same wooden floor, same daylight. The children are never touched by the tree and are never underneath it. Real weight and gravity — the tree topples on its own mass and stops on the floor, she drops straight down, nobody is thrown or launched. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark. No subtitles, no captions and no on-screen words of any kind anywhere in the picture.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
```

---

## Traceability - 2026-09-23

This file was repaired on 2026-09-23. Two defects were found; nothing else was changed.

1. **Truncated tail.** The file ended mid-sentence inside the final `### Image prompt` block. The block was completed from the Higgsfield image-generation record (`eac2a2e1-2de4-47da-98cf-3a07ac625721`) and verified byte-exact; the surviving text was an exact prefix of it. The `### Video prompt` and `### Take history` subsections that the section was missing were then added in the same shape the sibling sections use.
2. **Missing animation records.** Every `### Video prompt` in this file read "No animation requested or generated in this round." while all seven clips and their 2K upscales sit on disk. The submitted prompts were recovered verbatim from the video-generation records and archived as `### Video prompt - take N` subsections, each with its job ID, the media roles read off the record, and an ffprobe verification line. No prompt text was reworded or reconstructed from a neighbouring take or from watching a clip.

**Unresolved:** this round has no archived upscale job IDs and no archived `generate_audio` / `mode` / `declined_preset_id` values, so the `**Settings:**` lines above carry only what the generation record returned. Take numbering follows the NAMING.md rule that `K` is assigned in submission order; takes are listed in ascending submitted-at order.


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

### C01 — Stair hall — reaching for the topper

**In the cut:** `starting_frames/v15_c01_g1.png` → `clips/v15_c01_g1.mp4`

#### Image prompt — `starting_frames/v15_c01_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `eac2a2e1-2de4-47da-98cf-3a07ac625721`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_172612_eac2a2e1-2de4-47da-98cf-3a07ac625721.png
**References, in submission order**
- @Image 1: `content/video_10_assets/starting_frames/v10_c01_g7.png` · Higgsfield media `ff02562a-4709-4fc1-bade-56457b3e7817`
- @Image 2: `content/video_15_assets/starting_frames/v15_c07_g1.png` · Higgsfield media `c3133600-4ea8-4653-9a1c-2783e1959255`

````text
Copy the FIRST attached reference photo EXACTLY as a photograph, changing only the room finishes and people described below: a different two-storey American French-country entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, a honey-oak staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, a heavy honey-oak newel post in the lower right corner, pale sage painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, a honey-oak polished wood floor. Same composition, same perspective, same scale of the tree. Change only the room finishes and the people; retain every object's position.

THE PEOPLE - REMOVE AND REPLACE: the mother who is up on the staircase in the FIRST reference is replaced by a different MOTHER in exactly her position, at exactly her height on the stairs, at exactly her distance from the camera and exactly her size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother about 35 with fair freckled skin and copper-auburn hair in a low ponytail. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom of the frame over to the LEFT side of the frame, on the opposite side of the picture from the staircase and the newel post, well clear of the tree and NOT in front of it - the floor directly in front of the tree's base is left completely empty - with their backs to the camera, small in the frame because they are far below the top of the tree, two children - a boy about 6 with fair freckled skin and short tousled copper-red hair and a girl about 8 with fair freckled skin and wavy auburn hair in two low braids - are seen from behind, standing on the floor with their heads tipped back looking up at their mother and at the top of the tall tree, the boy holding the little girl's hand. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the pale sage wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean pale sage paint, the staircase and floor as natural honey oak, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact camera, framing, person positions, staircase geometry, tree scale and iPhone photograph look. @Image 2 supplies only the French-country house's honey-oak material look and the new children's hair and appearance. Do not import its composition, poses, projected imagery, darkness or lighting. This hook is a brightly and evenly lit daytime hall with plain pale sage walls. Keep the American-flag pyjamas from @Image 1. The children remain on the LEFT, away from the staircase and clear of the tree base. The mother remains leaning over the railing at the same scale and position.
````

#### Video prompt — `clips/v15_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `4c07e686-8865-4f3c-97ce-7248fd16ca4c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191351_4c07e686-8865-4f3c-97ce-7248fd16ca4c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v15_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_15_assets/starting_frames/v15_c01_g1.png` · Higgsfield media `eac2a2e1-2de4-47da-98cf-3a07ac625721`

````text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the hallway floor holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the staircase behind the honey-oak railing, leaning out over it with one arm stretched up to the gold star on top of the tall decorated Christmas tree beside the stairs. Two small children in matching American-flag pajamas stand on the floor at the lower left of the frame with their backs to the camera, watching her. Wrapped presents at the foot of the tree.

ACTION TIMELINE:
0.0–1.0s — Both hands now on the gold star, she works it down onto the top of the tree, stretching further and further out over the railing, more and more of her weight going onto the tree itself.
1.0–1.6s — The tree tips. It leans away from the stairs toward the open floor and keeps going, and she loses her balance and comes over the railing with it, still holding on. At the same instant the two children take three quick steps further to the left, well out of the way, and stop there — the tree never comes near them.
1.6–2.4s — The whole tree swings down diagonally across the frame and crashes flat onto the wooden floor, branches flattening, the gold star snapping off the top and skittering away on its own.
2.4–3.2s — She lands on the floor face-down across the fallen tree, and the impact bursts a wave of ornaments off the branches — dozens of red, gold, pink and white baubles bouncing out low across the wooden floor and rolling toward the camera, spreading right across the bottom of the frame.
3.2–5.0s — The last ornaments wobble to a stop on the floor. She lies still across the fallen tree for a beat, then lifts her head, blows the hair out of her face and starts laughing. The two children stay where they moved to on the left, staring at the mess. End frame: the tree flat on the floor, ornaments scattered everywhere, her looking up laughing.

AUDIO: her real voice, lip-synced, matching her appearance — a short yelp as she goes over, then breathless laughing at the end; the dry rush of the tree branches going over; the heavy thud of the tree hitting the wooden floor; dozens of glass and plastic ornaments clattering, bouncing and rolling on hard wood; one small surprised squeal from a child. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip, and the two children keep exactly the same clothes and size. The hallway stays pixel-faithful to the start frame — same staircase, same honey-oak railing and newel post, same American flag on the wall, same wooden floor, same daylight. The children are never touched by the tree and are never underneath it. Real weight and gravity — the tree topples on its own mass and stops on the floor, she drops straight down, nobody is thrown or launched. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark. No subtitles, no captions and no on-screen words of any kind anywhere in the picture.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v15_c02_g1.png` → `clips/v15_c02_g1.mp4`

#### Image prompt — `starting_frames/v15_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `87bb29f6-bdc9-4513-9a89-9babf4f67faa`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150809_87bb29f6-bdc9-4513-9a89-9babf4f67faa.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 35, with fair skin with light freckles and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a sage-green cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a honey-oak farmhouse dining table with broad straight grain, a satin-matte finish and a substantial square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive French-country dining room with warm ivory plaster walls, pale oak cabinets, an antique brass mirror, a carved limestone fireplace with red stockings and a Christmas tree dressed with burgundy bows and gold glass ornaments. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v15_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `90706e24-d8e5-4120-92c7-a2dff79a5d02`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191501_90706e24-d8e5-4120-92c7-a2dff79a5d02.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v15_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_15_assets/starting_frames/v15_c02_g1.png` · Higgsfield media `87bb29f6-bdc9-4513-9a89-9babf4f67faa`
- image ref 1: `content/video_15_assets/starting_frames/v15_c02_g1.png` · Higgsfield media `87bb29f6-bdc9-4513-9a89-9babf4f67faa`

````text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a honey-oak farmhouse dining table with broad straight grain, a satin-matte finish and a substantial square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a sage-green cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a honey-oak farmhouse dining table with broad straight grain, a satin-matte finish and a substantial square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive French-country dining room with warm ivory plaster walls, pale oak cabinets, an antique brass mirror, a carved limestone fireplace with red stockings and a Christmas tree dressed with burgundy bows and gold glass ornaments. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the pale cream terrazzo dining table with small terracotta and warm-white stone chips, a satin-matte surface and a square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v15_c03_g1.png` → `clips/v15_c03_g1.mp4`

#### Image prompt — `starting_frames/v15_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `6521ec22-9695-4f86-82fa-fa33156e0a5d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150939_6521ec22-9695-4f86-82fa-fa33156e0a5d.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
- @Image 2: `content/video_15_assets/starting_frames/v15_c02_g1.png` · Higgsfield media `87bb29f6-bdc9-4513-9a89-9babf4f67faa`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with fair skin with light freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a sage-green cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same sage-green cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C02 and owns the new woman's hands, sweater, photographic look and full-size carton-to-projector scale; the projector should plausibly fill that carton when unpacked; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v15_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `f7853fb5-540d-4529-9274-ab8549d245d6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191500_f7853fb5-540d-4529-9274-ab8549d245d6.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v15_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_15_assets/starting_frames/v15_c03_g1.png` · Higgsfield media `6521ec22-9695-4f86-82fa-fa33156e0a5d`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in sage-green cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy; behind it soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the dark charcoal honed granite counter with very fine silver-grey mineral flecks and a straight eased edge, matte rather than mirror-polished.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v15_c04_g1.png` → `clips/v15_c04_g1.mp4`

#### Image prompt — `starting_frames/v15_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `93ade77e-7356-4b70-afc6-976b87529bde`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151211_93ade77e-7356-4b70-afc6-976b87529bde.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`
- @Image 2: `content/video_15_assets/starting_frames/v15_c03_g1.png` · Higgsfield media `6521ec22-9695-4f86-82fa-fa33156e0a5d`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with fair skin with light freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a sage-green cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C03 and owns the enlarged product's physical dimensions relative to the hands, exact product identity, kitchen finishes, hands, sweater and photographic look; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v15_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `28fd0fca-2a1f-48b1-80ca-761e96aed71f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191501_28fd0fca-2a1f-48b1-80ca-761e96aed71f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v15_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_15_assets/starting_frames/v15_c04_g1.png` · Higgsfield media `93ade77e-7356-4b70-afc6-976b87529bde`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand PLUGS a white USB-C connector INTO the small dark socket in the bottom rim of the projector's white dome, and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a sage-green cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same sage-green cable-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a pale ivory honed limestone countertop with tiny natural shell flecks and a straight eased edge, matte rather than glossy; behind it soft duck-egg blue shaker cabinets with aged brass pulls, ivory handmade ceramic backsplash tiles, a cream enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the stone and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the stone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v15_c05_g1.png`, `references/v15_c05_r1.png` → `clips/v15_c05_g1.mp4`

#### Image prompt — `starting_frames/v15_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `b3101160-afff-496e-8980-229304195285`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150958_b3101160-afff-496e-8980-229304195285.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- @Image 2: `content/video_15_assets/starting_frames/v15_c02_g1.png` · Higgsfield media `87bb29f6-bdc9-4513-9a89-9babf4f67faa`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the sage-green cable-knit wool sleeve and no jewellery, with fair skin with light freckles, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a muted sage-green painted four-panel solid wood door with two tall upper panels and two shorter lower panels, a satin finish and crisp mouldings, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the sage-green paint reads clearly as muted green, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Image prompt — `references/v15_c05_r1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `b711e297-8ca5-4199-aa1d-dcd291687645`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150809_b711e297-8ca5-4199-aa1d-dcd291687645.png
**References, in submission order**
- @Image 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about six with fair freckled skin and short tousled copper-red hair; the girl is of about eight with fair freckled skin and wavy auburn hair in two low braids. Both children are fully dressed for winter in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. Seen from the doorway; the new a muted sage-green painted four-panel solid wood door with two tall upper panels and two shorter lower panels, a satin finish and crisp mouldings is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The six deep ceiling coffers remain visibly three-dimensional. The sleigh, ribbons and garlands split at every plaster beam edge, continue down the recessed vertical sides and reappear on each separate flat inset panel, foreshortened according to its angle. At the limestone chimney the panorama folds around both projecting corners; joints and fine stone texture remain visible. Window arches and oak doorway reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the burgundy wool rug, the cream linen sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the pale limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v15_c05_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `777cba5a-8326-46af-a24e-049df166e251`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191800_777cba5a-8326-46af-a24e-049df166e251.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v15_c05_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_15_assets/starting_frames/v15_c05_g1.png` · Higgsfield media `b3101160-afff-496e-8980-229304195285`
- video ref 1: `content/video_15_assets/clips/v15_c07_g1.mp4` — earlier generated clip · Higgsfield media `7a28dda2-126c-456b-b9ba-f29fd781f87a`

````text
DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Video 1. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high coffered ceiling meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

PRIMARY REQUIREMENT: this is a continuously ANIMATED Christmas movie projected on real walls and ceiling. The sleigh travels, reindeer gallop and smoke actively billows from every illustrated house chimney. Most other existing illustrated subjects move too. A static decorative image behind moving children is a failed result. Apply the detailed PROJECTED FILM ACTION below at every instant; retain the existing camera and child choreography.

CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the coffered ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the existing illustrated villagers and toy/train procession travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a muted sage-green painted four-panel solid wood door with two tall upper panels and two shorter lower panels, a satin finish and crisp mouldings fully closed with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, coffered ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED FILM ACTION - THE MAIN SUBJECT IS THE MOVING CHRISTMAS ARTWORK. Animate the existing illustrated objects themselves, not just the camera, children, brightness or glitter. At every moment MOST visible illustrated subjects are visibly changing position or shape independently. Keep the physical room and the projection's overall footprint fixed.
SLEIGH AND REINDEER: the existing sleigh team travels along the plaster ceiling at roughly one fifth of the visible ceiling width per second, crossing architectural seams and passing the fixed central star. Every reindeer continuously cycles its legs in a running gallop; heads bob, harnesses flex and the sleigh rocks behind them. The team must move relative to the stationary beams, star and ceiling corners in every half-second interval. Do not rotate the ceiling picture as a single disc.
CHIMNEYS: each visible illustrated house chimney continuously emits a clearly visible cream-grey animated smoke plume, contained INSIDE the flat wall illustration. New curls emerge every 0.25 second, rise one roof-height per second, expand and deform, then dissolve as more curls follow. Several different plumes must be visibly evolving at once; none may remain a frozen drawn squiggle. These are moving pixels on the wall, never real smoke entering the room.
VILLAGE: the existing illustrated figures walk along the wall, take full alternating steps and swing arms. Gift carriers lift and pass the existing parcels. Existing animal drawings walk with articulating legs, toy processions advance and wheels turn where present. Existing house-window light flickers independently. Buildings stay fixed so the moving figures and chimney smoke read clearly.
RIBBONS, GARLANDS AND BELLS: successive waves visibly deform each existing ribbon along its length while bright gold crests travel from the central star toward the walls, covering half a ribbon length per second. Existing bell drawings swing left-right-left roughly once per second with independently swinging clappers. Existing ornament drawings rotate within the projected picture. Do not leave the wall decorations frozen while only the ceiling sleigh moves.
SNOW AND STARS: existing snowflake drawings translate along the ceiling planes and down the walls continuously, at different speeds. Ceiling snow stays flush to ceiling plaster and follows its slope, never drops into the air. Stars twinkle independently while existing shooting-star streaks traverse the surface. Nothing moves over the boy or children, furniture, floor or in the open room.
All these actions run simultaneously from the first visible projected frame until the final frame, at normal playback speed, without a fade-in, opening pause, final freeze or settling back into the reference image. The supplied visual references fix architecture, identities and artwork appearance ONLY; replace their static or weak artwork motion with the explicit motion above. The original full projection is already on at frame zero or behind the closed door. All animated pixels bend at actual wall and ceiling seams, remain flat on those surfaces and are occluded by real foreground objects.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the actual room surfaces. The broad flat central ceiling and all four smooth ceiling transitions remain visible. The sleigh trail and garlands run across the flat panel then curve and progressively stretch around the rounded coves before continuing vertically down the walls; no invented ridge or angular fold interrupts the coves. At the chimney breast the picture breaks sharply around the two projecting vertical corners, carrying across every brick face with crisp mortar-line texture and tiny mortar shadows. The arched doorway and window reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole coffered ceiling and over every ceiling seam, right into all four corners. No bare un-animated patch of plaster and no bare ceiling detail anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera crosses the single thin doorway threshold directly into the living room, already beside its sectional and rug shown in the reference without passing through any intervening space, while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the existing illustrated villagers and toy/train procession and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl with East Asian features, light warm skin and long straight dark hair  runs a broad curving path across the rug and alongside the sofa; the boy with fair freckled skin and short tousled copper-red hair follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole coffered ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; a ribbon that sits still; a parked sleigh; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, chimney surface and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and ceiling details. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.

ROOM AND IDENTITY - a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about eight with fair freckled skin and wavy auburn hair in two low braids; a boy of about six with fair freckled skin and short tousled copper-red hair. Both fully dressed in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Preserve these identities and architecture from @Video 1.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing toy train rolls steadily through the projected village with its wheels turning; toy-shop elves walk and pass gifts; nutcrackers move their arms and nod. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v15_c06_g1.png` → `clips/v15_c06_g1.mp4`

#### Image prompt — `starting_frames/v15_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `b85e97dc-8031-4a3c-9ff5-6129174c1acd`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150940_b85e97dc-8031-4a3c-9ff5-6129174c1acd.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
- @Image 2: `content/video_15_assets/references/v15_c05_r1.png` · Higgsfield media `b711e297-8ca5-4199-aa1d-dcd291687645`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with fair freckled skin and short tousled copper-red hair, fully dressed for winter in a burgundy-and-cream brushed-cotton Christmas pyjama set patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a cosy French-country bedroom with a high BARREL-VAULTED CEILING: one continuous smooth plaster arch curves from the left wall to the right wall without ridges or beams, ending against a vertical flat back wall with two narrow arched windows. An oak bed with a woven-cane headboard is centred on the back wall, cream bedding and a burgundy quilt, oak bedside chests, honey-oak floorboards and a burgundy wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The smooth barrel vault remains one continuous rounded plaster surface. The sleigh and ribbons curve and progressively stretch over the arch, then break cleanly at its junction with the flat back wall. The two arched window reveals interrupt the image at their real edges. No invented ridge or crossing beams interrupt the vault. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his cotton pyjama top catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v15_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `7dc73fdd-7a79-4d8c-b2f8-d763ee33d10f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191536_7dc73fdd-7a79-4d8c-b2f8-d763ee33d10f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v15_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_15_assets/starting_frames/v15_c06_g1.png` · Higgsfield media `b85e97dc-8031-4a3c-9ff5-6129174c1acd`
- image ref 1: `content/video_15_assets/starting_frames/v15_c06_g1.png` · Higgsfield media `b85e97dc-8031-4a3c-9ff5-6129174c1acd`

````text
SURFACE ANIMATION - PRIMARY CORRECTION: all Christmas graphics are an already-playing flat movie projected ONTO walls and ceiling. Increase clearly visible independent animation: sleigh and galloping reindeer traverse the ceiling, deer walk briskly along the wall, elves pass gifts, bells swing and strong bright waves travel along existing ribbons continuously. Both walls and ceiling show changing graphic positions every half-second, independent of camera movement. The room air is completely clear and empty. ZERO airborne snow, floating flakes, glitter, volumetric particles or objects falling from the ceiling. On ceiling planes, flat snowflake drawings slide along the plaster; on wall planes they slide down the wall. Never cross the open space between those surfaces. The child and furniture occlude the projection: no graphic appears over their silhouettes or on the bed or floor. Every moving shape foreshortens, bends and clips at the actual ceiling planes, trim faces and wall corners. The architecture and projection footprint remain stationary, while the picture inside moves strongly. Retain the already-illuminated opening and existing camera/child choreography.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the barrel-vaulted ceiling, including the entire ceiling and its source-facing architectural details. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the wall shown in the starting frame behind the bed and the whole barrel-vaulted ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a cosy French-country bedroom with a high BARREL-VAULTED CEILING: one continuous smooth plaster arch curves from the left wall to the right wall without ridges or beams, ending against a vertical flat back wall with two narrow arched windows. An oak bed with a woven-cane headboard is centred on the back wall, cream bedding and a burgundy quilt, oak bedside chests, honey-oak floorboards and a burgundy wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about six with fair freckled skin and short tousled copper-red hair, fully dressed for winter in a burgundy-and-cream brushed-cotton Christmas pyjama set patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall shown in the starting frame and the whole barrel-vaulted ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE DRAWINGS - animated flat smoke curls rise within the projected cottage drawings on the wall, leaning right and changing shape while new drawn curls form below. These are pixels on plaster, not real smoke or haze in the room.
- THE RISING SPARK DRAWINGS - flat gold pixels climb along the wall from the illustrated village chimneys toward the painted star field at roughly one roof height each half-second. They are part of the projected wall movie, with no real sparks, airborne trails or particles between the camera and the wall.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about half of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a quarter of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE EXISTING VILLAGE FIGURES AND THE ELVES. Existing toy-shop elves walk and pass gifts, nutcrackers nod and lift their arms, and the toy train rolls through the village with turning wheels. They continuously change position at real-time speed.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about half of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE PROJECTED ORNAMENT DRAWINGS - the tiny elves keep passing gifts within the flat wall illustration beside the log-cabin depot. Flat bauble and candy-cane drawings translate and turn along the wall and ceiling planes; they have no depth in the real room. Big gold bell drawings swing visibly side to side within the same projected surface, their clapper drawings moving inside them. All obey surface perspective and architectural occlusion.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - these are strictly flat two-dimensional moving light marks on plaster, never physical flakes. On the ceiling they glide tangentially ALONG each ceiling surface toward its edge or wall seam, following its perspective; they never fall away from the ceiling into the room. On the walls they translate downward along the wall at about one quarter wall-height per second. At a wall-ceiling corner their path bends onto the adjoining surface and remains flush with it; behind the real boy, bed, headboard and beams they are occluded and disappear, never drawn over those objects. Keep their projected scale tied to the surface, with no foreground enlargement, blur, depth or free-space parallax. Every flake stays visibly attached to one architectural plane in every frame.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the wall shown in the starting frame and the barrel-vaulted ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the barrel-vaulted ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The single smooth barrel vault remains continuous. Drawings curve smoothly over its arch without an invented ridge or beam; arched window reveals and the vertical back wall interrupt light at their real boundaries. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing toy train rolls steadily through the projected village with its wheels turning; toy-shop elves walk and pass gifts; nutcrackers move their arms and nod. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v15_c07_g1.png` → `clips/v15_c07_g1.mp4`

#### Image prompt — `starting_frames/v15_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `c3133600-4ea8-4653-9a1c-2783e1959255`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150958_c3133600-4ea8-4653-9a1c-2783e1959255.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
- @Image 2: `content/video_15_assets/references/v15_c05_r1.png` · Higgsfield media `b711e297-8ca5-4199-aa1d-dcd291687645`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about eight with fair freckled skin and wavy auburn hair in two low braids; a boy of about six with fair freckled skin and short tousled copper-red hair. Both fully dressed in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The six deep ceiling coffers remain visibly three-dimensional. The sleigh, ribbons and garlands split at every plaster beam edge, continue down the recessed vertical sides and reappear on each separate flat inset panel, foreshortened according to its angle. At the limestone chimney the panorama folds around both projecting corners; joints and fine stone texture remain visible. Window arches and oak doorway reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the burgundy wool rug, the cream linen sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the pale limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v15_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `7a28dda2-126c-456b-b9ba-f29fd781f87a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191352_7a28dda2-126c-456b-b9ba-f29fd781f87a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v15_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_15_assets/starting_frames/v15_c07_g1.png` · Higgsfield media `c3133600-4ea8-4653-9a1c-2783e1959255`

````text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, coffered ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire coffered ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a spacious double-height French-country Christmas great room with a high COFFERED CEILING: a flat rectangular ceiling divided into six large deep square recesses by broad straight plaster beams. A tall pale limestone chimney breast stands on the back wall with a carved oak mantel; two tall arched windows occupy the left wall and a rectangular oak-trimmed opening sits on the right. Honey-oak floorboards, a large cream linen sectional sofa, a rectangular cream upholstered ottoman and a burgundy wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about six with fair freckled skin and short tousled copper-red hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with fair freckled skin and wavy auburn hair in two low braids, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in burgundy-and-cream brushed-cotton Christmas pyjama sets patterned with small gold nutcrackers and fir trees, with matching loose pyjama trousers and cream wool socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole coffered ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical NUTCRACKER CHRISTMAS TOY TOWN: snow-covered European toy shops with ruby-red doors, glowing golden windows, holly wreaths and tiny ribboned gifts; tall friendly red-and-gold wooden nutcrackers flank a grand illuminated Christmas tree, and cheerful elves carry drums, teddy bears and rocking horses between open workshops. A tiny red toy train carries stacks of wrapped gifts through the snowy village. Along the upper walls, sumptuous red velvet ribbon swags, gold bells and emerald fir garlands join the village into one uninterrupted festive panorama. ACROSS THE CEILING, Santa's red-and-gold sleigh and eight reindeer cross a large fine-pointed gold Christmas star, with sweeping scarlet ribbons, delicate snowflakes, small hanging baubles and countless crisp golden star points. This is unmistakably Christmas Eve, rich ruby red and antique gold dominant with deep emerald accents and a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, wall material and ceiling details and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE EXISTING VILLAGE FIGURES AND THE ELVES. The illustrated deer travel steadily among the projected fir trees along the lower wall, legs walking and heads nodding, moving about one body length every second. Existing rabbits make small grounded hops within the wall drawing; elves bend, lift existing wrapped gifts and pass them toward the red sleigh at the log-cabin depot. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster ceiling details, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny elves keep passing gifts beside the Christmas gift workshops and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, wall material and ceiling details. NOTHING IS PROJECTED ON THE FLOOR: the floorboards shown in the starting frame, the rug and sectional sofa shown in the starting frame, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the coffered ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their cotton pyjamas read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the coffered ceiling or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The six deep ceiling coffers and broad plaster beams remain stationary. Moving drawings break at each beam edge, continue down recess sides and reappear on inset panels, with narrow real occlusion shadows; the limestone chimney and arched window reveals stay solid. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing toy train rolls steadily through the projected village with its wheels turning; toy-shop elves walk and pass gifts; nutcrackers move their arms and nod. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
````
