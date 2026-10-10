# Video 5 - MerryGlowUSA Christmas projector B-roll

**Current status (2026-09-22):** All five selected clips, including the hook, upscaled with ByteDance Pro at 2K/30 fps. AIGC for C01; Common for C02-C05. Originals preserved; upscales saved directly under clips/upscaled with exact source names. Verified 1440x2560, 30 fps, audio present and full decode exit 0. Board points to the upscales.

## Reusable blocks

GPT Image 2.5 Sunburst; 2K; medium; 9:16. Exact reusable camera, scale and quality blocks appear verbatim in each prompt below.


## C02 - frame take 1

**File:** starting_frames/v5_c02_g1.png
**Status:** submitted; awaiting result.
**Job ID:** 1d144c78-ecdc-411b-906d-0f263935b57e
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"ef120f6b-b2f6-414a-af8f-0f9197f667de"},{"role":"image","value":"4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919"}]}
**References:** @Image 1: ../video_3_assets/starting_frames/v3_c02_g1.png (job/media ef120f6b-b2f6-414a-af8f-0f9197f667de); @Image 2: ../../product_images/box_heritage_green_g1.png (job/media 4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919)
**Lineage:** Reused from v3 C02 frame g1 — changed only skin/sleeve, materials, room decor and Christmas landscape nouns for Video 5; framing, scale, geometry and quality instructions retained.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Replace the FIRST reference's carton with OUR MerryGlowUSA product box exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton with forest green body, a blank dark-red band across the top bordered in gold, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold-and-red star-and-tree burst over a printed render of a white cylindrical projector in a white U-shaped pivoting bracket on a round flat white base, a black circular slatted front grille with a central glass lens, a slim black remote printed beside it, gold village skyline along the bottom, and the bottom labels REMOTE CONTROL, 45 MIN, 90 MIN, no transparent window. Preserve the tilted projector ILLUSTRATION printed on the box exactly; it is artwork only. The physical projector is concealed in the closed carton in this starting frame. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only the product carton, the table and the background; keep the hands and pose.

FIRST - THE HANDS. A woman's hands, about 35, with medium golden-brown skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a warm taupe cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a spacious festive American dining room with soft dove-grey walls, honey-oak shelving, a rectangular bronze mirror, a pale stone fireplace with forest-green stockings and a tall Christmas tree with burgundy glass ornaments, ivory ribbons and warm-white lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The red band must remain BLANK, exactly as on the SECOND attached reference. No THEXMASGLOW wordmark, no invented MerryGlowUSA wordmark, no brand name added anywhere on the carton. Preserve the exact headline and bottom labels from the SECOND reference, sharp and legible.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, box placement, hand positions and camera. @Image 2 owns the MerryGlowUSA carton geometry and product identity. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
```

### Video prompt
**Status:** submitted, completed and saved; this take is the one selected on the board. One generation; no reroll.
**Clip:** `clips/v5_c02_g1.mp4`
**Upscale:** `clips/upscaled/v5_c02_g1.mp4` - ByteDance Pro at 2K/30 fps, Common preset. The round kept one aggregate upscale record only; no per-clip upscale job ID was archived.
**Job ID:** `72e57310-1c9a-42e7-9128-221fe8ba70f7`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; audio is present in the delivered mp4 (aac).
**References:** start_image `1d144c78-ecdc-411b-906d-0f263935b57e` = `starting_frames/v5_c02_g1.png`; additional image `4101c330-1b9c-4116-9e6e-246ae3a4434e` = `starting_frames/v5_c03_g1.png`.
**Lineage:** Reused from v4 C02 video take 1 - changed: "honey-oak" -> "ivory limestone"; "fine straight wood grain, a satin-matte" -> "subtle pale-grey fossil markings, a honed matte"; "deep forest-green knitted" -> "warm taupe cable-knit"; "warm cream" -> "soft dove-grey"; "dark-oak built-in shelves, an arched antique-brass" -> "honey-oak shelving, a rectangular bronze"; "white brick" -> "pale stone"; "ivory" -> "forest-green"; "red" -> "burgundy"; "gold bells." -> "ivory ribbons.". Every other word of the prompt - camera, action timeline, beat timings, audio and the hard-rule bans - is byte-identical to the source.

```text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing MerryGlowUSA carton. Keep the blank dark-red top band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and black remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls frame 0.0s, the exact printed box, hands, table, room, props and light. @Image 1 is the approved C03 image and supplies ONLY the actual upright projector design and orientation, not its kitchen or hands. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a blank dark red band across the top, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white cylindrical projector in a white U-shaped bracket on a round base, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: the exact larger matte-white upright CYLINDER shown in @Image 1, retaining its full physical size and proportions, in its white U-shaped bracket on a flat round white base. The cylinder axis is VERTICAL, lens facing straight UP at the ceiling. Its flat circular black slatted top face surrounds a central blue lens. The top face is BLACK and stays black for every frame. The cylinder is locked upright relative to its bracket throughout the lift; never inclined on the mount, never copied from the angled illustration on the carton. Round base horizontal. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a warm taupe cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, the supplied festive dining room with soft dove-grey walls, honey-oak shelving, a rectangular bronze mirror, a pale stone fireplace with forest-green stockings and a tall Christmas tree with warm-white lights, burgundy glass ornaments and ivory ribbons. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK slatted circular top face and central blue lens visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
```

**Archive note:** prompt text, job ID and media roles recovered verbatim from the Higgsfield generation record on 2026-09-23. This section previously read "Not submitted; stills only.", which was wrong - the clip and its 2K upscale are on disk and the board points at the upscale.


## C04 - reference take 1

**File:** references/v5_c04_r1.png
**Status:** submitted; awaiting result.
**Job ID:** fbbdcee4-579b-486d-bc0a-2a99ea8e968a
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"d5c01f65-2395-4799-82cc-d479c50f61bf"},{"role":"image","value":"4ac06232-8065-4c69-a050-491de9e9538f"}]}
**References:** @Image 1: ../video_3_assets/references/v3_c04_r1.png (job/media d5c01f65-2395-4799-82cc-d479c50f61bf); @Image 2: ../video_3_assets/starting_frames/v3_c05_g1.png (job/media 4ac06232-8065-4c69-a050-491de9e9538f)
**Lineage:** Reused from v3 C04 reference r1 — changed only skin/sleeve, materials, room decor and Christmas landscape nouns for Video 5; framing, scale, geometry and quality instructions retained.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create one vertical 9:16 LIGHTS-OFF REFERENCE FRAME for a new MerryGlowUSA Christmas projector video. @Image 1 owns the exact room layout, camera position, viewing direction and furniture arrangement; change only the room materials/decor listed below and improve the projected view. @Image 2 supplies the Christmas-window theme only, never its blur, painterly scenery or protruding window geometry. Create a real handheld iPhone photograph of a real bedroom with a luminous flat wall projection.

KEEP THE ROOM LAYOUT FROM @Image 1 but use these new materials: soft dove-grey plaster walls and ceiling, dark walnut floor, ivory woven rug, king-size honey-oak bed with a crisp white cotton quilt and deep-green-and-gold tartan runner, two forest-green cushions and one central burgundy velvet cushion, white pillows, honey-oak nightstands and bronze lamps, ivory linen curtains behind the headboard on the BACK wall, real fir garland with tiny warm lights and burgundy bows around the headboard, tall Christmas tree in the back-right corner, burgundy upholstered bench at the foot of the bed with a cream woven throw over its right side. Same spatial layout and distances. The LEFT wall remains a solid flat wall with no actual windows.

CAMERA LOCATION: preserve @Image 1's existing viewpoint, standing to the right of the foot of the bed and looking diagonally LEFT toward the long wall. The enormous projected window view fills the left and central 70 percent of the picture; the familiar bed, runner and a sliver of the garland-wrapped headboard appear along the lower-right and right edge. Correct consistent perspective, no mirrored layout, no moving walls, no relocated bed. This will be the reveal orientation; the matching lights-on frame will be made by rotating the phone RIGHT from this same physical standing point. No people or hands visible.

LIGHTS ARE NOW OFF: the ceiling-fan light and both bedside lamps are off, warm bulbs not glowing. Keep only tiny Christmas garland/tree pin lights and the spectacular wall projection as illumination. Expose expertly for the projection while keeping real bedding folds and room silhouettes readable; beautifully subtle icy blue and golden light spill on the near cream duvet and pale floor.

THE PAYOFF ON THE LEFT WALL: one huge brilliant, high-contrast projection of an elegant grand arched window with warm timber mullions. Frame and scenery are projected onto the SAME FLAT WALL, with no structural opening. Through the panes is ONE continuous photographic landscape: a breathtaking REALISTIC old Quebec Christmas town above a frozen river: richly detailed stone townhouses with steep snowy roofs, warm golden windows and visible smoking chimneys lining a cobbled Christmas street, a grand historic copper-roofed chateau on the hill, one magnificent illuminated Christmas tree beside a small festive market, glowing street lanterns, and a beautiful old stone bridge over the partly frozen river. Snow-laden pines and distant rolling snowy hills give the town enormous photographic depth. Emerald-and-violet aurora curtains stretch across the clear deep-blue winter sky. Santa's small sleigh and a clear team of reindeer are visible in the upper sky. Distinct falling snowflakes, believable natural snow surfaces, detailed weathered stone and warm holiday lights. An expansive photographic landscape with a few legible hero buildings rather than dense miniature CGI clutter. Every pane shows its proper part of the same continuous landscape, with no repeated panels. Opaque-looking, crisp dark mullions form an uninterrupted foreground layer all the way down to the projected sill. Scenery and snowy branches remain BEHIND every mullion, never overlapping or interrupting its base.

PROJECTION PHYSICS: substantially stronger, richer and less transparent than @Image 1. Dense luminous color and decisive contrast cover the wall, no ghostly double exposure and no pale wall color washing through the scenic image. Deep dark window-frame shapes, brilliant controlled highlights without bloom, clear photographic details. The room is dark enough for a vivid high-output projection. Wall texture is only a barely perceptible surface grain, not visible through the buildings. All projected geometry is FLAT on the wall, follows one coherent perspective, and stays bounded by the real ceiling junction and baseboard. Physically believable blue and gold light spill on actual bedding; natural room shadows, no beam haze. Vivid projection while retaining real-room photographic credibility.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
```

### Video prompt

Not submitted; stills only.


## C03 - frame take 1

**File:** starting_frames/v5_c03_g1.png
**Status:** submitted; awaiting result.
**Job ID:** 4101c330-1b9c-4116-9e6e-246ae3a4434e
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"0b51a9d5-141b-4052-a50b-62619fc01123"},{"role":"image","value":"1d144c78-ecdc-411b-906d-0f263935b57e"}]}
**References:** @Image 1: ../video_1_assets/starting_frames/v1_c03_g3.png (job/media 0b51a9d5-141b-4052-a50b-62619fc01123); @Image 2: ../video_5_assets/starting_frames/v5_c02_g1.png (job/media 1d144c78-ecdc-411b-906d-0f263935b57e)
**Lineage:** Reused from v3 C03 frame g1 — changed only room materials, decor, skin/sleeve and scenery nouns for Video 5. Camera, framing, enlarged lens-UP product scale and image-quality blocks retained. References use the matching new C02/C04 reveal where applicable.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create the next MerryGlowUSA C3 photograph using @Image 1 for the upright product design, kitchen composition and camera, and @Image 2 for the real product SCALE relative to its carton and adult hands, the skin and sweater. Make the physical projector appreciably BIGGER than @Image 1 so it matches the product that fits inside the carton in @Image 2. Use the new kitchen and materials below. Keep the cylinder perfectly upright, lens pointing straight UP.

