# Video 4 - MerryGlowUSA Christmas projector B-roll

**Current status (2026-09-22):** All five selected clips, including the hook, upscaled with ByteDance Pro at 2K/30 fps. AIGC for C01; Common for C02-C05. Originals preserved; upscales saved directly under clips/upscaled with exact source names. Verified 1440x2560, 30 fps, audio present and full decode exit 0. Board points to the upscales.

## Reusable blocks

GPT Image 2.5 Sunburst; 2K; medium; 9:16. Exact reusable camera, scale and quality blocks appear verbatim in each prompt below.


## C02 - frame take 1

**File:** starting_frames/v4_c02_g1.png
**Status:** submitted; awaiting result.
**Job ID:** 6dddb32c-15b8-4f79-a196-ccbc3442cfea
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"ce82f8a0-2382-4681-892e-d3490b97f74e"},{"role":"image","value":"4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919"}]}
**References:** @Image 1: ../video_2_assets/starting_frames/v2_c02_g1.png (job/media ce82f8a0-2382-4681-892e-d3490b97f74e); @Image 2: ../../product_images/box_heritage_green_g1.png (job/media 4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919)
**Lineage:** Reused from v2 C02 frame g1 — changed only skin/sleeve, materials, room decor and Christmas landscape nouns for Video 4; framing, scale, geometry and quality instructions retained.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Replace the FIRST reference's carton with OUR MerryGlowUSA product box exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton with forest green body, a blank dark-red band across the top bordered in gold, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold-and-red star-and-tree burst over a printed render of a white cylindrical projector in a white U-shaped pivoting bracket on a round flat white base, a black circular slatted front grille with a central glass lens, a slim black remote printed beside it, gold village skyline along the bottom, and the bottom labels REMOTE CONTROL, 45 MIN, 90 MIN, no transparent window. Preserve the tilted projector ILLUSTRATION printed on the box exactly; it is artwork only. The physical projector is concealed in the closed carton in this starting frame. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only the product carton, the table and the background; keep the hands and pose.

FIRST - THE HANDS. A woman's hands, about 35, with light warm-beige skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep forest-green knitted wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a spacious festive American dining room with warm cream walls, dark-oak built-in shelves, an arched antique-brass mirror, a white brick fireplace with ivory stockings and a tall Christmas tree with red glass ornaments, gold bells and warm-white lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The red band must remain BLANK, exactly as on the SECOND attached reference. No THEXMASGLOW wordmark, no invented MerryGlowUSA wordmark, no brand name added anywhere on the carton. Preserve the exact headline and bottom labels from the SECOND reference, sharp and legible.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, box placement, hand positions and camera. @Image 2 owns the MerryGlowUSA carton geometry and product identity. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt

Still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Video prompt - take 1
**Clip:** `clips/v4_c02_g1.mp4`
**Job ID:** `9d57b955-e8c2-464a-9899-916b0380c2f0`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `6dddb32c-15b8-4f79-a196-ccbc3442cfea` = `starting_frames/v4_c02_g1.png`
- image `a377849d-5074-4036-bb06-c73ae580a73a` = `starting_frames/v4_c03_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 2198356 bytes.
**Upscale:** `clips/upscaled/v4_c02_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing MerryGlowUSA carton. Keep the blank dark-red top band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and black remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls frame 0.0s, the exact printed box, hands, table, room, props and light. @Image 1 is the approved C03 image and supplies ONLY the actual upright projector design and orientation, not its kitchen or hands. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a blank dark red band across the top, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white cylindrical projector in a white U-shaped bracket on a round base, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: the exact larger matte-white upright CYLINDER shown in @Image 1, retaining its full physical size and proportions, in its white U-shaped bracket on a flat round white base. The cylinder axis is VERTICAL, lens facing straight UP at the ceiling. Its flat circular black slatted top face surrounds a central blue lens. The top face is BLACK and stays black for every frame. The cylinder is locked upright relative to its bracket throughout the lift; never inclined on the mount, never copied from the angled illustration on the carton. Round base horizontal. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a deep forest-green knitted wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, the supplied festive dining room with warm cream walls, dark-oak built-in shelves, an arched antique-brass mirror, a white brick fireplace with ivory stockings and a tall Christmas tree with warm-white lights, red glass ornaments and gold bells. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK slatted circular top face and central blue lens visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
```


## C04 - reference take 1

**File:** references/v4_c04_r1.png
**Status:** submitted; awaiting result.
**Job ID:** 81006fa3-03cd-43e5-8db4-bc59b8c62bb0
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"38a01390-440a-4f96-8feb-1274528f605b"},{"role":"image","value":"c65fa6e9-597c-4be1-a4c4-0348d73c6d2b"}]}
**References:** @Image 1: ../video_2_assets/references/v2_c04_r1.png (job/media 38a01390-440a-4f96-8feb-1274528f605b); @Image 2: ../video_2_assets/starting_frames/v2_c05_g1.png (job/media c65fa6e9-597c-4be1-a4c4-0348d73c6d2b)
**Lineage:** Reused from v2 C04 reference r1 — changed only skin/sleeve, materials, room decor and Christmas landscape nouns for Video 4; framing, scale, geometry and quality instructions retained.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create one vertical 9:16 LIGHTS-OFF REFERENCE FRAME for a new MerryGlowUSA Christmas projector video. @Image 1 owns the exact room layout, camera position, viewing direction and furniture arrangement; change only the room materials/decor listed below and improve the projected view. @Image 2 supplies the Christmas-window theme only, never its blur, painterly scenery or protruding window geometry. Create a real handheld iPhone photograph of a real bedroom with a luminous flat wall projection.

KEEP THE ROOM LAYOUT FROM @Image 1 but use these new materials: warm cream plaster walls and ceiling, medium honey-oak floor, burgundy wool rug, king-size dark-oak bed with a crisp ivory cotton quilt and burgundy-and-cream tartan runner, two cream cable-knit cushions and one central forest-green cushion, ivory pillows, dark-oak nightstands and aged-brass lamps, oatmeal linen curtains behind the headboard on the BACK wall, real fir garland with warm pin lights and deep-red bows around the headboard, tall Christmas tree in the back-right corner, forest-green upholstered bench at the foot of the bed with an ivory woven throw over its right side. Same spatial layout and distances. The LEFT wall remains a solid flat wall with no actual windows.

CAMERA LOCATION: preserve @Image 1's existing viewpoint, standing to the right of the foot of the bed and looking diagonally LEFT toward the long wall. The enormous projected window view fills the left and central 70 percent of the picture; the familiar bed, runner and a sliver of the garland-wrapped headboard appear along the lower-right and right edge. Correct consistent perspective, no mirrored layout, no moving walls, no relocated bed. This will be the reveal orientation; the matching lights-on frame will be made by rotating the phone RIGHT from this same physical standing point. No people or hands visible.

LIGHTS ARE NOW OFF: the ceiling-fan light and both bedside lamps are off, warm bulbs not glowing. Keep only tiny Christmas garland/tree pin lights and the spectacular wall projection as illumination. Expose expertly for the projection while keeping real bedding folds and room silhouettes readable; beautifully subtle icy blue and golden light spill on the near cream duvet and pale floor.

THE PAYOFF ON THE LEFT WALL: one huge brilliant, high-contrast projection of an elegant grand arched window with warm timber mullions. Frame and scenery are projected onto the SAME FLAT WALL, with no structural opening. Through the panes is ONE continuous photographic landscape: a magnificent REALISTIC Austrian lakeside Christmas town beneath immense snowy Alps: a few beautifully resolved pastel village houses and timber chalets with thick fresh snow on roofs, glowing amber windows and clearly visible smoking chimneys, a graceful narrow church spire beside the lake, a grand decorated Christmas spruce and golden lanterns in the waterfront square, a charming illuminated Christmas market, and an old stone footbridge crossing a small stream into the dark-blue lake. The still water mirrors the warm village lights and natural emerald-and-rose aurora. Snow-laden fir branches frame the view beyond the window. Santa's small sleigh and a clear team of reindeer cross the upper sky. Fine individual snowflakes, luminous gold lights, forest green and deep cobalt snow. Vast mountain scale and photographic depth with a few legible hero buildings rather than countless tiny smeared buildings. Every pane shows its proper part of the same continuous landscape, with no repeated panels. Opaque-looking, crisp dark mullions form an uninterrupted foreground layer all the way down to the projected sill. Scenery and snowy branches remain BEHIND every mullion, never overlapping or interrupting its base.

PROJECTION PHYSICS: substantially stronger, richer and less transparent than @Image 1. Dense luminous color and decisive contrast cover the wall, no ghostly double exposure and no pale wall color washing through the scenic image. Deep dark window-frame shapes, brilliant controlled highlights without bloom, clear photographic details. The room is dark enough for a vivid high-output projection. Wall texture is only a barely perceptible surface grain, not visible through the buildings. All projected geometry is FLAT on the wall, follows one coherent perspective, and stays bounded by the real ceiling junction and baseboard. Physically believable blue and gold light spill on actual bedding; natural room shadows, no beam haze. Vivid projection while retaining real-room photographic credibility.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
```

### Video prompt

Not submitted; stills only.


## C03 - frame take 1

**File:** starting_frames/v4_c03_g1.png
**Status:** submitted; awaiting result.
**Job ID:** a377849d-5074-4036-bb06-c73ae580a73a
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"0b51a9d5-141b-4052-a50b-62619fc01123"},{"role":"image","value":"6dddb32c-15b8-4f79-a196-ccbc3442cfea"}]}
**References:** @Image 1: ../video_1_assets/starting_frames/v1_c03_g3.png (job/media 0b51a9d5-141b-4052-a50b-62619fc01123); @Image 2: ../video_4_assets/starting_frames/v4_c02_g1.png (job/media 6dddb32c-15b8-4f79-a196-ccbc3442cfea)
**Lineage:** Reused from v2 C03 frame g1 — changed only room materials, decor, skin/sleeve and scenery nouns for Video 4. Camera, framing, enlarged lens-UP product scale and image-quality blocks retained. References use the matching new C02/C04 reveal where applicable.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create the next MerryGlowUSA C3 photograph using @Image 1 for the upright product design, kitchen composition and camera, and @Image 2 for the real product SCALE relative to its carton and adult hands, the skin and sweater. Make the physical projector appreciably BIGGER than @Image 1 so it matches the product that fits inside the carton in @Image 2. Use the new kitchen and materials below. Keep the cylinder perfectly upright, lens pointing straight UP.

KEEP THE COMPOSITION FROM @Image 1: the camera position, camera height, lens, distance, vertical 9:16 crop, the general two-handed supporting pose, central product placement and forearm entry points. Enlarge the complete projector about 40 percent relative to the adult hands and picture; adapt finger contacts naturally to the larger device, keeping anatomy and hand size realistic.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with light warm-beige skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a deep forest-green knitted wool sweater sleeve pushed back; right forearm enters from the right in the same deep forest-green knitted wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the complete upright projector, from the top black lens panel to the bottom round base, occupies about 42 percent of the full image height. Base diameter occupies about 30 percent of image width. A substantial real device held in two adult hands, not a miniature. Its actual overall height is about 80-85 percent of the tall carton in @Image 2, allowing realistic packaging clearance. Enlarge all product components together, preserve their original proportions and ordinary adult hand dimensions. Keep visible air beneath the base and counter. Both hands support the device firmly and naturally.

