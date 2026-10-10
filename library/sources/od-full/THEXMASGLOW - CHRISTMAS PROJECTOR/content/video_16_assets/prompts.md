# Video 16 - image archive

**Animation status (2026-09-22):** All seven requested shots, C01-C07, have local video take 1 and board players for review. Hooks use 1080p; B-roll uses 720p; each clip is 4 or 5 seconds as archived below. One generation per shot; image and earlier hook takes retained. Sampled review issues are recorded with each clip.

**Current status (2026-09-22):** C01 g2 ladder/Santa hook plus 7 B-roll images saved and on the board for review. C01 g1 tangled-lights concept superseded and retained. All current images await Daniel's review.

**Settings:** Higgsfield `gpt_image_2_5`; variant `sunburst`; resolution `2k`; quality `medium`; aspect_ratio `9:16`; count `1` per image. Reference role image is mapped by the backend to image_references.

## Reusable blocks
Exact camera, geometry, product and sharpness wording reopened from video 14. Full submitted prompts below include every reused block verbatim except the documented changes. New house finishes, hands, children, pyjamas, projection story and surface mapping; C03/C04 explicitly enlarged to match the C02 product scale. One generation per image; no self-rerolls.


## C02 - starting frame

**Frame:** `starting_frames/v16_c02_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "bbfc652c-e9eb-4430-9b53-610b56917312"}, {"role": "image", "value": "2597b25d-60d1-4060-9602-32b0ee26c2f7"}]}`
**Job ID:** 4a245f88-bad7-496c-b5a8-08562cabb85d
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 6686756 bytes; SHA-256 3702ff1585d0f383a2c86f535d927d3757c3b42922ec1981dfefaa63c4b440e1. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c02_g1.png` - bbfc652c-e9eb-4430-9b53-610b56917312 - role image (backend image_references)
2. `../../product_images/box_festive_green_g2.png` - 2597b25d-60d1-4060-9602-32b0ee26c2f7 - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C02 - starting frame image take 1 - changed: New hands and sleeve, table and house finishes. Theme: Mountain lodge · Gingerbread Christmas.

### Image prompt
```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 35, with deep brown skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a warm oatmeal rib-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a dark smoked-walnut dining table with long flowing timber grain, a matte oiled finish and a thick straight edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive mountain-lodge dining room with warm cream walls, exposed natural oak posts, a charcoal stone fireplace with ivory stockings, a copper pendant and a Christmas tree dressed with red gingham ribbons and wooden stars. Every background detail stays in focus; the box remains dominant through its scale and placement.

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
**Clip:** `clips/v16_c02_g1.mp4`
**Job ID:** `9ebb2315-1596-41cd-accf-acf6be9556ee`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `4a245f88-bad7-496c-b5a8-08562cabb85d` = `starting_frames/v16_c02_g1.png`
- image `4a245f88-bad7-496c-b5a8-08562cabb85d` = `starting_frames/v16_c02_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 2057010 bytes.
**Upscale:** `clips/upscaled/v16_c02_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a dark smoked-walnut dining table with long flowing timber grain, a matte oiled finish and a thick straight edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a warm oatmeal rib-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a dark smoked-walnut dining table with long flowing timber grain, a matte oiled finish and a thick straight edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive mountain-lodge dining room with warm cream walls, exposed natural oak posts, a charcoal stone fireplace with ivory stockings, a copper pendant and a Christmas tree dressed with red gingham ribbons and wooden stars. The same table, carton, decorations and background remain visible through the final frame.

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

**Frame:** `starting_frames/v16_c03_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "4b0ce2fa-f22e-4fdc-a781-0a2f43789130"}, {"role": "image", "value": "4a245f88-bad7-496c-b5a8-08562cabb85d"}]}`
**Job ID:** 723f2460-183b-4a63-8bb7-27cb62c2030f
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 5813005 bytes; SHA-256 9b5093efd20aa3a792877124b3891f8662811ea741f3103914ae496d1f015413. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c03_g1.png` - 4b0ce2fa-f22e-4fdc-a781-0a2f43789130 - role image (backend image_references)
2. `starting_frames/v16_c02_g1.png` - 4a245f88-bad7-496c-b5a8-08562cabb85d - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C03 - starting frame image take 1 - changed: New hand/sleeve, countertop and kitchen finishes; enlarged full projector to approximately 42 percent of frame height and dome to approximately 46 percent of frame width, replacing the older small-product scale wording. Second reference changed to this video C02 for hand, photographic-look and product-scale continuity. Theme: Mountain lodge · Gingerbread Christmas.

### Image prompt
```text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with deep brown skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a warm oatmeal rib-knit wool sweater sleeve pushed back; right forearm enters from the right in the same warm oatmeal rib-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

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
**Clip:** `clips/v16_c03_g1.mp4`
**Job ID:** `e9b559f0-7bfb-40bb-8cee-aebbc7b7a685`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `723f2460-183b-4a63-8bb7-27cb62c2030f` = `starting_frames/v16_c03_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 1917220 bytes.
**Upscale:** `clips/upscaled/v16_c03_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in warm oatmeal rib-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte; behind it warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

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

**Frame:** `starting_frames/v16_c04_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "e243effc-2c21-4bed-9551-e592483315ca"}, {"role": "image", "value": "723f2460-183b-4a63-8bb7-27cb62c2030f"}]}`
**Job ID:** f1d4724f-28eb-4868-aad6-c04d1b501c17
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 6329536 bytes; SHA-256 c8884276ea58f4ed17345db0791b38c81edb26516409129ada607e915389dc23. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c04_g1.png` - e243effc-2c21-4bed-9551-e592483315ca - role image (backend image_references)
2. `starting_frames/v16_c03_g1.png` - 723f2460-183b-4a63-8bb7-27cb62c2030f - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C04 - starting frame image take 1 - changed: New hand/sleeve, countertop and kitchen finishes; enlarged full projector to approximately 42 percent of frame height and dome to approximately 46 percent of frame width, replacing the older small-product scale wording. Second reference changed to this video C03 for the enlarged product, hands and kitchen continuity. Theme: Mountain lodge · Gingerbread Christmas.

### Image prompt
```text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with deep brown skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a warm oatmeal rib-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

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
**Clip:** `clips/v16_c04_g1.mp4`
**Job ID:** `111be539-afc1-4170-836a-5b9704a36f20`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `f1d4724f-28eb-4868-aad6-c04d1b501c17` = `starting_frames/v16_c04_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 1373856 bytes.
**Upscale:** `clips/upscaled/v16_c04_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

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
THE LEFT HAND - a woman's hand in a warm oatmeal rib-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same warm oatmeal rib-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte; behind it warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

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

**Frame:** `starting_frames/v16_c05_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "6a0df249-6245-439e-a380-e9bbdf6dc580"}, {"role": "image", "value": "4a245f88-bad7-496c-b5a8-08562cabb85d"}]}`
**Job ID:** a698375c-69a0-44fe-8e3b-c90263edf838
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 6153072 bytes; SHA-256 b68109c76554d0d213433d27d22cca28bd3c433402fe7167bb4cfd184af297bb. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c05_g1.png` - 6a0df249-6245-439e-a380-e9bbdf6dc580 - role image (backend image_references)
2. `starting_frames/v16_c02_g1.png` - 4a245f88-bad7-496c-b5a8-08562cabb85d - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C05 - starting frame image take 1 - changed: New door, hand tone and sleeve. Second reference changed to this video C02 for hand and sleeve look. Theme: Mountain lodge · Gingerbread Christmas.

### Image prompt
```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the warm oatmeal rib-knit wool sleeve and no jewellery, with deep brown skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a warm natural-oak vertical-plank solid wood door with a narrow raised perimeter frame, a matte waxed finish and clearly visible straight oak grain, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the oak grain reads clearly as warm honey brown, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** Continuity note: the generated hand/forearm is lighter than the deep-brown skin in C02/C03. One take retained for Daniel's review; no reroll.

