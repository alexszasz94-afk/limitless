# Video 24 - image archive

**C01 hook (2026-09-26):** clip `g3` APPROVED by Daniel. Earlier: clips g1 and g2 rejected, re-roll g3 CLIP FOR REVIEW. Frame: start frame generated (one generation), on the board as FRAME FOR REVIEW.

**Upscaled 2026-09-26:** all seven approved clips (C01 g3, C02–C07 g1) upscaled with Preset AIGC - see `## Upscales`.

**Current status (2026-09-25):** B-roll start frames C02–C07 plus the C05 room reference (r1) and its empty-room edit (r2) generated (one generation each), saved and on the board as FRAME FOR REVIEW. Hook (C01) not chosen yet. Clips round 1 generated 2026-09-25 (one take each), on the board as CLIP FOR REVIEW.

**Settings:** Higgsfield `gpt_image_2_5`; variant `sunburst`; resolution `2k`; quality `medium`; aspect_ratio `9:16`; count `1` per image.

## Reusable blocks
Every prompt is the video 23 verified-record prompt of the same slot, pasted verbatim with only the physically different nouns replaced (English Tudor-revival set, limed oak, cranberry / forest green / gold; northern-lights Christmas village projection), same geometry references and settings. Daniel's request for this video (2026-09-25): C05 room reference, C06 and C07 just a little less cinematic, and the projection visible on the wooden frames too. Two blocks implement it, pasted identically into r1, C06 and C07:

**Wood block** (appended after the existing "THE WOODEN FRAMES CARRY THE PICTURE TOO" sentence):
````text
THIS IS THE KEY CORRECTION FOR THIS SET: the exposed wood must visibly carry the picture. Every exposed piece of limed oak in shot - each truss, rafter, purlin, beam, brace, half-timber post and rail, window mullion, frame and glazing bar, the door and doorway casings, the skirting and the mantel - is painted over by the projection in the same full colour as the plaster beside it: the village, garlands, aurora, stars and snowflakes run straight across the face of the wood and bend at each edge, the wood grain showing faintly through the projected colour. No beam, frame or casing stays as a dark bare wooden stripe or an unlit outline. Only the window GLASS stays the dark night outside.
````

**Less-cinematic block** (replaces the v23 "NATURAL, LESS CINEMATIC LOOK" paragraph):
````text
NATURAL, LESS CINEMATIC LOOK - one small notch more natural than a polished film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster, a painting or an advert. True-to-life colour and contrast exactly as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting, no heightened fantasy glow on the children, and no storybook-illustration or oil-painting finish on the projection. The projection is still dense, bright and colourful, but its colour sits a touch closer to real life - rich, not neon - and it reads as the real light of a home Christmas projector falling on real walls: the plaster texture and wood grain show faintly through it, and the shadows keep a little more ordinary room detail, with the furniture, rug and floor clearly readable in the soft spill.
````

All submitted prompts were checked byte-identical against the Higgsfield job records.

## C02 - Hands on the box
**Frame:** `starting_frames/v24_c02_g1.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`
**Lineage:** Reused from v23 C02 - changed: hands (fair, freckled), sweater (cranberry-red cable-knit), table (limed-oak refectory), background (Tudor-revival dining room), bauble colours.

### Image prompt
````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 30, with fair skin with a light dusting of freckles and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive English Tudor-revival dining room with cream lime-plaster walls framed by pale limed-oak half-timber posts and beams, a black wrought-iron candle chandelier, a carved stone fireplace with cranberry and forest-green knitted stockings, a limed-oak dresser with blue-and-white plates, and a Christmas tree dressed with cranberry-red, forest-green and gold glass baubles and warm white fairy lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few small pinecones, two or three small cranberry and gold glass baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).

## C03 - The projector lifted
**Frame:** `starting_frames/v24_c03_g1.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `03992926-ec39-4527-bb57-1d0443957611`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
- @Image 2: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**Lineage:** Reused from v23 C03 - changed: hands, sweater, counter (pale honed limestone), kitchen finishes (limed-oak Shaker, cream zellige, oak ceiling beams, cranberry range), tree ornaments; @Image 2 = v24 C02.

### Image prompt
````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 30, with fair skin with a light dusting of freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a cranberry-red cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same cranberry-red cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C02 and owns the new woman's hands, sweater, photographic look and full-size carton-to-projector scale; the projector should plausibly fill that carton when unpacked; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).

## C04 - The cable going in
**Frame:** `starting_frames/v24_c04_g1.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `4d260de1-556a-41ac-afe1-a8f708913c72`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`
- @Image 2: `content/video_24_assets/starting_frames/v24_c03_g1.png` · Higgsfield media `03992926-ec39-4527-bb57-1d0443957611`
**Lineage:** Reused from v23 C04 - changed: the same nouns as C03; @Image 2 = v24 C03.

### Image prompt
````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 30, with fair skin with a light dusting of freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C03 and owns the enlarged product's physical dimensions relative to the hands, exact product identity, kitchen finishes, hands, sweater and photographic look; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).

## C05 - The door opens on the room — start frame
**Frame:** `starting_frames/v24_c05_g1.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `afe8c961-388f-423a-9ade-7a7c05b20121`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- @Image 2: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**Lineage:** Reused from v23 C05 - changed: hands/sweater, door (forest-green oak plank door, iron strap hinges, limed-oak casing), wall, exposure colour line; @Image 2 = v24 C02.

### Image prompt
````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the cranberry-red cable-knit wool sleeve and no jewellery, with fair skin with a light dusting of freckles, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a deep forest-green painted oak plank door with black wrought-iron strap hinges, a satin finish and a pale limed-oak surrounding casing, an antique brass round knob and matching brass escutcheon, set in a cream lime-plaster wall. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear door surface visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest-green paint reads clearly as deep green, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).

## C05 F2 - The door opens on the room — room reference
**Frame:** `references/v24_c05_r1.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `85ba004e-383a-478a-88e5-b67066ac8da9`
**References:**
- @Image 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`
**Lineage:** Reused from v23 C05 r1 - changed: children, pyjamas, room (open-timbered GABLED Tudor great hall), door, tree/stockings colours, projection theme (northern-lights village: chimney smoke, aurora, sleigh - chosen so the later clips have lots to move), architecture-fold sentences. Daniel's 2026-09-25 improvements: added the "KEY CORRECTION" wood paragraph (projection must visibly cover every exposed wooden beam, frame and casing) and replaced the NATURAL, LESS CINEMATIC LOOK paragraph with a one-notch-more-natural version.

### Image prompt
````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about six with fair freckled skin and tousled copper-red hair; the girl is of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons. Both children are fully dressed for winter in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height English Tudor-revival Christmas great hall with a high open-timbered GABLED CEILING: two broad cream lime-plaster roof planes rise to a crisp central ridge, crossed by three pale limed-oak king-post trusses with curved braces. Pale limed-oak half-timber posts, rails and diagonal braces divide the cream lime-plaster walls into large panels. A tall carved limestone chimney breast stands on the back wall with a deep stone hearth; a wall of tall leaded casement windows in pale limed-oak mullioned frames occupies the left wall and a wide limed-oak doorway sits on the right. Wide pale oak floorboards, a large deep forest-green velvet chesterfield sectional sofa, a round tan leather ottoman and a soft cream wool rug. Seen from the doorway; the new a deep forest-green painted oak plank door with black wrought-iron strap hinges, a satin finish and a pale limed-oak surrounding casing is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, cranberry-red, forest-green and gold glass baubles, tinsel and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cranberry-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping roof planes and their central ridge remain clearly three-dimensional, meeting at a crisp ridge line. The sleigh and the ceiling picture fold at the ridge and are foreshortened along each slope, running straight across the faces of the three limed-oak trusses and their curved braces, before continuing onto the walls. The tall limestone chimney breast receives a continuous picture with clear folds at its projecting corners. The limed-oak half-timber posts, rails and braces, the mullioned window frames, glazing bars and the doorway frame carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. THIS IS THE KEY CORRECTION FOR THIS SET: the exposed wood must visibly carry the picture. Every exposed piece of limed oak in shot - each truss, rafter, purlin, beam, brace, half-timber post and rail, window mullion, frame and glazing bar, the door and doorway casings, the skirting and the mantel - is painted over by the projection in the same full colour as the plaster beside it: the village, garlands, aurora, stars and snowflakes run straight across the face of the wood and bend at each edge, the wood grain showing faintly through the projected colour. No beam, frame or casing stays as a dark bare wooden stripe or an unlit outline. Only the window GLASS stays the dark night outside. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the soft cream wool rug, the forest-green velvet chesterfield sectional sofa, the round tan leather ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

NATURAL, LESS CINEMATIC LOOK - one small notch more natural than a polished film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster, a painting or an advert. True-to-life colour and contrast exactly as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting, no heightened fantasy glow on the children, and no storybook-illustration or oil-painting finish on the projection. The projection is still dense, bright and colourful, but its colour sits a touch closer to real life - rich, not neon - and it reads as the real light of a home Christmas projector falling on real walls: the plaster texture and wood grain show faintly through it, and the shadows keep a little more ordinary room detail, with the furniture, rug and floor clearly readable in the soft spill.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the grain of the limed-oak half-timbering and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).

## C05 F3 - The door opens on the room — empty-room reference
**Frame:** `references/v24_c05_r2.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `207fb72f-8668-4fad-8a0a-4009eac963dc`
**References:**
- @Image 1: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield media `85ba004e-383a-478a-88e5-b67066ac8da9`
**Lineage:** Reused from v23 C05 r2 - changed: room name and ceiling type only; @Image 1 = v24 r1.

### Image prompt
````text
Edit the supplied image. Reproduce it exactly - the same English Tudor-revival Christmas great hall, the same open-timbered gabled ceiling, the same camera position, framing, lens and lighting, the same furniture, Christmas tree, fireplace, rug and the exact same projected Christmas artwork on the walls and ceiling, pixel for pixel wherever possible. The ONLY change: remove all children completely. The room is empty of people - no children, no adults, no pets. Where the children stood, show the floor, rug and sofa that were behind them, continuing naturally. Keep the projection, colours and sharpness unchanged. No text, no watermark.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).

## C06 - The bed bounce
**Frame:** `starting_frames/v24_c06_g1.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `a36295bc-fdfd-47c2-8bf2-b7b5cd062961`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
- @Image 2: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield media `85ba004e-383a-478a-88e5-b67066ac8da9`
**Lineage:** Reused from v23 C06 - changed: boy, pyjamas, room (SHED-ceiling Tudor bedroom with limed-oak rafters and half-timbering), tree ornaments, projection theme, fold sentences; plus the same two 2026-09-25 improvements as r1 (wood paragraph, less-cinematic paragraph).

### Image prompt
````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same natural low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with fair freckled skin and tousled copper-red hair, fully dressed for winter in a cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama set with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a bright-proportioned English Tudor-revival bedroom with a high SHED CEILING: a single cream lime-plaster plane sloping up from the front of the room to the tall back wall, crossed by pale limed-oak rafters. A pale limed-oak panelled bed with a wide upholstered cream headboard is centred on the flat back wall between two tall leaded casement windows with pale limed-oak mullioned frames and glazing bars, the back wall divided by pale limed-oak half-timber posts and rails, white bedding with a cranberry-red knitted throw, limed-oak bedside chests, wide pale oak floorboards and a soft cream wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and cranberry-red and gold ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The single sloping ceiling plane remains clearly three-dimensional, meeting the walls at crisp lines. The sleigh and the ceiling picture are foreshortened along the slope, run straight across the faces of the limed-oak rafters, and fold at the wall line before continuing down the walls. The flat wall, the limed-oak half-timber posts and rails, the mullioned window frames and glazing bars and the cream headboard carry properly foreshortened portions of the same continuous projection across their faces. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. THIS IS THE KEY CORRECTION FOR THIS SET: the exposed wood must visibly carry the picture. Every exposed piece of limed oak in shot - each truss, rafter, purlin, beam, brace, half-timber post and rail, window mullion, frame and glazing bar, the door and doorway casings, the skirting and the mantel - is painted over by the projection in the same full colour as the plaster beside it: the village, garlands, aurora, stars and snowflakes run straight across the face of the wood and bend at each edge, the wood grain showing faintly through the projected colour. No beam, frame or casing stays as a dark bare wooden stripe or an unlit outline. Only the window GLASS stays the dark night outside. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the soft cream wool rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his cotton pyjama top catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

NATURAL, LESS CINEMATIC LOOK - one small notch more natural than a polished film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster, a painting or an advert. True-to-life colour and contrast exactly as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting, no heightened fantasy glow on the children, and no storybook-illustration or oil-painting finish on the projection. The projection is still dense, bright and colourful, but its colour sits a touch closer to real life - rich, not neon - and it reads as the real light of a home Christmas projector falling on real walls: the plaster texture and wood grain show faintly through it, and the shadows keep a little more ordinary room detail, with the furniture, rug and floor clearly readable in the soft spill.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).

## C07 - The whole Christmas room
**Frame:** `starting_frames/v24_c07_g1.png`
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `e02e1c3d-02cb-4e8d-add1-0d8fccdbe38a`
**References:**
- @Image 1: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
- @Image 2: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield media `85ba004e-383a-478a-88e5-b67066ac8da9`
**Lineage:** Reused from v23 C07 - changed: children, pyjamas, room (VAULTED Tudor family room, limed-oak ridge beam and purlins, Cotswold-stone chimney), tree/stockings colours, projection theme, fold sentences; plus the same two 2026-09-25 improvements as r1.