KEEP THE COMPOSITION FROM @Image 1: the camera position, camera height, lens, distance, vertical 9:16 crop, the general two-handed supporting pose, central product placement and forearm entry points. Enlarge the complete projector about 40 percent relative to the adult hands and picture; adapt finger contacts naturally to the larger device, keeping anatomy and hand size realistic.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with medium golden-brown skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a warm taupe cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same warm taupe cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the complete upright projector, from the top black lens panel to the bottom round base, occupies about 42 percent of the full image height. Base diameter occupies about 30 percent of image width. A substantial real device held in two adult hands, not a miniature. Its actual overall height is about 80-85 percent of the tall carton in @Image 2, allowing realistic packaging clearance. Enlarge all product components together, preserve their original proportions and ordinary adult hand dimensions. Keep visible air beneath the base and counter. Both hands support the device firmly and naturally.

THE PRODUCT - the same MerryGlowUSA matte-white cylindrical projector barrel in its white U-shaped pivot bracket on a round flat white base. USER-CONFIRMED ORIENTATION: THE CYLINDER STANDS VERTICALLY UPRIGHT, WITH THE BLACK LENS/GRILLE FACE ON TOP POINTING STRAIGHT UP AT THE CEILING. Retain @Image 1's already confirmed upright lens-UP orientation without any tilt. Its long axis is vertical and PERPENDICULAR to the horizontal circular base, like an upright can standing on end. The circular black slatted lens face is a HORIZONTAL TOP FACE, parallel to the round base, visible from above as an ellipse at this existing camera height; the central blue glass lens looks upward. The solid white barrel extends straight down below that top face, sitting vertically between the two upright support arms. The round base remains flat and horizontal, and the support arms remain vertical. The projector does NOT point at the camera, does NOT lie sideways, and does NOT lean diagonally. No forward-facing black front disc: the black disc is now on TOP. Preserve the exact existing cylinder shell, horizontal ventilation slats across the black lens panel, blue glass lens, side pivot, U bracket and circular base; do not replace it with the older dome projector or four-legged stand. @Image 2 supplies product materials and component identity only; IGNORE its printed tilted pose. The device has the same design and upright configuration as @Image 1.

THE COUNTER - a white marble counter with delicate pale-grey veins, a straight eased edge and matte surface. Same shape, position and amount visible as @Image 1.

THE KITCHEN - a sharply resolved traditional Christmas kitchen: slate-blue shaker cabinets with aged brass pulls, creamy white tiles, dark-walnut open shelves, a cream enamel range, forest-green velvet ribbons, warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree in the far corner. Balanced soft window fill and warm interior light, realistic iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns camera, layout and upright product geometry only, not its undersized scale. @Image 2 owns the adult hand appearance, sweater, material realism and physical carton-to-projector scale. Its printed tilted product illustration must NEVER set the real projector orientation. The physical unit is larger, perfectly vertical, lens UP. All parts in natural crisp iPhone deep focus, no portrait mode, bokeh or blur.
```

### Video prompt
**Status:** submitted, completed and saved; this take is the one selected on the board. One generation; no reroll.
**Clip:** `clips/v5_c03_g1.mp4`
**Upscale:** `clips/upscaled/v5_c03_g1.mp4` - ByteDance Pro at 2K/30 fps, Common preset. The round kept one aggregate upscale record only; no per-clip upscale job ID was archived.
**Job ID:** `372279eb-f186-466f-9281-d07cf5c5589a`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; audio is present in the delivered mp4 (aac).
**References:** start_image `4101c330-1b9c-4116-9e6e-246ae3a4434e` = `starting_frames/v5_c03_g1.png`. No additional media attached.
**Lineage:** Reused from v4 C03 video take 1 - changed: "pale ivory quartz" -> "white marble"; "fine warm-grey" -> "delicate pale-grey"; "deep forest-green knitted" -> "warm taupe cable-knit"; "warm mushroom" -> "slate-blue"; "bronze" -> "brass"; "ivory handmade square" -> "creamy white"; "honey-oak" -> "dark-walnut"; "white" -> "cream". Every other word of the prompt - camera, action timeline, beat timings, audio and the hard-rule bans - is byte-identical to the source.

```text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a white marble counter with delicate pale-grey veins and a straight eased edge, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - the exact matte-white upright CYLINDER in the start image, in its white U-shaped bracket on a flat round white base. Cylinder axis VERTICAL, lens pointing straight UP at the ceiling. Its black slatted circular top face surrounds the central blue lens. The top face is BLACK and stays black for every frame. The cylinder stays locked upright within the bracket throughout; no inclination on its mount. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in warm taupe cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a white marble counter with delicate pale-grey veins and a straight eased edge; behind it slate-blue shaker cabinets with aged brass pulls, creamy white tiles, dark-walnut shelves, a cream enamel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the white marble counter with delicate pale-grey veins and a straight eased edge, matte rather than mirror-polished.

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

**Archive note:** prompt text, job ID and media roles recovered verbatim from the Higgsfield generation record on 2026-09-23. This section previously read "Not submitted; stills only.", which was wrong - the clip and its 2K upscale are on disk and the board points at the upscale.


## C04 - frame take 1

**File:** starting_frames/v5_c04_g1.png
**Status:** submitted; awaiting result.
**Job ID:** cb3b1593-094e-46ca-8caf-f3d6c3019202
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"fbbdcee4-579b-486d-bc0a-2a99ea8e968a"},{"role":"image","value":"11720edc-b38f-48f6-bc92-8278407f2181"}]}
**References:** @Image 1: ../video_5_assets/references/v5_c04_r1.png (job/media fbbdcee4-579b-486d-bc0a-2a99ea8e968a); @Image 2: ../video_1_assets/starting_frames/v1_c04_g3.png (job/media 11720edc-b38f-48f6-bc92-8278407f2181)
**Lineage:** Reused from v3 C04 frame g1 — changed only room materials, decor, skin/sleeve and scenery nouns for Video 5. Camera, framing, enlarged lens-UP product scale and image-quality blocks retained. References use the matching new C02/C04 reveal where applicable.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create the LIGHTS-ON STARTING FRAME by editing @Image 1, the existing matching lights-off bedroom reference. Keep the photographer in the EXACT SAME physical place, at the same eye height, with the same lens and standing location as @Image 1, but ROTATE THE PHONE TO THE RIGHT by roughly 30 degrees. The viewing direction and framing MUST change; the camera's physical location must not. @Image 1 owns all geometry. @Image 2 is the previous lights-on image and supplies ONLY the brightness, realistic photographic look and red-sleeved hand holding the black MerryGlowUSA remote; it must NOT control camera position or framing. Changes are only: turn the phone's view RIGHT from that stationary location, turn room lights on, turn the wall projection completely off, and add the remote hand.

KEEP THE ROOM FROM @Image 1: soft dove-grey plaster walls and ceiling, dark walnut floor, ivory woven rug, king-size honey-oak bed with a crisp white cotton quilt and deep-green-and-gold tartan runner, two forest-green cushions and one central burgundy velvet cushion, white pillows, honey-oak nightstands and bronze lamps, ivory linen curtains behind the headboard on the BACK wall, real fir garland with tiny warm lights and burgundy bows around the headboard, tall Christmas tree in the back-right corner, burgundy upholstered bench at the foot of the bed with a cream woven throw over its right side. Same spatial layout and distances. The LEFT wall is an uninterrupted plain warm-greige wall with no actual windows. It remains the same solid flat wall.

CAMERA LOCATION VERSUS VIEW DIRECTION - CRITICAL CORRECTION: the photographer's feet and the camera lens centre stay exactly at @Image 1's viewing point, to the right of the foot of the bed, at the same height. From there, turn the phone RIGHT about 30 degrees, with no sideways movement, no walking and no zoom. The starting image looks more toward the bed and its headboard/back curtains; the bed and upholstered foot-bench become the central subjects. The left projection wall recedes diagonally along only the LEFT 20-30 percent of the starting image, not across the middle. The back-left room corner shifts clearly LEFTWARD in the picture compared with @Image 1. Show more of the back wall, headboard and right-hand part of the bedroom. The perspective still comes from the same off-centre spot right of the bed's foot, never the central doorway view. Do not preserve @Image 1's exact crop or orientation: that was the previous mistake. Do not move any furniture or mirror the room. This frame is the START BEFORE a future LEFTWARD PAN: the camera will later rotate left from this fixed spot to arrive at @Image 1's reveal framing. Capture the right-facing starting orientation now.

LIGHTS ARE NOW ON: the ceiling-fan light and both bedside lamps illuminate the same room with clean warm light. Keep the fairy lights on the headboard and tree. Match the well-exposed natural warm interior-photo look of @Image 2, while preserving @Image 1's room geometry and applying the new right-facing camera orientation. Fine duvet, rug and wood details stay crisp; do not make the room dark.

THE LEFT WALL BEFORE ACTIVATION: completely REMOVE the entire projected Christmas scene AND every projected arch, window frame, mullion, sill, frost edge and glow from @Image 1. The same wall is now one continuous blank smooth warm-ivory wall, with its real baseboard and ceiling junction in their original positions. No actual window exists on this left wall. No remnants, embossed arches, ghost outlines, rectangular screen, poster or scenery. The real white curtains on the BACK wall remain.

REMOTE HAND: add the same adult right hand and red pajama sleeve visible in @Image 2, entering naturally from the lower right and holding the exact same slim black MerryGlowUSA remote at a comfortable arm's length. The thumb is poised over the central OK/play control before pressing; correct five-finger anatomy, black direction pad, red power button, matching remote scale. Keep the hand low in the right foreground, leaving the blank left wall and its corner unobstructed. It must read as the POV of the person standing at @Image 1's fixed location, not a second person or floating hand. No product box.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
```

### Video prompt
**Status:** submitted, completed and saved; this take is the one selected on the board. One generation; no reroll.
**Clip:** `clips/v5_c04_g1.mp4`
**Upscale:** `clips/upscaled/v5_c04_g1.mp4` - ByteDance Pro at 2K/30 fps, Common preset. The round kept one aggregate upscale record only; no per-clip upscale job ID was archived.
**Job ID:** `420693b7-22e8-4fe7-b641-d825753c063e`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 5, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; audio is present in the delivered mp4 (aac).
**References:** start_image `cb3b1593-094e-46ca-8caf-f3d6c3019202` = `starting_frames/v5_c04_g1.png`; additional image `fbbdcee4-579b-486d-bc0a-2a99ea8e968a` = `references/v5_c04_r1.png`; motion reference `b3902899-d75c-4875-ae1e-3c0e4fbec222` = `../video_1_assets/clips/v1_c04_g1.mp4`.
**Lineage:** Reused from v4 C04 video take 1 - changed: "burgundy-and-cream" -> "deep-green-and-gold"; "burgundy" -> "ivory"; "Austrian lakeside" -> "old Quebec"; "lake," -> "river,"; "lake" -> "river". Every other word of the prompt - camera, action timeline, beat timings, audio and the hard-rule bans - is byte-identical to the source.

```text
One continuous 5-second POV handheld iPhone video. The attached start image is the EXACT first frame and owns the bedroom geometry, bed, bench, rug, red sleeve, hand and black remote. @Image 1 supplies the Christmas projection artwork for the LEFT wall. Its bedroom perspective is not an endpoint to morph into. Keep the physical room of the starting frame throughout. @Video 1 is the approved Video 1 C04 clip, used as a MOTION reference only: closely copy its quick thumb press, natural lowering of the remote hand and subsequent leftward handheld camera pan. Do not copy its different bedroom, lower image quality, text overlays or sound.

