# Video 11 - B-roll image archive

**C01 hook status (2026-09-21):** g4 completed and saved as the final requested reroll; exact g3 prompt, settings and approved starting frame. Awaiting Daniel's review; earlier takes retained.

**Current status (2026-09-21):** C05 take 4 completed and added to the existing board for review; takes 1, 2 and 3 retained. Five-second request at 720p with the original closed-door starting frame and corrected C07 clip as room reference; camera-only prompt correction for continuous simultaneous forward movement and upward tilt. This round affects C05 only.

**Settings:** Higgsfield `gpt_image_2_5`, `variant=sunburst`, `resolution=2k`, `quality=medium`, `aspect_ratio=9:16`, `count=1`. Canonical reference role `image` is mapped by the backend to `image_references`.

## Reusable blocks

Camera and pose paragraphs are preserved from the named source prompts. Projection density and sharpness blocks below are copied from v10 take 2, which archives their lineage to approved v9 take 4. Full assembled submitted text is stored per shot below.

### opacity
```text
HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely. 
```

### antiwash
```text
It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white. 
```

### origin
```text
AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.  
```

### falloff
```text
There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room. 
```

### sharp
```text
The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.
```

### dark
```text
AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn. 
```

## C02 - starting frame

**Frame:** `starting_frames/v11_c02_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** bbfc652c-e9eb-4430-9b53-610b56917312
**Status:** Completed, saved locally, awaiting Daniel's review.
**References, in attached order:**
1. `../video_1_assets/starting_frames/v1_c02_g1.png` - 1cdfcc53-e771-4bba-9eab-b1788346098b - role image (backend image_references)
2. `../../product_images/box_festive_green_g2.png` - 2597b25d-60d1-4060-9602-32b0ee26c2f7 - role image (backend image_references)

Reused from v10 C02 image take 1 - changed: Changed hands/skin/sleeves; table or counter and background; C05 door. Removed background blur per current brief. C04 port wording corrected to the documented dome-body socket.

### Image prompt
```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 38, with warm medium-brown skin and softly rounded short natural nails, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a ivory cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a rich honey-toned solid elm dining table with broad flowing grain and a matte finish, a substantial straight edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a sharply resolved traditional Christmas dining room: muted forest-green walls with cream picture rails, a cream limestone fireplace with brass candleholders and red knitted stockings, a Christmas tree with red glass baubles and gold ribbon to the left, and a built-in dark walnut bookcase to the right. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the elm table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte elm, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt - take 1