### Image prompt
````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the children only; this is a different room of the same house, described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons; a boy of about six with fair freckled skin and tousled copper-red hair. Both fully dressed in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height English Tudor-revival Christmas family room with a high VAULTED CEILING: two broad sloping cream lime-plaster planes rising to a crisp central ridge, with one heavy pale limed-oak ridge beam running along it and pale limed-oak purlins crossing each slope. Cream lime-plaster walls. A tall chimney breast of honey-coloured Cotswold stone stands on the back wall with a thick limed-oak beam mantel; a full-height wall of leaded windows in pale limed-oak mullioned frames and glazing bars fills the left wall and a wide limed-oak plank door sits on the right. A herringbone pale oak floor, a large camel-brown velvet sectional sofa, a round deep-green leather ottoman and a soft cream-and-cranberry Persian-style wool rug. A different room from @Image 2 - not the same living room - seen from the middle of the family room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, cranberry-red, forest-green and gold glass baubles, tinsel and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cranberry-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping plaster planes, the limed-oak ridge beam and the purlins remain clearly three-dimensional. The sleigh and the snowflakes fold at the ridge and continue straight across the faces of the ridge beam and the purlins, foreshortened along each slope, before continuing onto the walls. The tall stone chimney breast receives a continuous picture with clear folds at its two projecting corners. The limed-oak mullioned window frames, glazing bars and the limed-oak plank door carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. THIS IS THE KEY CORRECTION FOR THIS SET: the exposed wood must visibly carry the picture. Every exposed piece of limed oak in shot - each truss, rafter, purlin, beam, brace, half-timber post and rail, window mullion, frame and glazing bar, the door and doorway casings, the skirting and the mantel - is painted over by the projection in the same full colour as the plaster beside it: the village, garlands, aurora, stars and snowflakes run straight across the face of the wood and bend at each edge, the wood grain showing faintly through the projected colour. No beam, frame or casing stays as a dark bare wooden stripe or an unlit outline. Only the window GLASS stays the dark night outside. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The herringbone oak floor, the soft cream-and-cranberry Persian-style wool rug, the camel-brown velvet sectional sofa, the round deep-green leather ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

NATURAL, LESS CINEMATIC LOOK - one small notch more natural than a polished film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster, a painting or an advert. True-to-life colour and contrast exactly as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting, no heightened fantasy glow on the children, and no storybook-illustration or oil-painting finish on the projection. The projection is still dense, bright and colourful, but its colour sits a touch closer to real life - rich, not neon - and it reads as the real light of a home Christmas projector falling on real walls: the plaster texture and wood grain show faintly through it, and the shadows keep a little more ordinary room detail, with the furniture, rug and floor clearly readable in the soft spill.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the cream lime plaster and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### Take history
- g1 / r - 2026-09-25 - generated once, FOR REVIEW (awaiting Daniel).


## Clips - round 1 (2026-09-25)

Daniel 2026-09-25: "make the clips only for video 24 and 25 ... only one generation for each clip" - frames treated as approved. One generation per clip, no re-rolls. Model settings for every clip: seedance_2_5 · omni_reference · 720p · 9:16 · audio on (C02-C04 and C07 4 s, C05-C06 5 s).

### C02 clip
**Clip:** `clips/v24_c02_g1.mp4` (CLIP FOR REVIEW)
**Settings:** seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job ID:** `a919c88f-65fd-4257-8a03-8b9a0414c62a`
**Attached:**
- start_image: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
- image: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**Lineage:** Reused from v23 C02 g1 (verified record, in the cut) - changed only the physically different nouns: sleeve, table, bauble colours and dining room.

### Video prompt
````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 4-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no zoom, no reframe. Every stage of the box opening is shown happening - the flap lifting, folding back and the hand reaching in - never skipped. The box, hands and table stay continuous frame to frame.

STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a cranberry-red cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge fills the frame. The lit cream candle, fir sprigs, small pinecones, small cranberry and gold glass baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive English Tudor-revival dining room with cream lime-plaster walls framed by pale limed-oak half-timber posts and beams, a black wrought-iron candle chandelier, a carved stone fireplace with cranberry and forest-green knitted stockings, a limed-oak dresser with blue-and-white plates, and a Christmas tree dressed with cranberry-red, forest-green and gold glass baubles and warm white fairy lights. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge, lid flaps folded back. The printed front artwork, candle, fir, baubles, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

### C03 clip
**Clip:** `clips/v24_c03_g1.mp4` (CLIP FOR REVIEW)
**Settings:** seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job ID:** `8b7047c6-2f67-4d69-b083-03864340d9e2`
**Attached:**
- start_image: `content/video_24_assets/starting_frames/v24_c03_g1.png` · Higgsfield media `03992926-ec39-4527-bb57-1d0443957611`
**Lineage:** Reused from v23 C03 g1 (verified record, in the cut) - changed only the sleeve, counter material (incl. every "terrazzo") and kitchen finishes/tree ornaments.

### Video prompt
````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in cranberry-red cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy; behind it pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the limestone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the limestone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the limestone.
3.0-3.4s - the four feet of the stand touch the limestone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the limestone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### C04 clip
**Clip:** `clips/v24_c04_g1.mp4` (CLIP FOR REVIEW)
**Settings:** seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job ID:** `677de711-bb9b-4853-9fe8-789a51aef013`
**Attached:**
- start_image: `content/video_24_assets/starting_frames/v24_c04_g1.png` · Higgsfield media `4d260de1-556a-41ac-afe1-a8f708913c72`
**Lineage:** Reused from v23 C04 g1 (verified record, in the cut) - changed only the sleeve, counter material (incl. every "terrazzo") and kitchen finishes/tree ornaments.

### Video prompt
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
THE LEFT HAND - a woman's hand in a cranberry-red cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same cranberry-red cable-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy; behind it pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the limestone and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the limestone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the limestone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

### C05 clip
**Clip:** `clips/v24_c05_g1.mp4` (CLIP FOR REVIEW)
**Settings:** seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on
**Job ID:** `0aa11eb0-619c-4ab5-9676-aee7a7468ce8`
**Attached:**
- start_image: `content/video_24_assets/starting_frames/v24_c05_g1.png` · Higgsfield media `afe8c961-388f-423a-9ade-7a7c05b20121`
- image: `content/video_24_assets/references/v24_c05_r2.png` · Higgsfield media `207fb72f-8668-4fad-8a0a-4009eac963dc`
**Lineage:** NEW prompt built 2026-09-25 from the v23 C05 g3 (in the cut) structure after reviewing every C05-C07 take and Daniel verdict in v17-v23. Kept: animated-cartoon projection block with per-element travel rates and per-second track, the single forward-and-upward glide, direct room entry, empty-room reference, exact-two-children count lock. Changed per Daniel 2026-09-25: the children are no longer a chase game - they are spellbound by the ceiling (pointing, following the sleigh, gasping), always moving, already far from the door when it opens; feet stay on the floor (sofa jumps looked fake on v23 g1); theme-specific moving elements (aurora / reindeer herd); ONE CONTINUOUS TAKE rule added at the top; asset roles named in plain words instead of mixed @Image numbering.

### Video prompt
````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 5-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no dissolve, no zoom, no reframe. Everything in it happens continuously, frame to frame.

PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas picture on the walls and the open-timbered gabled ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. Only the projected picture is animated; the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in EVERY frame from the first to the last, independent of the camera. Only the drawn buildings, trees and the moon stay put; everything else in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is never parked with only its legs moving. It flies in one smooth sweeping arc from where it is first seen across the open-timbered gabled ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place every second and has crossed most of the ceiling by the end. The reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- NORTHERN LIGHTS: the green and violet aurora curtains along the upper walls ripple and billow continuously like silk in the wind - their folds roll sideways along the wall about one curtain-width every second while bright waves of green light run up and down through them. The aurora is never frozen.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY cottage chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the horse-drawn sleigh with its lanterns glides steadily along the lane with the horses trotting; the villagers walk along the street carrying their Christmas tree home; the children on sledges slide down the snowy hill; the amber cottage windows flicker.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall - flat light on the wall and ceiling surfaces, never real snow in the room.
- SKY AND LIGHTS: the silver full moon glows; golden stars twinkle; now and then a shooting star streaks across the ceiling; bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (5 s):
0-1s: the door opens onto the room; through the very first gap the sleigh is already flying and smoke is already rising from every cottage chimney and the aurora is already rippling.
1-2s: the sleigh team travels across the open-timbered gabled ceiling, clearly changing position, reindeer galloping; smoke columns climb the wall; the aurora curtains roll sideways; the horse-drawn sleigh glides along the lane; snow drifts down.
2-3s: the sleigh has flown on another quarter of the ceiling; the aurora billows; the villagers carry their tree along the street; the children sledge down the hill.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; the aurora ripples on; a shooting star streaks across.
4-5s: all of it still moving at the same pace in the final frame - sleigh flying, smoke rising, aurora rippling, horse-drawn sleigh gliding, snow falling.
All of this is flat projected light lying on the real lime plaster, the limed-oak trusses and half-timbering and the mullioned window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CHILDREN - SPELLBOUND BY THE CEILING AND ALWAYS MOVING. EXACTLY TWO CHILDREN exist in this clip - THE BOY and THE GIRL described below - and nobody else ever appears: no third child, no extra kids in the background, on the sofa or in the doorway, no adult. The room reference photo is EMPTY, so there is no pose or spot to copy. When the first gap of the door opens, both children are ALREADY in the middle and far side of the room, at least three metres from the door - never standing in or near the doorway, never lined up facing the camera, never side by side. They were already watching the projection before the door opened and they are completely amazed by it: mouths wide open, eyebrows raised, gasping and laughing, eyes glued to the flying sleigh on the ceiling. They keep moving the whole time and follow the sleigh with their eyes, arms and feet. Per second:
0-1s: in the very first gap THE BOY is already walking slowly backwards across the rug, head tipped far back, one arm stretched straight up pointing at Santa's flying sleigh; THE GIRL, a few steps away from him, is up on tiptoe with both hands pressed to her cheeks, mouth open, staring straight up.
1-2s: THE BOY keeps stepping backwards and turns his body to follow the sleigh as it flies overhead, his pointing arm tracking it across the ceiling; THE GIRL runs three quick little steps across the rug in the same direction the sleigh is flying, one hand reaching up toward it.
2-3s: THE BOY looks over at THE GIRL, points up again and shouts with excitement, then looks straight back up; THE GIRL spins round once on the rug with her arms out and her face turned up to the ceiling, laughing.
3-4s: THE GIRL does two small excited bunny-hops on the spot, landing back on the rug at real speed, pointing up at the rippling northern lights; THE BOY walks sideways past the ottoman with his head still tipped back, following the sleigh.
4-5s: both are still moving in the last frame - THE BOY still stepping and pointing up, THE GIRL trotting toward the Christmas tree while gazing up - never frozen.
They never stand still, never pose, never face the camera and never wait. Their feet stay on the floor: they never climb, jump onto or jump over the sofa, the ottoman or any furniture. Both stay in view: neither ducks behind furniture and pops up somewhere else. Real speed, real weight, grounded feet - no sliding, floating, slow motion or running in place. This child action never alters the camera movement.

CAMERA CONTINUITY: the entire five seconds are ONE slow, uninterrupted forward-and-upward glide. Forward travel and upward aim are coupled as one motion, already underway together in frame zero. Keep the same gentle pace and the same forward-to-upward ratio for every frame, including while the door opens and while crossing its sill. Travel only about 0.8 metres forward over the entire shot, with an even upward tilt of about 18 degrees over those same five seconds. The wreath, door-panel edges and later the back-wall details drift smoothly downward in the frame from the beginning while perspective advances very gently. There is no forward-only phase and no later tilt-only phase. Do not accelerate the beginning, hurry through the door, ease in, ease out, steepen the tilt, speed-ramp or catch up to an end composition. The final frame can remain near the threshold with the back wall, furniture and ceiling visible. The door opens naturally during the same slow glide; its opening is not a camera cue.

DIRECT ROOM ENTRY: the closed door in the start image is fitted directly into the great room's entrance wall and its far face opens straight into the furnished Christmas room shown in the room reference photo. ONE door, ONE thin normal threshold about 15 cm deep. The very first gap reveals the room itself, the already-moving children and the already-playing projection, close behind this door. No hall, foyer, vestibule, passage, empty approach space, second doorway or arch between this door and the room. The side doorway on the reference room's right wall is a lateral feature only and never lies ahead of the camera.

Wholesome family Christmas scene, children at home at Christmas.

TASK AND ASSETS: image-to-video, one continuous handheld phone POV take, vertical 9:16. The START IMAGE is frame 0.0s: a deep forest-green painted oak plank door with black wrought-iron strap hinges, a satin finish and a pale limed-oak surrounding casing fully closed with a wreath, a woman's hand with fair skin with a light dusting of freckles and a cranberry-red cable-knit wool sleeve on the brass knob. The ROOM REFERENCE IMAGE (attached as an image reference) controls only the room's architecture, furniture, colours and projected artwork; it contains no people and it is not an end frame, camera target or transition destination - never dissolve, cut, morph or snap into its composition. The two children come only from this text.

CONTINUOUS ACTION: during approximately the first 1.5 seconds the hand turns the knob and opens the door with a smooth, ordinary, unhurried push. The room behind it is already running: the projection is already playing and both children are already moving - the widening gap only uncovers more of a scene that was already happening. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain wood - no glowing strip, no coloured fringe, no bright seam in the gap. The shot ends during the same gentle glide with the back wall, furniture and ceiling still visible.

CAMERA - eye height, normal wide-angle phone lens, a steady natural phone glide as described. No zoom, orbit, fisheye, lens warping, stop, second move or cut. The camera is the person's eyes; no phone, screen or device in frame. Hold the sharpness and exposure of the start image - crisp phone footage, in focus from the first frame to the last.

AUDIO - dry documentary sound only: the handle, the door swinging, the children gasping, laughing and calling out in delight, their footsteps on the floor, quiet room tone. (no BGM). No subtitles.

ROOM AND IDENTITY - a spacious double-height English Tudor-revival Christmas great hall with a high open-timbered GABLED CEILING: two broad cream lime-plaster roof planes rise to a crisp central ridge, crossed by three pale limed-oak king-post trusses with curved braces. Pale limed-oak half-timber posts, rails and diagonal braces divide the cream lime-plaster walls into large panels. A tall carved limestone chimney breast stands on the back wall with a deep stone hearth; a wall of tall leaded casement windows in pale limed-oak mullioned frames occupies the left wall and a wide limed-oak doorway sits on the right. Wide pale oak floorboards, a large deep forest-green velvet chesterfield sectional sofa, a round tan leather ottoman and a soft cream wool rug.
THE BOY - a boy of about six with fair freckled skin and tousled copper-red hair. THE GIRL - a girl of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons. Both fully dressed in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

BANNED - a third child or any extra people appearing at any moment; an adult; a child standing still, frozen, posed or waiting at any moment; the children standing in or next to the doorway when it opens; the children side by side or facing the camera; a child climbing onto or jumping on or over furniture; a child disappearing behind furniture and reappearing elsewhere; slow motion or floaty movement; a camera that moves, stops and moves again; a zoom; a cut; a glow along the door edge; light that grows or fills the room as the door opens; the projector unit visible; blur; music; subtitles.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the aurora does not ripple; the horse-drawn sleigh or the villagers do not travel; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture slides as one sheet; any projected shape floats in the room.
````