THE PRODUCT - the same MerryGlowUSA matte-white cylindrical projector barrel in its white U-shaped pivot bracket on a round flat white base. USER-CONFIRMED ORIENTATION: THE CYLINDER STANDS VERTICALLY UPRIGHT, WITH THE BLACK LENS/GRILLE FACE ON TOP POINTING STRAIGHT UP AT THE CEILING. Retain @Image 1's already confirmed upright lens-UP orientation without any tilt. Its long axis is vertical and PERPENDICULAR to the horizontal circular base, like an upright can standing on end. The circular black slatted lens face is a HORIZONTAL TOP FACE, parallel to the round base, visible from above as an ellipse at this existing camera height; the central blue glass lens looks upward. The solid white barrel extends straight down below that top face, sitting vertically between the two upright support arms. The round base remains flat and horizontal, and the support arms remain vertical. The projector does NOT point at the camera, does NOT lie sideways, and does NOT lean diagonally. No forward-facing black front disc: the black disc is now on TOP. Preserve the exact existing cylinder shell, horizontal ventilation slats across the black lens panel, blue glass lens, side pivot, U bracket and circular base; do not replace it with the older dome projector or four-legged stand. @Image 2 supplies product materials and component identity only; IGNORE its printed tilted pose. The device has the same design and upright configuration as @Image 1.

THE COUNTER - a pale ivory quartz counter with fine warm-grey veins, a straight eased edge and matte surface. Same shape, position and amount visible as @Image 1.

THE KITCHEN - a sharply resolved traditional Christmas kitchen: warm mushroom shaker cabinets with aged bronze pulls, ivory handmade square tiles, honey-oak open shelves, a white enamel range, burgundy velvet ribbons, warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree in the far corner. Balanced soft window fill and warm interior light, realistic iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns camera, layout and upright product geometry only, not its undersized scale. @Image 2 owns the adult hand appearance, sweater, material realism and physical carton-to-projector scale. Its printed tilted product illustration must NEVER set the real projector orientation. The physical unit is larger, perfectly vertical, lens UP. All parts in natural crisp iPhone deep focus, no portrait mode, bokeh or blur.
```

### Video prompt

Still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Video prompt - take 1
**Clip:** `clips/v4_c03_g1.mp4`
**Job ID:** `b81ca219-faa7-4983-9d80-fbef2ba6dabf`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `a377849d-5074-4036-bb06-c73ae580a73a` = `starting_frames/v4_c03_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 1761623 bytes.
**Upscale:** `clips/upscaled/v4_c03_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale ivory quartz counter with fine warm-grey veins and a straight eased edge, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - the exact matte-white upright CYLINDER in the start image, in its white U-shaped bracket on a flat round white base. Cylinder axis VERTICAL, lens pointing straight UP at the ceiling. Its black slatted circular top face surrounds the central blue lens. The top face is BLACK and stays black for every frame. The cylinder stays locked upright within the bracket throughout; no inclination on its mount. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in deep forest-green knitted wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a pale ivory quartz counter with fine warm-grey veins and a straight eased edge; behind it warm mushroom shaker cabinets with aged bronze pulls, ivory handmade square tiles, honey-oak shelves, a white enamel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the pale ivory quartz counter with fine warm-grey veins and a straight eased edge, matte rather than mirror-polished.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the round base and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the cylinder, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the base approaches the stone.
3.0-3.4s - the flat round base of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has; those tiny movements affect the WHOLE rigid product, never a rotation of the cylinder inside the bracket. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the cylinder.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
```


## C04 - frame take 1

**File:** starting_frames/v4_c04_g1.png
**Status:** submitted; awaiting result.
**Job ID:** 7ec309eb-af70-4367-b50c-4850ec4e3479
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"81006fa3-03cd-43e5-8db4-bc59b8c62bb0"},{"role":"image","value":"11720edc-b38f-48f6-bc92-8278407f2181"}]}
**References:** @Image 1: ../video_4_assets/references/v4_c04_r1.png (job/media 81006fa3-03cd-43e5-8db4-bc59b8c62bb0); @Image 2: ../video_1_assets/starting_frames/v1_c04_g3.png (job/media 11720edc-b38f-48f6-bc92-8278407f2181)
**Lineage:** Reused from v2 C04 frame g1 — changed only room materials, decor, skin/sleeve and scenery nouns for Video 4. Camera, framing, enlarged lens-UP product scale and image-quality blocks retained. References use the matching new C02/C04 reveal where applicable.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create the LIGHTS-ON STARTING FRAME by editing @Image 1, the existing matching lights-off bedroom reference. Keep the photographer in the EXACT SAME physical place, at the same eye height, with the same lens and standing location as @Image 1, but ROTATE THE PHONE TO THE RIGHT by roughly 30 degrees. The viewing direction and framing MUST change; the camera's physical location must not. @Image 1 owns all geometry. @Image 2 is the previous lights-on image and supplies ONLY the brightness, realistic photographic look and red-sleeved hand holding the black MerryGlowUSA remote; it must NOT control camera position or framing. Changes are only: turn the phone's view RIGHT from that stationary location, turn room lights on, turn the wall projection completely off, and add the remote hand.

KEEP THE ROOM FROM @Image 1: warm cream plaster walls and ceiling, medium honey-oak floor, burgundy wool rug, king-size dark-oak bed with a crisp ivory cotton quilt and burgundy-and-cream tartan runner, two cream cable-knit cushions and one central forest-green cushion, ivory pillows, dark-oak nightstands and aged-brass lamps, oatmeal linen curtains behind the headboard on the BACK wall, real fir garland with warm pin lights and deep-red bows around the headboard, tall Christmas tree in the back-right corner, forest-green upholstered bench at the foot of the bed with an ivory woven throw over its right side. Same spatial layout and distances. The LEFT wall is an uninterrupted plain warm-ivory wall with no actual windows. It remains the same solid flat wall.

CAMERA LOCATION VERSUS VIEW DIRECTION - CRITICAL CORRECTION: the photographer's feet and the camera lens centre stay exactly at @Image 1's viewing point, to the right of the foot of the bed, at the same height. From there, turn the phone RIGHT about 30 degrees, with no sideways movement, no walking and no zoom. The starting image looks more toward the bed and its headboard/back curtains; the bed and upholstered foot-bench become the central subjects. The left projection wall recedes diagonally along only the LEFT 20-30 percent of the starting image, not across the middle. The back-left room corner shifts clearly LEFTWARD in the picture compared with @Image 1. Show more of the back wall, headboard and right-hand part of the bedroom. The perspective still comes from the same off-centre spot right of the bed's foot, never the central doorway view. Do not preserve @Image 1's exact crop or orientation: that was the previous mistake. Do not move any furniture or mirror the room. This frame is the START BEFORE a future LEFTWARD PAN: the camera will later rotate left from this fixed spot to arrive at @Image 1's reveal framing. Capture the right-facing starting orientation now.

LIGHTS ARE NOW ON: the ceiling-fan light and both bedside lamps illuminate the same room with clean warm light. Keep the fairy lights on the headboard and tree. Match the well-exposed natural warm interior-photo look of @Image 2, while preserving @Image 1's room geometry and applying the new right-facing camera orientation. Fine duvet, rug and wood details stay crisp; do not make the room dark.

THE LEFT WALL BEFORE ACTIVATION: completely REMOVE the entire projected Christmas scene AND every projected arch, window frame, mullion, sill, frost edge and glow from @Image 1. The same wall is now one continuous blank smooth warm-ivory wall, with its real baseboard and ceiling junction in their original positions. No actual window exists on this left wall. No remnants, embossed arches, ghost outlines, rectangular screen, poster or scenery. The real white curtains on the BACK wall remain.

REMOTE HAND: add the same adult right hand and red pajama sleeve visible in @Image 2, entering naturally from the lower right and holding the exact same slim black MerryGlowUSA remote at a comfortable arm's length. The thumb is poised over the central OK/play control before pressing; correct five-finger anatomy, black direction pad, red power button, matching remote scale. Keep the hand low in the right foreground, leaving the blank left wall and its corner unobstructed. It must read as the POV of the person standing at @Image 1's fixed location, not a second person or floating hand. No product box.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
```

### Video prompt

Still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Video prompt - take 1
**Clip:** `clips/v4_c04_g1.mp4`
**Job ID:** `da16f526-c050-4ac9-a1ec-ffec26e37c3c`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 5, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `7ec309eb-af70-4367-b50c-4850ec4e3479` = `starting_frames/v4_c04_g1.png`
- image `81006fa3-03cd-43e5-8db4-bc59b8c62bb0` = `references/v4_c04_r1.png`
- image `b3902899-d75c-4875-ae1e-3c0e4fbec222` = `unresolved on this drive`
**Output verification:** 720x1280; 24/1 fps; 121 frames; encoded duration 5.05s; audio stream aac; 1899819 bytes.
**Upscale:** `clips/upscaled/v4_c04_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
One continuous 5-second POV handheld iPhone video. The attached start image is the EXACT first frame and owns the bedroom geometry, bed, bench, rug, red sleeve, hand and black remote. @Image 1 supplies the Christmas projection artwork for the LEFT wall. Its bedroom perspective is not an endpoint to morph into. Keep the physical room of the starting frame throughout. @Video 1 is the approved Video 1 C04 clip, used as a MOTION reference only: closely copy its quick thumb press, natural lowering of the remote hand and subsequent leftward handheld camera pan. Do not copy its different bedroom, lower image quality, text overlays or sound.

0.0-0.2s: from the supplied remote position the wrist makes a small natural forward/up adjustment and the thumb visibly depresses the play/OK button ONCE. Match the reference's immediate decisive press, not a long aiming gesture.
At exactly the button depression, around 0.2s: the ceiling light and bedside lamps switch OFF instantly, and the luminous Christmas-window projection switches ON on the LEFT wall in the SAME moment. No delayed reveal and no gradual fade. Existing Christmas fairy lights remain dimly lit.
0.2-1.6s: the hand relaxes and naturally lowers the still-gripped remote down toward the lower right and out of view, following @Video 1's hand movement. No waving, no tossing the remote, no second press. Simultaneously begin a gentle continuous pan LEFT at normal handheld-phone pace.
1.6-4.2s: continue rotating the phone LEFT from the same standing spot until the left wall projection dominates the view, showing @Image 1's artwork from the actual camera's viewpoint. The bed shifts toward the right edge as a result of this rotation. No walking forward, no sideways camera translation, no zoom and no cut. Natural tiny hand tremor, coherent room perspective.
4.2-5.0s: settle into the spectacular left-wall view with slight natural handheld drift.

ROOM RIGIDITY: Keep the starting room a single solid three-dimensional space. Its flat left wall, straight ceiling junction, rear curtain wall and floor remain rigidly connected at fixed angles. The camera turns within that room; walls never rotate, bend, expand, slide or change shape. The bench, bed, rug and ceiling fan keep their original dimensions and positions. Preserve the burgundy-and-cream tartan bed runner and burgundy rug from the starting image; do not borrow the red runner or green rug from @Video 1. The sole tall Christmas tree remains to the RIGHT of the bed. The projection is flat light on the existing left wall, not an opening or new room. The window artwork obeys that wall's perspective and remains fixed on it. Use @Image 1 for artwork content only, never its room outline or furniture placement.