0.0-0.2s: from the supplied remote position the wrist makes a small natural forward/up adjustment and the thumb visibly depresses the play/OK button ONCE. Match the reference's immediate decisive press, not a long aiming gesture.
At exactly the button depression, around 0.2s: the ceiling light and bedside lamps switch OFF instantly, and the luminous Christmas-window projection switches ON on the LEFT wall in the SAME moment. No delayed reveal and no gradual fade. Existing Christmas fairy lights remain dimly lit.
0.2-1.6s: the hand relaxes and naturally lowers the still-gripped remote down toward the lower right and out of view, following @Video 1's hand movement. No waving, no tossing the remote, no second press. Simultaneously begin a gentle continuous pan LEFT at normal handheld-phone pace.
1.6-4.2s: continue rotating the phone LEFT from the same standing spot until the left wall projection dominates the view, showing @Image 1's artwork from the actual camera's viewpoint. The bed shifts toward the right edge as a result of this rotation. No walking forward, no sideways camera translation, no zoom and no cut. Natural tiny hand tremor, coherent room perspective.
4.2-5.0s: settle into the spectacular left-wall view with slight natural handheld drift.

ROOM RIGIDITY: Keep the starting room a single solid three-dimensional space. Its flat left wall, straight ceiling junction, rear curtain wall and floor remain rigidly connected at fixed angles. The camera turns within that room; walls never rotate, bend, expand, slide or change shape. The bench, bed, rug and ceiling fan keep their original dimensions and positions. Preserve the deep-green-and-gold tartan bed runner and ivory rug from the starting image; do not borrow the red runner or green rug from @Video 1. The sole tall Christmas tree remains to the RIGHT of the bed. The projection is flat light on the existing left wall, not an opening or new room. The window artwork obeys that wall's perspective and remains fixed on it. Use @Image 1 for artwork content only, never its room outline or furniture placement.

The wall projection must be a visibly ANIMATED Christmas scene, never a frozen still. Preserve @Image 1's window framing and continuous snowy old Quebec Christmas town, illuminated houses, trees, river, mountains, aurora and sleigh. From the instant the projection appears through the final frame, soft smoke continuously curls upward and drifts from multiple house chimneys, Santa's sleigh and pulling reindeer visibly travel across the sky with gently cycling reindeer legs, and luminous aurora curtains continuously ripple and flow. Fine snow falls within the projected scene; river reflections shimmer gently. All this motion occurs INSIDE the projection. The projected window frame remains fixed to the real wall. The entire projection does not slide, breathe, scale or float. Preserve the actual bedroom walls, bedding and furniture as solid stationary physical objects. Projection light naturally spills across the room and duvet after the click.

Sharp realistic iPhone footage, clean low-light exposure and detailed moving scenery. Exactly one visible hand holding one remote, natural thumb anatomy. No new person, no real window opening in the wall, no overlay text, no watermarks, no scene transition, no reversed pan, no music. Only quiet bedroom ambience, subtle sleeve movement and the single dry remote click. Ignore all audio in @Video 1. (no BGM). No subtitles.
```

**Archive note:** prompt text, job ID and media roles recovered verbatim from the Higgsfield generation record on 2026-09-23. This section previously read "Not submitted; stills only.", which was wrong - the clip and its 2K upscale are on disk and the board points at the upscale.


## C05 - frame take 1

**File:** starting_frames/v5_c05_g1.png
**Status:** submitted; awaiting result.
**Job ID:** bfca2ec6-d4aa-4aa4-9724-ad9e41653a27
**Settings:** {"model":"gpt_image_2_5","variant":"sunburst","resolution":"2k","quality":"medium","aspect_ratio":"9:16","count":1,"medias":[{"role":"image","value":"4ac06232-8065-4c69-a050-491de9e9538f"},{"role":"image","value":"fbbdcee4-579b-486d-bc0a-2a99ea8e968a"}]}
**References:** @Image 1: ../video_3_assets/starting_frames/v3_c05_g1.png (job/media 4ac06232-8065-4c69-a050-491de9e9538f); @Image 2: ../video_5_assets/references/v5_c04_r1.png (job/media fbbdcee4-579b-486d-bc0a-2a99ea8e968a)
**Lineage:** Reused from v3 C05 frame g1 — changed only room materials, decor, skin/sleeve and scenery nouns for Video 5. Camera, framing, enlarged lens-UP product scale and image-quality blocks retained. References use the matching new C02/C04 reveal where applicable.
**Backend adjustments:** {"medias[0].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"},"medias[1].role":{"requested":"image","used":"image_references","reason":"GPT Image 2.5 backend expects schema-key media roles"}}

### Image prompt

```text
Create a new hyperrealistic low-light iPhone photograph for MerryGlowUSA C5. @Image 1 supplies ONLY the low bed-level camera position, wide full-wall composition and continuous foreground window-frame layout. Do NOT copy its blurry rendering, painterly scenery, stone texture or fake CGI surfaces. @Image 2 supplies the new photographic Christmas landscape and rich opaque-looking projection. Render the entire image afresh in crisp native detail. Real bedroom materials: white linen duvet with resolved stitched seams and green-and-gold plaid blanket edge, a simple low honey-oak cabinet, a modest real potted fir, soft dove-grey wall and dark walnut floor. Preserve the believable low lying-in-bed perspective from @Image 1. Use elegant warm timber Gothic projected arches with slender mullions. ALL window arches, vertical posts and bottom sill form one continuous opaque foreground layer over the scenery. Every post runs uninterrupted from the arch to a clear connection with the sill. Snow, trees, roofs and lights are behind the frame and can NEVER overlap, erase or interrupt a post at its bottom. The entire frame and scenery are FLAT projected light on the solid wall, never actual structural windows or protruding architecture.

POV lying comfortably in bed, camera at pillow height, no visible person, face or hands. Real softly folded duvet fills the lower foreground with exceptionally clear weave, seams and natural weight. The broad wall ahead is covered edge to edge and ceiling-junction to baseboard by one seamless luminous panorama seen through tall elegant Gothic timber window arches. BOTH window architecture and landscape are projected light on the plain wall, not actual openings. ALL visible wall is covered, including both sides. The panorama continues beyond the crop with room for a later LEFTWARD PAN; no blank strip or cropped-off projection rectangle. The real ceiling junction, room corner and baseboard establish the physical room. Main lights off, believable controlled blue and golden reflected light on the actual duvet and cabinet. One coherent flat wall perspective, straight window posts, no warped arches. The distant landscape has believable photographic depth inside the projected panes but does not extend physically into the room.

Beyond the coherent projected arches is ONE continuous spectacular Christmas view: a breathtaking REALISTIC old Quebec Christmas town above a frozen river: richly detailed stone townhouses with steep snowy roofs, warm golden windows and visible smoking chimneys lining a cobbled Christmas street, a grand historic copper-roofed chateau on the hill, one magnificent illuminated Christmas tree beside a small festive market, glowing street lanterns, and a beautiful old stone bridge over the partly frozen river. Snow-laden pines and distant rolling snowy hills give the town enormous photographic depth. Emerald-and-violet aurora curtains stretch across the clear deep-blue winter sky. Santa's small sleigh and a clear team of reindeer are visible in the upper sky. Distinct falling snowflakes, believable natural snow surfaces, detailed weathered stone and warm holiday lights. An expansive photographic landscape with a few legible hero buildings rather than dense miniature CGI clutter. The scene must be photorealistic location photography, not a fairytale painting, video-game environment, miniature model or 3D illustration. Clearly separate near snow-laden fir branches, the legible hero village buildings and immense distant mountains. Steam/smoke visibly rises above the chimneys, the small Santa sleigh and its reindeer are already present, and the bright aurora is already present. Every pane shows its proper portion of the same continuous view. Never repeat identical views in adjacent panes. Rich dense luminous color, brilliant but controlled Christmas lights, deep blue snowy shadows and clear natural texture; not translucent or washed out. Window posts remain dark solid continuous shapes in front of all outdoor objects, joined to the sill. Keep real-room light spill subtle and physically plausible.

CRITICAL IMAGE QUALITY: crisp, clean native-2K iPhone photograph with excellent low-light exposure and deep focus across foreground bedding, furniture, wall and the projected scenery. Clearly resolved duvet weave and seams, wood grain, plant leaves, stone tracery edges, individual rooflines, window mullions, snow on branches, distant palace towers and chimney outlines. High microcontrast without oversharpened halos. Render every visible surface freshly and precisely; do not copy softened or smeared pixels from the references. No shallow depth of field, no soft duvet, no haze, no fog over the image, no glowing bloom hiding detail, no gaussian blur, no motion blur, no muddy shadows, no painterly smearing, no grain, no bokeh, no fisheye or barrel distortion. Maintain natural photographic light and texture, not a plastic CGI render. No text, captions, watermarks or playback icons.
```

### Video prompt
**Status:** submitted, completed and saved; this take is the one selected on the board. One generation; no reroll.
**Clip:** `clips/v5_c05_g1.mp4`
**Upscale:** `clips/upscaled/v5_c05_g1.mp4` - ByteDance Pro at 2K/30 fps, Common preset. The round kept one aggregate upscale record only; no per-clip upscale job ID was archived.
**Job ID:** `f5494f27-03ee-49e1-b653-70553062483b`
**Settings:** {"model": "seedance_2_5", "resolution": "720p", "duration": 4, "aspect_ratio": "9:16"} - model, resolution and duration read back from the generation record; audio is present in the delivered mp4 (aac).
**References:** start_image `bfca2ec6-d4aa-4aa4-9724-ad9e41653a27` = `starting_frames/v5_c05_g1.png`; the same frame was also attached a second time as an image reference.
**Lineage:** Reused from v4 C05 video take 1 - changed: "ivory cotton" -> "white linen"; added "stone"; "village houses" -> "townhouses"; "lake" -> "river". Every other word of the prompt - camera, action timeline, beat timings, audio and the hard-rule bans - is byte-identical to the source.

```text
A four-second handheld first-person RIGHT PAN from bed, beginning at exactly the supplied photograph. The lens is at pillow height above the white linen duvet. This is a phone recording of a Christmas projection covering a bedroom wall.

Immediately turn the recording camera to the RIGHT through a broad 35-45 degree arc over the full four seconds, in one continuous, clearly visible sweep. By 1.5 seconds the cabinet, potted fir and the starting leftmost window arch have completely left the left edge. Keep turning until the window arch that begins at the far RIGHT of the starting photograph is near the MIDDLE of the view, revealing more of the projected wall beyond the original right edge. The entire bedroom view changes naturally with this turn: the duvet, baseboard, ceiling edge and wall-fixed window posts all travel LEFT across the recording together. This is a substantial rightward turn of the recording phone, not a tiny drift. A relaxed wrist movement with slight hand wobble, constant lens, no zoom or sideways travel. Only the room and bedding are visible; the recording person, their hands and phone stay behind the lens.

The projected scene plays like an animated Christmas illustration on a screen fixed to the wall. The Gothic window borders, village buildings, stone waterfront townhouses and mountains remain stationary on that screen. Houses do not change window panes. The illustration has no panning camera of its own.