### C06 clip
**Clip:** `clips/v24_c06_g1.mp4` (CLIP FOR REVIEW)
**Settings:** seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on
**Job ID:** `c849f730-dead-468f-8ae7-4d94a85bc10b`
**Attached:**
- start_image: `content/video_24_assets/starting_frames/v24_c06_g1.png` · Higgsfield media `a36295bc-fdfd-47c2-8bf2-b7b5cd062961`
- image: `content/video_24_assets/starting_frames/v24_c06_g1.png` · Higgsfield media `a36295bc-fdfd-47c2-8bf2-b7b5cd062961`
**Lineage:** NEW prompt built 2026-09-25 from v23 C06 g2 (in the cut) + the REAL-TIME SPEED sentence from v22 C06 g3 (in the cut). Kept: animated projection block, one slow tilt DOWN from the exact start framing, real-mattress bounce spec. Added: ONE CONTINUOUS TAKE rule, theme-specific moving elements, the boy pointing at and following the sleigh while he bounces.

### Video prompt
````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 5-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no dissolve, no zoom, no reframe. Everything in it happens continuously, frame to frame.

PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas picture on the walls and the shed ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. Only the projected picture is animated; the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in EVERY frame from the first to the last, independent of the camera. Only the drawn buildings, trees and the moon stay put; everything else in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is never parked with only its legs moving. It flies in one smooth sweeping arc from where it is first seen across the shed ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place every second and has crossed most of the ceiling by the end. The reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- NORTHERN LIGHTS: the green and violet aurora curtains along the upper walls ripple and billow continuously like silk in the wind - their folds roll sideways along the wall about one curtain-width every second while bright waves of green light run up and down through them. The aurora is never frozen.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY cottage chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the horse-drawn sleigh with its lanterns glides steadily along the lane with the horses trotting; the villagers walk along the street carrying their Christmas tree home; the children on sledges slide down the snowy hill; the amber cottage windows flicker.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall - flat light on the wall and ceiling surfaces, never real snow in the room.
- SKY AND LIGHTS: the silver full moon glows; golden stars twinkle; now and then a shooting star streaks across the ceiling; bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (while the camera tilts down):
0-1s: snow streams down the whole projection; the sleigh is already flying across the ceiling; smoke is already rising from every cottage chimney and the aurora is already rippling.
1-2s: the sleigh has flown a quarter of the way across the ceiling; smoke columns climb the wall; the aurora curtains roll sideways; the horse-drawn sleigh glides along the lane.
2-3s: the sleigh flies on across the ceiling; the aurora billows; the villagers carry their tree along the street; the children sledge down the hill.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; the aurora ripples on; a shooting star streaks across.
4-5s: sleigh flying, smoke rising, aurora rippling, horse-drawn sleigh gliding, snow falling - all still moving in the last frame.
All of this is flat projected light lying on the real lime plaster, the limed-oak rafters and half-timbering and the window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, the bed or the boy.

CAMERA - ONE slow, small tilt DOWN, the opposite of the other room clips in this set.
0.0s: the clip starts EXACTLY on the start image - the same framing, with the fully projected ceiling at the top of the frame. The camera never aims above this framing, so no part of the ceiling that is not in the start image ever appears, and every visible part of the ceiling is covered with the projection from the first frame - no bare plaster or bare wood anywhere.
0.0-4.0s: the camera tilts DOWN slowly and smoothly by about 10 degrees, like a calm parent filming: the projected ceiling slides up and partly out of the top of the frame while more of the bed, the covers and the rug come into view at the bottom. The boy stays fully in frame from head to feet.
4.0-5.0s: it eases to a gentle stop.
One continuous take: no cut, no zoom, no push-in, no pull-back, never a tilt up.

THE BOY BOUNCES LIKE A REAL CHILD ON A REAL MATTRESS - natural, believable and unexaggerated, at real speed for all five seconds. Small, springy, continuous bounces on the same spot in the middle of the bed: his feet leave the mattress by only about 10 to 20 centimetres, about two bounces per second, the soft mattress visibly sinking under his feet on every landing and pushing him back up. REAL-TIME SPEED, NOT SLOW MOTION: each bounce is quick and snappy, taking only about half a second from push-off to landing under normal gravity, exactly like a real child filmed at normal speed - the footage is never slowed down, never time-stretched and never dreamy. Knees soft, head tipped back, mouth open, laughing up at the ceiling in amazement. While he bounces he throws one arm straight up and points at Santa's sleigh, turning his head to follow it as it flies across the ceiling, then drops the arm and points again. His body keeps exactly the same size, proportions, face and clothing in every frame; he stays in the same spot on the bed. No high leaps, no hanging in the air, no floating, no hopping across the bed, no stiff puppet-like body, no morphing limbs.

Wholesome family Christmas scene, a child at home with his family at Christmas. Crisp real iPhone footage at night, handheld, real-time speed, sharp from first frame to last.

ASSET ROLES: the start image, also attached as the image reference, is the approved still that controls a bright-proportioned English Tudor-revival bedroom with a high SHED CEILING: a single cream lime-plaster plane sloping up from the front of the room to the tall back wall, crossed by pale limed-oak rafters. A pale limed-oak panelled bed with a wide upholstered cream headboard is centred on the flat back wall between two tall leaded casement windows with pale limed-oak mullioned frames and glazing bars, the back wall divided by pale limed-oak half-timber posts and rails, white bedding with a cranberry-red knitted throw, limed-oak bedside chests, wide pale oak floorboards and a soft cream wool rug. Preserve the exact child identity, clothing, furniture, colours and the full projected artwork of the start image; its framing is the FIRST frame of this clip.

SUBJECTS:
THE BOY - exactly one child, a boy of about six with fair freckled skin and tousled copper-red hair, fully dressed for winter in a cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama set with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks, standing on the bed. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the walls and the whole shed ceiling. Everything glowing on the plaster and the wood is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing and gasping in delight. (no BGM). No subtitles.

DO NOT INCLUDE: a still, frozen or printed-looking projection; a projection that only twinkles; a sleigh parked in one place; chimneys without smoke; an aurora that does not ripple; a horse-drawn sleigh or villagers that do not travel; snow that does not fall; bare, white or unprojected ceiling or wall; a camera that starts higher than the start image; a camera that tilts up; zoom, push-in or pull-back; slow-motion or floaty jumping; high exaggerated leaps; the boy changing size or shape; real snow or particles in the air of the room; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
````

### C07 clip
**Clip:** `clips/v24_c07_g1.mp4` (CLIP FOR REVIEW)
**Settings:** seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job ID:** `0a8665a2-25e1-432e-954b-e835bbb51b53`
**Attached:**
- start_image: `content/video_24_assets/starting_frames/v24_c07_g1.png` · Higgsfield media `e02e1c3d-02cb-4e8d-add1-0d8fccdbe38a`
**Lineage:** NEW prompt built 2026-09-25 from v23 C07 g2 (in the cut). Kept: opening-state lock, animated projection block, step / hold / limited tilt-up camera with no-bare-ceiling lock, surface mapping. Changed per Daniel 2026-09-25: both children fascinated and always moving - the girl bounces along the sofa pointing up at the sleigh, the boy walks backwards following it; ONE CONTINUOUS TAKE rule; theme-specific moving elements.

### Video prompt
````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 4-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no dissolve, no zoom, no reframe. Everything in it happens continuously, frame to frame.

OPENING STATE - frame 0.0s preserves the start image's complete, saturated projection on every visible wall, the chimney breast, the whole vaulted ceiling and every beam. The projector has been running for a long time before filming. Full coverage and brightness stay on for all four seconds while the drawn elements are already moving. There is no lighting-up, unveiling, growth, wipe or fade-in, and the ceiling artwork is never erased and redrawn.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children in a double-height Christmas family room are amazed by a projected Christmas picture that is PLAYING across the back wall and the entire vaulted ceiling, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical 9:16.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no washed-out exposure, no colour shift.

ASSET ROLES: the start image is frame 0.0s and controls a spacious double-height English Tudor-revival Christmas family room with a high VAULTED CEILING: two broad sloping cream lime-plaster planes rising to a crisp central ridge, with one heavy pale limed-oak ridge beam running along it and pale limed-oak purlins crossing each slope. Cream lime-plaster walls. A tall chimney breast of honey-coloured Cotswold stone stands on the back wall with a thick limed-oak beam mantel; a full-height wall of leaded windows in pale limed-oak mullioned frames and glazing bars fills the left wall and a wide limed-oak plank door sits on the right. A herringbone pale oak floor, a large camel-brown velvet sectional sofa, a round deep-green leather ottoman and a soft cream-and-cranberry Persian-style wool rug. Preserve the exact child identity, clothing, furniture, colours, full existing projection and opening framing.

SUBJECTS:
THE GIRL - a girl of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons, on the sofa, caught mid-jump in the start image.
THE BOY - a boy of about six with fair freckled skin and tousled copper-red hair, on the rug in front of the sofa, back to camera and slightly to the side, looking up at the projected ceiling with his arms out.
Both in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. Both stay small in frame, in scale with the huge room. EXACTLY TWO CHILDREN - no third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole vaulted ceiling.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas picture on the walls and the vaulted ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. Only the projected picture is animated; the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in EVERY frame from the first to the last, independent of the camera. Only the drawn buildings, trees and the moon stay put; everything else in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is never parked with only its legs moving. It flies in one smooth sweeping arc from where it is first seen across the vaulted ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place every second and has crossed most of the ceiling by the end. The reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- NORTHERN LIGHTS: the green and violet aurora curtains along the upper walls ripple and billow continuously like silk in the wind - their folds roll sideways along the wall about one curtain-width every second while bright waves of green light run up and down through them. The aurora is never frozen.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY cottage chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the horse-drawn sleigh with its lanterns glides steadily along the lane with the horses trotting; the villagers walk along the street carrying their Christmas tree home; the children on sledges slide down the snowy hill; the amber cottage windows flicker.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall - flat light on the wall and ceiling surfaces, never real snow in the room.
- SKY AND LIGHTS: the silver full moon glows; golden stars twinkle; now and then a shooting star streaks across the ceiling; bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (4 s):
0-1s: the sleigh team is already flying, reindeer galloping; smoke is already rising from every cottage chimney and the aurora is already rippling.
1-2s: the sleigh has moved a quarter of the ceiling and is crossing the silver moon; smoke columns climb the wall; the aurora curtains roll sideways; the horse-drawn sleigh glides along the lane.
2-3s: as the camera tilts up the sleigh flies on across the vaulted ceiling; the aurora billows; the villagers carry their tree along the street; the children sledge down the hill.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; the aurora ripples on; a shooting star streaks across - sleigh flying, smoke rising, aurora rippling, horse-drawn sleigh gliding, snow falling, all moving in the final frame.
All of this is flat projected light lying on the real lime plaster, the limed-oak ridge beam and purlins, the Cotswold-stone chimney breast and the mullioned window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CHILDREN - AMAZED, AND ALWAYS MOVING:
THE GIRL lands from the jump shown in the start image onto the sofa cushions and keeps bouncing along the sofa with small, springy, real-speed bounces - her feet leave the cushion by only 15 to 25 centimetres, about two bounces per second, the cushion visibly sinking on every landing - moving a little further along the sofa with each bounce while she points one arm straight up at Santa's flying sleigh, head tipped back, mouth wide open, squealing with delight.
THE BOY walks slowly backwards across the rug with his head tipped far back, one arm stretched up pointing at the sleigh, turning his body to follow it as it flies across the ceiling; around 2 seconds he glances across at his sister, points up again and laughs, then keeps stepping and gazing up.
Neither child ever stands still, poses or faces the camera. Real children moving at real speed with real weight: quick, snappy bounces under normal gravity, never slow motion, never floating, never a high exaggerated leap, no morphing limbs.

TIMELINE (camera):
0.0-1.0s the person filming takes one small step forward; the frame moves in slightly and settles.
1.0-2.0s the camera holds in the closer position.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree, only far enough that the vaulted ceiling fills the upper half of the frame - it never tilts past the projected picture. The ENTIRE vaulted ceiling in view, every plane, beam and corner, is covered with the projection - starry midnight sky, the silver full moon, the snowflakes and the flying sleigh - no bare plaster, no bare wood, no unprojected corner anywhere in view. Both children stay low in the frame and keep moving.
No zoom - the only forward movement is the one small physical step.

AUDIO: room tone, two children laughing, gasping and squealing, cushions thumping, feet on a rug. (no BGM). No subtitles.

SURFACE MAPPING - The two sloping plaster planes, the limed-oak ridge beam and the purlins remain stationary. The drawings fold at the ridge and run across the faces of the ridge beam and purlins, fold around the Cotswold-stone chimney corners and carry across the limed-oak mullioned window frames, glazing bars and the limed-oak plank door, with correct surface perspective and occlusion. All physical architecture stays stationary.

DO NOT INCLUDE: bare, blank, white or partly unprojected ceiling, beam, corner or wall in any frame, especially at the end when the camera looks up; a camera that tilts up beyond the projected picture; a projection appearing, fading in or revealing itself; children standing still; slow motion; floating or weightless movement; a third child; an adult; any music; the projector unit in shot; a zoom; blur; a cut; on-screen text; subtitles.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the aurora does not ripple; the horse-drawn sleigh or the villagers do not travel; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````

## C01 - Hook — Ladder — painting the ceiling
**Frame:** `starting_frames/v24_c01_g1.png`
**Clip:** none yet (Daniel validates the image first)
**Settings:** gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688 · count 1 · media role image → image_references (backend)
**Job ID:** `9c549b3c-52d9-45f1-b771-86c8687c9317`
**References:**
- @Image 1: `content/video_6_assets/starting_frames/v6_c01_g4.png` · Higgsfield media `9cd2cb32-1f96-4484-ad2f-cc726aca8088`
- @Image 2: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield job `85ba004e-383a-478a-88e5-b67066ac8da9`
**Result:** https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_230633_9c549b3c-52d9-45f1-b771-86c8687c9317.png · md5 `7a4b390730f66b079a6c0f4fafb692cc` (downloaded byte-identical)
**Lineage:** Reused from v18 C01 (`starting_frames/v18_c01_g1.png`, job 7cc3af15, verified record) - Daniel 2026-09-26: "like video 18 but the woman paints on the ceiling a Christmas painting that is not looking too good, paint bucket in one hand and brush in the other; different room, woman, background". Same @Image 1 (v6_c01_g4) and settings; @Image 2 = this video's room reference in the role v18_c05_r3 had. Changed: the opening sentence (Santa/tape removed, 'same pose ... both arms up' → 'same position ... arms up at the ceiling'); 'two things' → 'three things'; THE WOMAN's description and her last sentence (tape roll → paint bucket in LEFT hand, brush in RIGHT hand on the ceiling); THE ROOM line (Gustavian → English Tudor-revival); the flag-wall noun; a new '3. THE CEILING' paragraph (bad amateur Christmas ceiling painting where the Santa was); in REFERENCE ROLES 'taped inflatable Santa, duct tape roll,' removed, the @Image 2 palette sentence, and the Santa-tape sentence replaced by the no-Santa/no-tape sentence. Everything else byte-identical.

