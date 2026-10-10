# Video 21 - image archive

**Current status (2026-09-24):** B-roll start frames C02–C07 plus the C05 room reference (r1) and its empty-room edit (r2) generated (one generation each), saved and on the board as FRAME FOR REVIEW. C01 hook frame approved; clip g1 rejected 2026-09-25, re-roll g2 on the board as CLIP FOR REVIEW. Nothing animated.

**Settings:** Higgsfield `gpt_image_2_5`; variant `sunburst`; resolution `2k`; quality `medium`; aspect_ratio `9:16`; count `1` per image.

## Reusable blocks
Every prompt is the video 20 verified-record prompt of the same slot, pasted verbatim with only the physically different nouns replaced (English Arts-and-Crafts set), with the same geometry references and settings. Improvements carried over: projection covers the whole ceiling and all wooden trim, C07 is a different room from C05, and a children-free room reference (r2) is made up front so the C05 clip never copies the kids' reference poses. All submitted prompts were checked byte-identical against the Higgsfield job records.

## C02 - Hands on the box
**Frame:** `starting_frames/v21_c02_g1.png`
**Clip:** `clips/v21_c02_g1.mp4`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `202d4a72-692f-4460-be7e-108d47ed4044`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

### Image prompt
````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 35, with warm tan skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a forest-green chunky cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive English country dining room with sage-green painted panelled walls, a carved white-painted wooden fireplace hung with red plaid stockings, a brass-framed oval mirror, a painted pine dresser displaying blue-and-white plates and a Christmas tree dressed with red plaid bows, gingerbread ornaments and warm white fairy lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few red holly berries, two or three small red and gold glass baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Video prompt
**Clip:** `clips/v21_c02_g1.mp4` — take 1, generated 2026-09-24, unreviewed.
**Settings:** seedance_2_5 · mode omni_reference · 720p · 4 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job ID:** `dfa2191f-4977-489f-9619-7f4cc799be4b`
**Attached:**
- start_image: `starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`
- @Image 1 (image reference): `starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`
**Result:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022208_dfa2191f-4977-489f-9619-7f4cc799be4b.mp4 · md5 `b7c0927e90b098abf0feb6768f9add0c` (downloaded byte-identical) · 720,1280,24/1 · 4.050000
**Lineage:** Reused from v20 C02 take 2 (verified record, APPROVED) - the version with the 'ONE CONTINUOUS TAKE - ABSOLUTE RULE' added after Daniel rejected v20 take 1 for a cut. Only the physically different nouns changed: sleeve, table, props and dining room. Start frame attached as start_image and as image reference, as in v20.

````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 4-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no zoom, no reframe. Every stage of the box opening is shown happening - the flap lifting, folding back and the hand reaching in - never skipped. The box, hands and table stay continuous frame to frame.

STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a forest-green chunky cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge fills the frame. The lit cream candle, fir sprigs, red holly berries, small red and gold glass baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive English country dining room with sage-green painted panelled walls, a carved white-painted wooden fireplace hung with red plaid stockings, a brass-framed oval mirror, a painted pine dresser displaying blue-and-white plates and a Christmas tree dressed with red plaid bows, gingerbread ornaments and warm white fairy lights. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge, lid flaps folded back. The printed front artwork, candle, fir, baubles, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

### Take history
- `starting_frames/v21_c02_g1.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C02 verified record — changed: hands (woman ~35, warm tan skin, forest-green cable-knit sleeves), bleached-oak table, English country dining room (sage panelling, blue-and-white plates).
- `clips/v21_c02_g1.mp4` - take 1, generated 2026-09-24, unreviewed.


## C03 - The projector lifted
**Frame:** `starting_frames/v21_c03_g1.png`
**Clip:** `clips/v21_c03_g1.mp4`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `5038db7d-ab48-4d9f-af51-249dfbee0a98`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
- @Image 2: `content/video_21_assets/starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`

### Image prompt
````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with warm tan skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a forest-green chunky cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same forest-green chunky cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C02 and owns the new woman's hands, sweater, photographic look and full-size carton-to-projector scale; the projector should plausibly fill that carton when unpacked; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Video prompt
**Clip:** `clips/v21_c03_g1.mp4` — take 1, generated 2026-09-24, unreviewed.
**Settings:** seedance_2_5 · mode omni_reference · 720p · 4 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job ID:** `3cab83e5-fbc0-4955-973a-f285275c3779`
**Attached:**
- start_image: `starting_frames/v21_c03_g1.png` · Higgsfield media `5038db7d-ab48-4d9f-af51-249dfbee0a98`
**Result:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022302_3cab83e5-fbc0-4955-973a-f285275c3779.mp4 · md5 `31979de1361f943e9572610500e862be` (downloaded byte-identical) · 720,1280,24/1 · 4.042000
**Lineage:** Reused from v20 C03 take 1 (verified record, APPROVED) - only sleeve, countertop material and kitchen changed.

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in forest-green chunky cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy; behind it deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the quartz. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the quartz in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the quartz.
3.0-3.4s - the four feet of the stand touch the quartz; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the quartz, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### Take history
- `starting_frames/v21_c03_g1.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C03 verified record — changed: hands (woman ~35, warm tan skin, forest-green cable-knit sleeves), white quartz counter, forest-green shaker kitchen with zellige backsplash.
- `clips/v21_c03_g1.mp4` - take 1, generated 2026-09-24, unreviewed.


## C04 - The cable going in
**Frame:** `starting_frames/v21_c04_g1.png`
**Clip:** `clips/v21_c04_g1.mp4`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `e4cd729b-bb65-42ba-8817-3ae44ca10657`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`
- @Image 2: `content/video_21_assets/starting_frames/v21_c03_g1.png` · Higgsfield media `5038db7d-ab48-4d9f-af51-249dfbee0a98`

### Image prompt
````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with warm tan skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a forest-green chunky cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C03 and owns the enlarged product's physical dimensions relative to the hands, exact product identity, kitchen finishes, hands, sweater and photographic look; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Video prompt
**Clip:** `clips/v21_c04_g1.mp4` — take 1, generated 2026-09-24, unreviewed.
**Settings:** seedance_2_5 · mode omni_reference · 720p · 4 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job ID:** `06f2ac72-2057-43d6-840b-e612a5521f1c`
**Attached:**
- start_image: `starting_frames/v21_c04_g1.png` · Higgsfield media `e4cd729b-bb65-42ba-8817-3ae44ca10657`
**Result:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022359_06f2ac72-2057-43d6-840b-e612a5521f1c.mp4 · md5 `23ef1cc82a01056e04416422f328a08b` (downloaded byte-identical) · 720,1280,24/1 · 4.050000
**Lineage:** Reused from v20 C04 take 1 (verified record, APPROVED) - only sleeve, countertop material and kitchen changed.

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
THE LEFT HAND - a woman's hand in a forest-green chunky cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same forest-green chunky cable-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy; behind it deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the quartz and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the quartz around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the quartz immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### Take history
- `starting_frames/v21_c04_g1.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C04 verified record — changed: hands (woman ~35, warm tan skin, forest-green cable-knit sleeves), white quartz counter, forest-green shaker kitchen with zellige backsplash.
- `clips/v21_c04_g1.mp4` - take 1, generated 2026-09-24, unreviewed.


## C05 - The door opens on the room — start frame
**Frame:** `starting_frames/v21_c05_g1.png`
**Clip:** `clips/v21_c05_g1.mp4`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `417cea70-8c6e-43c6-a99c-e068f223b4bd`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- @Image 2: `content/video_21_assets/starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`

### Image prompt
````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the forest-green chunky cable-knit wool sleeve and no jewellery, with warm tan skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear door surface visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the burgundy-red paint reads clearly as deep red, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Video prompt
**Clip:** `clips/v21_c05_g1.mp4` — take 1, generated 2026-09-24, unreviewed.
**Settings:** seedance_2_5 · mode omni_reference · 720p · 5 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job ID:** `7c9425b4-578c-492d-a0fc-deb71e9cdb3f`
**Attached:**
- start_image: `starting_frames/v21_c05_g1.png` · Higgsfield media `417cea70-8c6e-43c6-a99c-e068f223b4bd`
- @Image 1 (image reference): `references/v21_c05_r2.png` · Higgsfield media `95f8c0ab-4fd7-41c7-a379-76ae45dda0d2`
**Result:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022501_7c9425b4-578c-492d-a0fc-deb71e9cdb3f.mp4 · md5 `3e6b4367716f39b4df33069c1e650198` (downloaded byte-identical) · 720,1280,24/1 · 5.050000
**Lineage:** Reused from v20 C05 take 2 (verified record, APPROVED) - carries every C05 fix: EMPTY-room reference r2 (so the kids never copy a reference pose), 'EXACTLY TWO CHILDREN' with a per-second chase (no extra kids), the PROJECTED ANIMATION block with strong per-element motion (sleigh travels ~1/4 ceiling per second, smoke from every chimney, snowfall) and a closing MOTION GUARDRAILS line. Changed: door, sleeve, ceiling noun, children, pyjamas, room, projected scene and its moving elements (this video's village life replaces v20's cable car/sledges).

````text
CAMERA CONTINUITY - PRIMARY CORRECTION: the entire five seconds are ONE slow, uninterrupted forward-and-upward glide. Forward travel and upward aim are mechanically coupled as one motion, already underway together in frame zero. Keep the same gentle pace and the same forward-to-upward ratio for every frame, including while the door opens and while crossing its sill. Travel only about 0.8 metres forward over the entire shot, with an even upward tilt of about 18 degrees over those same five seconds. The wreath, door-panel edges and later the back-wall details drift smoothly downward in the frame from the beginning while perspective advances very gently. There is no forward-only phase and no later tilt-only phase. Never complete an entrance and then begin looking up. Do not accelerate the beginning, hurry through the door, ease in, ease out, steepen the tilt, speed-ramp or catch up to an end composition. The final frame can remain near the threshold with the back wall, furniture and ceiling visible; covering more distance or revealing the whole ceiling is not a goal. The door opens naturally during the same slow glide; its opening is not a camera cue. Preserve the same doorframe and room features across adjacent frames as the camera physically crosses the single sill. No cut, concealed edit, dissolve, match cut, scene replacement, teleport, jump or sudden perspective change. Maintain this single gentle motion unchanged until the clip ends.

CHILD MOVEMENT - PRIMARY CORRECTION: @Image 2 shows the room EMPTY. EXACTLY TWO CHILDREN exist in this clip - the girl and the boy described in this text - and nobody else ever appears: no third child, no extra kids in the background, on the sofa or in the doorway, no adult. There is no pose, spot or arrangement of them to copy, and they never stand still anywhere. They are already running a game of chase behind the closed door, and the chase never ends inside this clip. Per second:
0-1s: in the very first gap of the opening door the girl is already running, caught mid-stride crossing the gap from left to right, one foot off the floor; the boy runs two strides behind her.
1-2s: both run a wide curve across the rug away from the camera, arms swinging; the boy throws one arm up and points at the flying sleigh on the ceiling while still running.
2-3s: the girl spins round once while running, arms out, laughing up at the ceiling; the boy runs round the ottoman after her.
3-4s: the girl runs past the Christmas tree toward the right-hand side of the room; the boy chases two strides behind at a different depth.
4-5s: both are still running mid-stride when the clip ends, the girl near the right edge of the frame, the boy crossing the rug behind her.
They are never side by side, never face the camera, never pause, never stop in front of the sofa. This child action must not alter the camera movement specified above.

DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Image 2. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high coffered ceiling meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim fully closed with a wreath, a hand on the brass knob. @Image 2 is a reference photo of the EMPTY room for the layout, coffered ceiling, furniture, colours and projection artwork appearance; it contains no people. Use only the single continuous camera move and child actions specified in this prompt; the room still supplies appearance only. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED ANIMATION - THE MAIN SUBJECT. The Christmas picture on the walls and ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, not a still illustration; only the projected picture is animated, while the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in every frame from the first to the last, independent of the camera. The architecture, the workshops, the barn and the moon stay put; everything else drawn in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is not parked with only its legs moving. It flies in one smooth sweeping arc, flying from where it is first seen across the coffered ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place on the ceiling every second and has crossed most of the ceiling by the end. While it travels the reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY workshop chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from the chimney below. Several plumes are clearly rising at once, all the time.
- SKY: the huge golden full moon glows and its halo pulses brighter and dimmer; the drifting snowflakes swirl across the ceiling; the golden stars twinkle; now and then a shooting star streaks across.
- VILLAGE LIFE: the little red steam train chugs steadily along its snowy track pulling its wagons of presents, puffing white steam; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock toss their heads and trot.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall, flat on the wall and ceiling surfaces.
- LIGHTS: bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (5 s):
0-1s: the door opens onto the room; through the gap the sleigh is already flying and smoke is already rising from the workshop chimneys.
1-2s: the sleigh team travels across the coffered ceiling, clearly changing position, reindeer galloping; smoke columns climb the wall; the steam train chugs along its track; snow drifts down.
2-3s: the sleigh has moved on a quarter of the ceiling past the beams; the snowflakes swirl; the elves hammer in the workshop windows.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; a shooting star streaks across.
4-5s: all of it still moving at the same pace in the final frame - sleigh flying, smoke rising, train chugging, snow falling.
All of this is flat projected light lying on the real plaster, wall panelling and window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CONTINUOUS ACTION, NOT CAMERA PHASES
0.0-5.0s - ONE identical slow forward-and-upward glide continues for the full duration, already underway at frame zero. The view rises gently while moving forward at the same steady ratio throughout. During approximately the first 1.5 seconds the hand turns the knob and opens the door with a smooth, ordinary unhurried push, never a quick shove or a fast reveal. The camera does not wait for the door, rush through it, pause for the room, change speed at the sill, or start a new movement afterward. The closed-door frame and the revealed room belong to the same continuous physical shot. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap. Cross only the single thin threshold directly into the living room; no intervening space. There is no stop at the sofa or separate ceiling reveal. The shot ends during that same gentle glide, with back wall, furniture and ceiling still visible. All through it the smoke pours from every chimney, the sleigh flies on across the ceiling, the existing illustrated steam train and busy elves keep moving, the workshop windows flicker, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl, about five with warm brown skin and long black braids tied with small gold beads, runs a broad curving path across the rug and alongside the sofa; the boy, about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue the same open-ended curving chase naturally around the available floor space, curving away from furniture and each other; this is not a loop that returns them to a reference pose. During the final 1.5 seconds the girl continues around the right-hand edge of the rug while the boy follows two running strides behind, with their bodies at different depths and turned along their route. The girl can leave the frame at the side while still running and the boy keeps following; neither child is required to remain centred or fully visible. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. While running, the boy throws one arm up and points at the flying sleigh and the golden full moon on the ceiling, and the girl looks up in delight mid-stride, but their feet keep stepping and their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, a steady natural phone glide. One constant slow forward-and-upward movement, both components active together from frame zero through frame last, with the same gentle speed and same ratio throughout. No opening rush, acceleration, easing, speed ramp, phase change, level hold, delayed upward tilt, pitch jump, reframe, stop, second move, cut, concealed edit, dissolve, teleport, zoom, orbit, fisheye or lens warping. The camera is the person's eyes; no phone, screen or device in frame.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