The wall projection must be a visibly ANIMATED Christmas scene, never a frozen still. Preserve @Image 1's window framing and continuous snowy Austrian lakeside Christmas town, illuminated houses, trees, lake, mountains, aurora and sleigh. From the instant the projection appears through the final frame, soft smoke continuously curls upward and drifts from multiple house chimneys, Santa's sleigh and pulling reindeer visibly travel across the sky with gently cycling reindeer legs, and luminous aurora curtains continuously ripple and flow. Fine snow falls within the projected scene; lake reflections shimmer gently. All this motion occurs INSIDE the projection. The projected window frame remains fixed to the real wall. The entire projection does not slide, breathe, scale or float. Preserve the actual bedroom walls, bedding and furniture as solid stationary physical objects. Projection light naturally spills across the room and duvet after the click.

Sharp realistic iPhone footage, clean low-light exposure and detailed moving scenery. Exactly one visible hand holding one remote, natural thumb anatomy. No new person, no real window opening in the wall, no overlay text, no watermarks, no scene transition, no reversed pan, no music. Only quiet bedroom ambience, subtle sleeve movement and the single dry remote click. Ignore all audio in @Video 1. (no BGM). No subtitles.
```


## C05 - frame take 1

**File:** starting_frames/v4_c05_g1.png
**Status:** submitted; awaiting result.
**Job ID:** 4cc5336f-bbc1-4e91-bc9d-84b485026ec0
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"c65fa6e9-597c-4be1-a4c4-0348d73c6d2b"},{"role":"image","value":"81006fa3-03cd-43e5-8db4-bc59b8c62bb0"}]}
**References:** @Image 1: ../video_2_assets/starting_frames/v2_c05_g1.png (job/media c65fa6e9-597c-4be1-a4c4-0348d73c6d2b); @Image 2: ../video_4_assets/references/v4_c04_r1.png (job/media 81006fa3-03cd-43e5-8db4-bc59b8c62bb0)
**Lineage:** Reused from v2 C05 frame g1 — changed only room materials, decor, skin/sleeve and scenery nouns for Video 4. Camera, framing, enlarged lens-UP product scale and image-quality blocks retained. References use the matching new C02/C04 reveal where applicable.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create a new hyperrealistic low-light iPhone photograph for MerryGlowUSA C5. @Image 1 supplies ONLY the low bed-level camera position, wide full-wall composition and continuous foreground window-frame layout. Do NOT copy its blurry rendering, painterly scenery, stone texture or fake CGI surfaces. @Image 2 supplies the new photographic Christmas landscape and rich opaque-looking projection. Render the entire image afresh in crisp native detail. Real bedroom materials: ivory cotton duvet with visible fine woven texture and burgundy blanket edge, a simple low dark-oak cabinet, a modest real potted fir, warm cream wall and honey-oak floor. Preserve the believable low lying-in-bed perspective from @Image 1. Use elegant warm timber Gothic projected arches with slender mullions. ALL window arches, vertical posts and bottom sill form one continuous opaque foreground layer over the scenery. Every post runs uninterrupted from the arch to a clear connection with the sill. Snow, trees, roofs and lights are behind the frame and can NEVER overlap, erase or interrupt a post at its bottom. The entire frame and scenery are FLAT projected light on the solid wall, never actual structural windows or protruding architecture.

POV lying comfortably in bed, camera at pillow height, no visible person, face or hands. Real softly folded duvet fills the lower foreground with exceptionally clear weave, seams and natural weight. The broad wall ahead is covered edge to edge and ceiling-junction to baseboard by one seamless luminous panorama seen through tall elegant Gothic timber window arches. BOTH window architecture and landscape are projected light on the plain wall, not actual openings. ALL visible wall is covered, including both sides. The panorama continues beyond the crop with room for a later LEFTWARD PAN; no blank strip or cropped-off projection rectangle. The real ceiling junction, room corner and baseboard establish the physical room. Main lights off, believable controlled blue and golden reflected light on the actual duvet and cabinet. One coherent flat wall perspective, straight window posts, no warped arches. The distant landscape has believable photographic depth inside the projected panes but does not extend physically into the room.

Beyond the coherent projected arches is ONE continuous spectacular Christmas view: a magnificent REALISTIC Austrian lakeside Christmas town beneath immense snowy Alps: a few beautifully resolved pastel village houses and timber chalets with thick fresh snow on roofs, glowing amber windows and clearly visible smoking chimneys, a graceful narrow church spire beside the lake, a grand decorated Christmas spruce and golden lanterns in the waterfront square, a charming illuminated Christmas market, and an old stone footbridge crossing a small stream into the dark-blue lake. The still water mirrors the warm village lights and natural emerald-and-rose aurora. Snow-laden fir branches frame the view beyond the window. Santa's small sleigh and a clear team of reindeer cross the upper sky. Fine individual snowflakes, luminous gold lights, forest green and deep cobalt snow. Vast mountain scale and photographic depth with a few legible hero buildings rather than countless tiny smeared buildings. The scene must be photorealistic location photography, not a fairytale painting, video-game environment, miniature model or 3D illustration. Clearly separate near snow-laden fir branches, the legible hero village buildings and immense distant mountains. Steam/smoke visibly rises above the chimneys, the small Santa sleigh and its reindeer are already present, and the bright aurora is already present. Every pane shows its proper portion of the same continuous view. Never repeat identical views in adjacent panes. Rich dense luminous color, brilliant but controlled Christmas lights, deep blue snowy shadows and clear natural texture; not translucent or washed out. Window posts remain dark solid continuous shapes in front of all outdoor objects, joined to the sill. Keep real-room light spill subtle and physically plausible.

CRITICAL IMAGE QUALITY: crisp, clean native-2K iPhone photograph with excellent low-light exposure and deep focus across foreground bedding, furniture, wall and the projected scenery. Clearly resolved duvet weave and seams, wood grain, plant leaves, stone tracery edges, individual rooflines, window mullions, snow on branches, distant palace towers and chimney outlines. High microcontrast without oversharpened halos. Render every visible surface freshly and precisely; do not copy softened or smeared pixels from the references. No shallow depth of field, no soft duvet, no haze, no fog over the image, no glowing bloom hiding detail, no gaussian blur, no motion blur, no muddy shadows, no painterly smearing, no grain, no bokeh, no fisheye or barrel distortion. Maintain natural photographic light and texture, not a plastic CGI render. No text, captions, watermarks or playback icons.
```

### Video prompt

Still-image round: no clip was requested at that stage. The animation request and the exact submitted take are archived below, recovered verbatim from the generation record on 2026-09-23.

### Video prompt - take 1
**Clip:** `clips/v4_c05_g1.mp4`
**Job ID:** `f39219d2-e80d-407d-828e-47a66a75650f`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; no other parameter was archived for this round.
**References, in attached order:**
- start_image `4cc5336f-bbc1-4e91-bc9d-84b485026ec0` = `starting_frames/v4_c05_g1.png`
- image `4cc5336f-bbc1-4e91-bc9d-84b485026ec0` = `starting_frames/v4_c05_g1.png`
**Output verification:** 720x1280; 24/1 fps; 97 frames; encoded duration 4.05s; audio stream aac; 2149377 bytes.
**Upscale:** `clips/upscaled/v4_c05_g1.mp4` exists on disk - ByteDance Pro, 2K/30 fps. No upscale job ID was archived for this round.

```text
A four-second handheld first-person RIGHT PAN from bed, beginning at exactly the supplied photograph. The lens is at pillow height above the ivory cotton duvet. This is a phone recording of a Christmas projection covering a bedroom wall.

Immediately turn the recording camera to the RIGHT through a broad 35-45 degree arc over the full four seconds, in one continuous, clearly visible sweep. By 1.5 seconds the cabinet, potted fir and the starting leftmost window arch have completely left the left edge. Keep turning until the window arch that begins at the far RIGHT of the starting photograph is near the MIDDLE of the view, revealing more of the projected wall beyond the original right edge. The entire bedroom view changes naturally with this turn: the duvet, baseboard, ceiling edge and wall-fixed window posts all travel LEFT across the recording together. This is a substantial rightward turn of the recording phone, not a tiny drift. A relaxed wrist movement with slight hand wobble, constant lens, no zoom or sideways travel. Only the room and bedding are visible; the recording person, their hands and phone stay behind the lens.

The projected scene plays like an animated Christmas illustration on a screen fixed to the wall. The Gothic window borders, village buildings, waterfront village houses and mountains remain stationary on that screen. Houses do not change window panes. The illustration has no panning camera of its own.

Animate these subjects clearly from beginning to end: rolling plumes of white smoke rise and curl from several fixed chimneys; Santa's sleigh travels across the sky behind running reindeer, passing the stationary moon; broad emerald aurora ribbons wave and ripple above stationary mountain peaks. Falling snow and rippling lake reflections add continuous movement. Window posts stay intact in front of all these moving subjects. Keep the rest of the scene still relative to the wall while the recording camera turns.

One uncut realistic iPhone night shot, sharp room textures and luminous projection, natural room ambience. No visible devices, cuts, captions or music.
```


## Completed image round - 2026-09-22

All five images completed and downloaded at 1520 x 2688. Awaiting Daniel's review. Hooks deferred and no animation submitted. Earlier submitted status is historical.

### Completion - starting_frames/v4_c02_g1.png
**Job ID:** 6dddb32c-15b8-4f79-a196-ccbc3442cfea
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151947_6dddb32c-15b8-4f79-a196-ccbc3442cfea.png
**SHA256:** 32405b3bb2197861017784b5ff4d8895044ffbc1d00569137a1ff92e50c6a4d7

### Completion - references/v4_c04_r1.png
**Job ID:** 81006fa3-03cd-43e5-8db4-bc59b8c62bb0
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151954_81006fa3-03cd-43e5-8db4-bc59b8c62bb0.png
**SHA256:** 595bb6285846089e3899f1e04411ef87de5855a93774b7ddfd2a41a4fd5a0873

### Completion - starting_frames/v4_c03_g1.png
**Job ID:** a377849d-5074-4036-bb06-c73ae580a73a
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153816_a377849d-5074-4036-bb06-c73ae580a73a.png
**SHA256:** fcc1ea354a6cc7e70eed9a70cb3d4a2565299adf4e3267fe2aad093cbe2c15c1

### Completion - starting_frames/v4_c04_g1.png
**Job ID:** 7ec309eb-af70-4367-b50c-4850ec4e3479
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153808_7ec309eb-af70-4367-b50c-4850ec4e3479.png
**SHA256:** da9faef648bec9ba963323bc3a02ccec95048a243d5a42d6937d9f305faaf604

### Completion - starting_frames/v4_c05_g1.png
**Job ID:** 4cc5336f-bbc1-4e91-bc9d-84b485026ec0
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153803_4cc5336f-bbc1-4e91-bc9d-84b485026ec0.png
**SHA256:** bdb81dd198bd2c11a01b73edc8aa03c2b459a90948e7432427397dde8a693962


## C01 - Hook image - 2026-09-22

**Current hook status:** image and animation take 1 approved by Daniel; selected on the MerryGlowUSA board.
**Frame:** `starting_frames/v4_c01_g1.png`
**Job ID:** `43bb8d74-81db-493f-b07d-0930346e65e9`
**Settings:** GPT Image 2.5 (`gpt_image_2_5`), Sunburst, 2K, medium quality, 9:16, count 1; use_unlim omitted. Backend mapped image roles to image_references.
**References (submitted order):**
1. `references/v4_c01_r1.png` - geometry, camera, pose and framing; service ID `d7843aad-a3e1-4413-9f7b-7cd489a9319c`; original `THEXMASGLOW - CHRISTMAS PROJECTOR/content/video_8_assets/starting_frames/v8_c01_g5.png`; SHA-256 `e12c1ccea70d5673b340701a551cf3711e47d89075130e23792a0d6f1c3c3bc0`.
2. `references/v4_c01_r2.png` - photographic look only; service ID `94808c0a-842c-454d-aeab-104f3b6a2381`; original `THEXMASGLOW - CHRISTMAS PROJECTOR/content/video_12_assets/starting_frames/v12_c01_g1.png`; SHA-256 `8ad5a013de15fa8621fc007dca9f6bb934bdfed2228ed4d0c44907b87551564e`.