### Image prompt — `starting_frames/v24_c01_g1.png`
Exact text in the verified record below (`### C01`).

### Take history
- `starting_frames/v24_c01_g1.png` — generated 2026-09-26, one generation, FRAME FOR REVIEW.
- `clips/v24_c01_g1.mp4` — seedance_2_5, one generation 2026-09-26, job `820ffc95-c049-470f-9903-ef5339afe87f`, md5 `768382f682394d7002f2c0032c057138` (downloaded byte-identical), CLIP FOR REVIEW. Reused from v23 C01 g2 (`clips/v23_c01_g2.mp4`, job 6da5e760, verified record, in the cut; = v18 C01 g3 text) - Daniel 2026-09-26: ladder-fail style, first second she paints the ceiling, then falls off the ladder onto the floor spilling paint all over the floor. Same settings. Changed: the START FRAME LOCK noun (taped Santa → her ceiling painting, bucket in left hand, brush in right); the first-second line (taping → painting the ceiling); 'taping motion'/'taping and the fall' → painting; added after the ladder sentence: the bucket comes down with her, tips over, red paint spreads in a big pool; 'stays down on the floor' + 'in the spreading red paint'; the Santa-stays-taped line replaced by a paint-realism + PAINT SOURCE paragraph (all paint from the one bucket, nothing from the brush or ceiling, ceiling painting unchanged) adapted from v21 C01 g2; audio 'the tape' → brush on the ceiling, + bucket clanging and paint splashing; FALL AND FRAMING LOCK: + 'The ladder, the bucket and the paint stay inside the frame.', 'taped Santa' → 'painting'. Motion, camera, pacing and framing text otherwise byte-identical.
- `clips/v24_c01_g1.mp4` — Daniel 2026-09-26: REJECTED — "it's looking completely faked. Looks like she's stunned. It's looking very weird and completely unnatural".
- `clips/v24_c01_g2.mp4` — seedance_2_5, one generation 2026-09-26, job `cd64b13d-3933-4771-975c-e188d6d24d5b`, md5 `b16d2942fa9ca91062db8a4bd7b6fff7` (downloaded byte-identical), CLIP FOR REVIEW. Re-roll of g1 on the same approved frame, same settings. Rebuilt from v23 C01 g2 (the fall used for v30, which Daniel pointed to) with ONLY the ceiling-painting nouns changed: START FRAME LOCK 'the inflatable Santa taped to the ceiling' → 'her Christmas painting on the ceiling'; first-second line → painting (brush right, bucket left, both hands up); 'taping' → 'painting' in the fall sentence; one sentence added after the ladder sentence: the bucket drops, hits the floor and red paint splashes out beside her; 'The inflatable Santa stays taped...' → 'The painting stays on the ceiling the whole time.'; audio 'the tape' → 'the brush', 'the ladder hitting' → 'the ladder and the bucket hitting'; FALL LOCK 'taped Santa' → 'painting'. Dropped g1's additions (big spreading pool, lying in the paint, PAINT SOURCE paragraph, bucket-stays-in-frame line) - they made the fall and landing look staged.
- `clips/v24_c01_g2.mp4` — Daniel 2026-09-26: REJECTED — "came out the same, I still don't like it, it's looking very fake and unnatural".
- `clips/v24_c01_g3.mp4` — seedance_2_5, one generation 2026-09-26, job `a2c9a375-b99f-42f6-9476-8c798f48710f`, md5 `dd7309b28845855966ab360bc4bd2fdd` (downloaded byte-identical), CLIP FOR REVIEW. Re-roll of g2 on the same approved frame, same settings. Changed (prompt edit only): the fall sentence now says she leans too far, the ladder rocks and tips sideways under her, and bans climbing down / stepping down the rungs / crouching on the ladder first (g1 and g2 both showed her crouched on the ladder before falling); the landing paragraph replaced - she lands on her side and hip, twisted, never flat on her back or spread-eagled or posed, then curls up, clutches her hip, groans, rolls and props up on one elbow, moving the whole time, never frozen (g1/g2 ended in a still star-shaped pose, the 'stunned' look Daniel called fake); audio ending 'her breathing' → 'her groaning in pain'. Seen on review: the landing now reads as hurt and curled; the ladder stays standing instead of going over, and around 1.7 s she still half-steps down before dropping; the camera still tilts down to follow her.
- `clips/v24_c01_g3.mp4` — Daniel 2026-09-26: APPROVED ("now all the hooks are good"; kept as is despite the notes above).

## Upscales

Approved clips upscaled 2026-09-26 on higgsfield.ai/upscale (Chrome extension), Daniel's exact settings - this time ONE setting for ALL clips, hook and B-roll alike (Daniel: "I want to try something new"; earlier videos used Preset Common for C02–C07). Each clip was uploaded from its local file (the uploaded input's md5 equals the local clip), the settings were read back off the page before every submit, and each job's stored params were read back after (`model_version pro · resolution 2k · fps 30 · preset aigc`, type `bytedance_video_upscale`). Each upscale keeps its source's exact name in `clips/upscaled/`; each download is byte-identical to the Higgsfield result.

C01–C07: **ByteDance Upscale · Model version Pro · Resolution 2K · FPS 30 fps · Preset AIGC**

| Upscale file | Source clip | Source md5 | Upscale job | Result | md5 | Output |
|---|---|---|---|---|---|---|
| `clips/upscaled/v24_c01_g3.mp4` | `clips/v24_c01_g3.mp4` | `dd7309b28845855966ab360bc4bd2fdd` | `3b0138a7-51f5-486e-b4ed-6d83d5089596` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_003007_9ac1df1e-bd6b-4a7f-b49c-2dcfc8703996.mp4 | `302458721acf9a519741d4179ac613a4` | 1440×2560, 30 fps, 4.07 s |
| `clips/upscaled/v24_c02_g1.mp4` | `clips/v24_c02_g1.mp4` | `d5da8648cab80690775eafa8b951e656` | `29ff698e-8008-4683-92c6-207d768b9ed1` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_003052_7163ef88-5d9e-44f7-a1dc-7215650e430f.mp4 | `a162e862767c949d8ff05dadb6ee902d` | 1440×2560, 30 fps, 4.07 s |
| `clips/upscaled/v24_c03_g1.mp4` | `clips/v24_c03_g1.mp4` | `9ce7bef8937743c5ee6ac07da31ccfd4` | `b1765b6f-713c-4cb7-8479-d0c2417cbdd8` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_003122_461c9368-7308-4491-b195-6e121e342f0b.mp4 | `a6e8ba05d070243628d09d31bf62a239` | 1440×2560, 30 fps, 4.07 s |
| `clips/upscaled/v24_c04_g1.mp4` | `clips/v24_c04_g1.mp4` | `b2298a6fcd1fd08a18a7f273d8e14b0e` | `3a4ca3ad-9a91-43ec-a53b-02d350d64484` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_003159_fad5bc9e-bd7d-4547-aa1e-66403c7f4e7e.mp4 | `8eecea66937dbc30a81361aae03aa80a` | 1440×2560, 30 fps, 4.07 s |
| `clips/upscaled/v24_c05_g1.mp4` | `clips/v24_c05_g1.mp4` | `6c493074d9c1b8b5a3e907af2d318cb0` | `297265ae-5939-4e4c-8c6f-7c0f60407b98` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_003233_ed474a2a-54e6-422c-ade7-e0d61ed86b3b.mp4 | `3fdc0b5d1ce6248e3954fda2c5573d7a` | 1440×2560, 30 fps, 5.06 s |
| `clips/upscaled/v24_c06_g1.mp4` | `clips/v24_c06_g1.mp4` | `410d704c75559b37a8e99a0cc1d29dd0` | `873e25a8-7bb4-4cbd-bcfa-9147b344264b` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_003306_3971704f-8931-418a-87a3-860751eb3b19.mp4 | `2c9c6da3b280834c2a3a12809e86fe6f` | 1440×2560, 30 fps, 5.06 s |
| `clips/upscaled/v24_c07_g1.mp4` | `clips/v24_c07_g1.mp4` | `005a85a68ed88d40518aaf044c91b777` | `d943743c-fca6-4392-8ae9-bb57c28b4058` | https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_003340_f841c65f-8c22-415d-93dd-d249bb520d2d.mp4 | `40d96a8dad4a65ffa038fee5e99079cd` | 1440×2560, 30 fps, 4.07 s |

## Verified record — Higgsfield (checked 2026-09-25)

Recovered from `show_generation_by_ids` right after generation; byte-identical to the prompts above.

### C01 — Ladder — painting the ceiling

#### Image prompt — `starting_frames/v24_c01_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `9c549b3c-52d9-45f1-b771-86c8687c9317`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_230633_9c549b3c-52d9-45f1-b771-86c8687c9317.png
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c01_g4.png` · Higgsfield media `9cd2cb32-1f96-4484-ad2f-cc726aca8088`
- @Image 2: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield job `85ba004e-383a-478a-88e5-b67066ac8da9`

````text
Keep the FIRST attached image exactly as it is - the same room layout, the same camera position, distance and angle, a different woman in the same position near the top of the same ladder with her arms up at the ceiling, the same curved staircase, garland, stockings, fireplace, mirror, Christmas tree, sofa and rug positions, the same lighting, and the same clean empty band of ceiling across the top sixth of the frame. Change only these three things:

1. THE WOMAN: replace her with a mother about 30 with fair skin and straight light-auburn hair pulled back in a loose low ponytail. She is wearing matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit. Same body scale, same position on the ladder, same thick grey wool socks. She holds an open round metal paint bucket by its wire handle in her LEFT hand, and a wide paintbrush loaded with red paint in her RIGHT hand, raised and pressed against the ceiling mid-stroke. No duct tape and no tape roll anywhere.

2. THE ROOM: a different double-height English Tudor-revival living room, with cream lime-plaster walls and pale limed-oak half-timber posts and panelling, a pale limed-oak curved staircase in the same position, a carved pale stone fireplace with a lit fire and a round antique pewter-framed mirror above it, a cranberry-red velvet sofa and a forest-green wool rug over wide limed-oak floorboards. Keep the high plain white ceiling at exactly the same height and shape. The garland, stockings, tree, lamps and furniture stay in exactly the same positions and at the same scale as @Image 1. A real fabric United States flag hangs flat against the plain cream plaster wall in the same background position as @Image 1, clearly readable stars and stripes, hanging straight and still. It does not cover the Christmas tree, the fireplace or the staircase, and it does not reach up into the empty band of ceiling at the top of the frame.

3. THE CEILING: there is no inflatable Santa and no tape. Instead, exactly where the Santa was in @Image 1, she is painting a Christmas picture straight onto the plain white ceiling in flat red, green, white and yellow house paint - and it looks bad: a lopsided Santa face with a crooked red hat and a wonky white beard, a lumpy green Christmas tree leaning to one side, a few uneven yellow stars, thick streaky brush strokes, patchy coverage, smudged outlines and a couple of red drips running down from the brush. Clearly an amateur, messy, half-finished ceiling painting, but still readable as Santa and a Christmas tree. The painting stays below the clean empty band of ceiling at the top of the frame.

Everything else in the picture stays exactly as it is. Same neutral white balance with no orange cast, same iPhone snapshot look, tack sharp and in focus everywhere, absolutely nothing blurry, no background blur.

REFERENCE ROLES: @Image 1 is the approved Video 6 hook and owns the exact camera, low three-quarters-from-behind angle, framing, tall A-frame ladder, woman scale and raised-arm pose, American-flag pyjamas and crisp iPhone lighting. @Image 2 supplies only the English Tudor-revival material palette - cream lime plaster, pale limed oak, carved pale stone, cranberry red and forest green. Do not import its children, projected Christmas imagery, open-timbered gabled roof, darkness, camera or composition. This hook contains one woman on the ladder, as in @Image 1. There is no taped Santa and no tape: the only thing on the ceiling is her bad hand-painted Christmas picture, and the paint bucket and brush are in her hands. No projected patterns, no text, no captions, no watermark, no bokeh. Perfectly exposed, extremely high quality, tack sharp edge to edge.
````

#### Video prompt — `clips/v24_c01_g3.mp4` — APPROVED

**Settings** - seedance_2_5 · omni_reference · 1080p · 4 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `a2c9a375-b99f-42f6-9476-8c798f48710f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_001239_a2c9a375-b99f-42f6-9476-8c798f48710f.mp4
**Attached, in submission order**
- `starting_frames/v24_c01_g1.png` · job `9c549b3c-52d9-45f1-b771-86c8687c9317` (start_image, and again as @Image 1 in image_references)
**md5** - `dd7309b28845855966ab360bc4bd2fdd`

````text
START FRAME LOCK - HIGHEST PRIORITY: frame 0.0s is EXACTLY the supplied start image, @Image 1 is the same picture. Keep its wide framing for the whole clip: the whole double-height room is visible - the curved staircase with garland and stockings on the left, the fireplace and mirror, the sofa, the Christmas tree and the United States flag on the right - and the woman is seen from behind near the top of the tall wooden ladder in the middle of the frame, with her Christmas painting on the ceiling above her. The camera never moves closer to her, never zooms in, never crops in and never reframes onto her; she stays the same small size in the frame as in the start image.

Real home video, shot on a hand-held iPhone by a person standing in the room a few steps behind her, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow her, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and her body never resets, jumps position or teleports between one part and the next.

For the first second she is just painting the ceiling - brush in her right hand, paint bucket in her left, both hands up, nothing dramatic.

Then, without any pause or break in the movement, she leans too far to reach the painting, the ladder rocks and tips sideways under her, and she falls off it to the floor. She never climbs down, never steps down the rungs and never crouches on the ladder first - she simply goes over with it. Her arms are still up and still coming down out of the painting motion as her balance goes - the painting and the fall are one unbroken piece of movement, not two separate actions.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug. The paint bucket drops from her hand, hits the floor and red paint splashes out across the floor beside her.