REFERENCE-ONLY LOCK - @Image 2 is a still photograph of the EMPTY room. It supplies architecture, furniture, colours and projected artwork appearance ONLY. It is not an end frame, camera target or transition destination; never dissolve, cut, morph or snap into its composition. Only the closed-door @Image 1 defines frame zero. The two children come only from the text above and are running from the first gap to the last frame; no other people ever appear. The new clip is exactly 5 seconds and has no end frame or driving video.

ROOM AND IDENTITY - a spacious double-height English Arts-and-Crafts Christmas great room with a high COFFERED CEILING: a broad flat plaster ceiling divided into a deep grid of square recessed coffers by crisp white-painted wooden beams. Sage-green painted wooden wall panelling lines the walls. A tall chimney breast of honey-coloured limestone stands on the back wall with a carved oak mantel; two tall casement windows with white-painted wooden frames and slim glazing bars occupy the left wall and a wide round-arched doorway with a white-painted wooden casing sits on the right. Wide honey-oak floorboards, a large rust-orange velvet sectional sofa, a round tan leather ottoman and a soft cream wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about five with warm brown skin and long black braids tied with small gold beads; a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut. Both fully dressed in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Preserve the architecture from @Image 2; the children's appearance comes from this text only.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

BANNED - a third child or any extra children appearing anywhere, at any moment; an adult; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; any camera acceleration or speed ramp; treating the room reference as a destination; either child standing still, frozen, posed or waiting at any moment, including in the first gap of the door; either child climbing onto the sofa; the two children side by side or facing the camera; a glow or bright seam along the door edge; light that grows or fills the room as the door opens; the projector unit visible; blur; a cut.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the steam train or the elves do not move; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture rotates or slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````

### Take history
- `starting_frames/v21_c05_g1.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C05 verified record — changed: hands (woman ~35, warm tan skin, forest-green cable-knit sleeves), door (deep burgundy-red four-panel door).
- `clips/v21_c05_g1.mp4` - take 1, generated 2026-09-24, unreviewed.


## C05 F2 - The door opens on the room — room reference
**Frame:** `references/v21_c05_r1.png`
**Clip:** none yet
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`
**References:**
- @Image 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`

### Image prompt
````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut; the girl is of about five with warm brown skin and long black braids tied with small gold beads. Both children are fully dressed for winter in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height English Arts-and-Crafts Christmas great room with a high COFFERED CEILING: a broad flat plaster ceiling divided into a deep grid of square recessed coffers by crisp white-painted wooden beams. Sage-green painted wooden wall panelling lines the walls. A tall chimney breast of honey-coloured limestone stands on the back wall with a carved oak mantel; two tall casement windows with white-painted wooden frames and slim glazing bars occupy the left wall and a wide round-arched doorway with a white-painted wooden casing sits on the right. Wide honey-oak floorboards, a large rust-orange velvet sectional sofa, a round tan leather ottoman and a soft cream wool rug. Seen from the doorway; the new a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, copper and cream baubles, dried orange slices, plaid ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cream-and-rust knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The deep coffered ceiling remains clearly three-dimensional, its white-painted beams crossing in a crisp square grid. The sleigh and the ceiling picture continue straight across every beam face and underside and down into each recessed coffer, folding at the beam edges with correct offsets, before continuing onto the walls. The tall chimney breast receives a continuous picture with clear folds at its two projecting corners. The white-painted wooden window frames, glazing bars, doorway casing and wall panelling carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the soft cream wool rug, the rust-orange velvet sectional sofa, the round tan leather ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

NATURAL, LESS CINEMATIC LOOK - a little less cinematic than a film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster or an advert. True-to-life colour and contrast as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting and no heightened fantasy glow on the children. The projection is still dense, bright and colourful, but it reads as the real light of a home Christmas projector falling on real walls, and the shadows keep a little ordinary room detail.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the sage-green painted wooden panelling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### Video prompt
Not animated yet.

### Take history
- `references/v21_c05_r1.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C05 F2 verified record — changed: children (boy ~8 fair, freckles, sandy-blond; girl ~5 warm brown skin, black braids with gold beads; cranberry-red pyjamas with gingerbread men, candy canes, silver stars), room (COFFERED great room, sage-green panelling, limestone chimney breast, rust velvet sofa), projection (toy-workshop village, steam train, sleigh past a golden full moon), door (deep burgundy-red four-panel door).

## C05 F3 - The door opens on the room — empty-room reference
**Frame:** `references/v21_c05_r2.png`
**Clip:** none yet
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `95f8c0ab-4fd7-41c7-a379-76ae45dda0d2`
**References:**
- @Image 1: `content/video_21_assets/references/v21_c05_r1.png` · Higgsfield media `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`

### Image prompt
````text
Edit the supplied image. Reproduce it exactly - the same English Arts-and-Crafts Christmas great room, the same coffered ceiling, the same camera position, framing, lens and lighting, the same furniture, Christmas tree, fireplace, rug and the exact same projected Christmas artwork on the walls and ceiling, pixel for pixel wherever possible. The ONLY change: remove all children completely. The room is empty of people - no children, no adults, no pets. Where the children stood, show the floor, rug and sofa that were behind them, continuing naturally. Keep the projection, colours and sharpness unchanged. No text, no watermark.
````

### Video prompt
Not animated yet.

### Take history
- `references/v21_c05_r2.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C05 F3 verified record — changed: new prompt (same as v20 r2 with only the room name swapped): an edit of this video's r1 with the children removed, so the C05 clip has no child poses to copy.

## C06 - The bed bounce
**Frame:** `starting_frames/v21_c06_g1.png`
**Clip:** `clips/v21_c06_g1.mp4`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `15262a8d-8083-4414-b8e0-aca9abaed7b2`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
- @Image 2: `content/video_21_assets/references/v21_c05_r1.png` · Higgsfield media `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`

### Image prompt
````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same natural low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, fully dressed for winter in a cranberry-red brushed-cotton Christmas pyjama set patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a bright-proportioned English country bedroom with a high CATHEDRAL CEILING: two steep sloping plaster planes rise from the side walls to meet at a crisp central ridge. A white-painted iron bed with a tall arched headboard is centred on the flat back wall between two tall casement windows with white-painted wooden frames and slim glazing bars, white bedding with a rust-orange knitted throw, sage-green painted bedside chests, wide honey-oak floorboards and a soft cream wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and copper and cream ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two steep sloping ceiling planes remain clearly three-dimensional, meeting at a crisp central ridge. The sleigh and the ceiling picture fold at the ridge and are foreshortened along each slope before continuing down the walls. The flat wall, the white-painted wooden window frames and glazing bars and the arched iron headboard carry properly foreshortened portions of the same continuous projection across their faces. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the soft cream wool rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his cotton pyjama top catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

NATURAL, LESS CINEMATIC LOOK - a little less cinematic than a film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster or an advert. True-to-life colour and contrast as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting and no heightened fantasy glow on the children. The projection is still dense, bright and colourful, but it reads as the real light of a home Christmas projector falling on real walls, and the shadows keep a little ordinary room detail.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### Video prompt
**Clip:** `clips/v21_c06_g1.mp4` — take 1, generated 2026-09-24, unreviewed.
**Settings:** seedance_2_5 · mode omni_reference · 720p · 5 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job ID:** `fa36df2f-9828-4f1a-9943-ddcdf123eee1`
**Attached:**
- @Image 1 (image reference): `starting_frames/v21_c06_g1.png` · Higgsfield media `15262a8d-8083-4414-b8e0-aca9abaed7b2`
**Result:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022718_fa36df2f-9828-4f1a-9943-ddcdf123eee1.mp4 · md5 `3b6e6d0183c42c712b2b4cfc4989a1fa` (downloaded byte-identical) · 720,1280,24/1 · 5.050000
**Lineage:** Reused from v20 C06 take 5 (verified record, APPROVED - 'both of them are good') - carries every C06 fix: approved frame attached ONLY as image reference so the camera can start a little higher and tilt DOWN (opposite of C05/C07), starting 'only a little higher than @Image 1 - NOT far up', animation block first with fast streaming snow, sleigh a third of the ceiling per second and chimney smoke. Changed: ceiling noun, boy, pyjamas, bedroom, projected scene and its moving elements.

````text
PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas projection on the walls and the cathedral ceiling is a MOVING CARTOON FILM playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. In every second of the clip, big parts of the picture visibly move:
1. SNOWFALL - hundreds of big glowing projected snowflakes stream continuously down across the whole projection, over the walls and the ceiling, falling fast like a real snowstorm seen through a window, about half the wall height every second. They are flat light on the walls and ceiling, never real snow in the room. This constant streaming snow is the most obvious motion in the frame.
2. SANTA'S SLEIGH - Santa's red sleigh and eight reindeer FLY across the ceiling from one side to the other, clearly travelling and changing place every second, crossing about a third of the ceiling each second, reindeer legs galloping and the golden trail streaming behind. It is never parked in one spot.
3. CHIMNEY SMOKE - thick white smoke pours upward out of every chimney on the wall, puff after puff, rising and curling fast.
4. SKY - the huge golden full moon glows and its halo pulses brighter and dimmer; the drifting snowflakes swirl across the ceiling; the golden stars twinkle; now and then a shooting star streaks across.
5. VILLAGE - the little red steam train chugs along its snowy track pulling its wagons of presents; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock trot.
Only the buildings and the moon hold still; everything else in the projection moves all the time, from the first frame to the last. The room and the boy are real photographic phone footage; only the projected picture is animated.

CAMERA - ONE slow tilt from UP to DOWN, the opposite of the other clips in this set.
0.0s: the camera is aimed only a little higher than @Image 1 - NOT far up. The fully projected cathedral ceiling fills roughly the upper half of the frame, the projected wall and the top of the headboard fill the middle, and THE BOY is in the lower part of the frame, fully visible from head to feet, mid-jump. Every visible part of the ceiling is covered with the projection - no bare plaster anywhere.
0.0-4.0s: the camera tilts DOWN slowly and smoothly, like a calm parent filming.
4.0-5.0s: it eases to a stop exactly on the framing of @Image 1.
One continuous take: no cut, no zoom, no push-in, no pull-back, never a tilt up.

PER-SECOND ANIMATION TRACK (while the camera tilts down):
0-1s: snow streams down the whole projection; the sleigh is already flying across the ceiling; smoke pours from the workshop chimneys.
1-2s: the sleigh has flown a third of the way across the ceiling; the steam train chugs along its track.
2-3s: the sleigh flies on across the ceiling; fresh smoke puffs rise above the workshop roofs; the elves hammer in the workshop windows.
3-4s: the sleigh keeps flying toward the far side of the ceiling; a shooting star streaks across.
4-5s: snow still streaming, smoke still rising, sleigh still flying in the last frame.

THE BOY JUMPS AT REAL SPEED for all five seconds: quick springy bounces, about one full jump every 1.2 seconds. Each jump: knees bend, a fast push-off, a brief moment in the air, a fast drop under normal gravity, the mattress compressing and springing back; arms swinging, laughing. Never slow motion, never floaty.

Wholesome family Christmas scene, a child at home with his family at Christmas. Crisp real iPhone footage at night, handheld, real-time speed, sharp from first frame to last.

ASSET ROLES: @Image 1 is the approved still that controls a bright-proportioned English country bedroom with a high CATHEDRAL CEILING: two steep sloping plaster planes rise from the side walls to meet at a crisp central ridge. A white-painted iron bed with a tall arched headboard is centred on the flat back wall between two tall casement windows with white-painted wooden frames and slim glazing bars, white bedding with a rust-orange knitted throw, sage-green painted bedside chests, wide honey-oak floorboards and a soft cream wool rug. Preserve exact child identity, clothing, furniture, colours and the full projected artwork of @Image 1; its framing is the END framing of this clip.

SUBJECTS:
THE BOY - exactly one child, a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, fully dressed for winter in a cranberry-red brushed-cotton Christmas pyjama set patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall shown in @Image 1 and the whole cathedral ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in @Image 1. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

DO NOT INCLUDE: a still, frozen or printed-looking projection; a projection that only twinkles; a sleigh parked in one place; chimneys without smoke; snow that does not fall; a steam train and elves that do not move; bare, white or unprojected ceiling or wall; a camera that starts far up on the ceiling; a camera that tilts up; zoom, push-in or pull-back; slow-motion or floaty jumping; real snow or particles in the air of the room; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
````

### Take history
- `starting_frames/v21_c06_g1.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C06 verified record — changed: boy (boy ~8 fair, freckles, sandy-blond), room (CATHEDRAL-ceiling bedroom, white iron bed), projection (toy-workshop village, steam train, sleigh past a golden full moon).
- `clips/v21_c06_g1.mp4` - take 1, generated 2026-09-24, unreviewed.


## C07 - The whole Christmas room
**Frame:** `starting_frames/v21_c07_g1.png`
**Clip:** `clips/v21_c07_g1.mp4`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `5579aef2-ea00-428d-9f24-52a2f7736941`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
- @Image 2: `content/video_21_assets/references/v21_c05_r1.png` · Higgsfield media `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`