### Video prompt - take 1
**Clip:** `clips/v16_c05_g1.mp4`
**Job ID:** `f22ebe00-0577-42ca-ab40-5c315d3627ae`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 5, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `a698375c-69a0-44fe-8e3b-c90263edf838` = `starting_frames/v16_c05_g1.png`
- image `a245e6a3-ccec-4124-bd01-5ec1ec549148` = `unresolved on this drive`
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; audio stream aac; 4228344 bytes.
**Upscale:** `clips/upscaled/v16_c05_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Video 1. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high pitched ceiling with oak tie beams meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

PRIMARY REQUIREMENT: this is a continuously ANIMATED Christmas movie projected on real walls and ceiling. The sleigh travels, reindeer gallop and smoke actively billows from every illustrated house chimney. Most other existing illustrated subjects move too. A static decorative image behind moving children is a failed result. Apply the detailed PROJECTED FILM ACTION below at every instant; retain the existing camera and child choreography.

CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the pitched ceiling with oak tie beams are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the existing illustrated villagers and toy/train procession travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a warm natural-oak vertical-plank solid wood door with a narrow raised perimeter frame, a matte waxed finish and clearly visible straight oak grain fully closed with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, pitched ceiling with oak tie beams, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED FILM ACTION - THE MAIN SUBJECT IS THE MOVING CHRISTMAS ARTWORK. Animate the existing illustrated objects themselves, not just the camera, children, brightness or glitter. At every moment MOST visible illustrated subjects are visibly changing position or shape independently. Keep the physical room and the projection's overall footprint fixed.
SLEIGH AND REINDEER: the existing sleigh team travels along the plaster ceiling at roughly one fifth of the visible ceiling width per second, crossing architectural seams and passing the fixed central star. Every reindeer continuously cycles its legs in a running gallop; heads bob, harnesses flex and the sleigh rocks behind them. The team must move relative to the stationary beams, star and ceiling corners in every half-second interval. Do not rotate the ceiling picture as a single disc.
CHIMNEYS: each visible illustrated house chimney continuously emits a clearly visible cream-grey animated smoke plume, contained INSIDE the flat wall illustration. New curls emerge every 0.25 second, rise one roof-height per second, expand and deform, then dissolve as more curls follow. Several different plumes must be visibly evolving at once; none may remain a frozen drawn squiggle. These are moving pixels on the wall, never real smoke entering the room.
VILLAGE: the existing illustrated figures walk along the wall, take full alternating steps and swing arms. Gift carriers lift and pass the existing parcels. Existing animal drawings walk with articulating legs, toy processions advance and wheels turn where present. Existing house-window light flickers independently. Buildings stay fixed so the moving figures and chimney smoke read clearly.
RIBBONS, GARLANDS AND BELLS: successive waves visibly deform each existing ribbon along its length while bright gold crests travel from the central star toward the walls, covering half a ribbon length per second. Existing bell drawings swing left-right-left roughly once per second with independently swinging clappers. Existing ornament drawings rotate within the projected picture. Do not leave the wall decorations frozen while only the ceiling sleigh moves.
SNOW AND STARS: existing snowflake drawings translate along the ceiling planes and down the walls continuously, at different speeds. Ceiling snow stays flush to ceiling plaster and follows its slope, never drops into the air. Stars twinkle independently while existing shooting-star streaks traverse the surface. Nothing moves over the boy or children, furniture, floor or in the open room.
All these actions run simultaneously from the first visible projected frame until the final frame, at normal playback speed, without a fade-in, opening pause, final freeze or settling back into the reference image. The supplied visual references fix architecture, identities and artwork appearance ONLY; replace their static or weak artwork motion with the explicit motion above. The original full projection is already on at frame zero or behind the closed door. All animated pixels bend at actual wall and ceiling seams, remain flat on those surfaces and are occluded by real foreground objects.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the actual room surfaces. The broad flat central ceiling and all four smooth ceiling transitions remain visible. The sleigh trail and garlands run across the flat panel then curve and progressively stretch around the rounded coves before continuing vertically down the walls; no invented ridge or angular fold interrupts the coves. At the chimney breast the picture breaks sharply around the two projecting vertical corners, carrying across every brick face with crisp mortar-line texture and tiny mortar shadows. The arched doorway and window reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole pitched ceiling with oak tie beams and over every ceiling seam, right into all four corners. No bare un-animated patch of plaster and no bare ceiling detail anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera crosses the single thin doorway threshold directly into the living room, already beside its sectional and rug shown in the reference without passing through any intervening space, while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the existing illustrated villagers and toy/train procession and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl with East Asian features, light warm skin and long straight dark hair  runs a broad curving path across the rug and alongside the sofa; the boy with deep brown skin and short tightly curled black hair follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole pitched ceiling with oak tie beams is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; a ribbon that sits still; a parked sleigh; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, chimney surface and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and ceiling details. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.

ROOM AND IDENTITY - a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon; a boy of about five with deep brown skin and short tightly curled black hair. Both fully dressed in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Preserve these identities and architecture from @Video 1.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing illustrated elves walk, lift gingerbread gifts and pass them through the bakery village; bakery windows flicker naturally, existing gingerbread figures wave and move. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
```


## C05 F2 - room reference

**Reference:** `references/v16_c05_r1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "dda4701e-8d9d-4351-99f8-60bb9093cf68"}, {"role": "image", "value": "1c500339-2855-45b6-bd9b-4c3633b5a272"}]}`
**Job ID:** decf983c-602d-4321-99e7-dfbc4755777d
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 7774702 bytes; SHA-256 d23f2070c51bf376644d6c659198ea27b42d4d5bc468c4e77fe566f1870c7b74. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/references/v11_c05_r1.png` - dda4701e-8d9d-4351-99f8-60bb9093cf68 - role image (backend image_references)
2. `../video_9_assets/references/v9_c05_r4.png` - 1c500339-2855-45b6-bd9b-4c3633b5a272 - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C05 F2 - room reference image take 1 - changed: New children, cotton Christmas pyjamas, house/bedroom architecture, projected Christmas story and geometry-specific surface mapping; remaining camera, pose, projection contrast and sharpness blocks retained. Theme: Mountain lodge · Gingerbread Christmas.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about five with deep brown skin and short tightly curled black hair; the girl is of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon. Both children are fully dressed for winter in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. Seen from the doorway; the new a warm natural-oak vertical-plank solid wood door with a narrow raised perimeter frame, a matte waxed finish and clearly visible straight oak grain is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two broad roof slopes, straight ridge and three solid oak tie beams remain legible. The sleigh and ribbon trail fold cleanly over the ridge. Each beam receives its own offset slice of the projected picture on its visible faces and casts a narrow hard-edged shadow behind it. The tall fieldstone chimney divides the picture at its projecting corners and irregular stone faces; the large window and doorway reveals cut the image at their real edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the cream wool rug, the warm tan linen sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the charcoal fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
No animation requested or generated in this round.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** New architecture, children, pyjamas and Christmas projection story. Some chimney surfaces remain less covered by projection; review as generated. One take, no reroll.


## C06 - starting frame

**Frame:** `starting_frames/v16_c06_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "a11380c1-3dd8-4a0a-accc-481aec5fa3bf"}, {"role": "image", "value": "decf983c-602d-4321-99e7-dfbc4755777d"}]}`
**Job ID:** 7b114869-01cc-443f-8ed1-cb95049fdfc0
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 7635958 bytes; SHA-256 239d904fa9a7b397a8a1383c751d05445b6545a8109d719e5a46c1535a1a29b1. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c06_g1.png` - a11380c1-3dd8-4a0a-accc-481aec5fa3bf - role image (backend image_references)
2. `references/v16_c05_r1.png` - decf983c-602d-4321-99e7-dfbc4755777d - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C06 - starting frame image take 1 - changed: New children, cotton Christmas pyjamas, house/bedroom architecture, projected Christmas story and geometry-specific surface mapping; remaining camera, pose, projection contrast and sharpness blocks retained. Second reference changed to this video C05 room reference for child, pyjama and projection continuity; C06 retains its separate bedroom architecture. Theme: Mountain lodge · Gingerbread Christmas.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about five with deep brown skin and short tightly curled black hair, fully dressed for winter in a forest-green brushed-cotton Christmas pyjama set patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a snug mountain-lodge bedroom with a high TRAY CEILING: a large flat rectangular raised central panel, a sloping border on all four sides and a lower flat perimeter ledge, with no ridge or beams. A walnut bed with a low square upholstered headboard is centred on a flat back wall between two rectangular windows, cream bedding with a deep forest-green quilt, walnut bedside chests, smoked-walnut floorboards and a cream wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The raised flat centre, four sloping tray borders and lower perimeter ledge remain geometrically distinct. Ribbons and the sleigh stretch across the central panel, fold at each tray edge, keystone down the slopes and break again at the lower flat ledge. The back wall and rectangular window casings receive their own properly angled slices of light. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

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
**Clip:** `clips/v16_c06_g1.mp4`
**Job ID:** `3debd321-a2b0-4eba-b00f-440a68e77bfb`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 5, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `7b114869-01cc-443f-8ed1-cb95049fdfc0` = `starting_frames/v16_c06_g1.png`
- image `7b114869-01cc-443f-8ed1-cb95049fdfc0` = `starting_frames/v16_c06_g1.png`
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; audio stream aac; 4949735 bytes.
**Upscale:** `clips/upscaled/v16_c06_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
SURFACE ANIMATION - PRIMARY CORRECTION: all Christmas graphics are an already-playing flat movie projected ONTO walls and ceiling. Increase clearly visible independent animation: sleigh and galloping reindeer traverse the ceiling, deer walk briskly along the wall, elves pass gifts, bells swing and strong bright waves travel along existing ribbons continuously. Both walls and ceiling show changing graphic positions every half-second, independent of camera movement. The room air is completely clear and empty. ZERO airborne snow, floating flakes, glitter, volumetric particles or objects falling from the ceiling. On ceiling planes, flat snowflake drawings slide along the plaster; on wall planes they slide down the wall. Never cross the open space between those surfaces. The child and furniture occlude the projection: no graphic appears over their silhouettes or on the bed or floor. Every moving shape foreshortens, bends and clips at the actual ceiling planes, trim faces and wall corners. The architecture and projection footprint remain stationary, while the picture inside moves strongly. Retain the already-illuminated opening and existing camera/child choreography.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the tray ceiling, including the entire ceiling and its source-facing architectural details. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the wall shown in the starting frame behind the bed and the whole tray ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a snug mountain-lodge bedroom with a high TRAY CEILING: a large flat rectangular raised central panel, a sloping border on all four sides and a lower flat perimeter ledge, with no ridge or beams. A walnut bed with a low square upholstered headboard is centred on a flat back wall between two rectangular windows, cream bedding with a deep forest-green quilt, walnut bedside chests, smoked-walnut floorboards and a cream wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with deep brown skin and short tightly curled black hair, fully dressed for winter in a forest-green brushed-cotton Christmas pyjama set patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall shown in the starting frame and the whole tray ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE DRAWINGS - animated flat smoke curls rise within the projected cottage drawings on the wall, leaning right and changing shape while new drawn curls form below. These are pixels on plaster, not real smoke or haze in the room.
- THE RISING SPARK DRAWINGS - flat gold pixels climb along the wall from the illustrated village chimneys toward the painted star field at roughly one roof height each half-second. They are part of the projected wall movie, with no real sparks, airborne trails or particles between the camera and the wall.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about half of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a quarter of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE EXISTING VILLAGE FIGURES AND THE ELVES. Existing bakery elves walk, lift gingerbread gifts and pass them along the village; the existing gingerbread figures wave and move. They continuously change position at real-time speed.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about half of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE PROJECTED ORNAMENT DRAWINGS - the tiny elves keep passing gifts within the flat wall illustration beside the log-cabin depot. Flat bauble and candy-cane drawings translate and turn along the wall and ceiling planes; they have no depth in the real room. Big gold bell drawings swing visibly side to side within the same projected surface, their clapper drawings moving inside them. All obey surface perspective and architectural occlusion.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - these are strictly flat two-dimensional moving light marks on plaster, never physical flakes. On the ceiling they glide tangentially ALONG each ceiling surface toward its edge or wall seam, following its perspective; they never fall away from the ceiling into the room. On the walls they translate downward along the wall at about one quarter wall-height per second. At a wall-ceiling corner their path bends onto the adjoining surface and remains flush with it; behind the real boy, bed, headboard and beams they are occluded and disappear, never drawn over those objects. Keep their projected scale tied to the surface, with no foreground enlargement, blur, depth or free-space parallax. Every flake stays visibly attached to one architectural plane in every frame.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the wall shown in the starting frame and the tray ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the tray ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The raised tray centre, four sloping borders and flat stepped perimeter remain stationary. Drawings fold at each plane change and stretch down sloping borders; no ridge or tie beams are added. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing illustrated elves walk, lift gingerbread gifts and pass them through the bakery village; bakery windows flicker naturally, existing gingerbread figures wave and move. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
```