She lands hard on her side and hip, one arm and her shoulder taking the impact, her body twisted and bent the way a real person lands - never flat on her back, never spread-eagled like a star, never in a neat or posed position. The movement carries straight on without a break: she curls up in pain, clutches her hip with one hand, groans and rolls slightly, then props herself up weakly on one elbow. She stays on the floor, visibly hurt and moving the whole time, never frozen, never a still pose, until the clip ends.

The painting stays on the ceiling the whole time.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the brush, a short gasp, the ladder and the bucket hitting the floor, then her groaning in pain.

FALL AND FRAMING LOCK - CHECK THIS LAST: she drops straight down beside the ladder and lands on the rug right at the foot of the ladder, in the middle of the frame, in front of the coffee table and fully visible. She does not jump, step back or leap sideways off the ladder, and she does not land behind or under any furniture. The camera keeps the start image's framing to the very last frame - the ceiling and the painting stay at the top of the picture; it never tilts down to follow her fall.
````

#### Video prompt — `clips/v24_c01_g2.mp4` — REJECTED (still fake and unnatural)

**Settings** - seedance_2_5 · omni_reference · 1080p · 4 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `cd64b13d-3933-4771-975c-e188d6d24d5b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260926_000056_cd64b13d-3933-4771-975c-e188d6d24d5b.mp4
**Attached, in submission order**
- `starting_frames/v24_c01_g1.png` · job `9c549b3c-52d9-45f1-b771-86c8687c9317` (start_image, and again as @Image 1 in image_references)
**md5** - `b16d2942fa9ca91062db8a4bd7b6fff7`

````text
START FRAME LOCK - HIGHEST PRIORITY: frame 0.0s is EXACTLY the supplied start image, @Image 1 is the same picture. Keep its wide framing for the whole clip: the whole double-height room is visible - the curved staircase with garland and stockings on the left, the fireplace and mirror, the sofa, the Christmas tree and the United States flag on the right - and the woman is seen from behind near the top of the tall wooden ladder in the middle of the frame, with her Christmas painting on the ceiling above her. The camera never moves closer to her, never zooms in, never crops in and never reframes onto her; she stays the same small size in the frame as in the start image.

Real home video, shot on a hand-held iPhone by a person standing in the room a few steps behind her, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow her, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and her body never resets, jumps position or teleports between one part and the next.

For the first second she is just painting the ceiling - brush in her right hand, paint bucket in her left, both hands up, nothing dramatic.

Then, without any pause or break in the movement, she loses her footing and falls off the ladder to the floor. Her arms are still up and still coming down out of the painting motion as her balance goes - the painting and the fall are one unbroken piece of movement, not two separate actions.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug. The paint bucket drops from her hand, hits the floor and red paint splashes out across the floor beside her.

She lands hard and the movement carries straight on into stillness without a break - she settles, rocks slightly as her weight comes to rest, and stays down on the floor for the rest of the clip, not moving much, just stunned and breathing. Her chest is still moving and she is still there when the clip ends.

The painting stays on the ceiling the whole time.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the brush, a short gasp, the ladder and the bucket hitting the floor, then her breathing.

FALL AND FRAMING LOCK - CHECK THIS LAST: she drops straight down beside the ladder and lands on the rug right at the foot of the ladder, in the middle of the frame, in front of the coffee table and fully visible. She does not jump, step back or leap sideways off the ladder, and she does not land behind or under any furniture. The camera keeps the start image's framing to the very last frame - the ceiling and the painting stay at the top of the picture; it never tilts down to follow her fall.
````

#### Video prompt — `clips/v24_c01_g1.mp4` — REJECTED (fake, unnatural fall)

**Settings** - seedance_2_5 · omni_reference · 1080p · 4 s · 9:16 · audio on · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612
**Job** - `820ffc95-c049-470f-9903-ef5339afe87f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_234334_820ffc95-c049-470f-9903-ef5339afe87f.mp4
**Attached, in submission order**
- `starting_frames/v24_c01_g1.png` · job `9c549b3c-52d9-45f1-b771-86c8687c9317` (start_image, and again as @Image 1 in image_references)
**md5** - `768382f682394d7002f2c0032c057138`

````text
START FRAME LOCK - HIGHEST PRIORITY: frame 0.0s is EXACTLY the supplied start image, @Image 1 is the same picture. Keep its wide framing for the whole clip: the whole double-height room is visible - the curved staircase with garland and stockings on the left, the fireplace and mirror, the sofa, the Christmas tree and the United States flag on the right - and the woman is seen from behind near the top of the tall wooden ladder in the middle of the frame, with her half-finished Christmas painting on the ceiling above her, the open paint bucket in her left hand and the paintbrush in her right. The camera never moves closer to her, never zooms in, never crops in and never reframes onto her; she stays the same small size in the frame as in the start image.

Real home video, shot on a hand-held iPhone by a person standing in the room a few steps behind her, phone held upright at chest height. One continuous shot. The camera stays in exactly the same spot for the whole clip with only tiny natural hand sway and micro-jitter - the small live breathing wobble of real hand-held phone footage, never a steady locked-off tripod look. It does not reframe, does not follow her, does not tilt, pan, zoom or push in. No phone, hand, fingers, thumb or arm ever appears in the foreground.

HARD RULE, THIS ONE FIRST: the whole clip is ONE single unbroken shot from the first frame to the last. No cut, no jump cut, no second angle, no scene change, no transition, no dissolve at any point. The motion runs continuously - every moment grows out of the moment before it, and her body never resets, jumps position or teleports between one part and the next.

For the first second she is just painting the ceiling - her right hand stroking the brush across the Christmas picture above her, the open paint bucket held up in her left hand, nothing dramatic.

Then, without any pause or break in the movement, she loses her footing and falls off the ladder to the floor. Her arms are still up and still coming down out of the painting motion as her balance goes - the painting and the fall are one unbroken piece of movement, not two separate actions.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug. The open paint bucket comes down with her in her left hand, hits the floor beside her and tips over, and thick red paint gushes out of it and spreads fast in a big glossy pool across the rug and the floor around her.

She lands hard and the movement carries straight on into stillness without a break - she settles, rocks slightly as her weight comes to rest, and stays down on the floor in the spreading red paint for the rest of the clip, not moving much, just stunned and breathing. Her chest is still moving and she is still there when the clip ends.

The paint is thick glossy red house paint and behaves like real paint: it pours, splashes and spreads in a flat puddle, with red spatter on her pyjamas and the rug. PAINT SOURCE: every drop of paint in the clip comes out of the one open bucket in her left hand. No paint ever appears from the brush or out of nowhere, and nothing drips from the ceiling. The Christmas painting on the ceiling stays exactly as it is the whole time.

No slow motion. No speed ramp, no speed change of any kind - the clip plays at one constant real-time speed from start to finish. No zoom, no push-in, no pan, no tilt. No captions or text.

Audio: room tone only, no music - the brush on the ceiling, a short gasp, the ladder hitting the floor, the bucket clanging and the paint splashing, then her breathing.

FALL AND FRAMING LOCK - CHECK THIS LAST: she drops straight down beside the ladder and lands on the rug right at the foot of the ladder, in the middle of the frame, in front of the coffee table and fully visible. She does not jump, step back or leap sideways off the ladder, and she does not land behind or under any furniture. The ladder, the bucket and the paint stay inside the frame. The camera keeps the start image's framing to the very last frame - the ceiling and the painting stay at the top of the picture; it never tilts down to follow her fall.
````

### C02 — Hands on the box

#### Image prompt — `starting_frames/v24_c02_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_144704_4f13ea50-1ad7-4579-bcbf-a9afbc7673da.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c02_g1.png` · Higgsfield media `bbfc652c-e9eb-4430-9b53-610b56917312`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`
**md5** - `fdc05d81ac8fa5ef9288770e51d6fce8`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 30, with fair skin with a light dusting of freckles and slender fingers, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is now a heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a festive English Tudor-revival dining room with cream lime-plaster walls framed by pale limed-oak half-timber posts and beams, a black wrought-iron candle chandelier, a carved stone fireplace with cranberry and forest-green knitted stockings, a limed-oak dresser with blue-and-white plates, and a Christmas tree dressed with cranberry-red, forest-green and gold glass baubles and warm white fairy lights. Every background detail stays in focus; the box remains dominant through its scale and placement.

Dress the dining table more festively: a sprig of fir and a few small pinecones, two or three small cranberry and gold glass baubles, a short cream candle, a soft warm string light trailing across the matte table surface, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and carton artwork only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### C03 — The projector lifted

#### Image prompt — `starting_frames/v24_c03_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `03992926-ec39-4527-bb57-1d0443957611`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_144947_03992926-ec39-4527-bb57-1d0443957611.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c03_g1.png` · Higgsfield media `4b0ce2fa-f22e-4fdc-a781-0a2f43789130`
- @Image 2: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**md5** - `dcdbb6926ee0c8530b0117e12f03dbc8`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's position and tilt in frame, with the larger size specified below, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 30, with fair skin with a light dusting of freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a cranberry-red cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same cranberry-red cable-knit wool sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - enlarge the projector to match the full-size product unpacked in C02 (@Image 2). The complete projector from black top mesh to the bottom of its stand fills approximately 42 percent of the frame height; the dome is approximately 46 percent of the frame width. Keep it just right of the centre line and a little above the middle, with every foot visible. Maintain realistic adult hand anatomy; the fingers spread naturally around the enlarged dome rather than enclosing a tiny palm-sized unit. Preserve the pose, camera angle and visible countertop wedge. No zoomed-out or miniaturised product.

THE PRODUCT - a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is now a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen: pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, deep depth of field with the entire kitchen sharply resolved.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C02 and owns the new woman's hands, sweater, photographic look and full-size carton-to-projector scale; the projector should plausibly fill that carton when unpacked; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### C04 — The cable going in

#### Image prompt — `starting_frames/v24_c04_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `4d260de1-556a-41ac-afe1-a8f708913c72`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_145136_4d260de1-556a-41ac-afe1-a8f708913c72.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c04_g1.png` · Higgsfield media `e243effc-2c21-4bed-9551-e592483315ca`
- @Image 2: `content/video_24_assets/starting_frames/v24_c03_g1.png` · Higgsfield media `03992926-ec39-4527-bb57-1d0443957611`
**md5** - `87b7857158df60228d8c00172cfd3209`

````text
COPY @Image 1's shot and action, with the specified larger product scale. Change only the product scale, hands, countertop material and kitchen described below. Preserve the actual product shape and black perforated top.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is approximately 46 percent of the frame width and the full projector including its stand fills approximately 42 percent of the frame height, matching the same full-size projector in @Image 2 and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a substantial matte-white rounded dome-shaped body on a separate white four-legged splayed stand, full-size rather than a miniature. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 30, with fair skin with a light dusting of freckles and slender fingers: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a cranberry-red cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME BODY, just above where the dome meets the stand, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is now a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A sharply resolved traditional Christmas kitchen across the top third of the frame: pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Balanced soft window fill and warm interior light, clean and even; realistic natural iPhone deep focus throughout.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 is this video's C03 and owns the enlarged product's physical dimensions relative to the hands, exact product identity, kitchen finishes, hands, sweater and photographic look; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### C05 — The door opens on the room — start frame

#### Image prompt — `starting_frames/v24_c05_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `afe8c961-388f-423a-9ade-7a7c05b20121`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_144948_afe8c961-388f-423a-9ade-7a7c05b20121.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c05_g1.png` · Higgsfield media `6a0df249-6245-439e-a380-e9bbdf6dc580`
- @Image 2: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**md5** - `e1412b0c9411fd48f78d4668607f1eb2`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the cranberry-red cable-knit wool sleeve and no jewellery, with fair skin with a light dusting of freckles, slender adult woman's fingers and short natural nails, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is now a deep forest-green painted oak plank door with black wrought-iron strap hinges, a satin finish and a pale limed-oak surrounding casing, an antique brass round knob and matching brass escutcheon, set in a cream lime-plaster wall. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear door surface visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest-green paint reads clearly as deep green, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

REFERENCE ROLES: @Image 1 owns the exact layout, product geometry, hand positions and camera. @Image 2 owns the established photographic look and product fidelity only; use the new hands, materials and background specified above. All parts of this photograph, including the background, are in crisp natural iPhone deep focus, no portrait mode, no bokeh, no blur.
````

### C05 F2 — The door opens on the room — room reference

#### Image prompt — `references/v24_c05_r1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `85ba004e-383a-478a-88e5-b67066ac8da9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_144702_85ba004e-383a-478a-88e5-b67066ac8da9.png
**References, in submission order**
- @Image 1: `content/video_11_assets/references/v11_c05_r1.png` · Higgsfield media `dda4701e-8d9d-4351-99f8-60bb9093cf68`
- @Image 2: `content/video_9_assets/references/v9_c05_r4.png` · Higgsfield media `1c500339-2855-45b6-bd9b-4c3633b5a272`
**md5** - `12500c44587ab9669c8f0625a949d1bd`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look; change the architecture and children to the descriptions below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

The boy is of about six with fair freckled skin and tousled copper-red hair; the girl is of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons. Both children are fully dressed for winter in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 1 - THE ROOM. Build a structurally believable room: a spacious double-height English Tudor-revival Christmas great hall with a high open-timbered GABLED CEILING: two broad cream lime-plaster roof planes rise to a crisp central ridge, crossed by three pale limed-oak king-post trusses with curved braces. Pale limed-oak half-timber posts, rails and diagonal braces divide the cream lime-plaster walls into large panels. A tall carved limestone chimney breast stands on the back wall with a deep stone hearth; a wall of tall leaded casement windows in pale limed-oak mullioned frames occupies the left wall and a wide limed-oak doorway sits on the right. Wide pale oak floorboards, a large deep forest-green velvet chesterfield sectional sofa, a round tan leather ottoman and a soft cream wool rug. Seen from the doorway; the new a deep forest-green painted oak plank door with black wrought-iron strap hinges, a satin finish and a pale limed-oak surrounding casing is open out of frame.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, cranberry-red, forest-green and gold glass baubles, tinsel and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cranberry-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 2 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping roof planes and their central ridge remain clearly three-dimensional, meeting at a crisp ridge line. The sleigh and the ceiling picture fold at the ridge and are foreshortened along each slope, running straight across the faces of the three limed-oak trusses and their curved braces, before continuing onto the walls. The tall limestone chimney breast receives a continuous picture with clear folds at its projecting corners. The limed-oak half-timber posts, rails and braces, the mullioned window frames, glazing bars and the doorway frame carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. THIS IS THE KEY CORRECTION FOR THIS SET: the exposed wood must visibly carry the picture. Every exposed piece of limed oak in shot - each truss, rafter, purlin, beam, brace, half-timber post and rail, window mullion, frame and glazing bar, the door and doorway casings, the skirting and the mantel - is painted over by the projection in the same full colour as the plaster beside it: the village, garlands, aurora, stars and snowflakes run straight across the face of the wood and bend at each edge, the wood grain showing faintly through the projected colour. No beam, frame or casing stays as a dark bare wooden stripe or an unlit outline. Only the window GLASS stays the dark night outside. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the soft cream wool rug, the forest-green velvet chesterfield sectional sofa, the round tan leather ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their cotton pyjamas catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