### Image prompt
````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the children only; this is a different room of the same house, described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about five with warm brown skin and long black braids tied with small gold beads; a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut. Both fully dressed in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height English country Christmas family room with a high TRAY CEILING: a broad flat raised centre surrounded by four gently sloping plaster border planes and a wide flat perimeter ledge with crisp stepped moulding. White-painted tongue-and-groove panelling lines the walls. A tall chimney breast of red brick stands on the back wall with a dark oak beam mantel; a wide bay of casement windows with white-painted wooden frames and slim glazing bars fills the left wall and a pair of white-painted wooden French doors sits on the right. Wide honey-oak floorboards, a large moss-green corduroy sectional sofa, a square tan leather ottoman and a soft rust-and-cream striped wool rug. A different room from @Image 2 - not the same living room - seen from the middle of the family room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, copper and cream baubles, dried orange slices, plaid ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cream-and-rust knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The raised flat centre, the four sloping border planes and the stepped perimeter ledge remain clearly three-dimensional, meeting at crisp moulded edges. The sleigh and the snowflakes bend at every edge of the tray and are foreshortened along each sloping border before continuing onto the walls. The tall chimney breast receives a continuous picture with clear folds at its two projecting corners. The white-painted wooden window frames, glazing bars, French doors and tongue-and-groove panelling carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the soft rust-and-cream striped wool rug, the moss-green corduroy sectional sofa, the square tan leather ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

NATURAL, LESS CINEMATIC LOOK - a little less cinematic than a film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster or an advert. True-to-life colour and contrast as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting and no heightened fantasy glow on the children. The projection is still dense, bright and colourful, but it reads as the real light of a home Christmas projector falling on real walls, and the shadows keep a little ordinary room detail.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the white-painted tongue-and-groove panelling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### Video prompt
**Clip:** `clips/v21_c07_g1.mp4` — take 1, generated 2026-09-24, unreviewed.
**Settings:** seedance_2_5 · mode omni_reference · 720p · 4 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job ID:** `a72a0ad2-168f-44de-8109-1e74b04ff418`
**Attached:**
- start_image: `starting_frames/v21_c07_g1.png` · Higgsfield media `5579aef2-ea00-428d-9f24-52a2f7736941`
**Result:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022843_a72a0ad2-168f-44de-8109-1e74b04ff418.mp4 · md5 `59ba2ec04636c984e7e0b5b982f842da` (downloaded byte-identical) · 720,1280,24/1 · 4.050000
**Lineage:** Reused from v18 C07 take 3 (verified record, APPROVED) rather than v20 C07 take 1, because v18 take 3 is the version with all of Daniel's C07 fixes: one PROJECTED ANIMATION block with big per-element motion (take 2 fix: 'smoke out of the chimneys, sleigh in motion, aurora in motion') and the tilt-up that stops before the edge of the projected picture with the whole ceiling covered (take 3 fix: 'no projected animation on a big part of the ceiling toward the end'). Changed: room, ceiling nouns and SURFACE MAPPING for this video's ceiling, children (labels THE BOY / THE GIRL), pyjamas, projected scene; the aurora bullet became this video's sky motion.

````text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, tray ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas family room while a projected Christmas village picture is PLAYING across the back wall and the entire tray ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a spacious double-height English country Christmas family room with a high TRAY CEILING: a broad flat raised centre surrounded by four gently sloping plaster border planes and a wide flat perimeter ledge with crisp stepped moulding. White-painted tongue-and-groove panelling lines the walls. A tall chimney breast of red brick stands on the back wall with a dark oak beam mantel; a wide bay of casement windows with white-painted wooden frames and slim glazing bars fills the left wall and a pair of white-painted wooden French doors sits on the right. Wide honey-oak floorboards, a large moss-green corduroy sectional sofa, a square tan leather ottoman and a soft rust-and-cream striped wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE BOY - a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE GIRL - a girl of about five with warm brown skin and long black braids tied with small gold beads, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole tray ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

PROJECTED ANIMATION - THE MAIN SUBJECT. The Christmas picture on the walls and ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, not a still illustration; only the projected picture is animated, while the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in every frame from the first to the last, independent of the camera. The architecture, the workshops, the barn and the moon stay put; everything drawn around them travels.
- MOON AND SNOW SKY: the huge golden full moon glows and its halo pulses brighter and dimmer; big drifting snowflakes swirl in wide visible eddies across the whole tray ceiling; the golden stars twinkle; now and then a shooting star streaks across.
- SANTA'S SLEIGH AND EIGHT REINDEER: the team FLIES. It travels in one smooth sweeping arc across the ceiling, starting where it sits in the start image and flying past the huge golden full moon and on across the tray ceiling, covering about one quarter of the ceiling's width every second, so it is in a clearly different place every second. The reindeer's legs gallop in a running cycle, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY workshop chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from the chimney below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the little red steam train chugs steadily along its snowy track pulling its wagons of presents, puffing white steam; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock toss their heads and trot.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall, flat on the wall and ceiling surfaces.
- LIGHTS: bright gold sparkle waves travel along the garlands and ribbons; stars twinkle; now and then a shooting star streaks across the ceiling.
PER-SECOND ANIMATION TRACK (4 s):
0-1s: snowflakes are already swirling across the tray ceiling; the sleigh team is already flying, reindeer galloping; smoke rises from every workshop chimney on the back wall; the steam train chugs along its track.
1-2s: the sleigh has moved a quarter of the ceiling and is crossing the golden moon; snow drifts down the walls; the elves hammer in the workshop windows.
2-3s: as the camera tilts up the moon's halo pulses and the snowflakes swirl; the sleigh flies on past the moon.
3-4s: the sleigh keeps flying toward the far side of the tray ceiling, snow still swirling, smoke still rising, the train still chugging, a shooting star streaking across - all moving in the final frame.
All of this is flat projected light lying on the real plaster, trim and window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE GIRL bounces on the sofa cushions with both arms up, laughing. THE BOY turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE GIRL pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE BOY keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree, only far enough that the tray ceiling fills the upper half of the frame - it never tilts past the projected picture. The ENTIRE tray ceiling - the raised flat centre, the four sloping border planes and the stepped perimeter ledge - is covered with the projection: starry midnight sky, the golden full moon, the swirling snowflakes and the sleigh - no bare white plaster, no unprojected centre, border or moulding anywhere in view; the ribbons rippling along it, the travelling gold light waves spreading outward from the moon and the sleigh team still flying on across the ceiling. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their cotton pyjamas read clearly. One continuous take with no cut. The camera makes one move per beat and no more. THE GIRL stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: bare, blank, white or partly unprojected tray ceiling, border plane, ledge or wall in any frame, especially at the end when the camera looks up; a camera that tilts up beyond the projected picture; a projection appearing, fading in or revealing itself; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; blur; a cut; on-screen text; subtitles.

SURFACE MAPPING - The raised flat centre, the four sloping border planes and the stepped perimeter ledge of the tray ceiling remain stationary. Drawings bend at every edge of the tray, fold around the red-brick chimney corners and carry across the white-painted window frames, glazing bars, French doors and tongue-and-groove panelling, with correct surface perspective and occlusion. All physical architecture stays stationary.

MOTION GUARDRAILS - Failed if: the snowflakes do not swirl or the moon's halo never pulses; the sleigh stays in one place; any chimney has no rising smoke; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture rotates or slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````

### Take history
- `starting_frames/v21_c07_g1.png` — g1, generated 2026-09-24, unreviewed.
- Reused from v20 C07 verified record — changed: children (boy ~8 fair, freckles, sandy-blond; girl ~5 warm brown skin, black braids with gold beads; cranberry-red pyjamas with gingerbread men, candy canes, silver stars), room (TRAY-ceiling family room, red-brick chimney, moss-green sofa), projection (toy-workshop village, steam train, sleigh past a golden full moon).
- `clips/v21_c07_g1.mp4` - take 1, generated 2026-09-24, unreviewed.


## C01 - Hook — Painting the Christmas mural (new hook)

**Frame:** `starting_frames/v21_c01_g1.png`
**Clip:** `clips/v21_c01_g2.mp4` (CLIP FOR REVIEW; g1 rejected)
**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job ID:** `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
**References:**
- @Image 1: `content/video_21_assets/references/v21_c01_r1.png` · Higgsfield media `3a196b34-d0c6-4f5a-9272-69f66c3843b2`
- @Image 2: `content/video_21_assets/starting_frames/v21_c07_g1.png` · Higgsfield media `5579aef2-ea00-428d-9f24-52a2f7736941`

### Image prompt
Exact text in the verified record below (`### C01`).

### Video prompt
Exact text in the verified record below (`### C01`).

### Take history
- `starting_frames/v21_c01_g1.png` — generated 2026-09-24, one generation, FRAME FOR REVIEW.
- New prompt (no source shot). Daniel's brief 2026-09-24: in the style and framing of his attached screenshot (man on a ladder painting a Christmas mural, woman on the floor painting), slightly similar look, more space at the top for the caption, different man, woman and room. Reference `references/v21_c01_r1.png` = Daniel's screenshot exactly as attached (348×622 RGBA, md5 cc5bb899bccaaea194f24af516588240, caption "Christmas decor in 1986" + emoji visible in it), uploaded to Higgsfield as media `3a196b34-d0c6-4f5a-9272-69f66c3843b2`. @Image 2 = this video's C07 frame as the Arts-and-Crafts palette, the same role v17 C01 gave its own C07.
- Frame APPROVED 2026-09-24: Daniel asked for it to be animated.
- `clips/v21_c01_g1.mp4` — seedance_2_5, one generation, job `a5c6ea61-0e81-444a-81a2-92d2b8ef3b4d`, CLIP FOR REVIEW. New clip prompt, built from Daniel's reference clip `references/v21_c01_r2.mp4` (his upload `hook.mp4`, 1080×1920 HEVC, 3.11 s, 30 fps, WITH audio (AAC), md5 6662c5cd77bd8c3bc5a5b2adb49316d5; Higgsfield media `bc765eba-1c9c-4bf7-bc9f-ce21d57006b6`). Beats read off the reference at 6 fps: 0–0.5 s painting; 0.5–1.7 s foot slips, he leans into the wall and the red tin smears a vertical streak down the mural while the ladder slides out; 1.8–2.4 s he drops face-down on the floor left of the woman, ladder on his legs; 2.4–3.1 s red paint floods the floor toward the camera, tin rolls toward the lens, woman turned round in shock. Structure (START FRAME LOCK, HARD RULE, fall-weight paragraph, speed ban, FALL AND FRAMING LOCK) taken from v18 C01 g3.
- FAILED, no file: job `f292be42-fddb-48f4-86f7-bf5c22d2854b` — same prompt plus a MOTION REFERENCE paragraph, with `references/v21_c01_r2.mp4` attached as video_references (@Video 1). Higgsfield returned status `ip_detected` and produced nothing: the real TikTok clip (real people, burned-in caption) was blocked. Re-run once without the video reference and without that paragraph - that is the job in the cut. Exact failed prompt in the verified record.
- `clips/v21_c01_g1.mp4` — Daniel 2026-09-25: REJECTED — "it doesn't make sense, paint appears magically from his right hand, he has the paint bottle in the left hand".
- `clips/v21_c01_g2.mp4` — seedance_2_5, one generation, job `4e76e56a-bdef-4338-b64e-69016b9701cb`, CLIP FOR REVIEW. Re-roll of g1 on the same approved frame, same settings. Changed (prompt edit only): the 0.6-1.6s line now has him throw his LEFT hand, the one gripping the open tin, against the wall, the tin's mouth pressed to the mural making the streak, and says his RIGHT hand holds only the brush and leaves no paint; added a PAINT SOURCE sentence after the paint-realism sentence (every drop comes out of the one tin in his left hand, no paint from the right hand, the brush or nowhere). Reason: Daniel's rejection of g1.

## Re-roll C05 — 2026-09-25

- `clips/v21_c05_g1.mp4` — Daniel 2026-09-25: REJECTED — "one kid magically appears" (the boy runs out of view behind the sofa and pops back up by the fireplace at about 3.2 s). It had already been upscaled; `clips/upscaled/v21_c05_g1.mp4` stays on disk as the old take's upscale.
- `clips/v21_c05_g2.mp4` — seedance_2_5, one generation, job `313436fd-e789-446c-8441-e7e50a5d5723`, CLIP FOR REVIEW. Re-roll of g1 on the same start frame and room reference, same settings (720p, 5 s, omni_reference). Changed, prompt edit only: added a VISIBILITY sentence to CHILD MOVEMENT (each child stays visible from the door gap to the last frame, never runs behind the sofa, ottoman, tree or door, never leaves and re-enters the frame); replaced "The girl can leave the frame at the side while still running and the boy keeps following; neither child is required to remain centred or fully visible." with "Both children stay inside the frame and in full view until the last frame; neither is required to be centred."; added "a child popping into view that was not visible a moment before; a child vanishing behind furniture;" to BANNED.
- `clips/v21_c05_g2.mp4` — Daniel 2026-09-25: REJECTED — "I don't want the kids to be right in front of the doors when the door opens; the rest is perfect."
- `clips/v21_c05_g3.mp4` — seedance_2_5, one generation, job `38a7f121-94b5-47df-b5cc-b34b5283e52f`, CLIP FOR REVIEW. Re-roll of g2, same start frame, reference and settings. Changed, prompt edit only: the CHILD MOVEMENT 0-1s line "in the very first gap of the opening door the girl is already running, caught mid-stride crossing the gap from left to right, one foot off the floor; the boy runs two strides behind her." became "when the door opens the two children are already running well inside the room, at least three metres from the door, on the open floor across the rug - never right in front of the door and never close to the camera; the girl is mid-stride, one foot off the floor, and the boy runs two strides behind her."; BANNED gained "either child right in front of the door or close to the camera as it opens;" at its start.
- Daniel 2026-09-25: "For V21 C5 - we will use g2". `clips/v21_c05_g2.mp4` is APPROVED and in the cut (despite the note above on the kids at the door); `clips/v21_c05_g3.mp4` stays on disk, not used.

## Upscales