## C07 - starting frame

**Frame:** `starting_frames/v16_c07_g1.png`
**Settings:** `{"model": "gpt_image_2_5", "variant": "sunburst", "resolution": "2k", "quality": "medium", "aspect_ratio": "9:16", "count": 1, "medias": [{"role": "image", "value": "b5910d54-c9bd-4be4-9ae3-3b870ad2e793"}, {"role": "image", "value": "decf983c-602d-4321-99e7-dfbc4755777d"}]}`
**Job ID:** 182f725f-9cf4-4ae1-91e8-3ad6af5cc43c
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 7786213 bytes; SHA-256 e4dbd467357a70e57b1bbf9f27c976862798a8e8ffa02da53224bbe71d7bb9f3. Requested model setting 2k / 9:16; dimensions are the native returned dimensions. Temp-to-destination copy hash verified.
**References, in attached order:**
1. `../video_11_assets/starting_frames/v11_c07_g1.png` - b5910d54-c9bd-4be4-9ae3-3b870ad2e793 - role image (backend image_references)
2. `references/v16_c05_r1.png` - decf983c-602d-4321-99e7-dfbc4755777d - role image (backend image_references)
**Backend adjustments:** `{"medias[0].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}, "medias[1].role": {"requested": "image", "used": "image_references", "reason": "GPT Image 2.5 backend expects schema-key media roles"}}`

Reused from v14 C07 - starting frame image take 1 - changed: New children, cotton Christmas pyjamas, house/bedroom architecture, projected Christmas story and geometry-specific surface mapping; remaining camera, pose, projection contrast and sharpness blocks retained. Second reference changed to this video C05 room reference for child, pyjama and projection continuity; C06 retains its separate bedroom architecture. Theme: Mountain lodge · Gingerbread Christmas.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon; a boy of about five with deep brown skin and short tightly curled black hair. Both fully dressed in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two broad roof slopes, straight ridge and three solid oak tie beams remain legible. The sleigh and ribbon trail fold cleanly over the ridge. Each beam receives its own offset slice of the projected picture on its visible faces and casts a narrow hard-edged shadow behind it. The tall fieldstone chimney divides the picture at its projecting corners and irregular stone faces; the large window and doorway reveals cut the image at their real edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the cream wool rug, the warm tan linen sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the charcoal fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
Take 1 only; pending Daniel's review. No prior generation overwritten and no self-reroll.

**Review note:** New architecture, children, pyjamas and Christmas projection story. Some chimney surfaces remain less covered by projection; review as generated. One take, no reroll.