NATURAL, LESS CINEMATIC LOOK - one small notch more natural than a polished film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster, a painting or an advert. True-to-life colour and contrast exactly as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting, no heightened fantasy glow on the children, and no storybook-illustration or oil-painting finish on the projection. The projection is still dense, bright and colourful, but its colour sits a touch closer to real life - rich, not neon - and it reads as the real light of a home Christmas projector falling on real walls: the plaster texture and wood grain show faintly through it, and the shadows keep a little more ordinary room detail, with the furniture, rug and floor clearly readable in the soft spill.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the grain of the limed-oak half-timbering and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### C05 F3 — The door opens on the room — empty-room reference

#### Image prompt — `references/v24_c05_r2.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `207fb72f-8668-4fad-8a0a-4009eac963dc`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_144947_207fb72f-8668-4fad-8a0a-4009eac963dc.png
**References, in submission order**
- @Image 1: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield media `85ba004e-383a-478a-88e5-b67066ac8da9`
**md5** - `65bc0b056a5b652db4e9f7818500bed1`

````text
Edit the supplied image. Reproduce it exactly - the same English Tudor-revival Christmas great hall, the same open-timbered gabled ceiling, the same camera position, framing, lens and lighting, the same furniture, Christmas tree, fireplace, rug and the exact same projected Christmas artwork on the walls and ceiling, pixel for pixel wherever possible. The ONLY change: remove all children completely. The room is empty of people - no children, no adults, no pets. Where the children stood, show the floor, rug and sofa that were behind them, continuing naturally. Keep the projection, colours and sharpness unchanged. No text, no watermark.
````

### C06 — The bed bounce

#### Image prompt — `starting_frames/v24_c06_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a36295bc-fdfd-47c2-8bf2-b7b5cd062961`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_144947_a36295bc-fdfd-47c2-8bf2-b7b5cd062961.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c06_g1.png` · Higgsfield media `a11380c1-3dd8-4a0a-accc-481aec5fa3bf`
- @Image 2: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield media `85ba004e-383a-478a-88e5-b67066ac8da9`
**md5** - `0ad4ace3626059c7dab7b1391d30ebfd`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the same boy's identity, Christmas pyjamas and dense saturated photographic projection look for this video; place that boy in the different bedroom described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same natural low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with fair freckled skin and tousled copper-red hair, fully dressed for winter in a cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama set with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. Build a structurally believable room: a bright-proportioned English Tudor-revival bedroom with a high SHED CEILING: a single cream lime-plaster plane sloping up from the front of the room to the tall back wall, crossed by pale limed-oak rafters. A pale limed-oak panelled bed with a wide upholstered cream headboard is centred on the flat back wall between two tall leaded casement windows with pale limed-oak mullioned frames and glazing bars, the back wall divided by pale limed-oak half-timber posts and rails, white bedding with a cranberry-red knitted throw, limed-oak bedside chests, wide pale oak floorboards and a soft cream wool rug. The bed stays in the same place in the frame, leaving the room's ceiling geometry clearly visible.

It is night, all house lamps switched off. The bed keeps the bedding described above, with pillows and a knitted stocking. A small real Christmas tree with gold lights and cranberry-red and gold ornaments stands by the window.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every roof plane and seam, wall above the headboard, window jambs and lintels. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The single sloping ceiling plane remains clearly three-dimensional, meeting the walls at crisp lines. The sleigh and the ceiling picture are foreshortened along the slope, run straight across the faces of the limed-oak rafters, and fold at the wall line before continuing down the walls. The flat wall, the limed-oak half-timber posts and rails, the mullioned window frames and glazing bars and the cream headboard carry properly foreshortened portions of the same continuous projection across their faces. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. THIS IS THE KEY CORRECTION FOR THIS SET: the exposed wood must visibly carry the picture. Every exposed piece of limed oak in shot - each truss, rafter, purlin, beam, brace, half-timber post and rail, window mullion, frame and glazing bar, the door and doorway casings, the skirting and the mantel - is painted over by the projection in the same full colour as the plaster beside it: the village, garlands, aurora, stars and snowflakes run straight across the face of the wood and bend at each edge, the wood grain showing faintly through the projected colour. No beam, frame or casing stays as a dark bare wooden stripe or an unlit outline. Only the window GLASS stays the dark night outside. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The timber floorboards, the soft cream wool rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his cotton pyjama top catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

NATURAL, LESS CINEMATIC LOOK - one small notch more natural than a polished film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster, a painting or an advert. True-to-life colour and contrast exactly as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting, no heightened fantasy glow on the children, and no storybook-illustration or oil-painting finish on the projection. The projection is still dense, bright and colourful, but its colour sits a touch closer to real life - rich, not neon - and it reads as the real light of a home Christmas projector falling on real walls: the plaster texture and wood grain show faintly through it, and the shadows keep a little more ordinary room detail, with the furniture, rug and floor clearly readable in the soft spill.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the plaster, the crisp architectural edges of the ceiling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### C07 — The whole Christmas room

#### Image prompt — `starting_frames/v24_c07_g1.png` — FOR REVIEW

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `e02e1c3d-02cb-4e8d-add1-0d8fccdbe38a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_144948_e02e1c3d-02cb-4e8d-add1-0d8fccdbe38a.png
**References, in submission order**
- @Image 1: `content/video_11_assets/starting_frames/v11_c07_g1.png` · Higgsfield media `b5910d54-c9bd-4be4-9ae3-3b870ad2e793`
- @Image 2: `content/video_24_assets/references/v24_c05_r1.png` · Higgsfield media `85ba004e-383a-478a-88e5-b67066ac8da9`
**md5** - `4bd984c0fc25971ec4c7dffae36a62b9`

````text
Recreate @Image 1's camera, framing, scale and poses. Wholesome family Christmas scene. @Image 1 owns composition geometry only. @Image 2 owns the dense saturated photographic projection look and the identity of the children only; this is a different room of the same house, described below. Both reference images are generated stills, not photographs of a documented real house.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same natural low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. The same new children as @Image 2: a girl of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons; a boy of about six with fair freckled skin and tousled copper-red hair. Both fully dressed in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. Wholesome family Christmas scene.

CHANGE 2 - THE ROOM. Build a structurally believable room: a spacious double-height English Tudor-revival Christmas family room with a high VAULTED CEILING: two broad sloping cream lime-plaster planes rising to a crisp central ridge, with one heavy pale limed-oak ridge beam running along it and pale limed-oak purlins crossing each slope. Cream lime-plaster walls. A tall chimney breast of honey-coloured Cotswold stone stands on the back wall with a thick limed-oak beam mantel; a full-height wall of leaded windows in pale limed-oak mullioned frames and glazing bars fills the left wall and a wide limed-oak plank door sits on the right. A herringbone pale oak floor, a large camel-brown velvet sectional sofa, a round deep-green leather ottoman and a soft cream-and-cranberry Persian-style wool rug. A different room from @Image 2 - not the same living room - seen from the middle of the family room with the whole ceiling in shot.

It is night, all house lamps switched off. A real Christmas tree with warm gold lights, cranberry-red, forest-green and gold glass baubles, tinsel and wrapped gifts stands beside the fireplace. Evergreen garland with holly berries covers the mantel, with three cranberry-and-cream knitted stockings below. The projection is the main illumination.

CHANGE 3 - THE PROJECTION. ONE continuous Christmas panorama covers every visible wall and the entire ceiling, including the whole ceiling, every architectural plane and seam, every beam or cove, and the entire chimney breast all the way to the ceiling. No rectangle, no screen, no blank ceiling or wall patch. Architectural occlusion shadows remain real and narrow. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room. AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn.  HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely.  The material colour is overpowered by the projected colour; only surface texture and physical shadows remain legible through it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.   The two sloping plaster planes, the limed-oak ridge beam and the purlins remain clearly three-dimensional. The sleigh and the snowflakes fold at the ridge and continue straight across the faces of the ridge beam and the purlins, foreshortened along each slope, before continuing onto the walls. The tall stone chimney breast receives a continuous picture with clear folds at its two projecting corners. The limed-oak mullioned window frames, glazing bars and the limed-oak plank door carry the projection straight across their faces, with thin shadow breaks only at their actual edges. Bright imagery follows the built curves and planes, never a flat picture hovering across the room. All raised trim casts a real hard-edged shadow behind it. THE WOODEN FRAMES CARRY THE PICTURE TOO: the painted wooden window frames, sashes and glazing bars, the door and doorway casings, the skirting boards, the mantel and every other piece of wooden trim the beam crosses are covered by the same continuous projected imagery as the wall beside them - never left as bare white unlit outlines - with only a thin real shadow line at each edge. THIS IS THE KEY CORRECTION FOR THIS SET: the exposed wood must visibly carry the picture. Every exposed piece of limed oak in shot - each truss, rafter, purlin, beam, brace, half-timber post and rail, window mullion, frame and glazing bar, the door and doorway casings, the skirting and the mantel - is painted over by the projection in the same full colour as the plaster beside it: the village, garlands, aurora, stars and snowflakes run straight across the face of the wood and bend at each edge, the wood grain showing faintly through the projected colour. No beam, frame or casing stays as a dark bare wooden stripe or an unlit outline. Only the window GLASS stays the dark night outside. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room.  EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP: every elf, toy, ribbon, nutcracker detail, antler, snowflake, fir needle and window has precise edges. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The herringbone oak floor, the soft cream-and-cranberry Persian-style wool rug, the camel-brown velvet sectional sofa, the round deep-green leather ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Christmas figures, no gift village, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their cotton pyjamas read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

NATURAL, LESS CINEMATIC LOOK - one small notch more natural than a polished film still: this is a candid photo a parent snapped on an iPhone at home, not a movie frame, a poster, a painting or an advert. True-to-life colour and contrast exactly as they come straight out of the phone camera: no colour grading, no teal-and-orange grade, no vignette, no dramatic spotlighting, no heightened fantasy glow on the children, and no storybook-illustration or oil-painting finish on the projection. The projection is still dense, bright and colourful, but its colour sits a touch closer to real life - rich, not neon - and it reads as the real light of a home Christmas projector falling on real walls: the plaster texture and wood grain show faintly through it, and the shadows keep a little more ordinary room detail, with the furniture, rug and floor clearly readable in the soft spill.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the fine cotton weave of the pyjamas, the grain of the floorboards, the tooth of the drywall, the surface texture of the cream lime plaster and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### Clips - round 1 (verified 2026-09-25)

#### Video prompt — `clips/v24_c02_g1.mp4` — APPROVED (Daniel 2026-09-26)

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `a919c88f-65fd-4257-8a03-8b9a0414c62a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_173114_a919c88f-65fd-4257-8a03-8b9a0414c62a.mp4
**Attached, in submission order**
- start_image: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
- image: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `4f13ea50-1ad7-4579-bcbf-a9afbc7673da`
**md5** - `d5da8648cab80690775eafa8b951e656`

````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 4-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no zoom, no reframe. Every stage of the box opening is shown happening - the flap lifting, folding back and the hand reaching in - never skipped. The box, hands and table stay continuous frame to frame.

STARTING-FRAME AND PRINT LOCK - use the attached starting image exactly at frame 0, including the front-facing THEXMASGLOW carton. Keep the dark-red brand band, cream CHRISTMAS LIGHT PROJECTOR lettering, printed white projector and red remote, gold star/tree and gold village artwork visible and unchanged on that same rigid front panel throughout. The box stays upright and never rotates away. The left hand braces its lower side without covering the main artwork. Opening only bends the top flaps; it never erases the front printing.

AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. No video reference is attached. If any music appears anywhere in the 4 seconds the clip is wrong.

HAND ROLES - SECOND MOST IMPORTANT: THE RIGHT HAND opens the lid and then grips and lifts the projector alone. THE LEFT HAND stays braced against the lower left side of THE BOX from first frame to last, fingers resting below the main printed artwork. The left hand never lifts, follows the projector, gestures, reaches into the box or leaves the carton. It steadies the box on the table while the right hand and product rise. Exactly two hands with separate jobs: right hand carries the product, left hand anchors the carton.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. THE RIGHT HAND lifts it out and keeps going straight up until the projector and right hand leave the top of frame. At 4.0s the open carton remains on the table, held steady by THE LEFT HAND. The right hand never pauses to present the product.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image AND @Image 1 are the same approved image, attached as start_image and image reference. They alone control frame 0.0s, the exact printed box, hands, table, room, props and light. Begin on that exact view and animate it. No reference video, no alternate carton, no plain-box substitute.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a cranberry-red cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge fills the frame. The lit cream candle, fir sprigs, small pinecones, small cranberry and gold glass baubles and warm string lights stay exactly where they are in the start image. Behind them, sharply in focus, a festive English Tudor-revival dining room with cream lime-plaster walls framed by pale limed-oak half-timber posts and beams, a black wrought-iron candle chandelier, a carved stone fireplace with cranberry and forest-green knitted stockings, a limed-oak dresser with blue-and-white plates, and a Christmas tree dressed with cranberry-red, forest-green and gold glass baubles and warm white fairy lights. The same table, carton, decorations and background remain visible through the final frame.