Approved clips upscaled 2026-09-25 on higgsfield.ai/upscale (Chrome extension), Daniel's exact settings. Each upscale keeps its source's exact name in `clips/upscaled/`; each download is byte-identical to the Higgsfield result (md5 of the download = file on disk). Settings were read back off the page before every submit.

C01 hook: **ByteDance Upscale · Model version Pro · Resolution 2K · FPS 30 fps · Preset AIGC**

| Upscale file | Source clip | Source md5 | Upscale job | Result | md5 | Output |
|---|---|---|---|---|---|---|
| `clips/upscaled/v21_c01_g2.mp4` | `clips/v21_c01_g2.mp4` | `c41e8458b5fb126fa9a66d2ce5a4a295` | `e05b8acd-915c-47f6-a0f5-82cff441aba5` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_212307_c1b4d54f-d12f-478a-ae89-c9f6e705a3a9.mp4 | `79b4330be8abcc7a5af09a1d3bdddf0e` | 1440×2560, 30 fps, 4.07 s |

C02–C07: **ByteDance Upscale · Model version Pro · Resolution 2K · FPS 30 fps · Preset Common**

| Upscale file | Source clip | Source md5 | Upscale job | Result | md5 | Output |
|---|---|---|---|---|---|---|
| `clips/upscaled/v21_c02_g1.mp4` | `clips/v21_c02_g1.mp4` | `b7c0927e90b098abf0feb6768f9add0c` | `65f1a8d4-9b1d-4a74-bb2d-6c40e707df30` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_212734_f17b9a80-29ef-48d2-af5a-fd606048163e.mp4 | `cd9bc10dac70b1e5eaf7be1dded8074f` | 1440×2560, 30 fps, 4.07 s |
| `clips/upscaled/v21_c03_g1.mp4` | `clips/v21_c03_g1.mp4` | `31979de1361f943e9572610500e862be` | `2e25c818-1990-4f53-bc20-f3b7caa27c3e` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_212812_305bc38f-9928-4a70-963d-8584a2cfca7d.mp4 | `8222695a72c30aec12298781de5314e7` | 1440×2560, 30 fps, 3.97 s |
| `clips/upscaled/v21_c04_g1.mp4` | `clips/v21_c04_g1.mp4` | `23ef1cc82a01056e04416422f328a08b` | `90fed077-b081-439d-a593-81437d2f46f8` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_212848_68e12b36-cb2d-44de-abb2-3f60e614fd62.mp4 | `de795d1fd7c9671ee180bc4fbdec92cc` | 1440×2560, 30 fps, 4.07 s |
| `clips/upscaled/v21_c05_g1.mp4` | `clips/v21_c05_g1.mp4` | `3e6b4367716f39b4df33069c1e650198` | `e717eac4-b553-4fc9-840e-4d1308e8cc67` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_212920_2b988020-e82b-4623-8430-dd721dbc284b.mp4 | `bd43410b7c7bb2028fc213c8f85ab55e` | 1440×2560, 30 fps, 5.06 s |
| `clips/upscaled/v21_c06_g1.mp4` | `clips/v21_c06_g1.mp4` | `3b6e6d0183c42c712b2b4cfc4989a1fa` | `f342246e-7111-4dab-ae96-ec8ab7c112ed` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_212953_348a95e6-faab-45d9-b3ab-cdeb1fc85011.mp4 | `31a1415f4726bf7853722a8042ae7e8d` | 1440×2560, 30 fps, 5.06 s |
| `clips/upscaled/v21_c07_g1.mp4` | `clips/v21_c07_g1.mp4` | `59ba2ec04636c984e7e0b5b982f842da` | `041c6874-d2e3-4f97-ace4-e0af0c03adb3` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_213024_b7f2d892-a91c-49d8-b590-f256b9b75691.mp4 | `0ae0e63e4cc5ac032598470a033ec5c1` | 1440×2560, 30 fps, 4.07 s |

Re-roll upscaled 2026-09-25, same C02–C07 settings (**ByteDance Upscale · Pro · 2K · 30 fps · Preset Common**, Chrome extension, settings read back before submit). It replaces the upscale of the rejected g1 in the cut; that file stays on disk.

| Upscale file | Source clip | Source md5 | Upscale job | Result | md5 | Output |
|---|---|---|---|---|---|---|
| `clips/upscaled/v21_c05_g2.mp4` | `clips/v21_c05_g2.mp4` | `dbb01cb88cd5f133e2623a1dfc7787ab` | `8bef8489-1184-451f-8857-3dfa2e0f5608` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_224705_33d2667d-9f13-4bb2-90c8-edd8f4f7a9d1.mp4 | `d8b6c8e15cc2e666d82aff2aa2b714c0` | 1440×2560, 30 fps, 5.06 s |

## Verified record — Higgsfield (checked 2026-09-24)

Each file was downloaded straight from its Higgsfield result (md5 of download = file on disk); each prompt was compared byte-for-byte with the job's stored `params.prompt`. When anything above disagrees, this section wins.

### C01 — Painting the Christmas mural (new hook)

#### Image prompt — `starting_frames/v21_c01_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_203900_fac082d9-b1f8-4967-8c3c-5dde5090a2f9.png
**References, in submission order**
- @Image 1: `content/video_21_assets/references/v21_c01_r1.png` · Higgsfield media `3a196b34-d0c6-4f5a-9272-69f66c3843b2`
- @Image 2: `content/video_21_assets/starting_frames/v21_c07_g1.png` · Higgsfield media `5579aef2-ea00-428d-9f24-52a2f7736941`
**md5** - `94efd25e80cdf10b12ec0e7ca3d7e17b`

````text
Extremely high quality candid vertical iPhone photo inside a family's living room on a winter afternoon: a husband stands high up on a tall orange stepladder painting a big hand-painted Christmas mural onto the living room wall, while his wife sits on a white drop cloth on the floor below him painting the bottom of the same mural.

Use the FIRST attached reference photograph for BOTH the staging AND the camera position - the man standing near the top of the tall stepladder on the left of the mural wall with his arm raised painting the upper part of it, the woman sitting on the floor in the lower right on the drop cloth painting the lower part, the mural wall running away diagonally on the right, the open doorway on the left and the drop cloth spread over the wooden floor. COPY ITS CAMERA POSITION AND ITS COMPOSITION. Copy nothing else from it: the room, the man, the woman and the mural are all described below and are all different people in a different house.

FRAMING AND ANGLE: the camera is handheld at about the chest height of a standing adult, standing in the corner of the room and looking along the mural wall, which runs from the middle of the frame away to the right at an angle. The man on the ladder is in the upper LEFT half of the frame, seen from behind at three quarters, his head around the upper third of the picture. The ladder stands on the drop cloth with its feet in the lower middle of the frame. The woman sits on the floor in the lower RIGHT of the frame, seen from behind at three quarters, close to the camera and large in the picture. An open doorway with a white-painted wooden casing is on the LEFT edge of the frame. The floor and the drop cloth fill the bottom third of the frame. Nobody is looking at the camera and nobody is posing.

HEADROOM FOR A CAPTION - IMPORTANT: compared with the reference, the camera is tilted up very slightly so there is MORE empty space above the man's head. The top fifth of the frame is plain uncluttered cream plaster wall and plain white ceiling with a single flush round ceiling light - no mural, no pictures, no shelves, no garland, no hanging decorations and no lettering up there - so a caption can sit across the top of the picture. The man, the ladder and the woman stay the same size in the frame; do not shrink them to make that room.

THE MURAL: a big cheerful hand-painted Christmas mural in flat acrylic house paint directly on the cream plaster wall, looking genuinely painted by hand by amateurs - visible brush strokes, slightly uneven outlines, flat colours. A tall green Christmas tree with red and gold baubles and a gold star on top, a big jolly Santa in a red suit with a white beard waving one mittened hand, a smiling snowman with a red scarf and a carrot nose, a few wrapped presents at the base of the tree, a white snowy ground line and light blue snowflakes scattered across the wall. It is nearly finished: the man is painting the top of Santa's hat, the woman is painting one of the presents at the bottom.

THE ROOM: a cosy English Arts-and-Crafts living room. Warm cream plaster walls above sage-green painted wooden wainscoting with a simple oak cap rail, wide honey-oak floorboards, white-painted wooden door casing, a white ceiling. A large white canvas drop cloth is spread over the floor along the mural wall, with a few paint tins, a jar of brushes and a small palette of acrylic paints on it next to the woman.

THE MAN: about 40, short dark-brown hair going grey at the temples, a trimmed dark beard, a forest-green knit sweater with the sleeves pushed up, light stone chinos and brown leather boots. He stands on one of the top steps of a tall orange fibreglass stepladder, holding a small paint tin in his left hand and reaching up with a brush in his right, painting the top of Santa's hat.

THE WOMAN: about 38, long wavy chestnut-brown hair loose over her shoulders, an oversized oatmeal chunky cable-knit cardigan over a white top, faded blue jeans and thick grey wool socks. She sits on the drop cloth with her legs folded to one side, leaning in towards the wall, a fine brush in her right hand painting a red present at the bottom of the mural.

COLOUR: natural neutral daylight white balance, the way an iPhone renders a bright living room on a winter afternoon. NOT orange, NOT sepia, NOT heavily graded. Skin reads natural, the cream wall reads clean cream, the ladder reads true safety orange, the floorboards read as real wood.

LIGHTING AND QUALITY: perfect soft bright light - daylight from the doorway plus the ceiling light - every face, every brush stroke in the mural and every rung of the ladder clearly readable, no dark corners, no blown highlights. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere from the woman in the foreground to the top of the mural, realistic skin, hair, knitwear and paint texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical, no fisheye distortion.

No captions, no watermarks, no added lettering anywhere in the image, no writing on the mural or on any clothing, no user-interface elements and no social-media overlays.

REFERENCE ROLES: @Image 1 owns the camera position, the composition, the man-on-the-ladder and woman-on-the-floor staging and the mural-on-the-wall idea; it is a low-resolution screenshot, so copy its layout only, not its image quality, its people, its room or its exact mural, and ignore its caption text and emoji. @Image 2 supplies only the Arts-and-Crafts material palette of sage-green painted wood, honey oak and warm cream. Ignore its children, its projected imagery, its darkness, its camera and its composition.
````

#### Video prompt — `clips/v21_c01_g2.mp4` — FOR REVIEW