**Lineage:** Reused from TheXmasGlow v8 C01 image g5; changed room/person nouns and reference-role wording; Video 5 also changes carton and display artwork to MerryGlowUSA. Camera, framing, pose and quality instructions retained.

### Image prompt
```text
REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality candid vertical iPhone photo taken from the floor of a double-height Christmas living room, looking up and across at a woman standing on the mezzanine landing, evening. We see her from below and slightly to the side, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: the camera stands on the living-room floor MUCH closer in to the stairs than a wide establishing shot, tilted up, so the woman and the inflatable she is taping fill most of the picture and the room reads as context around them rather than as the subject. The mezzanine landing crosses the frame with its black metal railing along it, and the woman stands on that landing behind the railing DEAD CENTRE on the vertical axis of the frame, framed from roughly the waist up and very large in the picture - she is the biggest thing in the photograph and the taped inflatable is directly above and ahead of her, also near the centre, so her reaching arm and the inflatable together sit in the middle of the frame. A short stretch of the open white staircase still enters the lower right corner, and the living-room floor is still clearly visible below her in the lower part of the picture, so the drop from the landing to the floor reads plainly. She is NOT on a ladder - there is no ladder anywhere in the picture.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE HIGH WHITE CEILING above the double-height space, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. It hangs out over the open double-height void rather than over the landing. One corner has started to peel, with a long strip of tape hanging down.

HER POSE - THIS IS THE POINT OF THE PICTURE: she is leaning far out over the landing railing to reach it. Her hips are pressed against the top rail, her weight is tipped forward past it and out over the open void, her feet still on the landing behind her with her heels lifting, one hand gripping the rail and the other stretched up and out pressing a fresh strip of silver duct tape onto Santa's shoulder, a roll of duct tape in her gripping hand. She is visibly overreaching and off balance, the rail the only thing holding her, empty air and the floor below her.

THE ROOM - CHANGE ONLY THE ROOM FINISHES: a different double-height American living room, with the exact same built geometry and every furnishing in the same position and at the same scale as the FIRST photograph - pale limestone plaster walls, a wall of tall black-framed windows at the right with a dark winter garden behind them, a white open-tread staircase with slim black metal spindles, a mezzanine landing with a matching black rail and a green garland with red bows wound along it, a pale limestone fireplace with a dark walnut mantel on the ground floor, a tall green Christmas tree with warm white lights and red and gold baubles standing in the double-height space, smoked wide-plank oak floor, a muted sage linen sofa and an ivory textured rug.

A UNITED STATES FLAG: a real fabric United States flag hangs flat against the pale limestone wall in the background under the landing, clearly readable stars and stripes, hanging straight and still, about the size of a large poster. It does not cover the Christmas tree or the fireplace and it does not reach up into the empty band of ceiling at the top of the frame.

HER CLOTHES: matching American-flag Christmas pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick grey wool socks. She is early 30s with golden-blonde hair in a loose low bun, fair skin and an angular face.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling reads as clean white paint and the walls read as pale limestone plaster, the window frames and the rail read as true black, the oak floor reads as natural wood, the flag keeps true red, white and navy. The Christmas tree lights, the fireplace and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling, on the landing and on her, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the weave of her pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave a generous clean band of plain empty ceiling across the very top of the image - roughly the top fifth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Make that room by tilting the camera up slightly, NOT by pulling the camera back and NOT by shrinking the woman - she stays close and large and centred exactly as described above.

No captions, no watermarks, no lettering anywhere in the image.
```

### Exact prompt substitutions

- Original: "Extremely high quality"
  Replacement: "REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.\n\nExtremely high quality"

- Original: "THE ROOM - COPY IT FROM THE FIRST ATTACHED PHOTOGRAPH: the room in this picture is the EXACT SAME ROOM as the first attached photograph, same house, same light, same furniture in the same places - a double-height white modern American farmhouse living room - white painted walls"
  Replacement: "THE ROOM - CHANGE ONLY THE ROOM FINISHES: a different double-height American living room, with the exact same built geometry and every furnishing in the same position and at the same scale as the FIRST photograph - pale limestone plaster walls"

- Original: "white plaster fireplace"
  Replacement: "pale limestone fireplace with a dark walnut mantel"

- Original: "pale wide-plank oak floor"
  Replacement: "smoked wide-plank oak floor"

- Original: "a light linen sofa and a cream rug"
  Replacement: "a muted sage linen sofa and an ivory textured rug"

- Original: "against the white wall"
  Replacement: "against the pale limestone wall"

- Original: "mid 30s with dark brown hair in a loose low bun"
  Replacement: "early 30s with golden-blonde hair in a loose low bun, fair skin and an angular face"

- Original: "The ceiling and the walls read as clean white paint"
  Replacement: "The ceiling reads as clean white paint and the walls read as pale limestone plaster"

### Generation result and take history
- `starting_frames/v4_c01_g1.png`: completed, 1520 x 2688 PNG, 5603128 bytes; SHA-256 `2fd3f4657ae46c4da5782911383a5ab14ae8fe663ee20a00a055177a6d218d19`.
- Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_164728_43bb8d74-81db-493f-b07d-0930346e65e9.png
- Visual check: Framing closely follows the source. Changed people and room finishes; room changes are subtle. Room still strongly resembles the source; sofa and floor changes are not clearly realized.
- Review status: unreviewed by Daniel. One generation only; no automatic reroll.


### C01 animation - take 1 - 2026-09-22

**Status:** approved by Daniel; completed, saved and selected on the board. One generation; no reroll.
**Starting frame approval:** Daniel approved the C01 image in this conversation: "They camed out good".
**Frame:** `starting_frames/v4_c01_g1.png` - approved.
**Clip:** `clips/v4_c01_g1.mp4`
**Job ID:** `2811ebe2-61f5-4eac-94cd-e779c7c9587e`
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "1080p", "duration": 5, "aspect_ratio": "9:16", "generate_audio": true, "count": 1, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "43bb8d74-81db-493f-b07d-0930346e65e9"}]}
**References:** approved starting frame only, existing Higgsfield image generation `43bb8d74-81db-493f-b07d-0930346e65e9`, role start_image. No source video attached.
**Source:** THEXMASGLOW - CHRISTMAS PROJECTOR/content/video_8_assets/prompts.md; C01 video g2, confirmed selected on its board.

Reused from TheXmasGlow v8 C01 video g2 - changed: nothing. Prompt copied verbatim; approved MerryGlowUSA starting frame substituted.

#### Video prompt
```text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the living room floor below and holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the upstairs balcony, leaning her hips against the dark wooden top rail, both arms stretched up over her head, pressing strips of silver duct tape onto the white ceiling to hold up a big inflatable Santa. Below her: the two-storey living room with the lit fireplace, the American flag on the wall, the decorated Christmas tree and the white sofa.

ACTION TIMELINE:
0.0–1.0s — Up on her toes, she smooths one more strip of silver tape onto the ceiling with her palm, then gives the inflatable Santa a quick test tug to check it is holding, leaning her whole weight forward into the wooden top rail.
1.0–1.5s — The section of the dark wooden top rail she is leaning on splits with a loud crack and swings away from her, and she pitches forward over the balcony edge, eyes wide, both hands clamping onto the inflatable Santa.
1.5–2.5s — She drops down into the living room, the inflatable Santa peeling straight off the ceiling and coming with her — the silver tape strips tearing free and trailing, the green garland and a red bow sliding off the broken rail behind her.
2.5–3.4s — She misses the sofa completely and lands flat on her back on the wooden living room floor in front of it, hitting the floor and settling straight down with no bounce, and the big inflatable Santa flops down on top of her, covering her from the waist up.
3.4–5.0s — She shoves the inflatable Santa's head sideways off her face, hair everywhere, looks straight up at the camera and bursts out laughing, still flat on her back on the floor with the Santa across her lap. End frame: her laughing on the floor under the inflatable, the empty broken balcony rail above her.

AUDIO: her real voice, lip-synced, matching her appearance — a short surprised yelp as the rail gives way, then breathless laughing at the end; the sharp crack of splitting wood; duct tape ripping off the ceiling; the squeaky rubbery scuff of the big inflatable; the heavy flat thud of her body landing on the wooden floor; the fireplace crackling quietly under everything. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip. The living room stays pixel-faithful to the start frame — same fireplace, same flag, same Christmas tree, same sofa, same windows, same warm lamp light. The inflatable Santa stays the same size, colours and printed face the whole clip and never deforms into a different character. Real weight and gravity on the fall — she drops straight down, she is never thrown or launched sideways. She lands on the wooden floor, NOT on the sofa - she never touches the sofa at any point in the clip. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
```

#### Take history
One generation submitted; no automatic reroll.

**Result:** {"video": 4, "width": 1080, "height": 1920, "fps": "24/1", "duration": "5.050000", "audio": ["aac"], "bytes": 6028828, "sha256": "f7d2ea72e9a78940329c85dc259dc02aadc24cf34db6c3bc209b65b39cd80df3", "decode_exit": 0, "url": "https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_165751_2811ebe2-61f5-4eac-94cd-e779c7c9587e.mp4", "note": "Sampled frames show the woman falling to the floor and Santa landing over her. Camera tilts/reframes downward despite the framing lock."}
**Prompt verification:** service-returned prompt matches submitted and archived text exactly. Full video/audio decode exit 0.
**Review limits:** sampled frames inspected; audio presence and decoding verified, spoken lines not transcribed. Frame-by-frame review was not performed.

---

## Traceability - 2026-09-23

This file was repaired on 2026-09-23. Two defects were found; nothing else was changed.

**Missing animation records.** Every `### Video prompt` in the frame sections read "Not submitted; stills only." while all five clips, their 2K upscales and the cut in `videos_to_post/` sit on disk. The C01 section already carried its own animation record and was left untouched. The submitted prompts were recovered verbatim from the video-generation records and archived as `### Video prompt - take N` subsections, each with its job ID, the media roles read off the record, and an ffprobe verification line. No prompt text was reworded or reconstructed from a neighbouring take or from watching a clip. The `## C04 - reference take 1` section keeps its line: a reference image is never animated.

**Truncated tail.** The file also ended mid-word. That sentence was completed from the surrounding record; no new fact was introduced.

**Unresolved:** this round has no archived upscale job IDs and no archived `generate_audio` / `mode` / `declined_preset_id` values, so the `**Settings:**` lines above carry only what the generation record returned.



---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: clips byte-identical (md5) to their Higgsfield result unless the entry says otherwise, generated images by exact byte size, and every start frame checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C02: the board did not show the exact image prompt of `v4_c02_g1.png`; it now does.
- C02: the board did not show the exact clip prompt of `v4_c02_g1.mp4`; it now does.
- C03: the board did not show the exact image prompt of `v4_c03_g1.png`; it now does.
- C04: the board did not show the exact image prompt of `v4_c04_g1.png`; it now does.
- C04: the board did not show the exact image prompt of `v4_c04_r1.png`; it now does.
- C05: the board did not show the exact image prompt of `v4_c05_g1.png`; it now does.