Animate these subjects clearly from beginning to end: rolling plumes of white smoke rise and curl from several fixed chimneys; Santa's sleigh travels across the sky behind running reindeer, passing the stationary moon; broad emerald aurora ribbons wave and ripple above stationary mountain peaks. Falling snow and rippling river reflections add continuous movement. Window posts stay intact in front of all these moving subjects. Keep the rest of the scene still relative to the wall while the recording camera turns.

One uncut realistic iPhone night shot, sharp room textures and luminous projection, natural room ambience. No visible devices, cuts, captions or music.
```

**Archive note:** prompt text, job ID and media roles recovered verbatim from the Higgsfield generation record on 2026-09-23. This section previously read "Not submitted; stills only.", which was wrong - the clip and its 2K upscale are on disk and the board points at the upscale.


## Completed image round - 2026-09-22

All five images completed and downloaded at 1520 x 2688. Awaiting Daniel's review. Hooks deferred and no animation submitted. Earlier submitted status is historical.

### Completion - starting_frames/v5_c02_g1.png
**Job ID:** 1d144c78-ecdc-411b-906d-0f263935b57e
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_152018_1d144c78-ecdc-411b-906d-0f263935b57e.png
**SHA256:** a65deff824291bff9e1265f270f2ed2b475664d2c63f683678e12e20ecfeac22

### Completion - references/v5_c04_r1.png
**Job ID:** fbbdcee4-579b-486d-bc0a-2a99ea8e968a
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151950_fbbdcee4-579b-486d-bc0a-2a99ea8e968a.png
**SHA256:** 33fa50127582c8c4a867fb95cd9229dc7f60ab6a044f9b663a6c0a88f3ec3c9a

### Completion - starting_frames/v5_c03_g1.png
**Job ID:** 4101c330-1b9c-4116-9e6e-246ae3a4434e
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153822_4101c330-1b9c-4116-9e6e-246ae3a4434e.png
**SHA256:** a7f17f578a67b76abfb759d63fa29a3538d7edea847754961fa1ae233ed9fefa

### Completion - starting_frames/v5_c04_g1.png
**Job ID:** cb3b1593-094e-46ca-8caf-f3d6c3019202
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153753_cb3b1593-094e-46ca-8caf-f3d6c3019202.png
**SHA256:** 9f22e1345765035848786456b0ccab20cd6110b67a73d7abcfb32be779bf5f32

### Completion - starting_frames/v5_c05_g1.png
**Job ID:** bfca2ec6-d4aa-4aa4-9724-ad9e41653a27
**Status:** completed, unreviewed.
**Original URL:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153752_bfca2ec6-d4aa-4aa4-9724-ad9e41653a27.png
**SHA256:** 45a4013c6d32d28a51d5b5680a2c71eab72f901baee3424e53c163efb45f63f9


## C01 - Hook image - 2026-09-22

**Current hook status:** image and animation take 1 approved by Daniel; selected on the MerryGlowUSA board.
**Frame:** `starting_frames/v5_c01_g1.png`
**Job ID:** `7ff54a17-55d7-4423-9cc7-71d4f58ceded`
**Settings:** GPT Image 2.5 (`gpt_image_2_5`), Sunburst, 2K, medium quality, 9:16, count 1; use_unlim omitted. Backend mapped image roles to image_references.
**References (submitted order):**
1. `references/v5_c01_r1.png` - geometry, camera, pose and framing; service ID `f97d7572-0d90-4688-af6e-2555fe14ddb7`; original `THEXMASGLOW - CHRISTMAS PROJECTOR/content/video_7_assets/starting_frames/v7_c01_g2.png`; SHA-256 `d37eadcd82b4ac43931c515388fee445d28e9159387a4fbfe262e2cf519204fd`.
2. `references/v5_c01_r2.png` - MerryGlowUSA carton artwork and product look; service ID `4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919`; original `MerryGlowUSA - CHRISTMAS PROJECTOR/product_images/box_heritage_green_g1.png`; SHA-256 `347c9e17057524a79812f05d0677b167fdf4f34a0a23c8f85065b3eab3c70c22`.

**Lineage:** Reused from TheXmasGlow v7 C01 image g2; changed room/person nouns and reference-role wording; Video 5 also changes carton and display artwork to MerryGlowUSA. Camera, framing, pose and quality instructions retained.

### Image prompt
```text
Copy the FIRST attached reference photo EXACTLY as a photograph: the same camera position standing a couple of steps behind and slightly to the left of the woman, the same eye-level height, the same distance, the same vertical 9:16 framing, the same three-quarters-from-behind view of her with her head and shoulders cropped at the upper left of the frame, the same blue plastic shopping basket hanging from her hand low at the bottom left, the same white retail gondola shelving unit running across the right two thirds of the frame at the same oblique angle, the same four loaded shelves, the same tall narrow printed display banner standing at the right edge, the same polished pale terrazzo store floor, bright neutral overhead LED store lighting and a white slatted store ceiling with recessed rectangular light fixtures across the top. Same composition, same scale of everything. Change only the store finishes, the woman and the product artwork described below; keep the exact same framing and shelf geometry.

FIRST - THE PRODUCT BOXES. Every box on the shelves and every box stacked on top of the shelving unit is now OUR carton, exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, proportions about 1 to 1.6, forest green body, a blank dark red band across the top bordered in gold, with no wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR under it, a gold-and-red star-and-tree burst over a printed render of a white cylindrical projector in a white U-shaped pivoting bracket on a round flat white base, a black circular slatted front grille with a central glass lens, a slim black remote printed beside it, a gold village skyline and the labels REMOTE CONTROL, 45 MIN, 90 MIN along the bottom edge, a thin gold foil border framing the panel, and no transparent window anywhere. SIZE IS CRITICAL: our carton is a SMALL package - roughly 15 cm wide by 15 cm deep by 24 cm tall, about the size of a shoebox stood upright on its end, no taller than the woman's forearm from wrist to elbow, and reaching only about half way up the gap between one shelf and the shelf above it, leaving a clear band of empty shelf air over every row. Keep the corrected small-carton scale shown in the FIRST reference. Because our carton is small, MANY more of them fit: the cartons stand upright side by side, front panels facing the camera, packed tightly from one end of every shelf to the other with at least nine or ten of them across each shelf, four full shelves of them, perfectly aligned in dense neat rows the way a retail end-cap is faced, every carton identical to every other in size, proportion and printing.

SECOND - THE TALL DISPLAY BANNER at the right edge. It is now our banner: a tall narrow vertical printed panel in the same forest green as the carton with a gold foil border, a gold star at the top, no brand wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR, a large printed photograph of the same white MerryGlowUSA projector with its black circular slatted grille, white U-shaped pivoting bracket and round flat base throwing warm gold trees and snowflakes across a dark living-room wall, and a column of small feature icons with the lines Remote Control, 45 MIN and 90 MIN down the lower half. Same position, same width, same height, same angle as in the FIRST reference.

THIRD - THE WOMAN. A different woman from the reference: early 30s, long wavy copper-red hair falling loose down her back, fair freckled skin, an oversized oatmeal cream knitted sweater, and matching American-flag Christmas pyjama bottoms - soft brushed cotton pyjama trousers with bold red and white horizontal stripes and small white five-pointed stars printed across the navy blue waistband panel, slightly loose the way real pyjamas fit - with white ribbed socks in white trainers. She stands in exactly the same place, the same three-quarters-from-behind pose, the same shoulders, the same head turn toward the shelf, the same arm down holding the same blue plastic shopping basket. Same scale in the frame.

FRAMING: leave a clean band of plain store ceiling across the very top of the image - roughly the top eighth of the frame - free of boxes, banners, signage and lettering, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room; she stays exactly the size she is in the FIRST reference.

The cartons must match the SECOND reference exactly, including its blank red top band: do not print THEXMASGLOW or invent a brand wordmark. CHRISTMAS LIGHT PROJECTOR, REMOTE CONTROL, 45 MIN and 90 MIN must be correctly spelled, sharp and legible. The second reference owns product artwork and carton appearance only; do not copy its hands or background.

LIGHTING AND QUALITY: bright, clean, evenly lit big-box store interior, neutral white balance with no orange and no colour cast, no dark corners. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp legible printing on every carton, realistic fabric and skin texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own cartons and banner.
```

### Exact prompt substitutions

- Original: "polished grey concrete store floor"
  Replacement: "polished pale terrazzo store floor"

- Original: "the same bright overhead store lighting and the same ceiling with its light fixtures across the top"
  Replacement: "bright neutral overhead LED store lighting and a white slatted store ceiling with recessed rectangular light fixtures across the top"

- Original: "Change only the three things below."
  Replacement: "Change only the store finishes, the woman and the product artwork described below; keep the exact same framing and shelf geometry."

- Original: "a dark red band across the top carrying a gold THEXMASGLOW wordmark"
  Replacement: "a blank dark red band across the top bordered in gold, with no wordmark"

- Original: "a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector standing on a separate white four-legged splayed stand base, a slim red remote printed beside it"
  Replacement: "a gold-and-red star-and-tree burst over a printed render of a white cylindrical projector in a white U-shaped pivoting bracket on a round flat white base, a black circular slatted front grille with a central glass lens, a slim black remote printed beside it"

- Original: "a gold village skyline along the bottom edge"
  Replacement: "a gold village skyline and the labels REMOTE CONTROL, 45 MIN, 90 MIN along the bottom edge"

- Original: "Do NOT copy the size of the boxes in the FIRST reference - those are much larger packages and their footprint must be ignored completely."
  Replacement: "Keep the corrected small-carton scale shown in the FIRST reference."

- Original: "a gold star at the top, the gold wordmark THEXMASGLOW, a cream serif headline"
  Replacement: "a gold star at the top, no brand wordmark, a cream serif headline"

- Original: "the white dome projector"
  Replacement: "the same white MerryGlowUSA projector with its black circular slatted grille, white U-shaped pivoting bracket and round flat base"

- Original: "16 Patterns, Remote Control, Timer and Indoor and Outdoor"
  Replacement: "Remote Control, 45 MIN and 90 MIN"

- Original: "late 20s, long dark brown hair falling loose down her back"
  Replacement: "early 30s, long wavy copper-red hair falling loose down her back, fair freckled skin"

- Original: "The wordmark printed on the cartons and on the banner must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere in the picture."
  Replacement: "The cartons must match the SECOND reference exactly, including its blank red top band: do not print THEXMASGLOW or invent a brand wordmark. CHRISTMAS LIGHT PROJECTOR, REMOTE CONTROL, 45 MIN and 90 MIN must be correctly spelled, sharp and legible. The second reference owns product artwork and carton appearance only; do not copy its hands or background."

### Generation result and take history
- `starting_frames/v5_c01_g1.png`: completed, 1520 x 2688 PNG, 6542648 bytes; SHA-256 `981f202edf188c9e709128f8f0258307b5e87ca03f7a4b9d0a3f7082a6c9587a`.
- Result URL: https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_164730_7ff54a17-55d7-4423-9cc7-71d4f58ceded.png
- Visual check: Framing closely follows the source. Changed people and room finishes; room changes are subtle. MerryGlowUSA carton and banner artwork visible, blank red band retained. Store ceiling remains close to the original.
- Review status: unreviewed by Daniel. One generation only; no automatic reroll.


### C01 animation - take 1 - 2026-09-22

**Status:** approved by Daniel; completed, saved and selected on the board. One generation; no reroll.
**Starting frame approval:** Daniel approved the C01 image in this conversation: "They camed out good".
**Frame:** `starting_frames/v5_c01_g1.png` - approved.
**Clip:** `clips/v5_c01_g1.mp4`
**Job ID:** `509c4235-a939-48ba-a4da-c96809f3f689`
**Settings:** {"model": "seedance_2_5", "mode": "omni_reference", "resolution": "1080p", "duration": 5, "aspect_ratio": "9:16", "generate_audio": true, "count": 1, "use_unlim": false, "declined_preset_id": "24bae836-2c4a-48e0-89b6-49fcc0b21612", "medias": [{"role": "start_image", "value": "7ff54a17-55d7-4423-9cc7-71d4f58ceded"}]}
**References:** approved starting frame only, existing Higgsfield image generation `7ff54a17-55d7-4423-9cc7-71d4f58ceded`, role start_image. No source video attached.
**Source:** THEXMASGLOW - CHRISTMAS PROJECTOR/content/video_7_assets/prompts.md; C01 video g2, confirmed selected on its board.

Reused from TheXmasGlow v7 C01 video g2 - changed: only the following person/room/product nouns to match the approved MerryGlowUSA frame; all motion, camera, timing, audio and bans unchanged.
- "THEXMASGLOW CHRISTMAS LIGHT PROJECTOR" -> "MerryGlowUSA CHRISTMAS LIGHT PROJECTOR"

#### Video prompt
```text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by a friend standing a few steps behind the woman — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in; all distance changes happen because the woman physically moves, never the lens.