**Clip:** clips/v11_c02_g1.mp4
**Settings:** seedance_2_5; mode omni_reference; 720p; 9:16; duration 4s; count 1; generate_audio true; multi_shots false; use_unlim false; declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612.
**Job ID:** 4749d6c1-fcdf-44dc-a192-b071bb1df133
**Status:** Completed and saved locally; awaiting Daniel's selection. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested duration 4s; audio stream present; 1718870 bytes.
**Sampled visual review:** Review flag: the box opens and the projector exits the frame, but the lift is one-handed instead of the requested two-handed lift. The carton front also appears plain in the render. Single generation retained; no reroll.
**References, in order:**
- starting_frames/v11_c02_g1.png | bbfc652c-e9eb-4430-9b53-610b56917312 | submitted role start_image
- Existing archived unboxing-mechanics uploaded media; exact local source mapping not recorded in v10 archive. Reused unchanged. | 1d2e8a8d-1e49-422a-8b04-d1a1230096a4 | submitted role video
**Backend adjustments:** {"medias[1].role": {"requested": "video", "used": "video_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v10 C02 video take 1 - changed: room/product-scene nouns to match v11; C05-C07 replace absent carnival elements with the existing workshop, train, elves, bells and ribbons, and add Daniel's explicitly requested continuous-motion checks. All source beat times retained. C05 uses the corrected 5-second g2 source and a reference-only room image, never an end frame.

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a honey-toned elm table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a ivory cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a honey-toned elm table fills the frame: broad flowing timber grain, a matte finish and a substantial straight edge. A lit cream pillar candle sits at the left, fir sprigs with white berries and small antique gold and pearl-white baubles beside it, and behind it, sharply in focus, muted forest-green walls with cream picture rails, a cream limestone fireplace with brass candleholders and red knitted stockings, a Christmas tree with red glass baubles and gold ribbon to the left, and a built-in dark walnut bookcase to the right. The candle, the fir, the berries, the baubles, the fireplace and the tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the honey-toned elm table, lid flaps folded back, with the candle, the fir, the berries, the fireplace and the tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
```

#### Exact source edits - in application order

1. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
deep burgundy wool
TO:
ivory cable-knit wool
```

2. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
limed white-oak
TO:
honey-toned elm
```

3. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
[5] LOCATION - a honey-toned elm table fills the frame: pale blond timber whose open grain is filled with a chalky white lime wax so the pores read as fine white lines drifting across the surface, finished dead matte with no sheen at all, and a simple square edge. A lit cream pillar candle sits at the left, fir sprigs with white berries and small antique gold and pearl-white baubles beside it, and behind it, softly out of focus, chalk-white painted shiplap boards, a chalk-white painted brick fireplace with a simple pale oak mantel and cream knitted stockings hanging from it, a narrow shelf high on the wall carrying a row of pale green sea-glass jars, and a decorated Christmas tree with warm white fairy lights and antique gold and pearl-white ornaments. The candle, the fir, the berries, the baubles, the defocused fireplace and the defocused tree must still be in the final frame.
TO:
[5] LOCATION - a honey-toned elm table fills the frame: broad flowing timber grain, a matte finish and a substantial straight edge. A lit cream pillar candle sits at the left, fir sprigs with white berries and small antique gold and pearl-white baubles beside it, and behind it, sharply in focus, muted forest-green walls with cream picture rails, a cream limestone fireplace with brass candleholders and red knitted stockings, a Christmas tree with red glass baubles and gold ribbon to the left, and a built-in dark walnut bookcase to the right. The candle, the fir, the berries, the baubles, the fireplace and the tree must still be in the final frame.
```

4. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
the defocused fireplace and the defocused tree
TO:
the fireplace and the tree
```

#### Animation take history
Take 1 completed and saved locally. Sampled review recorded above; awaiting Daniel's selection. C01 and videos 12-14 were not animated in this round.


### Take history
Take 1 only. Not reviewed by Daniel. No previous take overwritten.

## C03 - starting frame

**Frame:** `starting_frames/v11_c03_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** 4b0ce2fa-f22e-4fdc-a781-0a2f43789130
**Status:** Completed, saved locally, awaiting Daniel's review.
**References, in attached order:**
1. `../video_1_assets/starting_frames/v1_c03_g1.png` - 7ccdd557-bfee-45b0-a067-0652320f537b - role image (backend image_references)
2. `../video_10_assets/starting_frames/v10_c03_g1.png` - 89ed549a-35bb-4e66-8865-c5a112bc239a - role image (backend image_references)

Reused from v10 C03 image take 1 - changed: Changed hands/skin/sleeves; table or counter and background; C05 door. Removed background blur per current brief. C04 port wording corrected to the documented dome-body socket.

### Image prompt
```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 38, with warm medium-brown skin and softly rounded short natural nails: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a ivory cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same ivory cable-knit sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a pale ivory honed travertine counter, small natural pores and delicate beige mineral veins, matte stone with a straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: deep sage-green inset cabinets with aged brass cup pulls, warm ivory square ceramic tiles, a brushed brass range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt - take 1

**Clip:** clips/v11_c03_g1.mp4
**Settings:** seedance_2_5; mode omni_reference; 720p; 9:16; duration 4s; count 1; generate_audio true; multi_shots false; use_unlim false; declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612.
**Job ID:** a41072e9-50d5-4bf5-9c21-745e7bfe12dc
**Status:** Completed and saved locally; awaiting Daniel's selection. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested duration 4s; audio stream present; 1717182 bytes.
**Sampled visual review:** Sampled frames show the projector lifted with both hands, lowered onto the counter and released.
**References, in order:**
- starting_frames/v11_c03_g1.png | 4b0ce2fa-f22e-4fdc-a781-0a2f43789130 | submitted role start_image
**Backend adjustments:** {}

Reused from v10 C03 video take 1 - changed: room/product-scene nouns to match v11; C05-C07 replace absent carnival elements with the existing workshop, train, elves, bells and ribbons, and add Daniel's explicitly requested continuous-motion checks. All source beat times retained. C05 uses the corrected 5-second g2 source and a reference-only room image, never an end frame.

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale ivory honed travertine kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in ivory cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a pale ivory honed travertine countertop - small natural pores and delicate beige mineral veins, matte stone and a straight square edge - fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with deep sage-green inset cabinets with aged brass cup pulls, a brushed brass range built into the tall cabinet run on the left, a warm ivory square ceramic tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays crisp and in focus, matching the start image. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the travertine counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The travertine is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
```

#### Exact source edits - in application order

1. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
deep burgundy wool
TO:
ivory cable-knit wool
```

2. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
thick end-grain walnut butcher-block
TO:
pale ivory honed travertine
```

3. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish
TO:
small natural pores and delicate beige mineral veins, matte stone and a straight square edge
```

4. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
chalk-white shaker cabinets with polished nickel bin pulls
TO:
deep sage-green inset cabinets with aged brass cup pulls
```

5. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a cream enamel range
TO:
a brushed brass range
```

6. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches
TO:
a warm ivory square ceramic tile backsplash
```

7. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
white berries along the top
TO:
red berries along the top
```

8. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
The kitchen stays soft and out of focus.
TO:
The kitchen stays crisp and in focus, matching the start image.
```

9. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
the timber
TO:
the stone
```

10. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
butcher-block counter
TO:
travertine counter
```

11. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
The butcher block is hard
TO:
The travertine is hard
```

#### Animation take history
Take 1 completed and saved locally. Sampled review recorded above; awaiting Daniel's selection. C01 and videos 12-14 were not animated in this round.


### Take history
Take 1 only. Not reviewed by Daniel. No previous take overwritten.

## C04 - starting frame

**Frame:** `starting_frames/v11_c04_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** e243effc-2c21-4bed-9551-e592483315ca
**Status:** Completed, saved locally, awaiting Daniel's review.
**References, in attached order:**
1. `../video_1_assets/starting_frames/v1_c04_g1.png` - 0327ed0d-ff56-40c1-a9a9-389a7ceb9916 - role image (backend image_references)
2. `../video_10_assets/starting_frames/v10_c04_g1.png` - 1d69a04c-84ad-4a97-8d55-d5ce334848c1 - role image (backend image_references)

Reused from v10 C04 image take 1 - changed: Changed hands/skin/sleeves; table or counter and background; C05 door. Removed background blur per current brief. C04 port wording corrected to the documented dome-body socket.

### Image prompt
```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 38, with warm medium-brown skin and softly rounded short natural nails: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a ivory cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a pale ivory honed travertine counter, small natural pores and delicate beige mineral veins, matte stone with a straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: deep sage-green inset cabinets with aged brass cup pulls, warm ivory square ceramic tiles, a brushed brass range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt - take 1

**Clip:** clips/v11_c04_g1.mp4
**Settings:** seedance_2_5; mode omni_reference; 720p; 9:16; duration 4s; count 1; generate_audio true; multi_shots false; use_unlim false; declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612.
**Job ID:** 3a7b4dc6-57a3-4f8f-adb5-3629e268e08b
**Status:** Completed and saved locally; awaiting Daniel's selection. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested duration 4s; audio stream present; 1295394 bytes.
**Sampled visual review:** Sampled frames show the cable entering the lower body socket, followed by red illumination.
**References, in order:**
- starting_frames/v11_c04_g1.png | e243effc-2c21-4bed-9551-e592483315ca | submitted role start_image
**Backend adjustments:** {}

Reused from v10 C04 video take 2 - changed: room/product-scene nouns to match v11; C05-C07 replace absent carnival elements with the existing workshop, train, elves, bells and ribbons, and add Daniel's explicitly requested continuous-motion checks. All source beat times retained. C05 uses the corrected 5-second g2 source and a reference-only room image, never an end frame.

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
THE LEFT HAND - a woman's hand in a ivory cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same ivory cable-knit sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a pale ivory honed travertine countertop - small natural pores and delicate beige mineral veins, matte stone and a straight square edge - fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with deep sage-green inset cabinets with aged brass cup pulls, a brushed brass range built into the tall cabinet run on the right, a warm ivory square ceramic tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays crisp and in focus, matching the start image. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

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
```

#### Exact source edits - in application order

1. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
deep burgundy wool
TO:
ivory cable-knit wool
```

2. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
deep burgundy sleeve
TO:
ivory cable-knit sleeve
```

3. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
thick end-grain walnut butcher-block
TO:
pale ivory honed travertine
```

4. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish
TO:
small natural pores and delicate beige mineral veins, matte stone and a straight square edge
```

5. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
chalk-white shaker cabinets with polished nickel bin pulls
TO:
deep sage-green inset cabinets with aged brass cup pulls
```

6. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a cream enamel range
TO:
a brushed brass range
```

7. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches
TO:
a warm ivory square ceramic tile backsplash
```

8. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
white berries along the top
TO:
red berries along the top
```

9. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
The kitchen stays soft and out of focus.
TO:
The kitchen stays crisp and in focus, matching the start image.
```

10. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
the timber
TO:
the stone
```

#### Animation take history
Take 1 completed and saved locally. Sampled review recorded above; awaiting Daniel's selection. C01 and videos 12-14 were not animated in this round.


### Take history
Take 1 only. Not reviewed by Daniel. No previous take overwritten.

## C05 - starting frame

**Frame:** `starting_frames/v11_c05_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** 6a0df249-6245-439e-a380-e9bbdf6dc580
**Status:** Completed, saved locally, awaiting Daniel's review.
**References, in attached order:**
1. `../video_1_assets/starting_frames/v1_c05_g2.png` - c9e1f960-9e19-4b9b-ad88-8f5298db1880 - role image (backend image_references)
2. `../video_10_assets/starting_frames/v10_c05_g1.png` - c301edff-f38f-42fc-bdde-d914d68ab37d - role image (backend image_references)

Reused from v10 C05 image take 1 - changed: Changed hands/skin/sleeves; table or counter and background; C05 door. Removed background blur per current brief. C04 port wording corrected to the documented dome-body socket.

### Image prompt
```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the ivory cable-knit sleeve and no jewellery, with warm medium-brown skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a forest-green painted solid wood door with three equal horizontal recessed panels, satin finish and fine natural brush texture, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest-green paint reads clearly as a rich green rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt - take 1

**Clip:** clips/v11_c05_g1.mp4
**Settings:** seedance_2_5; mode omni_reference; 720p; 9:16; duration 5s; count 1; generate_audio true; multi_shots false; use_unlim false; declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612.
**Job ID:** 057801b4-0ec9-4cfd-b356-d833a7a1d06d
**Status:** Completed and saved locally; awaiting Daniel's selection. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; requested duration 5s; audio stream present; 4057505 bytes.
**Sampled visual review:** Requested exactly 5 seconds. The room image was attached only as image_references, with no end frame. Sampled frames show children moving as the doorway reveals them and continuing through the scene. Bright moving light streaks are visible; review whether the larger projected characters travel enough.
**References, in order:**
- starting_frames/v11_c05_g1.png | 6a0df249-6245-439e-a380-e9bbdf6dc580 | submitted role start_image
- references/v11_c05_r1.png | dda4701e-8d9d-4351-99f8-60bb9093cf68 | submitted role image
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v10 C05 video take 2 - changed: room/product-scene nouns to match v11; C05-C07 replace absent carnival elements with the existing workshop, train, elves, bells and ribbons, and add Daniel's explicitly requested continuous-motion checks. All source beat times retained. C05 uses the corrected 5-second g2 source and a reference-only room image, never an end frame.

```text
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Image 1 is ONE PAUSED FRAME of that movie. At 0.0s it un-pauses and keeps running to the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Image 1 is the great room behind that door and the authority on its layout, barrel-vault ceiling, furniture, the two children, their clothes, the colours, and the exact set and style of every projected shape.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Every chimney in the North Pole Christmas workshop village pours smoke like a real wood fire on a cold still evening: it boils out of the pot, leans right, climbs and widens and thins away, and the next plume is already forming behind it. Not one chimney in the village is without its plume.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the floating baubles and candy canes turn slowly as they drift, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white barrel-vault ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. The door opens on two kids in the middle of doing something, not on two kids standing waiting to be filmed, and neither of them is ever still. THE BOY, the child on the right, initially facing the doorway but already turning toward the sofa as he runs, is already mid-stride as the gap widens; he takes three or four quick real steps and LAUNCHES HIMSELF UP ONTO the big ivory linen sectional sofa that wraps the room right behind him, landing on his knees with both arms flying up, laughing, and keeps bouncing there until the last frame. THE GIRL, the child on the left with the long copper-red braid, is already running as the door opens; she runs on across the room toward the lit Christmas tree without breaking step, tips her head right back to look straight up at the great radiating star on the barrel-vault ceiling and throws one arm up pointing at it, mouth open, delighted - and she is still moving and still pointing on the last frame. Both runs are ordinary excited-kid running at real speed with real weight: feet landing, knees bending, arms swinging, hair and jumpers moving with them. Projected shapes slide down the walls behind them and pass across their backs.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: the boy ends the clip bouncing on the sofa, the girl ends it still running and still pointing up at the ceiling. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Image 1 is a room-content reference, NOT an end frame and NOT a target pose. Do not converge to its still arrangement. The children are already mid-run before the door uncovers them; show moving limbs and changing positions from their first visible instant, with no pause to match the reference.
```

#### Exact source edits - in application order

1. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
flat coffered ceiling
TO:
curved barrel-vault ceiling
```

2. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
coffered ceiling
TO:
barrel-vault ceiling
```

3. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
drywall
TO:
plaster
```

4. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE AURORA
TO:
THE RIBBONS
```

5. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
aurora
TO:
ribbons
```

6. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
ripple rings
TO:
travelling gold light waves
```

7. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE RIPPLE RINGS
TO:
THE GOLD LIGHT WAVES
```

8. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE FERRIS WHEEL AND THE CAROUSEL
TO:
THE TOY TRAIN AND THE ELVES
```

9. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
Ferris wheel and the carousel
TO:
toy train and the elves
```

10. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a Ferris wheel or a carousel that does not turn
TO:
a toy train that does not travel or elves that do not move
```

11. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
four-panel oxblood-red door
TO:
three-panel forest-green door
```

12. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
oxblood-red door
TO:
forest-green door
```

13. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
bare forearm and its thin gold bangle
TO:
bare forearm and its ivory sleeve, with no jewellery
```

14. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
snowy storybook village
TO:
North Pole Christmas workshop village
```

15. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE TOY TRAIN AND THE ELVES. The enormous lit Ferris wheel TURNS steadily about its lit hub, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel TURNS the other way under its striped canopy, its horses rising and falling on their twisted brass poles as they come round, the lights along every scallop of the canopy chasing round the rim. Both keep turning from the first frame to the last.
TO:
THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
```

16. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE GOLD LIGHT WAVES. The seven concentric rings SPREAD OUTWARD from the great star across the ceiling like rings on water, each one travelling away from the core, widening and thinning and fading as it reaches the walls, while a fresh ring is already forming at the centre behind it, so the spread never stops.
TO:
THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
```

17. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
Everything else travels too: the tiny skating silhouettes circling on the frozen pond, shooting stars streaking and fading, the floating baubles and candy canes turning slowly as they drift, the big gold bells swinging gently on their crimson bow with the clappers glowing inside them, the lit shopfront windows and the church clock flickering warm, and wisps of crimson and gold cloud drifting between the ribbons bands. Only the glowing clock face of the church holds position; it simply breathes brighter and dimmer.
TO:
Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the floating baubles and candy canes turn slowly as they drift, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.
```

18. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, steps up into every sunken coffer and back down onto the beams between them, and breaks where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.
TO:
ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.
```

19. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, its spreading travelling gold light waves, the radiating ribbons, the flying sleigh, pouring snow and twinkling stars run into every single coffer panel and over every beam, right into all four corners. No bare un-animated coffer panel and no bare white beam anywhere in the closing framing.
TO:
THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.
```

20. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
the child on the right with his back to camera
TO:
the child on the right, initially facing the doorway but already turning toward the sofa as he runs
```

21. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
big oatmeal linen sectional sofa
TO:
big ivory linen sectional sofa
```

22. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
long wavy hair
TO:
long copper-red braid
```

23. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
the toy train and the elves turn
TO:
the toy train travels and the elves work
```

24. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
the toy train and the elves keep turning
TO:
the toy train and the elves keep moving
```

25. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
an un-animated coffer panel
TO:
an un-animated patch of the vault
```

26. Daniel explicitly requested continuous wall/ceiling motion, reference-only room image and no frozen children.
```text
FROM:

TO:
CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Image 1 is a room-content reference, NOT an end frame and NOT a target pose. Do not converge to its still arrangement. The children are already mid-run before the door uncovers them; show moving limbs and changing positions from their first visible instant, with no pause to match the reference.
```

#### Animation take history
Take 1 completed and saved locally. Sampled review recorded above; awaiting Daniel's selection. C01 and videos 12-14 were not animated in this round.


### Take history
Take 1 only. Not reviewed by Daniel. No previous take overwritten.


### Video prompt - take 2

**Clip:** clips/v11_c05_g2.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "6a0df249-6245-439e-a380-e9bbdf6dc580"}, {"role": "image", "value": "dda4701e-8d9d-4351-99f8-60bb9093cf68"}]}
**Job ID:** c7c75cb6-0103-4fa7-95a5-ab42dc93a4e9
**Status:** Completed and saved locally; take 2 added to the board for Daniel's review. One generation in this revision round.
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; requested 5s; audio stream present; 6406442 bytes.
**Sampled visual review:** Take 2 review flag: despite removing the reference-position cues and explicitly banning a matching pause, the children still gather near the reference arrangement and linger around 2.0-3.2 seconds; the requested uninterrupted run is not achieved. The doorway reveals a moving child at the start. No obvious free-space fireplace object appears in the sampled frames, and projected sleigh motion is visible. Requested 5 seconds; room attached only as image_references, with no end frame. Single revision retained for Daniel's review; no automatic reroll.
**References, in order:**
- starting_frames/v11_c05_g1.png | 6a0df249-6245-439e-a380-e9bbdf6dc580 | submitted role start_image
- references/v11_c05_r1.png | dda4701e-8d9d-4351-99f8-60bb9093cf68 | submitted role image
**Backend adjustments:** {"medias[1].role": {"requested": "image", "used": "image_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v11 C05 video take 1 - only the prompt corrections listed below changed. Same starting frame, model, resolution, duration and media roles. C05 remains exactly a 5-second request with the room as reference-only, never an end frame.

```text
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Image 1 supplies the room design and projection artwork only; it does not specify a frame, a moment in time, the children's positions, or any pose to reproduce. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Image 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the two children's identities and clothes, the colours, and the set and style of projected shapes. Ignore the children's reference positions, orientations and poses completely. It is not a start, intermediate, target or end frame.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole workshop picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white barrel-vault ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. Their play is one uninterrupted action that began before the door opened, with no intermediate pose or rendezvous. THE BOY with close-cropped dark curls follows a direct curving run toward the nearest sofa cushion; without stopping, facing the camera, lining up beside the girl or matching any reference position, his existing run flows straight into a jump onto that cushion and repeated excited bouncing. THE GIRL with the long copper-red braid keeps her own continuous curving run toward the Christmas tree, passing through the room independently; she glances upward and lifts one arm as she runs without planting her feet or interrupting her stride. Their paths do not converge into a side-by-side tableau. They never arrive at, recreate, hold or reset to the poses or arrangement of @Image 1, even for an instant. Movement remains continuous through the middle and last second, with grounded footfalls, bent knees, swinging arms, moving hair and knitwear. Reference-image matching must never interrupt the children's play.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: the boy ends the clip bouncing on the sofa, the girl ends it still running and still pointing up at the ceiling. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Image 1 is only a design and identity reference. There is no time at which the children must occupy its positions. Never interpolate toward it, use it as an intermediate keyframe, line the children up, pause there, then restart. Preserve the already-moving doorway reveal and carry each child's momentum continuously through the entire 5 seconds. No reference pose and no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, limestone and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and arch ribs. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.
```

#### Exact source edits - in application order

1. Remove a temporal target from the room reference.

Before:
```text
@Image 1 is ONE PAUSED FRAME of that movie. At 0.0s it un-pauses and keeps running to the last frame.
```

```text
@Image 1 supplies the room design and projection artwork only; it does not specify a frame, a moment in time, the children's positions, or any pose to reproduce. Behind the closed door the projected movie is already playing, and it keeps running through the last frame.
```

2. Reference identity and layout only.

Before:
```text
@Image 1 is the great room behind that door and the authority on its layout, barrel-vault ceiling, furniture, the two children, their clothes, the colours, and the exact set and style of every projected shape.
```

```text
@Image 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the two children's identities and clothes, the colours, and the set and style of projected shapes. Ignore the children's reference positions, orientations and poses completely. It is not a start, intermediate, target or end frame.
```

3. Eliminate real smoke language above fireplace.

Before:
```text
SMOKE. Every chimney in the North Pole Christmas workshop village pours smoke like a real wood fire on a cold still evening: it boils out of the pot, leans right, climbs and widens and thins away, and the next plume is already forming behind it. Not one chimney in the village is without its plume.
```

```text
SMOKE. Inside the flat projected North Pole workshop picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.
```

4. Keep ornaments on surfaces.

Before:
```text
the floating baubles and candy canes turn slowly as they drift
```

```text
the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces
```

5. Remove reference-position choreography and mid-clip pause.

Before:
```text
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. The door opens on two kids in the middle of doing something, not on two kids standing waiting to be filmed, and neither of them is ever still. THE BOY, the child on the right, initially facing the doorway but already turning toward the sofa as he runs, is already mid-stride as the gap widens; he takes three or four quick real steps and LAUNCHES HIMSELF UP ONTO the big ivory linen sectional sofa that wraps the room right behind him, landing on his knees with both arms flying up, laughing, and keeps bouncing there until the last frame. THE GIRL, the child on the left with the long copper-red braid, is already running as the door opens; she runs on across the room toward the lit Christmas tree without breaking step, tips her head right back to look straight up at the great radiating star on the barrel-vault ceiling and throws one arm up pointing at it, mouth open, delighted - and she is still moving and still pointing on the last frame. Both runs are ordinary excited-kid running at real speed with real weight: feet landing, knees bending, arms swinging, hair and jumpers moving with them. Projected shapes slide down the walls behind them and pass across their backs.
```

```text
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. Their play is one uninterrupted action that began before the door opened, with no intermediate pose or rendezvous. THE BOY with close-cropped dark curls follows a direct curving run toward the nearest sofa cushion; without stopping, facing the camera, lining up beside the girl or matching any reference position, his existing run flows straight into a jump onto that cushion and repeated excited bouncing. THE GIRL with the long copper-red braid keeps her own continuous curving run toward the Christmas tree, passing through the room independently; she glances upward and lifts one arm as she runs without planting her feet or interrupting her stride. Their paths do not converge into a side-by-side tableau. They never arrive at, recreate, hold or reset to the poses or arrangement of @Image 1, even for an instant. Movement remains continuous through the middle and last second, with grounded footfalls, bent knees, swinging arms, moving hair and knitwear. Reference-image matching must never interrupt the children's play.
```

6. Explicit user correction for mid-clip reference snap.

Before:
```text
REFERENCE-ONLY LOCK - @Image 1 is a room-content reference, NOT an end frame and NOT a target pose. Do not converge to its still arrangement. The children are already mid-run before the door uncovers them; show moving limbs and changing positions from their first visible instant, with no pause to match the reference.
```

```text
REFERENCE-ONLY LOCK - @Image 1 is only a design and identity reference. There is no time at which the children must occupy its positions. Never interpolate toward it, use it as an intermediate keyframe, line the children up, pause there, then restart. Preserve the already-moving doorway reveal and carry each child's momentum continuously through the entire 5 seconds. No reference pose and no end frame.
```

7. Prevent fireplace projection becoming a physical room object.

Added paragraph:
```text
SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, limestone and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and arch ribs. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.
```

#### Animation take history - revision round
Take 1 retained. Daniel requested correction: Children settle into the reference arrangement mid-clip, then restart; an animated element above the fireplace appears in free room space.
Take 2 completed, saved and added to board. Awaiting Daniel's selection. No additional reroll.


### Video prompt - take 3

**Clip:** clips/v11_c05_g3.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "6a0df249-6245-439e-a380-e9bbdf6dc580"}, {"role": "video", "value": "2380e078-1cc7-464c-9594-77248972e878"}]}
**Job ID:** 30db6d40-b2c2-4ad8-bdef-a7aa1d64c7e9
**Status:** Completed and saved locally; take 3 added to the board for Daniel's review. This was the single further attempt requested.
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; requested 5s; audio stream present; 3586446 bytes.
**Sampled visual review:** Take 3: sampled frames show the children already active as the door reveals them, then continuing to bounce and turn through the middle rather than gathering into the static reference arrangement. The model adopted the moving reference's sofa bouncing and floor turning instead of the requested game of chase; that action differs from the prompt, but the previous shared pause is not apparent in the sampled frames. The sleigh travels across the ceiling. No obvious detached object above the fireplace is visible in the samples. Five-second request, original closed-door starting frame, moving C07 room reference only; no end frame. Awaiting Daniel's review.
**References, in order:**
- {"role": "start_image", "value": "6a0df249-6245-439e-a380-e9bbdf6dc580", "path": "starting_frames/v11_c05_g1.png"}
- {"role": "video", "value": "2380e078-1cc7-464c-9594-77248972e878", "path": "clips/v11_c07_g2.mp4", "sha256": "569172d47e9420cba8c6e9ae75a39bf9fadaf80cf06a33dbe12c1a039398b149", "duration": 4.05, "audio": true, "original_name": "v11_c07_g2.mp4"}
**Backend adjustments:** {"medias[1].role": {"requested": "video", "used": "video_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v11 C05 video take 2. Same closed-door starting frame, camera beats, Seedance 2.5, 720p and 5-second request. Reference substitution: clips/v11_c07_g2.mp4 replaces references/v11_c05_r1.png as the room-look and child-identity reference to remove the static pose attractor. The video reference has audio; it is not labelled silent. No end frame supplied. Child motion simplified to one uninterrupted game of chase; previous arrival, sofa-jump and ending-pose cues removed. Surface-only projection corrections retained.

```text
CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole workshop picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white barrel-vault ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The copper-braided girl runs a broad curving path across the rug and alongside the sofa; the dark-curled boy follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, limestone and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and arch ribs. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.
```

#### Exact source edits - in application order

1. Replace static pose-bearing room reference with existing moving room reference.

Before:
```text
@Image 1 supplies the room design and projection artwork only; it does not specify a frame, a moment in time, the children's positions, or any pose to reproduce.
```

After / added:
```text
@Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip.
```

2. Clarify distinct roles of closed-door frame and moving visual reference.

Before:
```text
@Image 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the two children's identities and clothes, the colours, and the set and style of projected shapes. Ignore the children's reference positions, orientations and poses completely. It is not a start, intermediate, target or end frame.
```

After / added:
```text
@Video 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.
```

3. Replace arrival-and-sofa-jump sequence with one uninterrupted action.

Before:
```text
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. Their play is one uninterrupted action that began before the door opened, with no intermediate pose or rendezvous. THE BOY with close-cropped dark curls follows a direct curving run toward the nearest sofa cushion; without stopping, facing the camera, lining up beside the girl or matching any reference position, his existing run flows straight into a jump onto that cushion and repeated excited bouncing. THE GIRL with the long copper-red braid keeps her own continuous curving run toward the Christmas tree, passing through the room independently; she glances upward and lifts one arm as she runs without planting her feet or interrupting her stride. Their paths do not converge into a side-by-side tableau. They never arrive at, recreate, hold or reset to the poses or arrangement of @Image 1, even for an instant. Movement remains continuous through the middle and last second, with grounded footfalls, bent knees, swinging arms, moving hair and knitwear. Reference-image matching must never interrupt the children's play.
```

After / added:
```text
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The copper-braided girl runs a broad curving path across the rug and alongside the sofa; the dark-curled boy follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.
```

4. Match uninterrupted running.

Before:
```text
AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone.
```

After / added:
```text
AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone.
```

5. Remove a required ending pose and action switch.

Before:
```text
the boy ends the clip bouncing on the sofa, the girl ends it still running and still pointing up at the ceiling.
```

After / added:
```text
both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose.
```

6. Remove conflicting old finish condition.

Before:
```text
the boy still standing on the floor at the end;
```

After / added:
```text
either child climbing or jumping onto the sofa;
```

7. Avoid any static image convergence and separate reference video behavior.

Before:
```text
REFERENCE-ONLY LOCK - @Image 1 is only a design and identity reference. There is no time at which the children must occupy its positions. Never interpolate toward it, use it as an intermediate keyframe, line the children up, pause there, then restart. Preserve the already-moving doorway reveal and carry each child's momentum continuously through the entire 5 seconds. No reference pose and no end frame.
```

After / added:
```text
REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.
```

8. Prioritize sustained child movement before projection instructions.

After / added:
```text
CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.
```

#### Animation take history - third attempt
Take 2 retained: children still linger near the reference positions in the middle. Daniel authorized exactly one more attempt. Take 3 completed and saved; on board for review. No further generation submitted.


### Video prompt - take 4

**Clip:** clips/v11_c05_g4.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "6a0df249-6245-439e-a380-e9bbdf6dc580"}, {"role": "video", "value": "2380e078-1cc7-464c-9594-77248972e878"}]}
**Job ID:** 51b47bb9-2af7-4489-abfb-e25eea49c11e
**Status:** Completed and saved locally; take 4 added to the board for Daniel's review. This was one generation for the camera-continuity correction.
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; requested 5s; audio stream present; 3815453 bytes.
**Sampled visual review:** Take 4 camera review: sampled framing rises progressively through the doorway, room and ceiling rather than showing the earlier prolonged level hold followed by a separate ceiling swing. The rise looks more gradual in the samples; review the complete playback for pacing. Children remain active, bouncing and turning as in the moving room reference. Projection motion and surface-only instructions retained. Same original starting frame and references; 5-second request at 720p; no end frame. Camera instructions were the only prompt changes.
**References, in order:**
- {"role": "start_image", "value": "6a0df249-6245-439e-a380-e9bbdf6dc580", "path": "starting_frames/v11_c05_g1.png"}
- {"role": "video", "value": "2380e078-1cc7-464c-9594-77248972e878", "path": "clips/v11_c07_g2.mp4", "sha256": "569172d47e9420cba8c6e9ae75a39bf9fadaf80cf06a33dbe12c1a039398b149", "duration": 4.05, "audio": true, "original_name": "v11_c07_g2.mp4"}
**Backend adjustments:** {"medias[1].role": {"requested": "video", "used": "video_references", "reason": "Seedance 2.5 backend expects schema-key media roles"}}

Reused from v11 C05 video take 3 - changed only camera instructions for simultaneous forward movement and constant gentle upward tilt from 0.0s, avoiding the delayed ceiling swing. Same starting frame, moving room reference, children and projection instructions, model, resolution and 5-second duration. No end frame.

```text
CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole workshop picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera advances slowly through the doorway while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The copper-braided girl runs a broad curving path across the rug and alongside the sofa; the dark-curled boy follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, limestone and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and arch ribs. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.
```

#### Exact source edits - in application order

1. Make simultaneous steady camera movement the primary correction, with no late ceiling tilt.

After / added:
```text
CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.
```

2. Remove an opening beat with undefined camera pitch.

Before:
```text
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
```

After / added:
```text
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
```

3. Eliminate the forward-then-ceiling camera sequence.

Before:
```text
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white barrel-vault ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
```

After / added:
```text
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera advances slowly through the doorway while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
```

4. Strengthen camera continuity and avoid conflicting framing language.

Before:
```text
CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.
```

After / added:
```text
CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.
```

5. Update positive lock.

Before:
```text
One single smooth camera move.
```

After / added:
```text
One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout.
```

6. Explicitly ban observed failure.

Before:
```text
two separate camera moves;
```

After / added:
```text
two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing;
```

#### Animation take history - camera correction
Take 3 retained. Daniel reported a forward movement followed by a sudden ceiling tilt. Take 4 completed and saved; on board for review. No further generation submitted.

## C05 F2 - room reference

**Reference:** `references/v11_c05_r1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** dda4701e-8d9d-4351-99f8-60bb9093cf68
**Status:** Completed, saved locally, awaiting Daniel's review.
**References, in attached order:**
1. `../video_10_assets/references/v10_c05_r2.png` - 1f88d0ff-b4ae-4d75-a61b-9e36719f41a5 - role image (backend image_references)
2. `../video_9_assets/references/v9_c05_r4.png` - 1c500339-2855-45b6-bd9b-4c3633b5a272 - role image (backend image_references)

Reused from v10 C05 F2 image take 2; approved v9 take 4 density and sharpness inherited in v10 - changed: Preserved camera and pose paragraphs, opacity, anti-wash, single-origin projection, full-coverage and pinpoint-sharpness wording. Changed room architecture and its surface mapping, children/clothing, Christmas scene content; two-reference roles explicitly updated. C05/C07 share new room and children.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is about six with warm brown skin and close-cropped dark curls; the girl is about nine with light freckled skin and long copper-red hair tied in a loose braid. Both children are fully dressed for winter in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a tall double-height English-country Christmas great room with a continuous cream plaster BARREL-VAULT ceiling: one smooth semicylindrical curve from the left wall up over the centre and down to the right wall, crossed by three evenly spaced shallow cream plaster arch ribs that follow the curve; no flat coffer grid, no ridge and no timber trusses. A tall warm limestone chimney breast stands on the back wall, a plain carved limestone mantel beneath it, two tall rectangular black-framed windows on the left, and a recessed arched doorway on the right. Pale oak floorboards, a large ivory linen sectional sofa, a rectangular upholstered ottoman and a deep-red Persian rug. Seen from the doorway; the new three-panel forest-green door is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the limestone fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole curved barrel vault, every projecting arch rib and the limestone chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one richly detailed NORTH POLE CHRISTMAS EVE panorama: Santa's red-and-gold timber workshop with glowing tiny windows, garland-wrapped columns, snow-covered roof and a toy-filled open doorway; smiling tiny elves in red and green winter clothes packing wooden toys and ribboned presents; a gingerbread bakery with icing-edged gables; rows of snow-laden fir trees hung with red baubles and gold stars; and an illuminated Christmas train carrying overflowing wrapped gifts along the bottom of the walls. Two majestic red-coated NUTCRACKER toy soldiers flank the workshop, with gold braid, black boots and precisely drawn faces. Large luminous CHRISTMAS WREATHS with scarlet bows and paired gold bells crown the upper walls. OVERHEAD, Santa in his red suit rides a richly detailed gold-runner sleigh drawn by eight reindeer across the ceiling, surrounded by arching crimson and gold ribbons of pinpoint light and long evergreen Christmas garlands woven with holly berries, striped candy canes, polished gold ornaments and ivory snowflakes. A radiant gold eight-pointed Christmas star anchors the centre overhead. The image is a single coherent richly layered storybook Christmas Eve scene on the surfaces, with deep dark sky between distinct illuminated elements; not unrelated floating icons, not physical props in the room. The dominant colours are Christmas crimson and ruby red, warm gold second, rich evergreen green and cream-white detail. No carnival Ferris wheel, no carousel, no galaxy, no nebula, no science-fiction vortex. The projected snow and all illustrated objects remain on walls and ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The barrel vault remains a visible smooth semicylindrical ceiling. The sleigh, garlands and stars visibly stretch around the curved plaster and descend onto the vertical walls, never floating as a flat sheet in front of them. At each shallow transverse arch rib the projected picture steps onto the rib's near face and is offset on the surface beyond, with a narrow hard shadow on its far edge. The limestone chimney projects from the wall; imagery bends at both vertical corners, crosses the individual stone faces and breaks at each mortar joint. The arched doorway and window recesses interrupt the picture at their real edges. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no nutcrackers, no workshop, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt
This is the C05 room-reference still, attached only as an image reference to C05 take 1. It is not an end frame and has no separate clip.

### Take history
Take 1 only. Not reviewed by Daniel. No previous take overwritten.

## C06 - starting frame

**Frame:** `starting_frames/v11_c06_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** a11380c1-3dd8-4a0a-accc-481aec5fa3bf
**Status:** Completed, saved locally, awaiting Daniel's review.
**References, in attached order:**
1. `../video_10_assets/starting_frames/v10_c06_g2.png` - 37832ca3-a7dd-48b5-ba4e-187e5f082652 - role image (backend image_references)
2. `../video_9_assets/starting_frames/v9_c06_g4.png` - 480dee42-d78d-4dd4-b3b0-cca1aed16477 - role image (backend image_references)

Reused from v10 C06 image take 2; approved v9 take 4 density and sharpness inherited in v10 - changed: Preserved camera and pose paragraphs, opacity, anti-wash, single-origin projection, full-coverage and pinpoint-sharpness wording. Changed room architecture and its surface mapping, children/clothing, Christmas scene content; two-reference roles explicitly updated. C05/C07 share new room and children.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with warm brown skin and close-cropped dark curls, fully dressed for winter in a cosy red-and-cream knitted Christmas jumper with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a cosy bedroom with a HIPPED CEILING: a small flat rectangular central ceiling panel, four broad smooth plaster slopes descending symmetrically to the four walls, and four straight diagonal hip seams where adjoining slopes meet; no tray recess, no coffer grid and no beams. Warm cream plaster walls, a broad scalloped walnut headboard on the back wall, one deep rectangular bay window on the right with dark outside glass and burgundy curtains, two walnut bedside chests, pale oak floorboards and a wool rug. The bed is under the low part of the ceiling, leaving the central panel and all adjoining slopes clearly visible.

It is night, all house lamps switched off. The bed has a cream wool duvet with red tartan throw, pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the bay window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including all four sloping planes and the central flat panel, wall above the headboard, bay window jambs and lintel. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one richly detailed NORTH POLE CHRISTMAS EVE panorama: Santa's red-and-gold timber workshop with glowing tiny windows, garland-wrapped columns, snow-covered roof and a toy-filled open doorway; smiling tiny elves in red and green winter clothes packing wooden toys and ribboned presents; a gingerbread bakery with icing-edged gables; rows of snow-laden fir trees hung with red baubles and gold stars; and an illuminated Christmas train carrying overflowing wrapped gifts along the bottom of the walls. Two majestic red-coated NUTCRACKER toy soldiers flank the workshop, with gold braid, black boots and precisely drawn faces. Large luminous CHRISTMAS WREATHS with scarlet bows and paired gold bells crown the upper walls. OVERHEAD, Santa in his red suit rides a richly detailed gold-runner sleigh drawn by eight reindeer across the ceiling, surrounded by arching crimson and gold ribbons of pinpoint light and long evergreen Christmas garlands woven with holly berries, striped candy canes, polished gold ornaments and ivory snowflakes. A radiant gold eight-pointed Christmas star anchors the centre overhead. The image is a single coherent richly layered storybook Christmas Eve scene on the surfaces, with deep dark sky between distinct illuminated elements; not unrelated floating icons, not physical props in the room. The dominant colours are Christmas crimson and ruby red, warm gold second, rich evergreen green and cream-white detail. No carnival Ferris wheel, no carousel, no galaxy, no nebula, no science-fiction vortex. The projected snow and all illustrated objects remain on walls and ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The flat central panel, all four sloping planes and every diagonal hip seam must be visibly legible. The sleigh, garlands and stars change perspective on each slope, kink at the straight hip seams, then break again where each sloping ceiling meets its vertical wall. Each slope foreshortens the picture differently from the flat middle panel. The bay-window recess stretches and clips the projected picture at its jambs and lintel. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no nutcrackers, no workshop, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the plaster, the crisp hip seams of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt - take 1

**Clip:** clips/v11_c06_g1.mp4
**Settings:** seedance_2_5; mode omni_reference; 720p; 9:16; duration 5s; count 1; generate_audio true; multi_shots false; use_unlim false; declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612.
**Job ID:** 49e73200-73f4-40ea-b642-cbc3b4aa24f8
**Status:** Completed and saved locally; awaiting Daniel's selection. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; requested duration 5s; audio stream present; 5072973 bytes.
**Sampled visual review:** Sampled frames show repeated jumping, camera movement and changing projected snowflakes. Review the strength of independent motion in the larger wall and ceiling motifs.
**References, in order:**
- starting_frames/v11_c06_g1.png | a11380c1-3dd8-4a0a-accc-481aec5fa3bf | submitted role start_image
**Backend adjustments:** {}

Reused from v10 C06 video take 1 - changed: room/product-scene nouns to match v11; C05-C07 replace absent carnival elements with the existing workshop, train, elves, bells and ribbons, and add Daniel's explicitly requested continuous-motion checks. All source beat times retained. C05 uses the corrected 5-second g2 source and a reference-only room image, never an end frame.

```text
Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected North Pole Christmas workshop picture is PLAYING across the cream plaster wall behind the bed and the whole hipped plaster ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the hipped ceiling with its small flat central panel, four broad sloping plaster planes and four straight hip seams, the cream plaster walls, the bed with its cream duvet and red tartan throw, the scalloped walnut headboard, the upholstered bench at the foot, the small lit Christmas tree, the wool rug, the right-hand recessed bay window with burgundy curtains, the stocking, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child, about six years old with warm brown skin and close-cropped dark curls, in cosy red-and-cream knitted Christmas jumper with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole hipped plaster ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny elves keep passing gifts outside the workshop, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the hip seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the cream plaster wall and the hipped plaster ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the hipped ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture bends at every real hip seam between the four sloping ceiling planes and the central flat panel, foreshortens on each plane and changes angle again onto the vertical walls and window recess. The planes and seams themselves never move.
```

#### Exact source edits - in application order

1. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
flat tray ceiling
TO:
hipped plaster ceiling
```

2. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
whole tray ceiling
TO:
whole hipped ceiling
```

3. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
the tray ceiling
TO:
the hipped ceiling
```

4. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE AURORA
TO:
THE RIBBONS
```

5. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
aurora
TO:
ribbons
```

6. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
ripple rings
TO:
travelling gold light waves
```

7. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE RIPPLE RINGS
TO:
THE GOLD LIGHT WAVES
```

8. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE FERRIS WHEEL AND THE CAROUSEL
TO:
THE TOY TRAIN AND THE ELVES
```

9. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a Ferris wheel or a carousel that does not turn
TO:
a toy train that does not travel or elves that do not move
```

10. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
snow-village picture
TO:
North Pole Christmas workshop picture
```

11. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the flat cream plaster ceiling and its single rectangular tray recess with its four angled reveals and its crown moulding, the flush recessed downlights in the flat border, the four-panel picture-frame moulding accent wall behind the bed, the bed with its deep crimson wool quilt and cream linen pillows, the wide cream upholstered headboard, the long cream upholstered bench at the foot of the bed, the small lit Christmas tree, the large oat flat-weave rug, the two windows with their curtains and garland, the stocking, THE BOY and the colour.
TO:
ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the hipped ceiling with its small flat central panel, four broad sloping plaster planes and four straight hip seams, the cream plaster walls, the bed with its cream duvet and red tartan throw, the scalloped walnut headboard, the upholstered bench at the foot, the small lit Christmas tree, the wool rug, the right-hand recessed bay window with burgundy curtains, the stocking, THE BOY and the colour.
```

12. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
about seven years old with short sandy-blond hair
TO:
about six years old with warm brown skin and close-cropped dark curls
```

13. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a warm cream and oatmeal nordic knitted Christmas jumper with a row of deep-green fir trees and rust-red reindeer across the yoke, charcoal knitted lounge trousers and thick mustard knitted socks
TO:
cosy red-and-cream knitted Christmas jumper with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks
```

14. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
panelled accent wall
TO:
cream plaster wall
```

15. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
panelled wall
TO:
cream plaster wall
```

16. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
near the crown moulding of the tray
TO:
near the hip seams of the ceiling
```

17. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
across the tray as it goes
TO:
across the hipped ceiling as it goes
```

18. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE PICTURE - the animated scene that cone is playing: a whole snowy storybook Christmas village running low along the walls with steep-gabled houses and lit shopfronts, a church with a lit steeple and a glowing clock face, market stalls under red-and-white striped awnings and lamp-posts hung with wreaths, a curl of smoke above every single chimney, a frozen silver-blue pond set into the village with tiny skating silhouettes circling on it, an enormous lit FERRIS WHEEL rising out of the village on the left in crimson and gold bulbs and a great golden CAROUSEL under a striped canopy on the right, wide ribbons ribbons in deep crimson and ruby red with warm gold and emerald green threaded between them radiating outward from the star overhead, one colossal eight-pointed STAR OF BETHLEHEM filling the whole hipped ceiling with four long rays reaching into its corners, seven concentric travelling gold light waves spreading outward from it, Santa's sleigh drawn by eight flying reindeer arcing in toward the star with a long tapering trail, a huge pair of ornate gold bells tied with a crimson bow high on one wall, floating glowing baubles and candy canes drifting at five or six different depths, a dense field of stars of many sizes, long-tailed shooting stars, and a heavy fall of large soft glowing six-point snowflakes and tiny points of light.
TO:
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.
```

19. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE TOY TRAIN AND THE ELVES - both TURN, steadily and without ever stopping. The enormous lit Ferris wheel turns about its lit hub roughly a quarter of a full turn every second, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel turns the other way under its striped canopy at about the same rate, its horses rising and falling on their twisted brass poles as they come round, and the lights along every scallop of the canopy edge chasing round the rim.
TO:
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
```

20. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE GOLD LIGHT WAVES - the seven concentric rings SPREAD OUTWARD from the great star across the hipped ceiling like rings on water, each one travelling away from the core toward the walls, widening and thinning and fading as it goes, while a fresh ring is already forming at the centre behind it, so the spread never stops.
TO:
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
```

21. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE SKATERS AND THE FLOATING THINGS - the tiny silhouettes keep circling on the frozen pond, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers glowing inside them.
TO:
- THE ELVES AND THE FLOATING THINGS - the tiny elves keep passing gifts outside the workshop, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
```

22. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE CHURCH CLOCK - the glowing clock face on the church steeple is the ONLY element that holds its position. It stays exactly where it is in the village for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
TO:
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
```

23. Daniel requested sustained movement; surface mapping adapted to the new room.
```text
FROM:

TO:
CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture bends at every real hip seam between the four sloping ceiling planes and the central flat panel, foreshortens on each plane and changes angle again onto the vertical walls and window recess. The planes and seams themselves never move.
```

#### Animation take history
Take 1 completed and saved locally. Sampled review recorded above; awaiting Daniel's selection. C01 and videos 12-14 were not animated in this round.


### Take history
Take 1 only. Not reviewed by Daniel. No previous take overwritten.

## C07 - starting frame

**Frame:** `starting_frames/v11_c07_g1.png`
**Settings:** gpt_image_2_5; sunburst; 2k; medium; 9:16; count 1.
**Job ID:** b5910d54-c9bd-4be4-9ae3-3b870ad2e793
**Status:** Completed, saved locally, awaiting Daniel's review.
**References, in attached order:**
1. `../video_10_assets/starting_frames/v10_c07_g2.png` - 9c101565-8f83-4591-9907-7aa314411d73 - role image (backend image_references)
2. `references/v11_c05_r1.png` - dda4701e-8d9d-4351-99f8-60bb9093cf68 - role image (backend image_references)

Reused from v10 C07 image take 2; approved v9 take 4 density and sharpness inherited in v10 - changed: Preserved camera and pose paragraphs, opacity, anti-wash, single-origin projection, full-coverage and pinpoint-sharpness wording. Changed room architecture and its surface mapping, children/clothing, Christmas scene content; two-reference roles explicitly updated. C05/C07 share new room and children.

### Image prompt
```text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: the girl is about nine with light freckled skin and long copper-red hair tied in a loose braid; the boy is about six with warm brown skin and close-cropped dark curls. Both fully dressed in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a tall double-height English-country Christmas great room with a continuous cream plaster BARREL-VAULT ceiling: one smooth semicylindrical curve from the left wall up over the centre and down to the right wall, crossed by three evenly spaced shallow cream plaster arch ribs that follow the curve; no flat coffer grid, no ridge and no timber trusses. A tall warm limestone chimney breast stands on the back wall, a plain carved limestone mantel beneath it, two tall rectangular black-framed windows on the left, and a recessed arched doorway on the right. Pale oak floorboards, a large ivory linen sectional sofa, a rectangular upholstered ottoman and a deep-red Persian rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the limestone fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole curved barrel vault, every projecting arch rib and the limestone chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one richly detailed NORTH POLE CHRISTMAS EVE panorama: Santa's red-and-gold timber workshop with glowing tiny windows, garland-wrapped columns, snow-covered roof and a toy-filled open doorway; smiling tiny elves in red and green winter clothes packing wooden toys and ribboned presents; a gingerbread bakery with icing-edged gables; rows of snow-laden fir trees hung with red baubles and gold stars; and an illuminated Christmas train carrying overflowing wrapped gifts along the bottom of the walls. Two majestic red-coated NUTCRACKER toy soldiers flank the workshop, with gold braid, black boots and precisely drawn faces. Large luminous CHRISTMAS WREATHS with scarlet bows and paired gold bells crown the upper walls. OVERHEAD, Santa in his red suit rides a richly detailed gold-runner sleigh drawn by eight reindeer across the ceiling, surrounded by arching crimson and gold ribbons of pinpoint light and long evergreen Christmas garlands woven with holly berries, striped candy canes, polished gold ornaments and ivory snowflakes. A radiant gold eight-pointed Christmas star anchors the centre overhead. The image is a single coherent richly layered storybook Christmas Eve scene on the surfaces, with deep dark sky between distinct illuminated elements; not unrelated floating icons, not physical props in the room. The dominant colours are Christmas crimson and ruby red, warm gold second, rich evergreen green and cream-white detail. No carnival Ferris wheel, no carousel, no galaxy, no nebula, no science-fiction vortex. The projected snow and all illustrated objects remain on walls and ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The barrel vault remains a visible smooth semicylindrical ceiling. The sleigh, garlands and stars visibly stretch around the curved plaster and descend onto the vertical walls, never floating as a flat sheet in front of them. At each shallow transverse arch rib the projected picture steps onto the rib's near face and is offset on the surface beyond, with a narrow hard shadow on its far edge. The limestone chimney projects from the wall; imagery bends at both vertical corners, crosses the individual stone faces and breaks at each mortar joint. The arched doorway and window recesses interrupt the picture at their real edges. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no nutcrackers, no workshop, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt - take 1

**Clip:** clips/v11_c07_g1.mp4
**Settings:** seedance_2_5; mode omni_reference; 720p; 9:16; duration 4s; count 1; generate_audio true; multi_shots false; use_unlim false; declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612.
**Job ID:** a4b77adb-67a0-4299-b927-544fb77b1e3d
**Status:** Completed and saved locally; awaiting Daniel's selection. One generation, no reroll.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested duration 4s; audio stream present; 3761984 bytes.
**Sampled visual review:** Review flag: the ceiling projection builds during the opening seconds instead of showing full ceiling motion immediately. Children move and the camera tilts upward. Kept as the single requested generation; no reroll.
**References, in order:**
- starting_frames/v11_c07_g1.png | b5910d54-c9bd-4be4-9ae3-3b870ad2e793 | submitted role start_image
**Backend adjustments:** {}

Reused from v10 C07 video take 1 - changed: room/product-scene nouns to match v11; C05-C07 replace absent carnival elements with the existing workshop, train, elves, bells and ribbons, and add Daniel's explicitly requested continuous-motion checks. All source beat times retained. C05 uses the corrected 5-second g2 source and a reference-only room image, never an end frame.

```text
Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected North Pole Christmas workshop picture is PLAYING across the back wall and the whole curved barrel-vault ceiling and its shallow plaster arch ribs, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the smooth cream barrel-vault ceiling crossed by three shallow plaster arch ribs, the cream plaster walls, the tall warm limestone chimney breast and carved mantel, the two tall rectangular black-framed windows on the left with night outside, the recessed arched doorway on the right, the lit Christmas tree and its presents, the large ivory linen sectional sofa wrapping the foreground, the rectangular upholstered ottoman, the deep-red Persian rug, the pale oak plank floor, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about six with warm brown skin and close-cropped dark curls, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about nine with light freckled skin and long copper-red hair in a loose braid, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, so their knitted jumpers read clearly. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole curved barrel-vault ceiling. Everything glowing on the plaster, limestone and cream arch ribs is that one cone landing.
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, limestone and cream arch ribs and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster arch ribs, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny elves keep passing gifts beside the workshop and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, limestone and cream arch ribs. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the curved barrel-vault ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the barrel vault or an un-animated arch rib in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture follows the real curve of the barrel vault, steps across each shallow arch rib with the proper offset and occlusion shadow, and bends at the projecting limestone chimney corners. The ceiling, arch ribs, stone and walls themselves never move.
```

#### Exact source edits - in application order

1. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
flat coffered ceiling
TO:
curved barrel-vault ceiling
```

2. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
coffered ceiling
TO:
barrel-vault ceiling
```

3. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
drywall, the brick and the white beams
TO:
plaster, limestone and cream arch ribs
```

4. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
drywall, the brick or the white beams
TO:
plaster, limestone and cream arch ribs
```

5. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
drywall
TO:
plaster
```

6. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE AURORA
TO:
THE RIBBONS
```

7. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
aurora
TO:
ribbons
```

8. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
ripple rings
TO:
travelling gold light waves
```

9. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE RIPPLE RINGS
TO:
THE GOLD LIGHT WAVES
```

10. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE FERRIS WHEEL AND THE CAROUSEL
TO:
THE TOY TRAIN AND THE ELVES
```

11. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a Ferris wheel or a carousel that does not turn
TO:
a toy train that does not travel or elves that do not move
```

12. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
snow-village picture
TO:
North Pole Christmas workshop picture
```

13. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the flat deep barrel-vault ceiling of chunky white beams crossing in a grid with a deep recessed panel in every square, the white raised-panel wainscot and its moulded chair rail running round the lower walls, the whitewashed painted brick chimney breast rising the full height on the back wall with its plain white mantel shelf, the second-floor gallery landing on the right behind its dark walnut handrail on slim black wrought-iron balusters, the three tall arched-top windows on the left with snow outside, the lit Christmas tree with its deep crimson and antique gold ornaments and its presents, the large oatmeal linen sectional sofa wrapping the foreground, the long upholstered ottoman, the oat flat-weave rug, the pale oak plank floor, the children and the colour.
TO:
ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the smooth cream barrel-vault ceiling crossed by three shallow plaster arch ribs, the cream plaster walls, the tall warm limestone chimney breast and carved mantel, the two tall rectangular black-framed windows on the left with night outside, the recessed arched doorway on the right, the lit Christmas tree and its presents, the large ivory linen sectional sofa wrapping the foreground, the rectangular upholstered ottoman, the deep-red Persian rug, the pale oak plank floor, the children and the colour.
```

14. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a boy of about five with straight black hair
TO:
a boy of about six with warm brown skin and close-cropped dark curls
```

15. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
a girl of about eight with short dark curly hair
TO:
a girl of about nine with light freckled skin and long copper-red hair in a loose braid
```

16. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
warm cream and oatmeal nordic knitted Christmas jumpers with a row of deep-green fir trees and rust-red reindeer across the yoke, charcoal knitted lounge trousers and thick mustard knitted socks
TO:
cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks
```

17. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
and its chunky white beams
TO:
and its shallow plaster arch ribs
```

18. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
near the ceiling beams
TO:
near the plaster arch ribs
```

19. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
oat flat-weave rug
TO:
deep-red Persian rug
```

20. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
oatmeal linen sectional sofa
TO:
ivory linen sectional sofa
```

21. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
an un-animated coffer panel or an un-animated white beam
TO:
an un-animated area of the barrel vault or an un-animated arch rib
```

22. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
THE PICTURE - the animated scene that cone is playing: a whole snowy storybook Christmas village running low along the walls with steep-gabled houses and lit shopfronts, a church with a lit steeple and a glowing clock face, market stalls under red-and-white striped awnings and lamp-posts hung with wreaths, a curl of smoke above every single chimney, a frozen silver-blue pond set into the village with tiny skating silhouettes circling on it, an enormous lit FERRIS WHEEL rising out of the village on the left in crimson and gold bulbs and a great golden CAROUSEL under a striped canopy on the right, wide ribbons ribbons in deep crimson and ruby red with warm gold and emerald green threaded between them radiating outward from the star overhead, one colossal eight-pointed STAR OF BETHLEHEM filling the entire barrel-vault ceiling with four long rays reaching into its four corners, seven concentric travelling gold light waves spreading outward from it across the ceiling, Santa's sleigh drawn by eight flying reindeer arcing in toward the star with a long tapering trail, a huge pair of ornate gold bells tied with a crimson velvet bow high on one wall, floating glowing baubles and red-and-white striped candy canes drifting at five or six different depths, a dense field of stars of many sizes, long-tailed shooting stars, and a heavy fall of large soft glowing six-point snowflakes and tiny points of light.
TO:
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.
```

23. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE TOY TRAIN AND THE ELVES - both TURN, steadily and without ever stopping. The enormous lit Ferris wheel turns about its lit hub roughly a quarter of a full turn every second, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel turns the other way under its striped canopy at about the same rate, its horses rising and falling on their twisted brass poles as they come round, and the lights along every scallop of the canopy edge chasing round the rim.
TO:
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
```

24. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE GOLD LIGHT WAVES - the seven concentric rings SPREAD OUTWARD from the great star across the barrel-vault ceiling like rings on water, each one travelling away from the core toward the walls, widening and thinning and fading as it goes, while a fresh ring is already forming at the centre behind it, so the spread never stops.
TO:
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
```

25. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny silhouettes keep circling on the frozen pond and the big gold bells swing gently on their crimson bow with the clappers glowing inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
TO:
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny elves keep passing gifts beside the workshop and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
```

26. Physical scene substitution to match the starting frame; camera and beat timing retained.
```text
FROM:
- THE CHURCH CLOCK - the glowing clock face on the church steeple is the ONLY element that holds its position. It stays exactly where it is in the village for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
TO:
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
```

27. Daniel requested sustained movement; surface mapping adapted to the new room.
```text
FROM:

TO:
CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture follows the real curve of the barrel vault, steps across each shallow arch rib with the proper offset and occlusion shadow, and bends at the projecting limestone chimney corners. The ceiling, arch ribs, stone and walls themselves never move.
```

#### Animation take history
Take 1 completed and saved locally. Sampled review recorded above; awaiting Daniel's selection. C01 and videos 12-14 were not animated in this round.


### Take history
Take 1 only. Not reviewed by Daniel. No previous take overwritten.



### Video prompt - take 2

**Clip:** clips/v11_c07_g2.mp4
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "720p", "aspect_ratio": "9:16", "duration": 4, "count": 1, "generate_audio": true, "multi_shots": false, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "b5910d54-c9bd-4be4-9ae3-3b870ad2e793"}]}
**Job ID:** 2380e078-1cc7-464c-9594-77248972e878
**Status:** Completed and saved locally; take 2 added to the board for Daniel's review. One generation in this revision round.
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; requested 4s; audio stream present; 4344574 bytes.
**Sampled visual review:** Take 2: sampled frames at 0.00, 0.20 and 0.40 seconds show the wall and ceiling projections already fully present, with no opening buildup. Later samples show the sleigh travelling across the ceiling while the children keep moving. Awaiting Daniel's review.
**References, in order:**
- starting_frames/v11_c07_g1.png | b5910d54-c9bd-4be4-9ae3-3b870ad2e793 | submitted role start_image
**Backend adjustments:** {}

Reused from v11 C07 video take 1 - only the prompt corrections listed below changed. Same starting frame, model, resolution, duration and media roles. C05 remains exactly a 5-second request with the room as reference-only, never an end frame.

```text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, barrel-vault ceiling panel and arch rib. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected North Pole Christmas workshop picture is PLAYING across the back wall and the whole curved barrel-vault ceiling and its shallow plaster arch ribs, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the smooth cream barrel-vault ceiling crossed by three shallow plaster arch ribs, the cream plaster walls, the tall warm limestone chimney breast and carved mantel, the two tall rectangular black-framed windows on the left with night outside, the recessed arched doorway on the right, the lit Christmas tree and its presents, the large ivory linen sectional sofa wrapping the foreground, the rectangular upholstered ottoman, the deep-red Persian rug, the pale oak plank floor, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about six with warm brown skin and close-cropped dark curls, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about nine with light freckled skin and long copper-red hair in a loose braid, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, so their knitted jumpers read clearly. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole curved barrel-vault ceiling. Everything glowing on the plaster, limestone and cream arch ribs is that one cone landing.
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, limestone and cream arch ribs and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster arch ribs, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny elves keep passing gifts beside the workshop and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, limestone and cream arch ribs. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the curved barrel-vault ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the barrel vault or an un-animated arch rib in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture follows the real curve of the barrel vault, steps across each shallow arch rib with the proper offset and occlusion shadow, and bends at the projecting limestone chimney corners. The ceiling, arch ribs, stone and walls themselves never move.
```

#### Exact source edits - in application order

1. Require full initial projection coverage.

Added paragraph:
```text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, barrel-vault ceiling panel and arch rib. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.
```

2. Remove an opening activation interpretation.

Before:
```text
The start image is one paused frame of that film; at 0.0s it un-pauses.
```

```text
The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself.
```

3. Ban initial projection buildup.

Before:
```text
DO NOT INCLUDE: a frozen or still pattern;
```

```text
DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern;
```

#### Animation take history - revision round
Take 1 retained. Daniel requested correction: Wall and ceiling projections build at the beginning instead of already being fully present.
Take 2 completed, saved and added to board. Awaiting Daniel's selection. No additional reroll.

## Result files - verified 2026-09-21

- `starting_frames/v11_c02_g1.png` - job `bbfc652c-e9eb-4430-9b53-610b56917312` - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134258_bbfc652c-e9eb-4430-9b53-610b56917312.png
- `starting_frames/v11_c03_g1.png` - job `4b0ce2fa-f22e-4fdc-a781-0a2f43789130` - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134259_4b0ce2fa-f22e-4fdc-a781-0a2f43789130.png
- `starting_frames/v11_c04_g1.png` - job `e243effc-2c21-4bed-9551-e592483315ca` - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134258_e243effc-2c21-4bed-9551-e592483315ca.png
- `starting_frames/v11_c05_g1.png` - job `6a0df249-6245-439e-a380-e9bbdf6dc580` - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134258_6a0df249-6245-439e-a380-e9bbdf6dc580.png
- `references/v11_c05_r1.png` - job `dda4701e-8d9d-4351-99f8-60bb9093cf68` - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134257_dda4701e-8d9d-4351-99f8-60bb9093cf68.png
- `starting_frames/v11_c06_g1.png` - job `a11380c1-3dd8-4a0a-accc-481aec5fa3bf` - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134257_a11380c1-3dd8-4a0a-accc-481aec5fa3bf.png
- `starting_frames/v11_c07_g1.png` - job `b5910d54-c9bd-4be4-9ae3-3b870ad2e793` - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134458_b5910d54-c9bd-4be4-9ae3-3b870ad2e793.png

All seven submissions completed; no failures, retries or rerolls. Temporary downloads were copied into the product folder and each copy verified with SHA256. Images remain unselected pending Daniel's review.

## C01 - Hook recreation - 2026-09-21

**Current status:** image generated, downloaded and inspected; awaiting Daniel's review. No animation requested until the image is approved. Existing B-roll records above remain unchanged.

**Frame:** `starting_frames/v11_c01_g1.png` (downloaded and verified)
**Clip:** not generated.
**Settings:** Higgsfield `gpt_image_2_5`, `variant=sunburst`, `resolution=2k`, `quality=medium`, `aspect_ratio=9:16`, `count=1`. The user explicitly requested these settings, overriding the older source model where different. `use_unlim` omitted. Both canonical `image` roles were mapped by the backend to `image_references`.
**Job ID:** `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`
**References (in submitted order):**
1. `../video_6_assets/starting_frames/v6_c01_g4.png`, completed generation ID `9cd2cb32-1f96-4484-ad2f-cc726aca8088`: owns geometry, framing, camera, pose and prop placement; confirmed selected frame on video_board.html.
2. `../video_6_assets/starting_frames/v6_c01_g1.png`, completed generation ID `836690da-363a-486e-8ca1-fdf21acd0523`: photographic look only, natural iPhone sharpness and materials, not room or people.

Reused from v6 C01 g4 - changed: people and room nouns only, plus reference-role wording needed for the new reference pair. Source v6 g4 is an edit of v6 g1; the complete v6 g1 prompt was copied, with the American-flag pyjama description and flag paragraph copied from v6 g4. Camera, framing, pose and quality blocks copied from the archived source. Historical edit instructions naming the people in the old source were adapted to the current selected reference where necessary. Every exact replacement is listed below.

### Image prompt
```text
REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas living room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height traditional living room with an open curved staircase - pale sage-green panelled walls, the wide staircase at the left with a thick green garland wound around its honey-oak banister and stockings hung along it, a pale limestone fireplace with a lit fire and an oval brass mirror above it, a tall Christmas tree with warm white lights and red and gold baubles at the right, a burgundy velvet sofa, a patterned cream and green rug on honey-oak boards.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid 30s with long jet-black hair in a loose low ponytail, warm medium-brown skin, matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit and thick grey wool socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling reads as clean white paint and the panelling as pale sage-green paint, her pyjamas keep true red, white and navy, the banister and the floor read as natural wood, the rug keeps its own colours. The Christmas tree lights, the fire and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the weave of her pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.

A UNITED STATES FLAG: a real fabric United States flag hangs flat against the pale sage-green wall in the background behind her, clearly readable stars and stripes, hanging straight and still. It does not cover the Christmas tree, the fireplace or the staircase, and it does not reach up into the empty band of ceiling at the top of the frame.
```

### Video prompt
Not submitted. Awaiting Daniel's image approval.

**Result (2026-09-21):** completed; 1520 x 2688 pixels, PNG, 5887433 bytes; MD5 f25216fb1e7e42125afee600339cc34c. One generation only. Source URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_152602_c649b5e6-5dec-42ba-ad82-8da4ac49ea2f.png

**Visual check:** Low three-quarters rear framing, tall ladder, taped Santa, USA pyjamas and flag preserved. Woman now has black hair; sage wall panels, burgundy sofa, oval mirror and rug distinguish the background. Unreviewed by Daniel.

### Take history
- `starting_frames/v11_c01_g1.png`: one submission, unreviewed. No automatic reroll.
- Source full prompt retrieved from the source prompts.md; dated traceability notes checked. Earlier unresolved takes were not used.

### What changed and why
The user requested an extremely similar hook with different people and a different room. A reference-role paragraph was prepended to prevent the look reference from changing geometry.

#### Change 1
Before:
```text
THE ROOM: a double-height traditional living room with an open curved staircase - cream panelled walls, the wide staircase at the left with a thick green garland wound around its dark timber banister and stockings hung along it, a white marble fireplace with a lit fire and a gold mirror above it, a tall Christmas tree with warm white lights and red and gold baubles at the right, a deep blue velvet sofa, a patterned red and blue rug on dark oak boards.
```
After:
```text
THE ROOM: a double-height traditional living room with an open curved staircase - pale sage-green panelled walls, the wide staircase at the left with a thick green garland wound around its honey-oak banister and stockings hung along it, a pale limestone fireplace with a lit fire and an oval brass mirror above it, a tall Christmas tree with warm white lights and red and gold baubles at the right, a burgundy velvet sofa, a patterned cream and green rug on honey-oak boards.
```

#### Change 2
Before:
```text
early 30s with long auburn hair in a loose low ponytail, a cream cable-knit sweater, black leggings and thick grey wool socks
```
After:
```text
mid 30s with long jet-black hair in a loose low ponytail, warm medium-brown skin, matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit and thick grey wool socks
```

#### Change 3
Before:
```text
The ceiling and the panelling read as clean white and cream paint, her sweater reads as true cream, the banister and the floor read as natural wood, the rug keeps its own colours.
```
After:
```text
The ceiling reads as clean white paint and the panelling as pale sage-green paint, her pyjamas keep true red, white and navy, the banister and the floor read as natural wood, the rug keeps its own colours.
```

#### Change 4
Before:
```text
knit of her sweater
```
After:
```text
weave of her pyjamas
```

The United States flag paragraph from v6 g4 was appended, changing only the wall colour from cream to pale sage-green. American-flag pyjamas retained as explicitly requested.


### C01 animation - take 1 - 2026-09-21

**Status:** completed and saved; awaiting Daniel's review. Daniel approved all four starting frames in this conversation and requested the same animation as the corresponding source, Seedance 2.5, 1080p. One generation per shot.
**Frame:** `starting_frames/v11_c01_g1.png` - approved.
**Clip:** `clips/v11_c01_g1.mp4` (downloaded and verified).
**Job ID:** `ab3a362b-a906-484f-b4cc-939bdc674a6a`
**Settings:** `seedance_2_5`, `mode=omni_reference`, `resolution=1080p`, `duration=4`, `aspect_ratio=9:16`, `generate_audio=true`, `count=1`, `use_unlim=false`, `declined_preset_id=24bae836-2c4a-48e0-89b6-49fcc0b21612`. Other model defaults unchanged.
**References:** approved frame `starting_frames/v11_c01_g1.png`, image generation job `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`, submitted twice as roles `start_image` and `image` (second normalized to `image_references`), matching source v6's attachment strategy. No source video attached.
**Source:** `../video_6_assets/prompts.md`, C01 video take g1; selected clip `../video_6_assets/clips/v6_c01_g1.mp4`, source generation `3be81f83-f33e-4612-8a19-7d3a2c532c38`, verified against the existing board. Source prompt and settings retrieved directly from the archive, including dated traceability notes.

Reused from v6 C01 g1 - changed: nothing in the prompt. Only the starting-frame reference changed. Motion, camera, pacing, beat timing, audio and bans unchanged. Original duration and settings retained.

No words changed; the full prompt is byte-identical to the source.

#### Video prompt
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

#### Take history
`clips/v11_c01_g1.mp4`: generated once, saved, awaiting Daniel's review. No automatic reroll. No upscale requested.


**Result:** completed; 1080x1920, 4.050000s, 24/1 fps, hevc video, aac audio; 4912183 bytes; MD5 83ce8a5038b1a17f0478baf36b0e1fc3. Temporary download and final file sizes/hashes matched. Full video/audio decode exit 0. Service-returned prompt matches the submitted and archived prompt exactly.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_153744_ab3a362b-a906-484f-b4cc-939bdc674a6a.mp4
**Visual check:** Sampled frames show taping, the ladder fall, floor landing and still finish, with Santa remaining on the ceiling. Camera widens during the fall despite the framing lock, as also noted for the source take. Kept for Daniel's review; no reroll.
**Review limits:** sampled visual frames inspected; audio stream presence and decoding verified, spoken wording not independently checked.


### C01 animation - take 2 - 2026-09-21

**Status:** completed, saved and checked; awaiting Daniel's review. One regeneration explicitly requested.
**Reason:** Daniel liked the hooks but requested a reroll of video 11 because the ladder looked weird after the fall. He explicitly requested the same prompt, suspecting a model error.
**Frame:** `starting_frames/v11_c01_g1.png` - approved, unchanged.
**Clip:** `clips/v11_c01_g2.mp4` (downloaded and verified).
**Job ID:** `f075727f-efcc-4f06-980a-cdc428271244`
**Settings:** `seedance_2_5`, `mode=omni_reference`, `resolution=1080p`, `duration=4`, `aspect_ratio=9:16`, `generate_audio=true`, `count=1`, `use_unlim=false`, `declined_preset_id=24bae836-2c4a-48e0-89b6-49fcc0b21612`. Same parameters as g1; other defaults unchanged.
**References:** `starting_frames/v11_c01_g1.png`, image job `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`, attached twice in order: `start_image`, `image` (second normalized to `image_references`). No source video attached.

Reused from v11 C01 video g1 - changed: nothing. Prompt copied byte-identically from the archive; no new wording for the ladder. Same starting frame and settings. Original lineage: v6 C01 video g1.

#### Video prompt
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

#### Take history
- `clips/v11_c01_g1.mp4`: retained. Daniel requested replacement because the ladder looked weird after the fall.
- `clips/v11_c01_g2.mp4`: generated once, saved; awaiting Daniel's review. No automatic further reroll.


**Result:** completed; 1080x1920, 4.05 seconds, 24 fps, HEVC video with AAC audio, 4573386 bytes. MD5 7672221ebba6eb3d89430fbec6da62ac. Download and saved copy hashes and lengths match. Full video/audio decode exit 0.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_155623_f075727f-efcc-4f06-980a-cdc428271244.mp4
**Visual check:** sampled at 2 fps. The ladder tips to the right and is visible lying on the rug beside her after landing, including the final sampled frames. Santa remains taped to the ceiling. Camera still widens during the fall despite the unchanged framing lock. Saved for Daniel's review; no further generation.


### C01 animation - take 3 - 2026-09-21

**Status:** completed, saved and checked; awaiting Daniel's review. One generation requested.
**Reason:** Daniel rejected g2 because it began much closer than the approved starting image and zoomed out, and requested another submission.
**Frame:** `starting_frames/v11_c01_g1.png`, approved original; MD5 f25216fb1e7e42125afee600339cc34c verified before submission.
**Clip:** `clips/v11_c01_g3.mp4` (downloaded and verified).
**Job ID:** `3b4c31ea-4040-480a-b9b6-f276568aec5b`
**Settings:** `seedance_2_5`, `mode=omni_reference`, `resolution=1080p`, `duration=4`, `aspect_ratio=9:16`, `generate_audio=true`, `count=1`, `use_unlim=false`, `declined_preset_id=24bae836-2c4a-48e0-89b6-49fcc0b21612`.
**References:** only `starting_frames/v11_c01_g1.png`, image job `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`, role `start_image`. The duplicated generic `image` reference used in g1/g2 was removed. No source video attached.

Reused from v11 C01 video g2 - changed: no prompt words. Only input-role configuration changed: removed the duplicate generic image reference, leaving the approved image as the sole start_image. This is an attempt to improve starting-frame adherence; duplicate-role causation is not proven. Same animation settings. Original lineage v6 C01 g1.

#### Video prompt
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

#### Take history
- g1 retained: user-reported ladder defect after landing.
- g2 retained, rejected by Daniel: close opening and zoom-out.
- g3 generated once and saved; awaiting Daniel's review. No further automatic generation.

**Result:** completed; 1080x1920, 4.05 seconds, 24 fps, HEVC video with AAC audio, 5180919 bytes. MD5 c38697d9b9852effa86b35a61fce0353. Download and saved copy hashes and lengths match. Full video/audio decode exit 0.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_181854_3b4c31ea-4040-480a-b9b6-f276568aec5b.mp4
**Visual check:** first frame and 2 fps contact sheet inspected. Opening shows the approved full-body woman and full ladder composition, without the previous close opening. Camera still widens/reframes during the fall despite the unchanged prompt. The ladder tips onto the rug, the woman lands on the floor, and Santa stays at the ceiling. This does not establish an exact camera lock or user approval. Saved for Daniel's review; no reroll.

### C01 animation - take 4 - 2026-09-21

**Status:** completed and saved; awaiting Daniel's review. One final reroll explicitly requested.
**Reason:** Daniel requested one last submission with the same prompt after take 3.
**Frame:** `starting_frames/v11_c01_g1.png`, approved original; MD5 f25216fb1e7e42125afee600339cc34c verified before submission.
**Clip:** `clips/v11_c01_g4.mp4` (downloaded and verified).
**Job ID:** `0dd9eb8c-5dfa-4129-ad73-44dd51d2eebc`
**Settings:** `seedance_2_5`, `mode=omni_reference`, `resolution=1080p`, `duration=4`, `aspect_ratio=9:16`, `generate_audio=true`, `count=1`, `use_unlim=false`, `declined_preset_id=24bae836-2c4a-48e0-89b6-49fcc0b21612`.
**References:** only `starting_frames/v11_c01_g1.png`, image job `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`, role `start_image`.

Reused from v11 C01 video g3 - changed: nothing. Exact 2344-character submitted prompt verified equal to g3; same starting image, media role and settings. Original lineage v6 C01 g1. All prior takes retained.

#### Video prompt
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

**Result:** completed; 1080x1920, 4.05 seconds, 24 fps, HEVC video with AAC audio, 4815888 bytes. MD5 06a62c29a18f137c31129252e34957de. Download and saved copy hashes and lengths match. Full video/audio decode exit 0. Visual quality awaits Daniel's review; no further generation.
**Result URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_183223_0dd9eb8c-5dfa-4129-ad73-44dd51d2eebc.mp4


## Upscale derivatives - 2026-09-22

**Status:** completed, downloaded and verified locally. Daniel requested the last animation take for each shot. No source generation was overwritten.

**Shared settings:** `ByteDance Upscale`, `model_version=Pro`, `resolution=2K`, `fps=30`. Saved derivatives are H.264 at 1440x2560 and 30 fps in `clips/upscaled/`, carrying the source clip's exact filename.

| Shot | Source clip | Upscaled derivative | Preset | Upscale job ID | Result |
|---|---|---|---|---|---|
| C01 | `clips/v11_c01_g4.mp4` | `clips/upscaled/v11_c01_g4.mp4` | `AIGC` | `c49a2c7f-a904-494e-9239-5c0096110ff1` | 4.06s; 8,771,902 bytes; MD5 `6dda38f93f80f9d9c277a5735d5f7c0f`; full local copy hash matched the download |
| C02 | `clips/v11_c02_g1.mp4` | `clips/upscaled/v11_c02_g1.mp4` | `Common` | `481f63f5-2280-4eaa-8367-68a4c57712d5` | 4.06s; 8,675,123 bytes; MD5 `8099f6650cf531fa1af77f6dd5064f46`; full local copy hash matched the download |
| C03 | `clips/v11_c03_g1.mp4` | `clips/upscaled/v11_c03_g1.mp4` | `Common` | `d728b094-8088-4445-a132-7027232eeb6d` | 4.06s; 8,491,970 bytes; MD5 `a179e94e64aebcedd471940314a4ba22`; full local copy hash matched the download |
| C04 | `clips/v11_c04_g1.mp4` | `clips/upscaled/v11_c04_g1.mp4` | `Common` | `c2668916-0dd9-4171-9541-991d4b3eaf5b` | 4.06s; 6,682,818 bytes; MD5 `1003d5fdc27c7eb51fe0c9f5e3b79b0e`; full local copy hash matched the download |
| C05 | `clips/v11_c05_g4.mp4` | `clips/upscaled/v11_c05_g4.mp4` | `Common` | `7f4ea953-dbbb-48b3-9bb4-c2fa539ae5b9` | 5.06s; 10,852,560 bytes; MD5 `70fbbc501283c879dcf378e8c62a3f62`; full local copy hash matched the download |
| C06 | `clips/v11_c06_g1.mp4` | `clips/upscaled/v11_c06_g1.mp4` | `Common` | `020de6d0-4d11-401d-9083-9c44410d1a74` | 5.06s; 10,692,647 bytes; MD5 `65eab3ccf9b7b458e064aee3ea29adfd`; full local copy hash matched the download |
| C07 | `clips/v11_c07_g2.mp4` | `clips/upscaled/v11_c07_g2.mp4` | `Common` | `c5cd37ee-c72a-45ed-a275-cb49729cd2d4` | 4.06s; 8,935,853 bytes; MD5 `c682ff849992ecd4cf0fc69065fe53ef`; full local copy hash matched the download |

**Verification:** all seven files reported H.264 video, 1440x2560, 30/1 fps in `ffprobe`; full video/audio decode exit 0 for every file. The copy into `clips/upscaled/` matched the downloaded source byte-for-byte by size and MD5.


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

### C01 — Ladder fail — taping Santa up

**In the cut:** `starting_frames/v11_c01_g1.png` → `clips/v11_c01_g4.mp4`

#### Image prompt — `starting_frames/v11_c01_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_152602_c649b5e6-5dec-42ba-ad82-8da4ac49ea2f.png
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c01_g4.png` · Higgsfield media `9cd2cb32-1f96-4484-ad2f-cc726aca8088`
- @Image 2: `content/video_6_assets/starting_frames/v6_c01_g1.png` · Higgsfield media `836690da-363a-486e-8ca1-fdf21acd0523`

````text
REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas living room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height traditional living room with an open curved staircase - pale sage-green panelled walls, the wide staircase at the left with a thick green garland wound around its honey-oak banister and stockings hung along it, a pale limestone fireplace with a lit fire and an oval brass mirror above it, a tall Christmas tree with warm white lights and red and gold baubles at the right, a burgundy velvet sofa, a patterned cream and green rug on honey-oak boards.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid 30s with long jet-black hair in a loose low ponytail, warm medium-brown skin, matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit and thick grey wool socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling reads as clean white paint and the panelling as pale sage-green paint, her pyjamas keep true red, white and navy, the banister and the floor read as natural wood, the rug keeps its own colours. The Christmas tree lights, the fire and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the weave of her pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.

A UNITED STATES FLAG: a real fabric United States flag hangs flat against the pale sage-green wall in the background behind her, clearly readable stars and stripes, hanging straight and still. It does not cover the Christmas tree, the fireplace or the staircase, and it does not reach up into the empty band of ceiling at the top of the frame.
````

#### Video prompt — `clips/v11_c01_g4.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `0dd9eb8c-5dfa-4129-ad73-44dd51d2eebc`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_183223_0dd9eb8c-5dfa-4129-ad73-44dd51d2eebc.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v11_c01_g4.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c01_g1.png` · Higgsfield media `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`

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

**Other takes of C01 on disk (3)**

#### Video prompt — `clips/v11_c01_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `ab3a362b-a906-484f-b4cc-939bdc674a6a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_153744_ab3a362b-a906-484f-b4cc-939bdc674a6a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c01_g1.png` · Higgsfield media `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`
- image ref 1: `content/video_11_assets/starting_frames/v11_c01_g1.png` · Higgsfield media `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`

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

#### Video prompt — `clips/v11_c01_g2.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `f075727f-efcc-4f06-980a-cdc428271244`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_155623_f075727f-efcc-4f06-980a-cdc428271244.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c01_g1.png` · Higgsfield media `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`
- image ref 1: `content/video_11_assets/starting_frames/v11_c01_g1.png` · Higgsfield media `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`

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

#### Video prompt — `clips/v11_c01_g3.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `3b4c31ea-4040-480a-b9b6-f276568aec5b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_181854_3b4c31ea-4040-480a-b9b6-f276568aec5b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c01_g1.png` · Higgsfield media `c649b5e6-5dec-42ba-ad82-8da4ac49ea2f`

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

### C02 — Hands on the box

**In the cut:** `starting_frames/v11_c02_g1.png` → `clips/v11_c02_g1.mp4`

#### Image prompt — `starting_frames/v11_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `bbfc652c-e9eb-4430-9b53-610b56917312`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134258_bbfc652c-e9eb-4430-9b53-610b56917312.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `1cdfcc53-e771-4bba-9eab-b1788346098b`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 38, with warm medium-brown skin and softly rounded short natural nails, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a ivory cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a rich honey-toned solid elm dining table with broad flowing grain and a matte finish, a substantial straight edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a sharply resolved traditional Christmas dining room: muted forest-green walls with cream picture rails, a cream limestone fireplace with brass candleholders and red knitted stockings, a Christmas tree with red glass baubles and gold ribbon to the left, and a built-in dark walnut bookcase to the right. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the elm table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte elm, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v11_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `4749d6c1-fcdf-44dc-a192-b071bb1df133`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_150958_4749d6c1-fcdf-44dc-a192-b071bb1df133.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v11_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- video ref 1: `references/scene_no_audio-2.mp4` — upload · 2.14 s · Higgsfield media `1d2e8a8d-1e49-422a-8b04-d1a1230096a4`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a honey-toned elm table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a ivory cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a honey-toned elm table fills the frame: broad flowing timber grain, a matte finish and a substantial straight edge. A lit cream pillar candle sits at the left, fir sprigs with white berries and small antique gold and pearl-white baubles beside it, and behind it, sharply in focus, muted forest-green walls with cream picture rails, a cream limestone fireplace with brass candleholders and red knitted stockings, a Christmas tree with red glass baubles and gold ribbon to the left, and a built-in dark walnut bookcase to the right. The candle, the fir, the berries, the baubles, the fireplace and the tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the honey-toned elm table, lid flaps folded back, with the candle, the fir, the berries, the fireplace and the tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v11_c03_g1.png` → `clips/v11_c03_g1.mp4`

#### Image prompt — `starting_frames/v11_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134259_4b0ce2fa-f22e-4fdc-a781-0a2f43789130.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `7ccdd557-bfee-45b0-a067-0652320f537b`
- @Image 2: `content/video_10_assets/starting_frames/v10_c03_g1.png` · Higgsfield media `89ed549a-35bb-4e66-8865-c5a112bc239a`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 38, with warm medium-brown skin and softly rounded short natural nails: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a ivory cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same ivory cable-knit sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a pale ivory honed travertine counter, small natural pores and delicate beige mineral veins, matte stone with a straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: deep sage-green inset cabinets with aged brass cup pulls, warm ivory square ceramic tiles, a brushed brass range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v11_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `a41072e9-50d5-4bf5-9c21-745e7bfe12dc`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_150958_a41072e9-50d5-4bf5-9c21-745e7bfe12dc.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v11_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale ivory honed travertine kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in ivory cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a pale ivory honed travertine countertop - small natural pores and delicate beige mineral veins, matte stone and a straight square edge - fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with deep sage-green inset cabinets with aged brass cup pulls, a brushed brass range built into the tall cabinet run on the left, a warm ivory square ceramic tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays crisp and in focus, matching the start image. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the travertine counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The travertine is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v11_c04_g1.png` → `clips/v11_c04_g1.mp4`

#### Image prompt — `starting_frames/v11_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `e243effc-2c21-4bed-9551-e592483315ca`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134258_e243effc-2c21-4bed-9551-e592483315ca.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`
- @Image 2: `content/video_10_assets/starting_frames/v10_c04_g1.png` · Higgsfield media `1d69a04c-84ad-4a97-8d55-d5ce334848c1`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 38, with warm medium-brown skin and softly rounded short natural nails: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a ivory cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a pale ivory honed travertine counter, small natural pores and delicate beige mineral veins, matte stone with a straight square edge. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: deep sage-green inset cabinets with aged brass cup pulls, warm ivory square ceramic tiles, a brushed brass range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with red and gold ornaments in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v11_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `3a7b4dc6-57a3-4f8f-adb5-3629e268e08b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_150958_3a7b4dc6-57a3-4f8f-adb5-3629e268e08b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v11_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`

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
THE LEFT HAND - a woman's hand in a ivory cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same ivory cable-knit sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a pale ivory honed travertine countertop - small natural pores and delicate beige mineral veins, matte stone and a straight square edge - fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with deep sage-green inset cabinets with aged brass cup pulls, a brushed brass range built into the tall cabinet run on the right, a warm ivory square ceramic tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays crisp and in focus, matching the start image. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

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
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v11_c05_g1.png`, `references/v11_c05_r1.png` → `clips/v11_c05_g4.mp4`

#### Image prompt — `starting_frames/v11_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `6a0df249-6245-439e-a380-e9bbdf6dc580`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134258_6a0df249-6245-439e-a380-e9bbdf6dc580.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `c9e1f960-9e19-4b9b-ad88-8f5298db1880`
- @Image 2: `content/video_10_assets/starting_frames/v10_c05_g1.png` · Higgsfield media `c301edff-f38f-42fc-bdde-d914d68ab37d`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the ivory cable-knit sleeve and no jewellery, with warm medium-brown skin, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a forest-green painted solid wood door with three equal horizontal recessed panels, satin finish and fine natural brush texture, an antique brass round knob and matching brass escutcheon, set in a cream painted frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest-green paint reads clearly as a rich green rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Image prompt — `references/v11_c05_r1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `dda4701e-8d9d-4351-99f8-60bb9093cf68`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134257_dda4701e-8d9d-4351-99f8-60bb9093cf68.png
**References, in submission order**
- @Image 1: `content/video_10_assets/references/v10_c05_r2.png` · Higgsfield media `1f88d0ff-b4ae-4d75-a61b-9e36719f41a5`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is about six with warm brown skin and close-cropped dark curls; the girl is about nine with light freckled skin and long copper-red hair tied in a loose braid. Both children are fully dressed for winter in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a tall double-height English-country Christmas great room with a continuous cream plaster BARREL-VAULT ceiling: one smooth semicylindrical curve from the left wall up over the centre and down to the right wall, crossed by three evenly spaced shallow cream plaster arch ribs that follow the curve; no flat coffer grid, no ridge and no timber trusses. A tall warm limestone chimney breast stands on the back wall, a plain carved limestone mantel beneath it, two tall rectangular black-framed windows on the left, and a recessed arched doorway on the right. Pale oak floorboards, a large ivory linen sectional sofa, a rectangular upholstered ottoman and a deep-red Persian rug. Seen from the doorway; the new three-panel forest-green door is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the limestone fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole curved barrel vault, every projecting arch rib and the limestone chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one richly detailed NORTH POLE CHRISTMAS EVE panorama: Santa's red-and-gold timber workshop with glowing tiny windows, garland-wrapped columns, snow-covered roof and a toy-filled open doorway; smiling tiny elves in red and green winter clothes packing wooden toys and ribboned presents; a gingerbread bakery with icing-edged gables; rows of snow-laden fir trees hung with red baubles and gold stars; and an illuminated Christmas train carrying overflowing wrapped gifts along the bottom of the walls. Two majestic red-coated NUTCRACKER toy soldiers flank the workshop, with gold braid, black boots and precisely drawn faces. Large luminous CHRISTMAS WREATHS with scarlet bows and paired gold bells crown the upper walls. OVERHEAD, Santa in his red suit rides a richly detailed gold-runner sleigh drawn by eight reindeer across the ceiling, surrounded by arching crimson and gold ribbons of pinpoint light and long evergreen Christmas garlands woven with holly berries, striped candy canes, polished gold ornaments and ivory snowflakes. A radiant gold eight-pointed Christmas star anchors the centre overhead. The image is a single coherent richly layered storybook Christmas Eve scene on the surfaces, with deep dark sky between distinct illuminated elements; not unrelated floating icons, not physical props in the room. The dominant colours are Christmas crimson and ruby red, warm gold second, rich evergreen green and cream-white detail. No carnival Ferris wheel, no carousel, no galaxy, no nebula, no science-fiction vortex. The projected snow and all illustrated objects remain on walls and ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The barrel vault remains a visible smooth semicylindrical ceiling. The sleigh, garlands and stars visibly stretch around the curved plaster and descend onto the vertical walls, never floating as a flat sheet in front of them. At each shallow transverse arch rib the projected picture steps onto the rib's near face and is offset on the surface beyond, with a narrow hard shadow on its far edge. The limestone chimney projects from the wall; imagery bends at both vertical corners, crosses the individual stone faces and breaks at each mortar joint. The arched doorway and window recesses interrupt the picture at their real edges. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no nutcrackers, no workshop, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v11_c05_g4.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `51b47bb9-2af7-4489-abfb-e25eea49c11e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_182103_51b47bb9-2af7-4489-abfb-e25eea49c11e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v11_c05_g4.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- video ref 1: `content/video_11_assets/clips/v11_c07_g2.mp4` — earlier generated clip · Higgsfield media `2380e078-1cc7-464c-9594-77248972e878`

````text
CAMERA CONTINUITY - PRIMARY CORRECTION: one simultaneous forward-and-upward movement spans the entire 5-second take. Beginning immediately at 0.0s, move forward gently while tilting upward gently at the SAME TIME. Keep the upward angular speed constant from first frame to last: approximately 5 degrees per second, about 25 degrees total. At 1s the upward tilt is already 5 degrees, at 2s 10 degrees, at 3s 15 degrees, at 4s 20 degrees, at 5s 25 degrees. These are points on ONE continuous movement, not separate beats. There is no forward-only opening, level hold, late tilt onset, sudden upward swing, acceleration, whip, or change of direction. The hand opens the door during this same gentle rising move. Once the threshold is clear, continue walking forward and rising at that exact same unhurried rate. The last frame still includes the back wall and some furniture under the ceiling; do not rush toward a ceiling-only final composition. @Video 1 supplies visual content ONLY: its delayed upward camera tilt is specifically WRONG for this shot and must not be copied.

CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole workshop picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The gentle upward tilt and gentle forward drift have ALREADY STARTED on the first frame and continue at constant speed while the hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - CONTINUE THE SAME SIMULTANEOUS FORWARD-AND-UPWARD MOVE ALREADY IN PROGRESS. Clearing the door is not a camera cue. The view must not travel straight ahead first and only later rise to the ceiling. The camera advances slowly through the doorway while its aim keeps rising at the same small constant angular rate that began at 0.0s; room features slide downward through the frame continuously as perspective gently advances. No hold on the children, no stop at the sofa, no separate ceiling reveal. Do not speed up the tilt in the last two seconds to finish a composition. The shot simply ends during the same ongoing gentle movement, with both back wall and ceiling still visible. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The copper-braided girl runs a broad curving path across the rug and alongside the sofa; the dark-curled boy follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, subtle natural handheld sway. One blended forward-and-upward move, with constant gentle upward angular speed across all five seconds. No delayed tilt, no pitch jump, no sudden reframe, no acceleration or speed ramp, no stop, no second move, no cut, no zoom, no orbit, no fisheye, no lens warping. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move with forward translation and upward tilt happening simultaneously from the first frame, at unchanged gentle speed throughout. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; a forward-only push followed by a late upward tilt; holding a level angle until entering the room; a sudden ceiling swing; accelerating the tilt near the end; copying @Video 1's camera timing; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, limestone and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and arch ribs. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.
````

**Other takes of C05 on disk (3)**

#### Video prompt — `clips/v11_c05_g1.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `057801b4-0ec9-4cfd-b356-d833a7a1d06d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_150959_057801b4-0ec9-4cfd-b356-d833a7a1d06d.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- image ref 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`

````text
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Image 1 is ONE PAUSED FRAME of that movie. At 0.0s it un-pauses and keeps running to the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Image 1 is the great room behind that door and the authority on its layout, barrel-vault ceiling, furniture, the two children, their clothes, the colours, and the exact set and style of every projected shape.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Every chimney in the North Pole Christmas workshop village pours smoke like a real wood fire on a cold still evening: it boils out of the pot, leans right, climbs and widens and thins away, and the next plume is already forming behind it. Not one chimney in the village is without its plume.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the floating baubles and candy canes turn slowly as they drift, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white barrel-vault ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. The door opens on two kids in the middle of doing something, not on two kids standing waiting to be filmed, and neither of them is ever still. THE BOY, the child on the right, initially facing the doorway but already turning toward the sofa as he runs, is already mid-stride as the gap widens; he takes three or four quick real steps and LAUNCHES HIMSELF UP ONTO the big ivory linen sectional sofa that wraps the room right behind him, landing on his knees with both arms flying up, laughing, and keeps bouncing there until the last frame. THE GIRL, the child on the left with the long copper-red braid, is already running as the door opens; she runs on across the room toward the lit Christmas tree without breaking step, tips her head right back to look straight up at the great radiating star on the barrel-vault ceiling and throws one arm up pointing at it, mouth open, delighted - and she is still moving and still pointing on the last frame. Both runs are ordinary excited-kid running at real speed with real weight: feet landing, knees bending, arms swinging, hair and jumpers moving with them. Projected shapes slide down the walls behind them and pass across their backs.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: the boy ends the clip bouncing on the sofa, the girl ends it still running and still pointing up at the ceiling. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Image 1 is a room-content reference, NOT an end frame and NOT a target pose. Do not converge to its still arrangement. The children are already mid-run before the door uncovers them; show moving limbs and changing positions from their first visible instant, with no pause to match the reference.
````

#### Video prompt — `clips/v11_c05_g2.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `c7c75cb6-0103-4fa7-95a5-ab42dc93a4e9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_153610_c7c75cb6-0103-4fa7-95a5-ab42dc93a4e9.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- image ref 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`

````text
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Image 1 supplies the room design and projection artwork only; it does not specify a frame, a moment in time, the children's positions, or any pose to reproduce. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Image 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the two children's identities and clothes, the colours, and the set and style of projected shapes. Ignore the children's reference positions, orientations and poses completely. It is not a start, intermediate, target or end frame.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole workshop picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white barrel-vault ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. Their play is one uninterrupted action that began before the door opened, with no intermediate pose or rendezvous. THE BOY with close-cropped dark curls follows a direct curving run toward the nearest sofa cushion; without stopping, facing the camera, lining up beside the girl or matching any reference position, his existing run flows straight into a jump onto that cushion and repeated excited bouncing. THE GIRL with the long copper-red braid keeps her own continuous curving run toward the Christmas tree, passing through the room independently; she glances upward and lifts one arm as she runs without planting her feet or interrupting her stride. Their paths do not converge into a side-by-side tableau. They never arrive at, recreate, hold or reset to the poses or arrangement of @Image 1, even for an instant. Movement remains continuous through the middle and last second, with grounded footfalls, bent knees, swinging arms, moving hair and knitwear. Reference-image matching must never interrupt the children's play.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: the boy ends the clip bouncing on the sofa, the girl ends it still running and still pointing up at the ceiling. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Image 1 is only a design and identity reference. There is no time at which the children must occupy its positions. Never interpolate toward it, use it as an intermediate keyframe, line the children up, pause there, then restart. Preserve the already-moving doorway reveal and carry each child's momentum continuously through the entire 5 seconds. No reference pose and no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, limestone and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and arch ribs. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.
````

#### Video prompt — `clips/v11_c05_g3.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `30db6d40-b2c2-4ad8-bdef-a7aa1d64c7e9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_155045_30db6d40-b2c2-4ad8-bdef-a7aa1d64c7e9.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- video ref 1: `content/video_11_assets/clips/v11_c07_g2.mp4` — earlier generated clip · Higgsfield media `2380e078-1cc7-464c-9594-77248972e878`

````text
CHILD MOVEMENT - PRIMARY CORRECTION: Behind the door two children are already playing chase, and they KEEP RUNNING throughout the shot. Show one continuous flow of alternating footfalls, changing positions and swinging arms. There is no arrival, regrouping, pause, pose or second activity. This movement has priority over matching any reference composition. The same closed-door opening and forward walk with upward tilt follow below.

HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the curved barrel-vault ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the plaster. @Video 1 supplies the room design, children's identities and moving projection artwork only. It is a visual room reference, not a timeline or camera reference. No frame of it is a target frame for this clip. Behind the closed door the projected movie is already playing, and it keeps running through the last frame. Smoke pours from every chimney, the ribbons radiates, the sleigh flies, the toy train travels and the elves work, the travelling gold light waves spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed three-panel forest-green door with a wreath, a hand on the brass knob. @Video 1 is a room-content reference for the layout, barrel-vault ceiling, furniture, the children's identities and clothes, colours, and moving projection artwork. Use the camera and child actions specified below, not the reference video's camera or its specific child actions. Only the closed-door start image defines frame 0.0s. No end frame is supplied.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Inside the flat projected North Pole workshop picture, illustrated smoke curls rise from the depicted tiny chimneys, leaning right, widening and fading while fresh drawn curls form below. These curls are moving pixels lying flush on the plaster or stone. The real fireplace, mantel and chimney breast release no smoke, sparks, objects or animation into the room.

THE RIBBONS. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the plaster; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.

THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the existing tiny elves keep carrying and passing wrapped gifts beside the workshop, shooting stars streak and fade, the flat projected bauble and candy-cane drawings rotate and travel along the wall and ceiling surfaces, the big gold bells swing gently on their crimson bow with their clappers swinging inside them, and the lit workshop windows flicker warm. Only the great gold Christmas star holds its centre position; its light simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, curves continuously around the barrel vault, steps over each shallow arch rib and breaks at both projecting corners of the limestone chimney and where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, the travelling gold light waves, the rippling red-and-gold ribbons, the flying sleigh, pouring snow and twinkling stars run across the whole barrel vault and over every shallow arch rib, right into all four corners. No bare un-animated patch of plaster and no bare arch rib anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white barrel-vault ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the ribbons ripples, the sleigh flies on across the ceiling, the toy train and the elves keep moving, the travelling gold light waves keep spreading and the snow keeps falling.
Inside that single move, the children are playing ONE CONTINUOUS GAME OF CHASE on the open floor. They are already mid-stride before the door reveals them. The copper-braided girl runs a broad curving path across the rug and alongside the sofa; the dark-curled boy follows two steps behind, both laughing, taking quick alternating footfalls with swinging arms. They continue their running loop naturally around the available floor space, curving away from furniture and each other. Their positions change in every successive instant, including the middle of the shot. They do not arrive at a destination, stop beside each other, face the camera, line up, switch activities or climb onto the sofa. This is already-running, still-running, keep-running: the same continuous playful action before the door opens, through the reveal and through the last frame in which they are visible. They may glance up while their feet keep stepping, but their momentum never stops. Real speed, grounded feet and natural weight; no sliding, teleporting or running in place.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the forest-green door, the brass knob, the bare forearm and its ivory sleeve, with no jewellery. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, continuous alternating running footfalls, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole barrel-vault ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: both children keep running their playful curving loop; the camera may tilt them out of view but never catches them settled into a pose. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an ribbons that sits still; a parked sleigh; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated patch of the vault in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; either child climbing or jumping onto the sofa; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

REFERENCE-ONLY LOCK - @Video 1 provides room, identity and projection appearance only. No static room image is attached. Preserve the closed-door starting frame and the established single walking-and-tilting camera move. The children are continuously running a playful chase; their actions are independent of all poses and activity changes in the reference video. Never copy the reference video's opening composition, sofa bouncing, camera movement, cuts or timing. The new clip is exactly 5 seconds and has no end frame.

SURFACE-ONLY LOCK - every animated Christmas shape, including every shape above the real fireplace, is flat projected light attached to the existing plaster, limestone and ceiling. Moving drawings follow the surface perspective and bend or clip at actual corners and arch ribs. They have no thickness, volume, free-space parallax or physical cast shadow. The real fireplace opening and mantel remain real stationary architecture. No character, sleigh, ribbon, spark, snowflake, smoke curl or ornament floats between the camera and a wall, emerges from the fireplace, hovers above the mantel, or enters the usable room. Apparent depth belongs only to the drawn illustration on the wall.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v11_c06_g1.png` → `clips/v11_c06_g1.mp4`

#### Image prompt — `starting_frames/v11_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134257_a11380c1-3dd8-4a0a-accc-481aec5fa3bf.png
**References, in submission order**
- @Image 1: `content/video_10_assets/starting_frames/v10_c06_g2.png` · Higgsfield media `37832ca3-a7dd-48b5-ba4e-187e5f082652`
- @Image 2: `content/video_9_assets/starting_frames/v9_c06_g4.png` · Higgsfield media `480dee42-d78d-4dd4-b3b0-cca1aed16477`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with warm brown skin and close-cropped dark curls, fully dressed for winter in a cosy red-and-cream knitted Christmas jumper with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a cosy bedroom with a HIPPED CEILING: a small flat rectangular central ceiling panel, four broad smooth plaster slopes descending symmetrically to the four walls, and four straight diagonal hip seams where adjoining slopes meet; no tray recess, no coffer grid and no beams. Warm cream plaster walls, a broad scalloped walnut headboard on the back wall, one deep rectangular bay window on the right with dark outside glass and burgundy curtains, two walnut bedside chests, pale oak floorboards and a wool rug. The bed is under the low part of the ceiling, leaving the central panel and all adjoining slopes clearly visible.

It is night, all house lamps switched off. The bed has a cream wool duvet with red tartan throw, pillows and a knitted stocking. A small real Christmas tree with gold lights and red ornaments stands by the bay window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including all four sloping planes and the central flat panel, wall above the headboard, bay window jambs and lintel. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one richly detailed NORTH POLE CHRISTMAS EVE panorama: Santa's red-and-gold timber workshop with glowing tiny windows, garland-wrapped columns, snow-covered roof and a toy-filled open doorway; smiling tiny elves in red and green winter clothes packing wooden toys and ribboned presents; a gingerbread bakery with icing-edged gables; rows of snow-laden fir trees hung with red baubles and gold stars; and an illuminated Christmas train carrying overflowing wrapped gifts along the bottom of the walls. Two majestic red-coated NUTCRACKER toy soldiers flank the workshop, with gold braid, black boots and precisely drawn faces. Large luminous CHRISTMAS WREATHS with scarlet bows and paired gold bells crown the upper walls. OVERHEAD, Santa in his red suit rides a richly detailed gold-runner sleigh drawn by eight reindeer across the ceiling, surrounded by arching crimson and gold ribbons of pinpoint light and long evergreen Christmas garlands woven with holly berries, striped candy canes, polished gold ornaments and ivory snowflakes. A radiant gold eight-pointed Christmas star anchors the centre overhead. The image is a single coherent richly layered storybook Christmas Eve scene on the surfaces, with deep dark sky between distinct illuminated elements; not unrelated floating icons, not physical props in the room. The dominant colours are Christmas crimson and ruby red, warm gold second, rich evergreen green and cream-white detail. No carnival Ferris wheel, no carousel, no galaxy, no nebula, no science-fiction vortex. The projected snow and all illustrated objects remain on walls and ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The flat central panel, all four sloping planes and every diagonal hip seam must be visibly legible. The sleigh, garlands and stars change perspective on each slope, kink at the straight hip seams, then break again where each sloping ceiling meets its vertical wall. Each slope foreshortens the picture differently from the flat middle panel. The bay-window recess stretches and clips the projected picture at its jambs and lintel. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no nutcrackers, no workshop, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the plaster, the crisp hip seams of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v11_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `49e73200-73f4-40ea-b642-cbc3b4aa24f8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_150958_49e73200-73f4-40ea-b642-cbc3b4aa24f8.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v11_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`

````text
Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected North Pole Christmas workshop picture is PLAYING across the cream plaster wall behind the bed and the whole hipped plaster ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the hipped ceiling with its small flat central panel, four broad sloping plaster planes and four straight hip seams, the cream plaster walls, the bed with its cream duvet and red tartan throw, the scalloped walnut headboard, the upholstered bench at the foot, the small lit Christmas tree, the wool rug, the right-hand recessed bay window with burgundy curtains, the stocking, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child, about six years old with warm brown skin and close-cropped dark curls, in cosy red-and-cream knitted Christmas jumper with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the cream plaster wall and the whole hipped plaster ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE ELVES AND THE FLOATING THINGS - the tiny elves keep passing gifts outside the workshop, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers moving inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the hip seams of the ceiling, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the cream plaster wall and the hipped plaster ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the ribbons rippling, the travelling gold light waves spreading and the sleigh flying across the hipped ceiling as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture bends at every real hip seam between the four sloping ceiling planes and the central flat panel, foreshortens on each plane and changes angle again onto the vertical walls and window recess. The planes and seams themselves never move.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v11_c07_g1.png` → `clips/v11_c07_g2.mp4`

#### Image prompt — `starting_frames/v11_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_134458_b5910d54-c9bd-4be4-9ae3-3b870ad2e793.png
**References, in submission order**
- @Image 1: `content/video_10_assets/starting_frames/v10_c07_g2.png` · Higgsfield media `9c101565-8f83-4591-9907-7aa314411d73`
- @Image 2: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the new room and children; it is the same house viewed from farther inside. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: the girl is about nine with light freckled skin and long copper-red hair tied in a loose braid; the boy is about six with warm brown skin and close-cropped dark curls. Both fully dressed in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a tall double-height English-country Christmas great room with a continuous cream plaster BARREL-VAULT ceiling: one smooth semicylindrical curve from the left wall up over the centre and down to the right wall, crossed by three evenly spaced shallow cream plaster arch ribs that follow the curve; no flat coffer grid, no ridge and no timber trusses. A tall warm limestone chimney breast stands on the back wall, a plain carved limestone mantel beneath it, two tall rectangular black-framed windows on the left, and a recessed arched doorway on the right. Pale oak floorboards, a large ivory linen sectional sofa, a rectangular upholstered ottoman and a deep-red Persian rug. The same room and decor as @Image 2, seen from the middle of the great room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, red baubles, gold ribbon and wrapped gifts stands beside the limestone fireplace. Evergreen garland with holly berries covers the mantel, with three red-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole curved barrel vault, every projecting arch rib and the limestone chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, one richly detailed NORTH POLE CHRISTMAS EVE panorama: Santa's red-and-gold timber workshop with glowing tiny windows, garland-wrapped columns, snow-covered roof and a toy-filled open doorway; smiling tiny elves in red and green winter clothes packing wooden toys and ribboned presents; a gingerbread bakery with icing-edged gables; rows of snow-laden fir trees hung with red baubles and gold stars; and an illuminated Christmas train carrying overflowing wrapped gifts along the bottom of the walls. Two majestic red-coated NUTCRACKER toy soldiers flank the workshop, with gold braid, black boots and precisely drawn faces. Large luminous CHRISTMAS WREATHS with scarlet bows and paired gold bells crown the upper walls. OVERHEAD, Santa in his red suit rides a richly detailed gold-runner sleigh drawn by eight reindeer across the ceiling, surrounded by arching crimson and gold ribbons of pinpoint light and long evergreen Christmas garlands woven with holly berries, striped candy canes, polished gold ornaments and ivory snowflakes. A radiant gold eight-pointed Christmas star anchors the centre overhead. The image is a single coherent richly layered storybook Christmas Eve scene on the surfaces, with deep dark sky between distinct illuminated elements; not unrelated floating icons, not physical props in the room. The dominant colours are Christmas crimson and ruby red, warm gold second, rich evergreen green and cream-white detail. No carnival Ferris wheel, no carousel, no galaxy, no nebula, no science-fiction vortex. The projected snow and all illustrated objects remain on walls and ceiling only. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The barrel vault remains a visible smooth semicylindrical ceiling. The sleigh, garlands and stars visibly stretch around the curved plaster and descend onto the vertical walls, never floating as a flat sheet in front of them. At each shallow transverse arch rib the projected picture steps onto the rib's near face and is offset on the surface beyond, with a narrow hard shadow on its far edge. The limestone chimney projects from the wall; imagery bends at both vertical corners, crosses the individual stone faces and breaks at each mortar joint. The arched doorway and window recesses interrupt the picture at their real edges. All raised trim casts a real hard-edged shadow behind it. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no nutcrackers, no workshop, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the limestone and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v11_c07_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `2380e078-1cc7-464c-9594-77248972e878`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_153610_2380e078-1cc7-464c-9594-77248972e878.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v11_c07_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`

````text
OPENING STATE - frame 0.0s must preserve the supplied start image's already complete, saturated projection on every visible wall, chimney surface, barrel-vault ceiling panel and arch rib. The projector has been running for a long time before filming. Full coverage and brightness remain on throughout all four seconds, while the illustrated elements are already moving. There is no lighting-up event, unveiling, growth, filling, wipe, fade-in or transition from bare plaster. Never erase the ceiling artwork at the beginning and redraw it later.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected North Pole Christmas workshop picture is PLAYING across the back wall and the whole curved barrel-vault ceiling and its shallow plaster arch ribs, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the smooth cream barrel-vault ceiling crossed by three shallow plaster arch ribs, the cream plaster walls, the tall warm limestone chimney breast and carved mantel, the two tall rectangular black-framed windows on the left with night outside, the recessed arched doorway on the right, the lit Christmas tree and its presents, the large ivory linen sectional sofa wrapping the foreground, the rectangular upholstered ottoman, the deep-red Persian rug, the pale oak plank floor, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about six with warm brown skin and close-cropped dark curls, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about nine with light freckled skin and long copper-red hair in a loose braid, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, so their knitted jumpers read clearly. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole curved barrel-vault ceiling. Everything glowing on the plaster, limestone and cream arch ribs is that one cone landing.
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, limestone and cream arch ribs and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image shows the film already fully projected across the walls AND the entire ceiling. From the first frame continue the moving artwork at the same full coverage and brightness. Start motion within the existing picture, never the appearance of the picture itself. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster arch ribs, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny elves keep passing gifts beside the workshop and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, limestone and cream arch ribs. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the curved barrel-vault ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: blank or partly blank walls or ceiling at the start; a projection appearing, switching on, fading in, spreading, growing or revealing itself during the shot; an opening before-and-after transformation; a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the barrel vault or an un-animated arch rib in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture follows the real curve of the barrel vault, steps across each shallow arch rib with the proper offset and occlusion shadow, and bends at the projecting limestone chimney corners. The ceiling, arch ribs, stone and walls themselves never move.
````

**Other takes of C07 on disk (1)**

#### Video prompt — `clips/v11_c07_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `a4b77adb-67a0-4299-b927-544fb77b1e3d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_150958_a4b77adb-67a0-4299-b927-544fb77b1e3d.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`

````text
Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected North Pole Christmas workshop picture is PLAYING across the back wall and the whole curved barrel-vault ceiling and its shallow plaster arch ribs, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the smooth cream barrel-vault ceiling crossed by three shallow plaster arch ribs, the cream plaster walls, the tall warm limestone chimney breast and carved mantel, the two tall rectangular black-framed windows on the left with night outside, the recessed arched doorway on the right, the lit Christmas tree and its presents, the large ivory linen sectional sofa wrapping the foreground, the rectangular upholstered ottoman, the deep-red Persian rug, the pale oak plank floor, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about six with warm brown skin and close-cropped dark curls, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about nine with light freckled skin and long copper-red hair in a loose braid, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in cosy red-and-cream knitted Christmas jumpers with white snowflakes and green Christmas trees, dark-green lounge trousers and cream knitted socks, so their knitted jumpers read clearly. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole curved barrel-vault ceiling. Everything glowing on the plaster, limestone and cream arch ribs is that one cone landing.
THE PICTURE - the animated scene that cone is playing: the exact North Pole Christmas Eve workshop panorama visible in the start image, with Santa's glowing red-and-gold timber workshop, elves packing wooden toys and wrapped presents, gingerbread bakery, snowy fir trees with red baubles, the lit gift-carrying toy train along the lower walls, two red-and-gold nutcrackers, wreaths and paired gold bells with crimson bows. On the ceiling, Santa in his sleigh with eight flying reindeer, existing crimson and gold ribbons and evergreen garlands with holly berries, candy canes, gold ornaments, ivory snowflakes and one radiant eight-pointed Christmas star. No Ferris wheel, carousel, frozen pond or new ripple rings; animate the things already present.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster, limestone and cream arch ribs and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the ribbons, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE RIBBONS - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE TOY TRAIN AND THE ELVES. The illuminated Christmas toy train TRAVELS steadily along the lower wall, its wheels rotating and its gift-filled wagons following the track around the wall corners; it covers about one carriage length every second, never parked. The tiny elves already visible beside Santa's workshop continuously bend, lift the existing wrapped gifts and pass them hand to hand, arms and legs moving at brisk real-time speed. The large red-and-gold nutcrackers gently march their legs and raise and lower their arms on the projected surface. All keep moving from the first frame to the last.
- THE GOLD LIGHT WAVES. Successive bright gold waves TRAVEL OUTWARD along the existing red-and-gold ribbon and evergreen-garland paths on the ceiling, each bright crest travelling about a third of its ribbon's length every second, fading behind as the next bright crest follows, so the existing ribbons sparkle and flow continuously. No new rings or new objects appear; the moving light stays within the shapes that already exist in the image.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the plaster arch ribs, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny elves keep passing gifts beside the workshop and the big gold bells swing gently on their crimson bow with the clappers moving inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE GREAT CHRISTMAS STAR - the gold eight-pointed star is the ONLY element that holds its centre position. It stays exactly where it is on the ceiling for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the ribbons and the stars on the wall are doing, the flakes, the ribbons and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster, limestone and cream arch ribs. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the deep-red Persian rug, the ivory linen sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the curved barrel-vault ceiling fills the upper half of the frame, the ribbons rippling along it, the travelling gold light waves still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an ribbons that sits still; a sleigh and reindeer parked in one place; a toy train that does not travel or elves that do not move; travelling gold light waves that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated area of the barrel vault or an un-animated arch rib in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.

CONTINUOUS MOTION CHECK - from the first visible frame through the very last frame, the wall AND ceiling each contain clearly travelling projected elements at the same time: the sleigh changes position across the ceiling, its reindeer gallop; the train advances along the wall; elves move and pass gifts; bells swing; ribbons carry travelling light waves; snowflakes translate across the surfaces. Twinkle alone and camera movement alone do not count. Maintain that same lively real-time motion with no opening freeze, no settling into a still image and no final freeze. All light bends with the real wall and ceiling geometry and stays on those surfaces.

SURFACE MAPPING - the moving picture follows the real curve of the barrel vault, steps across each shallow arch rib with the proper offset and occlusion shadow, and bends at the projecting limestone chimney corners. The ceiling, arch ribs, stone and walls themselves never move.
````