### C01 — Taping Santa from the landing

**In the cut:** `starting_frames/v4_c01_g1.png` → `clips/v4_c01_g1.mp4`

#### Image prompt — `starting_frames/v4_c01_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `43bb8d74-81db-493f-b07d-0930346e65e9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_164728_43bb8d74-81db-493f-b07d-0930346e65e9.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_4_assets/references/v4_c01_r1.png` · Higgsfield media `d7843aad-a3e1-4413-9f7b-7cd489a9319c`
- @Image 2: `content/video_4_assets/references/v4_c01_r2.png` · Higgsfield media `94808c0a-842c-454d-aeab-104f3b6a2381`

````text
REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality candid vertical iPhone photo taken from the floor of a double-height Christmas living room, looking up and across at a woman standing on the mezzanine landing, evening. We see her from below and slightly to the side, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: the camera stands on the living-room floor MUCH closer in to the stairs than a wide establishing shot, tilted up, so the woman and the inflatable she is taping fill most of the picture and the room reads as context around them rather than as the subject. The mezzanine landing crosses the frame with its black metal railing along it, and the woman stands on that landing behind the railing DEAD CENTRE on the vertical axis of the frame, framed from roughly the waist up and very large in the picture - she is the biggest thing in the photograph and the taped inflatable is directly above and ahead of her, also near the centre, so her reaching arm and the inflatable together sit in the middle of the frame. A short stretch of the open white staircase still enters the lower right corner, and the living-room floor is still clearly visible below her in the lower part of the picture, so the drop from the landing to the floor reads plainly. She is NOT on a ladder - there is no ladder anywhere in the picture.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE HIGH WHITE CEILING above the double-height space, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. It hangs out over the open double-height void rather than over the landing. One corner has started to peel, with a long strip of tape hanging down.

HER POSE - THIS IS THE POINT OF THE PICTURE: she is leaning far out over the landing railing to reach it. Her hips are pressed against the top rail, her weight is tipped forward past it and out over the open void, her feet still on the landing behind her with her heels lifting, one hand gripping the rail and the other stretched up and out pressing a fresh strip of silver duct tape onto Santa's shoulder, a roll of duct tape in her gripping hand. She is visibly overreaching and off balance, the rail the only thing holding her, empty air and the floor below her.

THE ROOM - CHANGE ONLY THE ROOM FINISHES: a different double-height American living room, with the exact same built geometry and every furnishing in the same position and at the same scale as the FIRST photograph - pale limestone plaster walls, a wall of tall black-framed windows at the right with a dark winter garden behind them, a white open-tread staircase with slim black metal spindles, a mezzanine landing with a matching black rail and a green garland with red bows wound along it, a pale limestone fireplace with a dark walnut mantel on the ground floor, a tall green Christmas tree with warm white lights and red and gold baubles standing in the double-height space, smoked wide-plank oak floor, a muted sage linen sofa and an ivory textured rug.

A UNITED STATES FLAG: a real fabric United States flag hangs flat against the pale limestone wall in the background under the landing, clearly readable stars and stripes, hanging straight and still, about the size of a large poster. It does not cover the Christmas tree or the fireplace and it does not reach up into the empty band of ceiling at the top of the frame.

HER CLOTHES: matching American-flag Christmas pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick grey wool socks. She is early 30s with golden-blonde hair in a loose low bun, fair skin and an angular face.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling reads as clean white paint and the walls read as pale limestone plaster, the window frames and the rail read as true black, the oak floor reads as natural wood, the flag keeps true red, white and navy. The Christmas tree lights, the fireplace and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling, on the landing and on her, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the weave of her pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave a generous clean band of plain empty ceiling across the very top of the image - roughly the top fifth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Make that room by tilting the camera up slightly, NOT by pulling the camera back and NOT by shrinking the woman - she stays close and large and centred exactly as described above.

No captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v4_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on
**Job** - `2811ebe2-61f5-4eac-94cd-e779c7c9587e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_165751_2811ebe2-61f5-4eac-94cd-e779c7c9587e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c01_g1.png` · Higgsfield media `43bb8d74-81db-493f-b07d-0930346e65e9`

````text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the living room floor below and holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the upstairs balcony, leaning her hips against the dark wooden top rail, both arms stretched up over her head, pressing strips of silver duct tape onto the white ceiling to hold up a big inflatable Santa. Below her: the two-storey living room with the lit fireplace, the American flag on the wall, the decorated Christmas tree and the white sofa.

ACTION TIMELINE:
0.0–1.0s — Up on her toes, she smooths one more strip of silver tape onto the ceiling with her palm, then gives the inflatable Santa a quick test tug to check it is holding, leaning her whole weight forward into the wooden top rail.
1.0–1.5s — The section of the dark wooden top rail she is leaning on splits with a loud crack and swings away from her, and she pitches forward over the balcony edge, eyes wide, both hands clamping onto the inflatable Santa.
1.5–2.5s — She drops down into the living room, the inflatable Santa peeling straight off the ceiling and coming with her — the silver tape strips tearing free and trailing, the green garland and a red bow sliding off the broken rail behind her.
2.5–3.4s — She misses the sofa completely and lands flat on her back on the wooden living room floor in front of it, hitting the floor and settling straight down with no bounce, and the big inflatable Santa flops down on top of her, covering her from the waist up.
3.4–5.0s — She shoves the inflatable Santa's head sideways off her face, hair everywhere, looks straight up at the camera and bursts out laughing, still flat on her back on the floor with the Santa across her lap. End frame: her laughing on the floor under the inflatable, the empty broken balcony rail above her.

AUDIO: her real voice, lip-synced, matching her appearance — a short surprised yelp as the rail gives way, then breathless laughing at the end; the sharp crack of splitting wood; duct tape ripping off the ceiling; the squeaky rubbery scuff of the big inflatable; the heavy flat thud of her body landing on the wooden floor; the fireplace crackling quietly under everything. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip. The living room stays pixel-faithful to the start frame — same fireplace, same flag, same Christmas tree, same sofa, same windows, same warm lamp light. The inflatable Santa stays the same size, colours and printed face the whole clip and never deforms into a different character. Real weight and gravity on the fall — she drops straight down, she is never thrown or launched sideways. She lands on the wooden floor, NOT on the sofa - she never touches the sofa at any point in the clip. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
````

**Other takes of C01 on disk (2)**

#### Image prompt — `references/v4_c01_r1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `d7843aad-a3e1-4413-9f7b-7cd489a9319c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_153036_d7843aad-a3e1-4413-9f7b-7cd489a9319c.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `c0110458-d06a-4210-a022-dd03bc325b7c`
- @Image 2: uploaded file, not on the drive · Higgsfield media `08325837-ce85-4fa4-b6b4-d7c8e0281ba1`

````text
Extremely high quality candid vertical iPhone photo taken from the floor of a double-height Christmas living room, looking up and across at a woman standing on the mezzanine landing, evening. We see her from below and slightly to the side, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: the camera stands on the living-room floor MUCH closer in to the stairs than a wide establishing shot, tilted up, so the woman and the inflatable she is taping fill most of the picture and the room reads as context around them rather than as the subject. The mezzanine landing crosses the frame with its black metal railing along it, and the woman stands on that landing behind the railing DEAD CENTRE on the vertical axis of the frame, framed from roughly the waist up and very large in the picture - she is the biggest thing in the photograph and the taped inflatable is directly above and ahead of her, also near the centre, so her reaching arm and the inflatable together sit in the middle of the frame. A short stretch of the open white staircase still enters the lower right corner, and the living-room floor is still clearly visible below her in the lower part of the picture, so the drop from the landing to the floor reads plainly. She is NOT on a ladder - there is no ladder anywhere in the picture.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE HIGH WHITE CEILING above the double-height space, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. It hangs out over the open double-height void rather than over the landing. One corner has started to peel, with a long strip of tape hanging down.

HER POSE - THIS IS THE POINT OF THE PICTURE: she is leaning far out over the landing railing to reach it. Her hips are pressed against the top rail, her weight is tipped forward past it and out over the open void, her feet still on the landing behind her with her heels lifting, one hand gripping the rail and the other stretched up and out pressing a fresh strip of silver duct tape onto Santa's shoulder, a roll of duct tape in her gripping hand. She is visibly overreaching and off balance, the rail the only thing holding her, empty air and the floor below her.

THE ROOM - COPY IT FROM THE FIRST ATTACHED PHOTOGRAPH: the room in this picture is the EXACT SAME ROOM as the first attached photograph, same house, same light, same furniture in the same places - a double-height white modern American farmhouse living room - white painted walls, a wall of tall black-framed windows at the right with a dark winter garden behind them, a white open-tread staircase with slim black metal spindles, a mezzanine landing with a matching black rail and a green garland with red bows wound along it, a white plaster fireplace on the ground floor, a tall green Christmas tree with warm white lights and red and gold baubles standing in the double-height space, pale wide-plank oak floor, a light linen sofa and a cream rug.

A UNITED STATES FLAG: a real fabric United States flag hangs flat against the white wall in the background under the landing, clearly readable stars and stripes, hanging straight and still, about the size of a large poster. It does not cover the Christmas tree or the fireplace and it does not reach up into the empty band of ceiling at the top of the frame.

HER CLOTHES: matching American-flag Christmas pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick grey wool socks. She is mid 30s with dark brown hair in a loose low bun.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and the walls read as clean white paint, the window frames and the rail read as true black, the oak floor reads as natural wood, the flag keeps true red, white and navy. The Christmas tree lights, the fireplace and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling, on the landing and on her, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the weave of her pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave a generous clean band of plain empty ceiling across the very top of the image - roughly the top fifth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Make that room by tilting the camera up slightly, NOT by pulling the camera back and NOT by shrinking the woman - she stays close and large and centred exactly as described above.

No captions, no watermarks, no lettering anywhere in the image.
````

#### Image prompt — `references/v4_c01_r2.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `94808c0a-842c-454d-aeab-104f3b6a2381`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260921_152601_94808c0a-842c-454d-aeab-104f3b6a2381.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `443746c4-8eeb-4ff2-a4da-e02a14293714`
- @Image 2: uploaded file, not on the drive · Higgsfield media `449ed0de-a806-4966-b15f-53bac6662a33`

````text
REFERENCE ROLES: the FIRST attached image owns the geometry, camera position, framing, pose and prop placement. The SECOND attached image is only a photographic-look reference for clear natural iPhone detail, realistic materials and colour; do not copy its people, room or composition. The new people and room are specified below. Preserve the FIRST image's composition.

Extremely high quality candid vertical iPhone photo taken from a hallway looking into a family's living room on a winter evening: a young mother kneels on the bare floor with a huge tangled knot of old multicoloured Christmas string lights in front of her, her arm stretched out to push the plug into a wall socket, while her two small children stand behind her watching the Christmas tree.

Use the attached reference photograph for BOTH the staging AND the camera position - the mother kneeling in the near foreground, the knot of lights on the floor beside her, her arm reaching out to the low wall socket, the two small children standing behind her, the tall Christmas tree on the right and the plain white wall corner the camera is looking past. COPY ITS CAMERA POSITION AND ITS COMPOSITION EXACTLY. Copy nothing else from it: the room, the mother and the children are all described below and are all different people in a different house.