Start frame: a young woman in a cream knit sweater and American-flag pajama pants stands in a bright store aisle holding a blue shopping basket, facing the shelf stacked with the green MerryGlowUSA CHRISTMAS LIGHT PROJECTOR product boxes.

ACTION TIMELINE:
0.0–1.0s — She spots the boxes on the shelf, freezes for a split second, then screams with real excitement: "No way — they actually have it!" Her whole body reacts, shoulders jumping.
1.0–2.0s — She lets the blue shopping basket drop straight out of her hand — it hits the store floor with a loud plastic clatter and tips over — as she spins around to the friend filming, one hand flying to her mouth, eyes huge, pure disbelief on her face.
2.0–3.5s — She whips back around and runs the few steps to the shelf, sweater flapping, shoes squeaking on the store floor, the camera staying put and letting her get smaller toward the shelf.
3.5–5.0s — She grabs one MerryGlowUSA CHRISTMAS LIGHT PROJECTOR box off the shelf with both hands, hugs it to her chest, and bounces on her feet laughing, extremely happy, turning halfway back toward the camera to show it. End frame: her hugging the box, beaming.

AUDIO: her real voice, lip-synced — the excited scream and line, then breathless laughing; the loud clatter of the dropped basket; running footsteps; bright store ambience with distant murmur and faint checkout beeps. NO music, no narration.

REALISM — HARD RULES: she keeps exactly the same face, hair, sweater and outfit as the start frame the whole clip. The shelf and every product box stay pixel-faithful to the start frame — same artwork, logo, colors, spelling, text rigid and never warping. The store background stays identical. Real phone-camera look, slight sensor noise, mild motion blur on the run, no cinematic bokeh, no text overlays, no watermark.
```

#### Take history
One generation submitted; no automatic reroll.

**Result:** {"video": 5, "width": 1080, "height": 1920, "fps": "24/1", "duration": "5.050000", "audio": ["aac"], "bytes": 6731998, "sha256": "04a70c84eb1fc7117e3b885401b8f90d84d43c5b738e8e54daa7dad0af1b2c4f", "decode_exit": 0, "url": "https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_165752_509c4235-a939-48ba-a4da-c96809f3f689.mp4", "note": "Sampled frames show the basket dropping, her turning to the shelf and hugging a carton. Shelf/display geometry shifts as the shot progresses."}
**Prompt verification:** service-returned prompt matches submitted and archived text exactly. Full video/audio decode exit 0.
**Review limits:** sampled frames inspected; audio presence and decoding verified, spoken lines not transcribed. Frame-by-frame review was not performed.
**Selected:** yes - `clips/upscaled/v5_c01_g1.mp4` is the take carried on the board.

---

## Traceability - 2026-09-23

This file was repaired on 2026-09-23 after an earlier session corrupted it. Three defects were found and fixed; nothing else in the file was touched.

1. **Double-encoded UTF-8.** 15 em- and en-dashes had been rewritten as `\u00e2\u20ac\u201d` / `\u00e2\u20ac\u201c`. All were restored. The six `### Image prompt` blocks were then verified byte-exact against the Higgsfield image-generation records (`1d144c78`, `fbbdcee4`, `4101c330`, `cb3b1593`, `bfca2ec6`, `7ff54a17`) - they are intact.
2. **Four missing video prompts.** C02-C05 each read "Not submitted; stills only." while the clips, their 2K upscales and the cut `videos_to_post/video_5.mp4` all exist. The prompts were recovered verbatim from the generation records and restored, with job IDs, the media roles read off each record, and a word-level lineage diff against the archived v4 prompts. No prompt text was rewritten, reworded or reconstructed from a neighbouring take.
3. **Truncated tail.** The file ended mid-word inside the C01 `**Review limits:**` line. That sentence was completed and the selection line restored.

**Unresolved:** the upscale round has no per-clip job IDs, only the aggregate record at the top of this file. Each `**Upscale:**` line above says so rather than naming an ID.



---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: clips byte-identical (md5) to their Higgsfield result unless the entry says otherwise, generated images by exact byte size, and every start frame checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C01: the board did not show the exact image prompt of `v5_c01_g1.png`; it now does.
- C01: the board did not show the exact clip prompt of `v5_c01_g1.mp4`; it now does.
- C02: the board did not show the exact image prompt of `v5_c02_g1.png`; it now does.
- C02: the board did not show the exact clip prompt of `v5_c02_g1.mp4`; it now does.
- C03: the board did not show the exact image prompt of `v5_c03_g1.png`; it now does.
- C04: the board did not show the exact image prompt of `v5_c04_g1.png`; it now does.
- C04: the board did not show the exact image prompt of `v5_c04_r1.png`; it now does.
- C05: the board did not show the exact image prompt of `v5_c05_g1.png`; it now does.

### C01 — Grabbing MerryGlowUSA off the store shelf

**In the cut:** `starting_frames/v5_c01_g1.png` → `clips/v5_c01_g1.mp4`

#### Image prompt — `starting_frames/v5_c01_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `7ff54a17-55d7-4423-9cc7-71d4f58ceded`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_164730_7ff54a17-55d7-4423-9cc7-71d4f58ceded.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_5_assets/references/v5_c01_r1.png` · Higgsfield media `f97d7572-0d90-4688-af6e-2555fe14ddb7`
- @Image 2: `content/video_5_assets/references/v5_c01_r2.png` · Higgsfield media `4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919`

````text
Copy the FIRST attached reference photo EXACTLY as a photograph: the same camera position standing a couple of steps behind and slightly to the left of the woman, the same eye-level height, the same distance, the same vertical 9:16 framing, the same three-quarters-from-behind view of her with her head and shoulders cropped at the upper left of the frame, the same blue plastic shopping basket hanging from her hand low at the bottom left, the same white retail gondola shelving unit running across the right two thirds of the frame at the same oblique angle, the same four loaded shelves, the same tall narrow printed display banner standing at the right edge, the same polished pale terrazzo store floor, bright neutral overhead LED store lighting and a white slatted store ceiling with recessed rectangular light fixtures across the top. Same composition, same scale of everything. Change only the store finishes, the woman and the product artwork described below; keep the exact same framing and shelf geometry.

FIRST - THE PRODUCT BOXES. Every box on the shelves and every box stacked on top of the shelving unit is now OUR carton, exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, proportions about 1 to 1.6, forest green body, a blank dark red band across the top bordered in gold, with no wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR under it, a gold-and-red star-and-tree burst over a printed render of a white cylindrical projector in a white U-shaped pivoting bracket on a round flat white base, a black circular slatted front grille with a central glass lens, a slim black remote printed beside it, a gold village skyline and the labels REMOTE CONTROL, 45 MIN, 90 MIN along the bottom edge, a thin gold foil border framing the panel, and no transparent window anywhere. SIZE IS CRITICAL: our carton is a SMALL package - roughly 15 cm wide by 15 cm deep by 24 cm tall, about the size of a shoebox stood upright on its end, no taller than the woman's forearm from wrist to elbow, and reaching only about half way up the gap between one shelf and the shelf above it, leaving a clear band of empty shelf air over every row. Keep the corrected small-carton scale shown in the FIRST reference. Because our carton is small, MANY more of them fit: the cartons stand upright side by side, front panels facing the camera, packed tightly from one end of every shelf to the other with at least nine or ten of them across each shelf, four full shelves of them, perfectly aligned in dense neat rows the way a retail end-cap is faced, every carton identical to every other in size, proportion and printing.

SECOND - THE TALL DISPLAY BANNER at the right edge. It is now our banner: a tall narrow vertical printed panel in the same forest green as the carton with a gold foil border, a gold star at the top, no brand wordmark, a cream serif headline CHRISTMAS LIGHT PROJECTOR, a large printed photograph of the same white UBU projector with its black circular slatted grille, white U-shaped pivoting bracket and round flat base throwing warm gold trees and snowflakes across a dark living-room wall, and a column of small feature icons with the lines Remote Control, 45 MIN and 90 MIN down the lower half. Same position, same width, same height, same angle as in the FIRST reference.

THIRD - THE WOMAN. A different woman from the reference: early 30s, long wavy copper-red hair falling loose down her back, fair freckled skin, an oversized oatmeal cream knitted sweater, and matching American-flag Christmas pyjama bottoms - soft brushed cotton pyjama trousers with bold red and white horizontal stripes and small white five-pointed stars printed across the navy blue waistband panel, slightly loose the way real pyjamas fit - with white ribbed socks in white trainers. She stands in exactly the same place, the same three-quarters-from-behind pose, the same shoulders, the same head turn toward the shelf, the same arm down holding the same blue plastic shopping basket. Same scale in the frame.

FRAMING: leave a clean band of plain store ceiling across the very top of the image - roughly the top eighth of the frame - free of boxes, banners, signage and lettering, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room; she stays exactly the size she is in the FIRST reference.

The cartons must match the SECOND reference exactly, including its blank red top band: do not print THEXMASGLOW or invent a brand wordmark. CHRISTMAS LIGHT PROJECTOR, REMOTE CONTROL, 45 MIN and 90 MIN must be correctly spelled, sharp and legible. The second reference owns product artwork and carton appearance only; do not copy its hands or background.

LIGHTING AND QUALITY: bright, clean, evenly lit big-box store interior, neutral white balance with no orange and no colour cast, no dark corners. Shot on an iPhone 16 Pro and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp legible printing on every carton, realistic fabric and skin texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own cartons and banner.
````