**Settings** - seedance_2_5 · omni_reference · 1080p · 4 s · 9:16 · audio on · genre auto · speedramp auto · multi_shots false · bitrate standard · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `4e76e56a-bdef-4338-b64e-69016b9701cb`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_210922_4e76e56a-bdef-4338-b64e-69016b9701cb.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c01_g1.png` · Higgsfield media `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
- @Image 1: `starting_frames/v21_c01_g1.png` · Higgsfield media `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
**md5** - `c41e8458b5fb126fa9a66d2ce5a4a295`

````text
START FRAME LOCK - HIGHEST PRIORITY: frame 0.0s is EXACTLY the supplied start image, @Image 1 is the same picture. Keep its framing for the whole clip: the cream mural wall with the hand-painted Christmas tree, Santa and snowman running away on the right, the open doorway on the left, the man near the top of the orange stepladder on the left of the mural, and the woman sitting on the white drop cloth in the lower right. The camera never moves closer, never zooms in, never crops in and never reframes; the plain wall and ceiling at the top of the frame stay empty the whole time.

Real home video, shot on a hand-held iPhone by a person standing in the corner of the room, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow him, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and nobody's body ever resets, jumps position or teleports between one part and the next.

ACTION TIMELINE:
0.0-0.6s - He is painting the top of Santa's hat, brush in his right hand, the open tin of red paint in his left. She is painting a present at the bottom of the mural. Calm, nothing dramatic.

0.6-1.6s - Without any pause, his foot slips on the step and the ladder starts to tip. He throws his LEFT hand - the hand gripping the open red paint tin - against the wall to catch himself, the open mouth of the tin pressed to the mural, and as that hand slides down the wall thick red paint pours out of the tin and runs down the wall in one long vertical red streak beside the painted tree. His RIGHT hand holds only the brush and leaves no paint anywhere. The feet of the ladder skid out across the drop cloth and the ladder slides out from under him.

1.6-2.3s - He falls forward and down, fast and heavy, and lands face-down on the bare wooden floor at the foot of the mural wall, to the left of the woman. The ladder crashes down beside and on top of his legs. The tin hits the floor and a big splash of red paint bursts out across the floorboards, spattering the lower wall and the edge of the drop cloth.

2.3-4.0s - He lies still face-down, stunned. A big glossy pool of red paint spreads fast across the floorboards towards the camera, and the empty tin rolls on its side through it towards the lens. The woman has twisted round on the drop cloth, one hand raised, mouth open in shock, staring at him. Red spatter on the wall, the drop cloth and her cardigan.

The fall has real weight. An ordinary man's balance goes, gravity takes him, and he is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. His limbs are heavy and human, not floaty or rubbery, and he never hangs in the air. The paint is bright red acrylic house paint, thick and glossy, and behaves like real paint: it pours, drips, splashes and spreads in a flat puddle on the wood. PAINT SOURCE: every drop of red paint in the clip comes out of the one open tin in his LEFT hand. No paint ever appears from his right hand, from the brush or out of nowhere; the streak on the wall starts exactly where the tin touches it.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the brush on the wall, the ladder scraping and crashing, a short yelp from him, the thud of his landing, the tin clanging and the paint splashing, then her shocked gasp.

FALL AND FRAMING LOCK - CHECK THIS LAST: he comes down right at the foot of the mural wall and lands on the floor in front of it, to the left of the woman, fully visible. He does not jump, step back or leap off the ladder, and he does not land behind her or out of frame. The ladder and the tin stay inside the frame. The mural stays on the wall. The camera keeps the start image's framing to the very last frame; it never tilts down to follow his fall.
````

#### Video prompt — `clips/v21_c01_g1.mp4` — REJECTED ("it doesn't make sense, paint appears magically from his right hand, he has the paint bottle in the left hand".)

**Settings** - seedance_2_5 · omni_reference · 1080p · 4 s · 9:16 · audio on · genre auto · speedramp auto · multi_shots false · bitrate standard · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `a5c6ea61-0e81-444a-81a2-92d2b8ef3b4d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_205547_a5c6ea61-0e81-444a-81a2-92d2b8ef3b4d.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c01_g1.png` · Higgsfield media `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
- @Image 1: `starting_frames/v21_c01_g1.png` · Higgsfield media `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
**md5** - `ca9b0c9091bc1155175f5e8dc6c059ad`

````text
START FRAME LOCK - HIGHEST PRIORITY: frame 0.0s is EXACTLY the supplied start image, @Image 1 is the same picture. Keep its framing for the whole clip: the cream mural wall with the hand-painted Christmas tree, Santa and snowman running away on the right, the open doorway on the left, the man near the top of the orange stepladder on the left of the mural, and the woman sitting on the white drop cloth in the lower right. The camera never moves closer, never zooms in, never crops in and never reframes; the plain wall and ceiling at the top of the frame stay empty the whole time.

Real home video, shot on a hand-held iPhone by a person standing in the corner of the room, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow him, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and nobody's body ever resets, jumps position or teleports between one part and the next.

ACTION TIMELINE:
0.0-0.6s - He is painting the top of Santa's hat, brush in his right hand, the open tin of red paint in his left. She is painting a present at the bottom of the mural. Calm, nothing dramatic.

0.6-1.6s - Without any pause, his foot slips on the step and the ladder starts to tip. He leans into the wall to catch himself and his left hand, still gripping the paint tin, slides down the mural - thick red paint pours out of the tin and runs down the wall in one long vertical red streak beside the painted tree. The feet of the ladder skid out across the drop cloth and the ladder slides out from under him.

1.6-2.3s - He falls forward and down, fast and heavy, and lands face-down on the bare wooden floor at the foot of the mural wall, to the left of the woman. The ladder crashes down beside and on top of his legs. The tin hits the floor and a big splash of red paint bursts out across the floorboards, spattering the lower wall and the edge of the drop cloth.

2.3-4.0s - He lies still face-down, stunned. A big glossy pool of red paint spreads fast across the floorboards towards the camera, and the empty tin rolls on its side through it towards the lens. The woman has twisted round on the drop cloth, one hand raised, mouth open in shock, staring at him. Red spatter on the wall, the drop cloth and her cardigan.

The fall has real weight. An ordinary man's balance goes, gravity takes him, and he is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. His limbs are heavy and human, not floaty or rubbery, and he never hangs in the air. The paint is bright red acrylic house paint, thick and glossy, and behaves like real paint: it pours, drips, splashes and spreads in a flat puddle on the wood.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the brush on the wall, the ladder scraping and crashing, a short yelp from him, the thud of his landing, the tin clanging and the paint splashing, then her shocked gasp.

FALL AND FRAMING LOCK - CHECK THIS LAST: he comes down right at the foot of the mural wall and lands on the floor in front of it, to the left of the woman, fully visible. He does not jump, step back or leap off the ladder, and he does not land behind her or out of frame. The ladder and the tin stay inside the frame. The mural stays on the wall. The camera keeps the start image's framing to the very last frame; it never tilts down to follow his fall.
````

#### Video prompt — no file — FAILED (`ip_detected`)

**Settings** - seedance_2_5 · omni_reference · 1080p · 4 s · 9:16 · audio on · genre auto · speedramp auto · multi_shots false · bitrate standard · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `f292be42-fddb-48f4-86f7-bf5c22d2854b`
**Result** - none (status `ip_detected`)
**Attached, in submission order**
- start_image: `starting_frames/v21_c01_g1.png` · Higgsfield media `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
- @Image 1: `starting_frames/v21_c01_g1.png` · Higgsfield media `fac082d9-b1f8-4967-8c3c-5dde5090a2f9`
- @Video 1: `references/v21_c01_r2.mp4` · Higgsfield media `bc765eba-1c9c-4bf7-bc9f-ce21d57006b6` · role video_references

````text
START FRAME LOCK - HIGHEST PRIORITY: frame 0.0s is EXACTLY the supplied start image, @Image 1 is the same picture. Keep its framing for the whole clip: the cream mural wall with the hand-painted Christmas tree, Santa and snowman running away on the right, the open doorway on the left, the man near the top of the orange stepladder on the left of the mural, and the woman sitting on the white drop cloth in the lower right. The camera never moves closer, never zooms in, never crops in and never reframes; the plain wall and ceiling at the top of the frame stay empty the whole time.

MOTION REFERENCE: @Video 1 is a real clip of this exact accident. Copy its action, its timing and the way the fall and the paint spill look, beat for beat. Copy nothing else from it: not its people, its room, its mural, its camera position, and NOT its caption text or emoji. The man, the woman, the room and the mural stay exactly as in the start image.

Real home video, shot on a hand-held iPhone by a person standing in the corner of the room, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow him, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and nobody's body ever resets, jumps position or teleports between one part and the next.

ACTION TIMELINE:
0.0-0.6s - He is painting the top of Santa's hat, brush in his right hand, the open tin of red paint in his left. She is painting a present at the bottom of the mural. Calm, nothing dramatic.

0.6-1.6s - Without any pause, his foot slips on the step and the ladder starts to tip. He leans into the wall to catch himself and his left hand, still gripping the paint tin, slides down the mural - thick red paint pours out of the tin and runs down the wall in one long vertical red streak beside the painted tree. The feet of the ladder skid out across the drop cloth and the ladder slides out from under him.

1.6-2.3s - He falls forward and down, fast and heavy, and lands face-down on the bare wooden floor at the foot of the mural wall, to the left of the woman. The ladder crashes down beside and on top of his legs. The tin hits the floor and a big splash of red paint bursts out across the floorboards, spattering the lower wall and the edge of the drop cloth.

2.3-4.0s - He lies still face-down, stunned. A big glossy pool of red paint spreads fast across the floorboards towards the camera, and the empty tin rolls on its side through it towards the lens. The woman has twisted round on the drop cloth, one hand raised, mouth open in shock, staring at him. Red spatter on the wall, the drop cloth and her cardigan.

The fall has real weight. An ordinary man's balance goes, gravity takes him, and he is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. His limbs are heavy and human, not floaty or rubbery, and he never hangs in the air. The paint is bright red acrylic house paint, thick and glossy, and behaves like real paint: it pours, drips, splashes and spreads in a flat puddle on the wood.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the brush on the wall, the ladder scraping and crashing, a short yelp from him, the thud of his landing, the tin clanging and the paint splashing, then her shocked gasp.

FALL AND FRAMING LOCK - CHECK THIS LAST: he comes down right at the foot of the mural wall and lands on the floor in front of it, to the left of the woman, fully visible. He does not jump, step back or leap off the ladder, and he does not land behind her or out of frame. The ladder and the tin stay inside the frame. The mural stays on the wall. The camera keeps the start image's framing to the very last frame; it never tilts down to follow his fall.
````

### C02 — Hands on the box

#### Image prompt — `starting_frames/v21_c02_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `202d4a72-692f-4460-be7e-108d47ed4044`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260923_235841_202d4a72-692f-4460-be7e-108d47ed4044.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`
**md5** - `4faff8101a64cf16b032c7e8eedc605f`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 35, with warm tan skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a forest-green chunky cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive English country dining room with sage-green painted panelled walls, a carved white-painted wooden fireplace hung with red plaid stockings, a brass-framed oval mirror, a painted pine dresser displaying blue-and-white plates and a Christmas tree dressed with red plaid bows, gingerbread ornaments and warm white fairy lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few red holly berries, two or three small red and gold glass baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v21_c02_g1.mp4` — FOR REVIEW

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `dfa2191f-4977-489f-9619-7f4cc799be4b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022208_dfa2191f-4977-489f-9619-7f4cc799be4b.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`
- @Image 1 (image reference): `starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`
**md5** - `b7c0927e90b098abf0feb6768f9add0c`

````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 4-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no zoom, no reframe. Every stage of the box opening is shown happening - the flap lifting, folding back and the hand reaching in - never skipped. The box, hands and table stay continuous frame to frame.

STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a forest-green chunky cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge fills the frame. The lit cream candle, fir sprigs, red holly berries, small red and gold glass baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive English country dining room with sage-green painted panelled walls, a carved white-painted wooden fireplace hung with red plaid stockings, a brass-framed oval mirror, a painted pine dresser displaying blue-and-white plates and a Christmas tree dressed with red plaid bows, gingerbread ornaments and warm white fairy lights. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the pale bleached-oak dining table with fine straight grain, a matte oiled finish and a softly rounded edge, lid flaps folded back. The printed front artwork, candle, fir, baubles, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

### C03 — The projector lifted

#### Image prompt — `starting_frames/v21_c03_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `5038db7d-ab48-4d9f-af51-249dfbee0a98`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_000210_5038db7d-ab48-4d9f-af51-249dfbee0a98.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
- @Image 2: `content/video_21_assets/starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`
**md5** - `1a7c235e3a86520710c231d72fa375ae`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with warm tan skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a forest-green chunky cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same forest-green chunky cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C02 and owns the new woman's hands, sweater, photographic look and full-size carton-to-projector scale; the projector should plausibly fill that carton when unpacked; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v21_c03_g1.mp4` — FOR REVIEW

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `3cab83e5-fbc0-4955-973a-f285275c3779`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022302_3cab83e5-fbc0-4955-973a-f285275c3779.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c03_g1.png` · Higgsfield media `5038db7d-ab48-4d9f-af51-249dfbee0a98`
**md5** - `31979de1361f943e9572610500e862be`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in forest-green chunky cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy; behind it deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the quartz. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the quartz in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the quartz.
3.0-3.4s - the four feet of the stand touch the quartz; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the quartz, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### C04 — The cable going in

#### Image prompt — `starting_frames/v21_c04_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `e4cd729b-bb65-42ba-8817-3ae44ca10657`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_000552_e4cd729b-bb65-42ba-8817-3ae44ca10657.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`
- @Image 2: `content/video_21_assets/starting_frames/v21_c03_g1.png` · Higgsfield media `5038db7d-ab48-4d9f-af51-249dfbee0a98`
**md5** - `5cbfe1674e2b79e73c32b84f12e4103e`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with warm tan skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a forest-green chunky cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C03 and owns the enlarged product's physical dimensions relative to the hands, exact product identity, kitchen finishes, hands, sweater and photographic look; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v21_c04_g1.mp4` — FOR REVIEW

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `06f2ac72-2057-43d6-840b-e612a5521f1c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022359_06f2ac72-2057-43d6-840b-e612a5521f1c.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c04_g1.png` · Higgsfield media `e4cd729b-bb65-42ba-8817-3ae44ca10657`
**md5** - `23ef1cc82a01056e04416422f328a08b`

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
THE LEFT HAND - a woman's hand in a forest-green chunky cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same forest-green chunky cable-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a white quartz countertop with soft grey veining and a straight eased edge, honed matte rather than glossy; behind it deep forest-green shaker cabinets with aged brass cup pulls, white square zellige backsplash tiles, a black enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments and plaid ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the quartz and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the quartz around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the quartz immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### C05 — The door opens on the room — start frame