FRAMING AND ANGLE - COPY THE CAMERA FROM THE REFERENCE: the camera is handheld at about the chest height of a standing adult, tilted very slightly down, standing in the next room and looking in through a doorway, so a plain white wall corner with a white skirting board runs floor to ceiling down the RIGHT EDGE of the frame and takes up roughly the right eighth of the picture - we are looking past it into the living room. The living room floor fills the bottom half of the frame and runs away into depth. The mother kneels in the lower LEFT of the frame, seen from behind at three quarters, close to the camera and large in the picture: her head and shoulders sit around the middle of the frame and the bottom edge of the picture cuts her just below the knees. The knot of lights lies on the bare floor immediately to her right, between her and that white wall corner, around the centre of the lower third of the picture. The Christmas tree stands on the RIGHT of the frame just inside the white corner, tall enough that the top edge of the picture cuts off its top. The two children stand on the floor in the middle distance between the mother and the tree, small in the frame, their heads in the middle third of the picture. Nobody is looking at the camera and nobody is posing. This is NOT a side angle, NOT a low floor-level angle and NOT a symmetrical composition.

THE KNOT AND THE PLUG: on the bare floorboards immediately to the mother's right lies a big ugly knot of old-fashioned Christmas string lights - dark green flex wound and knotted into a messy nest about the width of two floorboards across, studded with fat vintage multicoloured bulbs in red, green, blue and yellow, with a white in-line plug body and loops of slack wire lifting out of the top of it. She holds the end of that flex in her outstretched right hand and the two-pin plug is an inch from a white electrical socket set low on the white wall corner at the right of the frame. It is not plugged in yet and every bulb in the knot is dark.

THE CONNECTION - THIS IS THE IMPORTANT PART: one single continuous run of that SAME dark green flex with the SAME fat multicoloured bulbs leaves the far side of the knot, travels away across the floorboards to the right, passes behind the children, reaches the foot of the Christmas tree and climbs up into its lower branches, where it is plainly the very same string that is wound round and round the whole tree above. Same wire colour, same bulb size, same bulb spacing, one unbroken line. The eye must be able to follow the wire from the plug in her hand, through the knot on the floor, across the floor and up onto the tree without a single break or gap. The heap on the floor is NOT a separate loose pile with nothing leading out of it, and the tree is NOT wired to anything else.

THE TREE IS NOT SWITCHED ON: because the plug is still in her hand, every bulb on the tree is dark and unlit. The tree is not glowing, no light comes off it, and it throws no coloured light onto the floor, the walls or the children. It is still fully decorated and still reads as a beautiful Christmas tree - the baubles catch the warm lamplight in the room - it is simply not lit yet.

THE ROOM: a cosy American traditional living room. Walls of pale blue-grey painted plaster with white skirting, wide honey-oak floorboards running away from the camera, a rust-red velvet sofa along the left wall with a cream wool blanket folded over its back, a cream and blue Persian rug on the floor in front of it, a walnut side table behind the sofa carrying a brass table lamp with a white linen shade that is switched on and glowing, and a white-painted window with white muntins on the back wall showing a dark blue winter evening and snow on the sill outside.

THE TREE: a big real fir, dense and dark green, dressed with silver, white and pale blue glass baubles, cream knitted snowflakes, a wide cream linen ribbon wound down it and a silver star on top, with a heavy cream cable-knit tree skirt gathered round its base and four presents wrapped in white paper and green ribbon sitting on it.

THE MOTHER: about 34, shoulder-length curly dark-brown hair, warm olive skin and an oval face, an oversized forest-green chunky cable-knit sweater with the sleeves pushed up her forearms, charcoal grey joggers and thick oatmeal socks, no shoes. She kneels sitting back on her heels, her left hand flat on the floorboards taking her weight, her right arm stretched right out towards the socket with the plug pinched between her thumb and fingers, her head turned in profile watching the plug. She is concentrating, slightly fed up, not smiling.

THE CHILDREN: a boy of about seven standing on the rug behind his mother, short curly auburn hair and a freckled face, red-and-white striped pyjamas, barefoot, his mouth wide open in a huge exaggerated gasp of amazement and both hands up near his cheeks, staring at the tree. Beside him a girl of about four with dark-brown hair in two short pigtails and warm olive skin, a cream flannel nightgown printed with tiny red hearts, crouched down on one knee with her right arm flung out pointing straight at the tree. Neither child blocks the mother, the knot of lights or the tree.

COLOUR: warm domestic evening white balance, the way an iPhone renders a lamp-lit living room - warm but not orange. The picture is NOT sepia, NOT amber-washed and NOT heavily graded. Skin reads natural, the white wall corner reads clean white, the floorboards read as real wood and the sweater reads as true forest green.

LIGHTING AND QUALITY: the room is lit by the warm table lamp plus soft ambient light - cosy and warm, but still bright enough that every face, every twist of wire in the knot and the whole tree are clearly readable, with no dark corners where detail disappears and no blown highlights. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot somebody took of their family, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere from the mother in the foreground to the tree behind her, crisp detail in every individual bulb and every twist of flex in the tangle, realistic skin, hair and knitwear texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

FRAMING: leave the upper LEFT of the image - roughly the top eighth of the frame on the wall side - as plain uncluttered wall, free of pictures, shelves, garland, hanging decorations and lettering, so a caption can sit there. Do not pull the camera back or shrink the mother to make that room.

No captions, no watermarks, no added lettering anywhere in the image, no writing on any clothing, no user-interface elements, no mute or speaker icons and no social-media overlays.
````

### C02 — Hands on the MerryGlowUSA box

**In the cut:** `starting_frames/v4_c02_g1.png` → `clips/v4_c02_g1.mp4`

#### Image prompt — `starting_frames/v4_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `6dddb32c-15b8-4f79-a196-ccbc3442cfea`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151947_6dddb32c-15b8-4f79-a196-ccbc3442cfea.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_2_assets/starting_frames/v2_c02_g1.png` · Higgsfield media `ce82f8a0-2382-4681-892e-d3490b97f74e`
- @Image 2: `product_images/box_heritage_green_g1.png` · Higgsfield media `4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Replace the FIRST reference's carton with OUR UBU product box exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton with forest green body, a blank dark-red band across the top bordered in gold, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold-and-red star-and-tree burst over a printed render of a white cylindrical projector in a white U-shaped pivoting bracket on a round flat white base, a black circular slatted front grille with a central glass lens, a slim black remote printed beside it, gold village skyline along the bottom, and the bottom labels REMOTE CONTROL, 45 MIN, 90 MIN, no transparent window. Preserve the tilted projector ILLUSTRATION printed on the box exactly; it is artwork only. The physical projector is concealed in the closed carton in this starting frame. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only the product carton, the table and the background; keep the hands and pose.

FIRST - THE HANDS. A woman's hands, about 35, with light warm-beige skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep forest-green knitted wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a spacious festive American dining room with warm cream walls, dark-oak built-in shelves, an arched antique-brass mirror, a white brick fireplace with ivory stockings and a tall Christmas tree with red glass ornaments, gold bells and warm-white lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The red band must remain BLANK, exactly as on the SECOND attached reference. No THEXMASGLOW wordmark, no invented UBU wordmark, no brand name added anywhere on the carton. Preserve the exact headline and bottom labels from the SECOND reference, sharp and legible.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, box placement, hand positions and camera. @Image 2 owns the UBU carton geometry and product identity. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v4_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `9d57b955-e8c2-464a-9899-916b0380c2f0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192252_9d57b955-e8c2-464a-9899-916b0380c2f0.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c02_g1.png` · Higgsfield media `6dddb32c-15b8-4f79-a196-ccbc3442cfea`
- image ref 1: `content/video_4_assets/starting_frames/v4_c03_g1.png` · Higgsfield media `a377849d-5074-4036-bb06-c73ae580a73a`

````text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing UBU carton. Keep the blank dark-red top band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and black remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls frame 0.0s, the exact printed box, hands, table, room, props and light. @Image 1 is the approved C03 image and supplies ONLY the actual upright projector design and orientation, not its kitchen or hands. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a blank dark red band across the top, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white cylindrical projector in a white U-shaped bracket on a round base, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: the exact larger matte-white upright CYLINDER shown in @Image 1, retaining its full physical size and proportions, in its white U-shaped bracket on a flat round white base. The cylinder axis is VERTICAL, lens facing straight UP at the ceiling. Its flat circular black slatted top face surrounds a central blue lens. The top face is BLACK and stays black for every frame. The cylinder is locked upright relative to its bracket throughout the lift; never inclined on the mount, never copied from the angled illustration on the carton. Round base horizontal. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a deep forest-green knitted wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, the supplied festive dining room with warm cream walls, dark-oak built-in shelves, an arched antique-brass mirror, a white brick fireplace with ivory stockings and a tall Christmas tree with warm-white lights, red glass ornaments and gold bells. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK slatted circular top face and central blue lens visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the warm honey-oak dining table with fine straight wood grain, a satin-matte surface and a square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

### C03 — Larger upright projector

**In the cut:** `starting_frames/v4_c03_g1.png` → `clips/v4_c03_g1.mp4`

#### Image prompt — `starting_frames/v4_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a377849d-5074-4036-bb06-c73ae580a73a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153816_a377849d-5074-4036-bb06-c73ae580a73a.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `0b51a9d5-141b-4052-a50b-62619fc01123`
- @Image 2: `content/video_4_assets/starting_frames/v4_c02_g1.png` · Higgsfield media `6dddb32c-15b8-4f79-a196-ccbc3442cfea`

````text
Create the next UBU C3 photograph using @Image 1 for the upright product design, kitchen composition and camera, and @Image 2 for the real product SCALE relative to its carton and adult hands, the skin and sweater. Make the physical projector appreciably BIGGER than @Image 1 so it matches the product that fits inside the carton in @Image 2. Use the new kitchen and materials below. Keep the cylinder perfectly upright, lens pointing straight UP.

KEEP THE COMPOSITION FROM @Image 1: the camera position, camera height, lens, distance, vertical 9:16 crop, the general two-handed supporting pose, central product placement and forearm entry points. Enlarge the complete projector about 40 percent relative to the adult hands and picture; adapt finger contacts naturally to the larger device, keeping anatomy and hand size realistic.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with light warm-beige skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a deep forest-green knitted wool sweater sleeve pushed back; right forearm enters from the right in the same deep forest-green knitted wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the complete upright projector, from the top black lens panel to the bottom round base, occupies about 42 percent of the full image height. Base diameter occupies about 30 percent of image width. A substantial real device held in two adult hands, not a miniature. Its actual overall height is about 80-85 percent of the tall carton in @Image 2, allowing realistic packaging clearance. Enlarge all product components together, preserve their original proportions and ordinary adult hand dimensions. Keep visible air beneath the base and counter. Both hands support the device firmly and naturally.