#### Video prompt — `clips/v5_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on
**Job** - `509c4235-a939-48ba-a4da-c96809f3f689`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_165752_509c4235-a939-48ba-a4da-c96809f3f689.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v5_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_5_assets/starting_frames/v5_c01_g1.png` · Higgsfield media `7ff54a17-55d7-4423-9cc7-71d4f58ceded`

````text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by a friend standing a few steps behind the woman — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in; all distance changes happen because the woman physically moves, never the lens.

Start frame: a young woman in a cream knit sweater and American-flag pajama pants stands in a bright store aisle holding a blue shopping basket, facing the shelf stacked with the green UBU CHRISTMAS LIGHT PROJECTOR product boxes.

ACTION TIMELINE:
0.0–1.0s — She spots the boxes on the shelf, freezes for a split second, then screams with real excitement: "No way — they actually have it!" Her whole body reacts, shoulders jumping.
1.0–2.0s — She lets the blue shopping basket drop straight out of her hand — it hits the store floor with a loud plastic clatter and tips over — as she spins around to the friend filming, one hand flying to her mouth, eyes huge, pure disbelief on her face.
2.0–3.5s — She whips back around and runs the few steps to the shelf, sweater flapping, shoes squeaking on the store floor, the camera staying put and letting her get smaller toward the shelf.
3.5–5.0s — She grabs one UBU CHRISTMAS LIGHT PROJECTOR box off the shelf with both hands, hugs it to her chest, and bounces on her feet laughing, extremely happy, turning halfway back toward the camera to show it. End frame: her hugging the box, beaming.

AUDIO: her real voice, lip-synced — the excited scream and line, then breathless laughing; the loud clatter of the dropped basket; running footsteps; bright store ambience with distant murmur and faint checkout beeps. NO music, no narration.

REALISM — HARD RULES: she keeps exactly the same face, hair, sweater and outfit as the start frame the whole clip. The shelf and every product box stay pixel-faithful to the start frame — same artwork, logo, colors, spelling, text rigid and never warping. The store background stays identical. Real phone-camera look, slight sensor noise, mild motion blur on the run, no cinematic bokeh, no text overlays, no watermark.
````

**Other takes of C01 on disk (2)**

#### Image prompt — `references/v5_c01_r1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `f97d7572-0d90-4688-af6e-2555fe14ddb7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_173926_f97d7572-0d90-4688-af6e-2555fe14ddb7.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `MERRYGLOWUSA - LED CURTAIN LIGHTS/content/video_9_assets/starting_frames/v9_c01_g1.png` · Higgsfield media `1d8b4b34-7ef9-4002-ae4c-7d0d88cbf71e`
- @Image 2: `content/video_5_assets/references/v5_c01_r2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

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

#### Image prompt — `references/v5_c01_r2.png`

**Settings** - gpt_image_2 · 3:4 · 2k · medium · 1744×2336
**Job** - `6893e2d6-7e81-4606-af09-7d26402ca75e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_002130_6893e2d6-7e81-4606-af09-7d26402ca75e.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_5_assets/references/v5_c01_r2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`
- @Image 2: uploaded file, not on the drive · Higgsfield media `c31fb944-cddc-4b14-a4f8-be52c9061c41`

````text
Create a premium retail packaging concept for a Christmas light projector.

REFERENCE ROLES:
- Image 1 owns the PACKAGE FORMAT, CAMERA, PRESENTATION, MATERIALS, and FESTIVE RETAIL DESIGN LANGUAGE only.
- Image 2 owns the NEW PRODUCT GEOMETRY only. Reproduce that exact projector: a compact matte-white horizontal cylindrical body, rounded rear, large black circular slatted front grille, central blue glass projection lens, supported by a white U-shaped pivot bracket on a round white pedestal base. A slim black remote belongs beside it. Ignore Image 2's room, table, cropped timer graphics, and all background text.

PACKSHOT:
One tall upright rigid rectangular cardboard carton with a square footprint and crisp edges, approximately 1:1.6 proportions, closed tuck-top, absolutely no transparent window. Eye-level straight-on studio photograph with a very slight three-quarter view showing the front panel and a narrow sliver of the right side. Two natural adult hands grip the lower left and lower right sides, wrists cropped. Plain light-grey seamless backdrop, soft even studio lighting, soft contact shadow. Vertical edges perfectly straight and parallel. No fisheye. The carton fills the frame like Image 1.

DIRECTION 1 — HERITAGE FESTIVE GREEN:
Keep the winning visual language of Image 1: deep forest-green carton, dark cranberry-red band across the top, thin metallic-gold foil borders, elegant cream serif typography, restrained gold snowflakes, tiny stars, and a fine gold winter-village skyline along the bottom. In the center, show a clean accurate printed render of the NEW projector from Image 2 at a flattering three-quarter angle with its black front grille and blue lens clearly visible; place the slim black remote beside it. Add a subtle warm red-and-gold projected-light burst behind the product, with small Christmas trees and snowflakes emerging from the beam. Do not copy the old projector shown on Image 1.

TEXT:
Leave the small brand plaque on the red top band blank—no invented brand name.
Large front headline, spelled exactly: "CHRISTMAS LIGHT PROJECTOR"
Bottom feature line, spelled exactly: "REMOTE CONTROL   |   45 MIN   |   90 MIN"

Premium believable printed cardboard, commercial product photography, sharp legible packaging, physically plausible folds and seams. No window, no cutout, no open lid, no duplicate product, no camera/security-device appearance, no extra lens, no all-white front face, no gibberish, no misspelled text, no floating accessories.
````

### C02 — Hands on the MerryGlowUSA box

**In the cut:** `starting_frames/v5_c02_g1.png` → `clips/v5_c02_g1.mp4`

#### Image prompt — `starting_frames/v5_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `1d144c78-ecdc-411b-906d-0f263935b57e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_152018_1d144c78-ecdc-411b-906d-0f263935b57e.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_3_assets/starting_frames/v3_c02_g1.png` · Higgsfield media `ef120f6b-b2f6-414a-af8f-0f9197f667de`
- @Image 2: `content/video_5_assets/references/v5_c01_r2.png` · Higgsfield media `4f6cc9e8-b293-48d9-bd79-d9f7a4fa4919`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Replace the FIRST reference's carton with OUR UBU product box exactly as it appears in the SECOND attached reference: a tall upright rectangular tuck-top carton with forest green body, a blank dark-red band across the top bordered in gold, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold-and-red star-and-tree burst over a printed render of a white cylindrical projector in a white U-shaped pivoting bracket on a round flat white base, a black circular slatted front grille with a central glass lens, a slim black remote printed beside it, gold village skyline along the bottom, and the bottom labels REMOTE CONTROL, 45 MIN, 90 MIN, no transparent window. Preserve the tilted projector ILLUSTRATION printed on the box exactly; it is artwork only. The physical projector is concealed in the closed carton in this starting frame. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only the product carton, the table and the background; keep the hands and pose.

FIRST - THE HANDS. A woman's hands, about 35, with medium golden-brown skin and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a warm taupe cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a spacious festive American dining room with soft dove-grey walls, honey-oak shelving, a rectangular bronze mirror, a pale stone fireplace with forest-green stockings and a tall Christmas tree with burgundy glass ornaments, ivory ribbons and warm-white lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The red band must remain BLANK, exactly as on the SECOND attached reference. No THEXMASGLOW wordmark, no invented UBU wordmark, no brand name added anywhere on the carton. Preserve the exact headline and bottom labels from the SECOND reference, sharp and legible.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, box placement, hand positions and camera. @Image 2 owns the UBU carton geometry and product identity. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

#### Video prompt — `clips/v5_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `72e57310-1c9a-42e7-9128-221fe8ba70f7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192311_72e57310-1c9a-42e7-9128-221fe8ba70f7.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v5_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_5_assets/starting_frames/v5_c02_g1.png` · Higgsfield media `1d144c78-ecdc-411b-906d-0f263935b57e`
- image ref 1: `content/video_5_assets/starting_frames/v5_c03_g1.png` · Higgsfield media `4101c330-1b9c-4116-9e6e-246ae3a4434e`

````text
STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing UBU carton. Keep the blank dark-red top band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and black remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls frame 0.0s, the exact printed box, hands, table, room, props and light. @Image 1 is the approved C03 image and supplies ONLY the actual upright projector design and orientation, not its kitchen or hands. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a blank dark red band across the top, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white cylindrical projector in a white U-shaped bracket on a round base, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: the exact larger matte-white upright CYLINDER shown in @Image 1, retaining its full physical size and proportions, in its white U-shaped bracket on a flat round white base. The cylinder axis is VERTICAL, lens facing straight UP at the ceiling. Its flat circular black slatted top face surrounds a central blue lens. The top face is BLACK and stays black for every frame. The cylinder is locked upright relative to its bracket throughout the lift; never inclined on the mount, never copied from the angled illustration on the carton. Round base horizontal. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a warm taupe cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge fills the frame. The lit cream candle, fir sprigs, white berries, gold and pearl-white baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, the supplied festive dining room with soft dove-grey walls, honey-oak shelving, a rectangular bronze mirror, a pale stone fireplace with forest-green stockings and a tall Christmas tree with warm-white lights, burgundy glass ornaments and ivory ribbons. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK slatted circular top face and central blue lens visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the warm ivory limestone dining table with subtle pale-grey fossil markings, a honed matte surface and a square edge, lid flaps folded back. The printed front artwork, candle, fir, berries, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

### C03 — Larger upright projector

**In the cut:** `starting_frames/v5_c03_g1.png` → `clips/v5_c03_g1.mp4`

#### Image prompt — `starting_frames/v5_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `4101c330-1b9c-4116-9e6e-246ae3a4434e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153822_4101c330-1b9c-4116-9e6e-246ae3a4434e.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `0b51a9d5-141b-4052-a50b-62619fc01123`
- @Image 2: `content/video_5_assets/starting_frames/v5_c02_g1.png` · Higgsfield media `1d144c78-ecdc-411b-906d-0f263935b57e`

````text
Create the next UBU C3 photograph using @Image 1 for the upright product design, kitchen composition and camera, and @Image 2 for the real product SCALE relative to its carton and adult hands, the skin and sweater. Make the physical projector appreciably BIGGER than @Image 1 so it matches the product that fits inside the carton in @Image 2. Use the new kitchen and materials below. Keep the cylinder perfectly upright, lens pointing straight UP.

KEEP THE COMPOSITION FROM @Image 1: the camera position, camera height, lens, distance, vertical 9:16 crop, the general two-handed supporting pose, central product placement and forearm entry points. Enlarge the complete projector about 40 percent relative to the adult hands and picture; adapt finger contacts naturally to the larger device, keeping anatomy and hand size realistic.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 35, with medium golden-brown skin and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a warm taupe cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same warm taupe cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the complete upright projector, from the top black lens panel to the bottom round base, occupies about 42 percent of the full image height. Base diameter occupies about 30 percent of image width. A substantial real device held in two adult hands, not a miniature. Its actual overall height is about 80-85 percent of the tall carton in @Image 2, allowing realistic packaging clearance. Enlarge all product components together, preserve their original proportions and ordinary adult hand dimensions. Keep visible air beneath the base and counter. Both hands support the device firmly and naturally.

THE PRODUCT - the same UBU matte-white cylindrical projector barrel in its white U-shaped pivot bracket on a round flat white base. USER-CONFIRMED ORIENTATION: THE CYLINDER STANDS VERTICALLY UPRIGHT, WITH THE BLACK LENS/GRILLE FACE ON TOP POINTING STRAIGHT UP AT THE CEILING. Retain @Image 1's already confirmed upright lens-UP orientation without any tilt. Its long axis is vertical and PERPENDICULAR to the horizontal circular base, like an upright can standing on end. The circular black slatted lens face is a HORIZONTAL TOP FACE, parallel to the round base, visible from above as an ellipse at this existing camera height; the central blue glass lens looks upward. The solid white barrel extends straight down below that top face, sitting vertically between the two upright support arms. The round base remains flat and horizontal, and the support arms remain vertical. The projector does NOT point at the camera, does NOT lie sideways, and does NOT lean diagonally. No forward-facing black front disc: the black disc is now on TOP. Preserve the exact existing cylinder shell, horizontal ventilation slats across the black lens panel, blue glass lens, side pivot, U bracket and circular base; do not replace it with the older dome projector or four-legged stand. @Image 2 supplies product materials and component identity only; IGNORE its printed tilted pose. The device has the same design and upright configuration as @Image 1.