#### Image prompt — `starting_frames/v21_c05_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `417cea70-8c6e-43c6-a99c-e068f223b4bd`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_000210_417cea70-8c6e-43c6-a99c-e068f223b4bd.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- @Image 2: `content/video_21_assets/starting_frames/v21_c02_g1.png` · Higgsfield media `202d4a72-692f-4460-be7e-108d47ed4044`
**md5** - `aad6b2888af28d0d4739e89b27b595ac`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the forest-green chunky cable-knit wool sleeve and no jewellery, with warm tan skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear door surface visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the burgundy-red paint reads clearly as deep red, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v21_c05_g3.mp4` — NOT USED (Daniel chose g2)

**Settings** - seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `38a7f121-94b5-47df-b5cc-b34b5283e52f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_223737_38a7f121-94b5-47df-b5cc-b34b5283e52f.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c05_g1.png` · Higgsfield media `417cea70-8c6e-43c6-a99c-e068f223b4bd`
- @Image 1 (image reference): `references/v21_c05_r2.png` · Higgsfield media `95f8c0ab-4fd7-41c7-a379-76ae45dda0d2`
**md5** - `ab37d0eb3df1400e70f99b2287e6d838`

````text
CAMERA CONTINUITY - PRIMARY CORRECTION: the entire five seconds are ONE slow, uninterrupted forward-and-upward glide. Forward travel and upward aim are mechanically coupled as one motion, already underway together in frame zero. Keep the same gentle pace and the same forward-to-upward ratio for every frame, including while the door opens and while crossing its sill. Travel only about 0.8 metres forward over the entire shot, with an even upward tilt of about 18 degrees over those same five seconds. The wreath, door-panel edges and later the back-wall details drift smoothly downward in the frame from the beginning while perspective advances very gently. There is no forward-only phase and no later tilt-only phase. Never complete an entrance and then begin looking up. Do not accelerate the beginning, hurry through the door, ease in, ease out, steepen the tilt, speed-ramp or catch up to an end composition. The final frame can remain near the threshold with the back wall, furniture and ceiling visible; covering more distance or revealing the whole ceiling is not a goal. The door opens naturally during the same slow glide; its opening is not a camera cue. Preserve the same doorframe and room features across adjacent frames as the camera physically crosses the single sill. No cut, concealed edit, dissolve, match cut, scene replacement, teleport, jump or sudden perspective change. Maintain this single gentle motion unchanged until the clip ends.

CHILD MOVEMENT - PRIMARY CORRECTION: @Image 2 shows the room EMPTY. EXACTLY TWO CHILDREN exist in this clip - the girl and the boy described in this text - and nobody else ever appears: no third child, no extra kids in the background, on the sofa or in the doorway, no adult. There is no pose, spot or arrangement of them to copy, and they never stand still anywhere. They are already running a game of chase behind the closed door, and the chase never ends inside this clip. Per second:
0-1s: when the door opens the two children are already running well inside the room, at least three metres from the door, on the open floor across the rug - never right in front of the door and never close to the camera; the girl is mid-stride, one foot off the floor, and the boy runs two strides behind her.
1-2s: both run a wide curve across the rug away from the camera, arms swinging; the boy throws one arm up and points at the flying sleigh on the ceiling while still running.
2-3s: the girl spins round once while running, arms out, laughing up at the ceiling; the boy runs round the ottoman after her.
3-4s: the girl runs past the Christmas tree toward the right-hand side of the room; the boy chases two strides behind at a different depth.
4-5s: both are still running mid-stride when the clip ends, the girl near the right edge of the frame, the boy crossing the rug behind her.
They are never side by side, never face the camera, never pause, never stop in front of the sofa. VISIBILITY: from the moment each child is first seen in the door gap, that same child stays visible in every following frame. Neither child ever runs behind the sofa, the ottoman, the tree or the door, never leaves the frame and never re-enters; the boy is never hidden and then suddenly present somewhere new. Both stay on the open floor in view. This child action must not alter the camera movement specified above.

DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Image 2. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high coffered ceiling meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim fully closed with a wreath, a hand on the brass knob. @Image 2 is a reference photo of the EMPTY room for the layout, coffered ceiling, furniture, colours and projection artwork appearance; it contains no people. Use only the single continuous camera move and child actions specified in this prompt; the room still supplies appearance only. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED ANIMATION - THE MAIN SUBJECT. The Christmas picture on the walls and ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, not a still illustration; only the projected picture is animated, while the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in every frame from the first to the last, independent of the camera. The architecture, the workshops, the barn and the moon stay put; everything else drawn in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is not parked with only its legs moving. It flies in one smooth sweeping arc, flying from where it is first seen across the coffered ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place on the ceiling every second and has crossed most of the ceiling by the end. While it travels the reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY workshop chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from the chimney below. Several plumes are clearly rising at once, all the time.
- SKY: the huge golden full moon glows and its halo pulses brighter and dimmer; the drifting snowflakes swirl across the ceiling; the golden stars twinkle; now and then a shooting star streaks across.
- VILLAGE LIFE: the little red steam train chugs steadily along its snowy track pulling its wagons of presents, puffing white steam; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock toss their heads and trot.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall, flat on the wall and ceiling surfaces.
- LIGHTS: bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (5 s):
0-1s: the door opens onto the room; through the gap the sleigh is already flying and smoke is already rising from the workshop chimneys.
1-2s: the sleigh team travels across the coffered ceiling, clearly changing position, reindeer galloping; smoke columns climb the wall; the steam train chugs along its track; snow drifts down.
2-3s: the sleigh has moved on a quarter of the ceiling past the beams; the snowflakes swirl; the elves hammer in the workshop windows.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; a shooting star streaks across.
4-5s: all of it still moving at the same pace in the final frame - sleigh flying, smoke rising, train chugging, snow falling.
All of this is flat projected light lying on the real plaster, wall panelling and window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CONTINUOUS ACTION, NOT CAMERA PHASES
0.0-5.0s - ONE identical slow forward-and-upward glide continues for the full duration, already underway at frame zero. The view rises gently while moving forward at the same steady ratio throughout. During approximately the first 1.5 seconds the hand turns the knob and opens the door with a smooth, ordinary unhurried push, never a quick shove or a fast reveal. The camera does not wait for the door, rush through it, pause for the room, change speed at the sill, or start a new movement afterward. The closed-door frame and the revealed room belong to the same continuous physical shot. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap. Cross only the single thin threshold directly into the living room; no intervening space. There is no stop at the sofa or separate ceiling reveal. The shot ends during that same gentle glide, with back wall, furniture and ceiling still visible. All through it the smoke pours from every chimney, the sleigh flies on across the ceiling, the existing illustrated steam train and busy elves keep moving, the workshop windows flicker, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl, about five with warm brown skin and long black braids tied with small gold beads, runs a broad curving path across the rug and alongside the sofa; the boy, about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue the same open-ended curving chase naturally around the available floor space, curving away from furniture and each other; this is not a loop that returns them to a reference pose. During the final 1.5 seconds the girl continues around the right-hand edge of the rug while the boy follows two running strides behind, with their bodies at different depths and turned along their route. Both children stay inside the frame and in full view until the last frame; neither is required to be centred. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. While running, the boy throws one arm up and points at the flying sleigh and the golden full moon on the ceiling, and the girl looks up in delight mid-stride, but their feet keep stepping and their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, a steady natural phone glide. One constant slow forward-and-upward movement, both components active together from frame zero through frame last, with the same gentle speed and same ratio throughout. No opening rush, acceleration, easing, speed ramp, phase change, level hold, delayed upward tilt, pitch jump, reframe, stop, second move, cut, concealed edit, dissolve, teleport, zoom, orbit, fisheye or lens warping. The camera is the person's eyes; no phone, screen or device in frame.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

REFERENCE-ONLY LOCK - @Image 2 is a still photograph of the EMPTY room. It supplies architecture, furniture, colours and projected artwork appearance ONLY. It is not an end frame, camera target or transition destination; never dissolve, cut, morph or snap into its composition. Only the closed-door @Image 1 defines frame zero. The two children come only from the text above and are running from the first gap to the last frame; no other people ever appear. The new clip is exactly 5 seconds and has no end frame or driving video.

ROOM AND IDENTITY - a spacious double-height English Arts-and-Crafts Christmas great room with a high COFFERED CEILING: a broad flat plaster ceiling divided into a deep grid of square recessed coffers by crisp white-painted wooden beams. Sage-green painted wooden wall panelling lines the walls. A tall chimney breast of honey-coloured limestone stands on the back wall with a carved oak mantel; two tall casement windows with white-painted wooden frames and slim glazing bars occupy the left wall and a wide round-arched doorway with a white-painted wooden casing sits on the right. Wide honey-oak floorboards, a large rust-orange velvet sectional sofa, a round tan leather ottoman and a soft cream wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about five with warm brown skin and long black braids tied with small gold beads; a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut. Both fully dressed in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Preserve the architecture from @Image 2; the children's appearance comes from this text only.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

BANNED - either child right in front of the door or close to the camera as it opens; a third child or any extra children appearing anywhere, at any moment; a child popping into view that was not visible a moment before; a child vanishing behind furniture; an adult; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; any camera acceleration or speed ramp; treating the room reference as a destination; either child standing still, frozen, posed or waiting at any moment, including in the first gap of the door; either child climbing onto the sofa; the two children side by side or facing the camera; a glow or bright seam along the door edge; light that grows or fills the room as the door opens; the projector unit visible; blur; a cut.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the steam train or the elves do not move; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture rotates or slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````

#### Video prompt — `clips/v21_c05_g2.mp4` — IN THE CUT (Daniel 2026-09-25: "we will use g2")

**Settings** - seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `313436fd-e789-446c-8441-e7e50a5d5723`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_222453_313436fd-e789-446c-8441-e7e50a5d5723.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c05_g1.png` · Higgsfield media `417cea70-8c6e-43c6-a99c-e068f223b4bd`
- @Image 1 (image reference): `references/v21_c05_r2.png` · Higgsfield media `95f8c0ab-4fd7-41c7-a379-76ae45dda0d2`
**md5** - `dbb01cb88cd5f133e2623a1dfc7787ab`

````text
CAMERA CONTINUITY - PRIMARY CORRECTION: the entire five seconds are ONE slow, uninterrupted forward-and-upward glide. Forward travel and upward aim are mechanically coupled as one motion, already underway together in frame zero. Keep the same gentle pace and the same forward-to-upward ratio for every frame, including while the door opens and while crossing its sill. Travel only about 0.8 metres forward over the entire shot, with an even upward tilt of about 18 degrees over those same five seconds. The wreath, door-panel edges and later the back-wall details drift smoothly downward in the frame from the beginning while perspective advances very gently. There is no forward-only phase and no later tilt-only phase. Never complete an entrance and then begin looking up. Do not accelerate the beginning, hurry through the door, ease in, ease out, steepen the tilt, speed-ramp or catch up to an end composition. The final frame can remain near the threshold with the back wall, furniture and ceiling visible; covering more distance or revealing the whole ceiling is not a goal. The door opens naturally during the same slow glide; its opening is not a camera cue. Preserve the same doorframe and room features across adjacent frames as the camera physically crosses the single sill. No cut, concealed edit, dissolve, match cut, scene replacement, teleport, jump or sudden perspective change. Maintain this single gentle motion unchanged until the clip ends.

CHILD MOVEMENT - PRIMARY CORRECTION: @Image 2 shows the room EMPTY. EXACTLY TWO CHILDREN exist in this clip - the girl and the boy described in this text - and nobody else ever appears: no third child, no extra kids in the background, on the sofa or in the doorway, no adult. There is no pose, spot or arrangement of them to copy, and they never stand still anywhere. They are already running a game of chase behind the closed door, and the chase never ends inside this clip. Per second:
0-1s: in the very first gap of the opening door the girl is already running, caught mid-stride crossing the gap from left to right, one foot off the floor; the boy runs two strides behind her.
1-2s: both run a wide curve across the rug away from the camera, arms swinging; the boy throws one arm up and points at the flying sleigh on the ceiling while still running.
2-3s: the girl spins round once while running, arms out, laughing up at the ceiling; the boy runs round the ottoman after her.
3-4s: the girl runs past the Christmas tree toward the right-hand side of the room; the boy chases two strides behind at a different depth.
4-5s: both are still running mid-stride when the clip ends, the girl near the right edge of the frame, the boy crossing the rug behind her.
They are never side by side, never face the camera, never pause, never stop in front of the sofa. VISIBILITY: from the moment each child is first seen in the door gap, that same child stays visible in every following frame. Neither child ever runs behind the sofa, the ottoman, the tree or the door, never leaves the frame and never re-enters; the boy is never hidden and then suddenly present somewhere new. Both stay on the open floor in view. This child action must not alter the camera movement specified above.

DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Image 2. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high coffered ceiling meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim fully closed with a wreath, a hand on the brass knob. @Image 2 is a reference photo of the EMPTY room for the layout, coffered ceiling, furniture, colours and projection artwork appearance; it contains no people. Use only the single continuous camera move and child actions specified in this prompt; the room still supplies appearance only. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED ANIMATION - THE MAIN SUBJECT. The Christmas picture on the walls and ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, not a still illustration; only the projected picture is animated, while the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in every frame from the first to the last, independent of the camera. The architecture, the workshops, the barn and the moon stay put; everything else drawn in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is not parked with only its legs moving. It flies in one smooth sweeping arc, flying from where it is first seen across the coffered ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place on the ceiling every second and has crossed most of the ceiling by the end. While it travels the reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY workshop chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from the chimney below. Several plumes are clearly rising at once, all the time.
- SKY: the huge golden full moon glows and its halo pulses brighter and dimmer; the drifting snowflakes swirl across the ceiling; the golden stars twinkle; now and then a shooting star streaks across.
- VILLAGE LIFE: the little red steam train chugs steadily along its snowy track pulling its wagons of presents, puffing white steam; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock toss their heads and trot.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall, flat on the wall and ceiling surfaces.
- LIGHTS: bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (5 s):
0-1s: the door opens onto the room; through the gap the sleigh is already flying and smoke is already rising from the workshop chimneys.
1-2s: the sleigh team travels across the coffered ceiling, clearly changing position, reindeer galloping; smoke columns climb the wall; the steam train chugs along its track; snow drifts down.
2-3s: the sleigh has moved on a quarter of the ceiling past the beams; the snowflakes swirl; the elves hammer in the workshop windows.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; a shooting star streaks across.
4-5s: all of it still moving at the same pace in the final frame - sleigh flying, smoke rising, train chugging, snow falling.
All of this is flat projected light lying on the real plaster, wall panelling and window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CONTINUOUS ACTION, NOT CAMERA PHASES
0.0-5.0s - ONE identical slow forward-and-upward glide continues for the full duration, already underway at frame zero. The view rises gently while moving forward at the same steady ratio throughout. During approximately the first 1.5 seconds the hand turns the knob and opens the door with a smooth, ordinary unhurried push, never a quick shove or a fast reveal. The camera does not wait for the door, rush through it, pause for the room, change speed at the sill, or start a new movement afterward. The closed-door frame and the revealed room belong to the same continuous physical shot. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap. Cross only the single thin threshold directly into the living room; no intervening space. There is no stop at the sofa or separate ceiling reveal. The shot ends during that same gentle glide, with back wall, furniture and ceiling still visible. All through it the smoke pours from every chimney, the sleigh flies on across the ceiling, the existing illustrated steam train and busy elves keep moving, the workshop windows flicker, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl, about five with warm brown skin and long black braids tied with small gold beads, runs a broad curving path across the rug and alongside the sofa; the boy, about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue the same open-ended curving chase naturally around the available floor space, curving away from furniture and each other; this is not a loop that returns them to a reference pose. During the final 1.5 seconds the girl continues around the right-hand edge of the rug while the boy follows two running strides behind, with their bodies at different depths and turned along their route. Both children stay inside the frame and in full view until the last frame; neither is required to be centred. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. While running, the boy throws one arm up and points at the flying sleigh and the golden full moon on the ceiling, and the girl looks up in delight mid-stride, but their feet keep stepping and their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, a steady natural phone glide. One constant slow forward-and-upward movement, both components active together from frame zero through frame last, with the same gentle speed and same ratio throughout. No opening rush, acceleration, easing, speed ramp, phase change, level hold, delayed upward tilt, pitch jump, reframe, stop, second move, cut, concealed edit, dissolve, teleport, zoom, orbit, fisheye or lens warping. The camera is the person's eyes; no phone, screen or device in frame.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

REFERENCE-ONLY LOCK - @Image 2 is a still photograph of the EMPTY room. It supplies architecture, furniture, colours and projected artwork appearance ONLY. It is not an end frame, camera target or transition destination; never dissolve, cut, morph or snap into its composition. Only the closed-door @Image 1 defines frame zero. The two children come only from the text above and are running from the first gap to the last frame; no other people ever appear. The new clip is exactly 5 seconds and has no end frame or driving video.