[6] FIRST FRAME - exactly the supplied image: THE BOX closed and upright with its full printed front facing the camera; the right hand on the lid and the left hand bracing the lower side in their exact shown positions.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. THE LEFT HAND remains braced on the lower left side of THE BOX. THE RIGHT HAND slides its fingers under the front top flap and lifts it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - THE RIGHT HAND reaches into THE BOX and grips the upper side of THE PROJECTOR firmly with thumb and fingers, leaving the BLACK perforated mesh disc visible. THE LEFT HAND remains on the outside of THE BOX.
2.1-3.0s - THE RIGHT HAND lifts THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises. THE LEFT HAND remains planted on THE BOX.
3.0-3.6s - THE RIGHT HAND DOES NOT STOP. It keeps rising in the same continuous motion and carries THE PROJECTOR completely out of the top of frame. THE LEFT HAND stays on THE BOX at the same low height.
3.6-4.0s - THE PROJECTOR and THE RIGHT HAND are out of frame. THE LEFT HAND remains resting against the lower side of the open empty carton on the heavy pale limed-oak refectory dining table with open silvery grain, a matte waxed finish and a thick square edge, lid flaps folded back. The printed front artwork, candle, fir, baubles, fireplace and tree remain visible. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles against the left hand, which remains on the carton.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands: the right lifts the product; the left remains on the box throughout. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows the open printed box on the table with the left hand still bracing it.
BANNED: any music, song, score or soundtrack; the left hand rising with the projector, leaving the box, waving, hovering or disappearing; both hands lifting the product; the right hand pausing to present the product; the product still in frame at 4.0s; changing the supplied first frame, replacing the printed box with a plain green box, erasing or redesigning the wordmark, product illustration or lettering, turning the printed front away; the camera following the product; slow motion; an all-white product top, a front lens, a swivel head, a third hand; disappearing decorations; a second box; a cut; subtitles; added overlay text.
````

#### Video prompt — `clips/v24_c03_g1.mp4` — APPROVED (Daniel 2026-09-26)

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `8b7047c6-2f67-4d69-b083-03864340d9e2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_173231_8b7047c6-2f67-4d69-b083-03864340d9e2.mp4
**Attached, in submission order**
- start_image: `content/video_24_assets/starting_frames/v24_c03_g1.png` · Higgsfield media `03992926-ec39-4527-bb57-1d0443957611`
**md5** - `9ce7bef8937743c5ee6ac07da31ccfd4`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in cranberry-red cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every detail visible in the start image: a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy; behind it pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the left, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the limestone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the limestone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the limestone.
3.0-3.4s - the four feet of the stand touch the limestone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The counter is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the limestone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

#### Video prompt — `clips/v24_c04_g1.mp4` — APPROVED (Daniel 2026-09-26)

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `677de711-bb9b-4853-9fe8-789a51aef013`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_173232_677de711-bb9b-4853-9fe8-789a51aef013.mp4
**Attached, in submission order**
- start_image: `content/video_24_assets/starting_frames/v24_c04_g1.png` · Higgsfield media `4d260de1-556a-41ac-afe1-a8f708913c72`
**md5** - `b2298a6fcd1fd08a18a7f273d8e14b0e`

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
THE LEFT HAND - a woman's hand in a cranberry-red cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same cranberry-red cable-knit wool sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every detail visible in the start image: a pale honed limestone countertop with a soft fossil-flecked grain and a straight eased edge, honed matte rather than glossy; behind it pale limed-oak Shaker cabinets with black iron cup pulls, handmade cream zellige backsplash tiles, pale limed-oak ceiling beams, a deep cranberry-red enamel range set into the tall cabinet run on the right, clean warm under-cabinet lights, evergreen garland with red berries and tiny warm fairy lights across the upper cabinets, a small Christmas tree with cranberry-red and gold ornaments and red ribbon in the far corner. Preserve the same left/right placement and framing. The kitchen remains crisp and in focus. Do not remove the countertop or replace the kitchen.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the limestone and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the limestone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the limestone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.

PRODUCT SCALE LOCK: preserve the exact large full-size projector and its size relative to the adult hands in the supplied start frame. Never shrink it to a miniature; the black perforated mesh top, rigid white body and separate four-foot stand keep their proportions.
````

#### Video prompt — `clips/v24_c05_g1.mp4` — APPROVED (Daniel 2026-09-26)

**Settings** - seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on
**Job** - `0aa11eb0-619c-4ab5-9676-aee7a7468ce8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_173419_0aa11eb0-619c-4ab5-9676-aee7a7468ce8.mp4
**Attached, in submission order**
- start_image: `content/video_24_assets/starting_frames/v24_c05_g1.png` · Higgsfield media `afe8c961-388f-423a-9ade-7a7c05b20121`
- image: `content/video_24_assets/references/v24_c05_r2.png` · Higgsfield media `207fb72f-8668-4fad-8a0a-4009eac963dc`
**md5** - `6c493074d9c1b8b5a3e907af2d318cb0`

````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 5-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no dissolve, no zoom, no reframe. Everything in it happens continuously, frame to frame.

PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas picture on the walls and the open-timbered gabled ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. Only the projected picture is animated; the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in EVERY frame from the first to the last, independent of the camera. Only the drawn buildings, trees and the moon stay put; everything else in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is never parked with only its legs moving. It flies in one smooth sweeping arc from where it is first seen across the open-timbered gabled ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place every second and has crossed most of the ceiling by the end. The reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- NORTHERN LIGHTS: the green and violet aurora curtains along the upper walls ripple and billow continuously like silk in the wind - their folds roll sideways along the wall about one curtain-width every second while bright waves of green light run up and down through them. The aurora is never frozen.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY cottage chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the horse-drawn sleigh with its lanterns glides steadily along the lane with the horses trotting; the villagers walk along the street carrying their Christmas tree home; the children on sledges slide down the snowy hill; the amber cottage windows flicker.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall - flat light on the wall and ceiling surfaces, never real snow in the room.
- SKY AND LIGHTS: the silver full moon glows; golden stars twinkle; now and then a shooting star streaks across the ceiling; bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (5 s):
0-1s: the door opens onto the room; through the very first gap the sleigh is already flying and smoke is already rising from every cottage chimney and the aurora is already rippling.
1-2s: the sleigh team travels across the open-timbered gabled ceiling, clearly changing position, reindeer galloping; smoke columns climb the wall; the aurora curtains roll sideways; the horse-drawn sleigh glides along the lane; snow drifts down.
2-3s: the sleigh has flown on another quarter of the ceiling; the aurora billows; the villagers carry their tree along the street; the children sledge down the hill.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; the aurora ripples on; a shooting star streaks across.
4-5s: all of it still moving at the same pace in the final frame - sleigh flying, smoke rising, aurora rippling, horse-drawn sleigh gliding, snow falling.
All of this is flat projected light lying on the real lime plaster, the limed-oak trusses and half-timbering and the mullioned window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CHILDREN - SPELLBOUND BY THE CEILING AND ALWAYS MOVING. EXACTLY TWO CHILDREN exist in this clip - THE BOY and THE GIRL described below - and nobody else ever appears: no third child, no extra kids in the background, on the sofa or in the doorway, no adult. The room reference photo is EMPTY, so there is no pose or spot to copy. When the first gap of the door opens, both children are ALREADY in the middle and far side of the room, at least three metres from the door - never standing in or near the doorway, never lined up facing the camera, never side by side. They were already watching the projection before the door opened and they are completely amazed by it: mouths wide open, eyebrows raised, gasping and laughing, eyes glued to the flying sleigh on the ceiling. They keep moving the whole time and follow the sleigh with their eyes, arms and feet. Per second:
0-1s: in the very first gap THE BOY is already walking slowly backwards across the rug, head tipped far back, one arm stretched straight up pointing at Santa's flying sleigh; THE GIRL, a few steps away from him, is up on tiptoe with both hands pressed to her cheeks, mouth open, staring straight up.
1-2s: THE BOY keeps stepping backwards and turns his body to follow the sleigh as it flies overhead, his pointing arm tracking it across the ceiling; THE GIRL runs three quick little steps across the rug in the same direction the sleigh is flying, one hand reaching up toward it.
2-3s: THE BOY looks over at THE GIRL, points up again and shouts with excitement, then looks straight back up; THE GIRL spins round once on the rug with her arms out and her face turned up to the ceiling, laughing.
3-4s: THE GIRL does two small excited bunny-hops on the spot, landing back on the rug at real speed, pointing up at the rippling northern lights; THE BOY walks sideways past the ottoman with his head still tipped back, following the sleigh.
4-5s: both are still moving in the last frame - THE BOY still stepping and pointing up, THE GIRL trotting toward the Christmas tree while gazing up - never frozen.
They never stand still, never pose, never face the camera and never wait. Their feet stay on the floor: they never climb, jump onto or jump over the sofa, the ottoman or any furniture. Both stay in view: neither ducks behind furniture and pops up somewhere else. Real speed, real weight, grounded feet - no sliding, floating, slow motion or running in place. This child action never alters the camera movement.

CAMERA CONTINUITY: the entire five seconds are ONE slow, uninterrupted forward-and-upward glide. Forward travel and upward aim are coupled as one motion, already underway together in frame zero. Keep the same gentle pace and the same forward-to-upward ratio for every frame, including while the door opens and while crossing its sill. Travel only about 0.8 metres forward over the entire shot, with an even upward tilt of about 18 degrees over those same five seconds. The wreath, door-panel edges and later the back-wall details drift smoothly downward in the frame from the beginning while perspective advances very gently. There is no forward-only phase and no later tilt-only phase. Do not accelerate the beginning, hurry through the door, ease in, ease out, steepen the tilt, speed-ramp or catch up to an end composition. The final frame can remain near the threshold with the back wall, furniture and ceiling visible. The door opens naturally during the same slow glide; its opening is not a camera cue.

DIRECT ROOM ENTRY: the closed door in the start image is fitted directly into the great room's entrance wall and its far face opens straight into the furnished Christmas room shown in the room reference photo. ONE door, ONE thin normal threshold about 15 cm deep. The very first gap reveals the room itself, the already-moving children and the already-playing projection, close behind this door. No hall, foyer, vestibule, passage, empty approach space, second doorway or arch between this door and the room. The side doorway on the reference room's right wall is a lateral feature only and never lies ahead of the camera.

Wholesome family Christmas scene, children at home at Christmas.

TASK AND ASSETS: image-to-video, one continuous handheld phone POV take, vertical 9:16. The START IMAGE is frame 0.0s: a deep forest-green painted oak plank door with black wrought-iron strap hinges, a satin finish and a pale limed-oak surrounding casing fully closed with a wreath, a woman's hand with fair skin with a light dusting of freckles and a cranberry-red cable-knit wool sleeve on the brass knob. The ROOM REFERENCE IMAGE (attached as an image reference) controls only the room's architecture, furniture, colours and projected artwork; it contains no people and it is not an end frame, camera target or transition destination - never dissolve, cut, morph or snap into its composition. The two children come only from this text.

CONTINUOUS ACTION: during approximately the first 1.5 seconds the hand turns the knob and opens the door with a smooth, ordinary, unhurried push. The room behind it is already running: the projection is already playing and both children are already moving - the widening gap only uncovers more of a scene that was already happening. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain wood - no glowing strip, no coloured fringe, no bright seam in the gap. The shot ends during the same gentle glide with the back wall, furniture and ceiling still visible.

CAMERA - eye height, normal wide-angle phone lens, a steady natural phone glide as described. No zoom, orbit, fisheye, lens warping, stop, second move or cut. The camera is the person's eyes; no phone, screen or device in frame. Hold the sharpness and exposure of the start image - crisp phone footage, in focus from the first frame to the last.

AUDIO - dry documentary sound only: the handle, the door swinging, the children gasping, laughing and calling out in delight, their footsteps on the floor, quiet room tone. (no BGM). No subtitles.

ROOM AND IDENTITY - a spacious double-height English Tudor-revival Christmas great hall with a high open-timbered GABLED CEILING: two broad cream lime-plaster roof planes rise to a crisp central ridge, crossed by three pale limed-oak king-post trusses with curved braces. Pale limed-oak half-timber posts, rails and diagonal braces divide the cream lime-plaster walls into large panels. A tall carved limestone chimney breast stands on the back wall with a deep stone hearth; a wall of tall leaded casement windows in pale limed-oak mullioned frames occupies the left wall and a wide limed-oak doorway sits on the right. Wide pale oak floorboards, a large deep forest-green velvet chesterfield sectional sofa, a round tan leather ottoman and a soft cream wool rug.
THE BOY - a boy of about six with fair freckled skin and tousled copper-red hair. THE GIRL - a girl of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons. Both fully dressed in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks.

PROJECTED SCENE CONTENT - LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

BANNED - a third child or any extra people appearing at any moment; an adult; a child standing still, frozen, posed or waiting at any moment; the children standing in or next to the doorway when it opens; the children side by side or facing the camera; a child climbing onto or jumping on or over furniture; a child disappearing behind furniture and reappearing elsewhere; slow motion or floaty movement; a camera that moves, stops and moves again; a zoom; a cut; a glow along the door edge; light that grows or fills the room as the door opens; the projector unit visible; blur; music; subtitles.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the aurora does not ripple; the horse-drawn sleigh or the villagers do not travel; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture slides as one sheet; any projected shape floats in the room.
````

#### Video prompt — `clips/v24_c06_g1.mp4` — APPROVED (Daniel 2026-09-26)