THE COUNTER - a white marble counter with delicate pale-grey veins, a straight eased edge and matte surface. Same shape, position and amount visible as @Image 1.

THE KITCHEN - a sharply resolved traditional Christmas kitchen: slate-blue shaker cabinets with aged brass pulls, creamy white tiles, dark-walnut open shelves, a cream enamel range, forest-green velvet ribbons, warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree in the far corner. Balanced soft window fill and warm interior light, realistic iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns camera, layout and upright product geometry only, not its undersized scale. @Image 2 owns the adult hand appearance, sweater, material realism and physical carton-to-projector scale. Its printed tilted product illustration must NEVER set the real projector orientation. The physical unit is larger, perfectly vertical, lens UP. All parts in natural crisp iPhone deep focus, no portrait mode, bokeh or blur.
````

#### Video prompt — `clips/v5_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `372279eb-f186-466f-9281-d07cf5c5589a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192312_372279eb-f186-466f-9281-d07cf5c5589a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v5_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_5_assets/starting_frames/v5_c03_g1.png` · Higgsfield media `4101c330-1b9c-4116-9e6e-246ae3a4434e`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a white marble counter with delicate pale-grey veins and a straight eased edge, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - the exact matte-white upright CYLINDER in the start image, in its white U-shaped bracket on a flat round white base. Cylinder axis VERTICAL, lens pointing straight UP at the ceiling. Its black slatted circular top face surrounds the central blue lens. The top face is BLACK and stays black for every frame. The cylinder stays locked upright within the bracket throughout; no inclination on its mount. No front-facing lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in warm taupe cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a white marble counter with delicate pale-grey veins and a straight eased edge; behind it slate-blue shaker cabinets with aged brass pulls, creamy white tiles, dark-walnut shelves, a cream enamel range, warm under-cabinet lights, evergreen garland with red berries and fairy lights, and the small Christmas tree. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the white marble counter with delicate pale-grey veins and a straight eased edge, matte rather than mirror-polished.

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

**In the cut:** `starting_frames/v5_c04_g1.png`, `references/v5_c04_r1.png` → `clips/v5_c04_g1.mp4`

#### Image prompt — `starting_frames/v5_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `cb3b1593-094e-46ca-8caf-f3d6c3019202`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153753_cb3b1593-094e-46ca-8caf-f3d6c3019202.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_5_assets/references/v5_c04_r1.png` · Higgsfield media `fbbdcee4-579b-486d-bc0a-2a99ea8e968a`
- @Image 2: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `11720edc-b38f-48f6-bc92-8278407f2181`

````text
Create the LIGHTS-ON STARTING FRAME by editing @Image 1, the existing matching lights-off bedroom reference. Keep the photographer in the EXACT SAME physical place, at the same eye height, with the same lens and standing location as @Image 1, but ROTATE THE PHONE TO THE RIGHT by roughly 30 degrees. The viewing direction and framing MUST change; the camera's physical location must not. @Image 1 owns all geometry. @Image 2 is the previous lights-on image and supplies ONLY the brightness, realistic photographic look and red-sleeved hand holding the black UBU remote; it must NOT control camera position or framing. Changes are only: turn the phone's view RIGHT from that stationary location, turn room lights on, turn the wall projection completely off, and add the remote hand.

KEEP THE ROOM FROM @Image 1: soft dove-grey plaster walls and ceiling, dark walnut floor, ivory woven rug, king-size honey-oak bed with a crisp white cotton quilt and deep-green-and-gold tartan runner, two forest-green cushions and one central burgundy velvet cushion, white pillows, honey-oak nightstands and bronze lamps, ivory linen curtains behind the headboard on the BACK wall, real fir garland with tiny warm lights and burgundy bows around the headboard, tall Christmas tree in the back-right corner, burgundy upholstered bench at the foot of the bed with a cream woven throw over its right side. Same spatial layout and distances. The LEFT wall is an uninterrupted plain warm-greige wall with no actual windows. It remains the same solid flat wall.

CAMERA LOCATION VERSUS VIEW DIRECTION - CRITICAL CORRECTION: the photographer's feet and the camera lens centre stay exactly at @Image 1's viewing point, to the right of the foot of the bed, at the same height. From there, turn the phone RIGHT about 30 degrees, with no sideways movement, no walking and no zoom. The starting image looks more toward the bed and its headboard/back curtains; the bed and upholstered foot-bench become the central subjects. The left projection wall recedes diagonally along only the LEFT 20-30 percent of the starting image, not across the middle. The back-left room corner shifts clearly LEFTWARD in the picture compared with @Image 1. Show more of the back wall, headboard and right-hand part of the bedroom. The perspective still comes from the same off-centre spot right of the bed's foot, never the central doorway view. Do not preserve @Image 1's exact crop or orientation: that was the previous mistake. Do not move any furniture or mirror the room. This frame is the START BEFORE a future LEFTWARD PAN: the camera will later rotate left from this fixed spot to arrive at @Image 1's reveal framing. Capture the right-facing starting orientation now.

LIGHTS ARE NOW ON: the ceiling-fan light and both bedside lamps illuminate the same room with clean warm light. Keep the fairy lights on the headboard and tree. Match the well-exposed natural warm interior-photo look of @Image 2, while preserving @Image 1's room geometry and applying the new right-facing camera orientation. Fine duvet, rug and wood details stay crisp; do not make the room dark.

THE LEFT WALL BEFORE ACTIVATION: completely REMOVE the entire projected Christmas scene AND every projected arch, window frame, mullion, sill, frost edge and glow from @Image 1. The same wall is now one continuous blank smooth warm-ivory wall, with its real baseboard and ceiling junction in their original positions. No actual window exists on this left wall. No remnants, embossed arches, ghost outlines, rectangular screen, poster or scenery. The real white curtains on the BACK wall remain.

REMOTE HAND: add the same adult right hand and red pajama sleeve visible in @Image 2, entering naturally from the lower right and holding the exact same slim black UBU remote at a comfortable arm's length. The thumb is poised over the central OK/play control before pressing; correct five-finger anatomy, black direction pad, red power button, matching remote scale. Keep the hand low in the right foreground, leaving the blank left wall and its corner unobstructed. It must read as the POV of the person standing at @Image 1's fixed location, not a second person or floating hand. No product box.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
````

#### Image prompt — `references/v5_c04_r1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `fbbdcee4-579b-486d-bc0a-2a99ea8e968a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_151950_fbbdcee4-579b-486d-bc0a-2a99ea8e968a.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_3_assets/references/v3_c04_r1.png` · Higgsfield media `d5c01f65-2395-4799-82cc-d479c50f61bf`
- @Image 2: `content/video_3_assets/starting_frames/v3_c05_g1.png` · Higgsfield media `4ac06232-8065-4c69-a050-491de9e9538f`

````text
Create one vertical 9:16 LIGHTS-OFF REFERENCE FRAME for a new UBU Christmas projector video. @Image 1 owns the exact room layout, camera position, viewing direction and furniture arrangement; change only the room materials/decor listed below and improve the projected view. @Image 2 supplies the Christmas-window theme only, never its blur, painterly scenery or protruding window geometry. Create a real handheld iPhone photograph of a real bedroom with a luminous flat wall projection.

KEEP THE ROOM LAYOUT FROM @Image 1 but use these new materials: soft dove-grey plaster walls and ceiling, dark walnut floor, ivory woven rug, king-size honey-oak bed with a crisp white cotton quilt and deep-green-and-gold tartan runner, two forest-green cushions and one central burgundy velvet cushion, white pillows, honey-oak nightstands and bronze lamps, ivory linen curtains behind the headboard on the BACK wall, real fir garland with tiny warm lights and burgundy bows around the headboard, tall Christmas tree in the back-right corner, burgundy upholstered bench at the foot of the bed with a cream woven throw over its right side. Same spatial layout and distances. The LEFT wall remains a solid flat wall with no actual windows.

CAMERA LOCATION: preserve @Image 1's existing viewpoint, standing to the right of the foot of the bed and looking diagonally LEFT toward the long wall. The enormous projected window view fills the left and central 70 percent of the picture; the familiar bed, runner and a sliver of the garland-wrapped headboard appear along the lower-right and right edge. Correct consistent perspective, no mirrored layout, no moving walls, no relocated bed. This will be the reveal orientation; the matching lights-on frame will be made by rotating the phone RIGHT from this same physical standing point. No people or hands visible.

LIGHTS ARE NOW OFF: the ceiling-fan light and both bedside lamps are off, warm bulbs not glowing. Keep only tiny Christmas garland/tree pin lights and the spectacular wall projection as illumination. Expose expertly for the projection while keeping real bedding folds and room silhouettes readable; beautifully subtle icy blue and golden light spill on the near cream duvet and pale floor.

THE PAYOFF ON THE LEFT WALL: one huge brilliant, high-contrast projection of an elegant grand arched window with warm timber mullions. Frame and scenery are projected onto the SAME FLAT WALL, with no structural opening. Through the panes is ONE continuous photographic landscape: a breathtaking REALISTIC old Quebec Christmas town above a frozen river: richly detailed stone townhouses with steep snowy roofs, warm golden windows and visible smoking chimneys lining a cobbled Christmas street, a grand historic copper-roofed chateau on the hill, one magnificent illuminated Christmas tree beside a small festive market, glowing street lanterns, and a beautiful old stone bridge over the partly frozen river. Snow-laden pines and distant rolling snowy hills give the town enormous photographic depth. Emerald-and-violet aurora curtains stretch across the clear deep-blue winter sky. Santa's small sleigh and a clear team of reindeer are visible in the upper sky. Distinct falling snowflakes, believable natural snow surfaces, detailed weathered stone and warm holiday lights. An expansive photographic landscape with a few legible hero buildings rather than dense miniature CGI clutter. Every pane shows its proper part of the same continuous landscape, with no repeated panels. Opaque-looking, crisp dark mullions form an uninterrupted foreground layer all the way down to the projected sill. Scenery and snowy branches remain BEHIND every mullion, never overlapping or interrupting its base.

PROJECTION PHYSICS: substantially stronger, richer and less transparent than @Image 1. Dense luminous color and decisive contrast cover the wall, no ghostly double exposure and no pale wall color washing through the scenic image. Deep dark window-frame shapes, brilliant controlled highlights without bloom, clear photographic details. The room is dark enough for a vivid high-output projection. Wall texture is only a barely perceptible surface grain, not visible through the buildings. All projected geometry is FLAT on the wall, follows one coherent perspective, and stays bounded by the real ceiling junction and baseboard. Physically believable blue and gold light spill on actual bedding; natural room shadows, no beam haze. Vivid projection while retaining real-room photographic credibility.

Extremely high-quality iPhone 16 Pro wide-lens photo, crisp edge-to-edge deep focus on room and projected scene, precise microdetail, perfect lighting, natural straight verticals, no fisheye, no bokeh, no blur, no motion blur, no hazy bloom, no grain, no CGI bedroom, no text, captions, watermark or UI.
````