ROOM AND IDENTITY - a spacious double-height English Arts-and-Crafts Christmas great room with a high COFFERED CEILING: a broad flat plaster ceiling divided into a deep grid of square recessed coffers by crisp white-painted wooden beams. Sage-green painted wooden wall panelling lines the walls. A tall chimney breast of honey-coloured limestone stands on the back wall with a carved oak mantel; two tall casement windows with white-painted wooden frames and slim glazing bars occupy the left wall and a wide round-arched doorway with a white-painted wooden casing sits on the right. Wide honey-oak floorboards, a large rust-orange velvet sectional sofa, a round tan leather ottoman and a soft cream wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about five with warm brown skin and long black braids tied with small gold beads; a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut. Both fully dressed in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Preserve the architecture from @Image 2; the children's appearance comes from this text only.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

BANNED - a third child or any extra children appearing anywhere, at any moment; a child popping into view that was not visible a moment before; a child vanishing behind furniture; an adult; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; any camera acceleration or speed ramp; treating the room reference as a destination; either child standing still, frozen, posed or waiting at any moment, including in the first gap of the door; either child climbing onto the sofa; the two children side by side or facing the camera; a glow or bright seam along the door edge; light that grows or fills the room as the door opens; the projector unit visible; blur; a cut.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the steam train or the elves do not move; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture rotates or slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````

#### Video prompt — `clips/v21_c05_g1.mp4` — REJECTED (Daniel 2026-09-25)

**Settings** - seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on
**Job** - `7c9425b4-578c-492d-a0fc-deb71e9cdb3f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022501_7c9425b4-578c-492d-a0fc-deb71e9cdb3f.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c05_g1.png` · Higgsfield media `417cea70-8c6e-43c6-a99c-e068f223b4bd`
- @Image 1 (image reference): `references/v21_c05_r2.png` · Higgsfield media `95f8c0ab-4fd7-41c7-a379-76ae45dda0d2`
**md5** - `3e6b4367716f39b4df33069c1e650198`

````text
CAMERA CONTINUITY - PRIMARY CORRECTION: the entire five seconds are ONE slow, uninterrupted forward-and-upward glide. Forward travel and upward aim are mechanically coupled as one motion, already underway together in frame zero. Keep the same gentle pace and the same forward-to-upward ratio for every frame, including while the door opens and while crossing its sill. Travel only about 0.8 metres forward over the entire shot, with an even upward tilt of about 18 degrees over those same five seconds. The wreath, door-panel edges and later the back-wall details drift smoothly downward in the frame from the beginning while perspective advances very gently. There is no forward-only phase and no later tilt-only phase. Never complete an entrance and then begin looking up. Do not accelerate the beginning, hurry through the door, ease in, ease out, steepen the tilt, speed-ramp or catch up to an end composition. The final frame can remain near the threshold with the back wall, furniture and ceiling visible; covering more distance or revealing the whole ceiling is not a goal. The door opens naturally during the same slow glide; its opening is not a camera cue. Preserve the same doorframe and room features across adjacent frames as the camera physically crosses the single sill. No cut, concealed edit, dissolve, match cut, scene replacement, teleport, jump or sudden perspective change. Maintain this single gentle motion unchanged until the clip ends.

CHILD MOVEMENT - PRIMARY CORRECTION: @Image 2 shows the room EMPTY. EXACTLY TWO CHILDREN exist in this clip - the girl and the boy described in this text - and nobody else ever appears: no third child, no extra kids in the background, on the sofa or in the doorway, no adult. There is no pose, spot or arrangement of them to copy, and they never stand still anywhere. They are already running a game of chase behind the closed door, and the chase never ends inside this clip. Per second:
0-1s: in the very first gap of the opening door the girl is already running, caught mid-stride crossing the gap from left to right, one foot off the floor; the boy runs two strides behind her.
1-2s: both run a wide curve across the rug away from the camera, arms swinging; the boy throws one arm up and points at the flying sleigh on the ceiling while still running.
2-3s: the girl spins round once while running, arms out, laughing up at the ceiling; the boy runs round the ottoman after her.
3-4s: the girl runs past the Christmas tree toward the right-hand side of the room; the boy chases two strides behind at a different depth.
4-5s: both are still running mid-stride when the clip ends, the girl near the right edge of the frame, the boy crossing the rug behind her.
They are never side by side, never face the camera, never pause, never stop in front of the sofa. This child action must not alter the camera movement specified above.

DIRECT ROOM ENTRY - PRIMARY GEOMETRY CORRECTION: the closed door in @Image 1 is fitted directly into the living room's entrance wall. Its far face opens immediately into the furnished Christmas living room in @Image 2. There is ONE door and ONE thin normal wall-thickness threshold, about 15 cm deep. The very first gap reveals the living room itself, its already-moving children and active projections, close behind this door. As the camera crosses that single threshold it is already INSIDE the living room beside the near end of the sectional and rug shown in the reference. The living room floor begins at the far edge of the same sill; its side walls and high coffered ceiling meet this entrance wall directly. No intervening hall, foyer, vestibule, tunnel, passage, empty approach space, second doorway or arch to walk under. Do not frame the living room at the far end of another space. The side opening visible on the reference room's RIGHT SIDE WALL is a lateral room feature only, away from the camera's route; never place it in front of the camera or between this door and the living room. Preserve the exact supplied closed-door first frame. After opening that same door, the existing continuous forward movement enters the living room directly.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim fully closed with a wreath, a hand on the brass knob. @Image 2 is a reference photo of the EMPTY room for the layout, coffered ceiling, furniture, colours and projection artwork appearance; it contains no people. Use only the single continuous camera move and child actions specified in this prompt; the room still supplies appearance only. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

PROJECTED ANIMATION - THE MAIN SUBJECT. The Christmas picture on the walls and ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, not a still illustration; only the projected picture is animated, while the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in every frame from the first to the last, independent of the camera. The architecture, the workshops, the barn and the moon stay put; everything else drawn in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is not parked with only its legs moving. It flies in one smooth sweeping arc, flying from where it is first seen across the coffered ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place on the ceiling every second and has crossed most of the ceiling by the end. While it travels the reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY workshop chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from the chimney below. Several plumes are clearly rising at once, all the time.
- SKY: the huge golden full moon glows and its halo pulses brighter and dimmer; the drifting snowflakes swirl across the ceiling; the golden stars twinkle; now and then a shooting star streaks across.
- VILLAGE LIFE: the little red steam train chugs steadily along its snowy track pulling its wagons of presents, puffing white steam; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock toss their heads and trot.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall, flat on the wall and ceiling surfaces.
- LIGHTS: bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (5 s):
0-1s: the door opens onto the room; through the gap the sleigh is already flying and smoke is already rising from the workshop chimneys.
1-2s: the sleigh team travels across the coffered ceiling, clearly changing position, reindeer galloping; smoke columns climb the wall; the steam train chugs along its track; snow drifts down.
2-3s: the sleigh has moved on a quarter of the ceiling past the beams; the snowflakes swirl; the elves hammer in the workshop windows.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; a shooting star streaks across.
4-5s: all of it still moving at the same pace in the final frame - sleigh flying, smoke rising, train chugging, snow falling.
All of this is flat projected light lying on the real plaster, wall panelling and window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CONTINUOUS ACTION, NOT CAMERA PHASES
0.0-5.0s - ONE identical slow forward-and-upward glide continues for the full duration, already underway at frame zero. The view rises gently while moving forward at the same steady ratio throughout. During approximately the first 1.5 seconds the hand turns the knob and opens the door with a smooth, ordinary unhurried push, never a quick shove or a fast reveal. The camera does not wait for the door, rush through it, pause for the room, change speed at the sill, or start a new movement afterward. The closed-door frame and the revealed room belong to the same continuous physical shot. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap. Cross only the single thin threshold directly into the living room; no intervening space. There is no stop at the sofa or separate ceiling reveal. The shot ends during that same gentle glide, with back wall, furniture and ceiling still visible. All through it the smoke pours from every chimney, the sleigh flies on across the ceiling, the existing illustrated steam train and busy elves keep moving, the workshop windows flicker, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The girl, about five with warm brown skin and long black braids tied with small gold beads, runs a broad curving path across the rug and alongside the sofa; the boy, about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue the same open-ended curving chase naturally around the available floor space, curving away from furniture and each other; this is not a loop that returns them to a reference pose. During the final 1.5 seconds the girl continues around the right-hand edge of the rug while the boy follows two running strides behind, with their bodies at different depths and turned along their route. The girl can leave the frame at the side while still running and the boy keeps following; neither child is required to remain centred or fully visible. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. While running, the boy throws one arm up and points at the flying sleigh and the golden full moon on the ceiling, and the girl looks up in delight mid-stride, but their feet keep stepping and their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, a steady natural phone glide. One constant slow forward-and-upward movement, both components active together from frame zero through frame last, with the same gentle speed and same ratio throughout. No opening rush, acceleration, easing, speed ramp, phase change, level hold, delayed upward tilt, pitch jump, reframe, stop, second move, cut, concealed edit, dissolve, teleport, zoom, orbit, fisheye or lens warping. The camera is the person's eyes; no phone, screen or device in frame.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the door, the brass knob, the forearm and sleeve exactly as shown in the starting image, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

REFERENCE-ONLY LOCK - @Image 2 is a still photograph of the EMPTY room. It supplies architecture, furniture, colours and projected artwork appearance ONLY. It is not an end frame, camera target or transition destination; never dissolve, cut, morph or snap into its composition. Only the closed-door @Image 1 defines frame zero. The two children come only from the text above and are running from the first gap to the last frame; no other people ever appear. The new clip is exactly 5 seconds and has no end frame or driving video.

ROOM AND IDENTITY - a spacious double-height English Arts-and-Crafts Christmas great room with a high COFFERED CEILING: a broad flat plaster ceiling divided into a deep grid of square recessed coffers by crisp white-painted wooden beams. Sage-green painted wooden wall panelling lines the walls. A tall chimney breast of honey-coloured limestone stands on the back wall with a carved oak mantel; two tall casement windows with white-painted wooden frames and slim glazing bars occupy the left wall and a wide round-arched doorway with a white-painted wooden casing sits on the right. Wide honey-oak floorboards, a large rust-orange velvet sectional sofa, a round tan leather ottoman and a soft cream wool rug. The side opening on the right wall remains lateral to the route, never an extra threshold ahead. a girl of about five with warm brown skin and long black braids tied with small gold beads; a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut. Both fully dressed in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Preserve the architecture from @Image 2; the children's appearance comes from this text only.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

BANNED - a third child or any extra children appearing anywhere, at any moment; an adult; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; any camera acceleration or speed ramp; treating the room reference as a destination; either child standing still, frozen, posed or waiting at any moment, including in the first gap of the door; either child climbing onto the sofa; the two children side by side or facing the camera; a glow or bright seam along the door edge; light that grows or fills the room as the door opens; the projector unit visible; blur; a cut.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the steam train or the elves do not move; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture rotates or slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````

### C05 F2 — The door opens on the room — room reference

#### Image prompt — `references/v21_c05_r1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260923_235840_2fcbb86b-b10d-4ce6-8cd7-68d4ace96615.png
**References, in submission order**
- @Image 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`
**md5** - `c895b13c09b3e77920ae87f19f4f268b`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut; the girl is of about five with warm brown skin and long black braids tied with small gold beads. Both children are fully dressed for winter in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height English Arts-and-Crafts Christmas great room with a high COFFERED CEILING: a broad flat plaster ceiling divided into a deep grid of square recessed coffers by crisp white-painted wooden beams. Sage-green painted wooden wall panelling lines the walls. A tall chimney breast of honey-coloured limestone stands on the back wall with a carved oak mantel; two tall casement windows with white-painted wooden frames and slim glazing bars occupy the left wall and a wide round-arched doorway with a white-painted wooden casing sits on the right. Wide honey-oak floorboards, a large rust-orange velvet sectional sofa, a round tan leather ottoman and a soft cream wool rug. Seen from the doorway; the new a deep burgundy-red painted solid wood door with four square recessed panels, a satin finish and crisp white-painted surrounding trim is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, copper and cream baubles, dried orange slices, plaid ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cream-and-rust knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The deep coffered ceiling remains clearly three-dimensional, its white-painted beams crossing in a crisp square grid. The sleigh and the ceiling picture continue straight across every beam face and underside and down into each recessed coffer, folding at the beam edges with correct offsets, before continuing onto the walls. The tall chimney breast receives a continuous picture with clear folds at its two projecting corners. The white-painted wooden window frames, glazing bars, doorway casing and wall panelling carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the soft cream wool rug, the rust-orange velvet sectional sofa, the round tan leather ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

NATURAL, LESS CINEMATIC LOOK - a little less cinematic than a film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster or an advert. True-to-life colour and contrast as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting and no heightened fantasy glow on the children. The projection is still dense, bright and colourful, but it reads as the real light of a home Christmas projector falling on real walls, and the shadows keep a little ordinary room detail.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the sage-green painted wooden panelling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### C05 F3 — The door opens on the room — empty-room reference

#### Image prompt — `references/v21_c05_r2.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `95f8c0ab-4fd7-41c7-a379-76ae45dda0d2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_000210_95f8c0ab-4fd7-41c7-a379-76ae45dda0d2.png
**References, in submission order**
- @Image 1: `content/video_21_assets/references/v21_c05_r1.png` · Higgsfield media `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`
**md5** - `d8f167042e8cad5d66327ddd3518c2fa`

````text
Edit the supplied image. Reproduce it exactly - the same English Arts-and-Crafts Christmas great room, the same coffered ceiling, the same camera position, framing, lens and lighting, the same furniture, Christmas tree, fireplace, rug and the exact same projected Christmas artwork on the walls and ceiling, pixel for pixel wherever possible. The ONLY change: remove all children completely. The room is empty of people - no children, no adults, no pets. Where the children stood, show the floor, rug and sofa that were behind them, continuing naturally. Keep the projection, colours and sharpness unchanged. No text, no watermark.
````

### C06 — The bed bounce

#### Image prompt — `starting_frames/v21_c06_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `15262a8d-8083-4414-b8e0-aca9abaed7b2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_000437_15262a8d-8083-4414-b8e0-aca9abaed7b2.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
- @Image 2: `content/video_21_assets/references/v21_c05_r1.png` · Higgsfield media `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`
**md5** - `8cfd224b370b66c68489b87c78e57f13`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same natural low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, fully dressed for winter in a cranberry-red brushed-cotton Christmas pyjama set patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a bright-proportioned English country bedroom with a high CATHEDRAL CEILING: two steep sloping plaster planes rise from the side walls to meet at a crisp central ridge. A white-painted iron bed with a tall arched headboard is centred on the flat back wall between two tall casement windows with white-painted wooden frames and slim glazing bars, white bedding with a rust-orange knitted throw, sage-green painted bedside chests, wide honey-oak floorboards and a soft cream wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and copper and cream ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two steep sloping ceiling planes remain clearly three-dimensional, meeting at a crisp central ridge. The sleigh and the ceiling picture fold at the ridge and are foreshortened along each slope before continuing down the walls. The flat wall, the white-painted wooden window frames and glazing bars and the arched iron headboard carry properly foreshortened portions of the same continuous projection across their faces. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the soft cream wool rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his cotton pyjama top catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

NATURAL, LESS CINEMATIC LOOK - a little less cinematic than a film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster or an advert. True-to-life colour and contrast as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting and no heightened fantasy glow on the children. The projection is still dense, bright and colourful, but it reads as the real light of a home Christmas projector falling on real walls, and the shadows keep a little ordinary room detail.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v21_c06_g1.mp4` — FOR REVIEW