**Settings** - seedance_2_5 · omni_reference · 720p · 5 s · 9:16 · audio on
**Job** - `c849f730-dead-468f-8ae7-4d94a85bc10b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_173419_c849f730-dead-468f-8ae7-4d94a85bc10b.mp4
**Attached, in submission order**
- start_image: `content/video_24_assets/starting_frames/v24_c06_g1.png` · Higgsfield media `a36295bc-fdfd-47c2-8bf2-b7b5cd062961`
- image: `content/video_24_assets/starting_frames/v24_c06_g1.png` · Higgsfield media `a36295bc-fdfd-47c2-8bf2-b7b5cd062961`
**md5** - `410d704c75559b37a8e99a0cc1d29dd0`

````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 5-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no dissolve, no zoom, no reframe. Everything in it happens continuously, frame to frame.

PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas picture on the walls and the shed ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. Only the projected picture is animated; the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in EVERY frame from the first to the last, independent of the camera. Only the drawn buildings, trees and the moon stay put; everything else in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is never parked with only its legs moving. It flies in one smooth sweeping arc from where it is first seen across the shed ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place every second and has crossed most of the ceiling by the end. The reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- NORTHERN LIGHTS: the green and violet aurora curtains along the upper walls ripple and billow continuously like silk in the wind - their folds roll sideways along the wall about one curtain-width every second while bright waves of green light run up and down through them. The aurora is never frozen.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY cottage chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the horse-drawn sleigh with its lanterns glides steadily along the lane with the horses trotting; the villagers walk along the street carrying their Christmas tree home; the children on sledges slide down the snowy hill; the amber cottage windows flicker.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall - flat light on the wall and ceiling surfaces, never real snow in the room.
- SKY AND LIGHTS: the silver full moon glows; golden stars twinkle; now and then a shooting star streaks across the ceiling; bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (while the camera tilts down):
0-1s: snow streams down the whole projection; the sleigh is already flying across the ceiling; smoke is already rising from every cottage chimney and the aurora is already rippling.
1-2s: the sleigh has flown a quarter of the way across the ceiling; smoke columns climb the wall; the aurora curtains roll sideways; the horse-drawn sleigh glides along the lane.
2-3s: the sleigh flies on across the ceiling; the aurora billows; the villagers carry their tree along the street; the children sledge down the hill.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; the aurora ripples on; a shooting star streaks across.
4-5s: sleigh flying, smoke rising, aurora rippling, horse-drawn sleigh gliding, snow falling - all still moving in the last frame.
All of this is flat projected light lying on the real lime plaster, the limed-oak rafters and half-timbering and the window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, the bed or the boy.

CAMERA - ONE slow, small tilt DOWN, the opposite of the other room clips in this set.
0.0s: the clip starts EXACTLY on the start image - the same framing, with the fully projected ceiling at the top of the frame. The camera never aims above this framing, so no part of the ceiling that is not in the start image ever appears, and every visible part of the ceiling is covered with the projection from the first frame - no bare plaster or bare wood anywhere.
0.0-4.0s: the camera tilts DOWN slowly and smoothly by about 10 degrees, like a calm parent filming: the projected ceiling slides up and partly out of the top of the frame while more of the bed, the covers and the rug come into view at the bottom. The boy stays fully in frame from head to feet.
4.0-5.0s: it eases to a gentle stop.
One continuous take: no cut, no zoom, no push-in, no pull-back, never a tilt up.

THE BOY BOUNCES LIKE A REAL CHILD ON A REAL MATTRESS - natural, believable and unexaggerated, at real speed for all five seconds. Small, springy, continuous bounces on the same spot in the middle of the bed: his feet leave the mattress by only about 10 to 20 centimetres, about two bounces per second, the soft mattress visibly sinking under his feet on every landing and pushing him back up. REAL-TIME SPEED, NOT SLOW MOTION: each bounce is quick and snappy, taking only about half a second from push-off to landing under normal gravity, exactly like a real child filmed at normal speed - the footage is never slowed down, never time-stretched and never dreamy. Knees soft, head tipped back, mouth open, laughing up at the ceiling in amazement. While he bounces he throws one arm straight up and points at Santa's sleigh, turning his head to follow it as it flies across the ceiling, then drops the arm and points again. His body keeps exactly the same size, proportions, face and clothing in every frame; he stays in the same spot on the bed. No high leaps, no hanging in the air, no floating, no hopping across the bed, no stiff puppet-like body, no morphing limbs.

Wholesome family Christmas scene, a child at home with his family at Christmas. Crisp real iPhone footage at night, handheld, real-time speed, sharp from first frame to last.

ASSET ROLES: the start image, also attached as the image reference, is the approved still that controls a bright-proportioned English Tudor-revival bedroom with a high SHED CEILING: a single cream lime-plaster plane sloping up from the front of the room to the tall back wall, crossed by pale limed-oak rafters. A pale limed-oak panelled bed with a wide upholstered cream headboard is centred on the flat back wall between two tall leaded casement windows with pale limed-oak mullioned frames and glazing bars, the back wall divided by pale limed-oak half-timber posts and rails, white bedding with a cranberry-red knitted throw, limed-oak bedside chests, wide pale oak floorboards and a soft cream wool rug. Preserve the exact child identity, clothing, furniture, colours and the full projected artwork of the start image; its framing is the FIRST frame of this clip.

SUBJECTS:
THE BOY - exactly one child, a boy of about six with fair freckled skin and tousled copper-red hair, fully dressed for winter in a cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama set with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks, standing on the bed. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the walls and the whole shed ceiling. Everything glowing on the plaster and the wood is that one cone landing.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing and gasping in delight. (no BGM). No subtitles.

DO NOT INCLUDE: a still, frozen or printed-looking projection; a projection that only twinkles; a sleigh parked in one place; chimneys without smoke; an aurora that does not ripple; a horse-drawn sleigh or villagers that do not travel; snow that does not fall; bare, white or unprojected ceiling or wall; a camera that starts higher than the start image; a camera that tilts up; zoom, push-in or pull-back; slow-motion or floaty jumping; high exaggerated leaps; the boy changing size or shape; real snow or particles in the air of the room; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
````

#### Video prompt — `clips/v24_c07_g1.mp4` — APPROVED (Daniel 2026-09-26)

**Settings** - seedance_2_5 · omni_reference · 720p · 4 s · 9:16 · audio on
**Job** - `0a8665a2-25e1-432e-954b-e835bbb51b53`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260925_173419_0a8665a2-25e1-432e-954b-e835bbb51b53.mp4
**Attached, in submission order**
- start_image: `content/video_24_assets/starting_frames/v24_c07_g1.png` · Higgsfield media `e02e1c3d-02cb-4e8d-add1-0d8fccdbe38a`
**md5** - `005a85a68ed88d40518aaf044c91b777`

````text
ONE CONTINUOUS TAKE - ABSOLUTE RULE: this 4-second clip is a single uninterrupted real-time shot from the start image to the last frame. No cut, no jump cut, no hidden edit, no time skip, no dissolve, no zoom, no reframe. Everything in it happens continuously, frame to frame.

OPENING STATE - frame 0.0s preserves the start image's complete, saturated projection on every visible wall, the chimney breast, the whole vaulted ceiling and every beam. The projector has been running for a long time before filming. Full coverage and brightness stay on for all four seconds while the drawn elements are already moving. There is no lighting-up, unveiling, growth, wipe or fade-in, and the ceiling artwork is never erased and redrawn.

Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children in a double-height Christmas family room are amazed by a projected Christmas picture that is PLAYING across the back wall and the entire vaulted ceiling, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical 9:16.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no washed-out exposure, no colour shift.

ASSET ROLES: the start image is frame 0.0s and controls a spacious double-height English Tudor-revival Christmas family room with a high VAULTED CEILING: two broad sloping cream lime-plaster planes rising to a crisp central ridge, with one heavy pale limed-oak ridge beam running along it and pale limed-oak purlins crossing each slope. Cream lime-plaster walls. A tall chimney breast of honey-coloured Cotswold stone stands on the back wall with a thick limed-oak beam mantel; a full-height wall of leaded windows in pale limed-oak mullioned frames and glazing bars fills the left wall and a wide limed-oak plank door sits on the right. A herringbone pale oak floor, a large camel-brown velvet sectional sofa, a round deep-green leather ottoman and a soft cream-and-cranberry Persian-style wool rug. Preserve the exact child identity, clothing, furniture, colours, full existing projection and opening framing.

SUBJECTS:
THE GIRL - a girl of about five with warm brown skin and dark curly hair in two puffs tied with red ribbons, on the sofa, caught mid-jump in the start image.
THE BOY - a boy of about six with fair freckled skin and tousled copper-red hair, on the rug in front of the sofa, back to camera and slightly to the side, looking up at the projected ceiling with his arms out.
Both in cranberry-red and cream Fair Isle-patterned brushed-cotton Christmas pyjama sets with little reindeer and snowflake bands, with matching loose pyjama trousers and cream wool socks. Both stay small in frame, in scale with the huge room. EXACTLY TWO CHILDREN - no third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole vaulted ceiling.
THE PICTURE - the animated scene is the exact Christmas panorama visible in the start image. LOW ALONG THE WALLS, a SNOWY NORTHERN-LIGHTS CHRISTMAS VILLAGE: half-timbered cottages with glowing amber windows and thick snow on their roofs, a curl of white smoke rising from every chimney, a horse-drawn sleigh with lanterns gliding down the lane, villagers carrying a Christmas tree home, children sledging down a hill, and tall snow-laden fir trees rising between them. Along the upper walls, strings of golden lights, red velvet bows and dense emerald garlands link the rooftops into a continuous Christmas panorama, and wide rippling curtains of green and violet aurora borealis rise from behind the hills. ACROSS THE CEILING, Santa's red sleigh and eight reindeer fly in a wide arc through the aurora past a big silver full moon, among twinkling golden stars and big glowing snowflakes, a long sparkling golden trail streaming behind them. Unmistakably Christmas Eve, glowing gold, cranberry red and aurora emerald dominant with snow-white accents against a near-black midnight sky. One dense continuous panorama of projected light across the architecture, no isolated sticker icons, no carnival, no galaxy, no vortex. No projected shape floats physically in the room.

PROJECTED ANIMATION - THE MOST IMPORTANT THING IN THIS CLIP. The Christmas picture on the walls and the vaulted ceiling is a hand-drawn ANIMATED CHRISTMAS CARTOON playing at full speed, like a TV screen showing an animated Christmas movie - never a still picture. Only the projected picture is animated; the room and the children stay real photographic phone footage. Every drawn element below moves with big, bold, easy-to-read motion at normal playback speed, in EVERY frame from the first to the last, independent of the camera. Only the drawn buildings, trees and the moon stay put; everything else in the picture travels.
- SANTA'S SLEIGH AND EIGHT REINDEER: the WHOLE TEAM TRAVELS across the ceiling - it is never parked with only its legs moving. It flies in one smooth sweeping arc from where it is first seen across the vaulted ceiling toward the far side, covering about one quarter of the ceiling's width every second, so the sleigh is in a clearly different place every second and has crossed most of the ceiling by the end. The reindeer's legs gallop, heads bob, the sleigh rocks and dips, and the golden trail streams and curls behind it.
- NORTHERN LIGHTS: the green and violet aurora curtains along the upper walls ripple and billow continuously like silk in the wind - their folds roll sideways along the wall about one curtain-width every second while bright waves of green light run up and down through them. The aurora is never frozen.
- CHIMNEY SMOKE: tall soft white smoke plumes stream continuously out of EVERY cottage chimney in the village, rising in long wavy columns up the wall, swaying and curling, each puff climbing about one roof height every second, widening and fading as fresh puffs push up from below. Several plumes are clearly rising at once, all the time.
- VILLAGE LIFE: the horse-drawn sleigh with its lanterns glides steadily along the lane with the horses trotting; the villagers walk along the street carrying their Christmas tree home; the children on sledges slide down the snowy hill; the amber cottage windows flicker.
- SNOWFALL: big projected snowflakes drift steadily down across the whole picture, about a quarter of the wall height every second, turning as they fall - flat light on the wall and ceiling surfaces, never real snow in the room.
- SKY AND LIGHTS: the silver full moon glows; golden stars twinkle; now and then a shooting star streaks across the ceiling; bright gold sparkle waves travel along the garlands and ribbons.
PER-SECOND ANIMATION TRACK (4 s):
0-1s: the sleigh team is already flying, reindeer galloping; smoke is already rising from every cottage chimney and the aurora is already rippling.
1-2s: the sleigh has moved a quarter of the ceiling and is crossing the silver moon; smoke columns climb the wall; the aurora curtains roll sideways; the horse-drawn sleigh glides along the lane.
2-3s: as the camera tilts up the sleigh flies on across the vaulted ceiling; the aurora billows; the villagers carry their tree along the street; the children sledge down the hill.
3-4s: the sleigh keeps flying toward the far side of the ceiling; new smoke puffs rise from every chimney; the aurora ripples on; a shooting star streaks across - sleigh flying, smoke rising, aurora rippling, horse-drawn sleigh gliding, snow falling, all moving in the final frame.
All of this is flat projected light lying on the real lime plaster, the limed-oak ridge beam and purlins, the Cotswold-stone chimney breast and the mullioned window frames: it bends with the surfaces, never floats into the room, and nothing is projected on the floor, furniture or children.

CHILDREN - AMAZED, AND ALWAYS MOVING:
THE GIRL lands from the jump shown in the start image onto the sofa cushions and keeps bouncing along the sofa with small, springy, real-speed bounces - her feet leave the cushion by only 15 to 25 centimetres, about two bounces per second, the cushion visibly sinking on every landing - moving a little further along the sofa with each bounce while she points one arm straight up at Santa's flying sleigh, head tipped back, mouth wide open, squealing with delight.
THE BOY walks slowly backwards across the rug with his head tipped far back, one arm stretched up pointing at the sleigh, turning his body to follow it as it flies across the ceiling; around 2 seconds he glances across at his sister, points up again and laughs, then keeps stepping and gazing up.
Neither child ever stands still, poses or faces the camera. Real children moving at real speed with real weight: quick, snappy bounces under normal gravity, never slow motion, never floating, never a high exaggerated leap, no morphing limbs.

TIMELINE (camera):
0.0-1.0s the person filming takes one small step forward; the frame moves in slightly and settles.
1.0-2.0s the camera holds in the closer position.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree, only far enough that the vaulted ceiling fills the upper half of the frame - it never tilts past the projected picture. The ENTIRE vaulted ceiling in view, every plane, beam and corner, is covered with the projection - starry midnight sky, the silver full moon, the snowflakes and the flying sleigh - no bare plaster, no bare wood, no unprojected corner anywhere in view. Both children stay low in the frame and keep moving.
No zoom - the only forward movement is the one small physical step.

AUDIO: room tone, two children laughing, gasping and squealing, cushions thumping, feet on a rug. (no BGM). No subtitles.

SURFACE MAPPING - The two sloping plaster planes, the limed-oak ridge beam and the purlins remain stationary. The drawings fold at the ridge and run across the faces of the ridge beam and purlins, fold around the Cotswold-stone chimney corners and carry across the limed-oak mullioned window frames, glazing bars and the limed-oak plank door, with correct surface perspective and occlusion. All physical architecture stays stationary.

DO NOT INCLUDE: bare, blank, white or partly unprojected ceiling, beam, corner or wall in any frame, especially at the end when the camera looks up; a camera that tilts up beyond the projected picture; a projection appearing, fading in or revealing itself; children standing still; slow motion; floating or weightless movement; a third child; an adult; any music; the projector unit in shot; a zoom; blur; a cut; on-screen text; subtitles.

MOTION GUARDRAILS - Failed if: the sleigh stays in one place or only its legs move; any chimney has no rising smoke; the aurora does not ripple; the horse-drawn sleigh or the villagers do not travel; snow does not fall; the picture moves only because the camera moves; the animation starts late, pauses or freezes at the end; the whole picture slides as one sheet; any projected shape floats in the room. Real-time speed, no slow motion, no music, no subtitles.
````