### Video prompt - take 1
**Clip:** `clips/v16_c07_g1.mp4`
**Job ID:** `a245e6a3-ccec-4124-bd01-5ec1ec549148`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `182f725f-9cf4-4ae1-91e8-3ad6af5cc43c` = `starting_frames/v16_c07_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 4428663 bytes.
**Upscale:** `clips/upscaled/v16_c07_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, pitched ceiling with oak tie beams with oak tie beams panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire pitched ceiling with oak tie beams with oak tie beams and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with deep brown skin and short tightly curled black hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole pitched ceiling with oak tie beams with oak tie beams. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

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
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the pitched ceiling with oak tie beams with oak tie beams fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their cotton pyjamas read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the pitched ceiling with oak tie beams with oak tie beams or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The two pitched roof planes and three solid oak tie beams remain stationary. Drawings fold over the ridge, split across source-facing beam surfaces and reappear offset beyond them; stone chimney corners and triangular window reveals interrupt the projection. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing illustrated elves walk, lift gingerbread gifts and pass them through the bakery village; bakery windows flicker naturally, existing gingerbread figures wave and move. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
```


## C01 - hook starting frame

**Frame:** `starting_frames/v16_c01_g1.png`
**Settings:** `{"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"443746c4-8eeb-4ff2-a4da-e02a14293714"},{"role":"image","value":"182f725f-9cf4-4ae1-91e8-3ad6af5cc43c"}]}`
**Job ID:** d2e22619-70d8-4791-95a7-ef090cf50ea9
**Status:** Completed and saved locally; unreviewed.
**Output verification:** Original PNG; 1520x2688; 6352674 bytes; SHA-256 b94708f359e11fa1120625e4869cf87a7c2623c2157c9be52c5f4eb3c8b5e7fe. Native dimensions returned for requested 2k / 9:16. Temp-to-destination copy hash verified.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_172612_d2e22619-70d8-4791-95a7-ef090cf50ea9.png
**References, in attached order:**
1. `../video_9_assets/starting_frames/v9_c01_g8.png` - completed generation 443746c4-8eeb-4ff2-a4da-e02a14293714 - geometry and camera; role image mapped to image_references.
2. `starting_frames/v16_c07_g1.png` - completed generation 182f725f-9cf4-4ae1-91e8-3ad6af5cc43c - look only as constrained in prompt; role image mapped to image_references.

Reused from v9 C01 image g8 - changed: Room changed to mountain-lodge finishes; mother and children replaced. Exact source camera, framing, poses, tree, wire continuity and lighting blocks preserved.

### Image prompt
```text
Extremely high quality candid vertical iPhone photo taken from a hallway looking into a family's living room on a winter evening: a young mother kneels on the bare floor with a huge tangled knot of old multicoloured Christmas string lights in front of her, her arm stretched out to push the plug into a wall socket, while her two small children stand behind her watching the Christmas tree.

Use the FIRST attached reference photograph for BOTH the staging AND the camera position - the mother kneeling in the near foreground, the knot of lights on the floor beside her, her arm reaching out to the low wall socket, the two small children standing behind her, the tall Christmas tree on the right and the plain white wall corner the camera is looking past. COPY ITS CAMERA POSITION AND ITS COMPOSITION EXACTLY. Copy nothing else from it: the room, the mother and the children are all described below and are all different people in a different house.

FRAMING AND ANGLE - COPY THE CAMERA FROM THE REFERENCE: the camera is handheld at about the chest height of a standing adult, tilted very slightly down, standing in the next room and looking in through a doorway, so a plain white wall corner with a white skirting board runs floor to ceiling down the RIGHT EDGE of the frame and takes up roughly the right eighth of the picture - we are looking past it into the living room. The living room floor fills the bottom half of the frame and runs away into depth. The mother kneels in the lower LEFT of the frame, seen from behind at three quarters, close to the camera and large in the picture: her head and shoulders sit around the middle of the frame and the bottom edge of the picture cuts her just below the knees. The knot of lights lies on the bare floor immediately to her right, between her and that white wall corner, around the centre of the lower third of the picture. The Christmas tree stands on the RIGHT of the frame just inside the white corner, tall enough that the top edge of the picture cuts off its top. The two children stand on the floor in the middle distance between the mother and the tree, small in the frame, their heads in the middle third of the picture. Nobody is looking at the camera and nobody is posing. This is NOT a side angle, NOT a low floor-level angle and NOT a symmetrical composition.

THE KNOT AND THE PLUG: on the bare floorboards immediately to the mother's right lies a big ugly knot of old-fashioned Christmas string lights - dark green flex wound and knotted into a messy nest about the width of two floorboards across, studded with fat vintage multicoloured bulbs in red, green, blue and yellow, with a white in-line plug body and loops of slack wire lifting out of the top of it. She holds the end of that flex in her outstretched right hand and the two-pin plug is an inch from a white electrical socket set low on the white wall corner at the right of the frame. It is not plugged in yet and every bulb in the knot is dark.

THE CONNECTION - THIS IS THE IMPORTANT PART: one single continuous run of that SAME dark green flex with the SAME fat multicoloured bulbs leaves the far side of the knot, travels away across the floorboards to the right, passes behind the children, reaches the foot of the Christmas tree and climbs up into its lower branches, where it is plainly the very same string that is wound round and round the whole tree above. Same wire colour, same bulb size, same bulb spacing, one unbroken line. The eye must be able to follow the wire from the plug in her hand, through the knot on the floor, across the floor and up onto the tree without a single break or gap. The heap on the floor is NOT a separate loose pile with nothing leading out of it, and the tree is NOT wired to anything else.

THE TREE IS NOT SWITCHED ON: because the plug is still in her hand, every bulb on the tree is dark and unlit. The tree is not glowing, no light comes off it, and it throws no coloured light onto the floor, the walls or the children. It is still fully decorated and still reads as a beautiful Christmas tree - the baubles catch the warm lamplight in the room - it is simply not lit yet.

THE ROOM: a cosy American mountain-lodge living room. Walls of warm ivory plaster with white skirting and natural-oak trim, wide smoked-walnut floorboards running away from the camera, a warm tan linen sofa along the left wall with a deep red wool blanket folded over its back, a cream wool rug on the floor in front of it, a natural-oak side table behind the sofa carrying a hammered bronze table lamp with a white linen shade that is switched on and glowing, and an oak-trimmed window on the back wall showing a dark blue winter evening and snow on the sill outside. Preserve the plain white wall corner at the RIGHT EDGE exactly as in the FIRST reference.

THE TREE: a big real fir, dense and dark green, dressed with silver, white and pale blue glass baubles, cream knitted snowflakes, a wide cream linen ribbon wound down it and a silver star on top, with a heavy cream cable-knit tree skirt gathered round its base and four presents wrapped in white paper and green ribbon sitting on it.

THE MOTHER: about 34, deep brown skin and shoulder-length black curls pulled loosely back from her face, an oversized burgundy chunky cable-knit sweater with the sleeves pushed up her forearms, charcoal grey joggers and thick oatmeal socks, no shoes. She kneels sitting back on her heels, her left hand flat on the floorboards taking her weight, her right arm stretched right out towards the socket with the plug pinched between her thumb and fingers, her head turned in profile watching the plug. She is concentrating, slightly fed up, not smiling.

THE CHILDREN: a boy of about five standing on the rug behind his mother, deep brown skin and short tightly curled black hair, forest-green cotton Christmas pyjamas patterned with tiny red gingerbread houses, candy canes and white snowflakes, barefoot, his mouth wide open in a huge exaggerated gasp of amazement and both hands up near his cheeks, staring at the tree. Beside him a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon, matching forest-green cotton Christmas pyjamas patterned with tiny red gingerbread houses, candy canes and white snowflakes, crouched down on one knee with her right arm flung out pointing straight at the tree. Neither child blocks the mother, the knot of lights or the tree.

COLOUR: warm domestic evening white balance, the way an iPhone renders a lamp-lit living room - warm but not orange. The picture is NOT sepia, NOT amber-washed and NOT heavily graded. Skin reads natural, the white wall corner reads clean white, the floorboards read as real wood and the sweater reads as true burgundy.

LIGHTING AND QUALITY: the room is lit by the warm table lamp plus soft ambient light - cosy and warm, but still bright enough that every face, every twist of wire in the knot and the whole tree are clearly readable, with no dark corners where detail disappears and no blown highlights. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot somebody took of their family, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere from the mother in the foreground to the tree behind her, crisp detail in every individual bulb and every twist of flex in the tangle, realistic skin, hair and knitwear texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave the upper LEFT of the image - roughly the top eighth of the frame on the wall side - as plain uncluttered wall, free of pictures, shelves, garland, hanging decorations and lettering, so a caption can sit there. Do not pull the camera back or shrink the mother to make that room.

No captions, no watermarks, no added lettering anywhere in the image, no writing on any clothing, no user-interface elements, no mute or speaker icons and no social-media overlays.

REFERENCE ROLES: @Image 1 owns the exact camera, framing, scale, poses, wire continuity, tree and iPhone photograph look. @Image 2 supplies only the new children's appearance, pyjamas and mountain-lodge material palette. Do not import its framing, jumping pose, projected imagery, darkness or lighting. The new room uses warm ivory plaster, natural oak, smoked walnut and tan linen in the EXACT layout and camera framing of @Image 1. All walls are plain, with no projector patterns. Keep the source tree decorations unchanged and its lights unlit.
```

### Video prompt
No animation requested or generated.

### Take history
Take 1 only, completed 2026-09-22; pending Daniel's review. No self-reroll.



## C01 - hook revision, image take 2

**Frame:** `starting_frames/v16_c01_g2.png`
**Settings:** `{"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"9cd2cb32-1f96-4484-ad2f-cc726aca8088"},{"role":"image","value":"d2e22619-70d8-4791-95a7-ef090cf50ea9"}]}`
**Job ID:** 389685ed-adb4-44cf-a15f-d2f2d60d076f
**Status:** Completed and saved locally; current hook for review.
**Output verification:** Original PNG; 1520x2688; 6225787 bytes; SHA-256 bd33c42907008177dc5466c579df145a42a6b7f59621331daa1fabca0fe8dc92. Native result for requested 2k / 9:16; temp-to-destination hash verified.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_175857_389685ed-adb4-44cf-a15f-d2f2d60d076f.png
**References, in attached order:**
1. `../video_6_assets/starting_frames/v6_c01_g4.png` - generation 9cd2cb32-1f96-4484-ad2f-cc726aca8088 - geometry, framing, ladder/Santa staging, clothing and lighting.
2. `starting_frames/v16_c01_g1.png` - generation d2e22619-70d8-4791-95a7-ef090cf50ea9 - new woman identity and room material palette only.
Canonical image roles mapped to image_references by backend.

Reused from v6 C01 g4 - changed: the two edit blocks now change the woman's identity and room finishes, with the exact source camera, pose, ladder/Santa geometry, flag, pyjamas, caption space and sharpness language retained. Added explicit two-reference roles. Model/settings follow Daniel's current request: GPT Image 2.5 Sunburst, 2k, medium, 9:16, instead of the historical v6 GPT Image 2 high setting.

### Image prompt
```text
Keep the FIRST attached image exactly as it is - the same room layout, the same camera position, distance and angle, a different woman in the same pose near the top of the same ladder with both arms up, the same inflatable Santa taped flat to the ceiling with the same silver duct tape, the same curved staircase, garland, stockings, fireplace, mirror, Christmas tree, sofa and rug positions, the same lighting, and the same clean empty band of ceiling across the top sixth of the frame. Change only these two things:

1. THE WOMAN: replace her with a mother about 34 with deep brown skin and shoulder-length black curls pulled loosely back from her face, matching the woman's identity in @Image 2. She is wearing matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit. Same body scale, same pose, same thick grey wool socks, same roll of duct tape in her left hand.

2. THE ROOM: a different double-height mountain-lodge living room, with warm ivory plaster walls and natural-oak panelling, a natural-oak curved staircase in the same position, a charcoal fieldstone fireplace with a lit fire and an oak-framed mirror above it, a warm tan linen sofa and a cream wool rug over smoked-walnut floorboards. Keep the high plain white ceiling at exactly the same height and shape. The garland, stockings, tree, lamps and furniture stay in exactly the same positions and at the same scale as @Image 1. A real fabric United States flag hangs flat against the plain ivory wall in the same background position as @Image 1, clearly readable stars and stripes, hanging straight and still. It does not cover the Christmas tree, the fireplace or the staircase, and it does not reach up into the empty band of ceiling at the top of the frame.

Everything else in the picture stays exactly as it is. Same neutral white balance with no orange cast, same iPhone snapshot look, tack sharp and in focus everywhere, absolutely nothing blurry, no background blur.

REFERENCE ROLES: @Image 1 is the approved Video 6 hook and owns the exact camera, low three-quarters-from-behind angle, framing, tall A-frame ladder, woman scale and raised-arm pose, taped inflatable Santa, duct tape roll, American-flag pyjamas and crisp iPhone lighting. @Image 2 supplies only the new woman's face, skin and hair and the mountain-lodge material palette. Do not import its kneeling pose, children, tangled lights, socket action, camera or composition. This hook contains one woman on the ladder, as in @Image 1. Santa is taped flat to the ceiling with the same criss-crossed silver tape. No projected patterns, no text, no captions, no watermark, no bokeh. Perfectly exposed, extremely high quality, tack sharp edge to edge.
```

### Video prompt
Initial still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Take history
One generation submitted; no automatic reroll.

### Video prompt - take 1
**Clip:** `clips/v16_c01_g1.mp4`
**Job ID:** `594ebc7a-e9ba-4b29-82a7-61c3521f6717`
**Settings:** {"model": "seedance_2_5", "resolution": "1080p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `389685ed-adb4-44cf-a15f-d2f2d60d076f` = `starting_frames/v16_c01_g2.png`
**Output verification:** 1080x1920; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 5794550 bytes.
**Upscale:** `clips/upscaled/v16_c01_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
Real home video, shot on a hand-held iPhone by a person standing in the room a few steps behind her, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow her, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and her body never resets, jumps position or teleports between one part and the next.

For the first second she is just taping the inflatable Santa to the ceiling - both hands up, pressing and smoothing, nothing dramatic.

Then, without any pause or break in the movement, she loses her footing and falls off the ladder to the floor. Her arms are still up and still coming down out of the taping motion as her balance goes - the taping and the fall are one unbroken piece of movement, not two separate actions.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug.

She lands hard and the movement carries straight on into stillness without a break - she settles, rocks slightly as her weight comes to rest, and stays down on the floor for the rest of the clip, not moving much, just stunned and breathing. Her chest is still moving and she is still there when the clip ends.

The inflatable Santa stays taped to the ceiling the whole time.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the tape, a short gasp, the ladder hitting the floor, then her breathing.
```

---

## Traceability - 2026-09-23

This file was repaired on 2026-09-23. Two defects were found; nothing else was changed.

1. **Truncated tail.** The file ended mid-sentence inside the final `### Image prompt` block. The block was completed from the Higgsfield image-generation record (`389685ed-adb4-44cf-a15f-d2f2d60d076f`) and verified byte-exact; the surviving text was an exact prefix of it. The `### Video prompt` and `### Take history` subsections that the section was missing were then added in the same shape the sibling sections use.
2. **Missing animation records.** Every `### Video prompt` in this file read "No animation requested or generated in this round." while all seven clips and their 2K upscales sit on disk. The submitted prompts were recovered verbatim from the video-generation records and archived as `### Video prompt - take N` subsections, each with its job ID, the media roles read off the record, and an ffprobe verification line. No prompt text was reworded or reconstructed from a neighbouring take or from watching a clip.

**Unresolved:** this round has no archived upscale job IDs and no archived `generate_audio` / `mode` / `declined_preset_id` values, so the `**Settings:**` lines above carry only what the generation record returned. Take numbering follows the NAMING.md rule that `K` is assigned in submission order; takes are listed in ascending submitted-at order.


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C05: the board did not show the exact image prompt of `v16_c05_g1.png`; it now does.
- C05: the board did not show the exact image prompt of `v16_c05_r1.png`; it now does.

### C01 — Ladder fail — taping Santa up

**In the cut:** `starting_frames/v16_c01_g2.png` → `clips/v16_c01_g1.mp4`

#### Image prompt — `starting_frames/v16_c01_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `389685ed-adb4-44cf-a15f-d2f2d60d076f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_175857_389685ed-adb4-44cf-a15f-d2f2d60d076f.png
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c01_g4.png` · Higgsfield media `9cd2cb32-1f96-4484-ad2f-cc726aca8088`
- @Image 2: `content/video_16_assets/starting_frames/v16_c01_g1.png` · Higgsfield media `d2e22619-70d8-4791-95a7-ef090cf50ea9`

````text
Keep the FIRST attached image exactly as it is - the same room layout, the same camera position, distance and angle, a different woman in the same pose near the top of the same ladder with both arms up, the same inflatable Santa taped flat to the ceiling with the same silver duct tape, the same curved staircase, garland, stockings, fireplace, mirror, Christmas tree, sofa and rug positions, the same lighting, and the same clean empty band of ceiling across the top sixth of the frame. Change only these two things:

1. THE WOMAN: replace her with a mother about 34 with deep brown skin and shoulder-length black curls pulled loosely back from her face, matching the woman's identity in @Image 2. She is wearing matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit. Same body scale, same pose, same thick grey wool socks, same roll of duct tape in her left hand.

2. THE ROOM: a different double-height mountain-lodge living room, with warm ivory plaster walls and natural-oak panelling, a natural-oak curved staircase in the same position, a charcoal fieldstone fireplace with a lit fire and an oak-framed mirror above it, a warm tan linen sofa and a cream wool rug over smoked-walnut floorboards. Keep the high plain white ceiling at exactly the same height and shape. The garland, stockings, tree, lamps and furniture stay in exactly the same positions and at the same scale as @Image 1. A real fabric United States flag hangs flat against the plain ivory wall in the same background position as @Image 1, clearly readable stars and stripes, hanging straight and still. It does not cover the Christmas tree, the fireplace or the staircase, and it does not reach up into the empty band of ceiling at the top of the frame.

Everything else in the picture stays exactly as it is. Same neutral white balance with no orange cast, same iPhone snapshot look, tack sharp and in focus everywhere, absolutely nothing blurry, no background blur.

REFERENCE ROLES: @Image 1 is the approved Video 6 hook and owns the exact camera, low three-quarters-from-behind angle, framing, tall A-frame ladder, woman scale and raised-arm pose, taped inflatable Santa, duct tape roll, American-flag pyjamas and crisp iPhone lighting. @Image 2 supplies only the new woman's face, skin and hair and the mountain-lodge material palette. Do not import its kneeling pose, children, tangled lights, socket action, camera or composition. This hook contains one woman on the ladder, as in @Image 1. Santa is taped flat to the ceiling with the same criss-crossed silver tape. No projected patterns, no text, no captions, no watermark, no bokeh. Perfectly exposed, extremely high quality, tack sharp edge to edge.
````

#### Video prompt — `clips/v16_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `594ebc7a-e9ba-4b29-82a7-61c3521f6717`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191351_594ebc7a-e9ba-4b29-82a7-61c3521f6717.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v16_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_16_assets/starting_frames/v16_c01_g2.png` · Higgsfield media `389685ed-adb4-44cf-a15f-d2f2d60d076f`

````text
Real home video, shot on a hand-held iPhone by a person standing in the room a few steps behind her, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow her, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and her body never resets, jumps position or teleports between one part and the next.

For the first second she is just taping the inflatable Santa to the ceiling - both hands up, pressing and smoothing, nothing dramatic.

Then, without any pause or break in the movement, she loses her footing and falls off the ladder to the floor. Her arms are still up and still coming down out of the taping motion as her balance goes - the taping and the fall are one unbroken piece of movement, not two separate actions.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug.

She lands hard and the movement carries straight on into stillness without a break - she settles, rocks slightly as her weight comes to rest, and stays down on the floor for the rest of the clip, not moving much, just stunned and breathing. Her chest is still moving and she is still there when the clip ends.

The inflatable Santa stays taped to the ceiling the whole time.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the tape, a short gasp, the ladder hitting the floor, then her breathing.
````

**Other takes of C01 on disk (1)**

#### Image prompt — `starting_frames/v16_c01_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `d2e22619-70d8-4791-95a7-ef090cf50ea9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_172612_d2e22619-70d8-4791-95a7-ef090cf50ea9.png
**References, in submission order**
- @Image 1: `content/video_9_assets/starting_frames/v9_c01_g8.png` · Higgsfield media `443746c4-8eeb-4ff2-a4da-e02a14293714`
- @Image 2: `content/video_16_assets/starting_frames/v16_c07_g1.png` · Higgsfield media `182f725f-9cf4-4ae1-91e8-3ad6af5cc43c`

````text
Extremely high quality candid vertical iPhone photo taken from a hallway looking into a family's living room on a winter evening: a young mother kneels on the bare floor with a huge tangled knot of old multicoloured Christmas string lights in front of her, her arm stretched out to push the plug into a wall socket, while her two small children stand behind her watching the Christmas tree.

Use the FIRST attached reference photograph for BOTH the staging AND the camera position - the mother kneeling in the near foreground, the knot of lights on the floor beside her, her arm reaching out to the low wall socket, the two small children standing behind her, the tall Christmas tree on the right and the plain white wall corner the camera is looking past. COPY ITS CAMERA POSITION AND ITS COMPOSITION EXACTLY. Copy nothing else from it: the room, the mother and the children are all described below and are all different people in a different house.

FRAMING AND ANGLE - COPY THE CAMERA FROM THE REFERENCE: the camera is handheld at about the chest height of a standing adult, tilted very slightly down, standing in the next room and looking in through a doorway, so a plain white wall corner with a white skirting board runs floor to ceiling down the RIGHT EDGE of the frame and takes up roughly the right eighth of the picture - we are looking past it into the living room. The living room floor fills the bottom half of the frame and runs away into depth. The mother kneels in the lower LEFT of the frame, seen from behind at three quarters, close to the camera and large in the picture: her head and shoulders sit around the middle of the frame and the bottom edge of the picture cuts her just below the knees. The knot of lights lies on the bare floor immediately to her right, between her and that white wall corner, around the centre of the lower third of the picture. The Christmas tree stands on the RIGHT of the frame just inside the white corner, tall enough that the top edge of the picture cuts off its top. The two children stand on the floor in the middle distance between the mother and the tree, small in the frame, their heads in the middle third of the picture. Nobody is looking at the camera and nobody is posing. This is NOT a side angle, NOT a low floor-level angle and NOT a symmetrical composition.

THE KNOT AND THE PLUG: on the bare floorboards immediately to the mother's right lies a big ugly knot of old-fashioned Christmas string lights - dark green flex wound and knotted into a messy nest about the width of two floorboards across, studded with fat vintage multicoloured bulbs in red, green, blue and yellow, with a white in-line plug body and loops of slack wire lifting out of the top of it. She holds the end of that flex in her outstretched right hand and the two-pin plug is an inch from a white electrical socket set low on the white wall corner at the right of the frame. It is not plugged in yet and every bulb in the knot is dark.

THE CONNECTION - THIS IS THE IMPORTANT PART: one single continuous run of that SAME dark green flex with the SAME fat multicoloured bulbs leaves the far side of the knot, travels away across the floorboards to the right, passes behind the children, reaches the foot of the Christmas tree and climbs up into its lower branches, where it is plainly the very same string that is wound round and round the whole tree above. Same wire colour, same bulb size, same bulb spacing, one unbroken line. The eye must be able to follow the wire from the plug in her hand, through the knot on the floor, across the floor and up onto the tree without a single break or gap. The heap on the floor is NOT a separate loose pile with nothing leading out of it, and the tree is NOT wired to anything else.

THE TREE IS NOT SWITCHED ON: because the plug is still in her hand, every bulb on the tree is dark and unlit. The tree is not glowing, no light comes off it, and it throws no coloured light onto the floor, the walls or the children. It is still fully decorated and still reads as a beautiful Christmas tree - the baubles catch the warm lamplight in the room - it is simply not lit yet.

THE ROOM: a cosy American mountain-lodge living room. Walls of warm ivory plaster with white skirting and natural-oak trim, wide smoked-walnut floorboards running away from the camera, a warm tan linen sofa along the left wall with a deep red wool blanket folded over its back, a cream wool rug on the floor in front of it, a natural-oak side table behind the sofa carrying a hammered bronze table lamp with a white linen shade that is switched on and glowing, and an oak-trimmed window on the back wall showing a dark blue winter evening and snow on the sill outside. Preserve the plain white wall corner at the RIGHT EDGE exactly as in the FIRST reference.

THE TREE: a big real fir, dense and dark green, dressed with silver, white and pale blue glass baubles, cream knitted snowflakes, a wide cream linen ribbon wound down it and a silver star on top, with a heavy cream cable-knit tree skirt gathered round its base and four presents wrapped in white paper and green ribbon sitting on it.

THE MOTHER: about 34, deep brown skin and shoulder-length black curls pulled loosely back from her face, an oversized burgundy chunky cable-knit sweater with the sleeves pushed up her forearms, charcoal grey joggers and thick oatmeal socks, no shoes. She kneels sitting back on her heels, her left hand flat on the floorboards taking her weight, her right arm stretched right out towards the socket with the plug pinched between her thumb and fingers, her head turned in profile watching the plug. She is concentrating, slightly fed up, not smiling.

THE CHILDREN: a boy of about five standing on the rug behind his mother, deep brown skin and short tightly curled black hair, forest-green cotton Christmas pyjamas patterned with tiny red gingerbread houses, candy canes and white snowflakes, barefoot, his mouth wide open in a huge exaggerated gasp of amazement and both hands up near his cheeks, staring at the tree. Beside him a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon, matching forest-green cotton Christmas pyjamas patterned with tiny red gingerbread houses, candy canes and white snowflakes, crouched down on one knee with her right arm flung out pointing straight at the tree. Neither child blocks the mother, the knot of lights or the tree.

COLOUR: warm domestic evening white balance, the way an iPhone renders a lamp-lit living room - warm but not orange. The picture is NOT sepia, NOT amber-washed and NOT heavily graded. Skin reads natural, the white wall corner reads clean white, the floorboards read as real wood and the sweater reads as true burgundy.

LIGHTING AND QUALITY: the room is lit by the warm table lamp plus soft ambient light - cosy and warm, but still bright enough that every face, every twist of wire in the knot and the whole tree are clearly readable, with no dark corners where detail disappears and no blown highlights. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot somebody took of their family, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere from the mother in the foreground to the tree behind her, crisp detail in every individual bulb and every twist of flex in the tangle, realistic skin, hair and knitwear texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave the upper LEFT of the image - roughly the top eighth of the frame on the wall side - as plain uncluttered wall, free of pictures, shelves, garland, hanging decorations and lettering, so a caption can sit there. Do not pull the camera back or shrink the mother to make that room.

No captions, no watermarks, no added lettering anywhere in the image, no writing on any clothing, no user-interface elements, no mute or speaker icons and no social-media overlays.

REFERENCE ROLES: @Image 1 owns the exact camera, framing, scale, poses, wire continuity, tree and iPhone photograph look. @Image 2 supplies only the new children's appearance, pyjamas and mountain-lodge material palette. Do not import its framing, jumping pose, projected imagery, darkness or lighting. The new room uses warm ivory plaster, natural oak, smoked walnut and tan linen in the EXACT layout and camera framing of @Image 1. All walls are plain, with no projector patterns. Keep the source tree decorations unchanged and its lights unlit.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v16_c02_g1.png` → `clips/v16_c02_g1.mp4`

#### Image prompt — `starting_frames/v16_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `4a245f88-bad7-496c-b5a8-08562cabb85d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150809_4a245f88-bad7-496c-b5a8-08562cabb85d.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 35, with deep brown skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a warm oatmeal rib-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a dark smoked-walnut dining table with long flowing timber grain, a matte oiled finish and a thick straight edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive mountain-lodge dining room with warm cream walls, exposed natural oak posts, a charcoal stone fireplace with ivory stockings, a copper pendant and a Christmas tree dressed with red gingham ribbons and wooden stars. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v16_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `9ebb2315-1596-41cd-accf-acf6be9556ee`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191501_9ebb2315-1596-41cd-accf-acf6be9556ee.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v16_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_16_assets/starting_frames/v16_c02_g1.png` · Higgsfield media `4a245f88-bad7-496c-b5a8-08562cabb85d`
- image ref 1: `content/video_16_assets/starting_frames/v16_c02_g1.png` · Higgsfield media `4a245f88-bad7-496c-b5a8-08562cabb85d`

````text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a dark smoked-walnut dining table with long flowing timber grain, a matte oiled finish and a thick straight edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a warm oatmeal rib-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a dark smoked-walnut dining table with long flowing timber grain, a matte oiled finish and a thick straight edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive mountain-lodge dining room with warm cream walls, exposed natural oak posts, a charcoal stone fireplace with ivory stockings, a copper pendant and a Christmas tree dressed with red gingham ribbons and wooden stars. The same table, carton, decorations and background remain visible through the final frame.

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

**In the cut:** `starting_frames/v16_c03_g1.png` → `clips/v16_c03_g1.mp4`

#### Image prompt — `starting_frames/v16_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `723f2460-183b-4a63-8bb7-27cb62c2030f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150940_723f2460-183b-4a63-8bb7-27cb62c2030f.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
- @Image 2: `content/video_16_assets/starting_frames/v16_c02_g1.png` · Higgsfield media `4a245f88-bad7-496c-b5a8-08562cabb85d`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with deep brown skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a warm oatmeal rib-knit wool sweater sleeve pushed back; right forearm enters from the right in the same warm oatmeal rib-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C02 and owns the new woman's hands, sweater, photographic look and full-size carton-to-projector scale; the projector should plausibly fill that carton when unpacked; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v16_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `e9b559f0-7bfb-40bb-8cee-aebbc7b7a685`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191500_e9b559f0-7bfb-40bb-8cee-aebbc7b7a685.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v16_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_16_assets/starting_frames/v16_c03_g1.png` · Higgsfield media `723f2460-183b-4a63-8bb7-27cb62c2030f`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in warm oatmeal rib-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte; behind it warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

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

**In the cut:** `starting_frames/v16_c04_g1.png` → `clips/v16_c04_g1.mp4`

#### Image prompt — `starting_frames/v16_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `f1d4724f-28eb-4868-aad6-c04d1b501c17`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151211_f1d4724f-28eb-4868-aad6-c04d1b501c17.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`
- @Image 2: `content/video_16_assets/starting_frames/v16_c03_g1.png` · Higgsfield media `723f2460-183b-4a63-8bb7-27cb62c2030f`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with deep brown skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a warm oatmeal rib-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C03 and owns the enlarged product's physical dimensions relative to the hands, exact product identity, kitchen finishes, hands, sweater and photographic look; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v16_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `111be539-afc1-4170-836a-5b9704a36f20`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191501_111be539-afc1-4170-836a-5b9704a36f20.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v16_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_16_assets/starting_frames/v16_c04_g1.png` · Higgsfield media `f1d4724f-28eb-4868-aad6-c04d1b501c17`

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
THE LEFT HAND - a woman's hand in a warm oatmeal rib-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same warm oatmeal rib-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a dark soapstone countertop with delicate ivory veins and a straight eased edge, smooth and matte; behind it warm natural oak slab cabinets with matte black pulls, pale cream zellige backsplash tiles, a brushed stainless steel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

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

**In the cut:** `starting_frames/v16_c05_g1.png`, `references/v16_c05_r1.png` → `clips/v16_c05_g1.mp4`

#### Image prompt — `starting_frames/v16_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a698375c-69a0-44fe-8e3b-c90263edf838`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150958_a698375c-69a0-44fe-8e3b-c90263edf838.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- @Image 2: `content/video_16_assets/starting_frames/v16_c02_g1.png` · Higgsfield media `4a245f88-bad7-496c-b5a8-08562cabb85d`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the warm oatmeal rib-knit wool sleeve and no jewellery, with deep brown skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a warm natural-oak vertical-plank solid wood door with a narrow raised perimeter frame, a matte waxed finish and clearly visible straight oak grain, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the oak grain reads clearly as warm honey brown, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Image prompt — `references/v16_c05_r1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `decf983c-602d-4321-99e7-dfbc4755777d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150810_decf983c-602d-4321-99e7-dfbc4755777d.png
**References, in submission order**
- @Image 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about five with deep brown skin and short tightly curled black hair; the girl is of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon. Both children are fully dressed for winter in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. Seen from the doorway; the new a warm natural-oak vertical-plank solid wood door with a narrow raised perimeter frame, a matte waxed finish and clearly visible straight oak grain is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two broad roof slopes, straight ridge and three solid oak tie beams remain legible. The sleigh and ribbon trail fold cleanly over the ridge. Each beam receives its own offset slice of the projected picture on its visible faces and casts a narrow hard-edged shadow behind it. The tall fieldstone chimney divides the picture at its projecting corners and irregular stone faces; the large window and doorway reveals cut the image at their real edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the cream wool rug, the warm tan linen sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the charcoal fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v16_c05_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `f22ebe00-0577-42ca-ab40-5c315d3627ae`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191802_f22ebe00-0577-42ca-ab40-5c315d3627ae.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v16_c05_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_16_assets/starting_frames/v16_c05_g1.png` · Higgsfield media `a698375c-69a0-44fe-8e3b-c90263edf838`
- video ref 1: `content/video_16_assets/clips/v16_c07_g1.mp4` — earlier generated clip · Higgsfield media `a245e6a3-ccec-4124-bd01-5ec1ec549148`

````text
DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Video 1. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high pitched ceiling with oak tie beams meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

PRIMARY REQUIREMENT: this is a continuously ANIMATED Christmas movie projected on real walls and ceiling. The sleigh travels, reindeer gallop and smoke actively billows from every illustrated house chimney. Most other existing illustrated subjects move too. A static decorative image behind moving children is a failed result. Apply the detailed PROJECTED FILM ACTION below at every instant; retain the existing camera and child choreography.

CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the pitched ceiling with oak tie beams are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the existing illustrated villagers and toy/train procession travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a warm natural-oak vertical-plank solid wood door with a narrow raised perimeter frame, a matte waxed finish and clearly visible straight oak grain fully closed with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, pitched ceiling with oak tie beams, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED FILM ACTION - THE MAIN SUBJECT IS THE MOVING CHRISTMAS ARTWORK. Animate the existing illustrated objects themselves, not just the camera, children, brightness or glitter. At every moment MOST visible illustrated subjects are visibly changing position or shape independently. Keep the physical room and the projection's overall footprint fixed.
SLEIGH AND REINDEER: the existing sleigh team travels along the plaster ceiling at roughly one fifth of the visible ceiling width per second, crossing architectural seams and passing the fixed central star. Every reindeer continuously cycles its legs in a running gallop; heads bob, harnesses flex and the sleigh rocks behind them. The team must move relative to the stationary beams, star and ceiling corners in every half-second interval. Do not rotate the ceiling picture as a single disc.
CHIMNEYS: each visible illustrated house chimney continuously emits a clearly visible cream-grey animated smoke plume, contained INSIDE the flat wall illustration. New curls emerge every 0.25 second, rise one roof-height per second, expand and deform, then dissolve as more curls follow. Several different plumes must be visibly evolving at once; none may remain a frozen drawn squiggle. These are moving pixels on the wall, never real smoke entering the room.
VILLAGE: the existing illustrated figures walk along the wall, take full alternating steps and swing arms. Gift carriers lift and pass the existing parcels. Existing animal drawings walk with articulating legs, toy processions advance and wheels turn where present. Existing house-window light flickers independently. Buildings stay fixed so the moving figures and chimney smoke read clearly.
RIBBONS, GARLANDS AND BELLS: successive waves visibly deform each existing ribbon along its length while bright gold crests travel from the central star toward the walls, covering half a ribbon length per second. Existing bell drawings swing left-right-left roughly once per second with independently swinging clappers. Existing ornament drawings rotate within the projected picture. Do not leave the wall decorations frozen while only the ceiling sleigh moves.
SNOW AND STARS: existing snowflake drawings translate along the ceiling planes and down the walls continuously, at different speeds. Ceiling snow stays flush to ceiling plaster and follows its slope, never drops into the air. Stars twinkle independently while existing shooting-star streaks traverse the surface. Nothing moves over the boy or children, furniture, floor or in the open room.
All these actions run simultaneously from the first visible projected frame until the final frame, at normal playback speed, without a fade-in, opening pause, final freeze or settling back into the reference image. The supplied visual references fix architecture, identities and artwork appearance ONLY; replace their static or weak artwork motion with the explicit motion above. The original full projection is already on at frame zero or behind the closed door. All animated pixels bend at actual wall and ceiling seams, remain flat on those surfaces and are occluded by real foreground objects.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the actual room surfaces. The broad flat central ceiling and all four smooth ceiling transitions remain visible. The sleigh trail and garlands run across the flat panel then curve and progressively stretch around the rounded coves before continuing vertically down the walls; no invented ridge or angular fold interrupts the coves. At the chimney breast the picture breaks sharply around the two projecting vertical corners, carrying across every brick face with crisp mortar-line texture and tiny mortar shadows. The arched doorway and window reveals interrupt the light at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole pitched ceiling with oak tie beams and over every ceiling seam, right into all four corners. No bare un-animated patch of plaster and no bare ceiling detail anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera crosses the single thin doorway threshold directly into the living room, already beside its sectional and rug shown in the reference without passing through any intervening space, while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the existing illustrated villagers and toy/train procession and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl with East Asian features, light warm skin and long straight dark hair  runs a broad curving path across the rug and alongside the sofa; the boy with deep brown skin and short tightly curled black hair follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole pitched ceiling with oak tie beams is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; a ribbon that sits still; a parked sleigh; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, chimney surface and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and ceiling details. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.

ROOM AND IDENTITY - a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon; a boy of about five with deep brown skin and short tightly curled black hair. Both fully dressed in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Preserve these identities and architecture from @Video 1.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing illustrated elves walk, lift gingerbread gifts and pass them through the bakery village; bakery windows flicker naturally, existing gingerbread figures wave and move. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v16_c06_g1.png` → `clips/v16_c06_g1.mp4`

#### Image prompt — `starting_frames/v16_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `7b114869-01cc-443f-8ed1-cb95049fdfc0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150939_7b114869-01cc-443f-8ed1-cb95049fdfc0.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
- @Image 2: `content/video_16_assets/references/v16_c05_r1.png` · Higgsfield media `decf983c-602d-4321-99e7-dfbc4755777d`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about five with deep brown skin and short tightly curled black hair, fully dressed for winter in a forest-green brushed-cotton Christmas pyjama set patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a snug mountain-lodge bedroom with a high TRAY CEILING: a large flat rectangular raised central panel, a sloping border on all four sides and a lower flat perimeter ledge, with no ridge or beams. A walnut bed with a low square upholstered headboard is centred on a flat back wall between two rectangular windows, cream bedding with a deep forest-green quilt, walnut bedside chests, smoked-walnut floorboards and a cream wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The raised flat centre, four sloping tray borders and lower perimeter ledge remain geometrically distinct. Ribbons and the sleigh stretch across the central panel, fold at each tray edge, keystone down the slopes and break again at the lower flat ledge. The back wall and rectangular window casings receive their own properly angled slices of light. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his cotton pyjama top catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v16_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `3debd321-a2b0-4eba-b00f-440a68e77bfb`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191536_3debd321-a2b0-4eba-b00f-440a68e77bfb.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v16_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_16_assets/starting_frames/v16_c06_g1.png` · Higgsfield media `7b114869-01cc-443f-8ed1-cb95049fdfc0`
- image ref 1: `content/video_16_assets/starting_frames/v16_c06_g1.png` · Higgsfield media `7b114869-01cc-443f-8ed1-cb95049fdfc0`

````text
SURFACE ANIMATION - PRIMARY CORRECTION: all Christmas graphics are an already-playing flat movie projected ONTO walls and ceiling. Increase clearly visible independent animation: sleigh and galloping reindeer traverse the ceiling, deer walk briskly along the wall, elves pass gifts, bells swing and strong bright waves travel along existing ribbons continuously. Both walls and ceiling show changing graphic positions every half-second, independent of camera movement. The room air is completely clear and empty. ZERO airborne snow, floating flakes, glitter, volumetric particles or objects falling from the ceiling. On ceiling planes, flat snowflake drawings slide along the plaster; on wall planes they slide down the wall. Never cross the open space between those surfaces. The child and furniture occlude the projection: no graphic appears over their silhouettes or on the bed or floor. Every moving shape foreshortens, bends and clips at the actual ceiling planes, trim faces and wall corners. The architecture and projection footprint remain stationary, while the picture inside moves strongly. Retain the already-illuminated opening and existing camera/child choreography.

OPENING STATE - frame 0.0s is EXACTLY the supplied starting image, with its already complete, saturated Christmas projection on every visible wall and the tray ceiling, including the entire ceiling and its source-facing architectural details. The projector has been running for a long time before filming. Full coverage, colour density and brightness remain present throughout all five seconds; the illustrated elements are already travelling when filming starts. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later. Frame 0.0s, 0.1s, 0.5s and 1.0s all show the same fully illuminated room with the artwork at successive positions in its animation. @Image 1 fixes the opening geometry; @Image 2 is the SAME approved frame and fixes the already-lit appearance. Preserve the fully projected background from BOTH copies. Animate inside the existing picture immediately.

Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected Christmas village picture is PLAYING across the wall shown in the starting frame behind the bed and the whole tray ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a snug mountain-lodge bedroom with a high TRAY CEILING: a large flat rectangular raised central panel, a sloping border on all four sides and a lower flat perimeter ledge, with no ridge or beams. A walnut bed with a low square upholstered headboard is centred on a flat back wall between two rectangular windows, cream bedding with a deep forest-green quilt, walnut bedside chests, smoked-walnut floorboards and a cream wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE BOY - exactly one child, a boy of about five with deep brown skin and short tightly curled black hair, fully dressed for winter in a forest-green brushed-cotton Christmas pyjama set patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall shown in the starting frame and the whole tray ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The supplied starting frame already has the complete projection at full brightness. Continue motion inside that existing picture immediately; no fade-in or gradual appearance. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE DRAWINGS - animated flat smoke curls rise within the projected cottage drawings on the wall, leaning right and changing shape while new drawn curls form below. These are pixels on plaster, not real smoke or haze in the room.
- THE RISING SPARK DRAWINGS - flat gold pixels climb along the wall from the illustrated village chimneys toward the painted star field at roughly one roof height each half-second. They are part of the projected wall movie, with no real sparks, airborne trails or particles between the camera and the wall.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about half of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a quarter of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE EXISTING VILLAGE FIGURES AND THE ELVES. Existing bakery elves walk, lift gingerbread gifts and pass them along the village; the existing gingerbread figures wave and move. They continuously change position at real-time speed.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about half of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE PROJECTED ORNAMENT DRAWINGS - the tiny elves keep passing gifts within the flat wall illustration beside the log-cabin depot. Flat bauble and candy-cane drawings translate and turn along the wall and ceiling planes; they have no depth in the real room. Big gold bell drawings swing visibly side to side within the same projected surface, their clapper drawings moving inside them. All obey surface perspective and architectural occlusion.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - these are strictly flat two-dimensional moving light marks on plaster, never physical flakes. On the ceiling they glide tangentially ALONG each ceiling surface toward its edge or wall seam, following its perspective; they never fall away from the ceiling into the room. On the walls they translate downward along the wall at about one quarter wall-height per second. At a wall-ceiling corner their path bends onto the adjoining surface and remains flush with it; behind the real boy, bed, headboard and beams they are occluded and disappear, never drawn over those objects. Keep their projected scale tied to the surface, with no foreground enlargement, blur, depth or free-space parallax. Every flake stays visibly attached to one architectural plane in every frame.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the wall shown in the starting frame and the tray ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the tray ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The raised tray centre, four sloping borders and flat stepped perimeter remain stationary. Drawings fold at each plane change and stretch down sloping borders; no ridge or tie beams are added. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing illustrated elves walk, lift gingerbread gifts and pass them through the bakery village; bakery windows flicker naturally, existing gingerbread figures wave and move. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v16_c07_g1.png` → `clips/v16_c07_g1.mp4`

#### Image prompt — `starting_frames/v16_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `182f725f-9cf4-4ae1-91e8-3ad6af5cc43c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_150958_182f725f-9cf4-4ae1-91e8-3ad6af5cc43c.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
- @Image 2: `content/video_16_assets/references/v16_c05_r1.png` · Higgsfield media `decf983c-602d-4321-99e7-dfbc4755777d`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon; a boy of about five with deep brown skin and short tightly curled black hair. Both fully dressed in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two broad roof slopes, straight ridge and three solid oak tie beams remain legible. The sleigh and ribbon trail fold cleanly over the ridge. Each beam receives its own offset slice of the projected picture on its visible faces and casts a narrow hard-edged shadow behind it. The tall fieldstone chimney divides the picture at its projecting corners and irregular stone faces; the large window and doorway reveals cut the image at their real edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the cream wool rug, the warm tan linen sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the charcoal fieldstone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v16_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `a245e6a3-ccec-4124-bd01-5ec1ec549148`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_191351_a245e6a3-ccec-4124-bd01-5ec1ec549148.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v16_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_16_assets/starting_frames/v16_c07_g1.png` · Higgsfield media `182f725f-9cf4-4ae1-91e8-3ad6af5cc43c`

````text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, pitched ceiling with oak tie beams with oak tie beams panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected Christmas village picture is PLAYING across the back wall and the entire pitched ceiling with oak tie beams with oak tie beams and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a spacious double-height mountain-lodge Christmas great room with a high PITCHED CEILING: two broad smooth plaster slopes meet at one straight ridge and are crossed by three large natural-oak tie beams with square edges. A tall charcoal fieldstone chimney breast stands on the back wall with a thick oak mantel; a broad triangular-topped window occupies the left wall and a rectangular opening sits on the right. Smoked-walnut floorboards, a large warm tan linen sectional sofa, a rectangular tan upholstered ottoman and a cream wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with deep brown skin and short tightly curled black hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about nine with deep brown skin and shoulder-length black curls gathered with a cream ribbon, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in forest-green brushed-cotton Christmas pyjama sets patterned with tiny red gingerbread houses, candy canes and white snowflakes, with matching loose pyjama trousers and cream wool socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole pitched ceiling with oak tie beams with oak tie beams. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a magical GINGERBREAD CHRISTMAS BAKERY VILLAGE: richly detailed gingerbread cottages with white icing roof trim, crimson candy-cane pillars, glowing golden windows and evergreen wreaths; friendly elves in red coats carry gingerbread stars and ribboned Christmas parcels outside Santa's bustling gift bakery. A giant decorated fir tree stands in the village square, surrounded by wrapped red and gold presents and little gingerbread families wearing winter scarves. Along the upper walls, arching candy canes, gold bells, holly and red ribbon garlands connect the entire scene. ACROSS THE CEILING, Santa's glowing red sleigh and eight reindeer soar past a gold Christmas star, followed by curved scarlet ribbon trails, crisp white snowflakes and small shining golden ornaments. Unmistakably Christmas Eve: candy red, warm gold and dark fir green dominate against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. 

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
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the pitched ceiling with oak tie beams with oak tie beams fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their cotton pyjamas read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; a ribbon that sits still; a sleigh and reindeer parked in one place; a existing illustrated villagers and toy/train procession that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the pitched ceiling with oak tie beams with oak tie beams or an un-animated ceiling detail in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the existing illustrated villagers and toy/train procession advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - The two pitched roof planes and three solid oak tie beams remain stationary. Drawings fold over the ridge, split across source-facing beam surfaces and reappear offset beyond them; stone chimney corners and triangular window reveals interrupt the projection. All physical architecture stays stationary.

CURRENT BRIEF — STRONG CONTINUOUS MOTION: The existing illustrated elves walk, lift gingerbread gifts and pass them through the bakery village; bakery windows flicker naturally, existing gingerbread figures wave and move. Preserve the artwork already visible. Every illustrated chimney emits fresh curling smoke continuously, moving at least one chimney height per second; the sleigh crosses a substantial part of the ceiling with galloping reindeer. Existing ribbon light fields carry clearly travelling aurora-like waves along their length, with brightness crests moving rather than blinking in place. Do not add a new aurora object where none exists; animate the existing sky and ribbon shapes. The house structures and central star stay anchored while characters, vehicles, smoke and light waves travel independently. The only physical motion in the room is the specified children and camera; all Christmas artwork and illustrated smoke remain flat light on real wall/ceiling surfaces. No floating 3D objects. No frozen opening or ending. Use the exact architecture and artwork in this shot's references; animate only illustrated characters actually present, never invent source-template deer or rabbits. Natural room audio only, no music.
````