**Settings** - seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on
**Job** - `fa36df2f-9828-4f1a-9943-ddcdf123eee1`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022718_fa36df2f-9828-4f1a-9943-ddcdf123eee1.mp4
**Attached, in submission order**
- @Image 1 (image reference): `starting_frames/v21_c06_g1.png` · Higgsfield media `15262a8d-8083-4414-b8e0-aca9abaed7b2`
**md5** - `3b6e6d0183c42c712b2b4cfc4989a1fa`

````text
PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas projection on the walls and the cathedral ceiling is a MOVING CARTOON FILM playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. In every second of the clip, big parts of the picture visibly move:
1. SNOWFALL - hundreds of big glowing projected snowflakes stream continuously down across the whole projection, over the walls and the ceiling, falling fast like a real snowstorm seen through a window, about half the wall height every second. They are flat light on the walls and ceiling, never real snow in the room. This constant streaming snow is the most obvious motion in the frame.
2. SANTA'S SLEIGH - Santa's red sleigh and eight reindeer FLY across the ceiling from one side to the other, clearly travelling and changing place every second, crossing about a third of the ceiling each second, reindeer legs galloping and the golden trail streaming behind. It is never parked in one spot.
3. CHIMNEY SMOKE - thick white smoke pours upward out of every chimney on the wall, puff after puff, rising and curling fast.
4. SKY - the huge golden full moon glows and its halo pulses brighter and dimmer; the drifting snowflakes swirl across the ceiling; the golden stars twinkle; now and then a shooting star streaks across.
5. VILLAGE - the little red steam train chugs along its snowy track pulling its wagons of presents; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock trot.
Only the buildings and the moon hold still; everything else in the projection moves all the time, from the first frame to the last. The room and the boy are real photographic phone footage; only the projected picture is animated.

CAMERA - ONE slow tilt from UP to DOWN, the opposite of the other clips in this set.
0.0s: the camera is aimed only a little higher than @Image 1 - NOT far up. The fully projected cathedral ceiling fills roughly the upper half of the frame, the projected wall and the top of the headboard fill the middle, and THE BOY is in the lower part of the frame, fully visible from head to feet, mid-jump. Every visible part of the ceiling is covered with the projection - no bare plaster anywhere.
0.0-4.0s: the camera tilts DOWN slowly and smoothly, like a calm parent filming.
4.0-5.0s: it eases to a stop exactly on the framing of @Image 1.
One continuous take: no cut, no zoom, no push-in, no pull-back, never a tilt up.

PER-SECOND ANIMATION TRACK (while the camera tilts down):
0-1s: snow streams down the whole projection; the sleigh is already flying across the ceiling; smoke pours from the workshop chimneys.
1-2s: the sleigh has flown a third of the way across the ceiling; the steam train chugs along its track.
2-3s: the sleigh flies on across the ceiling; fresh smoke puffs rise above the workshop roofs; the elves hammer in the workshop windows.
3-4s: the sleigh keeps flying toward the far side of the ceiling; a shooting star streaks across.
4-5s: snow still streaming, smoke still rising, sleigh still flying in the last frame.

THE BOY JUMPS AT REAL SPEED for all five seconds: quick springy bounces, about one full jump every 1.2 seconds. Each jump: knees bend, a fast push-off, a brief moment in the air, a fast drop under normal gravity, the mattress compressing and springing back; arms swinging, laughing. Never slow motion, never floaty.

Wholesome family Christmas scene, a child at home with his family at Christmas. Crisp real iPhone footage at night, handheld, real-time speed, sharp from first frame to last.

ASSET ROLES: @Image 1 is the approved still that controls a bright-proportioned English country bedroom with a high CATHEDRAL CEILING: two steep sloping plaster planes rise from the side walls to meet at a crisp central ridge. A white-painted iron bed with a tall arched headboard is centred on the flat back wall between two tall casement windows with white-painted wooden frames and slim glazing bars, white bedding with a rust-orange knitted throw, sage-green painted bedside chests, wide honey-oak floorboards and a soft cream wool rug. Preserve exact child identity, clothing, furniture, colours and the full projected artwork of @Image 1; its framing is the END framing of this clip.

SUBJECTS:
THE BOY - exactly one child, a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, fully dressed for winter in a cranberry-red brushed-cotton Christmas pyjama set patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall shown in @Image 1 and the whole cathedral ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in @Image 1. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

DO NOT INCLUDE: a still, frozen or printed-looking projection; a projection that only twinkles; a sleigh parked in one place; chimneys without smoke; snow that does not fall; a steam train and elves that do not move; bare, white or unprojected ceiling or wall; a camera that starts far up on the ceiling; a camera that tilts up; zoom, push-in or pull-back; slow-motion or floaty jumping; real snow or particles in the air of the room; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
````

### C07 — The whole Christmas room

#### Image prompt — `starting_frames/v21_c07_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `5579aef2-ea00-428d-9f24-52a2f7736941`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_000437_5579aef2-ea00-428d-9f24-52a2f7736941.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
- @Image 2: `content/video_21_assets/references/v21_c05_r1.png` · Higgsfield media `2fcbb86b-b10d-4ce6-8cd7-68d4ace96615`
**md5** - `583b98aad9099a9c5d172f2040be3074`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the children only; this is a different room of the same house, described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about five with warm brown skin and long black braids tied with small gold beads; a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut. Both fully dressed in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height English country Christmas family room with a high TRAY CEILING: a broad flat raised centre surrounded by four gently sloping plaster border planes and a wide flat perimeter ledge with crisp stepped moulding. White-painted tongue-and-groove panelling lines the walls. A tall chimney breast of red brick stands on the back wall with a dark oak beam mantel; a wide bay of casement windows with white-painted wooden frames and slim glazing bars fills the left wall and a pair of white-painted wooden French doors sits on the right. Wide honey-oak floorboards, a large moss-green corduroy sectional sofa, a square tan leather ottoman and a soft rust-and-cream striped wool rug. A different room from @Image 2 - not the same living room - seen from the middle of the family room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, copper and cream baubles, dried orange slices, plaid ribbon and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cream-and-rust knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The raised flat centre, the four sloping border planes and the stepped perimeter ledge remain clearly three-dimensional, meeting at crisp moulded edges. The sleigh and the snowflakes bend at every edge of the tray and are foreshortened along each sloping border before continuing onto the walls. The tall chimney breast receives a continuous picture with clear folds at its two projecting corners. The white-painted wooden window frames, glazing bars, French doors and tongue-and-groove panelling carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the soft rust-and-cream striped wool rug, the moss-green corduroy sectional sofa, the square tan leather ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

NATURAL, LESS CINEMATIC LOOK - a little less cinematic than a film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster or an advert. True-to-life colour and contrast as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting and no heightened fantasy glow on the children. The projection is still dense, bright and colourful, but it reads as the real light of a home Christmas projector falling on real walls, and the shadows keep a little ordinary room detail.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the white-painted tongue-and-groove panelling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````


#### Video prompt — `clips/v21_c07_g1.mp4` — FOR REVIEW

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `a72a0ad2-168f-44de-8109-1e74b04ff418`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260924_022843_a72a0ad2-168f-44de-8109-1e74b04ff418.mp4
**Attached, in submission order**
- start_image: `starting_frames/v21_c07_g1.png` · Higgsfield media `5579aef2-ea00-428d-9f24-52a2f7736941`
**md5** - `59ba2ec04636c984e7e0b5b982f842da`

````text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, tray ceiling panel and ceiling detail. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas family room while a projected Christmas village picture is PLAYING across the back wall and the entire tray ceiling and its architectural details, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls a spacious double-height English country Christmas family room with a high TRAY CEILING: a broad flat raised centre surrounded by four gently sloping plaster border planes and a wide flat perimeter ledge with crisp stepped moulding. White-painted tongue-and-groove panelling lines the walls. A tall chimney breast of red brick stands on the back wall with a dark oak beam mantel; a wide bay of casement windows with white-painted wooden frames and slim glazing bars fills the left wall and a pair of white-painted wooden French doors sits on the right. Wide honey-oak floorboards, a large moss-green corduroy sectional sofa, a square tan leather ottoman and a soft rust-and-cream striped wool rug. Preserve exact child identity, clothing, furniture, colours, full existing projection and opening framing in the supplied image.

SUBJECTS:
THE BOY - a boy of about eight with fair skin, light freckles and straight sandy-blond hair in a short cut, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE GIRL - a girl of about five with warm brown skin and long black braids tied with small gold beads, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in cranberry-red brushed-cotton Christmas pyjama sets patterned with small white gingerbread men, green candy canes and silver stars, with matching loose pyjama trousers and grey wool socks. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole tray ceiling. Everything glowing on the plaster, wall material and ceiling details is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a cosy CHRISTMAS TOY WORKSHOP VILLAGE: Santa's elves hammer and paint toys inside glowing timber workshops with round windows, a little red steam train pulls wagons of presents along a snowy track between them, reindeer graze in a fenced paddock beside a candy-cane striped barn, and tall snow-laden fir trees rise between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the workshop roofs into a continuous Christmas panorama. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly past a huge glowing golden full moon through a sky of drifting snowflakes and twinkling golden stars, their long curling red-and-gold ribbon trail woven among tiny golden lights. Unmistakably Christmas Eve, glowing gold, cranberry red and deep midnight blue dominant with evergreen accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

PROJECTED ANIMATION - THE MAIN SUBJECT. The Christmas picture on the walls and ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, not a still illustration; only the projected picture is animated, while the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in every frame from the first to the last, independent of the camera. The architecture, the workshops, the barn and the moon stay put; everything drawn around them travels.
- MOON AND SNOW SKY: the huge golden full moon glows and its halo pulses brighter and dimmer; big drifting snowflakes swirl in wide visible eddies across the whole tray ceiling; the golden stars twinkle; now and then a shooting star streaks across.
- SANTA'S SLEIGH AND EIGHT REINDEER: the team FLIES. It travels in one smooth sweeping arc across the ceiling, starting where it sits in the start image and flying past the huge golden full moon and on across the tray ceiling, covering about one quarter of the ceiling's width every second, so it is in a clearly different place every second. The reindeer's legs gallop in a running cycle, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY workshop chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from the chimney below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the little red steam train chugs steadily along its snowy track pulling its wagons of presents, puffing white steam; the elves hammer and paint in the glowing workshop windows; the reindeer in the paddock toss their heads and trot.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall, flat on the wall and ceiling surfaces.
- LIGHTS: bright gold sparkle waves travel along the garlands and ribbons; stars twinkle; now and then a shooting star streaks across the ceiling.
PER-SECOND ANIMATION TRACK (4 s):
0-1s: snowflakes are already swirling across the tray ceiling; the sleigh team is already flying, reindeer galloping; smoke rises from every workshop chimney on the back wall; the steam train chugs along its track.
1-2s: the sleigh has moved a quarter of the ceiling and is crossing the golden moon; snow drifts down the walls; the elves hammer in the workshop windows.
2-3s: as the camera tilts up the moon's halo pulses and the snowflakes swirl; the sleigh flies on past the moon.
3-4s: the sleigh keeps flying toward the far side of the tray ceiling, snow still swirling, smoke still rising, the train still chugging, a shooting star streaking across - all moving in the final frame.
All of this is flat projected light lying on the real plaster, trim and window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE GIRL bounces on the sofa cushions with both arms up, laughing. THE BOY turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE GIRL pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE BOY keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree, only far enough that the tray ceiling fills the upper half of the frame - it never tilts past the projected picture. The ENTIRE tray ceiling - the raised flat centre, the four sloping border planes and the stepped perimeter ledge - is covered with the projection: starry midnight sky, the golden full moon, the swirling snowflakes and the sleigh - no bare white plaster, no unprojected centre, border or moulding anywhere in view; the ribbons rippling along it, the travelling gold light waves spreading outward from the moon and the sleigh team still flying on across the ceiling. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their cotton pyjamas read clearly. One continuous take with no cut. The camera makes one move per beat and no more. THE GIRL stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: bare, blank, white or partly unprojected tray ceiling, border plane, ledge or wall in any frame, especially at the end when the camera looks up; a camera that tilts up beyond the projected picture; a projection appearing, fading in or revealing itself; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; blur; a cut; on-screen text; subtitles.

SURFACE MAPPING - The raised flat centre, the four sloping border planes and the stepped perimeter ledge of the tray ceiling remain stationary. Drawings bend at every edge of the tray, fold around the red-brick chimney corners and carry across the white-painted window frames, glazing bars, French doors and tongue-and-groove panelling, with correct surface perspective and occlusion. All physical architecture stays stationary.

MOTION GUARDRAILS - Failed if: the snowflakes do not swirl or the moon's halo never pulses; the sleigh stays in one place; any chimney has no rising smoke; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture rotates or slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````