THE PRODUCT - the same UBU matte-white cylindrical projector barrel in its white U-shaped pivot bracket on a round flat white base. USER-CONFIRMED ORIENTATION: THE CYLINDER STANDS VERTICALLY UPRIGHT, WITH THE BLACK LENS/GRILLE FACE ON TOP POINTING STRAIGHT UP AT THE CEILING. Retain @Image 1's already confirmed upright lens-UP orientation without any tilt. Its long axis is vertical and PERPENDICULAR to the horizontal circular base, like an upright can standing on end. The circular black slatted lens face is a HORIZONTAL TOP FACE, parallel to the round base, visible from above as an ellipse at this existing camera height; the central blue glass lens looks upward. The solid white barrel extends straight down below that top face, sitting vertically between the two upright support arms. The round base remains flat and horizontal, and the support arms remain vertical. The projector does NOT point at the camera, does NOT lie sideways, and does NOT lean diagonally. No forward-facing black front disc: the black disc is now on TOP. Preserve the exact existing cylinder shell, horizontal ventilation slats across the black lens panel, blue glass lens, side pivot, U bracket and circular base; do not replace it with the older dome projector or four-legged stand. @Image 2 supplies product materials and component identity only; IGNORE its printed tilted pose. The device has the same design and upright configuration as @Image 1.

THE COUNTER - a pale ivory quartz counter with fine warm-grey veins, a straight eased edge and matte surface. Same shape, position and amount visible as @Image 1.

THE KITCHEN - a sharply resolved traditional Christmas kitchen: warm mushroom shaker cabinets with aged bronze pulls, ivory handmade square tiles, honey-oak open shelves, a white enamel range, burgundy velvet ribbons, warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree in the far corner. Balanced soft window fill and warm interior light, realistic iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns camera, layout and upright product geometry only, not its undersized scale. @Image 2 owns the adult hand appearance, sweater, material realism and physical carton-to-projector scale. Its printed tilted product illustration must NEVER set the real projector orientation. The physical unit is larger, perfectly vertical, lens UP. All parts in natural crisp iPhone deep focus, no portrait mode, bokeh or blur.
````

#### Video prompt — `clips/v4_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `b81ca219-faa7-4983-9d80-fbef2ba6dabf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192252_b81ca219-faa7-4983-9d80-fbef2ba6dabf.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c03_g1.png` · Higgsfield media `a377849d-5074-4036-bb06-c73ae580a73a`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale ivory quartz counter with fine warm-grey veins and a straight eased edge, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - the exact matte-white upright CYLINDER in the start image, in its white U-shaped bracket on a flat round white base. Cylinder axis VERTICAL, lens pointing straight UP at the ceiling. Its black slatted circular top face surrounds the central blue lens. The top face is BLACK and stays black for every frame. The cylinder stays locked upright within the bracket throughout; no inclination on its mount. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in deep forest-green knitted wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a pale ivory quartz counter with fine warm-grey veins and a straight eased edge; behind it warm mushroom shaker cabinets with aged bronze pulls, ivory handmade square tiles, honey-oak shelves, a white enamel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the pale ivory quartz counter with fine warm-grey veins and a straight eased edge, matte rather than mirror-polished.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the round base and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the cylinder, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the base approaches the stone.
3.0-3.4s - the flat round base of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has; those tiny movements affect the WHOLE rigid product, never a rotation of the cylinder inside the bracket. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the cylinder.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

### C04 — Remote click → Christmas reveal

**In the cut:** `starting_frames/v4_c04_g1.png`, `references/v4_c04_r1.png` → `clips/v4_c04_g1.mp4`

#### Image prompt — `starting_frames/v4_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `7ec309eb-af70-4367-b50c-4850ec4e3479`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153808_7ec309eb-af70-4367-b50c-4850ec4e3479.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_4_assets/references/v4_c04_r1.png` · Higgsfield media `81006fa3-03cd-43e5-8db4-bc59b8c62bb0`
- @Image 2: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `11720edc-b38f-48f6-bc92-8278407f2181`

````text
Create the LIGHTS-ON STARTING FRAME by editing @Image 1, the existing matching lights-off bedroom reference. Keep the photographer in the EXACT SAME physical place, at the same eye height, with the same lens and standing location as @Image 1, but ROTATE THE PHONE TO THE RIGHT by roughly 30 degrees. The viewing direction and framing MUST change; the camera's physical location must not. @Image 1 owns all geometry. @Image 2 is the previous lights-on image and supplies ONLY the brightness, realistic photographic look and red-sleeved hand holding the black UBU remote; it must NOT control camera position or framing. Changes are only: turn the phone's view RIGHT from that stationary location, turn room lights on, turn the wall projection completely off, and add the remote hand.

KEEP THE ROOM FROM @Image 1: warm cream plaster walls and ceiling, medium honey-oak floor, burgundy wool rug, king-size dark-oak bed with a crisp ivory cotton quilt and burgundy-and-cream tartan runner, two cream cable-knit cushions and one central forest-green cushion, ivory pillows, dark-oak nightstands and aged-brass lamps, oatmeal linen curtains behind the headboard on the BACK wall, real fir garland with warm pin lights and deep-red bows around the headboard, tall Christmas tree in the back-right corner, forest-green upholstered bench at the foot of the bed with an ivory woven throw over its right side. Same spatial layout and distances. The LEFT wall is an uninterrupted plain warm-ivory wall with no actual windows. It remains the same solid flat wall.

CAMERA LOCATION VERSUS VIEW DIRECTION - CRITICAL CORRECTION: the photographer's feet and the camera lens centre stay exactly at @Image 1's viewing point, to the right of the foot of the bed, at the same height. From there, turn the phone RIGHT about 30 degrees, with no sideways movement, no walking and no zoom. The starting image looks more toward the bed and its headboard/back curtains; the bed and upholstered foot-bench become the central subjects. The left projection wall recedes diagonally along only the LEFT 20-30 percent of the starting image, not across the middle. The back-left room corner shifts clearly LEFTWARD in the picture compared with @Image 1. Show more of the back wall, headboard and right-hand part of the bedroom. The perspective still comes from the same off-centre spot right of the bed's foot, never the central doorway view. Do not preserve @Image 1's exact crop or orientation: that was the previous mistake. Do not move any furniture or mirror the room. This frame is the START BEFORE a future LEFTWARD PAN: the camera will later rotate left from this fixed spot to arrive at @Image 1's reveal framing. Capture the right-facing starting orientation now.

LIGHTS ARE NOW ON: the ceiling-fan light and both bedside lamps illuminate the same room with clean warm light. Keep the fairy lights on the headboard and tree. Match the well-exposed natural warm interior-photo look of @Image 2, while preserving @Image 1's room geometry and applying the new right-facing camera orientation. Fine duvet, rug and wood details stay crisp; do not make the room dark.

THE LEFT WALL BEFORE ACTIVATION: completely REMOVE the entire projected Christmas scene AND every projected arch, window frame, mullion, sill, frost edge and glow from @Image 1. The same wall is now one continuous blank smooth warm-ivory wall, with its real baseboard and ceiling junction in their original positions. No actual window exists on this left wall. No remnants, embossed arches, ghost outlines, rectangular screen, poster or scenery. The real white curtains on the BACK wall remain.

REMOTE HAND: add the same adult right hand and red pajama sleeve visible in @Image 2, entering naturally from the lower right and holding the exact same slim black UBU remote at a comfortable arm's length. The thumb is poised over the central OK/play control before pressing; correct five-finger anatomy, black direction pad, red power button, matching remote scale. Keep the hand low in the right foreground, leaving the blank left wall and its corner unobstructed. It must read as the POV of the person standing at @Image 1's fixed location, not a second person or floating hand. No product box.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
````

#### Image prompt — `references/v4_c04_r1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `81006fa3-03cd-43e5-8db4-bc59b8c62bb0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151954_81006fa3-03cd-43e5-8db4-bc59b8c62bb0.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_2_assets/references/v2_c04_r1.png` · Higgsfield media `38a01390-440a-4f96-8feb-1274528f605b`
- @Image 2: `content/video_2_assets/starting_frames/v2_c05_g1.png` · Higgsfield media `c65fa6e9-597c-4be1-a4c4-0348d73c6d2b`

````text
Create one vertical 9:16 LIGHTS-OFF REFERENCE FRAME for a new UBU Christmas projector video. @Image 1 owns the exact room layout, camera position, viewing direction and furniture arrangement; change only the room materials/decor listed below and improve the projected view. @Image 2 supplies the Christmas-window theme only, never its blur, painterly scenery or protruding window geometry. Create a real handheld iPhone photograph of a real bedroom with a luminous flat wall projection.

KEEP THE ROOM LAYOUT FROM @Image 1 but use these new materials: warm cream plaster walls and ceiling, medium honey-oak floor, burgundy wool rug, king-size dark-oak bed with a crisp ivory cotton quilt and burgundy-and-cream tartan runner, two cream cable-knit cushions and one central forest-green cushion, ivory pillows, dark-oak nightstands and aged-brass lamps, oatmeal linen curtains behind the headboard on the BACK wall, real fir garland with warm pin lights and deep-red bows around the headboard, tall Christmas tree in the back-right corner, forest-green upholstered bench at the foot of the bed with an ivory woven throw over its right side. Same spatial layout and distances. The LEFT wall remains a solid flat wall with no actual windows.

CAMERA LOCATION: preserve @Image 1's existing viewpoint, standing to the right of the foot of the bed and looking diagonally LEFT toward the long wall. The enormous projected window view fills the left and central 70 percent of the picture; the familiar bed, runner and a sliver of the garland-wrapped headboard appear along the lower-right and right edge. Correct consistent perspective, no mirrored layout, no moving walls, no relocated bed. This will be the reveal orientation; the matching lights-on frame will be made by rotating the phone RIGHT from this same physical standing point. No people or hands visible.

LIGHTS ARE NOW OFF: the ceiling-fan light and both bedside lamps are off, warm bulbs not glowing. Keep only tiny Christmas garland/tree pin lights and the spectacular wall projection as illumination. Expose expertly for the projection while keeping real bedding folds and room silhouettes readable; beautifully subtle icy blue and golden light spill on the near cream duvet and pale floor.

THE PAYOFF ON THE LEFT WALL: one huge brilliant, high-contrast projection of an elegant grand arched window with warm timber mullions. Frame and scenery are projected onto the SAME FLAT WALL, with no structural opening. Through the panes is ONE continuous photographic landscape: a magnificent REALISTIC Austrian lakeside Christmas town beneath immense snowy Alps: a few beautifully resolved pastel village houses and timber chalets with thick fresh snow on roofs, glowing amber windows and clearly visible smoking chimneys, a graceful narrow church spire beside the lake, a grand decorated Christmas spruce and golden lanterns in the waterfront square, a charming illuminated Christmas market, and an old stone footbridge crossing a small stream into the dark-blue lake. The still water mirrors the warm village lights and natural emerald-and-rose aurora. Snow-laden fir branches frame the view beyond the window. Santa's small sleigh and a clear team of reindeer cross the upper sky. Fine individual snowflakes, luminous gold lights, forest green and deep cobalt snow. Vast mountain scale and photographic depth with a few legible hero buildings rather than countless tiny smeared buildings. Every pane shows its proper part of the same continuous landscape, with no repeated panels. Opaque-looking, crisp dark mullions form an uninterrupted foreground layer all the way down to the projected sill. Scenery and snowy branches remain BEHIND every mullion, never overlapping or interrupting its base.

PROJECTION PHYSICS: substantially stronger, richer and less transparent than @Image 1. Dense luminous color and decisive contrast cover the wall, no ghostly double exposure and no pale wall color washing through the scenic image. Deep dark window-frame shapes, brilliant controlled highlights without bloom, clear photographic details. The room is dark enough for a vivid high-output projection. Wall texture is only a barely perceptible surface grain, not visible through the buildings. All projected geometry is FLAT on the wall, follows one coherent perspective, and stays bounded by the real ceiling junction and baseboard. Physically believable blue and gold light spill on actual bedding; natural room shadows, no beam haze. Vivid projection while retaining real-room photographic credibility.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
````