#### Video prompt — `clips/v5_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `420693b7-22e8-4fe7-b641-d825753c063e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192312_420693b7-22e8-4fe7-b641-d825753c063e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v5_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_5_assets/starting_frames/v5_c04_g1.png` · Higgsfield media `cb3b1593-094e-46ca-8caf-f3d6c3019202`
- image ref 1: `content/video_5_assets/references/v5_c04_r1.png` · Higgsfield media `fbbdcee4-579b-486d-bc0a-2a99ea8e968a`
- video ref 1: `content/video_1_assets/clips/v1_c04_g1.mp4` · Higgsfield media `b3902899-d75c-4875-ae1e-3c0e4fbec222`

````text
One continuous 5-second POV handheld iPhone video. The attached start image is the EXACT first frame and owns the bedroom geometry, bed, bench, rug, red sleeve, hand and black remote. @Image 1 supplies the Christmas projection artwork for the LEFT wall. Its bedroom perspective is not an endpoint to morph into. Keep the physical room of the starting frame throughout. @Video 1 is the approved Video 1 C04 clip, used as a MOTION reference only: closely copy its quick thumb press, natural lowering of the remote hand and subsequent leftward handheld camera pan. Do not copy its different bedroom, lower image quality, text overlays or sound.

0.0-0.2s: from the supplied remote position the wrist makes a small natural forward/up adjustment and the thumb visibly depresses the play/OK button ONCE. Match the reference's immediate decisive press, not a long aiming gesture.
At exactly the button depression, around 0.2s: the ceiling light and bedside lamps switch OFF instantly, and the luminous Christmas-window projection switches ON on the LEFT wall in the SAME moment. No delayed reveal and no gradual fade. Existing Christmas fairy lights remain dimly lit.
0.2-1.6s: the hand relaxes and naturally lowers the still-gripped remote down toward the lower right and out of view, following @Video 1's hand movement. No waving, no tossing the remote, no second press. Simultaneously begin a gentle continuous pan LEFT at normal handheld-phone pace.
1.6-4.2s: continue rotating the phone LEFT from the same standing spot until the left wall projection dominates the view, showing @Image 1's artwork from the actual camera's viewpoint. The bed shifts toward the right edge as a result of this rotation. No walking forward, no sideways camera translation, no zoom and no cut. Natural tiny hand tremor, coherent room perspective.
4.2-5.0s: settle into the spectacular left-wall view with slight natural handheld drift.

ROOM RIGIDITY: Keep the starting room a single solid three-dimensional space. Its flat left wall, straight ceiling junction, rear curtain wall and floor remain rigidly connected at fixed angles. The camera turns within that room; walls never rotate, bend, expand, slide or change shape. The bench, bed, rug and ceiling fan keep their original dimensions and positions. Preserve the deep-green-and-gold tartan bed runner and ivory rug from the starting image; do not borrow the red runner or green rug from @Video 1. The sole tall Christmas tree remains to the RIGHT of the bed. The projection is flat light on the existing left wall, not an opening or new room. The window artwork obeys that wall's perspective and remains fixed on it. Use @Image 1 for artwork content only, never its room outline or furniture placement.

The wall projection must be a visibly ANIMATED Christmas scene, never a frozen still. Preserve @Image 1's window framing and continuous snowy old Quebec Christmas town, illuminated houses, trees, river, mountains, aurora and sleigh. From the instant the projection appears through the final frame, soft smoke continuously curls upward and drifts from multiple house chimneys, Santa's sleigh and pulling reindeer visibly travel across the sky with gently cycling reindeer legs, and luminous aurora curtains continuously ripple and flow. Fine snow falls within the projected scene; river reflections shimmer gently. All this motion occurs INSIDE the projection. The projected window frame remains fixed to the real wall. The entire projection does not slide, breathe, scale or float. Preserve the actual bedroom walls, bedding and furniture as solid stationary physical objects. Projection light naturally spills across the room and duvet after the click.

Sharp realistic iPhone footage, clean low-light exposure and detailed moving scenery. Exactly one visible hand holding one remote, natural thumb anatomy. No new person, no real window opening in the wall, no overlay text, no watermarks, no scene transition, no reversed pan, no music. Only quiet bedroom ambience, subtle sleeve movement and the single dry remote click. Ignore all audio in @Video 1. (no BGM). No subtitles.
````

### C05 — Christmas view from bed

**In the cut:** `starting_frames/v5_c05_g1.png` → `clips/v5_c05_g1.mp4`

#### Image prompt — `starting_frames/v5_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `bfca2ec6-d4aa-4aa4-9724-ad9e41653a27`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_153752_bfca2ec6-d4aa-4aa4-9724-ad9e41653a27.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_3_assets/starting_frames/v3_c05_g1.png` · Higgsfield media `4ac06232-8065-4c69-a050-491de9e9538f`
- @Image 2: `content/video_5_assets/references/v5_c04_r1.png` · Higgsfield media `fbbdcee4-579b-486d-bc0a-2a99ea8e968a`

````text
Create a new hyperrealistic low-light iPhone photograph for UBU C5. @Image 1 supplies ONLY the low bed-level camera position, wide full-wall composition and continuous foreground window-frame layout. Do NOT copy its blurry rendering, painterly scenery, stone texture or fake CGI surfaces. @Image 2 supplies the new photographic Christmas landscape and rich opaque-looking projection. Render the entire image afresh in crisp native detail. Real bedroom materials: white linen duvet with resolved stitched seams and green-and-gold plaid blanket edge, a simple low honey-oak cabinet, a modest real potted fir, soft dove-grey wall and dark walnut floor. Preserve the believable low lying-in-bed perspective from @Image 1. Use elegant warm timber Gothic projected arches with slender mullions. ALL window arches, vertical posts and bottom sill form one continuous opaque foreground layer over the scenery. Every post runs uninterrupted from the arch to a clear connection with the sill. Snow, trees, roofs and lights are behind the frame and can NEVER overlap, erase or interrupt a post at its bottom. The entire frame and scenery are FLAT projected light on the solid wall, never actual structural windows or protruding architecture.

POV lying comfortably in bed, camera at pillow height, no visible person, face or hands. Real softly folded duvet fills the lower foreground with exceptionally clear weave, seams and natural weight. The broad wall ahead is covered edge to edge and ceiling-junction to baseboard by one seamless luminous panorama seen through tall elegant Gothic timber window arches. BOTH window architecture and landscape are projected light on the plain wall, not actual openings. ALL visible wall is covered, including both sides. The panorama continues beyond the crop with room for a later LEFTWARD PAN; no blank strip or cropped-off projection rectangle. The real ceiling junction, room corner and baseboard establish the physical room. Main lights off, believable controlled blue and golden reflected light on the actual duvet and cabinet. One coherent flat wall perspective, straight window posts, no warped arches. The distant landscape has believable photographic depth inside the projected panes but does not extend physically into the room.

Beyond the coherent projected arches is ONE continuous spectacular Christmas view: a breathtaking REALISTIC old Quebec Christmas town above a frozen river: richly detailed stone townhouses with steep snowy roofs, warm golden windows and visible smoking chimneys lining a cobbled Christmas street, a grand historic copper-roofed chateau on the hill, one magnificent illuminated Christmas tree beside a small festive market, glowing street lanterns, and a beautiful old stone bridge over the partly frozen river. Snow-laden pines and distant rolling snowy hills give the town enormous photographic depth. Emerald-and-violet aurora curtains stretch across the clear deep-blue winter sky. Santa's small sleigh and a clear team of reindeer are visible in the upper sky. Distinct falling snowflakes, believable natural snow surfaces, detailed weathered stone and warm holiday lights. An expansive photographic landscape with a few legible hero buildings rather than dense miniature CGI clutter. The scene must be photorealistic location photography, not a fairytale painting, video-game environment, miniature model or 3D illustration. Clearly separate near snow-laden fir branches, the legible hero village buildings and immense distant mountains. Steam/smoke visibly rises above the chimneys, the small Santa sleigh and its reindeer are already present, and the bright aurora is already present. Every pane shows its proper portion of the same continuous view. Never repeat identical views in adjacent panes. Rich dense luminous color, brilliant but controlled Christmas lights, deep blue snowy shadows and clear natural texture; not translucent or washed out. Window posts remain dark solid continuous shapes in front of all outdoor objects, joined to the sill. Keep real-room light spill subtle and physically plausible.

CRITICAL IMAGE QUALITY: crisp, clean native-2K iPhone photograph with excellent low-light exposure and deep focus across foreground bedding, furniture, wall and the projected scenery. Clearly resolved duvet weave and seams, wood grain, plant leaves, stone tracery edges, individual rooflines, window mullions, snow on branches, distant palace towers and chimney outlines. High microcontrast without oversharpened halos. Render every visible surface freshly and precisely; do not copy softened or smeared pixels from the references. No shallow depth of field, no soft duvet, no haze, no fog over the image, no glowing bloom hiding detail, no gaussian blur, no motion blur, no muddy shadows, no painterly smearing, no grain, no bokeh, no fisheye or barrel distortion. Maintain natural photographic light and texture, not a plastic CGI render. No text, captions, watermarks or playback icons.
````

#### Video prompt — `clips/v5_c05_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `f5494f27-03ee-49e1-b653-70553062483b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260922_192313_f5494f27-03ee-49e1-b653-70553062483b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v5_c05_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_5_assets/starting_frames/v5_c05_g1.png` · Higgsfield media `bfca2ec6-d4aa-4aa4-9724-ad9e41653a27`
- image ref 1: `content/video_5_assets/starting_frames/v5_c05_g1.png` · Higgsfield media `bfca2ec6-d4aa-4aa4-9724-ad9e41653a27`

````text
A four-second handheld first-person RIGHT PAN from bed, beginning at exactly the supplied photograph. The lens is at pillow height above the white linen duvet. This is a phone recording of a Christmas projection covering a bedroom wall.

Immediately turn the recording camera to the RIGHT through a broad 35-45 degree arc over the full four seconds, in one continuous, clearly visible sweep. By 1.5 seconds the cabinet, potted fir and the starting leftmost window arch have completely left the left edge. Keep turning until the window arch that begins at the far RIGHT of the starting photograph is near the MIDDLE of the view, revealing more of the projected wall beyond the original right edge. The entire bedroom view changes naturally with this turn: the duvet, baseboard, ceiling edge and wall-fixed window posts all travel LEFT across the recording together. This is a substantial rightward turn of the recording phone, not a tiny drift. A relaxed wrist movement with slight hand wobble, constant lens, no zoom or sideways travel. Only the room and bedding are visible; the recording person, their hands and phone stay behind the lens.

The projected scene plays like an animated Christmas illustration on a screen fixed to the wall. The Gothic window borders, village buildings, stone waterfront townhouses and mountains remain stationary on that screen. Houses do not change window panes. The illustration has no panning camera of its own.

Animate these subjects clearly from beginning to end: rolling plumes of white smoke rise and curl from several fixed chimneys; Santa's sleigh travels across the sky behind running reindeer, passing the stationary moon; broad emerald aurora ribbons wave and ripple above stationary mountain peaks. Falling snow and rippling river reflections add continuous movement. Window posts stay intact in front of all these moving subjects. Keep the rest of the scene still relative to the wall while the recording camera turns.

One uncut realistic iPhone night shot, sharp room textures and luminous projection, natural room ambience. No visible devices, cuts, captions or music.
````