#### Video prompt — `clips/v4_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `da16f526-c050-4ac9-a1ec-ffec26e37c3c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192252_da16f526-c050-4ac9-a1ec-ffec26e37c3c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c04_g1.png` · Higgsfield media `7ec309eb-af70-4367-b50c-4850ec4e3479`
- image ref 1: `content/video_4_assets/references/v4_c04_r1.png` · Higgsfield media `81006fa3-03cd-43e5-8db4-bc59b8c62bb0`
- video ref 1: `content/video_1_assets/clips/v1_c04_g1.mp4` · Higgsfield media `b3902899-d75c-4875-ae1e-3c0e4fbec222`

````text
One continuous 5-second POV handheld iPhone video. The attached start image is the EXACT first frame and owns the bedroom geometry, bed, bench, rug, red sleeve, hand and black remote. @Image 1 supplies the Christmas projection artwork for the LEFT wall. Its bedroom perspective is not an endpoint to morph into. Keep the physical room of the starting frame throughout. @Video 1 is the approved Video 1 C04 clip, used as a MOTION reference only: closely copy its quick thumb press, natural lowering of the remote hand and subsequent leftward handheld camera pan. Do not copy its different bedroom, lower image quality, text overlays or sound.

0.0-0.2s: from the supplied remote position the wrist makes a small natural forward/up adjustment and the thumb visibly depresses the play/OK button ONCE. Match the reference's immediate decisive press, not a long aiming gesture.
At exactly the button depression, around 0.2s: the ceiling light and bedside lamps switch OFF instantly, and the luminous Christmas-window projection switches ON on the LEFT wall in the SAME moment. No delayed reveal and no gradual fade. Existing Christmas fairy lights remain dimly lit.
0.2-1.6s: the hand relaxes and naturally lowers the still-gripped remote down toward the lower right and out of view, following @Video 1's hand movement. No waving, no tossing the remote, no second press. Simultaneously begin a gentle continuous pan LEFT at normal handheld-phone pace.
1.6-4.2s: continue rotating the phone LEFT from the same standing spot until the left wall projection dominates the view, showing @Image 1's artwork from the actual camera's viewpoint. The bed shifts toward the right edge as a result of this rotation. No walking forward, no sideways camera translation, no zoom and no cut. Natural tiny hand tremor, coherent room perspective.
4.2-5.0s: settle into the spectacular left-wall view with slight natural handheld drift.

ROOM RIGIDITY: Keep the starting room a single solid three-dimensional space. Its flat left wall, straight ceiling junction, rear curtain wall and floor remain rigidly connected at fixed angles. The camera turns within that room; walls never rotate, bend, expand, slide or change shape. The bench, bed, rug and ceiling fan keep their original dimensions and positions. Preserve the burgundy-and-cream tartan bed runner and burgundy rug from the starting image; do not borrow the red runner or green rug from @Video 1. The sole tall Christmas tree remains to the RIGHT of the bed. The projection is flat light on the existing left wall, not an opening or new room. The window artwork obeys that wall's perspective and remains fixed on it. Use @Image 1 for artwork content only, never its room outline or furniture placement.

The wall projection must be a visibly ANIMATED Christmas scene, never a frozen still. Preserve @Image 1's window framing and continuous snowy Austrian lakeside Christmas town, illuminated houses, trees, lake, mountains, aurora and sleigh. From the instant the projection appears through the final frame, soft smoke continuously curls upward and drifts from multiple house chimneys, Santa's sleigh and pulling reindeer visibly travel across the sky with gently cycling reindeer legs, and luminous aurora curtains continuously ripple and flow. Fine snow falls within the projected scene; lake reflections shimmer gently. All this motion occurs INSIDE the projection. The projected window frame remains fixed to the real wall. The entire projection does not slide, breathe, scale or float. Preserve the actual bedroom walls, bedding and furniture as solid stationary physical objects. Projection light naturally spills across the room and duvet after the click.

Sharp realistic iPhone footage, clean low-light exposure and detailed moving scenery. Exactly one visible hand holding one remote, natural thumb anatomy. No new person, no real window opening in the wall, no overlay text, no watermarks, no scene transition, no reversed pan, no music. Only quiet bedroom ambience, subtle sleeve movement and the single dry remote click. Ignore all audio in @Video 1. (no BGM). No subtitles.
````

### C05 — Christmas view from bed

**In the cut:** `starting_frames/v4_c05_g1.png` → `clips/v4_c05_g1.mp4`

#### Image prompt — `starting_frames/v4_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `4cc5336f-bbc1-4e91-bc9d-84b485026ec0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153803_4cc5336f-bbc1-4e91-bc9d-84b485026ec0.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_2_assets/starting_frames/v2_c05_g1.png` · Higgsfield media `c65fa6e9-597c-4be1-a4c4-0348d73c6d2b`
- @Image 2: `content/video_4_assets/references/v4_c04_r1.png` · Higgsfield media `81006fa3-03cd-43e5-8db4-bc59b8c62bb0`

````text
Create a new hyperrealistic low-light iPhone photograph for UBU C5. @Image 1 supplies ONLY the low bed-level camera position, wide full-wall composition and continuous foreground window-frame layout. Do NOT copy its blurry rendering, painterly scenery, stone texture or fake CGI surfaces. @Image 2 supplies the new photographic Christmas landscape and rich opaque-looking projection. Render the entire image afresh in crisp native detail. Real bedroom materials: ivory cotton duvet with visible fine woven texture and burgundy blanket edge, a simple low dark-oak cabinet, a modest real potted fir, warm cream wall and honey-oak floor. Preserve the believable low lying-in-bed perspective from @Image 1. Use elegant warm timber Gothic projected arches with slender mullions. ALL window arches, vertical posts and bottom sill form one continuous opaque foreground layer over the scenery. Every post runs uninterrupted from the arch to a clear connection with the sill. Snow, trees, roofs and lights are behind the frame and can NEVER overlap, erase or interrupt a post at its bottom. The entire frame and scenery are FLAT projected light on the solid wall, never actual structural windows or protruding architecture.

POV lying comfortably in bed, camera at pillow height, no visible person, face or hands. Real softly folded duvet fills the lower foreground with exceptionally clear weave, seams and natural weight. The broad wall ahead is covered edge to edge and ceiling-junction to baseboard by one seamless luminous panorama seen through tall elegant Gothic timber window arches. BOTH window architecture and landscape are projected light on the plain wall, not actual openings. ALL visible wall is covered, including both sides. The panorama continues beyond the crop with room for a later LEFTWARD PAN; no blank strip or cropped-off projection rectangle. The real ceiling junction, room corner and baseboard establish the physical room. Main lights off, believable controlled blue and golden reflected light on the actual duvet and cabinet. One coherent flat wall perspective, straight window posts, no warped arches. The distant landscape has believable photographic depth inside the projected panes but does not extend physically into the room.

Beyond the coherent projected arches is ONE continuous spectacular Christmas view: a magnificent REALISTIC Austrian lakeside Christmas town beneath immense snowy Alps: a few beautifully resolved pastel village houses and timber chalets with thick fresh snow on roofs, glowing amber windows and clearly visible smoking chimneys, a graceful narrow church spire beside the lake, a grand decorated Christmas spruce and golden lanterns in the waterfront square, a charming illuminated Christmas market, and an old stone footbridge crossing a small stream into the dark-blue lake. The still water mirrors the warm village lights and natural emerald-and-rose aurora. Snow-laden fir branches frame the view beyond the window. Santa's small sleigh and a clear team of reindeer cross the upper sky. Fine individual snowflakes, luminous gold lights, forest green and deep cobalt snow. Vast mountain scale and photographic depth with a few legible hero buildings rather than countless tiny smeared buildings. The scene must be photorealistic location photography, not a fairytale painting, video-game environment, miniature model or 3D illustration. Clearly separate near snow-laden fir branches, the legible hero village buildings and immense distant mountains. Steam/smoke visibly rises above the chimneys, the small Santa sleigh and its reindeer are already present, and the bright aurora is already present. Every pane shows its proper portion of the same continuous view. Never repeat identical views in adjacent panes. Rich dense luminous color, brilliant but controlled Christmas lights, deep blue snowy shadows and clear natural texture; not translucent or washed out. Window posts remain dark solid continuous shapes in front of all outdoor objects, joined to the sill. Keep real-room light spill subtle and physically plausible.

CRITICAL IMAGE QUALITY: crisp, clean native-2K iPhone photograph with excellent low-light exposure and deep focus across foreground bedding, furniture, wall and the projected scenery. Clearly resolved duvet weave and seams, wood grain, plant leaves, stone tracery edges, individual rooflines, window mullions, snow on branches, distant palace towers and chimney outlines. High microcontrast without oversharpened halos. Render every visible surface freshly and precisely; do not copy softened or smeared pixels from the references. No shallow depth of field, no soft duvet, no haze, no fog over the image, no glowing bloom hiding detail, no gaussian blur, no motion blur, no muddy shadows, no painterly smearing, no grain, no bokeh, no fisheye or barrel distortion. Maintain natural photographic light and texture, not a plastic CGI render. No text, captions, watermarks or playback icons.
````

#### Video prompt — `clips/v4_c05_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `f39219d2-e80d-407d-828e-47a66a75650f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192252_f39219d2-e80d-407d-828e-47a66a75650f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c05_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c05_g1.png` · Higgsfield media `4cc5336f-bbc1-4e91-bc9d-84b485026ec0`
- image ref 1: `content/video_4_assets/starting_frames/v4_c05_g1.png` · Higgsfield media `4cc5336f-bbc1-4e91-bc9d-84b485026ec0`

````text
A four-second handheld first-person RIGHT PAN from bed, beginning at exactly the supplied photograph. The lens is at pillow height above the ivory cotton duvet. This is a phone recording of a Christmas projection covering a bedroom wall.

Immediately turn the recording camera to the RIGHT through a broad 35-45 degree arc over the full four seconds, in one continuous, clearly visible sweep. By 1.5 seconds the cabinet, potted fir and the starting leftmost window arch have completely left the left edge. Keep turning until the window arch that begins at the far RIGHT of the starting photograph is near the MIDDLE of the view, revealing more of the projected wall beyond the original right edge. The entire bedroom view changes naturally with this turn: the duvet, baseboard, ceiling edge and wall-fixed window posts all travel LEFT across the recording together. This is a substantial rightward turn of the recording phone, not a tiny drift. A relaxed wrist movement with slight hand wobble, constant lens, no zoom or sideways travel. Only the room and bedding are visible; the recording person, their hands and phone stay behind the lens.

The projected scene plays like an animated Christmas illustration on a screen fixed to the wall. The Gothic window borders, village buildings, waterfront village houses and mountains remain stationary on that screen. Houses do not change window panes. The illustration has no panning camera of its own.

Animate these subjects clearly from beginning to end: rolling plumes of white smoke rise and curl from several fixed chimneys; Santa's sleigh travels across the sky behind running reindeer, passing the stationary moon; broad emerald aurora ribbons wave and ripple above stationary mountain peaks. Falling snow and rippling lake reflections add continuous movement. Window posts stay intact in front of all these moving subjects. Keep the rest of the scene still relative to the wall while the recording camera turns.

One uncut realistic iPhone night shot, sharp room textures and luminous projection, natural room ambience. No visible devices, cuts, captions or music.
````
