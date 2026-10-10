# Video 35 — B-roll — exported video (initial round: starting frames)

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_35.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

Same seven-shot structure as v34 (C02–C08 plus a C06 animation companion frame), new houses,
new backgrounds, new Santa-vs-Grinch gags. One generation per shot.

**Change from v34:** C03 moves from a bed POV to a **living-room couch POV** — person sitting
back on a sofa, box flat across the lap, same first-person style and angle. v34's C03 anatomy
flaw ("she is like rotated") is guarded against with an explicit ANATOMY block.

Generated 2026-09-17.

## Generation settings

| | |
|---|---|
| model | `gpt_image_2` |
| resolution | `2k` (1520 × 2688) |
| quality | `medium` |
| aspect_ratio | `9:16` |
| count | 1 |
| use_unlim | false |
| workspace | Oneofone1 (`b2c97bd7-fedf-489d-b211-3de4e39dc90a`) |

## Reference media

| Role | id |
|---|---|
| store self-checkout POV (v19 C2) | `0c78d477-e3dd-4cec-bf67-8148d996d891` |
| bed POV (v19 C3) — used in v35 C03 for POV *style only* | `7329e69e-a7d9-495f-bdb3-750b9908752e` |
| ladder wide (v6 C4) | `8f80a2c0-3b8f-4490-a42d-ad17a9c43817` |
| ladder close (v6 C5) | `75cc4e34-3210-4f0f-9579-ad5a627135c6` |
| windowless box packshot | `3ca7d301-ed13-43cf-ab78-9900942bc250` |
| v33 C04 — garage framing + unlit curtain + phone | `e1ee11e2-11c4-4548-9f19-42e0ea71ed0a` |
| v33 C05 — wall-filling curtain, picket fence | `f8d942f2-70c2-4b4a-820a-54e099c7844e` |
| v33 C06 g2 — garage curtain, crowd, pastel wash | `08a6fdc9-6e1f-475c-a1ad-4a5740d54085` |
| bulb-artwork richness guide | `40058517-9846-48c1-88e3-d48519a63b52` |

## Job IDs

| File | job_id |
|---|---|
| `v35_c02_g1.png` | `5d7f2b94-6446-4bcf-a35e-a427bc4707e4` |
| `v35_c03_g1.png` | `f53983c6-ebab-4542-bd7d-901184f78984` |
| `v35_c04_g1.png` | `dd9d90f9-79e5-4792-bda0-209f97b65890` | rejected |
| **`v35_c04_g2.png`** | `01242684-615e-4bfe-be76-aaf56437f91e` | **keep** |
| `v35_c05_g1.png` | `940c5e2d-4958-4ea5-adad-121f9eacdd5a` | rejected |
| **`v35_c05_g2.png`** | `55a6a06f-4df9-49bc-b3c6-182c94af8510` | **keep** |
| `v35_c06_g1.png` | `c0339254-04bb-49ff-8d17-f49b42daec08` |
| `v35_c06_r1.png` | `a9cec9e7-aa44-4a1a-8780-14c39d38cdb0` |
| `v35_c07_g1.png` | `646ce417-da2b-410d-a602-20cb46e09178` |
| `v35_c08_g1.png` | `cbd75703-07a7-4b2d-8dc1-7e4969d83bac` |

Two waves. Wave 1 = C02, C03, C04, C06, C07, C08. Wave 2 = C05 (references the finished C04 job
for the house) and C06 anim (references the finished C06 job for the house and curtain).

## Houses and gags used in v35

| Shot | House / setting | Gag |
|---|---|---|
| C02 | upmarket department store, brass + pale wood, garland arch over the lane | — |
| C03 | living room: charcoal sofa, brick fireplace, three red stockings, tree right | — |
| C04 / C05 | honey-toned cedar shingle two-storey, white trim, dark green door | — |
| C06 | charcoal-grey lap siding, white carriage-style door, black gooseneck lights | — |
| C06 anim | same as C06 | tug-of-war over the last present |
| C07 | pale sage-green clapboard, grey shingle roof, deep red door | the sack swing |
| C08 | cream stucco with dark chocolate Tudor half-timber gable | the candy-cane duel |

Gags across v32–v35 stay non-repeating.

---

## C02 — store self-checkout POV

Refs: @Image 1 store POV (framing) · @Image 2 windowless box packshot

### Image prompt

```text
Use REFERENCE IMAGE 1 as the EXACT framing reference — match its camera position, camera height, angle, focal length and composition precisely. A first-person POV phone shot at a store self-checkout: two hands in cream ribbed-knit jumper sleeves hold a large flat rectangular product box up flat to the camera just above the scanner plate, the printed front face square to the lens, wrists angled slightly outward under the weight, forearms cropped at the bottom edge of frame, no body and no face. A metal shopping trolley at the left edge, the glowing self-checkout terminal and card reader at the right.

CHANGE THE BACKGROUND to a DIFFERENT store, still heavily decorated for Christmas: a smart upmarket department store at Christmas — a polished pale wood floor, warm brass and glass fittings, a tall arch of fresh green garland studded with warm white lights spanning over the checkout lane, a floor-to-ceiling display wall of red and gold glass ornaments glinting behind it, a pair of decorated flocked Christmas trees further back, soft warm downlights, blurred well-dressed shoppers carrying paper bags deeper in the hall.

THE BOX must match REFERENCE IMAGE 2 exactly — this is our real product packshot. A matte black rigid retail box, large and flat, roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands. Front panel from top to bottom: a large white condensed uppercase headline reading LED CURTAIN LIGHTS; a warm gold subline reading Create Your Own Magic; a red diagonal BEST SELLER ribbon flag across the top-right corner; one large photographic panel with a thin gold hairline border filling the middle and lower two thirds, showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door and warm fairy-lit trees either side; and a bottom row of five small gold line icons with white captions.

THE BOX IS CLOSED AND SEALED — CRITICAL. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap. The front is fully printed, opaque, closed cardboard.

SCALE: the box is big. The left hand grips the far left edge near the lower corner and the right hand the far right edge near the lower corner, thumbs flat on the printed front face, fingers wrapped around the sides toward the back. The hands must read SMALL relative to the box — each hand spans less than a quarter of the box width.

No text overlays, no captions, no watermarks, no readable brand names or logos on the store fittings, no writing anywhere in the photograph except the printing on the box itself.

Hyper-realistic photograph shot on an iPhone 15 Pro, razor-sharp focus on the box and the hands, absolutely no motion blur and no blurry areas, clean low-noise exposure, natural true-to-life colour, vertical 9:16.
```

### Video prompt

Refs on the video job: @Image 1 `v35_c02_g1.png` (start frame) · @Image 2 box packshot `3ca7d301-…`

```text
Vertical first-person point-of-view phone video inside a department store. The first frame of the video IS the start image, unchanged. The two hands holding the LED curtain lights box lower it and slide it face-down across the self-checkout scanner; the box tilts as the barcode passes over the glass and the screen flashes. The hands then lift the box, turn it away from the camera and drop it into the metal shopping cart on the left, the box landing flat with a small bounce and settle. The point of view follows the box down into the cart with a natural downward head tilt. Warm ceiling-light glare slides across the glossy printed cardboard as it moves. Shoppers and aisles stay blurred in the background. Handheld micro-shake, real phone-camera look, no zoom, no slow motion, no cinematic bokeh.

THE BOX IS CLOSED AND SEALED — CRITICAL, and it matches the SECOND reference image exactly. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap. The front is fully printed, opaque, closed cardboard: a large white condensed uppercase headline reading LED CURTAIN LIGHTS, a warm gold subline reading Create Your Own Magic, a red diagonal BEST SELLER ribbon flag across the top-right corner, one large photographic panel with a thin gold hairline border showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door, and a bottom row of five small gold line icons. Every letter stays rigid, sharp and correctly spelled — the print never warps, morphs or re-renders as the box moves. The box is BIG — roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands; each hand spans less than a quarter of the box width, and it keeps that size for the whole clip.

DO NOT CHANGE: the cream ribbed-knit jumper sleeves, the store, the polished pale wood floor, the brass and glass fittings, the tall arch of green garland studded with warm white lights spanning over the checkout lane, the display wall of red and gold glass ornaments behind it, the decorated flocked trees further back, the soft warm downlights, the exposure and white balance of the reference frame.

AUDIO: natural room sound only — no music, no score, no background song. Store ambience, the scanner beep, cardboard sliding on the scale platform, the box landing in the metal cart, distant trolleys and chatter. No voice.

LOOK: real phone-camera footage, soft warm store lighting, mild sensor noise, no cinematic bokeh, no colour grade, no lens flare, no text overlays, no captions, no watermark, no slow motion.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{5dd97495-…, start_image}`, `{3ca7d301-…, image_references}`.

**Job** `cfa18803-d890-4f1c-8e2d-f4717d717f84` → `clips/v35_c02_g1.mp4` · completed 2026-09-18.

Reused from v34 C02 — changed: the store nouns only, because v35 is a different shop —
"warehouse store" → "department store", and the DO NOT CHANGE list swapped from the v34
steel-truss ceiling / racking / poinsettias / garland on the checkout railing / hanging baubles
to the v35 polished pale wood floor, brass and glass fittings, the tall arch of green garland
with warm white lights over the checkout lane, the ornament display wall and the flocked trees;
LOOK "flat bright store lighting" → "soft warm store lighting" to match the frame. Camera,
timeline, hand action, box handling, AUDIO and the ban lists are byte-identical.


### Video prompt — take g2 (2026-09-18)

Daniel on g1: *“C2 — the shopping cart looks very fake and unnatural.”*

The cart is not a missing prop — it IS in `v35_c02_g1.png`, a chrome wire basket with a red
plastic top rail at the lower-left edge. In g1 seedance ignored it, invented a second cart
underneath the box late in the clip, and let the box drop into it weightlessly. So this is a
prompt edit on the same starting frame, not a new frame.

References: `starting_frames/v35_c02_g1.png` (`5dd97495-…`, start_image) + the box packshot
(`3ca7d301-…`, image_references) — unchanged from g1.

```
Vertical first-person point-of-view phone video inside a department store. The first frame of the video IS the start image, unchanged. The two hands holding the LED curtain lights box lower it and slide it face-down across the self-checkout scanner; the box tilts as the barcode passes over the glass and the screen flashes. The hands then lift the box, turn it away from the camera and lower it into the SAME shopping cart that is already standing at the lower-left edge of the first frame — the chrome wire-mesh basket with the red plastic handle bar along its top rail. The hands keep hold of the box the whole way down and set it into the basket under control, letting go only once it is resting; it leans against the wire and settles with real weight. The point of view follows the box down into the cart with a natural downward head tilt. Warm ceiling-light glare slides across the glossy printed cardboard as it moves. Shoppers and aisles stay blurred in the background. Handheld micro-shake, real phone-camera look, no zoom, no slow motion, no cinematic bokeh.

THE BOX IS CLOSED AND SEALED — CRITICAL, and it matches the SECOND reference image exactly. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap. The front is fully printed, opaque, closed cardboard: a large white condensed uppercase headline reading LED CURTAIN LIGHTS, a warm gold subline reading Create Your Own Magic, a red diagonal BEST SELLER ribbon flag across the top-right corner, one large photographic panel with a thin gold hairline border showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door, and a bottom row of five small gold line icons. Every letter stays rigid, sharp and correctly spelled — the print never warps, morphs or re-renders as the box moves. The box is BIG — roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands; each hand spans less than a quarter of the box width, and it keeps that size for the whole clip.

THE CART IS THE ONE ALREADY IN FRAME — CRITICAL. There is exactly one shopping cart in the video and it is the one visible at the lower left of the first frame: an open chrome wire-mesh basket on a bare steel tube frame, with a red plastic bar along the top rail. It stays where it is and does not slide, roll, grow, shrink, swap, duplicate or re-render. NO second cart, NO cart sliding or popping into frame, NO cart appearing out of nowhere underneath the box. The basket is REAL OPEN WIRE seen in three dimensions: the individual chrome rods keep their spacing and thickness, the gaps between them show the pale wood floor and the cart's own shadow underneath, and the far wall of the basket sits visibly behind the near wall. It is NOT a flat printed grid, NOT a solid-sided tub, NOT a plastic crate, and the mesh never warps, ripples, melts or changes pattern. The box is physically smaller than the basket opening and clearly fits inside it. The box never floats, hovers, hangs in mid-air, passes through the wire or drops from a height.

DO NOT CHANGE: the cream ribbed-knit jumper sleeves, the store, the polished pale wood floor, the brass and glass fittings, the tall arch of green garland studded with warm white lights spanning over the checkout lane, the display wall of red and gold glass ornaments behind it, the decorated flocked trees further back, the soft warm downlights, the exposure and white balance of the reference frame.

AUDIO: natural room sound only — no music, no score, no background song. Store ambience, the scanner beep, cardboard sliding on the scale platform, the box landing in the metal cart, distant trolleys and chatter. No voice.

LOOK: real phone-camera footage, soft warm store lighting, mild sensor noise, no cinematic bokeh, no colour grade, no lens flare, no text overlays, no captions, no watermark, no slow motion.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{5dd97495-…, start_image}`, `{3ca7d301-…, image_references}`.

**Job** `4ec82d6e-218b-4f25-97f0-ba2d3e8e5e6e` → `clips/v35_c02_g2.mp4` · completed 2026-09-18.

Changed from g1 — two edits, both about the cart, nothing else touched:
1. The drop sentence. “drop it into the metal shopping cart on the left, the box landing flat
   with a small bounce and settle” → the hands **lower** it into “the SAME shopping cart that is
   already standing at the lower-left edge of the first frame — the chrome wire-mesh basket with
   the red plastic handle bar along its top rail”, keeping hold the whole way down and letting go
   only once it is resting. A bounce was licensing the weightless drop.
2. A new THE CART IS THE ONE ALREADY IN FRAME block, modelled on the existing box block: one cart
   only, no second cart, no cart sliding or popping in, the basket is real open wire in three
   dimensions with the floor and its own shadow showing through the gaps, not a flat printed grid
   or a solid tub, and the box fits inside it and never floats or passes through the wire.

The box block, the DO NOT CHANGE list, the camera, AUDIO and LOOK are byte-identical to g1.


---

## C03 — living-room couch POV, box across the lap

Refs: @Image 1 bed POV (**POV style only** — its bedroom is explicitly rejected) · @Image 2 windowless box packshot

New for v35 at Daniel's request. Carries the ANATOMY block added after the v34 C03 rotation flaw.

### Image prompt

```text
Use REFERENCE IMAGE 1 ONLY as a guide to the POV STYLE, camera height and lens — a first-person phone shot looking down at the sitter's own lap, the box held flat and square to the camera. Do NOT copy its bed, its bedding or its bedroom.

THE SCENE — a person sitting back on a SOFA in a living room at night, shot from their own eyeline looking down: their own thighs and knees in soft charcoal-grey lounge trousers run away from the camera across the seat cushions, feet in thick cream knit socks resting on a low wooden coffee table at the far end of the frame, and the large flat rectangular product box lies flat ACROSS THEIR LAP, resting on the tops of the thighs, its printed front face square to the camera and fully visible. A cream chunky-knit throw is rumpled over the arm of the sofa beside them. No body above the waist, no hands, no face.

THE ROOM — a warm living room on a winter evening: a deep charcoal fabric sofa, a tall decorated Christmas tree with warm white lights and red and gold baubles standing to the right beyond the coffee table, a brick fireplace behind it with three red stockings hung along the mantel and a garland of greenery draped across it, a table lamp with a cream shade glowing warmly on the left, a rug over pale oak floorboards, warm low light throughout.

THE BOX must match REFERENCE IMAGE 2 exactly — this is our real product packshot. A matte black rigid retail box, large and flat, roughly 55 cm wide by 42 cm tall by 10 cm deep. Front panel from top to bottom: a large white condensed uppercase headline reading LED CURTAIN LIGHTS; a warm gold subline reading Create Your Own Magic; a red diagonal BEST SELLER ribbon flag across the top-right corner; one large photographic panel with a thin gold hairline border filling the middle and lower two thirds, showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door and warm fairy-lit trees either side; and a bottom row of five small gold line icons with white captions.

THE BOX IS CLOSED AND SEALED — CRITICAL. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap, the lid is not lifted and not removed. The front is fully printed, opaque, closed cardboard.

ANATOMY — CRITICAL. The legs are relaxed, straight and natural, both knees pointing the same way straight away from the camera, symmetrical, seen from directly above in a normal seated position. NO twisted torso, NO rotated hips, NO bent or impossible joints, NO third leg, correct human proportions throughout.

SCALE: the box is big — it spans the full width of the lap and overhangs the thighs on both sides.

No text overlays, no captions, no watermarks, no writing anywhere in the photograph except the printing on the box itself.

Hyper-realistic photograph shot on an iPhone 15 Pro, razor-sharp focus on the box, absolutely no motion blur and no blurry areas, clean low-noise exposure, warm natural true-to-life colour, vertical 9:16.
```

### Video prompt

Refs on the video job: @Image 1 `v35_c03_g1.png` (start frame) · @Image 2 box packshot `3ca7d301-…` · @Image 3 open box interior `f01fecfe-…`

```text
Animate the START IMAGE exactly as it is. The first frame of the video IS the start image, unchanged. The FIRST reference image is the product packshot - it is there ONLY to define exactly what the printed lid artwork looks like and how BIG the box is. The SECOND reference image is the open box interior - it is there ONLY to define exactly what is inside the box once the lid opens.

CAMERA - HELD IPHONE, FIRST-PERSON POV, LOCKED FRAMING: a genuine point-of-view shot, she is holding her own phone and looking down her own body as she sits back on the sofa. NO cuts, NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO crop, NO reframe. Only natural handheld micro-drift and the faint breathing rise and fall of her own chest behind the camera. One single continuous unbroken take, no cut, no jump, no reset.

START FRAME: first-person view looking down her own legs on a sofa. She wears soft charcoal-grey lounge trousers and thick cream knit socks, her feet resting on a low wooden coffee table at the far end of the frame. A large matte-black rigid magnetic LED CURTAIN LIGHTS box lies flat ACROSS HER LAP, resting on the tops of her thighs, with its printed front face toward the camera, the lid fully CLOSED, hinged along the FAR edge. No hands are in frame yet. Warm out-of-focus living room light behind — the tall decorated Christmas tree standing to the right beyond the coffee table, the brick fireplace with three red stockings along the mantel and a garland of greenery across it, the cream-shaded table lamp glowing on the left.

ACTION TIMELINE - THE HANDS COME IN AND THE LID OPENS FROM THE FRONT:
0.0-0.7s - both of her own hands rise into frame from the bottom edge and reach onto the box, fingertips hooking under the NEAR FRONT EDGE of the closed lid, knuckles flexing with visible pressure, and the magnets release with a small firm snap.
0.7-2.2s - THE FRONT EDGE OF THE LID LIFTS FIRST and the lid pivots up and back on its hinge at the far edge in one smooth controlled motion, the printed top face rotating up and away from the camera as the gap widens along the front, opening to roughly seventy degrees and staying there, still attached, never detached, never lifted off, never carried out of frame. Her wrists rotate naturally with it. The box rocks very slightly on her lap and her thighs shift a little under the weight, then settle.
2.2-4.0s - the open interior is revealed and held, exactly as the SECOND reference image: a fitted matte-black cardboard tray holding the LED curtain light set itself - thin BLACK wire strings with small round bulbs coiled and folded into neat flat coils side by side, completely UNLIT - and beside the coils a small printed instruction booklet and a slim white plastic remote control seated in their own cut-outs, all against a matte black interior. The contents settle very slightly as the light reaches them. One hand releases the lid and lowers a little; the other steadies the base. The box stays resting on her lap and never floats or slides off.

HARD RULES: the lights stay completely OFF and dark for the whole clip - no glow, no sparkle, no light coming out of the box, no illumination on her hands or her legs. Nothing is ever lifted out of the box. The lid is never detached and never falls off. No extra objects appear. Exactly two hands are ever in frame, each with exactly five fingers at all times. Her face is never visible - this is her own point of view.

PRODUCT - LOCKED TO THE FIRST REFERENCE IMAGE: the lid is matte black and carries, exactly as in the packshot, the bold white condensed headline LED CURTAIN LIGHTS, the warm-gold subtitle Create Your Own Magic, a red diagonal BEST SELLER corner flag, a night photo panel of a house facade with a glowing LED Christmas tree on the garage, and gold feature icons along the bottom. It is NOT a plain box, NOT a different product, NOT a generic package. There is NO transparent window, NO clear plastic panel and NO die-cut cutout anywhere on the printed face. Every letter stays rigid, sharp and correctly spelled - the print never warps, morphs or re-renders as the lid rotates.

SIZE - THE BOX IS BIG: roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands. Each of her hands spans less than a quarter of the box width, and the box spans the full width of her lap and overhangs her thighs on each side. It keeps that size for the whole clip and never shrinks into a small gift box.

DO NOT CHANGE: the soft charcoal-grey lounge trousers, the cream knit socks, her legs, the deep charcoal fabric sofa, the low wooden coffee table, the cream chunky-knit throw rumpled over the arm of the sofa, the tall decorated Christmas tree on the right, the brick fireplace with its three red stockings and its greenery garland, the cream-shaded table lamp on the left, the rug over the pale oak floorboards, the exposure and white balance of the reference frame.

AUDIO - NO VOICE: the soft magnetic pop of the lid releasing, cardboard flexing, a faint rustle as the wire strings settle, the sofa cushions shifting, quiet room tone. NO music, NO narration, NO voice-over, nobody speaks in this shot.

LOOK: real phone-camera footage, natural warm indoor light, mild sensor noise, no cinematic bokeh, no colour grade, no lens flare, no text overlays, no captions, no watermark, no slow motion.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{9f0028fb-…, start_image}`, `{3ca7d301-…, image_references}`, `{f01fecfe-…, image_references}`.

**Job** `779198ed-555b-4b8f-89aa-2e7c8a8e6bc4` → `clips/v35_c03_g1.mp4` · completed 2026-09-18.

Reused from v34 C03 — changed: bed → sofa and the room nouns that follow from it, because the
v35 frame is a living room — "lies propped up on the bed" → "sits back on the sofa", the flannel
pyjama bottoms → charcoal-grey lounge trousers, the duvet → feet on a low wooden coffee table,
the attic ceiling / green velvet headboard / brass bedside lamp → the tall decorated tree, the
brick fireplace with three red stockings and a greenery garland, and the cream-shaded table lamp;
the box now lies ACROSS HER LAP on the tops of her thighs instead of across her shins, so "shins"
→ "lap"/"thighs" in the rock, the size lock and the stay-put rule, and "bedding shifting" → "the
sofa cushions shifting" in AUDIO. CAMERA, the beat timings, the lid mechanics, the box size lock
in cm and every ban list are byte-identical.

---

## C04 — install, wide, from the lawn

Refs: @Image 1 ladder wide (framing)

### Image prompt

```text
Use REFERENCE IMAGE 1 as the EXACT framing and composition reference — match its camera position, camera height, distance, angle, focal length and the placement of every element in the frame. Change ONLY the house and its surroundings.

A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

FRAMING — copied from REFERENCE IMAGE 1. The camera stands out on the snowy front lawn, level, far enough back that the whole front of a two-storey house fills the frame with sky above it. An aluminium extension ladder leans against the house at the upper left, and a man in a dark winter jacket, tan work trousers and boots stands high on it with one arm reaching up to the roofline, fixing the top of the light curtain under the eaves. He is seen from behind and slightly below; no face detail.

THE HOUSE — a DIFFERENT house from the reference. A two-storey HONEY-TONED CEDAR SHINGLE house — warm golden-brown weathered wood shingles laid in neat overlapping rows across the whole facade, crisp white window trim, a covered front porch with slim white posts and a DARK GREEN front door with a red-bow wreath, a warm black lantern beside the door, thick green garland spiralled up each porch post. Warm lit windows on the ground floor. Snow-laden shrubs along the foundation and two small snowy fir trees at the right edge. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey-green.

THE LIGHT CURTAIN — a huge dense curtain of warm white string lights hangs flat over the whole front bay of the upper storey, spanning almost the full width of that wall, its top edge tucked just under the eaves where the man is working, its bottom hem uneven and wavy where the strands end at slightly different heights. It is built from many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles and the white window mullions read clearly through the gaps between strands, and the lit windows behind glow through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
```

### Video prompt

Refs on the video job: @Image 1 `v35_c04_g2.png` (start frame)

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house with crisp white trim and a dark green front door, same aluminium extension ladder at the upper left, same dense warm-white LED curtain hanging over the front bay of the upper storey, same blue-hour navy sky, same snow. Nothing changes.

ACTION: he is installing the LED curtain. He reaches up with both hands, presses the top rail of the curtain flat against the wall and works it onto its clips, fingers adjusting the top edge. Then he grips the curtain and gives it THREE small shakes — the whole net of hanging LED strands sways and ripples, individual strands swinging out and settling back with real weight and momentum, a few strands untangling as they drop. He shifts his weight on the ladder rung and the ladder flexes a fraction. Cold breath visible.
0.0-0.7s — both hands press the top rail flat against the cedar shingles just under the eaves, thumbs pushing a clip closed.
0.7-1.7s — FIRST SHAKE: he takes hold of the curtain and gives it one firm shake; the whole net swings out to one side and ripples back, strands swaying across the full width.
1.7-2.7s — SECOND SHAKE, a little harder; the strands swing out again, a couple of tangled strands fall free and settle at a new length, the ladder flexes a fraction.
2.7-4.0s — THIRD SHAKE, then he lets go and steadies the top rail with one hand; the strands ripple, slow and settle. His breath fogs.

The LED strands keep exactly the same brightness, colour and state they have in the first frame — they do not turn on, off, or change pattern; they only move because the curtain is being shaken. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — FIRST-PERSON POV, WALKING FORWARD. The person filming takes A FEW SLOW STEPS FORWARD across the snowy front lawn toward the man on the ladder, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house and the ladder grow steadily and continuously larger and NEVER recede. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the snow-laden boxwood shrubs and the small snowy fir trees at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect. No cuts.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy lawn ahead.

HARD RULES: no other people, no cars, no pets enter frame. The man is seen from behind and slightly below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, boots crunching on packed snow with each stride, the aluminium ladder ticking and flexing, a plastic clip snapping shut, the faint rattle of the light strands, breath. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, slight motion blur on the walk, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{e96d3a3b-…, start_image}`.

**Job** `d1fd7102-2050-4897-a6ef-d06fd5a746c5` → `clips/v35_c04_g1.mp4` · completed 2026-09-18.

Reused from v34 C04 — changed: the house nouns only, because v35 is a different house —
"terracotta-red brick colonial with white trim and black shutters" → "honey-toned cedar shingle
two-storey house with crisp white trim and a dark green front door", and every later mention of
"the brick" → "the cedar shingles" (the 0.0-0.7s clip press and the SEE-THROUGH curtain line).
The walking-forward POV CAMERA block, the HARD NEGATIVE — NO PHONE IN SHOT block, all three shake
beats with their time ranges, the black-wire rule, AUDIO and LOOK are byte-identical.


### Video prompt — take g2 (2026-09-18)

Daniel on g1: *“In the beggining the lights should be turned on for C5 but I like them much
better this way so I want the lights off for C4 too.”*

C05 g1 came out with the curtain unlit even though `v35_c05_g2.png` is lit — seedance treats the
start image as a reference, not a hard frame 1, and drifted. Daniel prefers the unlit look, so C04
has to be made to agree on purpose rather than by accident. Same starting frame as g1.

Reference: `starting_frames/v35_c04_g2.png` (`e96d3a3b-…`, start_image) — unchanged from g1.

```
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house with crisp white trim and a dark green front door, same aluminium extension ladder at the upper left, same dense LED curtain hanging over the front bay of the upper storey but with the curtain SWITCHED OFF — unlit, dark bulbs on black wire, not glowing, same blue-hour navy sky, same snow. Nothing changes.

ACTION: he is installing the LED curtain. He reaches up with both hands, presses the top rail of the curtain flat against the wall and works it onto its clips, fingers adjusting the top edge. Then he grips the curtain and gives it THREE small shakes — the whole net of hanging LED strands sways and ripples, individual strands swinging out and settling back with real weight and momentum, a few strands untangling as they drop. He shifts his weight on the ladder rung and the ladder flexes a fraction. Cold breath visible.
0.0-0.7s — both hands press the top rail flat against the cedar shingles just under the eaves, thumbs pushing a clip closed.
0.7-1.7s — FIRST SHAKE: he takes hold of the curtain and gives it one firm shake; the whole net swings out to one side and ripples back, strands swaying across the full width.
1.7-2.7s — SECOND SHAKE, a little harder; the strands swing out again, a couple of tangled strands fall free and settle at a new length, the ladder flexes a fraction.
2.7-4.0s — THIRD SHAKE, then he lets go and steadies the top rail with one hand; the strands ripple, slow and settle. His breath fogs.

The LED strands are SWITCHED OFF for the whole clip — dark, unlit bulbs on black wire, no glow, no warm white light, no colour, no twinkle, no pattern, no light spilling onto the cedar shingles or the snow from the curtain. They never light up at any moment; they only move because the curtain is being shaken. The only light on the house is the warm glow from the windows, the porch lantern and the small lights on the door wreath and the porch garland, exactly as in the first frame. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — FIRST-PERSON POV, WALKING FORWARD. The person filming takes A FEW SLOW STEPS FORWARD across the snowy front lawn toward the man on the ladder, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house and the ladder grow steadily and continuously larger and NEVER recede. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the snow-laden boxwood shrubs and the small snowy fir trees at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect. No cuts.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy lawn ahead.

HARD RULES: the LED curtain never illuminates — not at the start, not on a shake, not at the end. No other people, no cars, no pets enter frame. The man is seen from behind and slightly below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, boots crunching on packed snow with each stride, the aluminium ladder ticking and flexing, a plastic clip snapping shut, the faint rattle of the light strands, breath. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, slight motion blur on the walk, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{e96d3a3b-…, start_image}`.

**Job** `86a77228-96c9-4fd3-b865-1528d15aee20` → `clips/v35_c04_g2.mp4` · completed 2026-09-18.

Changed from g1 — three edits, all of them the lights state, nothing else touched:
1. Opening inventory: “same dense warm-white LED curtain hanging over the front bay” → “same dense
   LED curtain hanging over the front bay … but with the curtain SWITCHED OFF — unlit, dark bulbs
   on black wire, not glowing”.
2. The state paragraph. “The LED strands keep exactly the same brightness, colour and state they
   have in the first frame — they do not turn on, off, or change pattern” → “The LED strands are
   SWITCHED OFF for the whole clip — dark, unlit bulbs on black wire, no glow, no warm white
   light, no colour, no twinkle, no pattern, no light spilling onto the cedar shingles or the snow
   from the curtain”, plus a line naming the windows, porch lantern, wreath and porch garland as
   the only light on the house. Inheriting the state from the frame was the thing to remove: the
   frame is lit.
3. HARD RULES gained “the LED curtain never illuminates — not at the start, not on a shake, not
   at the end”.

The three shake beats with their time ranges, the walking-forward POV CAMERA block, the
HARD NEGATIVE — NO PHONE IN SHOT block, the black-wire and SEE-THROUGH rules, AUDIO and LOOK are
byte-identical to g1.



### Video prompt — take g3 (2026-09-18)

Daniel on g2: *“C04 - the shake it’s kinda too agressive, like the man it’s mad on the lights, I
don’t like it.”*

Cause: the g2 beats were inherited from v34 and **escalate** — “one firm shake”, then “a little
harder”, then a third. Escalation is what reads as anger. The fix is a prompt edit on the same
starting frame, not a new still: all three shakes made identical in size and speed, wrist-only,
with the ladder held still and an explicit ban list.

Reference: `starting_frames/v35_c04_g2.png` (`e96d3a3b-…`, start_image) — unchanged from g1/g2.

```
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house with crisp white trim and a dark green front door, same aluminium extension ladder at the upper left, same dense LED curtain hanging over the front bay of the upper storey but with the curtain SWITCHED OFF — unlit, dark bulbs on black wire, not glowing, same blue-hour navy sky, same snow. Nothing changes.

ACTION: he is installing the LED curtain. He reaches up with both hands, presses the top rail of the curtain flat against the wall and works it onto its clips, fingers adjusting the top edge. Then he takes the curtain lightly in one hand and gives it THREE SMALL, GENTLE SHAKES from the wrist — the unhurried, careful movement of someone settling the strands straight, not yanking them. The net sways softly and the strands swing a few centimetres and settle back under their own weight, one or two untangling and dropping to a straight hang. He stays balanced and relaxed on the ladder rung. Cold breath visible.
0.0-0.7s — both hands press the top rail flat against the cedar shingles just under the eaves, thumbs pushing a clip closed.
0.7-1.7s — FIRST GENTLE SHAKE: he takes hold of the curtain near the top and gives it one soft, small shake from the wrist; the strands sway a few centimetres to one side and settle back, a slow ripple travelling down the net.
1.7-2.7s — SECOND GENTLE SHAKE, exactly as soft as the first; the strands sway again by the same small amount, a couple of tangled strands slip free and settle at a new length. The ladder does not move.
2.7-4.0s — THIRD GENTLE SHAKE, then he lets go and steadies the top rail with one hand; the strands ripple softly, slow and settle straight. His breath fogs.

The LED strands are SWITCHED OFF for the whole clip — dark, unlit bulbs on black wire, no glow, no warm white light, no colour, no twinkle, no pattern, no light spilling onto the cedar shingles or the snow from the curtain. They never light up at any moment; they only move because the curtain is being shaken. The only light on the house is the warm glow from the windows, the porch lantern and the small lights on the door wreath and the porch garland, exactly as in the first frame. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — FIRST-PERSON POV, WALKING FORWARD. The person filming takes A FEW SLOW STEPS FORWARD across the snowy front lawn toward the man on the ladder, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house and the ladder grow steadily and continuously larger and NEVER recede. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the snow-laden boxwood shrubs and the small snowy fir trees at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect. No cuts.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy lawn ahead.

THE SHAKES ARE GENTLE — CRITICAL. This is a calm, patient man tidying the strands straight, and the whole clip is unhurried. All three shakes are the SAME small size and the SAME slow speed — they never escalate. No hard yank, no tug, no jerk, no wrenching, no whipping, no rattling, no violent or angry motion, no frustration, no fast or snappy movement, no shaking with both arms, no wide swinging of the net, no strands flying out sideways, no jolt through the ladder. His shoulders and body stay still and easy; only the forearm and wrist move.

HARD RULES: the LED curtain never illuminates — not at the start, not on a shake, not at the end. No other people, no cars, no pets enter frame. The man is seen from behind and slightly below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, boots crunching on packed snow with each stride, a plastic clip snapping shut, the faint soft rustle of the light strands, breath. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, slight motion blur on the walk, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{e96d3a3b-…, start_image}`.

**Job** `79af1fd7-736e-446b-bc1b-c8cb817a7412` → `clips/v35_c04_g3.mp4` · completed 2026-09-18 · 4.05 s · md5 `c8f7a1a4ac4a818129ff1ee787bc5fa7`.

Changed from g2 — five edits, all of them the shake, nothing else touched:
1. ACTION sentence: “Then he grips the curtain and gives it THREE small shakes — the whole net …
   swinging out … He shifts his weight on the ladder rung and the ladder flexes a fraction” →
   “Then he takes the curtain lightly in one hand and gives it THREE SMALL, GENTLE SHAKES from the
   wrist — the unhurried, careful movement of someone settling the strands straight, not yanking
   them … He stays balanced and relaxed on the ladder rung.”
2. Beat 0.7-1.7s: “FIRST SHAKE … one firm shake; the whole net swings out to one side” →
   “FIRST GENTLE SHAKE … one soft, small shake from the wrist; the strands sway a few centimetres
   to one side and settle back, a slow ripple travelling down the net.”
3. Beat 1.7-2.7s: “SECOND SHAKE, a little harder … the ladder flexes a fraction” →
   “SECOND GENTLE SHAKE, exactly as soft as the first … The ladder does not move.” The escalation
   is the line that had to go.
4. Beat 2.7-4.0s: “THIRD SHAKE” → “THIRD GENTLE SHAKE”, strands “ripple softly, slow and settle
   straight”.
5. New block before HARD RULES: “THE SHAKES ARE GENTLE — CRITICAL”, banning yank, tug, jerk,
   wrenching, whipping, rattling, angry or frustrated motion, both-arm shaking, wide swinging of
   the net, strands flying sideways and any jolt through the ladder — only forearm and wrist move.

AUDIO was made to agree: “the aluminium ladder ticking and flexing … the faint rattle of the light
strands” → “a plastic clip snapping shut, the faint soft rustle of the light strands”. Asking for
a ticking ladder contradicts “the ladder does not move”.

The beat **time ranges**, the walking-forward POV CAMERA block, the HARD NEGATIVE — NO PHONE IN
SHOT block, the lights-OFF paragraph, the black-wire and SEE-THROUGH rules, HARD RULES and LOOK are
byte-identical to g2.

Flagged, not fixed — in this take the walk ends with the man high on the ladder and cropped at the
top edge of frame, and the unlit curtain is hard to read against the shingles. The shake itself is
now calm.


---

## C05 — install, closer and lower, same house

Refs: @Image 1 ladder close (framing) · @Image 2 `v35_c04_g1` job (the house — must match exactly)

Generated in a second wave so it could reference the finished C04 job and inherit the house.

### Image prompt

```text
A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

CAMERA AND FRAMING — copy this EXACTLY from REFERENCE IMAGE 1. This is the same house and the same moment as REFERENCE IMAGE 2, just seen from much closer and lower: the camera has moved in toward the house and around to the LEFT, standing low on the snow and looking up and along the front facade at an angle, so the wall runs away from the camera in perspective rather than sitting square-on. The aluminium extension ladder dominates the LEFT side of the frame, running steeply up out of the top-left corner, and the man in the dark winter jacket, tan work trousers and boots is higher on it now, up near the roofline with one arm reaching to the eaves, seen from behind and below with no face detail. Snow-laden evergreen shrubs fill the bottom foreground of the frame.

THE HOUSE — IDENTICAL to REFERENCE IMAGE 2 in every detail. The SAME two-storey HONEY-TONED CEDAR SHAKE SHINGLE house: warm tan-brown weathered wood shingles covering the whole facade, crisp white trim and white eaves, tall white-framed multi-pane sash windows with white shutters, the white columned front portico at the right with deep green garland spiralled up the column, the DARK GREEN front door with its red-bow wreath, the warm brass lantern hanging in the porch ceiling, snow-laden evergreen shrubs and small snow-covered conifers along the foundation. Same shingle colour, same white trim, same portico, same green door. Do NOT invent a different house, a different colour or a different style. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey.

THE LIGHT CURTAIN — the SAME huge dense curtain of warm white string lights as in REFERENCE IMAGE 2, now seen much closer and at an angle so the individual strands and bulbs are clearly resolved. It hangs flat over the front bay of the upper storey, its top edge tucked under the eaves where the man is working, its bottom hem uneven and wavy. It is built from many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles and the white window mullions read clearly through the gaps between strands, and behind one upstairs window a lit Christmas tree glows through the curtain from inside the house. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
```

### Video prompt

Refs on the video job: @Image 1 `v35_c05_g2.png` (start frame)

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house, same aluminium extension ladder dominating the left of frame, same dense warm-white LED curtain, same close low angle looking up and along the facade, same snow-laden shrubs in the bottom foreground, same blue-hour navy sky. Nothing changes.

ACTION: he continues installing the LED curtain from this angle. He raises both hands to the top rail, presses it against the wall and hooks it into place, thumbs pushing a clip closed. Then he takes hold of the curtain and gives it ONE firm shake — the full net of LED strands swings out and ripples, strands swaying out and settling back with real weight and momentum, a couple of tangled strands falling free. He adjusts his footing on the ladder rung and leans in slightly. Cold breath visible.
0.0-1.0s — both hands rise to the top rail, press it flat against the cedar shingles under the eaves and push a clip closed.
1.0-1.6s — he slides one hand down, grips the curtain and gives it ONE firm shake; the whole net swings out to one side.
1.6-2.8s — the strands ripple back across the full width with real weight, a couple of tangled strands drop free and settle at a new length; the ladder flexes a fraction.
2.8-4.0s — he adjusts his footing on the rung, leans in slightly and steadies the top rail with one hand; the strands slow and settle. His breath fogs.

The LED strands keep exactly the same brightness, colour and state they have in the first frame — they do not turn on, off, or change pattern; they only move because the curtain is being shaken. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time, and the lit Christmas tree behind the upstairs window keeps glowing through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH, portrait, exactly the framing of the start image, feet planted. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO CUT. The house stays the same size in frame throughout. The ONLY permitted camera move is a small gentle TILT UP across the clip, a few degrees, as if the person filming lifts their phone slightly to follow his hands up toward the eaves — a tilt only, never a rise, never a zoom, never a step forward.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snow-laden shrubs.

HARD RULES: no other people, no cars, no pets enter frame. The man is seen from behind and below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, the aluminium ladder ticking and flexing, boots shifting on a rung, a plastic clip snapping shut, the faint rattle of the light strands, breath, light wind. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{ceda1595-…, start_image}`.

**Job** `e2f1c20f-e0be-4788-ba00-c76e67f71133` → `clips/v35_c05_g1.mp4` · completed 2026-09-18.

Reused from v34 C05 — changed: the house nouns only, the same swap as C04 because C04 and C05
are the same wall — "terracotta-red brick colonial" → "honey-toned cedar shingle two-storey
house", and "the brick" → "the cedar shingles" in the 0.0-1.0s clip press and in the SEE-THROUGH
curtain line. The locked-off-plus-tilt CAMERA block, the single shake beat, the ladder and shrub
framing, AUDIO and LOOK are byte-identical.

---

## C06 — garage door, unlit curtain, phone in hand

Refs: @Image 1 v33 C04 (framing + unlit curtain + phone)

The unlit curtain failed to render on v34 C06. Fixed here by (a) strengthening the visibility
language — *"and it MUST be clearly visible"*, *"the dark strands stand out plainly against the
pale door"*, *"there is no bare patch of door anywhere"* — and (b) choosing a WHITE carriage
door so the black strands contrast. It rendered correctly on g1.

### Image prompt

```text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a driveway.

CAMERA AND FRAMING — copy this exactly from REFERENCE IMAGE 1. The camera stands on the driveway directly in front of a double garage door, square-on and level, close enough that the door fills almost the whole frame: the lintel and the two lit lamps across the top, snow-dusted concrete driveway across the bottom. Night, dark sky, the only light coming from the two lamps.

THE HOUSE — a DIFFERENT house from the reference. The garage wall is CHARCOAL GREY HORIZONTAL LAP SIDING — dark slate-grey painted boards running side to side in long horizontal lines. NOT green, NOT vertical, NOT board-and-batten, NOT brick, NOT stucco, NOT white. The double garage door itself is WHITE CARRIAGE-STYLE with raised rectangular panels, decorative black strap hinges and handles, and a row of small square windows across the top, framed by crisp white trim, with a warm-glowing BLACK GOOSENECK BARN LIGHT mounted on the charcoal siding above each end of the door.

THE CURTAIN — DENSE, exactly as dense as in REFERENCE IMAGE 1, and it MUST be clearly visible. A light curtain hangs over the whole white garage door from a header cable pinned under the lintel. Many, many thin BLACK vertical wires hung very close together side by side with only a narrow gap between neighbouring strands, covering the full width and full height of the door from edge to edge, wall to wall, top to bottom, each wire carrying small round bulbs spaced along it. Right now the bulbs are UNLIT and dark, so the curtain reads as a fine dense veil of black vertical dotted lines laid over the white door — the dark strands stand out plainly against the pale door, and you can still clearly see the door's panel seams and its row of small square windows through them. The veil covers the ENTIRE door: there is no bare patch of door anywhere, and it does not stop partway down. The bottom hem is uneven and wavy where the strands end at slightly different heights, and the strands sag a little. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet — it is separate hanging strings with visible gaps between them.

EVERY STRAND IS IDENTICAL — CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the curtain to the other, top to bottom. There must be NO section anywhere in the sheet where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice — only plain vertical strands hanging straight down.

THE PHONE — from the bottom edge of the frame a bare right hand rises into shot holding a phone upright, screen facing the camera, tilted very slightly, the phone sitting in the lower centre of the frame in front of the garage door. On the screen: a black app background, a TWO-COLUMN grid of small square scene tiles each showing a simple blue-and-white pixel-art Christmas picture, and a large round blue play button centred below the grid. The screen is sharp, bright and clearly readable. No words or labels anywhere on the screen.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph.
```

---

## C06 anim — same garage door, lit, the tug-of-war over the last present

Refs: @Image 1 `v35_c06_g1` job (house + framing + curtain) · @Image 2 richness guide

Structure mirrors `p33.P["c04anim"]`. Generated in wave 2 so it could chain off the finished C06 job.

**Known issue on g1:** the lit rectangle sits noticeably narrower and higher than the curtain in
C06 — the door reads closer to single-width, the driveway glow spill is missing, and there is a
large empty band below the figures. Flagged rather than re-rolled.

### Image prompt

```text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a driveway — the exact same house, same garage door and same camera position as REFERENCE IMAGE 1.

THE HOUSE AND FRAMING — identical to REFERENCE IMAGE 1: CHARCOAL-GREY horizontal lap siding, a CREAM / OFF-WHITE carriage-style double garage door filling almost the whole frame, square-on and level, with its row of small square black-paned windows across the upper section, black strap hinges and black centre handles, a white-painted surround, a warm-glowing BLACK GOOSENECK BARN LIGHT above each end, snow-dusted concrete driveway across the bottom, dark night sky. NO hand and NO phone in this photograph — the frame is completely clear of them.

THE CURTAIN IS NOW LIT and showing a picture across the whole garage door.

CRITICAL — HOW THE LIGHTS ARE BUILT. This is NOT an LED video wall, NOT a TV screen, NOT a projection, NOT a printed banner and NOT a pixel display. It is the same hanging curtain of string lights as in REFERENCE IMAGE 1: many separate thin BLACK wires hung close together side by side from a header cable under the lintel, each wire carrying small round bulbs. The whole picture is drawn in VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is a little wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square matrix. The curtain is SEE-THROUGH — through the gaps you plainly read the cream carriage door behind it, its panel seams and its row of small square windows, and the unlit areas are just dark garage door with dull grey unlit bulbs and faint black wires, NOT a solid coloured field and NOT a bright grey or white glowing background. Every lit bulb is a point source with a blown-out white core, a coloured halo and a small star flare, individually countable. The strands sag slightly and the bottom hem is uneven and wavy; the glow bounces back off the door as a soft halo and spills onto the snowy driveway in a speckled, uneven pattern.

HOW DETAILED AND BEAUTIFUL THE PICTURE IS — THE MOST IMPORTANT INSTRUCTION. This is a PREMIUM, EXPENSIVE, PROFESSIONALLY DESIGNED commercial Christmas light display, and the artwork must look it. The bulb grid is FINE and HIGH RESOLUTION — many hundreds of small bulbs across the width — so the characters are richly and skilfully drawn: proper expressive faces with real eyes, eyebrows and open mouths, confident clean outlines, folds and shading in the fabric, fur trim that actually reads as soft fur, highlights and shadow giving the figures roundness and volume, smooth flowing curves in the arms and body. Gorgeous, polished, eye-catching artwork. It is absolutely NOT a crude blocky 8-bit pixel sprite, NOT jagged, NOT clumsy, NOT a chunky Minecraft or cross-stitch chart, NOT low resolution, NOT a child's drawing. The only coarseness in the image comes from the physical gaps between the hanging strands — never from the drawing itself being clumsy or low-detail.

BUILT TO BE ANIMATED — READ THIS BEFORE DRAWING THE PICTURE. The picture contains exactly TWO large characters plus ONE simple prop, and nothing else. No crowds, no small background figures, no confetti, no arcs, no debris, no speed lines, no stars, no falling snowflakes, no scattered decorations. Roughly half of the curtain rectangle stays completely black and empty. Both characters are FULL FIGURES drawn at the same large size as each other, head to foot, planted firmly on the same ground line with their weight clearly readable, and clearly separated by a wide band of dark unlit curtain. Neither character is small, partial, hidden or cropped. The joke reads from held physical force one frame before it gives way — a strain frozen at its peak, not an action already finished.

THE PICTURE IN THE LIGHTS — THE TUG-OF-WAR OVER THE LAST PRESENT, seen side-on. In the CENTRE, between them, hangs ONE big square GOLD-WRAPPED PRESENT with a bright red ribbon cross and bow, lifted clear of the ground. On the LEFT stands Santa in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, both white-gloved hands clamped on the left edge of the present, leaning hard back and away to the LEFT with his heels dug in and his body at a steep angle, face screwed up with effort and his mouth wide open shouting. On the RIGHT stands the Grinch, a tall vivid lime-green figure in a red Santa hat and a red coat, both green hands clamped on the right edge of the same present, leaning hard back and away to the RIGHT at the same steep angle, heels dug in, teeth bared in a straining grin, eyes squeezed shut. They are stretched apart in a perfectly balanced deadlock, the present taut between them, held exactly one frame before it rips in half. The two figures and the one present are the ONLY things in the picture. Everything else is black unlit curtain.

The entire picture is contained INSIDE the rectangle of the curtain and touches none of its edges — both figures sit wholly within the lit rectangle with a clear margin all the way around, heads well below the top edge, boots well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the siding, the lintel, the sky or the driveway.

ABSOLUTELY NO text, letters, numbers, words or writing anywhere in the lights or anywhere else in the photograph.

COLOUR IS THE POINT. This is a full-colour RGB curtain and the shot has to sell that. Santa's coat is a deep saturated red with brilliant white fur trim, the Grinch is a vivid lime green, the present is bright gold with a vivid red ribbon. The picture must never collapse into a single warm-white or single-blue wash. Use REFERENCE IMAGE 2 ONLY as a guide to how rich, detailed and colourful bulb artwork looks — do NOT copy its subject matter or its composition.

Fully clothed cartoon figures, a silly slapstick pose and nothing more. No nudity, no bare skin beyond the green cartoon arms and face.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
```

### Video prompt

Refs on the video job: @Image 1 `v35_c06_g1.png` (unlit start frame) · @Image 2 `v35_c06_r2.png` (redrawn lit artwork, style guide only)

```text
THE FIRST FRAME OF THIS VIDEO IS THE START IMAGE, PIXEL FOR PIXEL, UNCHANGED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT.

WHAT IS IN THE START IMAGE, AND WHAT MUST THEREFORE BE IN FRAME 1: night, a suburban driveway shot on a held iPhone in portrait, square-on to the house; a wide CREAM / OFF-WHITE CARRIAGE-STYLE sectional double garage door with raised rectangular panels, black strap hinges, black centre handles and a row of small square black-paned windows across the top, set in CRISP WHITE trim; CHARCOAL-GREY HORIZONTAL LAP SIDING around it, dark slate-grey painted boards running side to side in long horizontal lines; ONE BLACK GOOSENECK BARN LIGHT mounted on the charcoal siding above each end of the door, one left and one right, both glowing warm downward; a snow-dusted concrete driveway across the bottom; the unlit BLACK LED curtain hanging flat across the garage door — and in this start image it is DENSE AND CLEARLY VISIBLE, reading as a fine dense veil of black vertical dotted lines and small dull unlit dots laid over the pale cream door, covering the entire door from edge to edge with no bare patch of door anywhere; and AT THE BOTTOM OF FRAME, A BARE RIGHT HAND RISING IN FROM THE BOTTOM EDGE HOLDING AN IPHONE UPRIGHT IN THE LOWER CENTRE OF FRAME, screen toward camera, showing a simple two-column grid of small blue preview tiles with a large round blue PLAY BUTTON at the bottom centre of the screen. Do NOT start on an empty driveway. Do NOT start on a bare garage door. Do NOT have the hand enter frame later. The hand and the phone are ALREADY THERE in frame 1, exactly as in the start image, rising in from the bottom edge.

THE SECOND ATTACHED IMAGE IS NOT A FRAME OF THIS VIDEO. It is only a style guide showing what the lit artwork must look like once the lights come on. Never cut to it, never start on it, never copy its framing, never copy its camera height, never copy its distance. Take from it ONLY the drawing that appears in the bulbs.

THE ARTWORK THAT APPEARS IN THE LIGHTS — THE TUG-OF-WAR OVER THE LAST PRESENT, seen side-on. In the CENTRE, between the two of them, hangs ONE big square GOLD-WRAPPED PRESENT with a bright red ribbon cross and bow, lifted clear of the ground. On the RIGHT stands the green character — a short, chunky, stocky green cartoon goblin with SMOOTH hairless kelly-green skin, a big round ball head with fat cheeks and no muzzle, a small round button nose, big round white eyes with small black pupils, short ROUNDED ears, short stubby arms and short bandy legs, chunky three-fingered mitten hands, a floppy FOREST-GREEN pointed cap with a white pom-pom, a mustard-yellow scarf and brown ankle boots — not tall, not lanky, no fur, no long muzzle, no pointed ears, NEVER named, simply the green character — both chunky mitten hands clamped on the right edge of the present, leaning hard back and away to the RIGHT at a steep angle, heels dug into the ground line, teeth bared in a straining grin, eyes squeezed shut. On the LEFT stands SANTA in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, both white-gloved fists clamped on the left edge of the same present, leaning hard back and away to the LEFT at the same steep angle, heels dug in, face screwed up with effort and his mouth wide open shouting. The two figures and the present are the ONLY things in the picture. The row of small square windows of the garage door reads through the top of the curtain behind the picture. Do NOT invent a different picture.

HOW THE LIGHTS MUST STAY BUILT. The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the lintel, each wire carrying small round bulbs. The whole picture is built out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix. The curtain is SEE-THROUGH: through the gaps between strands you clearly read the cream carriage door behind it, its panel seams and its row of small square windows, and the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark door, with unlit bulbs as tiny dull grey dots and the thin BLACK wires as faint vertical lines. Every lit bulb is a tiny point source: blown-out white core, coloured halo, small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing. The strands sag slightly, each ends at a slightly different height so the bottom hem is uneven and wavy, and the glow bounces back off the door as a soft halo and spills onto the snowy driveway in a speckled uneven pattern.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH, portrait, exactly the framing of the start image. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO CUT. The garage door stays the same size in frame throughout. The ONLY permitted camera move is a small gentle TILT UP in the second half of the clip, a few degrees, as if the person filming lifts their phone slightly to take in the whole door.

REAL TIME — NORMAL 1x SPEED. No fast motion, no sped-up playback, no time-lapse, no speed ramp.

THE PHONE SCREEN SCROLLS ONCE, EARLY, AND THEN STOPS FOR GOOD. In the first half-second the two-column grid of blue preview tiles physically TRAVELS UP THE GLASS under the moving thumb: whole rows slide upward and off the top edge while fresh rows rise in from the bottom. ONE swipe only. The instant the thumb presses play the screen is FINISHED — the grid freezes, the thumb stops moving, and nothing on the glass ever scrolls, slides or shifts again for the rest of the clip.

THE HAND LEAVES AND NEVER COMES BACK. THIS IS A HARD REQUIREMENT AND THE MOST COMMON WAY THIS SHOT FAILS. The hand and the phone are in frame for the first third of the clip ONLY. After the play press the hand drops straight down and out through the bottom edge in one smooth unhurried movement, the way you lower your arm to your side. From that moment on there is NO hand, NO phone, NO screen, NO thumb, NO fingers, NO wrist, NO sleeve and NO glow from a screen anywhere in frame — the bottom of the frame is bare snowy driveway. The hand does not linger, does not hover at the edge, does not rise back in, and is NOT still holding the phone at the end of the clip. A phone visible in the final second is a TOTAL FAILURE.

THE ANIMATION IN THE LIGHTS IS A REAL TUG-OF-WAR PLAYING AT NORMAL SPEED. Each action has room to read: a strain, a heave, a give. Every movement follows through and settles before the next one begins, the way two people actually move. It is lively and continuous, never frantic — a blur of limbs changing every few frames is a FAILURE, and so is a static or barely-moving picture.

TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.5s — exactly the start image, the curtain dark and unlit. The thumb is already pressed against the glass and SWIPES UP once: the whole two-column grid of blue tiles scrolls upward with it, the top row sliding up and off the top edge of the screen while a new row of tiles rises in from the bottom edge, then decelerating and settling, leaving the big round blue PLAY BUTTON at the bottom centre of the screen.
0.5-0.7s — the thumb slides onto the blue PLAY BUTTON and presses it. The button dips and highlights under the press. The grid behind it is now completely frozen and never moves again.
0.7-0.9s — IN THE SAME FRAME, without any cut, the whole LED curtain snaps ON at once, the tug-of-war appearing all together in chunky bulbs, and warm coloured light floods across the snowy driveway.
0.9-1.4s — the hand lowers steadily and smoothly straight down and out through the bottom edge of frame. By 1.4s the hand and the phone are COMPLETELY GONE from the picture and never return. Nothing is left along the bottom edge but snowy driveway.
1.4-4.0s — the camera drifts gently upward a few degrees and the tug-of-war gag plays out in FOUR unhurried beats, each one given enough time to read clearly:
1.4-2.0s — THE STRAIN. Both figures lean further back and away from each other, heels skidding a little along the ground line, the gold present stretched taut between them; Santa's white beard swings out sideways and the green character's pom-pom cap tips back off his forehead.
2.0-2.6s — SANTA HEAVES. Santa hauls back on the present hand over hand and drags the green character a full step toward him, both brown ankle boots skidding along the ground line, his short stubby arms pulled out straight in front of him.
2.6-3.2s — THE GREEN CHARACTER HEAVES BACK. He digs both boots in, throws his whole weight backward and drags Santa a step the other way, Santa's big black boots skidding along the ground line and his white beard swinging forward across his face.
3.2-4.0s — THE PAYOFF. The red ribbon gives all at once, the present pops free, and both figures drop flat on their backs along the ground line with their boots up, the gold present bouncing once on the ground line between them and settling there.
Each pose is rendered by bulbs switching on and off row by row across the grid — chunky and stepped, never smooth morphing, never a crossfade. NO BEAT IS EVER A BRIGHTNESS CHANGE: every beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.

MOTION QUALITY — HARD RULE: from 1.4s onward the two figures are moving continuously, but as WHOLE BODIES with real weight, not as a flicker of separate parts. Arms swing from the shoulder, bodies lean into a heave and follow through past it, boots skid and settle, the present swings and jerks between them. An arm that teleports between poses, a limb that changes length, a figure that jitters in place or a body that dissolves and reforms is a FAILURE.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER LEAVES THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the door. No green arm, no green foot, no white glove, no boot, no gold present and no trailing red ribbon ever crosses outside the curtain rectangle. At every instant every figure keeps a clear margin of at least two full unlit strands of dark door inside every edge of the curtain. If a pose would take a limb or the tugged present out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Both figures keep their feet on the same ground line and stay low and contained; nothing launches upward out of the picture. Nothing lit ever appears on the crisp white trim, the charcoal-grey lap siding, the black gooseneck barn lights, the sky or the driveway except as reflected spill.

EVERYTHING ELSE IS UNCHANGED: the house, the cream carriage door, the two black gooseneck barn lights, the charcoal-grey lap siding, the snow and the camera position are identical from first frame to last. No people, no cars, no pets enter frame.

NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural sound only — no music, no score, no background song. Cold quiet suburban night ambience, a soft phone tap, a faint electrical hum and tick from the lights, a distant car, light wind. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{c719b16c-…, start_image}`, `{c80b46fc-…, image_references}`.

**Job** `854da8b0-617f-49e8-875d-0fa402474a60` → `clips/v35_c06_g1.mp4` · completed 2026-09-18.

Reused from v34 C06 (the g2 thinned version Daniel approved) — changed: the house nouns and the
gag, because v35 is a different garage and a different picture. House: chestnut-brown stained-wood
door → CREAM / OFF-WHITE CARRIAGE-STYLE door with raised panels, black strap hinges and centre
handles; DARK BRONZE trim → CRISP WHITE trim; SAND-TAUPE STUCCO → CHARCOAL-GREY HORIZONTAL LAP
SIDING; the terracotta roof tiles dropped (not in the v35 frame); BLACK WALL SCONCE → BLACK
GOOSENECK BARN LIGHT. The unlit curtain description flipped from "VERY SUBTLE … faint thin dark
vertical lines" to "DENSE AND CLEARLY VISIBLE … no bare patch of door anywhere", because that is
what the v35 start frame actually shows. Gag: THE SNOWBALL AMBUSH → THE TUG-OF-WAR OVER THE LAST
PRESENT, so the artwork paragraph, the framing line ("a wind-up, a throw, an impact" → "a strain,
a heave, a give"), the 0.7-0.9s line and the four named beats were rewritten — but the beat
STRUCTURE is untouched: still exactly FOUR beats on the same 1.4-2.0 / 2.0-2.6 / 2.6-3.2 / 3.2-4.0
ranges, the eight-event thinning that fixed v34 C06. Containment list: the shovel and snowball →
the gold present and trailing red ribbon; MOTION QUALITY "lean into a throw" → "lean into a
heave". The pixel-for-pixel opening rule, the style-guide paragraph, the CAMERA block, REAL TIME,
the phone-scroll block, THE HAND LEAVES block, the whole 0.0-1.4s timeline, the bulb-render rules,
NO TEXT, AUDIO and LOOK are byte-identical.

First submission `58ffd974-2dc2-405f-ae52-ef0b36cd99e9` was refused with `ip_detected` after
several minutes of rendering; the identical payload was resubmitted once per the standing
first-refusal protocol and completed. Refused jobs cost nothing.

---

## C07 — wall-filling curtain, the sack swing

Refs: @Image 1 v33 C05 (framing + wall-filling curtain) · @Image 2 richness guide

### Image prompt

```text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on the snowy front garden of a suburban house.

FRAMING — copy this exactly from REFERENCE IMAGE 1. The camera stands on the shovelled front path at chest height, square-on to the front of a two-storey house and tilted very slightly up. A low white picket fence and the snowy path run across the foreground; the house fills the upper two thirds of the frame; a dark evergreen stands at the right edge.

THE HOUSE — a DIFFERENT house from the reference: PALE SAGE-GREEN painted clapboard with horizontal weatherboards, crisp white trim, a grey shingle roof, white window frames with warm lit windows upstairs, and a small covered front porch with white posts and a DEEP RED front door with a wreath on it. Snow on the ground and along the fence. NOT red brick, NOT stone, NOT stucco, NOT white, NOT blue.

WHERE THE CURTAIN HANGS — CRITICAL. There is ONE single light curtain and it is BIG. It is one clean rectangle, hung flat and perfectly level, and it FILLS THE WHOLE WIDE UPPER WALL of the house front — spanning almost the full width of the sage-green facade, its left and right edges running out close to the corners of the house, leaving only a narrow strip of wall, NOT a wide margin. Its top edge sits just under the eaves. This is a LARGE, dominant, wall-filling display that takes up most of the visible wall — NOT a small panel floating in the middle of the wall with big empty margins around it, NOT two separate patches of light.

HOW DETAILED AND BEAUTIFUL THE PICTURE IS — THE MOST IMPORTANT INSTRUCTION. This is a PREMIUM, EXPENSIVE, PROFESSIONALLY DESIGNED commercial Christmas light display, and the artwork must look it. The bulb grid is FINE and HIGH RESOLUTION — many hundreds of small bulbs across the width — so the characters are richly and skilfully drawn: proper expressive faces with real eyes, eyebrows and open mouths, confident clean outlines, folds and shading in the fabric, fur trim that actually reads as soft fur, highlights and shadow giving the figures roundness and volume, smooth flowing curves in the arms and body. Gorgeous, polished, eye-catching artwork. It is absolutely NOT a crude blocky 8-bit pixel sprite, NOT jagged, NOT clumsy, NOT a chunky Minecraft or cross-stitch chart, NOT low resolution, NOT a child's drawing. The only coarseness in the image comes from the physical gaps between the hanging strands — never from the drawing itself being clumsy or low-detail.

CRITICAL — HOW THE LIGHTS ARE BUILT. This is NOT an LED video wall, NOT a TV screen, NOT a projection, NOT a printed banner. It is a hanging curtain of string lights: many separate thin BLACK wires hung close together side by side from a header cable, each wire carrying a close-spaced run of small round bulbs. The picture is built from VERTICAL DOTTED LINES OF LIGHT — the horizontal gap between neighbouring strands is a little wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular rather than a square matrix. The curtain is SEE-THROUGH — through the gaps you can read the sage-green clapboard wall behind it, and the unlit areas are just dark wall with dull grey unlit bulbs and faint black wires, NOT a solid coloured field. Every lit bulb is a point source with a blown-out white core, a coloured halo and a small soft star flare. The strands sag slightly and the bottom hem is uneven and wavy; the glow bounces off the wall as a soft halo and spills onto the snow in a speckled, uneven pattern.

BUILT TO BE ANIMATED. Exactly TWO large characters and nothing else. NO crowd of little figures, NO confetti field, NO scattered snowflakes filling the background, NO dotted motion arcs, NO flying debris, NO speed lines, NO stars. Each character is one clear shape separated from the other by a wide band of completely dark unlit curtain, so you could trace its outline with a finger. Roughly HALF of the curtain rectangle stays BLACK and empty. Both characters are FULL FIGURES drawn head to foot at the same large size as each other. The joke reads from a held physical force in their bodies, one frame before it gives way.

THE PICTURE IN THE LIGHTS — the sack swing. On the LEFT stands Santa in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, feet planted wide, twisted right round with his huge bulging RED SACK hoisted high over his head in both white-gloved hands like a hammer about to come down, knees bent, teeth gritted and eyes narrowed in effort. On the RIGHT the Grinch, a tall vivid lime-green figure in a red Santa hat and a red coat, is ducking — knees bent deep, head pulled down into his shoulders, both green hands clamped flat over the top of his head, one eye squinting up at the sack, mouth pulled wide in a terrified grimace. Held exactly one frame before the sack swings down.

The entire picture is contained INSIDE the rectangle of the curtain and touches none of its edges — both figures sit wholly within the lit rectangle with a clear margin all the way around, the sack and Santa's head well below the top edge, both sets of feet well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the wall, the roof, the sky or the ground.

ABSOLUTELY NO text, letters, numbers, words or writing anywhere in the lights or anywhere else in the photograph.

COLOUR IS THE POINT. Santa's coat and sack are a deep saturated red with brilliant white fur trim, his boots are black, the Grinch is a vivid lime green. The picture must never collapse into a single warm-white or single-blue wash. Use REFERENCE IMAGE 2 ONLY as a guide to how finely and richly bulb artwork can be drawn — do NOT copy its subject matter and do NOT copy its single-colour warm-white palette.

Fully clothed cartoon figures, a silly slapstick pose and nothing more.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, every bulb crisply resolved, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
```

### Video prompt

Refs on the video job: @Image 1 `v35_c07_g2.png` (redrawn start frame)

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same PALE SAGE-GREEN PAINTED CLAPBOARD house with horizontal weatherboards, a GREY SHINGLE ROOF and WHITE WINDOW FRAMES with warm lit windows upstairs, same low snow-capped white PICKET FENCE across the foreground, same shovelled snowy path running up to the house with snow either side, same covered front porch with square white posts and a DEEP RED FRONT DOOR with a WREATH, same dark snowy evergreen at the right edge, same single large lit LED curtain FILLING THE WHOLE WIDE UPPER WALL of the house front — one clean level rectangle spanning almost the full width of the sage-green clapboard facade, its left and right edges running out close to the corners of the house and its top edge just under the eaves — showing THE SACK SWING: at the LEFT SANTA in a deep saturated red coat with white fur trim, a white beard and a black belt, feet planted wide and twisted right round with his huge bulging RED SACK hoisted high over his head in both white-gloved fists like a hammer about to come down, knees bent, teeth gritted and eyes narrowed in effort; at the RIGHT the green character — a short, chunky, stocky green cartoon goblin with SMOOTH hairless kelly-green skin, a big round ball head with fat cheeks and no muzzle, a small round button nose, big round white eyes with small black pupils, short ROUNDED ears, short stubby arms and short bandy legs, chunky three-fingered mitten hands, a floppy FOREST-GREEN pointed cap with a white pom-pom, a mustard-yellow scarf and brown ankle boots — not tall, not lanky, no fur, no long muzzle, no pointed ears, NEVER named, simply the green character — ducking, knees bent deep, head pulled down into his shoulders, both chunky mitten hands clamped flat over the top of his floppy green cap, one eye squinting up at the sack, mouth pulled wide in a terrified grimace.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the picket fence, the snowbanks and the shrubs at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

MOVEMENT — THE ANIMATION IS THE WHOLE POINT AND IT NEVER RESTS. It is already ON and running at full speed in the very first frame and is STILL running flat out in the last frame. THE FIGURES REDRAW COMPLETELY EVERY QUARTER SECOND — SIXTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each a big obvious physical movement, never a small twitch. NO BEAT IS EVER A BRIGHTNESS CHANGE: every single beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.
0.25s — Santa hoists the red sack even higher up and back behind his head and both his elbows fly wider.
0.50s — the sack comes whipping down low across the picture in one heavy arc and Santa's whole body swings round after it.
0.75s — the green character flattens right down to the ground line with both mitten hands over his cap and the sack sweeps clean over him.
1.00s — Santa hauls the sack back up over his shoulder for a second swing, both black boots skidding a half-step on the ground line.
1.25s — the green character springs back up, plants both brown boots wide and flaps both stubby arms at him, cheeks puffed.
1.50s — the sack comes down a second time and he drops flat again, both bandy legs kicked out behind him.
1.75s — at the bottom of the arc the mouth of the sack flies open and ONE GOLD-WRAPPED PRESENT pops clear of it.
2.00s — Santa stops dead with both white gloves still clamped on the slack sack, his head snapping round after the present, his white beard swinging across his face.
2.25s — the gold present bounces twice along the ground line and rolls to a stop against the green character's brown boot.
2.50s — the green character bends down, picks it up, holds it up and waggles it, both huge white eyes going wide.
2.75s — Santa drops the sack, scrambles onto all fours and lunges for it, both gloves stretched out.
3.00s — his gloves slip out from under him on the packed ground line and he flattens out, arms and legs spread wide.
3.25s — the green character hops backward twice on one foot, still holding the present up out of reach.
3.50s — Santa gets one boot planted, pushes up and stands swaying, both arms out wide for balance.
3.75s — his boot catches the slack red sack and he tips right back over it, the sack upending behind him.
4.00s — everything peaks together: Santa tipped fully back with both boots up and both arms flung wide, the sack upended, the green character bent double howling with the gold present held overhead — every limb staying well inside the lit rectangle.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — Santa's boots, his arms, his hat and beard, his sack, the green character's arms, his legs, his ears, his eyes, his grin, the big red sack, the gold present. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the large sage-green clapboard upper wall of the house front". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. THE BIGGER THE MOTION GETS, THE MORE STRICTLY THIS APPLIES. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No flung arm, no black boot, no green leg, no brown boot, no swinging red sack and no tumbling gold present ever touches or crosses outside the curtain rectangle. At every instant, in every pose, every figure keeps a clear margin of at least two full unlit strands of dark wall inside every edge of the curtain — top, bottom, left and right. If a swing, a windmill, a thrown-up arm or a bouncing present would reach an edge, THE POSE IS DRAWN SMALLER so it stays inside — the rectangle is never made bigger to fit it. Santa falls along the ground line and stays low; nothing is launched upward out of the picture. Nothing spills onto the grey shingle roof, the white window frames, the porch, the deep red front door, the sky or the evergreen. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail and does not gain size.

HARD RULES: no people, no cars, no pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{87c55480-…, start_image}`.

**Job** `f5952bf7-80e4-45ae-9bc3-1e3ee804d229` → `clips/v35_c07_g1.mp4` · completed 2026-09-18.

Reused from v34 C07 — changed: the house nouns and the gag. House: WHITE CLAPBOARD FARMHOUSE →
PALE SAGE-GREEN PAINTED CLAPBOARD house; BLACK STANDING-SEAM METAL ROOF → GREY SHINGLE ROOF;
BLACK WINDOW FRAMES → WHITE WINDOW FRAMES; MATTE BLACK FRONT DOOR with a RED-BOW WREATH → DEEP
RED FRONT DOOR with a WREATH; the SURFACE OVERRIDE quote "the large white clapboard upper wall"
→ "the large sage-green clapboard upper wall". Gag: THE CANDY-CANE SLIP → THE SACK SWING, so the
opening pose and all sixteen beats were rewritten around the red sack — but the beat STRUCTURE is
untouched: still exactly sixteen beats on the same quarter-second grid. The DENSITY prop list and
the containment list swapped the candy cane for the sack, and the outside-surface list took the
new roof, window and door nouns. The walking-POV CAMERA block, HARD NEGATIVE — NO PHONE, the
whole lights-built block, HARD RULES, AUDIO and LOOK are byte-identical.

---

## C08 — garage door, crowd watching, the candy-cane duel

Refs: @Image 1 v33 C06 g2 (composition + curtain placement + pastel wash) · @Image 2 richness guide

### Image prompt

```text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a suburban driveway.

COPY THE COMPOSITION OF REFERENCE IMAGE 1 EXACTLY — THIS IS THE MOST IMPORTANT INSTRUCTION. Reproduce its camera position, its framing, its proportions and above all WHERE THE LIGHT CURTAIN HANGS. Change only the house and the picture shown in the lights.

WHERE THE CURTAIN HANGS — CRITICAL. The light curtain hangs across the DOUBLE GARAGE DOOR and nowhere else. It completely fills the garage door opening: one clean bright rectangle, noticeably wider than it is tall, sitting squarely inside the garage door frame, its top edge tucked right under the garage lintel and its left and right edges running all the way out to the door jambs, its bottom edge reaching down to the driveway behind the heads of the crowd. The garage door opening is entirely covered by the lit curtain, edge to edge, corner to corner. The curtain is NOT on the gable above, NOT on the upper wall, NOT on the roof, NOT floating in the middle of a blank wall — it is ON THE GARAGE DOOR, exactly as in REFERENCE IMAGE 1.

THE HOUSE — same layout as REFERENCE IMAGE 1 but a DIFFERENT house: CREAM STUCCO with dark chocolate-brown TUDOR HALF-TIMBER BEAMS crossing the projecting gable above the garage, a small black pendant lantern hanging in the peak, a warm lit leaded window off to the left, and a bare winter tree at the right edge. Snow on the ground. NOT clapboard, NOT yellow, NOT blue, NOT green.

THE FOREGROUND — exactly as in REFERENCE IMAGE 1. A group of neighbours in winter coats and bobble hats stands in the near foreground with their BACKS to the camera, in dark silhouette, watching the display. Their heads and shoulders fill the bottom third of the frame at a range of heights, adults and children together. The snowy driveway between them and the garage is wet and glossy and throws a long smeared multicoloured reflection of the lit curtain back toward the camera.

CRITICAL — HOW THE LIGHTS ARE BUILT. This is NOT an LED video wall, NOT a TV screen, NOT a projection, NOT a printed banner. It is a hanging curtain of string lights: many separate thin BLACK wires hung close together side by side from a header cable under the lintel, each wire carrying a close-spaced run of small round bulbs. The picture is built from VERTICAL DOTTED LINES OF LIGHT — the horizontal gap between neighbouring strands is a little wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular rather than a square matrix. The individual bulbs are clearly countable across the whole curtain, exactly as in REFERENCE IMAGE 1, and every lit bulb is a point source with a blown-out white core, a coloured halo and a small soft star flare. The strands sag slightly and the bottom hem is uneven and wavy.

HOW DETAILED AND BEAUTIFUL THE PICTURE IS — THE MOST IMPORTANT INSTRUCTION. This is a PREMIUM, EXPENSIVE, PROFESSIONALLY DESIGNED commercial Christmas light display, and the artwork must look it. The bulb grid is FINE and HIGH RESOLUTION — many hundreds of small bulbs across the width — so the characters are richly and skilfully drawn: proper expressive faces with real eyes, eyebrows and open mouths, confident clean outlines, folds and shading in the fabric, fur trim that actually reads as soft fur, highlights and shadow giving the figures roundness and volume, smooth flowing curves in the arms and body. Gorgeous, polished, eye-catching artwork. It is absolutely NOT a crude blocky 8-bit pixel sprite, NOT jagged, NOT clumsy, NOT a chunky Minecraft or cross-stitch chart, NOT low resolution, NOT a child's drawing.

THE BACKGROUND INSIDE THE CURTAIN — exactly like REFERENCE IMAGE 1: a soft, even, gently graded wash of pastel blue, violet and pink light filling the rectangle behind the characters, with the white grid of bulbs reading through it. It is a clean colourful backdrop, NOT a dirty grey haze, NOT a muddy fog, NOT a solid flat block of one colour.

BUILT TO BE ANIMATED — exactly TWO large characters and nothing else. NO crowd of little figures inside the lights, NO third character, NO confetti, NO dotted motion arcs, NO flying debris, NO speed lines, NO stars, NO floating hearts, NO scattered snowflakes. Each character is one clear shape, clearly separated from the other so you could trace its outline with a finger. Both are FULL FIGURES drawn head to foot at the same large size as each other. The joke reads from a held physical force in their bodies, one frame before it gives way.

THE PICTURE IN THE LIGHTS — the candy-cane duel. Santa on the LEFT and the Grinch on the RIGHT face each other across the middle of the rectangle like fencers, each gripping a huge red-and-white striped CANDY CANE two-handed like a sword, the two canes crossed and locked hard against each other in the centre between them, both figures leaning in with their front knee bent deep and their back leg braced straight behind, weight thrown forward, straining. Santa is in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, teeth gritted, one eye squeezed shut with effort. The Grinch is a tall vivid lime-green figure in a red Santa hat and a red coat, leaning in just as hard, mouth wide open in a snarling grin. Held exactly one frame before one of them gives way.

BOTH CHARACTERS SIT WHOLLY INSIDE THE RECTANGLE. Together they fill about two thirds of the height of the curtain rectangle, with a clear margin of background all the way around — heads well below the top edge, boots well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the garage frame, the stucco, the timber beams, the lantern, the sky or the driveway.

ABSOLUTELY NO text, letters, numbers, words or writing anywhere in the lights or anywhere else in the photograph.

COLOUR IS THE POINT. Santa's coat is a deep saturated red with brilliant white fur trim, the Grinch is a vivid lime green, the two candy canes are bright red and white, and the background wash is pastel blue, violet and pink. Use REFERENCE IMAGE 2 ONLY as a guide to how finely and richly bulb artwork can be drawn — do NOT copy its subject matter and do NOT copy its single-colour warm-white palette.

Fully clothed cartoon figures, a silly slapstick pose and nothing more. No nudity, no bare skin beyond the green cartoon arms and face.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, every bulb crisply resolved, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
```

### Video prompt

Refs on the video job: @Image 1 `v35_c08_g2.png` (redrawn start frame)

```text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same CREAM STUCCO house with dark chocolate-brown TUDOR HALF-TIMBER BEAMS crossing the projecting gable over the garage, same small BLACK PENDANT LANTERN hanging in the peak, same warm lit leaded window off to the left, same BARE WINTER TREE at the right edge of frame, same wet glossy driveway throwing the coloured light back in long smeared reflections, same crowd of neighbours in winter coats and bobble hats seen FROM BEHIND in the near foreground, adults and children together, their heads and shoulders filling the bottom third of the frame at a range of heights, same lit LED curtain covering the whole double garage door showing THE CANDY-CANE DUEL: at the LEFT SANTA in a deep saturated red coat with white fur trim, a black belt and big black boots, gripping a huge RED-AND-WHITE STRIPED CANDY CANE two-handed like a sword, front knee bent deep and back leg braced straight behind him, weight thrown forward, teeth gritted and one eye squeezed shut with effort; at the RIGHT the green character — a short, chunky, stocky green cartoon goblin with SMOOTH hairless kelly-green skin, a big round ball head with fat cheeks and no muzzle, a small round button nose, big round white eyes with small black pupils, short ROUNDED ears, short stubby arms and short bandy legs, chunky three-fingered mitten hands, a floppy FOREST-GREEN pointed cap with a white pom-pom, a mustard-yellow scarf and brown ankle boots — not tall, not lanky, no fur, no long muzzle, no pointed ears, NEVER named, simply the green character — gripping his own huge red-and-white striped candy cane two-handed in both mitten hands, leaning in just as hard with his front knee bent deep and his back leg braced straight, mouth wide open in a snarling grin; the two canes crossed and locked hard against each other in the centre between them.

ABSOLUTE FIRST RULE — THE LIT PICTURE IS TRAPPED INSIDE THE CURTAIN RECTANGLE. In the reference image the lit LED curtain is a rectangle hanging across the double garage door only, and it stops short of the door's edges. That rectangle is FIXED for the whole four seconds: it never grows, never widens, never rises, never rescales, never warps, never drifts, and the camera never changes size on it. Santa, the green character and the two crossed candy canes are drawn INSIDE that rectangle with a clear band left all the way round — a generous margin at the top, and margins at the left, right and bottom.
NOTHING LIT EVER CROSSES AN EDGE, AND THE BIGGER THE MOTION GETS THE MORE STRICTLY THIS APPLIES. No arm, no black boot, no brown ankle boot, no red hat, no floppy green cap and neither candy cane ever touches or crosses the edge of the curtain, and nothing lit ever appears on the cream stucco, the dark chocolate Tudor half-timber beams, the projecting gable, the black pendant lantern, the bare winter tree or the sky. At every instant, in every pose, every figure keeps a clear margin of at least two full unlit strands inside every edge of the curtain. If a pose would take a limb or a swinging candy cane out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. The duel stays low and contained: both figures keep their feet on the same ground line, and neither they nor a knocked-away cane is ever launched up toward the top edge. Every surface outside the curtain stays exactly as lit as it is in the reference image for the whole four seconds.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, filmed from behind the group at the bottom of the driveway. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE. The house and the garage door stay exactly the same size in frame from the first frame to the last.

THE CROWD IS CASUAL, RELAXED AND ALREADY HAPPY — AND ALREADY MOVING IN THE VERY FIRST FRAME. This is not an audience waiting for something to happen. Nobody is standing frozen staring at the garage in anticipation, nobody holds still and then reacts, there is no build-up and no big synchronised cheer. They are neighbours hanging about on a driveway on a cold night, chatting to each other, laughing at each other, sipping drinks, glancing over at the lights and then back at their friends. Their attention drifts on and off the garage the whole time. They are ALL seen FROM BEHIND — no face is ever turned toward camera.
AT 0.0s, IN THE VERY FIRST FRAME, EVERY PERSON IS ALREADY MID-MOVEMENT. There is NO still opening frame, NO frozen first beat, NO pause before the motion starts, NO moment where the group holds and waits. Someone is already mid-laugh, someone is already turning, someone is already raising a cup, a child is already bouncing on the spot. The clip starts in the middle of the action and never settles.
CONTINUOUS OVERLAPPING MOTION, EVERY HALF SECOND, NEVER IN UNISON — at any instant several different people are doing several different things, and their little actions start and stop at different times so the group always looks alive:
0.0-0.5s — two adults near the front are mid-conversation, heads turned to each other, one shrugging; a child at the left bounces twice on the spot and tugs at the sleeve of the adult beside them.
0.5-1.0s — a woman in the centre laughs and rocks back on her heels, shoulders shaking; a man at the right shifts his weight to his other foot; someone lifts a takeaway cup and drinks.
1.0-1.5s — someone in the front leans into the person beside them and points lazily at the lights without turning round; a teenager at the left shoves both hands deeper into their pockets, hunches, and blows out a long fog of breath.
1.5-2.0s — a woman at the left leans sideways into the person next to her and says something; they both laugh; another person scratches under their bobble hat and looks away from the garage entirely.
2.0-2.5s — two people knock shoulders and one claps once, casually; a small child is lifted up onto an adult's hip and settles there, bobble hat wobbling.
2.5-3.0s — scattered easy laughter ripples through the group, a few loose claps at different moments, not together; one adult crouches down to a child's height and points up at the lights; another points out at them with a cup still in hand.
3.0-3.5s — the man at the right wipes his eyes laughing and says something sideways; two heads tip together; a bobble hat bobs as someone nods along.
3.5-4.0s — a few people applaud loosely, hats bobbing, breath fogging, someone waves an arm overhead at a neighbour further down the drive, someone else is already turning to talk to the person behind them.
Coats crease, bobble hats bob, breath fogs, boots shift on the wet driveway, shoulders shake with laughter. NOBODY IS EVER STILL and nobody is waiting.

THE ARTWORK IS THE MAIN EVENT AND IT IS FRANTIC. THE VERY FIRST FRAME OF THE CLIP IS ALREADY MID-ACTION — THE LIT PICTURE DOES NOT HOLD, DOES NOT PAUSE, DOES NOT SETTLE AND DOES NOT EASE IN. There is NO still opening frame on the garage door, NO frozen first beat, NO moment at the start where Santa and the green character hold their reference pose while only the crowd moves. THE FIRST POSE CHANGE IN THE ARTWORK LANDS BEFORE 0.15s AND IS AS BIG AS EVERY LATER ONE. The picture redraws COMPLETELY EVERY QUARTER SECOND. SEVENTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each a big obvious physical change, never a small twitch. NO BEAT IS EVER A BRIGHTNESS CHANGE: every single beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.
0.00s — it lands out of the first frame already mid-move: the two crossed candy canes are already grinding hard against each other and snapping back apart, Santa already skidding a half-step to the right with both boots sliding on the ground line while the green character drives forward off his braced back boot.
0.25s — the canes break apart and both figures rock back, each cane swung out wide to its own side.
0.50s — they clash together again in the centre, the two canes cracking against each other, both heads jerking with the impact.
0.75s — the green character swings low at Santa's legs and Santa hops both black boots clear of the ground line.
1.00s — Santa counters with a hard swing at the middle and the green character parries it two-handed above his head, knees dipping.
1.25s — the canes lock again and the two of them push in until their faces almost touch, both leaning at a steep angle.
1.50s — Santa's red hat tips down over one eye and he shoves it back up with one white glove, his cane held off in the other fist.
1.75s — the green character's floppy green cap flops down over his face and he blows it back up out of his eyes, both mitten hands still clamped on his cane.
2.00s — both canes whip round in a fast figure-of-eight between them, elbows flying wide.
2.25s — they double-parry, the two canes crossed overhead, both pairs of boots skidding apart along the ground line.
2.50s — Santa lunges forward off his back boot, cane thrust straight out, his white beard streaming back.
2.75s — the green character twists aside, knees dipping deep, and hooks his own cane round Santa's.
3.00s — he twists Santa's cane clean out of both white gloves and it clatters down onto the ground line between them.
3.25s — Santa rocks right back on his heels, both empty gloves flying up wide, mouth open in a yell.
3.50s — the green character scoops the fallen cane up off the ground line and comes on with one in each mitten hand, waggling both at him.
3.75s — Santa backs off a step with both gloves up in surrender, boots skidding, knees bent.
4.00s — everything peaks together: the green character planted wide with both candy canes brandished overhead and his mouth open in a howl, Santa bent right back on his heels with both gloves flung up and his mouth wide open — every limb still well inside the lit rectangle.
Every pose change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing. The coloured reflections on the wet driveway shift and ripple with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — Santa's arms, his boots, his red hat, his beard, his face, the green character's arms, his legs, his brown ankle boots, his ears, his eyes, his grin, his floppy green cap and the two striped candy canes. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE. This must read as frantic, laugh-out-loud cartoon slapstick with something big happening everywhere you look.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
BACKGROUND OVERRIDE, READ THIS FIRST: in this reference image the curtain carries a SOFT PASTEL BLUE, VIOLET AND PINK BACKGROUND FIELD filling the whole rectangle behind the two figures. That coloured background is part of the start image and it STAYS exactly as it is — it is the one and only exception to the line further down about solid saturated background fields. But it is still built out of individual countable bulbs on see-through vertical strands, never a smooth colour wash, never a flat painted panel and never a screen. Its colours may shift and ripple with the animation, but the field itself never becomes a solid glowing surface, and it never turns into a dirty grey haze or a muddy fog. Everything else in the block below applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its horizontal panel seams, its trim, the faint shadows of the wires falling on it. Away from the coloured field the areas are NOT a solid painted surface — the unlit bulbs show as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the wet driveway in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE GARAGE DOOR IS THE ONLY LIT SURFACE. The artwork is hard-cropped at all four edges of the curtain. It NEVER grows, shrinks, shifts, warps or drifts. Nothing spills onto the cream stucco, the dark chocolate Tudor half-timber beams, the projecting gable, the roof, the black pendant lantern, the bare winter tree or the sky.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame, and nobody leaves. No cars and no pets enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, the odd loose clap, boots on wet tarmac, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
```

**Settings** — `seedance_2_5`, `mode: omni_reference`, `resolution: 720p`, `aspect_ratio: 9:16`, `duration: 4`, `generate_audio: true`, `count: 1`, `use_unlim: false`, `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`. `medias`: `{a8c877e2-…, start_image}`.

**Job** `3394f962-722a-4154-b92a-2aee0de63574` → `clips/v35_c08_g1.mp4` · completed 2026-09-18.

Reused from v34 C08 (the g2 remake with opening motion) — changed: the house nouns, the green
character's description and the gag. House: SLATE-BLUE PAINTED CLAPBOARD with crisp white trim →
CREAM STUCCO with dark chocolate-brown TUDOR HALF-TIMBER BEAMS across the projecting gable; "warm
lit window" → "warm lit leaded window". Character: the tall lime-green on-model description was
replaced with the short stocky goblin paragraph used in C06 and C07, pointed green shoes → brown
ankle boots, and his red Santa hat → floppy green cap throughout the beats. Gag: THE BEARD SWING
→ THE CANDY-CANE DUEL, so the ABSOLUTE FIRST RULE and all seventeen beats were rewritten — but
the beat STRUCTURE is untouched: still exactly seventeen beats on the same quarter-second grid.
The disarm at 3.00s sends the knocked cane DOWN onto the ground line rather than away, to satisfy
the standing containment rule that nothing is ever launched upward. The DENSITY prop list and both
outside-surface lists took the new nouns. The CAMERA block, the ENTIRE CROWD block including all
eight half-second crowd beats, the pastel BACKGROUND OVERRIDE, the rest of the lights-built block,
HARD RULES, AUDIO and LOOK are byte-identical.

---

## C04 g2 / C05 g2 — install pair REMAKE (2026-09-17)

**Why g1 was rejected.** Daniel: *"C4 and C5 - it's a different house and different lights
placement, remake"*. The g1 pair disagreed with each other and with the approved v34 pair:
`v35_c04_g1` put the curtain on the **upper-storey bay only**, while `v35_c05_g1` showed a
different window layout and a two-storey curtain. Reading the accepted `v34_c04_g1` /
`v34_c05_g1` settled the rule:

> **The install-pair curtain is FULL-FACADE.** Pinned under the eaves, one unbroken sheet
> hanging past the upstairs windows, past the band of wall between the floors, past the
> downstairs windows, finishing just above the foundation shrubs. Both storeys' windows glow
> through it. Never a rectangle on one storey with bare wall below.

**How the fix was built.** A dedicated block headed `WHERE THE CURTAIN HANGS — THE MOST
IMPORTANT INSTRUCTION` with the negatives spelled out, plus the approved **v34 C04 attached as a
second reference for curtain placement ONLY**, guarded with "Take NOTHING of the house itself
from REFERENCE IMAGE 2". C05 g2 then chains off C04 g2 and restates the same placement as
"IDENTICAL to REFERENCE IMAGE 2".

**House as rendered (canonical for this pair):** honey-toned cedar shingle two-storey, crisp
white trim, **dark green shutters**, covered porch at the RIGHT with slim white posts and green
garland, dark green front door with a red-bow wreath, warm brass lantern, snow-laden rounded
boxwood balls along the foundation, small snowy fir by the porch steps.

### C04 g2 — references

| Order | id | Used for |
|---|---|---|
| REFERENCE IMAGE 1 | `8f80a2c0-3b8f-4490-a42d-ad17a9c43817` (ladder wide, v6 C4) | framing / composition |
| REFERENCE IMAGE 2 | `ed1f7ffa-7285-4ced-ab37-92797ded7ff5` (v34 C04) | **curtain placement only** |

### C04 g2 — image prompt

```text
Use REFERENCE IMAGE 1 as the EXACT framing and composition reference — match its camera position, camera height, distance, angle, focal length and the placement of every element in the frame. Change ONLY the house and its surroundings.

A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

FRAMING — copied from REFERENCE IMAGE 1. The camera stands out on the snowy front lawn, level, far enough back that the whole front of a two-storey house fills the frame with sky above it. An aluminium extension ladder leans against the house at the upper left, and a man in a dark winter jacket, tan work trousers and boots stands high on it with one arm reaching up to the roofline, fixing the top of the light curtain under the eaves. He is seen from behind and slightly below; no face detail.

WHERE THE CURTAIN HANGS — THE MOST IMPORTANT INSTRUCTION. Copy the curtain placement EXACTLY from REFERENCE IMAGE 2. The curtain is ENORMOUS and covers the ENTIRE FRONT FACADE OF THE HOUSE, BOTH STOREYS AT ONCE. Its top edge is pinned under the eaves at the roofline where the man is working, and it hangs in one continuous unbroken sheet ALL THE WAY DOWN past the upstairs windows, past the band of wall between the floors, past the downstairs windows, and finishes just above the snow-laden shrubs at the foundation. It spans the full width of the main facade from the left corner of the house across to the porch. The upstairs AND the downstairs windows are BOTH behind the curtain and glow warmly through it. This is a full-house, floor-to-roof display. It is NOT a small rectangle on the upper storey only, NOT a single bay, NOT one panel floating high on the wall with bare wall below it, and it does NOT stop partway down.

THE HOUSE — a DIFFERENT house from both references. A two-storey HONEY-TONED CEDAR SHINGLE house — warm golden-brown weathered wood shingles laid in neat overlapping rows across the whole facade, crisp white window trim, dark green shutters flanking the windows, a covered front porch at the RIGHT with slim white posts and a DARK GREEN front door with a red-bow wreath, a warm brass lantern beside the door, thick green garland spiralled up each porch post. Warm lit windows behind the curtain on both floors. Snow-laden rounded boxwood shrubs along the foundation and a small snowy fir at the right. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey. Take NOTHING of the house itself from REFERENCE IMAGE 2 — use that image ONLY to see where the light curtain hangs.

HOW THE CURTAIN IS BUILT — a huge dense curtain of warm white string lights, built from many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles and the white window mullions read clearly through the gaps between strands, and the lit windows behind glow through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. The bottom hem is uneven and wavy where the strands end at slightly different heights. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
```

### C05 g2 — references

| Order | id | Used for |
|---|---|---|
| REFERENCE IMAGE 1 | `75cc4e34-3210-4f0f-9579-ad5a627135c6` (ladder close, v6 C5) | framing / composition |
| REFERENCE IMAGE 2 | `01242684-615e-4bfe-be76-aaf56437f91e` (v35 C04 g2) | house + curtain, must match exactly |

### C05 g2 — image prompt

```text
A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

CAMERA AND FRAMING — copy this EXACTLY from REFERENCE IMAGE 1. This is the SAME house and the SAME moment as REFERENCE IMAGE 2, just seen from much closer and lower: the camera has moved in toward the house and around to the LEFT, standing low on the snow and looking up and along the front facade at an angle, so the wall runs away from the camera in perspective rather than sitting square-on. The aluminium extension ladder dominates the LEFT side of the frame, running steeply up out of the top-left corner, and the man in the dark winter jacket, tan work trousers and boots is higher on it now, up near the roofline with one arm reaching to the eaves, seen from behind and below with no face detail. Snow-laden rounded boxwood shrubs fill the bottom foreground of the frame.

THE HOUSE — IDENTICAL to REFERENCE IMAGE 2 in every detail, just closer. The SAME two-storey HONEY-TONED CEDAR SHINGLE house: warm golden-brown weathered wood shingles laid in neat overlapping rows across the whole facade, crisp white window trim, DARK GREEN SHUTTERS flanking every window, tall white-framed multi-pane sash windows, the covered front porch at the RIGHT with slim white posts and thick green garland spiralled up them, the DARK GREEN front door with its red-bow wreath, the warm brass lantern beside the door, a small snowy fir beside the porch steps and a row of snow-laden rounded boxwood balls along the foundation. Same shingle colour, same white trim, same green shutters, same porch, same green door. Do NOT invent a different house, a different colour or a different style. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey.

WHERE THE CURTAIN HANGS — IDENTICAL to REFERENCE IMAGE 2. The curtain is ENORMOUS and covers the ENTIRE FRONT FACADE, BOTH STOREYS AT ONCE, in one continuous unbroken sheet: its top edge pinned under the eaves at the roofline where the man is working, hanging all the way down past the upstairs windows, past the band of wall between the floors, past the downstairs windows, finishing just above the snow-laden boxwood shrubs at the foundation. The upstairs AND downstairs windows are BOTH behind the curtain and glow warmly through it. It does NOT stop partway down, it is NOT a rectangle on the upper storey only, and it is NOT two separate panels.

HOW THE CURTAIN IS BUILT — the SAME dense curtain of warm white string lights as in REFERENCE IMAGE 2, now seen much closer and at an angle so the individual strands and bulbs are clearly resolved. Many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles, the green shutters and the white window mullions read clearly through the gaps between strands, and the lit rooms behind glow through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. The bottom hem is uneven and wavy. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
```

---

## Board metadata (archived from board.meta.json, 2026-09-18)

**Final cut order** - the order the shots appear in the edit,
which is not always the order the cards sit in on the board.

```
C02 → C03 → C04 → C05 → C06 → C07 → C08
```

**Stats trimmed off the lane panel**

| field | value |
|---|---|
| Stage | Start frames |
| Frames | gpt_image_2 · 2k · medium |
| Takes | 2 rounds · g1 – g2 on the install pair |

---

# C01 — HOOK FRAME — 2026-09-18

## C01 — the neighbours gathered, lights still off (hook)

**Frame** `starting_frames/v35_c01_g1.png`
**Job id** `4158136d-43a7-45d1-9ee4-288669e8c9d2`
**Settings** gpt_image_2 · 2k · quality medium · 9:16 · count 1 · workspace Oneofone1
**Result** 1520×2688 PNG · md5 `fee6a71307bd3ab25cbc56f63c1485d7`

**Brief from Daniel** — no reference image, only a description: "Almost night outside,
neighbors gathered in front of a house that is filled with our lights, shot made from the
neighbors crowd, the neighbors are facing the house, a family in front of the house (it's
their house) facing the neighbors. The lights are off." Clarified: a new house invented for
the hook, and a big crowd — 15+ neighbours, family of four.

**References attached**

| # | media id | what it is | what it is for |
|---|---|---|---|
| 1 | `08a6fdc9-6e1f-475c-a1ad-4a5740d54085` | v33 C06 g2 — crowd-foreground composition | the shot-from-inside-the-crowd viewpoint only |
| 2 | `c0339254-04bb-49ff-8d17-f49b42daec08` | v35 C06 g1 — the dense unlit black veil | the curtain density and strand uniformity |

Reference 1 is a **lit** garage shot, so the prompt carries an explicit guard —
"DO NOT COPY FROM REFERENCE IMAGE 1: its house, its garage door, its lit picture, its
colours or its glow" — because this frame must be completely unlit.

### Image prompt — g1 (verbatim)

```
A real iPhone photo, vertical 9:16, shot outdoors on a suburban front lawn at DUSK, almost night.

CAMERA AND FRAMING - copy the CROWD COMPOSITION of REFERENCE IMAGE 1 exactly, and nothing else from it. The camera is standing INSIDE the crowd, at the eye level of someone in the middle of it, holding the phone up over the shoulders of the people in front. Backs of heads, hats and shoulders fill the bottom third of the frame in near-silhouette at a range of heights; beyond them the ground opens out and the front of the house fills the middle and upper part of the frame. Same low-in-the-crowd viewpoint, same depth, same proportion of foreground crowd to house.

DO NOT COPY FROM REFERENCE IMAGE 1: its house, its garage door, its lit picture, its colours or its glow. There is NO lit artwork and NO glowing curtain anywhere in this photograph.

THE CROWD - a BIG gathering, more than fifteen neighbours packed into the near foreground with their BACKS TO THE CAMERA, facing the house, in dark winter coats, parkas, bobble hats and scarves, several deep, adults and teenagers and small children on shoulders, heads at many different heights, a few phones held up filming, one person with a dog on a lead at the left edge. They read as dark silhouetted shapes against the pale house, breath steaming in the cold. Nobody in the crowd is turned toward the camera.

THE FAMILY - standing out on the snowy front lawn directly in front of their own house, facing the crowd and therefore FACING THE CAMERA, a family of four seen full-length at a distance: a father in a dark green parka with one arm raised in a half-wave, a mother in a long camel wool coat and a cream beanie, a boy of about ten in a red puffer jacket, and a girl of about six in a pink snowsuit holding her mother's hand. They stand in a loose line a few steps out from the porch, small in the frame, clearly separate from the crowd, plainly the hosts about to show something off. Their faces are lit softly by the porch light and read as pleased and a little nervous.

THE HOUSE - a DIFFERENT house from any reference: a two-storey WARM CREAM PAINTED CLAPBOARD house with a wide front gable, crisp white trim, a covered front porch with two square white posts, a deep red front door with an evergreen wreath on it, and a black lantern sconce glowing warm beside the door. A bare winter maple stands at the right edge, a low picket fence runs off to the left, and there is snow on the roof, on the porch rail and across the whole lawn.

THE CURTAIN - the entire front of the house is covered by the light curtain and IT IS COMPLETELY UNLIT. Exactly as dense as in REFERENCE IMAGE 2: many, many thin BLACK vertical wires hung very close together side by side from header cables pinned along the eaves and along the porch roof, only a narrow gap between neighbouring strands, hanging straight down and covering the whole cream gable wall above the porch and the wall on either side of the porch, edge to edge, top to bottom. Each wire carries small round bulbs spaced along it and every single bulb is DARK, DULL GREY and UNLIT. The curtain reads as a fine dense dark veil laid over the pale cream house - the black strands stand out plainly against the pale clapboard, and you can still clearly see the clapboard boards, the white trim and the gable shape straight through the gaps. The veil covers the whole facade: there is no bare patch of wall anywhere and it does not stop partway down. The bottom hem is uneven and wavy where the strands end at slightly different heights, and the strands sag a little in the cold air.

THE WIRE IS BLACK: NOT white, NOT clear, NOT silver, NOT copper. EVERY STRAND IS IDENTICAL - CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the sheet to the other, top to bottom. There must be NO section anywhere where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice - only plain vertical strands hanging straight down. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a projection - it is separate hanging strings with visible gaps between them.

THE LIGHT - almost night. The sky is deep blue dusk with a last band of cold pale orange low on the horizon behind the roofline, the first stars just showing at the top. The only lights burning are the warm porch lantern by the red door and a cold street lamp off to the left throwing a pool across the snow. The snow is blue-white in the shadows and warm where the porch light reaches it. The house and the dark veil over it are clearly legible but everything is unmistakably dusk, not daylight and not black night.

THE CLEAN BAND AT THE TOP - the TOP EIGHTH OF THE FRAME, full width, is nothing but empty deep-blue dusk sky. No roof, no gable peak, no branch, no wire, no raised phone. Everything else sits below it.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural dusk colour, fine natural sensor grain, every strand and every dark bulb crisply resolved. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no bokeh, no colour grading, no fisheye or barrel distortion, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers, words, logos or writing anywhere in the photograph.
```

### Notes

- The curtain density paragraph and the every-strand-identical paragraph are lifted
  near-verbatim from the v35 C06 section above, because those are the two paragraphs that
  made the unlit veil read correctly there.
- The facade is pale cream on purpose. The black veil only reads against a pale wall — the
  same fix that made v35 C06 work with a white carriage door.
- Hook headroom: top eighth is empty dusk sky, kept clear for the CapCut caption.

### C01 g2 — 2026-09-18 — concept approved, house rejected

**Frame** `starting_frames/v35_c01_g2.png` · job `69585bbd-02a1-450b-b4da-d302a721d059`
**Settings** gpt_image_2 · 2k · quality medium · 9:16 · count 1
**md5** `ddfb64a4558c47fa0fba8debfd9c1ea2`

**Why g1 failed** — Daniel: "I like the concept, I want a much bigger house, and this house
has no windows so it's looking completely fake." The crowd, the family, the dusk and the
unlit veil all worked. The house came out as a small single-storey cottage with a blank
windowless facade.

**What changed** — two things only: the house is now a large two-storey home that fills the
frame edge to edge and towers over the family, and it has six named windows with white
frames, glazing bars, sills and real glass, three of them lit warm from inside, with the
curtain strands passing in front of the glass.

**References** — ref 1 is the g1 job itself (`4158136d-43a7-45d1-9ee4-288669e8c9d2`) so the
crowd composition, the family and the dusk light carry over; ref 2 is v35 C06 g1
(`c0339254-04bb-49ff-8d17-f49b42daec08`) for veil density and strand uniformity.

### Image prompt — g2 (verbatim)

```
A real iPhone photo, vertical 9:16, shot outdoors on a suburban front lawn at DUSK, almost night.

REFERENCE IMAGE 1 IS THE PHOTO TO CHANGE. Keep everything about it: the same camera standing INSIDE the crowd at the eye level of someone in the middle of it, the same big gathering of more than fifteen neighbours packed into the near foreground in near-silhouette with their BACKS TO THE CAMERA facing the house, the same family of four out on the snowy lawn facing the crowd and therefore facing the camera (father in a dark green parka with one arm raised in a half-wave, mother in a long camel wool coat and cream beanie, a boy of about ten in a red puffer jacket, a girl of about six in a pink snowsuit), the same deep blue dusk sky with a last cold band of orange low on the horizon, the same snow, the same warm porch lantern and cold street lamp as the only two lights burning, and the same completely UNLIT dark curtain hanging over the whole front of the house.

CHANGE TWO THINGS: MAKE THE HOUSE MUCH BIGGER, AND GIVE IT REAL WINDOWS.

THE HOUSE IS MUCH BIGGER. It is a LARGE two-storey family home, far taller and far wider than in REFERENCE IMAGE 1 - the kind of house with a proper upstairs. It fills the frame from the left edge to the right edge behind the crowd and its roofline rises high into the upper part of the picture. It TOWERS over the family standing on the lawn: a standing adult only reaches the top of the ground-floor windows, and there is a whole second storey of wall and then the gable above that. Warm cream painted clapboard, a wide front gable, crisp white trim, a covered front porch running along the front of it on square white posts, a deep red front door with an evergreen wreath, a black lantern sconce glowing warm beside the door, snow on the roof and along the porch rail.

THE WINDOWS - CRITICAL. THE LAST ATTEMPT HAD NO WINDOWS AT ALL AND THE HOUSE LOOKED COMPLETELY FAKE BECAUSE OF IT. This house has plenty of real windows and every one of them is clearly visible:
- TWO tall upstairs windows side by side in the gable wall above the porch roof.
- A smaller window up in the peak of the gable above those.
- TWO large ground-floor windows, one on each side of the front door, behind the porch.
- One more window on the side wall where it turns away from us.
Every window is a real window: white painted frame, a proper wooden sill, white glazing bars dividing the glass into panes, and real glass that catches a cold reflection of the dusk sky. THREE of them glow softly warm from inside - a table lamp behind one, a small lit Christmas tree visible through another - and the rest are dark. The hanging strands of the curtain pass IN FRONT of the glass, so you can see the white frames, the glazing bars and the lit rooms straight through the gaps between the strands.

THE CURTAIN - the entire front of the house is covered by the light curtain and IT IS COMPLETELY UNLIT. Exactly as dense as in REFERENCE IMAGE 2: many, many thin BLACK vertical wires hung very close together side by side from header cables pinned along the eaves and along the porch roof, only a narrow gap between neighbouring strands, hanging straight down and covering the whole cream gable wall, the whole upper storey and the wall on either side of the porch, edge to edge, top to bottom, with no bare patch anywhere. Each wire carries small round bulbs spaced along it and every single bulb is DARK, DULL GREY and UNLIT. It reads as a fine dense dark veil laid over the pale cream house - the black strands stand out plainly against the pale clapboard, and the clapboard boards, the white trim, the window frames and the gable shape all read clearly straight through the gaps. The bottom hem is uneven and wavy where the strands end at slightly different heights.

THE WIRE IS BLACK: NOT white, NOT clear, NOT silver, NOT copper. EVERY STRAND IS IDENTICAL - CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the sheet to the other, top to bottom. There must be NO section anywhere where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice - only plain vertical strands hanging straight down. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a projection - it is separate hanging strings with visible gaps between them.

There is NO lit artwork and NO glowing curtain anywhere in this photograph. The only light sources are the porch lantern, the street lamp and the three warm windows.

THE CLEAN BAND AT THE TOP - the TOP EIGHTH OF THE FRAME, full width, is nothing but empty deep-blue dusk sky. No roof, no gable peak, no branch, no wire, no raised phone. Everything else sits below it.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural dusk colour, fine natural sensor grain, every strand, every dark bulb and every window frame crisply resolved. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no bokeh, no colour grading, no fisheye or barrel distortion, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers, words, logos or writing anywhere in the photograph.
```

**Lesson — a house with no windows reads instantly as fake.** Describing a facade by its
material and its trim is not enough; the windows have to be enumerated by position and
described as objects (frame, sill, glazing bars, glass, what is lit behind them), or the
model leaves the wall blank. Worth carrying into every exterior prompt on this drive.

### C01 g3 — 2026-09-18 — Daniel rejected g2: shot from too far away

**Frame** `starting_frames/v35_c01_g3.png` · job `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`
**Settings** gpt_image_2 · 2k · quality medium · 9:16 · count 1
**md5** `fa3ccb988b2f3b92484ae60eeeac263a`

**Why g2 failed** — Daniel: "the shot is from too far away, the crowd must be closer to the
house." Making the house bigger in g2 pushed the camera back to fit it in, which opened a wide
empty stretch of snowy lawn between the back of the crowd and the family on the porch. The
house and the windows were fine.

**What changed** — one thing: distance. The camera walks forward into the crowd, the front row
of neighbours now stands almost at the bottom of the porch steps an arm's length from the
family, the empty lawn gap is explicitly banned, the nearest heads and shoulders are big and
close in the bottom third, and the house is stated to LOOM rather than shrink — being nearer
makes it bigger, not smaller. Everything else carries over from g2 by reference.

**References**

| slot | media | purpose |
|---|---|---|
| 1 | `69585bbd-02a1-450b-b4da-d302a721d059` | v35 C01 g2 — house, windows, family, crowd, dusk |
| 2 | `c0339254-04bb-49ff-8d17-f49b42daec08` | v35 C06 g1 — unlit veil density, strand uniformity |

### Image prompt — g3 (verbatim)

```
A real iPhone photo, vertical 9:16, shot outdoors on a suburban front lawn at DUSK, almost night.

REFERENCE IMAGE 1 IS THE PHOTO TO CHANGE. Keep everything about it: the same large two-storey cream clapboard house with its wide front gable, white trim, covered porch on square white posts, deep red front door with an evergreen wreath and warm black lantern sconce; the same six real white-framed windows with sills and glazing bars, three of them glowing warm from inside; the same family of four out in front of the porch facing the camera (father in a dark green parka with one arm raised in a half-wave, mother in a long camel wool coat and cream beanie, a boy of about ten in a red puffer jacket, a girl of about six in a pink snowsuit); the same big crowd of more than fifteen neighbours in the near foreground in near-silhouette with their BACKS TO THE CAMERA facing the house; the same deep blue dusk sky with a last cold band of orange low on the horizon; the same snow; the same completely UNLIT dark curtain over the whole front of the house.

CHANGE ONE THING: MOVE EVERYTHING MUCH CLOSER. THE LAST ATTEMPT WAS SHOT FROM FAR TOO FAR AWAY.

CLOSE IN. The camera has walked forward into the middle of the crowd and is now only a few metres from the family:
- The FRONT ROW OF THE CROWD IS RIGHT UP AT THE HOUSE. The nearest neighbours' backs are standing almost at the bottom of the porch steps, an arm's length or two from the family - NOT across the lawn from them. THERE IS NO WIDE EMPTY STRETCH OF SNOWY LAWN between the crowd and the family. The gap is small and the two groups nearly touch.
- The dark heads and shoulders of the nearest neighbours are BIG and CLOSE, filling the bottom third of the frame, cut off by the bottom edge and the side edges, heavily out of the way of the subject but unmistakably near the lens.
- The FAMILY IS LARGE IN FRAME. Read their faces, their coats, the father's raised hand. They stand well above the crowd's heads.
- The HOUSE LOOMS. It is close enough that it fills the frame from the left edge to the right edge and rises high, the porch roof and the whole upper storey and the gable stacked up above the family. Being nearer makes it bigger, not smaller.

THE CURTAIN - the entire front of the house is covered by the light curtain and IT IS COMPLETELY UNLIT. Exactly as dense as in REFERENCE IMAGE 2: many, many thin BLACK vertical wires hung very close together side by side from header cables pinned along the eaves and along the porch roof, only a narrow gap between neighbouring strands, hanging straight down and covering the whole cream gable wall, the whole upper storey and the wall on either side of the porch, edge to edge, top to bottom, with no bare patch anywhere. Each wire carries small round bulbs spaced along it and every single bulb is DARK, DULL GREY and UNLIT. It reads as a fine dense dark veil laid over the pale cream house - the black strands stand out plainly against the pale clapboard, and the clapboard boards, the white trim, the window frames, the glazing bars and the lit rooms all read clearly straight through the gaps between the strands.

THE WIRE IS BLACK: NOT white, NOT clear, NOT silver, NOT copper. EVERY STRAND IS IDENTICAL - CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the sheet to the other, top to bottom. There must be NO section anywhere where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice - only plain vertical strands hanging straight down. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a projection - it is separate hanging strings with visible gaps between them.

There is NO lit artwork and NO glowing curtain anywhere in this photograph. The only light sources are the porch lantern, a cold street lamp at the edge and the three warm windows.

THE CLEAN BAND AT THE TOP - the TOP EIGHTH OF THE FRAME, full width, is nothing but empty deep-blue dusk sky. No roof, no gable peak, no branch, no wire, no raised phone. Everything else sits below it.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural dusk colour, fine natural sensor grain, every strand, every dark bulb and every window frame crisply resolved. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no bokeh, no colour grading, no fisheye or barrel distortion, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers, words, logos or writing anywhere in the photograph.
```

**DEFECT IN THE OUTPUT — the veil did not render.** The distance fix worked, but the gable
and the upper storey came back as bare cream clapboard: no black strands anywhere on the
house. The unlit-curtain block is unchanged from g2, where it did render, so the likely cause
is that the "MOVE EVERYTHING MUCH CLOSER" instruction sat above it and took all the model's
attention. If g4 is wanted, the curtain block should be hoisted to the TOP of the prompt as
its own paragraph and the closer-in instruction dropped below it.

**Lesson — a one-word distance change still costs you the rest of the prompt.** Putting a
loud all-caps CHANGE ONE THING block first pushes everything under it down the priority order,
including blocks that rendered correctly on the previous take. Loud edit instructions belong
below the non-negotiables, not above them.

### C01 r1 — 2026-09-18 — lit companion reference, family turned to face the house

Reference image, not a starting frame. Daniel: *"For V35 we need to make another image that we will
add as refence, the family is now turned, facing the house. Now the house is fully lit up with a very
cool christmas animation (only where the lights are placed)"*

Chained off `v35_c01_g3` (job `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`) attached as reference image 1, so
the camera, distance, crop, house, porch, crowd and dusk light are carried by the picture rather than by
prose. Short-prompt pattern: only the two changes he named are written out.

**Prompt**

```
Recreate REFERENCE IMAGE 1 as a real iPhone photograph. Keep it exactly as it is - the same camera position, the same camera height, the same distance, the same crop, the same house, the same porch, the same crowd of neighbours in the foreground with their backs to camera, the same dusk light. Change only these two things:

1. The family of four on the porch has turned around. They now face the house, with their backs to the camera, exactly like the crowd in the foreground. Same people, same clothes, same positions on the porch - only turned around.

2. The house is now fully lit. A hanging LED curtain of vertical light strands covers the front face of the house, and it is switched on and running a vivid Christmas animation - bright warm white and cool white lights chasing and twinkling in waves down the strands, a few strands lit ahead of the others so the pattern reads as moving. The light pattern exists ONLY on the strands of the curtain where the lights are hung. The rest of the house - the roof, the sides, the porch trim, the windows - has no light pattern on it and stays dark.

Nothing else changes.

A real photograph shot on a modern iPhone, tack sharp, correct exposure, clean natural dusk light. Not blurry, not soft, no motion blur, no bokeh, no CGI or 3D-render look. No text, letters, numbers, logos, captions, watermarks, buttons, icons or interface overlays anywhere in the photograph.
```

**References**

| # | media | what it carries |
|---|---|---|
| 1 | job `29f6e4cb-8a99-4cd2-bf42-d63ef0931741` (`v35_c01_g3.png`) | camera, distance, crop, house, porch, crowd, dusk |

**Settings** — `gpt_image_2`, 2k, quality `medium`, 9:16, count 1, `use_unlim` false. Workspace Oneofone1.

**Job** `bf5da344-7730-412a-a2c5-acbbd2400d9d`
**File** `references/v35_c01_r1.png` — 1520×2688, md5 `e02b8db97c3035cb4e4e83c5f010d47a`

**Result** — family of four turned, backs to camera on the porch, matching the crowd. Curtain strands now
render across the whole front facade and are lit, with the glow held to the strands; roof, sides and the
ground around the porch stay dark. Note: g3 never rendered the unlit black veil at all, so on this take the
curtain arrives already lit — the lit and unlit versions of this shot therefore do not share a veil layout
byte for byte.


### C01 r2 — 2026-09-18 — pixel-artwork lit facade, supersedes r1

Daniel on r1: *"It looks good, but I don't want this style of animation on the house. maybe something in
the style of the images attached. Idk, think at a composition that will look good on the entire house"* —
with three photos of real LED-curtain houses displaying a pictorial image built out of the bulbs (Santa in
a sleigh, a Santa filling a gable end, a Santa going down a chimney flanked by two trees).

So the light is no longer a twinkle pattern: the curtain is a low-res display and the bulbs are pixels.
Composition chosen for this house because the facade is tall, narrow and punched with windows and a porch:
a waist-up Santa waving across the upper wall, deep blue sky and big snowflakes filling the gaps, and a
Christmas tree in each bottom corner so the bottom of the wall is not empty on either side of the porch.
The third attached photo was uploaded as the style reference — it is the one whose artwork is designed
around a two-storey facade with windows in it.

Chained off r1 (job `bf5da344-7730-412a-a2c5-acbbd2400d9d`), so camera, distance, house, turned family and
crowd all carry from the picture. Only the wall artwork is described.

**Prompt**

```
Recreate REFERENCE IMAGE 1 as a real iPhone photograph. Keep it exactly as it is - the same camera position, the same camera height, the same distance, the same crop, the same house, the same porch, the same family with their backs to camera, the same crowd of neighbours in the foreground, the same dusk light. Change only one thing:

The lights on the house are no longer a plain twinkling pattern. The LED curtain now displays a big picture, made of the individual bulbs acting as pixels, in exactly the style of REFERENCE IMAGE 2 - dense rows of glowing bulbs forming a bold, simple cartoon image with flat saturated colour and clean shapes, bright enough to read from across the street.

The picture on the wall is: a jolly cartoon Santa Claus in a red suit and white beard, seen from the waist up, filling the upper part of the wall with his raised hand waving, on a deep blue night background scattered with big white snowflakes, and one green Christmas tree with coloured baubles in the bottom left corner of the wall and another in the bottom right corner. The picture is built into the curtain of lights and covers the front wall of the house only. The windows and the front door stay where they are and read through the lights. The roof, the sides of the house and the ground stay dark.

Nothing else changes.

A real photograph shot on a modern iPhone, tack sharp, correct exposure, clean natural dusk light. Not blurry, not soft, no motion blur, no bokeh, no CGI or 3D-render look. No text, letters, numbers, logos, captions, watermarks, buttons, icons or interface overlays anywhere in the photograph.
```

**References**

| # | media | what it carries |
|---|---|---|
| 1 | job `bf5da344-7730-412a-a2c5-acbbd2400d9d` (`v35_c01_r1.png`) | camera, distance, house, turned family, crowd, dusk |
| 2 | media `ca55e296-fb0e-4c9d-ba1d-8e94307438c0` (Daniel's 3rd attachment) | the pixel-artwork look — bulbs as pixels, flat saturated cartoon |

**Settings** — `gpt_image_2`, 2k, quality `medium`, 9:16, count 1, `use_unlim` false. Workspace Oneofone1.

**Job** `dc410a06-b67d-4b52-943a-a3df3b7b8b7c`
**File** `references/v35_c01_r2.png` — 1520×2688, md5 `41a11f1388b58cb82dd4478fc76a7c29`

**Result** — reads as a real pixel display: Santa waving across the upper wall, snowflakes filling the sky
around him, a lit tree in each bottom corner, windows and the porch punching through the artwork. Roof and
sides dark, warm porch light still on, crowd and turned family unchanged from r1.

**Lesson.** "Animated Christmas pattern" as prose gets you chasing twinkle, which is what the light does,
not what it shows. This product's whole selling point is that the curtain is a low-res screen, so the
prompt has to say *the bulbs are pixels and they draw a picture* and attach a real photo of one doing it.
Describing the artwork alone would not have carried the bulb grid.


### C01 g1 (clip) — 2026-09-18 — the crowd 3-2-1 and the house lighting up

**Clip** `clips/v35_c01_g1.mp4` · job `2e2dd906-0b1b-4bf4-bdd3-9f6d98ccd4c3`
**Start image** `v35_c01_g3.png` (job `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`) — family facing camera, wall dark
**Extra refs** `dc410a06-b67d-4b52-943a-a3df3b7b8b7c` — `v35_c01_r2.png`, the lit pixel artwork
**Settings** seedance 2.5 · omni_reference · 720p · 9:16 · 5s · generate_audio true · count 1 · declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`
**md5** `21b9da36266cfc45e26c07345fd624df`

**Brief (Daniel, verbatim)** — "Suspense clip. the crowd and the family in front of the house
are all saying '3,2,1' and exactly after they say one the house lights up with the animation.
The animation it's not static: santa it's waving, the snow flakes are falling and the
christmas trees are moving. The family ion front of the house turn around to face the house
right before everyone says '1', everyone it's enthusiastic and happy. Don't forget to add the
reference with the animation. 5s clip … must be super natural and engaging"

**This is what `r1` and `r2` were built for.** The whole two-frame pair exists so that this
clip has a dark state and a lit state that are the same photograph. `g3` is the dark state and
the start image; `r2` is the lit state and goes in as the reference. Without `r2` attached the
model invents its own light show.

**How the artwork is written, per `feedback_projection_motion`** — it is a NAMED SUBJECT with
its own motion paths, not a line in a lighting block. Each of the three motions gets exactly
one sentence, said once: Santa's arm waves (and only his arm), the snowflakes drift downward
with a fade-out at the bottom row and a fade-in at the top so the count holds, the trees sway
from their bases with the baubles blinking. The field is explicitly ANCHORED — it does not
rotate, spin, sweep, slide or scroll — because a rotating sheet is the failure mode he
rejected outright on the projector product. Left and right of the wall are locked to the same
instant and the same speed. Motion is told where it ENDS: still lit, still running, crowd
still cheering on the last frame. `(no BGM)` and `No subtitles` are the literal sanctioned
tokens.

**Timing** — 0.8 / 0.7 / 0.7 for the three counts puts "ONE" at 2.2s and the switch-on at
2.5s, leaving 2.5s of the animation actually running. On a 5s clip the reveal has to land
early or the product is on screen for half a second.

### Video prompt — v35 C01 g1 (verbatim)

```text
Animate REFERENCE IMAGE 1 exactly as it is. The first frame of the video IS REFERENCE IMAGE 1, unchanged - same pale gable-front two-storey house, same covered porch with its white posts, same warm porch lantern and warm lit windows, same deep blue dusk sky, same family of four standing together on the porch facing the camera, same crowd of neighbours in winter coats and knitted hats packed across the foreground with their backs to the camera, same snow, same dark unlit front wall.

EVERYONE COUNTS DOWN TOGETHER, OUT LOUD. The crowd in the foreground and the family on the porch chant in unison in real voices: "Three... two... ONE!" Grinning, excited, breath fogging in the cold.

ACTION TIMELINE (5 seconds, one continuous take, no cuts):
0.0-0.8s - "Three!" The crowd chants, shoulders bouncing, a couple of arms and a raised phone going up. The family on the porch chant with them, still facing the camera.
0.8-1.5s - "Two!" Louder. A fist punches up in the crowd. The family on the porch begin to swing round.
1.5-2.2s - The family of four finish turning all the way around to face the house, backs to the camera, shoulder to shoulder exactly like the crowd, and on the last of that turn everybody shouts "ONE!"
2.2-2.5s - The whole front wall of the house switches on at once.
2.5-5.0s - The picture on the wall runs. The crowd erupts - arms up, hands clapping, heads tipping back, two of the children on the porch bouncing on the spot. THE MOTION ENDS HERE, with the picture still lit and still running and the crowd still cheering on the last frame.

THE PICTURE ON THE HOUSE IS THE MAIN SUBJECT FROM 2.2s ONWARD. The front wall of the house is a giant low-resolution screen made of hanging LED curtain strands, showing exactly the picture in REFERENCE IMAGE 2 - a cartoon Santa in a red suit with a white beard filling the upper wall on a deep blue field, big white snowflakes scattered around him, one green Christmas tree with coloured baubles in the bottom-left corner of the wall and another in the bottom-right corner, all built out of individual glowing bulbs acting as pixels. It is not a still picture. Three things move in it, continuously, from 2.2s to the very last frame:
- Santa's raised hand WAVES side to side, a steady friendly wave, about one wave per second. Only his arm moves; his body, face and beard stay exactly where they are.
- The white snowflakes DRIFT STEADILY DOWNWARD across the blue field, from the top of the wall toward the bottom, each one fading out as it reaches the lowest row of bulbs while a new one lights up near the top, so the number of snowflakes on the wall never alters.
- Both Christmas trees SWAY gently left and right from their bases like trees in a light breeze, and their coloured baubles blink on and off in a slow cycle.
The picture stays ANCHORED to the front wall. It does not rotate, does not spin, does not sweep across as one sheet, does not slide sideways, does not scroll and does not drift as a whole. Whatever the bulbs do on the left of the wall they do at the same instant and at the same speed on the right. The lights exist ONLY on the front wall of the house where the curtain hangs - the roof, the sides of the house, the porch ceiling and the ground carry no picture and stay as they are. The warm porch lantern and the warm lit windows stay on and read through the lights.

CAMERA - HELD IPHONE, LOCKED FRAMING. One single continuous handheld vertical shot from a phone held up at head height in the middle of the crowd, exactly the framing of REFERENCE IMAGE 1. NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO orbit, NO cuts, NO slow motion, NO speed ramp. The house, the porch and the crowd all stay exactly the same size in frame from the first frame to the last. Handheld micro-shake only.

POSITIVE LOCKS: real-time playback speed throughout, exactly as fast as this would happen on a real street. The crowd stays in the foreground with their backs to camera the whole clip. The house is dark until 2.2s and lit from 2.2s to the end.

HARD RULES: nobody turns round to face the camera. The family never turns back toward the camera once they have turned to the house. The wall never goes dark again. DO NOT CHANGE the house, the porch, the dusk sky, the snow or the crowd. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO WATERMARK anywhere in the video. No subtitles.

AUDIO: real lip-synced voices - the crowd and the family chanting "Three... two... ONE!" together, then a big genuine cheer, whooping, laughing and clapping. Cold outdoor night ambience, boots in snow, coats rustling. No narration. (no BGM)

LOOK: real iPhone UGC shot at dusk. Deep blue sky, warm porch light, the lit wall clipping slightly bright the way a phone sensor really does, tack sharp, fine natural sensor grain, no bokeh, no cinematic grade, no lens flare, no slow motion, no speed ramp. Nothing looks weightless, rubbery or animated.
```


### C01 g2 (clip)

**File** clips/v35_c01_g2.mp4 · **Job** 85f2ded8-8ad3-4865-86e1-d361f4182367 · **md5** fc1094b002818690a47d40143b328f38 · 1532594 bytes
**Start image** starting_frames/v35_c01_g3.png (job 29f6e4cb-8a99-4cd2-bf42-d63ef0931741)
**References** v35_c01_r2.png, the lit pixel artwork (job dc410a06-b67d-4b52-943a-a3df3b7b8b7c)
**Settings** seedance_2_5 · omni_reference · 720p · 9:16 · 5s · generate_audio true · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612

**Why this take** Daniel rejected g1, verbatim: "The didn't camed out natural at all, they are all bad. / V35 - the family should normally turn around, not jumping, and the cheering at the and with the aplause it's very fake".

**What changed from g1** Prompt edit only - same starting frame.
1. New standalone block near the top: "EVERYBODY KEEPS THEIR FEET ON THE GROUND. Nobody jumps, nobody hops, nobody bounces on the spot, nobody springs up, nobody is lifted, nobody spins..."
2. The 1.5-2.2s turn beat rewritten as an ordinary unhurried half-turn - feet step round, shoulders lead, heads follow, arms stay down at their sides - with an explicit no jump / no hop / no bounce / no spin / no arms up / no twirl list.
3. The 2.5-5.0s reaction beat rewritten as quiet staggered individual reactions at different moments: heads tilt back, one man points at Santa, a woman covers her mouth and laughs, someone speaks to a neighbour, a child leans into a parent.
4. New standalone block: "NOBODY APPLAUDS AND NOBODY CHEERS..." banning clapping, whooping, crowd roar, unison cheer, raised fists, jumping for joy, group hug and confetti, and naming the reaction as scattered rather than choreographed.
5. AUDIO rewritten to quiet gasps, a soft "ohhh", one short laugh and murmured words, with NO APPLAUSE, NO CLAPPING, no whooping, no cheering, no crowd roar, no stadium noise, no canned audience track, no laugh track.
6. POSITIVE LOCKS gained "Everybody's feet stay on the ground for the whole clip."
The whole PICTURE ON THE HOUSE named-subject block (waving arm, snowflakes with fade-out/fade-in so the count holds, trees swaying from their bases, field ANCHORED) is unchanged from g1.

#### Video prompt - v35 C01 g2 (verbatim)

```
Animate REFERENCE IMAGE 1 exactly as it is. The first frame of the video IS REFERENCE IMAGE 1, unchanged - same pale gable-front two-storey house, same covered porch with its white posts, same warm porch lantern and warm lit windows, same deep blue dusk sky, same family of four standing together on the porch facing the camera, same crowd of neighbours in winter coats and knitted hats packed across the foreground with their backs to the camera, same snow, same dark unlit front wall.

EVERYONE COUNTS DOWN TOGETHER, OUT LOUD. The crowd in the foreground and the family on the porch count in unison in real voices: "Three... two... ONE!" Warm, smiling, breath fogging in the cold.

EVERYBODY KEEPS THEIR FEET ON THE GROUND. Nobody jumps, nobody hops, nobody bounces on the spot, nobody springs up, nobody is lifted, nobody spins. This is a group of ordinary neighbours standing in the snow on a cold evening - they shift their weight, they lean, they turn their heads, and that is the whole extent of it.

ACTION TIMELINE (5 seconds, one continuous take, no cuts):
0.0-0.8s - "Three!" The crowd counts, standing where they are, heads up toward the house. Two or three phones are held up filming. The family on the porch count with them, still facing the camera.
0.8-1.5s - "Two!" A little louder. The family on the porch begin to turn.
1.5-2.2s - The family of four turn calmly right round on the spot to face the house, backs to the camera, shoulder to shoulder exactly like the crowd. It is an ordinary unhurried half-turn, the way anyone turns to look at something behind them: their feet step round, their shoulders lead, their heads follow, their arms stay down at their sides. They do not jump, do not hop, do not bounce, do not spin, do not throw their arms up and do not twirl. On the last of that turn everyone says "ONE!"
2.2-2.5s - The whole front wall of the house switches on at once.
2.5-5.0s - The picture on the wall runs. The reaction is quiet, delayed and real, and it happens at different moments for different people rather than all at once: heads tilt back to take in the whole wall, one man lifts a hand to point up at Santa, a woman near the front puts a hand over her mouth and laughs, someone turns to the person beside them and says something, a child on the porch leans in against a parent. THE MOTION ENDS HERE, with the picture still lit and still running and the crowd still standing there watching it on the last frame.

NOBODY APPLAUDS AND NOBODY CHEERS. No clapping, no hands together, no whooping, no crowd roar, no unison cheer, no arms punched into the air, no fists raised, no jumping for joy, no group hug, no confetti. The reaction is a handful of quiet individual reactions scattered across a few seconds, not one choreographed celebration.

THE PICTURE ON THE HOUSE IS THE MAIN SUBJECT FROM 2.2s ONWARD. The front wall of the house is a giant low-resolution screen made of hanging LED curtain strands, showing exactly the picture in REFERENCE IMAGE 2 - a cartoon Santa in a red suit with a white beard filling the upper wall on a deep blue field, big white snowflakes scattered around him, one green Christmas tree with coloured baubles in the bottom-left corner of the wall and another in the bottom-right corner, all built out of individual glowing bulbs acting as pixels. It is not a still picture. Three things move in it, continuously, from 2.2s to the very last frame:
- Santa's raised hand WAVES side to side, a steady friendly wave, about one wave per second. Only his arm moves; his body, face and beard stay exactly where they are.
- The white snowflakes DRIFT STEADILY DOWNWARD across the blue field, from the top of the wall toward the bottom, each one fading out as it reaches the lowest row of bulbs while a new one lights up near the top, so the number of snowflakes on the wall never alters.
- Both Christmas trees SWAY gently left and right from their bases like trees in a light breeze, and their coloured baubles blink on and off in a slow cycle.
The picture stays ANCHORED to the front wall. It does not rotate, does not spin, does not sweep across as one sheet, does not slide sideways, does not scroll and does not drift as a whole. Whatever the bulbs do on the left of the wall they do at the same instant and at the same speed on the right. The lights exist ONLY on the front wall of the house where the curtain hangs - the roof, the sides of the house, the porch ceiling and the ground carry no picture and stay as they are. The warm porch lantern and the warm lit windows stay on and read through the lights.

CAMERA - HELD IPHONE, LOCKED FRAMING. One single continuous handheld vertical shot from a phone held up at head height in the middle of the crowd, exactly the framing of REFERENCE IMAGE 1. NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO orbit, NO cuts, NO slow motion, NO speed ramp. The house, the porch and the crowd all stay exactly the same size in frame from the first frame to the last. Handheld micro-shake only.

POSITIVE LOCKS: real-time playback speed throughout, exactly as fast as this would happen on a real street. Everybody's feet stay on the ground for the whole clip. The crowd stays in the foreground with their backs to camera the whole clip. The house is dark until 2.2s and lit from 2.2s to the end.

HARD RULES: nobody turns round to face the camera. The family never turns back toward the camera once they have turned to the house. The wall never goes dark again. DO NOT CHANGE the house, the porch, the dusk sky, the snow or the crowd. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO WATERMARK anywhere in the video. No subtitles.

AUDIO: real lip-synced voices - the crowd and the family counting "Three... two... ONE!" together, then a scattering of genuine low reactions as the lights come on: quiet gasps, a soft "ohhh", one short laugh, a few murmured words between neighbours, overlapping and untidy and arriving at different moments rather than all together. NO APPLAUSE, NO CLAPPING, no whooping, no cheering, no crowd roar, no stadium noise, no canned audience track, no laugh track. Cold outdoor night ambience, boots shifting in snow, coats rustling. No narration. (no BGM)

LOOK: real iPhone UGC shot at dusk. Deep blue sky, warm porch light, the lit wall clipping slightly bright the way a phone sensor really does, tack sharp, fine natural sensor grain, no bokeh, no cinematic grade, no lens flare, no slow motion, no speed ramp. Nothing looks weightless, rubbery or animated.
```


### C01 g3 (clip)

- **File** `clips/v35_c01_g3.mp4`
- **Job** `7de89730-02d2-48db-8901-f98e0b86ef6f`
- **md5** `df5a72c3ec3baa2b574cced2ca47e656` · 2103145 bytes
- **Start image** `v35_c01_g3.png` (media `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`)
- **References** `v35_c01_r2.png` — the lit pixel artwork (media `dc410a06-b67d-4b52-943a-a3df3b7b8b7c`)
- **Settings** seedance 2.5 · omni_reference · 720p · 9:16 · 5s · audio on · count 1
- **Lineage** Reused from v35 C01 g1 — changed: the family's turn only.

**Reason for the re-roll** — Daniel on g2: *"you completly fucked all of them over, wait for my next comands"*, then: *"V35 - it's not good. The first try was better, use the prompt used for the first try and make the family turn around normal, just this thing"*.

**What changed from g2**
1. g2 is discarded entirely. The base is the **g1** prompt again, byte-identical, including the crowd's bouncing shoulders, the fist punch, the 2.5-5.0s eruption with arms up and clapping, and the g1 AUDIO line with "a big genuine cheer, whooping, laughing and clapping". g2's feet-on-ground block, staggered quiet reactions, no-applause block and rewritten AUDIO are all gone — that rewrite was the over-correction he rejected.
2. Exactly two lines differ from g1, both about the turn and nothing else:
   - 0.8-1.5s: "The family on the porch begin to **swing** round." -> "begin to **turn** round."
   - 1.5-2.2s: the jump-turn beat replaced with an ordinary unhurried half-turn — feet step round, shoulders lead, heads follow, arms down at their sides, feet stay on the ground, and an explicit no jump / no hop / no bounce / no spin / no twirl.

#### Video prompt - v35 C01 g3 (verbatim)

```
Animate REFERENCE IMAGE 1 exactly as it is. The first frame of the video IS REFERENCE IMAGE 1, unchanged - same pale gable-front two-storey house, same covered porch with its white posts, same warm porch lantern and warm lit windows, same deep blue dusk sky, same family of four standing together on the porch facing the camera, same crowd of neighbours in winter coats and knitted hats packed across the foreground with their backs to the camera, same snow, same dark unlit front wall.

EVERYONE COUNTS DOWN TOGETHER, OUT LOUD. The crowd in the foreground and the family on the porch chant in unison in real voices: "Three... two... ONE!" Grinning, excited, breath fogging in the cold.

ACTION TIMELINE (5 seconds, one continuous take, no cuts):
0.0-0.8s - "Three!" The crowd chants, shoulders bouncing, a couple of arms and a raised phone going up. The family on the porch chant with them, still facing the camera.
0.8-1.5s - "Two!" Louder. A fist punches up in the crowd. The family on the porch begin to turn round.
1.5-2.2s - The family of four turn calmly right round on the spot to face the house, backs to the camera, shoulder to shoulder exactly like the crowd. It is an ordinary unhurried half-turn, the way anyone turns to look at something behind them: their feet step round, their shoulders lead, their heads follow, their arms stay down at their sides, and their feet stay on the ground. They do not jump, do not hop, do not bounce, do not spin and do not twirl. On the last of that turn everybody shouts "ONE!"
2.2-2.5s - The whole front wall of the house switches on at once.
2.5-5.0s - The picture on the wall runs. The crowd erupts - arms up, hands clapping, heads tipping back, two of the children on the porch bouncing on the spot. THE MOTION ENDS HERE, with the picture still lit and still running and the crowd still cheering on the last frame.

THE PICTURE ON THE HOUSE IS THE MAIN SUBJECT FROM 2.2s ONWARD. The front wall of the house is a giant low-resolution screen made of hanging LED curtain strands, showing exactly the picture in REFERENCE IMAGE 2 - a cartoon Santa in a red suit with a white beard filling the upper wall on a deep blue field, big white snowflakes scattered around him, one green Christmas tree with coloured baubles in the bottom-left corner of the wall and another in the bottom-right corner, all built out of individual glowing bulbs acting as pixels. It is not a still picture. Three things move in it, continuously, from 2.2s to the very last frame:
- Santa's raised hand WAVES side to side, a steady friendly wave, about one wave per second. Only his arm moves; his body, face and beard stay exactly where they are.
- The white snowflakes DRIFT STEADILY DOWNWARD across the blue field, from the top of the wall toward the bottom, each one fading out as it reaches the lowest row of bulbs while a new one lights up near the top, so the number of snowflakes on the wall never alters.
- Both Christmas trees SWAY gently left and right from their bases like trees in a light breeze, and their coloured baubles blink on and off in a slow cycle.
The picture stays ANCHORED to the front wall. It does not rotate, does not spin, does not sweep across as one sheet, does not slide sideways, does not scroll and does not drift as a whole. Whatever the bulbs do on the left of the wall they do at the same instant and at the same speed on the right. The lights exist ONLY on the front wall of the house where the curtain hangs - the roof, the sides of the house, the porch ceiling and the ground carry no picture and stay as they are. The warm porch lantern and the warm lit windows stay on and read through the lights.

CAMERA - HELD IPHONE, LOCKED FRAMING. One single continuous handheld vertical shot from a phone held up at head height in the middle of the crowd, exactly the framing of REFERENCE IMAGE 1. NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO orbit, NO cuts, NO slow motion, NO speed ramp. The house, the porch and the crowd all stay exactly the same size in frame from the first frame to the last. Handheld micro-shake only.

POSITIVE LOCKS: real-time playback speed throughout, exactly as fast as this would happen on a real street. The crowd stays in the foreground with their backs to camera the whole clip. The house is dark until 2.2s and lit from 2.2s to the end.

HARD RULES: nobody turns round to face the camera. The family never turns back toward the camera once they have turned to the house. The wall never goes dark again. DO NOT CHANGE the house, the porch, the dusk sky, the snow or the crowd. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO WATERMARK anywhere in the video. No subtitles.

AUDIO: real lip-synced voices - the crowd and the family chanting "Three... two... ONE!" together, then a big genuine cheer, whooping, laughing and clapping. Cold outdoor night ambience, boots in snow, coats rustling. No narration. (no BGM)

LOOK: real iPhone UGC shot at dusk. Deep blue sky, warm porch light, the lit wall clipping slightly bright the way a phone sensor really does, tack sharp, fine natural sensor grain, no bokeh, no cinematic grade, no lens flare, no slow motion, no speed ramp. Nothing looks weightless, rubbery or animated.
```

---

## Upscale run — 2026-09-19

All eight picked takes upscaled with **ByteDance Upscale · Model version Pro · 2K · 30fps**.
Preset **AIGC** on the hook (C01), **Common** on C02–C08 — the same split Daniel specified for v35.

Results are saved in `clips/upscaled/` under the **source's exact filename** (the folder is the
suffix — no `_2k`, no `_upscaled`). All eight come back **1440×2560 @ 30fps**.

**Which take was upscaled, and why.** The board carries no v35 cards yet, so the picked take per
shot was resolved off this file's rejection chain: the highest generation of each shot is the
re-roll that answered Daniel's last note on it, and no higher generation was itself rejected.
C01 → g3 (g1 "didn't come out natural", g2 the over-correction he rejected), C02 → g2 (g1 cart
"very fake and unnatural"), C04 → g3 (g2 shake "too aggressive"), everything else single-take.

**Model version is not reachable from the MCP.** `upscale_video`'s bytedance branch accepts only
`provider`, `video_id`, `width`, `height`, `resolution`, `fps`, `preset`, with
`additionalProperties: false`; passing `model_version` returns `Unrecognized key: "model_version"`,
and `models_explore` lists no ByteDance upscale model. Standard/Pro is **UI-only**, so this run was
driven through `https://higgsfield.ai/upscale` in the browser, exactly like the v33 run.

| Shot | Source clip | Src bytes | Preset | Upscale job | Result bytes | Result md5 |
|---|---|---|---|---|---|---|
| C01 | `v35_c01_g3.mp4` | 2103145 | **AIGC** | `28c2ca67-3d3d-4b34-b3f8-8a047656a3fa` | 9283270 | `c16f5a4df350145d675f26f23c1c4fd8` |
| C02 | `v35_c02_g2.mp4` | 3729029 | Common | `19960f3a-8461-4024-b799-96249edf80b9` | 8814725 | `6af5786c8eba36ebc7a145afd9a7cf5e` |
| C03 | `v35_c03_g1.mp4` | 2193322 | Common | `65c01ae2-48a4-4124-bb3e-5e0943109a19` | 8817111 | `fe74a9bd695e0385ffd5ec22317daca4` |
| C04 | `v35_c04_g3.mp4` | 1930293 | Common | `94402cf7-0cad-439b-8370-7c30046598d4` | 8800715 | `eebdb1808e65b4b2bf9a11fdcacaf073` |
| C05 | `v35_c05_g1.mp4` | 2551483 | Common | `84077919-589f-4f04-9984-d5060978c1d8` | 8816211 | `41178c099bf6752913b0d85763db23b7` |
| C06 | `v35_c06_g1.mp4` | 2846061 | Common | `5844ea8a-5ce7-457f-b12a-35058c78d080` | 8671359 | `8bb901a3cc0937b62e336ac429966f35` |
| C07 | `v35_c07_g1.mp4` | 2382794 | Common | `2db37fb0-ccce-417b-829d-f72853deff66` | 8917827 | `274b67799bee28f9006ab77014ba60c0` |
| C08 | `v35_c08_g1.mp4` | 2073062 | Common | `00e3dd04-7d22-451d-acf9-bf4d0e7cae5d` | 7428557 | `fea55d506c6d2b5bdd2a54979f5f4f83` |

Cost: 2.02 credits for the AIGC job, 1.62 each for the seven Common jobs.

**How the source clip gets into the page.** `file_upload` no longer accepts host filesystem paths.
Each clip was fetched back from Higgsfield's own CDN inside the page and injected through a
`DataTransfer` into `input[type=file]`. The fetched blob's byte count was checked against the local
file **before** every submit — on the v33 run a single mistyped character in a job id silently
returned 403, and a wrong-but-valid id would have upscaled the wrong clip at full price.

**The sticky-preset trap, confirmed again.** Preset persists across navigations. After the C01
submit on AIGC, a freshly loaded `/upscale` still read AIGC for C02 — it was switched back to
Common explicitly and then zoom-verified. Every one of the eight panels was zoom-read
(model / version / resolution / fps / preset) immediately before its submit. Clicking a preset
option or the submit button by raw screen coordinate does nothing on this app; `find` plus a click
by element ref works every time.

**Pulling results down.** The upscale jobs are invisible to `show_generation_by_ids`
(`lookup_failed` for all eight) and the assets grid no longer exposes `video-job--` links, so each
result URL was read off `video.currentSrc` on
`https://higgsfield.ai/upscale/desktop?media=video-job--<id>`. The sandbox can curl
`d8j0ntlcm91z4.cloudfront.net` directly, so nothing was downloaded through the browser. A 4–5s
2K/30fps job took roughly 2–4 minutes.


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v35_c01_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v35_c02_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v35_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v35_c04_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v35_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v35_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v35_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v35_c08_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c01_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c02_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c04_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v35_c08_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v35_c01_r1.png` | Embedded PNG `hf-job-id`: `bf5da344-7730-412a-a2c5-acbbd2400d9d`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v35_c01_r2.png` | Embedded PNG `hf-job-id`: `dc410a06-b67d-4b52-943a-a3df3b7b8b7c`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v35_c06_r1.png` | Embedded PNG `hf-job-id`: `a9cec9e7-aa44-4a1a-8780-14c39d38cdb0`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v35_c06_r2.png` | Embedded PNG `hf-job-id`: `107c34e8-06b6-4303-afd6-0728eb6de24e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c01_g1.png` | Embedded PNG `hf-job-id`: `4158136d-43a7-45d1-9ee4-288669e8c9d2`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c01_g2.png` | Embedded PNG `hf-job-id`: `69585bbd-02a1-450b-b4da-d302a721d059`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c01_g3.png` | Embedded PNG `hf-job-id`: `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c02_g1.png` | Embedded PNG `hf-job-id`: `5d7f2b94-6446-4bcf-a35e-a427bc4707e4`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c03_g1.png` | Embedded PNG `hf-job-id`: `f53983c6-ebab-4542-bd7d-901184f78984`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c04_g1.png` | Embedded PNG `hf-job-id`: `dd9d90f9-79e5-4792-bda0-209f97b65890`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c04_g2.png` | Embedded PNG `hf-job-id`: `01242684-615e-4bfe-be76-aaf56437f91e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c05_g1.png` | Embedded PNG `hf-job-id`: `940c5e2d-4958-4ea5-adad-121f9eacdd5a`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c05_g2.png` | Embedded PNG `hf-job-id`: `55a6a06f-4df9-49bc-b3c6-182c94af8510`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c06_g1.png` | Embedded PNG `hf-job-id`: `c0339254-04bb-49ff-8d17-f49b42daec08`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c07_g1.png` | Embedded PNG `hf-job-id`: `646ce417-da2b-410d-a602-20cb46e09178`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c07_g2.png` | Embedded PNG `hf-job-id`: `f1c59969-baec-4f01-8c8f-52026ef97a8f`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c08_g1.png` | Embedded PNG `hf-job-id`: `cbd75703-07a7-4b2d-8dc1-7e4969d83bac`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v35_c08_g2.png` | Embedded PNG `hf-job-id`: `3c93d061-da86-486d-8e60-e326013cfb6f`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |



---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: clips byte-identical (md5) to their Higgsfield result unless the entry says otherwise, generated images by exact byte size, and every start frame checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C02: the board did not show the exact clip prompt of `v35_c02_g2.mp4`; it now does.
- C03: the board did not show the exact clip prompt of `v35_c03_g1.mp4`; it now does.
- C04: the board did not show the exact clip prompt of `v35_c04_g3.mp4`; it now does.
- C05: the board did not show the exact clip prompt of `v35_c05_g1.mp4`; it now does.
- C06: the board did not show the exact clip prompt of `v35_c06_g1.mp4`; it now does.
- C07: the board showed `v35_c07_g1.png` as the start frame, but the clip in the cut was animated from `v35_c07_g2.png` (the Higgsfield start image). Card corrected.
- C07: the board did not show the exact image prompt of `v35_c07_g2.png`; it now does.
- C07: the board did not show the exact clip prompt of `v35_c07_g1.mp4`; it now does.
- C08: the board showed `v35_c08_g1.png` as the start frame, but the clip in the cut was animated from `v35_c08_g2.png` (the Higgsfield start image). Card corrected.
- C08: the board did not show the exact image prompt of `v35_c08_g2.png`; it now does.
- C08: the board did not show the exact clip prompt of `v35_c08_g1.mp4`; it now does.

### C01 — The street watches the house light up

**In the cut:** `starting_frames/v35_c01_g3.png`, `references/v35_c01_r2.png` → `clips/v35_c01_g3.mp4`

#### Image prompt — `starting_frames/v35_c01_g3.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_184120_29f6e4cb-8a99-4cd2-bf42-d63ef0931741.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/starting_frames/v35_c01_g2.png` · Higgsfield media `69585bbd-02a1-450b-b4da-d302a721d059`
- @Image 2: `content/video_35_assets/starting_frames/v35_c06_g1.png` · Higgsfield media `c0339254-04bb-49ff-8d17-f49b42daec08`

````text
A real iPhone photo, vertical 9:16, shot outdoors on a suburban front lawn at DUSK, almost night.

REFERENCE IMAGE 1 IS THE PHOTO TO CHANGE. Keep everything about it: the same large two-storey cream clapboard house with its wide front gable, white trim, covered porch on square white posts, deep red front door with an evergreen wreath and warm black lantern sconce; the same six real white-framed windows with sills and glazing bars, three of them glowing warm from inside; the same family of four out in front of the porch facing the camera (father in a dark green parka with one arm raised in a half-wave, mother in a long camel wool coat and cream beanie, a boy of about ten in a red puffer jacket, a girl of about six in a pink snowsuit); the same big crowd of more than fifteen neighbours in the near foreground in near-silhouette with their BACKS TO THE CAMERA facing the house; the same deep blue dusk sky with a last cold band of orange low on the horizon; the same snow; the same completely UNLIT dark curtain over the whole front of the house.

CHANGE ONE THING: MOVE EVERYTHING MUCH CLOSER. THE LAST ATTEMPT WAS SHOT FROM FAR TOO FAR AWAY.

CLOSE IN. The camera has walked forward into the middle of the crowd and is now only a few metres from the family:
- The FRONT ROW OF THE CROWD IS RIGHT UP AT THE HOUSE. The nearest neighbours' backs are standing almost at the bottom of the porch steps, an arm's length or two from the family - NOT across the lawn from them. THERE IS NO WIDE EMPTY STRETCH OF SNOWY LAWN between the crowd and the family. The gap is small and the two groups nearly touch.
- The dark heads and shoulders of the nearest neighbours are BIG and CLOSE, filling the bottom third of the frame, cut off by the bottom edge and the side edges, heavily out of the way of the subject but unmistakably near the lens.
- The FAMILY IS LARGE IN FRAME. Read their faces, their coats, the father's raised hand. They stand well above the crowd's heads.
- The HOUSE LOOMS. It is close enough that it fills the frame from the left edge to the right edge and rises high, the porch roof and the whole upper storey and the gable stacked up above the family. Being nearer makes it bigger, not smaller.

THE CURTAIN - the entire front of the house is covered by the light curtain and IT IS COMPLETELY UNLIT. Exactly as dense as in REFERENCE IMAGE 2: many, many thin BLACK vertical wires hung very close together side by side from header cables pinned along the eaves and along the porch roof, only a narrow gap between neighbouring strands, hanging straight down and covering the whole cream gable wall, the whole upper storey and the wall on either side of the porch, edge to edge, top to bottom, with no bare patch anywhere. Each wire carries small round bulbs spaced along it and every single bulb is DARK, DULL GREY and UNLIT. It reads as a fine dense dark veil laid over the pale cream house - the black strands stand out plainly against the pale clapboard, and the clapboard boards, the white trim, the window frames, the glazing bars and the lit rooms all read clearly straight through the gaps between the strands.

THE WIRE IS BLACK: NOT white, NOT clear, NOT silver, NOT copper. EVERY STRAND IS IDENTICAL - CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the sheet to the other, top to bottom. There must be NO section anywhere where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice - only plain vertical strands hanging straight down. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a projection - it is separate hanging strings with visible gaps between them.

There is NO lit artwork and NO glowing curtain anywhere in this photograph. The only light sources are the porch lantern, a cold street lamp at the edge and the three warm windows.

THE CLEAN BAND AT THE TOP - the TOP EIGHTH OF THE FRAME, full width, is nothing but empty deep-blue dusk sky. No roof, no gable peak, no branch, no wire, no raised phone. Everything else sits below it.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural dusk colour, fine natural sensor grain, every strand, every dark bulb and every window frame crisply resolved. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no bokeh, no colour grading, no fisheye or barrel distortion, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers, words, logos or writing anywhere in the photograph.
````

#### Image prompt — `references/v35_c01_r2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `dc410a06-b67d-4b52-943a-a3df3b7b8b7c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_193315_dc410a06-b67d-4b52-943a-a3df3b7b8b7c.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/references/v35_c01_r1.png` · Higgsfield media `bf5da344-7730-412a-a2c5-acbbd2400d9d`
- @Image 2: uploaded file, not on the drive · Higgsfield media `ca55e296-fb0e-4c9d-ba1d-8e94307438c0`

````text
Recreate REFERENCE IMAGE 1 as a real iPhone photograph. Keep it exactly as it is - the same camera position, the same camera height, the same distance, the same crop, the same house, the same porch, the same family with their backs to camera, the same crowd of neighbours in the foreground, the same dusk light. Change only one thing:

The lights on the house are no longer a plain twinkling pattern. The LED curtain now displays a big picture, made of the individual bulbs acting as pixels, in exactly the style of REFERENCE IMAGE 2 - dense rows of glowing bulbs forming a bold, simple cartoon image with flat saturated colour and clean shapes, bright enough to read from across the street.

The picture on the wall is: a jolly cartoon Santa Claus in a red suit and white beard, seen from the waist up, filling the upper part of the wall with his raised hand waving, on a deep blue night background scattered with big white snowflakes, and one green Christmas tree with coloured baubles in the bottom left corner of the wall and another in the bottom right corner. The picture is built into the curtain of lights and covers the front wall of the house only. The windows and the front door stay where they are and read through the lights. The roof, the sides of the house and the ground stay dark.

Nothing else changes.

A real photograph shot on a modern iPhone, tack sharp, correct exposure, clean natural dusk light. Not blurry, not soft, no motion blur, no bokeh, no CGI or 3D-render look. No text, letters, numbers, logos, captions, watermarks, buttons, icons or interface overlays anywhere in the photograph.
````

#### Video prompt — `clips/v35_c01_g3.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `7de89730-02d2-48db-8901-f98e0b86ef6f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_205525_7de89730-02d2-48db-8901-f98e0b86ef6f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c01_g3.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c01_g3.png` · Higgsfield media `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`
- image ref 1: `content/video_35_assets/references/v35_c01_r2.png` · Higgsfield media `dc410a06-b67d-4b52-943a-a3df3b7b8b7c`

````text
Animate REFERENCE IMAGE 1 exactly as it is. The first frame of the video IS REFERENCE IMAGE 1, unchanged - same pale gable-front two-storey house, same covered porch with its white posts, same warm porch lantern and warm lit windows, same deep blue dusk sky, same family of four standing together on the porch facing the camera, same crowd of neighbours in winter coats and knitted hats packed across the foreground with their backs to the camera, same snow, same dark unlit front wall.

EVERYONE COUNTS DOWN TOGETHER, OUT LOUD. The crowd in the foreground and the family on the porch chant in unison in real voices: "Three... two... ONE!" Grinning, excited, breath fogging in the cold.

ACTION TIMELINE (5 seconds, one continuous take, no cuts):
0.0-0.8s - "Three!" The crowd chants, shoulders bouncing, a couple of arms and a raised phone going up. The family on the porch chant with them, still facing the camera.
0.8-1.5s - "Two!" Louder. A fist punches up in the crowd. The family on the porch begin to turn round.
1.5-2.2s - The family of four turn calmly right round on the spot to face the house, backs to the camera, shoulder to shoulder exactly like the crowd. It is an ordinary unhurried half-turn, the way anyone turns to look at something behind them: their feet step round, their shoulders lead, their heads follow, their arms stay down at their sides, and their feet stay on the ground. They do not jump, do not hop, do not bounce, do not spin and do not twirl. On the last of that turn everybody shouts "ONE!"
2.2-2.5s - The whole front wall of the house switches on at once.
2.5-5.0s - The picture on the wall runs. The crowd erupts - arms up, hands clapping, heads tipping back, two of the children on the porch bouncing on the spot. THE MOTION ENDS HERE, with the picture still lit and still running and the crowd still cheering on the last frame.

THE PICTURE ON THE HOUSE IS THE MAIN SUBJECT FROM 2.2s ONWARD. The front wall of the house is a giant low-resolution screen made of hanging LED curtain strands, showing exactly the picture in REFERENCE IMAGE 2 - a cartoon Santa in a red suit with a white beard filling the upper wall on a deep blue field, big white snowflakes scattered around him, one green Christmas tree with coloured baubles in the bottom-left corner of the wall and another in the bottom-right corner, all built out of individual glowing bulbs acting as pixels. It is not a still picture. Three things move in it, continuously, from 2.2s to the very last frame:
- Santa's raised hand WAVES side to side, a steady friendly wave, about one wave per second. Only his arm moves; his body, face and beard stay exactly where they are.
- The white snowflakes DRIFT STEADILY DOWNWARD across the blue field, from the top of the wall toward the bottom, each one fading out as it reaches the lowest row of bulbs while a new one lights up near the top, so the number of snowflakes on the wall never alters.
- Both Christmas trees SWAY gently left and right from their bases like trees in a light breeze, and their coloured baubles blink on and off in a slow cycle.
The picture stays ANCHORED to the front wall. It does not rotate, does not spin, does not sweep across as one sheet, does not slide sideways, does not scroll and does not drift as a whole. Whatever the bulbs do on the left of the wall they do at the same instant and at the same speed on the right. The lights exist ONLY on the front wall of the house where the curtain hangs - the roof, the sides of the house, the porch ceiling and the ground carry no picture and stay as they are. The warm porch lantern and the warm lit windows stay on and read through the lights.

CAMERA - HELD IPHONE, LOCKED FRAMING. One single continuous handheld vertical shot from a phone held up at head height in the middle of the crowd, exactly the framing of REFERENCE IMAGE 1. NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO orbit, NO cuts, NO slow motion, NO speed ramp. The house, the porch and the crowd all stay exactly the same size in frame from the first frame to the last. Handheld micro-shake only.

POSITIVE LOCKS: real-time playback speed throughout, exactly as fast as this would happen on a real street. The crowd stays in the foreground with their backs to camera the whole clip. The house is dark until 2.2s and lit from 2.2s to the end.

HARD RULES: nobody turns round to face the camera. The family never turns back toward the camera once they have turned to the house. The wall never goes dark again. DO NOT CHANGE the house, the porch, the dusk sky, the snow or the crowd. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO WATERMARK anywhere in the video. No subtitles.

AUDIO: real lip-synced voices - the crowd and the family chanting "Three... two... ONE!" together, then a big genuine cheer, whooping, laughing and clapping. Cold outdoor night ambience, boots in snow, coats rustling. No narration. (no BGM)

LOOK: real iPhone UGC shot at dusk. Deep blue sky, warm porch light, the lit wall clipping slightly bright the way a phone sensor really does, tack sharp, fine natural sensor grain, no bokeh, no cinematic grade, no lens flare, no slow motion, no speed ramp. Nothing looks weightless, rubbery or animated.
````

**Other takes of C01 on disk (5)**

#### Image prompt — `starting_frames/v35_c01_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `4158136d-43a7-45d1-9ee4-288669e8c9d2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_181657_4158136d-43a7-45d1-9ee4-288669e8c9d2.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_33_assets/starting_frames/v33_c06_g2.png` · Higgsfield media `08a6fdc9-6e1f-475c-a1ad-4a5740d54085`
- @Image 2: `content/video_35_assets/starting_frames/v35_c06_g1.png` · Higgsfield media `c0339254-04bb-49ff-8d17-f49b42daec08`

````text
A real iPhone photo, vertical 9:16, shot outdoors on a suburban front lawn at DUSK, almost night.

CAMERA AND FRAMING - copy the CROWD COMPOSITION of REFERENCE IMAGE 1 exactly, and nothing else from it. The camera is standing INSIDE the crowd, at the eye level of someone in the middle of it, holding the phone up over the shoulders of the people in front. Backs of heads, hats and shoulders fill the bottom third of the frame in near-silhouette at a range of heights; beyond them the ground opens out and the front of the house fills the middle and upper part of the frame. Same low-in-the-crowd viewpoint, same depth, same proportion of foreground crowd to house.

DO NOT COPY FROM REFERENCE IMAGE 1: its house, its garage door, its lit picture, its colours or its glow. There is NO lit artwork and NO glowing curtain anywhere in this photograph.

THE CROWD - a BIG gathering, more than fifteen neighbours packed into the near foreground with their BACKS TO THE CAMERA, facing the house, in dark winter coats, parkas, bobble hats and scarves, several deep, adults and teenagers and small children on shoulders, heads at many different heights, a few phones held up filming, one person with a dog on a lead at the left edge. They read as dark silhouetted shapes against the pale house, breath steaming in the cold. Nobody in the crowd is turned toward the camera.

THE FAMILY - standing out on the snowy front lawn directly in front of their own house, facing the crowd and therefore FACING THE CAMERA, a family of four seen full-length at a distance: a father in a dark green parka with one arm raised in a half-wave, a mother in a long camel wool coat and a cream beanie, a boy of about ten in a red puffer jacket, and a girl of about six in a pink snowsuit holding her mother's hand. They stand in a loose line a few steps out from the porch, small in the frame, clearly separate from the crowd, plainly the hosts about to show something off. Their faces are lit softly by the porch light and read as pleased and a little nervous.

THE HOUSE - a DIFFERENT house from any reference: a two-storey WARM CREAM PAINTED CLAPBOARD house with a wide front gable, crisp white trim, a covered front porch with two square white posts, a deep red front door with an evergreen wreath on it, and a black lantern sconce glowing warm beside the door. A bare winter maple stands at the right edge, a low picket fence runs off to the left, and there is snow on the roof, on the porch rail and across the whole lawn.

THE CURTAIN - the entire front of the house is covered by the light curtain and IT IS COMPLETELY UNLIT. Exactly as dense as in REFERENCE IMAGE 2: many, many thin BLACK vertical wires hung very close together side by side from header cables pinned along the eaves and along the porch roof, only a narrow gap between neighbouring strands, hanging straight down and covering the whole cream gable wall above the porch and the wall on either side of the porch, edge to edge, top to bottom. Each wire carries small round bulbs spaced along it and every single bulb is DARK, DULL GREY and UNLIT. The curtain reads as a fine dense dark veil laid over the pale cream house - the black strands stand out plainly against the pale clapboard, and you can still clearly see the clapboard boards, the white trim and the gable shape straight through the gaps. The veil covers the whole facade: there is no bare patch of wall anywhere and it does not stop partway down. The bottom hem is uneven and wavy where the strands end at slightly different heights, and the strands sag a little in the cold air.

THE WIRE IS BLACK: NOT white, NOT clear, NOT silver, NOT copper. EVERY STRAND IS IDENTICAL - CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the sheet to the other, top to bottom. There must be NO section anywhere where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice - only plain vertical strands hanging straight down. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a projection - it is separate hanging strings with visible gaps between them.

THE LIGHT - almost night. The sky is deep blue dusk with a last band of cold pale orange low on the horizon behind the roofline, the first stars just showing at the top. The only lights burning are the warm porch lantern by the red door and a cold street lamp off to the left throwing a pool across the snow. The snow is blue-white in the shadows and warm where the porch light reaches it. The house and the dark veil over it are clearly legible but everything is unmistakably dusk, not daylight and not black night.

THE CLEAN BAND AT THE TOP - the TOP EIGHTH OF THE FRAME, full width, is nothing but empty deep-blue dusk sky. No roof, no gable peak, no branch, no wire, no raised phone. Everything else sits below it.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural dusk colour, fine natural sensor grain, every strand and every dark bulb crisply resolved. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no bokeh, no colour grading, no fisheye or barrel distortion, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers, words, logos or writing anywhere in the photograph.
````

#### Image prompt — `starting_frames/v35_c01_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `69585bbd-02a1-450b-b4da-d302a721d059`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_183025_69585bbd-02a1-450b-b4da-d302a721d059.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/starting_frames/v35_c01_g1.png` · Higgsfield media `4158136d-43a7-45d1-9ee4-288669e8c9d2`
- @Image 2: `content/video_35_assets/starting_frames/v35_c06_g1.png` · Higgsfield media `c0339254-04bb-49ff-8d17-f49b42daec08`

````text
A real iPhone photo, vertical 9:16, shot outdoors on a suburban front lawn at DUSK, almost night.

REFERENCE IMAGE 1 IS THE PHOTO TO CHANGE. Keep everything about it: the same camera standing INSIDE the crowd at the eye level of someone in the middle of it, the same big gathering of more than fifteen neighbours packed into the near foreground in near-silhouette with their BACKS TO THE CAMERA facing the house, the same family of four out on the snowy lawn facing the crowd and therefore facing the camera (father in a dark green parka with one arm raised in a half-wave, mother in a long camel wool coat and cream beanie, a boy of about ten in a red puffer jacket, a girl of about six in a pink snowsuit), the same deep blue dusk sky with a last cold band of orange low on the horizon, the same snow, the same warm porch lantern and cold street lamp as the only two lights burning, and the same completely UNLIT dark curtain hanging over the whole front of the house.

CHANGE TWO THINGS: MAKE THE HOUSE MUCH BIGGER, AND GIVE IT REAL WINDOWS.

THE HOUSE IS MUCH BIGGER. It is a LARGE two-storey family home, far taller and far wider than in REFERENCE IMAGE 1 - the kind of house with a proper upstairs. It fills the frame from the left edge to the right edge behind the crowd and its roofline rises high into the upper part of the picture. It TOWERS over the family standing on the lawn: a standing adult only reaches the top of the ground-floor windows, and there is a whole second storey of wall and then the gable above that. Warm cream painted clapboard, a wide front gable, crisp white trim, a covered front porch running along the front of it on square white posts, a deep red front door with an evergreen wreath, a black lantern sconce glowing warm beside the door, snow on the roof and along the porch rail.

THE WINDOWS - CRITICAL. THE LAST ATTEMPT HAD NO WINDOWS AT ALL AND THE HOUSE LOOKED COMPLETELY FAKE BECAUSE OF IT. This house has plenty of real windows and every one of them is clearly visible:
- TWO tall upstairs windows side by side in the gable wall above the porch roof.
- A smaller window up in the peak of the gable above those.
- TWO large ground-floor windows, one on each side of the front door, behind the porch.
- One more window on the side wall where it turns away from us.
Every window is a real window: white painted frame, a proper wooden sill, white glazing bars dividing the glass into panes, and real glass that catches a cold reflection of the dusk sky. THREE of them glow softly warm from inside - a table lamp behind one, a small lit Christmas tree visible through another - and the rest are dark. The hanging strands of the curtain pass IN FRONT of the glass, so you can see the white frames, the glazing bars and the lit rooms straight through the gaps between the strands.

THE CURTAIN - the entire front of the house is covered by the light curtain and IT IS COMPLETELY UNLIT. Exactly as dense as in REFERENCE IMAGE 2: many, many thin BLACK vertical wires hung very close together side by side from header cables pinned along the eaves and along the porch roof, only a narrow gap between neighbouring strands, hanging straight down and covering the whole cream gable wall, the whole upper storey and the wall on either side of the porch, edge to edge, top to bottom, with no bare patch anywhere. Each wire carries small round bulbs spaced along it and every single bulb is DARK, DULL GREY and UNLIT. It reads as a fine dense dark veil laid over the pale cream house - the black strands stand out plainly against the pale clapboard, and the clapboard boards, the white trim, the window frames and the gable shape all read clearly straight through the gaps. The bottom hem is uneven and wavy where the strands end at slightly different heights.

THE WIRE IS BLACK: NOT white, NOT clear, NOT silver, NOT copper. EVERY STRAND IS IDENTICAL - CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the sheet to the other, top to bottom. There must be NO section anywhere where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice - only plain vertical strands hanging straight down. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a projection - it is separate hanging strings with visible gaps between them.

There is NO lit artwork and NO glowing curtain anywhere in this photograph. The only light sources are the porch lantern, the street lamp and the three warm windows.

THE CLEAN BAND AT THE TOP - the TOP EIGHTH OF THE FRAME, full width, is nothing but empty deep-blue dusk sky. No roof, no gable peak, no branch, no wire, no raised phone. Everything else sits below it.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural dusk colour, fine natural sensor grain, every strand, every dark bulb and every window frame crisply resolved. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no bokeh, no colour grading, no fisheye or barrel distortion, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers, words, logos or writing anywhere in the photograph.
````

#### Image prompt — `references/v35_c01_r1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `bf5da344-7730-412a-a2c5-acbbd2400d9d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_192703_bf5da344-7730-412a-a2c5-acbbd2400d9d.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/starting_frames/v35_c01_g3.png` · Higgsfield media `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`

````text
Recreate REFERENCE IMAGE 1 as a real iPhone photograph. Keep it exactly as it is - the same camera position, the same camera height, the same distance, the same crop, the same house, the same porch, the same crowd of neighbours in the foreground with their backs to camera, the same dusk light. Change only these two things:

1. The family of four on the porch has turned around. They now face the house, with their backs to the camera, exactly like the crowd in the foreground. Same people, same clothes, same positions on the porch - only turned around.

2. The house is now fully lit. A hanging LED curtain of vertical light strands covers the front face of the house, and it is switched on and running a vivid Christmas animation - bright warm white and cool white lights chasing and twinkling in waves down the strands, a few strands lit ahead of the others so the pattern reads as moving. The light pattern exists ONLY on the strands of the curtain where the lights are hung. The rest of the house - the roof, the sides, the porch trim, the windows - has no light pattern on it and stays dark.

Nothing else changes.

A real photograph shot on a modern iPhone, tack sharp, correct exposure, clean natural dusk light. Not blurry, not soft, no motion blur, no bokeh, no CGI or 3D-render look. No text, letters, numbers, logos, captions, watermarks, buttons, icons or interface overlays anywhere in the photograph.
````

#### Video prompt — `clips/v35_c01_g1.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `2e2dd906-0b1b-4bf4-bdd3-9f6d98ccd4c3`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_195523_2e2dd906-0b1b-4bf4-bdd3-9f6d98ccd4c3.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c01_g3.png` · Higgsfield media `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`
- image ref 1: `content/video_35_assets/references/v35_c01_r2.png` · Higgsfield media `dc410a06-b67d-4b52-943a-a3df3b7b8b7c`

````text
Animate REFERENCE IMAGE 1 exactly as it is. The first frame of the video IS REFERENCE IMAGE 1, unchanged - same pale gable-front two-storey house, same covered porch with its white posts, same warm porch lantern and warm lit windows, same deep blue dusk sky, same family of four standing together on the porch facing the camera, same crowd of neighbours in winter coats and knitted hats packed across the foreground with their backs to the camera, same snow, same dark unlit front wall.

EVERYONE COUNTS DOWN TOGETHER, OUT LOUD. The crowd in the foreground and the family on the porch chant in unison in real voices: "Three... two... ONE!" Grinning, excited, breath fogging in the cold.

ACTION TIMELINE (5 seconds, one continuous take, no cuts):
0.0-0.8s - "Three!" The crowd chants, shoulders bouncing, a couple of arms and a raised phone going up. The family on the porch chant with them, still facing the camera.
0.8-1.5s - "Two!" Louder. A fist punches up in the crowd. The family on the porch begin to swing round.
1.5-2.2s - The family of four finish turning all the way around to face the house, backs to the camera, shoulder to shoulder exactly like the crowd, and on the last of that turn everybody shouts "ONE!"
2.2-2.5s - The whole front wall of the house switches on at once.
2.5-5.0s - The picture on the wall runs. The crowd erupts - arms up, hands clapping, heads tipping back, two of the children on the porch bouncing on the spot. THE MOTION ENDS HERE, with the picture still lit and still running and the crowd still cheering on the last frame.

THE PICTURE ON THE HOUSE IS THE MAIN SUBJECT FROM 2.2s ONWARD. The front wall of the house is a giant low-resolution screen made of hanging LED curtain strands, showing exactly the picture in REFERENCE IMAGE 2 - a cartoon Santa in a red suit with a white beard filling the upper wall on a deep blue field, big white snowflakes scattered around him, one green Christmas tree with coloured baubles in the bottom-left corner of the wall and another in the bottom-right corner, all built out of individual glowing bulbs acting as pixels. It is not a still picture. Three things move in it, continuously, from 2.2s to the very last frame:
- Santa's raised hand WAVES side to side, a steady friendly wave, about one wave per second. Only his arm moves; his body, face and beard stay exactly where they are.
- The white snowflakes DRIFT STEADILY DOWNWARD across the blue field, from the top of the wall toward the bottom, each one fading out as it reaches the lowest row of bulbs while a new one lights up near the top, so the number of snowflakes on the wall never alters.
- Both Christmas trees SWAY gently left and right from their bases like trees in a light breeze, and their coloured baubles blink on and off in a slow cycle.
The picture stays ANCHORED to the front wall. It does not rotate, does not spin, does not sweep across as one sheet, does not slide sideways, does not scroll and does not drift as a whole. Whatever the bulbs do on the left of the wall they do at the same instant and at the same speed on the right. The lights exist ONLY on the front wall of the house where the curtain hangs - the roof, the sides of the house, the porch ceiling and the ground carry no picture and stay as they are. The warm porch lantern and the warm lit windows stay on and read through the lights.

CAMERA - HELD IPHONE, LOCKED FRAMING. One single continuous handheld vertical shot from a phone held up at head height in the middle of the crowd, exactly the framing of REFERENCE IMAGE 1. NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO orbit, NO cuts, NO slow motion, NO speed ramp. The house, the porch and the crowd all stay exactly the same size in frame from the first frame to the last. Handheld micro-shake only.

POSITIVE LOCKS: real-time playback speed throughout, exactly as fast as this would happen on a real street. The crowd stays in the foreground with their backs to camera the whole clip. The house is dark until 2.2s and lit from 2.2s to the end.

HARD RULES: nobody turns round to face the camera. The family never turns back toward the camera once they have turned to the house. The wall never goes dark again. DO NOT CHANGE the house, the porch, the dusk sky, the snow or the crowd. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO WATERMARK anywhere in the video. No subtitles.

AUDIO: real lip-synced voices - the crowd and the family chanting "Three... two... ONE!" together, then a big genuine cheer, whooping, laughing and clapping. Cold outdoor night ambience, boots in snow, coats rustling. No narration. (no BGM)

LOOK: real iPhone UGC shot at dusk. Deep blue sky, warm porch light, the lit wall clipping slightly bright the way a phone sensor really does, tack sharp, fine natural sensor grain, no bokeh, no cinematic grade, no lens flare, no slow motion, no speed ramp. Nothing looks weightless, rubbery or animated.
````

#### Video prompt — `clips/v35_c01_g2.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `85f2ded8-8ad3-4865-86e1-d361f4182367`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_204141_85f2ded8-8ad3-4865-86e1-d361f4182367.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c01_g3.png` · Higgsfield media `29f6e4cb-8a99-4cd2-bf42-d63ef0931741`
- image ref 1: `content/video_35_assets/references/v35_c01_r2.png` · Higgsfield media `dc410a06-b67d-4b52-943a-a3df3b7b8b7c`

````text
Animate REFERENCE IMAGE 1 exactly as it is. The first frame of the video IS REFERENCE IMAGE 1, unchanged - same pale gable-front two-storey house, same covered porch with its white posts, same warm porch lantern and warm lit windows, same deep blue dusk sky, same family of four standing together on the porch facing the camera, same crowd of neighbours in winter coats and knitted hats packed across the foreground with their backs to the camera, same snow, same dark unlit front wall.

EVERYONE COUNTS DOWN TOGETHER, OUT LOUD. The crowd in the foreground and the family on the porch count in unison in real voices: "Three... two... ONE!" Warm, smiling, breath fogging in the cold.

EVERYBODY KEEPS THEIR FEET ON THE GROUND. Nobody jumps, nobody hops, nobody bounces on the spot, nobody springs up, nobody is lifted, nobody spins. This is a group of ordinary neighbours standing in the snow on a cold evening - they shift their weight, they lean, they turn their heads, and that is the whole extent of it.

ACTION TIMELINE (5 seconds, one continuous take, no cuts):
0.0-0.8s - "Three!" The crowd counts, standing where they are, heads up toward the house. Two or three phones are held up filming. The family on the porch count with them, still facing the camera.
0.8-1.5s - "Two!" A little louder. The family on the porch begin to turn.
1.5-2.2s - The family of four turn calmly right round on the spot to face the house, backs to the camera, shoulder to shoulder exactly like the crowd. It is an ordinary unhurried half-turn, the way anyone turns to look at something behind them: their feet step round, their shoulders lead, their heads follow, their arms stay down at their sides. They do not jump, do not hop, do not bounce, do not spin, do not throw their arms up and do not twirl. On the last of that turn everyone says "ONE!"
2.2-2.5s - The whole front wall of the house switches on at once.
2.5-5.0s - The picture on the wall runs. The reaction is quiet, delayed and real, and it happens at different moments for different people rather than all at once: heads tilt back to take in the whole wall, one man lifts a hand to point up at Santa, a woman near the front puts a hand over her mouth and laughs, someone turns to the person beside them and says something, a child on the porch leans in against a parent. THE MOTION ENDS HERE, with the picture still lit and still running and the crowd still standing there watching it on the last frame.

NOBODY APPLAUDS AND NOBODY CHEERS. No clapping, no hands together, no whooping, no crowd roar, no unison cheer, no arms punched into the air, no fists raised, no jumping for joy, no group hug, no confetti. The reaction is a handful of quiet individual reactions scattered across a few seconds, not one choreographed celebration.

THE PICTURE ON THE HOUSE IS THE MAIN SUBJECT FROM 2.2s ONWARD. The front wall of the house is a giant low-resolution screen made of hanging LED curtain strands, showing exactly the picture in REFERENCE IMAGE 2 - a cartoon Santa in a red suit with a white beard filling the upper wall on a deep blue field, big white snowflakes scattered around him, one green Christmas tree with coloured baubles in the bottom-left corner of the wall and another in the bottom-right corner, all built out of individual glowing bulbs acting as pixels. It is not a still picture. Three things move in it, continuously, from 2.2s to the very last frame:
- Santa's raised hand WAVES side to side, a steady friendly wave, about one wave per second. Only his arm moves; his body, face and beard stay exactly where they are.
- The white snowflakes DRIFT STEADILY DOWNWARD across the blue field, from the top of the wall toward the bottom, each one fading out as it reaches the lowest row of bulbs while a new one lights up near the top, so the number of snowflakes on the wall never alters.
- Both Christmas trees SWAY gently left and right from their bases like trees in a light breeze, and their coloured baubles blink on and off in a slow cycle.
The picture stays ANCHORED to the front wall. It does not rotate, does not spin, does not sweep across as one sheet, does not slide sideways, does not scroll and does not drift as a whole. Whatever the bulbs do on the left of the wall they do at the same instant and at the same speed on the right. The lights exist ONLY on the front wall of the house where the curtain hangs - the roof, the sides of the house, the porch ceiling and the ground carry no picture and stay as they are. The warm porch lantern and the warm lit windows stay on and read through the lights.

CAMERA - HELD IPHONE, LOCKED FRAMING. One single continuous handheld vertical shot from a phone held up at head height in the middle of the crowd, exactly the framing of REFERENCE IMAGE 1. NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO orbit, NO cuts, NO slow motion, NO speed ramp. The house, the porch and the crowd all stay exactly the same size in frame from the first frame to the last. Handheld micro-shake only.

POSITIVE LOCKS: real-time playback speed throughout, exactly as fast as this would happen on a real street. Everybody's feet stay on the ground for the whole clip. The crowd stays in the foreground with their backs to camera the whole clip. The house is dark until 2.2s and lit from 2.2s to the end.

HARD RULES: nobody turns round to face the camera. The family never turns back toward the camera once they have turned to the house. The wall never goes dark again. DO NOT CHANGE the house, the porch, the dusk sky, the snow or the crowd. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO WATERMARK anywhere in the video. No subtitles.

AUDIO: real lip-synced voices - the crowd and the family counting "Three... two... ONE!" together, then a scattering of genuine low reactions as the lights come on: quiet gasps, a soft "ohhh", one short laugh, a few murmured words between neighbours, overlapping and untidy and arriving at different moments rather than all together. NO APPLAUSE, NO CLAPPING, no whooping, no cheering, no crowd roar, no stadium noise, no canned audience track, no laugh track. Cold outdoor night ambience, boots shifting in snow, coats rustling. No narration. (no BGM)

LOOK: real iPhone UGC shot at dusk. Deep blue sky, warm porch light, the lit wall clipping slightly bright the way a phone sensor really does, tack sharp, fine natural sensor grain, no bokeh, no cinematic grade, no lens flare, no slow motion, no speed ramp. Nothing looks weightless, rubbery or animated.
````

### C02 — Scanning it at the till

**In the cut:** `starting_frames/v35_c02_g1.png` → `clips/v35_c02_g2.mp4`

#### Image prompt — `starting_frames/v35_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `5d7f2b94-6446-4bcf-a35e-a427bc4707e4`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175638_5d7f2b94-6446-4bcf-a35e-a427bc4707e4.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_19_assets/starting_frames/v19_c02_g2.png` · Higgsfield media `0c78d477-e3dd-4cec-bf67-8148d996d891`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `3ca7d301-ed13-43cf-ab78-9900942bc250`

````text
Use REFERENCE IMAGE 1 as the EXACT framing reference — match its camera position, camera height, angle, focal length and composition precisely. A first-person POV phone shot at a store self-checkout: two hands in cream ribbed-knit jumper sleeves hold a large flat rectangular product box up flat to the camera just above the scanner plate, the printed front face square to the lens, wrists angled slightly outward under the weight, forearms cropped at the bottom edge of frame, no body and no face. A metal shopping trolley at the left edge, the glowing self-checkout terminal and card reader at the right.

CHANGE THE BACKGROUND to a DIFFERENT store, still heavily decorated for Christmas: a smart upmarket department store at Christmas — a polished pale wood floor, warm brass and glass fittings, a tall arch of fresh green garland studded with warm white lights spanning over the checkout lane, a floor-to-ceiling display wall of red and gold glass ornaments glinting behind it, a pair of decorated flocked Christmas trees further back, soft warm downlights, blurred well-dressed shoppers carrying paper bags deeper in the hall.

THE BOX must match REFERENCE IMAGE 2 exactly — this is our real product packshot. A matte black rigid retail box, large and flat, roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands. Front panel from top to bottom: a large white condensed uppercase headline reading LED CURTAIN LIGHTS; a warm gold subline reading Create Your Own Magic; a red diagonal BEST SELLER ribbon flag across the top-right corner; one large photographic panel with a thin gold hairline border filling the middle and lower two thirds, showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door and warm fairy-lit trees either side; and a bottom row of five small gold line icons with white captions.

THE BOX IS CLOSED AND SEALED — CRITICAL. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap. The front is fully printed, opaque, closed cardboard.

SCALE: the box is big. The left hand grips the far left edge near the lower corner and the right hand the far right edge near the lower corner, thumbs flat on the printed front face, fingers wrapped around the sides toward the back. The hands must read SMALL relative to the box — each hand spans less than a quarter of the box width.

No text overlays, no captions, no watermarks, no readable brand names or logos on the store fittings, no writing anywhere in the photograph except the printing on the box itself.

Hyper-realistic photograph shot on an iPhone 15 Pro, razor-sharp focus on the box and the hands, absolutely no motion blur and no blurry areas, clean low-noise exposure, natural true-to-life colour, vertical 9:16.
````

#### Video prompt — `clips/v35_c02_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `4ec82d6e-218b-4f25-97f0-ba2d3e8e5e6e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_192831_4ec82d6e-218b-4f25-97f0-ba2d3e8e5e6e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c02_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c02_g1.png` · Higgsfield media `5dd97495-2768-448e-af3c-86778784adfc`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `3ca7d301-ed13-43cf-ab78-9900942bc250`

````text
Vertical first-person point-of-view phone video inside a department store. The first frame of the video IS the start image, unchanged. The two hands holding the LED curtain lights box lower it and slide it face-down across the self-checkout scanner; the box tilts as the barcode passes over the glass and the screen flashes. The hands then lift the box, turn it away from the camera and lower it into the SAME shopping cart that is already standing at the lower-left edge of the first frame — the chrome wire-mesh basket with the red plastic handle bar along its top rail. The hands keep hold of the box the whole way down and set it into the basket under control, letting go only once it is resting; it leans against the wire and settles with real weight. The point of view follows the box down into the cart with a natural downward head tilt. Warm ceiling-light glare slides across the glossy printed cardboard as it moves. Shoppers and aisles stay blurred in the background. Handheld micro-shake, real phone-camera look, no zoom, no slow motion, no cinematic bokeh.

THE BOX IS CLOSED AND SEALED — CRITICAL, and it matches the SECOND reference image exactly. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap. The front is fully printed, opaque, closed cardboard: a large white condensed uppercase headline reading LED CURTAIN LIGHTS, a warm gold subline reading Create Your Own Magic, a red diagonal BEST SELLER ribbon flag across the top-right corner, one large photographic panel with a thin gold hairline border showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door, and a bottom row of five small gold line icons. Every letter stays rigid, sharp and correctly spelled — the print never warps, morphs or re-renders as the box moves. The box is BIG — roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands; each hand spans less than a quarter of the box width, and it keeps that size for the whole clip.

THE CART IS THE ONE ALREADY IN FRAME — CRITICAL. There is exactly one shopping cart in the video and it is the one visible at the lower left of the first frame: an open chrome wire-mesh basket on a bare steel tube frame, with a red plastic bar along the top rail. It stays where it is and does not slide, roll, grow, shrink, swap, duplicate or re-render. NO second cart, NO cart sliding or popping into frame, NO cart appearing out of nowhere underneath the box. The basket is REAL OPEN WIRE seen in three dimensions: the individual chrome rods keep their spacing and thickness, the gaps between them show the pale wood floor and the cart's own shadow underneath, and the far wall of the basket sits visibly behind the near wall. It is NOT a flat printed grid, NOT a solid-sided tub, NOT a plastic crate, and the mesh never warps, ripples, melts or changes pattern. The box is physically smaller than the basket opening and clearly fits inside it. The box never floats, hovers, hangs in mid-air, passes through the wire or drops from a height.

DO NOT CHANGE: the cream ribbed-knit jumper sleeves, the store, the polished pale wood floor, the brass and glass fittings, the tall arch of green garland studded with warm white lights spanning over the checkout lane, the display wall of red and gold glass ornaments behind it, the decorated flocked trees further back, the soft warm downlights, the exposure and white balance of the reference frame.

AUDIO: natural room sound only — no music, no score, no background song. Store ambience, the scanner beep, cardboard sliding on the scale platform, the box landing in the metal cart, distant trolleys and chatter. No voice.

LOOK: real phone-camera footage, soft warm store lighting, mild sensor noise, no cinematic bokeh, no colour grade, no lens flare, no text overlays, no captions, no watermark, no slow motion.
````

**Other takes of C02 on disk (1)**

#### Video prompt — `clips/v35_c02_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `cfa18803-d890-4f1c-8e2d-f4717d717f84`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_185045_cfa18803-d890-4f1c-8e2d-f4717d717f84.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c02_g1.png` · Higgsfield media `5dd97495-2768-448e-af3c-86778784adfc`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `3ca7d301-ed13-43cf-ab78-9900942bc250`

````text
Vertical first-person point-of-view phone video inside a department store. The first frame of the video IS the start image, unchanged. The two hands holding the LED curtain lights box lower it and slide it face-down across the self-checkout scanner; the box tilts as the barcode passes over the glass and the screen flashes. The hands then lift the box, turn it away from the camera and drop it into the metal shopping cart on the left, the box landing flat with a small bounce and settle. The point of view follows the box down into the cart with a natural downward head tilt. Warm ceiling-light glare slides across the glossy printed cardboard as it moves. Shoppers and aisles stay blurred in the background. Handheld micro-shake, real phone-camera look, no zoom, no slow motion, no cinematic bokeh.

THE BOX IS CLOSED AND SEALED — CRITICAL, and it matches the SECOND reference image exactly. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap. The front is fully printed, opaque, closed cardboard: a large white condensed uppercase headline reading LED CURTAIN LIGHTS, a warm gold subline reading Create Your Own Magic, a red diagonal BEST SELLER ribbon flag across the top-right corner, one large photographic panel with a thin gold hairline border showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door, and a bottom row of five small gold line icons. Every letter stays rigid, sharp and correctly spelled — the print never warps, morphs or re-renders as the box moves. The box is BIG — roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands; each hand spans less than a quarter of the box width, and it keeps that size for the whole clip.

DO NOT CHANGE: the cream ribbed-knit jumper sleeves, the store, the polished pale wood floor, the brass and glass fittings, the tall arch of green garland studded with warm white lights spanning over the checkout lane, the display wall of red and gold glass ornaments behind it, the decorated flocked trees further back, the soft warm downlights, the exposure and white balance of the reference frame.

AUDIO: natural room sound only — no music, no score, no background song. Store ambience, the scanner beep, cardboard sliding on the scale platform, the box landing in the metal cart, distant trolleys and chatter. No voice.

LOOK: real phone-camera footage, soft warm store lighting, mild sensor noise, no cinematic bokeh, no colour grade, no lens flare, no text overlays, no captions, no watermark, no slow motion.
````

### C03 — Opened it on the couch

**In the cut:** `starting_frames/v35_c03_g1.png` → `clips/v35_c03_g1.mp4`

#### Image prompt — `starting_frames/v35_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `f53983c6-ebab-4542-bd7d-901184f78984`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175638_f53983c6-ebab-4542-bd7d-901184f78984.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_19_assets/starting_frames/v19_c03_g2.png` · Higgsfield media `7329e69e-a7d9-495f-bdb3-750b9908752e`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `3ca7d301-ed13-43cf-ab78-9900942bc250`

````text
Use REFERENCE IMAGE 1 ONLY as a guide to the POV STYLE, camera height and lens — a first-person phone shot looking down at the sitter's own lap, the box held flat and square to the camera. Do NOT copy its bed, its bedding or its bedroom.

THE SCENE — a person sitting back on a SOFA in a living room at night, shot from their own eyeline looking down: their own thighs and knees in soft charcoal-grey lounge trousers run away from the camera across the seat cushions, feet in thick cream knit socks resting on a low wooden coffee table at the far end of the frame, and the large flat rectangular product box lies flat ACROSS THEIR LAP, resting on the tops of the thighs, its printed front face square to the camera and fully visible. A cream chunky-knit throw is rumpled over the arm of the sofa beside them. No body above the waist, no hands, no face.

THE ROOM — a warm living room on a winter evening: a deep charcoal fabric sofa, a tall decorated Christmas tree with warm white lights and red and gold baubles standing to the right beyond the coffee table, a brick fireplace behind it with three red stockings hung along the mantel and a garland of greenery draped across it, a table lamp with a cream shade glowing warmly on the left, a rug over pale oak floorboards, warm low light throughout.

THE BOX must match REFERENCE IMAGE 2 exactly — this is our real product packshot. A matte black rigid retail box, large and flat, roughly 55 cm wide by 42 cm tall by 10 cm deep. Front panel from top to bottom: a large white condensed uppercase headline reading LED CURTAIN LIGHTS; a warm gold subline reading Create Your Own Magic; a red diagonal BEST SELLER ribbon flag across the top-right corner; one large photographic panel with a thin gold hairline border filling the middle and lower two thirds, showing a night photo of a suburban house facade with a glowing pixel LED Christmas tree on the garage door and warm fairy-lit trees either side; and a bottom row of five small gold line icons with white captions.

THE BOX IS CLOSED AND SEALED — CRITICAL. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, NO glowing lights showing through, no lid gap, the lid is not lifted and not removed. The front is fully printed, opaque, closed cardboard.

ANATOMY — CRITICAL. The legs are relaxed, straight and natural, both knees pointing the same way straight away from the camera, symmetrical, seen from directly above in a normal seated position. NO twisted torso, NO rotated hips, NO bent or impossible joints, NO third leg, correct human proportions throughout.

SCALE: the box is big — it spans the full width of the lap and overhangs the thighs on both sides.

No text overlays, no captions, no watermarks, no writing anywhere in the photograph except the printing on the box itself.

Hyper-realistic photograph shot on an iPhone 15 Pro, razor-sharp focus on the box, absolutely no motion blur and no blurry areas, clean low-noise exposure, warm natural true-to-life colour, vertical 9:16.
````

#### Video prompt — `clips/v35_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `779198ed-555b-4b8f-89aa-2e7c8a8e6bc4`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_185044_779198ed-555b-4b8f-89aa-2e7c8a8e6bc4.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c03_g1.png` · Higgsfield media `9f0028fb-d3cc-4785-a87a-a622fa5352fd`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `3ca7d301-ed13-43cf-ab78-9900942bc250`
- image ref 2: `product_images/box_nowindow/box_interior_g5.png` · Higgsfield media `f01fecfe-9cbe-44a5-a617-63193a1108b0`

````text
Animate the START IMAGE exactly as it is. The first frame of the video IS the start image, unchanged. The FIRST reference image is the product packshot - it is there ONLY to define exactly what the printed lid artwork looks like and how BIG the box is. The SECOND reference image is the open box interior - it is there ONLY to define exactly what is inside the box once the lid opens.

CAMERA - HELD IPHONE, FIRST-PERSON POV, LOCKED FRAMING: a genuine point-of-view shot, she is holding her own phone and looking down her own body as she sits back on the sofa. NO cuts, NO zoom in, NO zoom out, NO push-in, NO pull-back, NO pan, NO tilt, NO dolly, NO crop, NO reframe. Only natural handheld micro-drift and the faint breathing rise and fall of her own chest behind the camera. One single continuous unbroken take, no cut, no jump, no reset.

START FRAME: first-person view looking down her own legs on a sofa. She wears soft charcoal-grey lounge trousers and thick cream knit socks, her feet resting on a low wooden coffee table at the far end of the frame. A large matte-black rigid magnetic LED CURTAIN LIGHTS box lies flat ACROSS HER LAP, resting on the tops of her thighs, with its printed front face toward the camera, the lid fully CLOSED, hinged along the FAR edge. No hands are in frame yet. Warm out-of-focus living room light behind — the tall decorated Christmas tree standing to the right beyond the coffee table, the brick fireplace with three red stockings along the mantel and a garland of greenery across it, the cream-shaded table lamp glowing on the left.

ACTION TIMELINE - THE HANDS COME IN AND THE LID OPENS FROM THE FRONT:
0.0-0.7s - both of her own hands rise into frame from the bottom edge and reach onto the box, fingertips hooking under the NEAR FRONT EDGE of the closed lid, knuckles flexing with visible pressure, and the magnets release with a small firm snap.
0.7-2.2s - THE FRONT EDGE OF THE LID LIFTS FIRST and the lid pivots up and back on its hinge at the far edge in one smooth controlled motion, the printed top face rotating up and away from the camera as the gap widens along the front, opening to roughly seventy degrees and staying there, still attached, never detached, never lifted off, never carried out of frame. Her wrists rotate naturally with it. The box rocks very slightly on her lap and her thighs shift a little under the weight, then settle.
2.2-4.0s - the open interior is revealed and held, exactly as the SECOND reference image: a fitted matte-black cardboard tray holding the LED curtain light set itself - thin BLACK wire strings with small round bulbs coiled and folded into neat flat coils side by side, completely UNLIT - and beside the coils a small printed instruction booklet and a slim white plastic remote control seated in their own cut-outs, all against a matte black interior. The contents settle very slightly as the light reaches them. One hand releases the lid and lowers a little; the other steadies the base. The box stays resting on her lap and never floats or slides off.

HARD RULES: the lights stay completely OFF and dark for the whole clip - no glow, no sparkle, no light coming out of the box, no illumination on her hands or her legs. Nothing is ever lifted out of the box. The lid is never detached and never falls off. No extra objects appear. Exactly two hands are ever in frame, each with exactly five fingers at all times. Her face is never visible - this is her own point of view.

PRODUCT - LOCKED TO THE FIRST REFERENCE IMAGE: the lid is matte black and carries, exactly as in the packshot, the bold white condensed headline LED CURTAIN LIGHTS, the warm-gold subtitle Create Your Own Magic, a red diagonal BEST SELLER corner flag, a night photo panel of a house facade with a glowing LED Christmas tree on the garage, and gold feature icons along the bottom. It is NOT a plain box, NOT a different product, NOT a generic package. There is NO transparent window, NO clear plastic panel and NO die-cut cutout anywhere on the printed face. Every letter stays rigid, sharp and correctly spelled - the print never warps, morphs or re-renders as the lid rotates.

SIZE - THE BOX IS BIG: roughly 55 cm wide by 42 cm tall by 10 cm deep, much wider than the span of two outstretched hands. Each of her hands spans less than a quarter of the box width, and the box spans the full width of her lap and overhangs her thighs on each side. It keeps that size for the whole clip and never shrinks into a small gift box.

DO NOT CHANGE: the soft charcoal-grey lounge trousers, the cream knit socks, her legs, the deep charcoal fabric sofa, the low wooden coffee table, the cream chunky-knit throw rumpled over the arm of the sofa, the tall decorated Christmas tree on the right, the brick fireplace with its three red stockings and its greenery garland, the cream-shaded table lamp on the left, the rug over the pale oak floorboards, the exposure and white balance of the reference frame.

AUDIO - NO VOICE: the soft magnetic pop of the lid releasing, cardboard flexing, a faint rustle as the wire strings settle, the sofa cushions shifting, quiet room tone. NO music, NO narration, NO voice-over, nobody speaks in this shot.

LOOK: real phone-camera footage, natural warm indoor light, mild sensor noise, no cinematic bokeh, no colour grade, no lens flare, no text overlays, no captions, no watermark, no slow motion.
````

### C04 — Up the ladder, wide

**In the cut:** `starting_frames/v35_c04_g2.png` → `clips/v35_c04_g3.mp4`

#### Image prompt — `starting_frames/v35_c04_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `01242684-615e-4bfe-be76-aaf56437f91e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_181451_01242684-615e-4bfe-be76-aaf56437f91e.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c04_g1.png` · Higgsfield media `8f80a2c0-3b8f-4490-a42d-ad17a9c43817`
- @Image 2: `content/video_34_assets/starting_frames/v34_c04_g1.png` · Higgsfield media `ed1f7ffa-7285-4ced-ab37-92797ded7ff5`

````text
Use REFERENCE IMAGE 1 as the EXACT framing and composition reference — match its camera position, camera height, distance, angle, focal length and the placement of every element in the frame. Change ONLY the house and its surroundings.

A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

FRAMING — copied from REFERENCE IMAGE 1. The camera stands out on the snowy front lawn, level, far enough back that the whole front of a two-storey house fills the frame with sky above it. An aluminium extension ladder leans against the house at the upper left, and a man in a dark winter jacket, tan work trousers and boots stands high on it with one arm reaching up to the roofline, fixing the top of the light curtain under the eaves. He is seen from behind and slightly below; no face detail.

WHERE THE CURTAIN HANGS — THE MOST IMPORTANT INSTRUCTION. Copy the curtain placement EXACTLY from REFERENCE IMAGE 2. The curtain is ENORMOUS and covers the ENTIRE FRONT FACADE OF THE HOUSE, BOTH STOREYS AT ONCE. Its top edge is pinned under the eaves at the roofline where the man is working, and it hangs in one continuous unbroken sheet ALL THE WAY DOWN past the upstairs windows, past the band of wall between the floors, past the downstairs windows, and finishes just above the snow-laden shrubs at the foundation. It spans the full width of the main facade from the left corner of the house across to the porch. The upstairs AND the downstairs windows are BOTH behind the curtain and glow warmly through it. This is a full-house, floor-to-roof display. It is NOT a small rectangle on the upper storey only, NOT a single bay, NOT one panel floating high on the wall with bare wall below it, and it does NOT stop partway down.

THE HOUSE — a DIFFERENT house from both references. A two-storey HONEY-TONED CEDAR SHINGLE house — warm golden-brown weathered wood shingles laid in neat overlapping rows across the whole facade, crisp white window trim, dark green shutters flanking the windows, a covered front porch at the RIGHT with slim white posts and a DARK GREEN front door with a red-bow wreath, a warm brass lantern beside the door, thick green garland spiralled up each porch post. Warm lit windows behind the curtain on both floors. Snow-laden rounded boxwood shrubs along the foundation and a small snowy fir at the right. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey. Take NOTHING of the house itself from REFERENCE IMAGE 2 — use that image ONLY to see where the light curtain hangs.

HOW THE CURTAIN IS BUILT — a huge dense curtain of warm white string lights, built from many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles and the white window mullions read clearly through the gaps between strands, and the lit windows behind glow through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. The bottom hem is uneven and wavy where the strands end at slightly different heights. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
````

#### Video prompt — `clips/v35_c04_g3.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `79af1fd7-736e-446b-bc1b-c8cb817a7412`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_193629_79af1fd7-736e-446b-bc1b-c8cb817a7412.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c04_g3.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c04_g2.png` · Higgsfield media `e96d3a3b-0a7e-4dab-b77b-04d87d93a685`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house with crisp white trim and a dark green front door, same aluminium extension ladder at the upper left, same dense LED curtain hanging over the front bay of the upper storey but with the curtain SWITCHED OFF — unlit, dark bulbs on black wire, not glowing, same blue-hour navy sky, same snow. Nothing changes.

ACTION: he is installing the LED curtain. He reaches up with both hands, presses the top rail of the curtain flat against the wall and works it onto its clips, fingers adjusting the top edge. Then he takes the curtain lightly in one hand and gives it THREE SMALL, GENTLE SHAKES from the wrist — the unhurried, careful movement of someone settling the strands straight, not yanking them. The net sways softly and the strands swing a few centimetres and settle back under their own weight, one or two untangling and dropping to a straight hang. He stays balanced and relaxed on the ladder rung. Cold breath visible.
0.0-0.7s — both hands press the top rail flat against the cedar shingles just under the eaves, thumbs pushing a clip closed.
0.7-1.7s — FIRST GENTLE SHAKE: he takes hold of the curtain near the top and gives it one soft, small shake from the wrist; the strands sway a few centimetres to one side and settle back, a slow ripple travelling down the net.
1.7-2.7s — SECOND GENTLE SHAKE, exactly as soft as the first; the strands sway again by the same small amount, a couple of tangled strands slip free and settle at a new length. The ladder does not move.
2.7-4.0s — THIRD GENTLE SHAKE, then he lets go and steadies the top rail with one hand; the strands ripple softly, slow and settle straight. His breath fogs.

The LED strands are SWITCHED OFF for the whole clip — dark, unlit bulbs on black wire, no glow, no warm white light, no colour, no twinkle, no pattern, no light spilling onto the cedar shingles or the snow from the curtain. They never light up at any moment; they only move because the curtain is being shaken. The only light on the house is the warm glow from the windows, the porch lantern and the small lights on the door wreath and the porch garland, exactly as in the first frame. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — FIRST-PERSON POV, WALKING FORWARD. The person filming takes A FEW SLOW STEPS FORWARD across the snowy front lawn toward the man on the ladder, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house and the ladder grow steadily and continuously larger and NEVER recede. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the snow-laden boxwood shrubs and the small snowy fir trees at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect. No cuts.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy lawn ahead.

THE SHAKES ARE GENTLE — CRITICAL. This is a calm, patient man tidying the strands straight, and the whole clip is unhurried. All three shakes are the SAME small size and the SAME slow speed — they never escalate. No hard yank, no tug, no jerk, no wrenching, no whipping, no rattling, no violent or angry motion, no frustration, no fast or snappy movement, no shaking with both arms, no wide swinging of the net, no strands flying out sideways, no jolt through the ladder. His shoulders and body stay still and easy; only the forearm and wrist move.

HARD RULES: the LED curtain never illuminates — not at the start, not on a shake, not at the end. No other people, no cars, no pets enter frame. The man is seen from behind and slightly below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, boots crunching on packed snow with each stride, a plastic clip snapping shut, the faint soft rustle of the light strands, breath. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, slight motion blur on the walk, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
````

**Other takes of C04 on disk (3)**

#### Image prompt — `starting_frames/v35_c04_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `dd9d90f9-79e5-4792-bda0-209f97b65890`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175637_dd9d90f9-79e5-4792-bda0-209f97b65890.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c04_g1.png` · Higgsfield media `8f80a2c0-3b8f-4490-a42d-ad17a9c43817`

````text
Use REFERENCE IMAGE 1 as the EXACT framing and composition reference — match its camera position, camera height, distance, angle, focal length and the placement of every element in the frame. Change ONLY the house and its surroundings.

A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

FRAMING — copied from REFERENCE IMAGE 1. The camera stands out on the snowy front lawn, level, far enough back that the whole front of a two-storey house fills the frame with sky above it. An aluminium extension ladder leans against the house at the upper left, and a man in a dark winter jacket, tan work trousers and boots stands high on it with one arm reaching up to the roofline, fixing the top of the light curtain under the eaves. He is seen from behind and slightly below; no face detail.

THE HOUSE — a DIFFERENT house from the reference. A two-storey HONEY-TONED CEDAR SHINGLE house — warm golden-brown weathered wood shingles laid in neat overlapping rows across the whole facade, crisp white window trim, a covered front porch with slim white posts and a DARK GREEN front door with a red-bow wreath, a warm black lantern beside the door, thick green garland spiralled up each porch post. Warm lit windows on the ground floor. Snow-laden shrubs along the foundation and two small snowy fir trees at the right edge. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey-green.

THE LIGHT CURTAIN — a huge dense curtain of warm white string lights hangs flat over the whole front bay of the upper storey, spanning almost the full width of that wall, its top edge tucked just under the eaves where the man is working, its bottom hem uneven and wavy where the strands end at slightly different heights. It is built from many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles and the white window mullions read clearly through the gaps between strands, and the lit windows behind glow through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
````

#### Video prompt — `clips/v35_c04_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `d1fd7102-2050-4897-a6ef-d06fd5a746c5`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_185044_d1fd7102-2050-4897-a6ef-d06fd5a746c5.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c04_g2.png` · Higgsfield media `e96d3a3b-0a7e-4dab-b77b-04d87d93a685`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house with crisp white trim and a dark green front door, same aluminium extension ladder at the upper left, same dense warm-white LED curtain hanging over the front bay of the upper storey, same blue-hour navy sky, same snow. Nothing changes.

ACTION: he is installing the LED curtain. He reaches up with both hands, presses the top rail of the curtain flat against the wall and works it onto its clips, fingers adjusting the top edge. Then he grips the curtain and gives it THREE small shakes — the whole net of hanging LED strands sways and ripples, individual strands swinging out and settling back with real weight and momentum, a few strands untangling as they drop. He shifts his weight on the ladder rung and the ladder flexes a fraction. Cold breath visible.
0.0-0.7s — both hands press the top rail flat against the cedar shingles just under the eaves, thumbs pushing a clip closed.
0.7-1.7s — FIRST SHAKE: he takes hold of the curtain and gives it one firm shake; the whole net swings out to one side and ripples back, strands swaying across the full width.
1.7-2.7s — SECOND SHAKE, a little harder; the strands swing out again, a couple of tangled strands fall free and settle at a new length, the ladder flexes a fraction.
2.7-4.0s — THIRD SHAKE, then he lets go and steadies the top rail with one hand; the strands ripple, slow and settle. His breath fogs.

The LED strands keep exactly the same brightness, colour and state they have in the first frame — they do not turn on, off, or change pattern; they only move because the curtain is being shaken. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — FIRST-PERSON POV, WALKING FORWARD. The person filming takes A FEW SLOW STEPS FORWARD across the snowy front lawn toward the man on the ladder, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house and the ladder grow steadily and continuously larger and NEVER recede. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the snow-laden boxwood shrubs and the small snowy fir trees at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect. No cuts.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy lawn ahead.

HARD RULES: no other people, no cars, no pets enter frame. The man is seen from behind and slightly below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, boots crunching on packed snow with each stride, the aluminium ladder ticking and flexing, a plastic clip snapping shut, the faint rattle of the light strands, breath. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, slight motion blur on the walk, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
````

#### Video prompt — `clips/v35_c04_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `86a77228-96c9-4fd3-b865-1528d15aee20`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_192803_86a77228-96c9-4fd3-b865-1528d15aee20.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c04_g2.png` · Higgsfield media `e96d3a3b-0a7e-4dab-b77b-04d87d93a685`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house with crisp white trim and a dark green front door, same aluminium extension ladder at the upper left, same dense LED curtain hanging over the front bay of the upper storey but with the curtain SWITCHED OFF — unlit, dark bulbs on black wire, not glowing, same blue-hour navy sky, same snow. Nothing changes.

ACTION: he is installing the LED curtain. He reaches up with both hands, presses the top rail of the curtain flat against the wall and works it onto its clips, fingers adjusting the top edge. Then he grips the curtain and gives it THREE small shakes — the whole net of hanging LED strands sways and ripples, individual strands swinging out and settling back with real weight and momentum, a few strands untangling as they drop. He shifts his weight on the ladder rung and the ladder flexes a fraction. Cold breath visible.
0.0-0.7s — both hands press the top rail flat against the cedar shingles just under the eaves, thumbs pushing a clip closed.
0.7-1.7s — FIRST SHAKE: he takes hold of the curtain and gives it one firm shake; the whole net swings out to one side and ripples back, strands swaying across the full width.
1.7-2.7s — SECOND SHAKE, a little harder; the strands swing out again, a couple of tangled strands fall free and settle at a new length, the ladder flexes a fraction.
2.7-4.0s — THIRD SHAKE, then he lets go and steadies the top rail with one hand; the strands ripple, slow and settle. His breath fogs.

The LED strands are SWITCHED OFF for the whole clip — dark, unlit bulbs on black wire, no glow, no warm white light, no colour, no twinkle, no pattern, no light spilling onto the cedar shingles or the snow from the curtain. They never light up at any moment; they only move because the curtain is being shaken. The only light on the house is the warm glow from the windows, the porch lantern and the small lights on the door wreath and the porch garland, exactly as in the first frame. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — FIRST-PERSON POV, WALKING FORWARD. The person filming takes A FEW SLOW STEPS FORWARD across the snowy front lawn toward the man on the ladder, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house and the ladder grow steadily and continuously larger and NEVER recede. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the snow-laden boxwood shrubs and the small snowy fir trees at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect. No cuts.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy lawn ahead.

HARD RULES: the LED curtain never illuminates — not at the start, not on a shake, not at the end. No other people, no cars, no pets enter frame. The man is seen from behind and slightly below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, boots crunching on packed snow with each stride, the aluminium ladder ticking and flexing, a plastic clip snapping shut, the faint rattle of the light strands, breath. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, slight motion blur on the walk, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
````

### C05 — Same install, closer and lower

**In the cut:** `starting_frames/v35_c05_g2.png` → `clips/v35_c05_g1.mp4`

#### Image prompt — `starting_frames/v35_c05_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `55a6a06f-4df9-49bc-b3c6-182c94af8510`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_181613_55a6a06f-4df9-49bc-b3c6-182c94af8510.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c05_g1.png` · Higgsfield media `75cc4e34-3210-4f0f-9579-ad5a627135c6`
- @Image 2: `content/video_35_assets/starting_frames/v35_c04_g2.png` · Higgsfield media `01242684-615e-4bfe-be76-aaf56437f91e`

````text
A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

CAMERA AND FRAMING — copy this EXACTLY from REFERENCE IMAGE 1. This is the SAME house and the SAME moment as REFERENCE IMAGE 2, just seen from much closer and lower: the camera has moved in toward the house and around to the LEFT, standing low on the snow and looking up and along the front facade at an angle, so the wall runs away from the camera in perspective rather than sitting square-on. The aluminium extension ladder dominates the LEFT side of the frame, running steeply up out of the top-left corner, and the man in the dark winter jacket, tan work trousers and boots is higher on it now, up near the roofline with one arm reaching to the eaves, seen from behind and below with no face detail. Snow-laden rounded boxwood shrubs fill the bottom foreground of the frame.

THE HOUSE — IDENTICAL to REFERENCE IMAGE 2 in every detail, just closer. The SAME two-storey HONEY-TONED CEDAR SHINGLE house: warm golden-brown weathered wood shingles laid in neat overlapping rows across the whole facade, crisp white window trim, DARK GREEN SHUTTERS flanking every window, tall white-framed multi-pane sash windows, the covered front porch at the RIGHT with slim white posts and thick green garland spiralled up them, the DARK GREEN front door with its red-bow wreath, the warm brass lantern beside the door, a small snowy fir beside the porch steps and a row of snow-laden rounded boxwood balls along the foundation. Same shingle colour, same white trim, same green shutters, same porch, same green door. Do NOT invent a different house, a different colour or a different style. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey.

WHERE THE CURTAIN HANGS — IDENTICAL to REFERENCE IMAGE 2. The curtain is ENORMOUS and covers the ENTIRE FRONT FACADE, BOTH STOREYS AT ONCE, in one continuous unbroken sheet: its top edge pinned under the eaves at the roofline where the man is working, hanging all the way down past the upstairs windows, past the band of wall between the floors, past the downstairs windows, finishing just above the snow-laden boxwood shrubs at the foundation. The upstairs AND downstairs windows are BOTH behind the curtain and glow warmly through it. It does NOT stop partway down, it is NOT a rectangle on the upper storey only, and it is NOT two separate panels.

HOW THE CURTAIN IS BUILT — the SAME dense curtain of warm white string lights as in REFERENCE IMAGE 2, now seen much closer and at an angle so the individual strands and bulbs are clearly resolved. Many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles, the green shutters and the white window mullions read clearly through the gaps between strands, and the lit rooms behind glow through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. The bottom hem is uneven and wavy. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
````

#### Video prompt — `clips/v35_c05_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `e2f1c20f-e0be-4788-ba00-c76e67f71133`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_185044_e2f1c20f-e0be-4788-ba00-c76e67f71133.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c05_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c05_g2.png` · Higgsfield media `ceda1595-8fb0-4189-b3fd-5bb94113a9c1`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same man, same honey-toned cedar shingle two-storey house, same aluminium extension ladder dominating the left of frame, same dense warm-white LED curtain, same close low angle looking up and along the facade, same snow-laden shrubs in the bottom foreground, same blue-hour navy sky. Nothing changes.

ACTION: he continues installing the LED curtain from this angle. He raises both hands to the top rail, presses it against the wall and hooks it into place, thumbs pushing a clip closed. Then he takes hold of the curtain and gives it ONE firm shake — the full net of LED strands swings out and ripples, strands swaying out and settling back with real weight and momentum, a couple of tangled strands falling free. He adjusts his footing on the ladder rung and leans in slightly. Cold breath visible.
0.0-1.0s — both hands rise to the top rail, press it flat against the cedar shingles under the eaves and push a clip closed.
1.0-1.6s — he slides one hand down, grips the curtain and gives it ONE firm shake; the whole net swings out to one side.
1.6-2.8s — the strands ripple back across the full width with real weight, a couple of tangled strands drop free and settle at a new length; the ladder flexes a fraction.
2.8-4.0s — he adjusts his footing on the rung, leans in slightly and steadies the top rail with one hand; the strands slow and settle. His breath fogs.

The LED strands keep exactly the same brightness, colour and state they have in the first frame — they do not turn on, off, or change pattern; they only move because the curtain is being shaken. The wire stays BLACK: not white, not clear, not silver. The curtain stays SEE-THROUGH — the cedar shingles and the white window mullions read through the gaps between strands the whole time, and the lit Christmas tree behind the upstairs window keeps glowing through it. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH, portrait, exactly the framing of the start image, feet planted. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO CUT. The house stays the same size in frame throughout. The ONLY permitted camera move is a small gentle TILT UP across the clip, a few degrees, as if the person filming lifts their phone slightly to follow his hands up toward the eaves — a tilt only, never a rise, never a zoom, never a step forward.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snow-laden shrubs.

HARD RULES: no other people, no cars, no pets enter frame. The man is seen from behind and below and never turns his face to camera. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the video, and no captions, subtitles or watermark.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban evening ambience, the aluminium ladder ticking and flexing, boots shifting on a rung, a plastic clip snapping shut, the faint rattle of the light strands, breath, light wind. No voice.

LOOK: real amateur phone video, same blue-hour lighting and colours as the first frame, grain in the dark areas, no colour grade, no bokeh, no cinematic look, no slow motion, no speed ramp.
````

**Other takes of C05 on disk (1)**

#### Image prompt — `starting_frames/v35_c05_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `940c5e2d-4958-4ea5-adad-121f9eacdd5a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_180044_940c5e2d-4958-4ea5-adad-121f9eacdd5a.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c05_g1.png` · Higgsfield media `75cc4e34-3210-4f0f-9579-ad5a627135c6`
- @Image 2: `content/video_35_assets/starting_frames/v35_c04_g1.png` · Higgsfield media `dd9d90f9-79e5-4792-bda0-209f97b65890`

````text
A real photograph, vertical 9:16, shot outdoors at BLUE HOUR on a winter evening — a deep navy sky, the last cold light on the snow.

CAMERA AND FRAMING — copy this EXACTLY from REFERENCE IMAGE 1. This is the same house and the same moment as REFERENCE IMAGE 2, just seen from much closer and lower: the camera has moved in toward the house and around to the LEFT, standing low on the snow and looking up and along the front facade at an angle, so the wall runs away from the camera in perspective rather than sitting square-on. The aluminium extension ladder dominates the LEFT side of the frame, running steeply up out of the top-left corner, and the man in the dark winter jacket, tan work trousers and boots is higher on it now, up near the roofline with one arm reaching to the eaves, seen from behind and below with no face detail. Snow-laden evergreen shrubs fill the bottom foreground of the frame.

THE HOUSE — IDENTICAL to REFERENCE IMAGE 2 in every detail. The SAME two-storey HONEY-TONED CEDAR SHAKE SHINGLE house: warm tan-brown weathered wood shingles covering the whole facade, crisp white trim and white eaves, tall white-framed multi-pane sash windows with white shutters, the white columned front portico at the right with deep green garland spiralled up the column, the DARK GREEN front door with its red-bow wreath, the warm brass lantern hanging in the porch ceiling, snow-laden evergreen shrubs and small snow-covered conifers along the foundation. Same shingle colour, same white trim, same portico, same green door. Do NOT invent a different house, a different colour or a different style. It is NOT brick, NOT clapboard, NOT stone, NOT painted, NOT grey.

THE LIGHT CURTAIN — the SAME huge dense curtain of warm white string lights as in REFERENCE IMAGE 2, now seen much closer and at an angle so the individual strands and bulbs are clearly resolved. It hangs flat over the front bay of the upper storey, its top edge tucked under the eaves where the man is working, its bottom hem uneven and wavy. It is built from many, many thin BLACK vertical wires hung very close together side by side from a header cable, each carrying small round bulbs spaced along it. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. The curtain is SEE-THROUGH — the cedar shingles and the white window mullions read clearly through the gaps between strands, and behind one upstairs window a lit Christmas tree glows through the curtain from inside the house. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet, NOT a printed banner — separate hanging strings with visible gaps between them. Every lit bulb is a point source with a blown-out white core and a small soft star flare; the glow bounces off the shingles as a soft halo and spills onto the snow below in a speckled, uneven pattern.

ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph. No other people, no faces to camera, no watermarks, no captions.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural cold blue-hour colour against the warm lights, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
````

### C06 — Night, phone, app — the tug-of-war

**In the cut:** `starting_frames/v35_c06_g1.png`, `references/v35_c06_r1.png` → `clips/v35_c06_g1.mp4`

#### Image prompt — `starting_frames/v35_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `c0339254-04bb-49ff-8d17-f49b42daec08`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175637_c0339254-04bb-49ff-8d17-f49b42daec08.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_33_assets/starting_frames/v33_c04_g1.png` · Higgsfield media `e1ee11e2-11c4-4548-9f19-42e0ea71ed0a`

````text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a driveway.

CAMERA AND FRAMING — copy this exactly from REFERENCE IMAGE 1. The camera stands on the driveway directly in front of a double garage door, square-on and level, close enough that the door fills almost the whole frame: the lintel and the two lit lamps across the top, snow-dusted concrete driveway across the bottom. Night, dark sky, the only light coming from the two lamps.

THE HOUSE — a DIFFERENT house from the reference. The garage wall is CHARCOAL GREY HORIZONTAL LAP SIDING — dark slate-grey painted boards running side to side in long horizontal lines. NOT green, NOT vertical, NOT board-and-batten, NOT brick, NOT stucco, NOT white. The double garage door itself is WHITE CARRIAGE-STYLE with raised rectangular panels, decorative black strap hinges and handles, and a row of small square windows across the top, framed by crisp white trim, with a warm-glowing BLACK GOOSENECK BARN LIGHT mounted on the charcoal siding above each end of the door.

THE CURTAIN — DENSE, exactly as dense as in REFERENCE IMAGE 1, and it MUST be clearly visible. A light curtain hangs over the whole white garage door from a header cable pinned under the lintel. Many, many thin BLACK vertical wires hung very close together side by side with only a narrow gap between neighbouring strands, covering the full width and full height of the door from edge to edge, wall to wall, top to bottom, each wire carrying small round bulbs spaced along it. Right now the bulbs are UNLIT and dark, so the curtain reads as a fine dense veil of black vertical dotted lines laid over the white door — the dark strands stand out plainly against the pale door, and you can still clearly see the door's panel seams and its row of small square windows through them. The veil covers the ENTIRE door: there is no bare patch of door anywhere, and it does not stop partway down. The bottom hem is uneven and wavy where the strands end at slightly different heights, and the strands sag a little. The wire is BLACK: NOT white, NOT clear, NOT silver, NOT copper. It is NOT an LED panel, NOT a screen, NOT a mesh fabric sheet — it is separate hanging strings with visible gaps between them.

EVERY STRAND IS IDENTICAL — CRITICAL. All the vertical wires are exactly the same thickness, the same darkness, the same length and the same spacing from one edge of the curtain to the other, top to bottom. There must be NO section anywhere in the sheet where the wires are thinner, finer, fainter, more closely bunched or drawn in a different pattern from the rest. There are NO horizontal cross-wires, NO ladder rungs, NO net, NO mesh weave, NO lattice — only plain vertical strands hanging straight down.

THE PHONE — from the bottom edge of the frame a bare right hand rises into shot holding a phone upright, screen facing the camera, tilted very slightly, the phone sitting in the lower centre of the frame in front of the garage door. On the screen: a black app background, a TWO-COLUMN grid of small square scene tiles each showing a simple blue-and-white pixel-art Christmas picture, and a large round blue play button centred below the grid. The screen is sharp, bright and clearly readable. No words or labels anywhere on the screen.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting. ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph.
````

#### Image prompt — `references/v35_c06_r1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `a9cec9e7-aa44-4a1a-8780-14c39d38cdb0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_180045_a9cec9e7-aa44-4a1a-8780-14c39d38cdb0.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/starting_frames/v35_c06_g1.png` · Higgsfield media `c0339254-04bb-49ff-8d17-f49b42daec08`
- @Image 2: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `40058517-9846-48c1-88e3-d48519a63b52`

````text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a driveway — the exact same house, same garage door and same camera position as REFERENCE IMAGE 1.

THE HOUSE AND FRAMING — identical to REFERENCE IMAGE 1: CHARCOAL-GREY horizontal lap siding, a CREAM / OFF-WHITE carriage-style double garage door filling almost the whole frame, square-on and level, with its row of small square black-paned windows across the upper section, black strap hinges and black centre handles, a white-painted surround, a warm-glowing BLACK GOOSENECK BARN LIGHT above each end, snow-dusted concrete driveway across the bottom, dark night sky. NO hand and NO phone in this photograph — the frame is completely clear of them.

THE CURTAIN IS NOW LIT and showing a picture across the whole garage door.

CRITICAL — HOW THE LIGHTS ARE BUILT. This is NOT an LED video wall, NOT a TV screen, NOT a projection, NOT a printed banner and NOT a pixel display. It is the same hanging curtain of string lights as in REFERENCE IMAGE 1: many separate thin BLACK wires hung close together side by side from a header cable under the lintel, each wire carrying small round bulbs. The whole picture is drawn in VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is a little wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square matrix. The curtain is SEE-THROUGH — through the gaps you plainly read the cream carriage door behind it, its panel seams and its row of small square windows, and the unlit areas are just dark garage door with dull grey unlit bulbs and faint black wires, NOT a solid coloured field and NOT a bright grey or white glowing background. Every lit bulb is a point source with a blown-out white core, a coloured halo and a small star flare, individually countable. The strands sag slightly and the bottom hem is uneven and wavy; the glow bounces back off the door as a soft halo and spills onto the snowy driveway in a speckled, uneven pattern.

HOW DETAILED AND BEAUTIFUL THE PICTURE IS — THE MOST IMPORTANT INSTRUCTION. This is a PREMIUM, EXPENSIVE, PROFESSIONALLY DESIGNED commercial Christmas light display, and the artwork must look it. The bulb grid is FINE and HIGH RESOLUTION — many hundreds of small bulbs across the width — so the characters are richly and skilfully drawn: proper expressive faces with real eyes, eyebrows and open mouths, confident clean outlines, folds and shading in the fabric, fur trim that actually reads as soft fur, highlights and shadow giving the figures roundness and volume, smooth flowing curves in the arms and body. Gorgeous, polished, eye-catching artwork. It is absolutely NOT a crude blocky 8-bit pixel sprite, NOT jagged, NOT clumsy, NOT a chunky Minecraft or cross-stitch chart, NOT low resolution, NOT a child's drawing. The only coarseness in the image comes from the physical gaps between the hanging strands — never from the drawing itself being clumsy or low-detail.

BUILT TO BE ANIMATED — READ THIS BEFORE DRAWING THE PICTURE. The picture contains exactly TWO large characters plus ONE simple prop, and nothing else. No crowds, no small background figures, no confetti, no arcs, no debris, no speed lines, no stars, no falling snowflakes, no scattered decorations. Roughly half of the curtain rectangle stays completely black and empty. Both characters are FULL FIGURES drawn at the same large size as each other, head to foot, planted firmly on the same ground line with their weight clearly readable, and clearly separated by a wide band of dark unlit curtain. Neither character is small, partial, hidden or cropped. The joke reads from held physical force one frame before it gives way — a strain frozen at its peak, not an action already finished.

THE PICTURE IN THE LIGHTS — THE TUG-OF-WAR OVER THE LAST PRESENT, seen side-on. In the CENTRE, between them, hangs ONE big square GOLD-WRAPPED PRESENT with a bright red ribbon cross and bow, lifted clear of the ground. On the LEFT stands Santa in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, both white-gloved hands clamped on the left edge of the present, leaning hard back and away to the LEFT with his heels dug in and his body at a steep angle, face screwed up with effort and his mouth wide open shouting. On the RIGHT stands the Grinch, a tall vivid lime-green figure in a red Santa hat and a red coat, both green hands clamped on the right edge of the same present, leaning hard back and away to the RIGHT at the same steep angle, heels dug in, teeth bared in a straining grin, eyes squeezed shut. They are stretched apart in a perfectly balanced deadlock, the present taut between them, held exactly one frame before it rips in half. The two figures and the one present are the ONLY things in the picture. Everything else is black unlit curtain.

The entire picture is contained INSIDE the rectangle of the curtain and touches none of its edges — both figures sit wholly within the lit rectangle with a clear margin all the way around, heads well below the top edge, boots well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the siding, the lintel, the sky or the driveway.

ABSOLUTELY NO text, letters, numbers, words or writing anywhere in the lights or anywhere else in the photograph.

COLOUR IS THE POINT. This is a full-colour RGB curtain and the shot has to sell that. Santa's coat is a deep saturated red with brilliant white fur trim, the Grinch is a vivid lime green, the present is bright gold with a vivid red ribbon. The picture must never collapse into a single warm-white or single-blue wash. Use REFERENCE IMAGE 2 ONLY as a guide to how rich, detailed and colourful bulb artwork looks — do NOT copy its subject matter or its composition.

Fully clothed cartoon figures, a silly slapstick pose and nothing more. No nudity, no bare skin beyond the green cartoon arms and face.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
````

#### Video prompt — `clips/v35_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `854da8b0-617f-49e8-875d-0fa402474a60`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_190454_854da8b0-617f-49e8-875d-0fa402474a60.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c06_g1.png` · Higgsfield media `c719b16c-d43c-408a-af06-79de9fb2a9da`
- image ref 1: `content/video_35_assets/references/v35_c06_r2.png` · Higgsfield media `c80b46fc-fbb5-45ab-a3d6-be0e8cadc9dc`

````text
THE FIRST FRAME OF THIS VIDEO IS THE START IMAGE, PIXEL FOR PIXEL, UNCHANGED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT.

WHAT IS IN THE START IMAGE, AND WHAT MUST THEREFORE BE IN FRAME 1: night, a suburban driveway shot on a held iPhone in portrait, square-on to the house; a wide CREAM / OFF-WHITE CARRIAGE-STYLE sectional double garage door with raised rectangular panels, black strap hinges, black centre handles and a row of small square black-paned windows across the top, set in CRISP WHITE trim; CHARCOAL-GREY HORIZONTAL LAP SIDING around it, dark slate-grey painted boards running side to side in long horizontal lines; ONE BLACK GOOSENECK BARN LIGHT mounted on the charcoal siding above each end of the door, one left and one right, both glowing warm downward; a snow-dusted concrete driveway across the bottom; the unlit BLACK LED curtain hanging flat across the garage door — and in this start image it is DENSE AND CLEARLY VISIBLE, reading as a fine dense veil of black vertical dotted lines and small dull unlit dots laid over the pale cream door, covering the entire door from edge to edge with no bare patch of door anywhere; and AT THE BOTTOM OF FRAME, A BARE RIGHT HAND RISING IN FROM THE BOTTOM EDGE HOLDING AN IPHONE UPRIGHT IN THE LOWER CENTRE OF FRAME, screen toward camera, showing a simple two-column grid of small blue preview tiles with a large round blue PLAY BUTTON at the bottom centre of the screen. Do NOT start on an empty driveway. Do NOT start on a bare garage door. Do NOT have the hand enter frame later. The hand and the phone are ALREADY THERE in frame 1, exactly as in the start image, rising in from the bottom edge.

THE SECOND ATTACHED IMAGE IS NOT A FRAME OF THIS VIDEO. It is only a style guide showing what the lit artwork must look like once the lights come on. Never cut to it, never start on it, never copy its framing, never copy its camera height, never copy its distance. Take from it ONLY the drawing that appears in the bulbs.

THE ARTWORK THAT APPEARS IN THE LIGHTS — THE TUG-OF-WAR OVER THE LAST PRESENT, seen side-on. In the CENTRE, between the two of them, hangs ONE big square GOLD-WRAPPED PRESENT with a bright red ribbon cross and bow, lifted clear of the ground. On the RIGHT stands the green character — a short, chunky, stocky green cartoon goblin with SMOOTH hairless kelly-green skin, a big round ball head with fat cheeks and no muzzle, a small round button nose, big round white eyes with small black pupils, short ROUNDED ears, short stubby arms and short bandy legs, chunky three-fingered mitten hands, a floppy FOREST-GREEN pointed cap with a white pom-pom, a mustard-yellow scarf and brown ankle boots — not tall, not lanky, no fur, no long muzzle, no pointed ears, NEVER named, simply the green character — both chunky mitten hands clamped on the right edge of the present, leaning hard back and away to the RIGHT at a steep angle, heels dug into the ground line, teeth bared in a straining grin, eyes squeezed shut. On the LEFT stands SANTA in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, both white-gloved fists clamped on the left edge of the same present, leaning hard back and away to the LEFT at the same steep angle, heels dug in, face screwed up with effort and his mouth wide open shouting. The two figures and the present are the ONLY things in the picture. The row of small square windows of the garage door reads through the top of the curtain behind the picture. Do NOT invent a different picture.

HOW THE LIGHTS MUST STAY BUILT. The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the lintel, each wire carrying small round bulbs. The whole picture is built out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix. The curtain is SEE-THROUGH: through the gaps between strands you clearly read the cream carriage door behind it, its panel seams and its row of small square windows, and the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark door, with unlit bulbs as tiny dull grey dots and the thin BLACK wires as faint vertical lines. Every lit bulb is a tiny point source: blown-out white core, coloured halo, small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing. The strands sag slightly, each ends at a slightly different height so the bottom hem is uneven and wavy, and the glow bounces back off the door as a soft halo and spills onto the snowy driveway in a speckled uneven pattern.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH, portrait, exactly the framing of the start image. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO CUT. The garage door stays the same size in frame throughout. The ONLY permitted camera move is a small gentle TILT UP in the second half of the clip, a few degrees, as if the person filming lifts their phone slightly to take in the whole door.

REAL TIME — NORMAL 1x SPEED. No fast motion, no sped-up playback, no time-lapse, no speed ramp.

THE PHONE SCREEN SCROLLS ONCE, EARLY, AND THEN STOPS FOR GOOD. In the first half-second the two-column grid of blue preview tiles physically TRAVELS UP THE GLASS under the moving thumb: whole rows slide upward and off the top edge while fresh rows rise in from the bottom. ONE swipe only. The instant the thumb presses play the screen is FINISHED — the grid freezes, the thumb stops moving, and nothing on the glass ever scrolls, slides or shifts again for the rest of the clip.

THE HAND LEAVES AND NEVER COMES BACK. THIS IS A HARD REQUIREMENT AND THE MOST COMMON WAY THIS SHOT FAILS. The hand and the phone are in frame for the first third of the clip ONLY. After the play press the hand drops straight down and out through the bottom edge in one smooth unhurried movement, the way you lower your arm to your side. From that moment on there is NO hand, NO phone, NO screen, NO thumb, NO fingers, NO wrist, NO sleeve and NO glow from a screen anywhere in frame — the bottom of the frame is bare snowy driveway. The hand does not linger, does not hover at the edge, does not rise back in, and is NOT still holding the phone at the end of the clip. A phone visible in the final second is a TOTAL FAILURE.

THE ANIMATION IN THE LIGHTS IS A REAL TUG-OF-WAR PLAYING AT NORMAL SPEED. Each action has room to read: a strain, a heave, a give. Every movement follows through and settles before the next one begins, the way two people actually move. It is lively and continuous, never frantic — a blur of limbs changing every few frames is a FAILURE, and so is a static or barely-moving picture.

TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.5s — exactly the start image, the curtain dark and unlit. The thumb is already pressed against the glass and SWIPES UP once: the whole two-column grid of blue tiles scrolls upward with it, the top row sliding up and off the top edge of the screen while a new row of tiles rises in from the bottom edge, then decelerating and settling, leaving the big round blue PLAY BUTTON at the bottom centre of the screen.
0.5-0.7s — the thumb slides onto the blue PLAY BUTTON and presses it. The button dips and highlights under the press. The grid behind it is now completely frozen and never moves again.
0.7-0.9s — IN THE SAME FRAME, without any cut, the whole LED curtain snaps ON at once, the tug-of-war appearing all together in chunky bulbs, and warm coloured light floods across the snowy driveway.
0.9-1.4s — the hand lowers steadily and smoothly straight down and out through the bottom edge of frame. By 1.4s the hand and the phone are COMPLETELY GONE from the picture and never return. Nothing is left along the bottom edge but snowy driveway.
1.4-4.0s — the camera drifts gently upward a few degrees and the tug-of-war gag plays out in FOUR unhurried beats, each one given enough time to read clearly:
1.4-2.0s — THE STRAIN. Both figures lean further back and away from each other, heels skidding a little along the ground line, the gold present stretched taut between them; Santa's white beard swings out sideways and the green character's pom-pom cap tips back off his forehead.
2.0-2.6s — SANTA HEAVES. Santa hauls back on the present hand over hand and drags the green character a full step toward him, both brown ankle boots skidding along the ground line, his short stubby arms pulled out straight in front of him.
2.6-3.2s — THE GREEN CHARACTER HEAVES BACK. He digs both boots in, throws his whole weight backward and drags Santa a step the other way, Santa's big black boots skidding along the ground line and his white beard swinging forward across his face.
3.2-4.0s — THE PAYOFF. The red ribbon gives all at once, the present pops free, and both figures drop flat on their backs along the ground line with their boots up, the gold present bouncing once on the ground line between them and settling there.
Each pose is rendered by bulbs switching on and off row by row across the grid — chunky and stepped, never smooth morphing, never a crossfade. NO BEAT IS EVER A BRIGHTNESS CHANGE: every beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.

MOTION QUALITY — HARD RULE: from 1.4s onward the two figures are moving continuously, but as WHOLE BODIES with real weight, not as a flicker of separate parts. Arms swing from the shoulder, bodies lean into a heave and follow through past it, boots skid and settle, the present swings and jerks between them. An arm that teleports between poses, a limb that changes length, a figure that jitters in place or a body that dissolves and reforms is a FAILURE.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER LEAVES THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the door. No green arm, no green foot, no white glove, no boot, no gold present and no trailing red ribbon ever crosses outside the curtain rectangle. At every instant every figure keeps a clear margin of at least two full unlit strands of dark door inside every edge of the curtain. If a pose would take a limb or the tugged present out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Both figures keep their feet on the same ground line and stay low and contained; nothing launches upward out of the picture. Nothing lit ever appears on the crisp white trim, the charcoal-grey lap siding, the black gooseneck barn lights, the sky or the driveway except as reflected spill.

EVERYTHING ELSE IS UNCHANGED: the house, the cream carriage door, the two black gooseneck barn lights, the charcoal-grey lap siding, the snow and the camera position are identical from first frame to last. No people, no cars, no pets enter frame.

NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural sound only — no music, no score, no background song. Cold quiet suburban night ambience, a soft phone tap, a faint electrical hum and tick from the lights, a distant car, light wind. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C06 on disk (1)**

#### Image prompt — `references/v35_c06_r2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `107c34e8-06b6-4303-afd6-0728eb6de24e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_184055_107c34e8-06b6-4303-afd6-0728eb6de24e.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/references/v35_c06_r1.png` · Higgsfield media `834e13c0-0ea4-4657-a730-d64fb18620c2`

````text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a driveway.

COPY REFERENCE IMAGE 1 EXACTLY in every respect EXCEPT the green character. Same CHARCOAL-GREY HORIZONTAL LAP SIDING, same CREAM / OFF-WHITE carriage-style double garage door filling almost the whole frame square-on and level, same row of small square black-paned windows across its upper section, same black strap hinges and black centre handles, same white-painted surround, same warm-glowing BLACK GOOSENECK BARN LIGHT above each end, same snow-dusted concrete driveway across the bottom, same dark night sky. Same lit LED light curtain across the whole garage door with the same size, position and black strand structure — many separate thin BLACK wires hung side by side, the picture drawn in VERTICAL DOTTED LINES OF LIGHT, see-through so the cream carriage door reads through the gaps, every lit bulb a point source with a blown-out white core and a coloured halo, roughly half the curtain staying black and empty. Same Santa on the LEFT in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, both white-gloved hands clamped on the left edge of the present, leaning hard back and away to the LEFT with his heels dug in and his body at a steep angle, face screwed up with effort and his mouth wide open shouting. Same ONE big square GOLD-WRAPPED PRESENT with a bright red ribbon cross and bow hanging in the CENTRE between them, lifted clear of the ground. Same rich premium bulb artwork, same colours, same wide band of dark unlit curtain between the two figures. NO hand and NO phone anywhere in the photograph.

THE ONLY CHANGE — THE GREEN CHARACTER IS A COMPLETELY DIFFERENT, ORIGINAL CHARACTER INVENTED FOR THIS ADVERT. Redraw him from scratch as follows. He is a short, CHUNKY, stocky little green cartoon goblin, clearly shorter than Santa, with a round pot belly. His skin is SMOOTH bright kelly green — completely hairless, no fur, no shaggy coat, no fuzzy or furry texture anywhere on him. His head is a big ROUND ball, wider than it is tall, with fat rounded cheeks and no muzzle at all. He has a small round button nose, a wide open mouth, two big round WHITE eyes with small round black pupils, and thick dark eyebrows. His ears are short and ROUNDED, like small coins flat against the side of his head. He has short stubby arms, short bandy legs and chunky three-fingered mitten hands. He wears a floppy FOREST-GREEN pointed cap with a white pom-pom on the end, a mustard-yellow scarf, and brown ankle boots with turned-up toes.

He must NOT be tall, lanky or spindly. NO fur anywhere. NO long snout and NO long grinning muzzle. NO pointed ears. NO yellow eyes. NO red-and-white Santa hat or Santa suit on him. He must not resemble any existing film, television or book character.

He stands on the RIGHT, a FULL FIGURE head to foot planted firmly on the same ground line as Santa and drawn LARGE in the curtain, both chunky mitten hands clamped on the right edge of the same gold present, leaning hard back and away to the RIGHT at the same steep angle as Santa, heels dug in, knees bent, teeth bared in a straining grin, eyes squeezed shut. They are stretched apart in a perfectly balanced deadlock, the present taut between them, held exactly one frame before it rips in half. The two figures and the one present are the ONLY things in the picture — no crowds, no confetti, no arcs, no debris, no speed lines, no stars, no falling snowflakes. Everything else is black unlit curtain.

The whole picture stays INSIDE the rectangle of the curtain and touches none of its edges — both figures sit wholly within the lit rectangle with a clear margin all the way around, heads well below the top edge, boots well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the siding, the lintel, the sky or the driveway. ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no CGI or 3D-render look, no illustration, no painting.
````

### C07 — The sack swing

**In the cut:** `starting_frames/v35_c07_g2.png` → `clips/v35_c07_g1.mp4`

#### Image prompt — `starting_frames/v35_c07_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `f1c59969-baec-4f01-8c8f-52026ef97a8f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_184055_f1c59969-baec-4f01-8c8f-52026ef97a8f.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/starting_frames/v35_c07_g1.png` · Higgsfield media `56eeae8f-2f34-4b4f-a35e-715c6cb5a266`

````text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on the snowy front garden of a suburban house.

COPY REFERENCE IMAGE 1 EXACTLY in every respect EXCEPT the green character. Same camera position on the shovelled front path at chest height, square-on to the house and tilted very slightly up. Same PALE SAGE-GREEN painted clapboard with horizontal weatherboards, same crisp white trim, same grey shingle roof, same white window frames with warm lit windows upstairs, same small covered front porch with white posts and a DEEP RED front door with a wreath on it, same low white picket fence and snowy path across the foreground, same dark evergreen at the right edge, same snow on the ground and along the fence, same dark night sky. Same single BIG light curtain hung flat and level filling the WHOLE WIDE UPPER WALL of the house front, same size and position, with the same black strand structure — many separate thin BLACK wires hung side by side, the picture drawn in VERTICAL DOTTED LINES OF LIGHT, see-through so the sage-green clapboard reads through the gaps, every lit bulb a point source with a blown-out white core and a coloured halo, roughly half the curtain staying black and empty. Same Santa on the LEFT in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, feet planted wide, twisted right round with his huge bulging RED SACK hoisted high over his head in both white-gloved hands like a hammer about to come down, knees bent, teeth gritted and eyes narrowed in effort. Same rich premium bulb artwork, same colours, same wide band of dark unlit curtain between the two figures. NO hand and NO phone anywhere in the photograph.

THE ONLY CHANGE — THE GREEN CHARACTER IS A COMPLETELY DIFFERENT, ORIGINAL CHARACTER INVENTED FOR THIS ADVERT. Redraw him from scratch as follows. He is a short, CHUNKY, stocky little green cartoon goblin, clearly shorter than Santa, with a round pot belly. His skin is SMOOTH bright kelly green — completely hairless, no fur, no shaggy coat, no fuzzy or furry texture anywhere on him. His head is a big ROUND ball, wider than it is tall, with fat rounded cheeks and no muzzle at all. He has a small round button nose, a wide open mouth, two big round WHITE eyes with small round black pupils, and thick dark eyebrows. His ears are short and ROUNDED, like small coins flat against the side of his head. He has short stubby arms, short bandy legs and chunky three-fingered mitten hands. He wears a floppy FOREST-GREEN pointed cap with a white pom-pom on the end, a mustard-yellow scarf, and brown ankle boots with turned-up toes.

He must NOT be tall, lanky or spindly. NO fur anywhere. NO long snout and NO long grinning muzzle. NO pointed ears. NO yellow eyes. NO red-and-white Santa hat or Santa suit on him. He must not resemble any existing film, television or book character.

He stands on the RIGHT, a FULL FIGURE head to foot planted firmly on the same ground line as Santa and drawn LARGE in the curtain, ducking — knees bent deep, head pulled down into his shoulders, both chunky mitten hands clamped flat over the top of his floppy green cap, one eye squinting up at the sack, mouth pulled wide in a terrified grimace. Held exactly one frame before the sack swings down. The two figures and the one red sack are the ONLY things in the picture — no crowds, no confetti, no arcs, no debris, no speed lines, no stars, no falling snowflakes. Everything else is black unlit curtain.

The whole picture stays INSIDE the rectangle of the curtain and touches none of its edges — both figures sit wholly within the lit rectangle with a clear margin all the way around, the sack and Santa's head well below the top edge, both sets of feet well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the wall, the roof, the sky or the ground. ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no CGI or 3D-render look, no illustration, no painting.
````

#### Video prompt — `clips/v35_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `f5952bf7-80e4-45ae-9bc3-1e3ee804d229`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_190004_f5952bf7-80e4-45ae-9bc3-1e3ee804d229.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c07_g2.png` · Higgsfield media `87c55480-d9ef-4185-874f-a06621e48f0f`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same PALE SAGE-GREEN PAINTED CLAPBOARD house with horizontal weatherboards, a GREY SHINGLE ROOF and WHITE WINDOW FRAMES with warm lit windows upstairs, same low snow-capped white PICKET FENCE across the foreground, same shovelled snowy path running up to the house with snow either side, same covered front porch with square white posts and a DEEP RED FRONT DOOR with a WREATH, same dark snowy evergreen at the right edge, same single large lit LED curtain FILLING THE WHOLE WIDE UPPER WALL of the house front — one clean level rectangle spanning almost the full width of the sage-green clapboard facade, its left and right edges running out close to the corners of the house and its top edge just under the eaves — showing THE SACK SWING: at the LEFT SANTA in a deep saturated red coat with white fur trim, a white beard and a black belt, feet planted wide and twisted right round with his huge bulging RED SACK hoisted high over his head in both white-gloved fists like a hammer about to come down, knees bent, teeth gritted and eyes narrowed in effort; at the RIGHT the green character — a short, chunky, stocky green cartoon goblin with SMOOTH hairless kelly-green skin, a big round ball head with fat cheeks and no muzzle, a small round button nose, big round white eyes with small black pupils, short ROUNDED ears, short stubby arms and short bandy legs, chunky three-fingered mitten hands, a floppy FOREST-GREEN pointed cap with a white pom-pom, a mustard-yellow scarf and brown ankle boots — not tall, not lanky, no fur, no long muzzle, no pointed ears, NEVER named, simply the green character — ducking, knees bent deep, head pulled down into his shoulders, both chunky mitten hands clamped flat over the top of his floppy green cap, one eye squinting up at the sack, mouth pulled wide in a terrified grimace.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the picket fence, the snowbanks and the shrubs at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

MOVEMENT — THE ANIMATION IS THE WHOLE POINT AND IT NEVER RESTS. It is already ON and running at full speed in the very first frame and is STILL running flat out in the last frame. THE FIGURES REDRAW COMPLETELY EVERY QUARTER SECOND — SIXTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each a big obvious physical movement, never a small twitch. NO BEAT IS EVER A BRIGHTNESS CHANGE: every single beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.
0.25s — Santa hoists the red sack even higher up and back behind his head and both his elbows fly wider.
0.50s — the sack comes whipping down low across the picture in one heavy arc and Santa's whole body swings round after it.
0.75s — the green character flattens right down to the ground line with both mitten hands over his cap and the sack sweeps clean over him.
1.00s — Santa hauls the sack back up over his shoulder for a second swing, both black boots skidding a half-step on the ground line.
1.25s — the green character springs back up, plants both brown boots wide and flaps both stubby arms at him, cheeks puffed.
1.50s — the sack comes down a second time and he drops flat again, both bandy legs kicked out behind him.
1.75s — at the bottom of the arc the mouth of the sack flies open and ONE GOLD-WRAPPED PRESENT pops clear of it.
2.00s — Santa stops dead with both white gloves still clamped on the slack sack, his head snapping round after the present, his white beard swinging across his face.
2.25s — the gold present bounces twice along the ground line and rolls to a stop against the green character's brown boot.
2.50s — the green character bends down, picks it up, holds it up and waggles it, both huge white eyes going wide.
2.75s — Santa drops the sack, scrambles onto all fours and lunges for it, both gloves stretched out.
3.00s — his gloves slip out from under him on the packed ground line and he flattens out, arms and legs spread wide.
3.25s — the green character hops backward twice on one foot, still holding the present up out of reach.
3.50s — Santa gets one boot planted, pushes up and stands swaying, both arms out wide for balance.
3.75s — his boot catches the slack red sack and he tips right back over it, the sack upending behind him.
4.00s — everything peaks together: Santa tipped fully back with both boots up and both arms flung wide, the sack upended, the green character bent double howling with the gold present held overhead — every limb staying well inside the lit rectangle.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — Santa's boots, his arms, his hat and beard, his sack, the green character's arms, his legs, his ears, his eyes, his grin, the big red sack, the gold present. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the large sage-green clapboard upper wall of the house front". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. THE BIGGER THE MOTION GETS, THE MORE STRICTLY THIS APPLIES. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No flung arm, no black boot, no green leg, no brown boot, no swinging red sack and no tumbling gold present ever touches or crosses outside the curtain rectangle. At every instant, in every pose, every figure keeps a clear margin of at least two full unlit strands of dark wall inside every edge of the curtain — top, bottom, left and right. If a swing, a windmill, a thrown-up arm or a bouncing present would reach an edge, THE POSE IS DRAWN SMALLER so it stays inside — the rectangle is never made bigger to fit it. Santa falls along the ground line and stays low; nothing is launched upward out of the picture. Nothing spills onto the grey shingle roof, the white window frames, the porch, the deep red front door, the sky or the evergreen. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail and does not gain size.

HARD RULES: no people, no cars, no pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C07 on disk (1)**

#### Image prompt — `starting_frames/v35_c07_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `646ce417-da2b-410d-a602-20cb46e09178`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175637_646ce417-da2b-410d-a602-20cb46e09178.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_33_assets/starting_frames/v33_c05_g1.png` · Higgsfield media `f8d942f2-70c2-4b4a-820a-54e099c7844e`
- @Image 2: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `40058517-9846-48c1-88e3-d48519a63b52`

````text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on the snowy front garden of a suburban house.

FRAMING — copy this exactly from REFERENCE IMAGE 1. The camera stands on the shovelled front path at chest height, square-on to the front of a two-storey house and tilted very slightly up. A low white picket fence and the snowy path run across the foreground; the house fills the upper two thirds of the frame; a dark evergreen stands at the right edge.

THE HOUSE — a DIFFERENT house from the reference: PALE SAGE-GREEN painted clapboard with horizontal weatherboards, crisp white trim, a grey shingle roof, white window frames with warm lit windows upstairs, and a small covered front porch with white posts and a DEEP RED front door with a wreath on it. Snow on the ground and along the fence. NOT red brick, NOT stone, NOT stucco, NOT white, NOT blue.

WHERE THE CURTAIN HANGS — CRITICAL. There is ONE single light curtain and it is BIG. It is one clean rectangle, hung flat and perfectly level, and it FILLS THE WHOLE WIDE UPPER WALL of the house front — spanning almost the full width of the sage-green facade, its left and right edges running out close to the corners of the house, leaving only a narrow strip of wall, NOT a wide margin. Its top edge sits just under the eaves. This is a LARGE, dominant, wall-filling display that takes up most of the visible wall — NOT a small panel floating in the middle of the wall with big empty margins around it, NOT two separate patches of light.

HOW DETAILED AND BEAUTIFUL THE PICTURE IS — THE MOST IMPORTANT INSTRUCTION. This is a PREMIUM, EXPENSIVE, PROFESSIONALLY DESIGNED commercial Christmas light display, and the artwork must look it. The bulb grid is FINE and HIGH RESOLUTION — many hundreds of small bulbs across the width — so the characters are richly and skilfully drawn: proper expressive faces with real eyes, eyebrows and open mouths, confident clean outlines, folds and shading in the fabric, fur trim that actually reads as soft fur, highlights and shadow giving the figures roundness and volume, smooth flowing curves in the arms and body. Gorgeous, polished, eye-catching artwork. It is absolutely NOT a crude blocky 8-bit pixel sprite, NOT jagged, NOT clumsy, NOT a chunky Minecraft or cross-stitch chart, NOT low resolution, NOT a child's drawing. The only coarseness in the image comes from the physical gaps between the hanging strands — never from the drawing itself being clumsy or low-detail.

CRITICAL — HOW THE LIGHTS ARE BUILT. This is NOT an LED video wall, NOT a TV screen, NOT a projection, NOT a printed banner. It is a hanging curtain of string lights: many separate thin BLACK wires hung close together side by side from a header cable, each wire carrying a close-spaced run of small round bulbs. The picture is built from VERTICAL DOTTED LINES OF LIGHT — the horizontal gap between neighbouring strands is a little wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular rather than a square matrix. The curtain is SEE-THROUGH — through the gaps you can read the sage-green clapboard wall behind it, and the unlit areas are just dark wall with dull grey unlit bulbs and faint black wires, NOT a solid coloured field. Every lit bulb is a point source with a blown-out white core, a coloured halo and a small soft star flare. The strands sag slightly and the bottom hem is uneven and wavy; the glow bounces off the wall as a soft halo and spills onto the snow in a speckled, uneven pattern.

BUILT TO BE ANIMATED. Exactly TWO large characters and nothing else. NO crowd of little figures, NO confetti field, NO scattered snowflakes filling the background, NO dotted motion arcs, NO flying debris, NO speed lines, NO stars. Each character is one clear shape separated from the other by a wide band of completely dark unlit curtain, so you could trace its outline with a finger. Roughly HALF of the curtain rectangle stays BLACK and empty. Both characters are FULL FIGURES drawn head to foot at the same large size as each other. The joke reads from a held physical force in their bodies, one frame before it gives way.

THE PICTURE IN THE LIGHTS — the sack swing. On the LEFT stands Santa in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, feet planted wide, twisted right round with his huge bulging RED SACK hoisted high over his head in both white-gloved hands like a hammer about to come down, knees bent, teeth gritted and eyes narrowed in effort. On the RIGHT the Grinch, a tall vivid lime-green figure in a red Santa hat and a red coat, is ducking — knees bent deep, head pulled down into his shoulders, both green hands clamped flat over the top of his head, one eye squinting up at the sack, mouth pulled wide in a terrified grimace. Held exactly one frame before the sack swings down.

The entire picture is contained INSIDE the rectangle of the curtain and touches none of its edges — both figures sit wholly within the lit rectangle with a clear margin all the way around, the sack and Santa's head well below the top edge, both sets of feet well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the wall, the roof, the sky or the ground.

ABSOLUTELY NO text, letters, numbers, words or writing anywhere in the lights or anywhere else in the photograph.

COLOUR IS THE POINT. Santa's coat and sack are a deep saturated red with brilliant white fur trim, his boots are black, the Grinch is a vivid lime green. The picture must never collapse into a single warm-white or single-blue wash. Use REFERENCE IMAGE 2 ONLY as a guide to how finely and richly bulb artwork can be drawn — do NOT copy its subject matter and do NOT copy its single-colour warm-white palette.

Fully clothed cartoon figures, a silly slapstick pose and nothing more.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, every bulb crisply resolved, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
````

### C08 — The candy-cane duel

**In the cut:** `starting_frames/v35_c08_g2.png` → `clips/v35_c08_g1.mp4`

#### Image prompt — `starting_frames/v35_c08_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `3c93d061-da86-486d-8e60-e326013cfb6f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_184055_3c93d061-da86-486d-8e60-e326013cfb6f.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_35_assets/starting_frames/v35_c08_g1.png` · Higgsfield media `1c444198-1556-4110-8ff4-547712468dcb`

````text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a suburban driveway.

COPY REFERENCE IMAGE 1 EXACTLY in every respect EXCEPT the green character. Same camera position, same framing and same proportions. Same CREAM STUCCO house with dark chocolate-brown TUDOR HALF-TIMBER BEAMS crossing the projecting gable above the garage, same small black pendant lantern hanging in the peak, same warm lit leaded window off to the left, same bare winter tree at the right edge, same snow on the ground. Same group of neighbours in winter coats and bobble hats standing in the near foreground with their BACKS to the camera in dark silhouette, their heads and shoulders filling the bottom third of the frame at a range of heights, and the same wet glossy driveway throwing a long smeared multicoloured reflection back toward the camera. Same light curtain hanging across the DOUBLE GARAGE DOOR and nowhere else, completely filling the garage door opening edge to edge and corner to corner, with the same black strand structure — many separate thin BLACK wires hung side by side, the picture drawn in VERTICAL DOTTED LINES OF LIGHT, every lit bulb a point source with a blown-out white core, a coloured halo and a small soft star flare, individually countable. Same soft, even, gently graded wash of PASTEL BLUE, VIOLET AND PINK light filling the rectangle behind the characters with the white grid of bulbs reading through it. Same Santa on the LEFT in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, gripping a huge red-and-white striped CANDY CANE two-handed like a sword, leaning in with his front knee bent deep and his back leg braced straight behind, weight thrown forward, teeth gritted, one eye squeezed shut with effort. Same two candy canes crossed and locked hard against each other in the centre between the two figures. Same rich premium bulb artwork and same colours. NO hand and NO phone anywhere in the photograph.

THE ONLY CHANGE — THE GREEN CHARACTER IS A COMPLETELY DIFFERENT, ORIGINAL CHARACTER INVENTED FOR THIS ADVERT. Redraw him from scratch as follows. He is a short, CHUNKY, stocky little green cartoon goblin, clearly shorter than Santa, with a round pot belly. His skin is SMOOTH bright kelly green — completely hairless, no fur, no shaggy coat, no fuzzy or furry texture anywhere on him. His head is a big ROUND ball, wider than it is tall, with fat rounded cheeks and no muzzle at all. He has a small round button nose, a wide open mouth, two big round WHITE eyes with small round black pupils, and thick dark eyebrows. His ears are short and ROUNDED, like small coins flat against the side of his head. He has short stubby arms, short bandy legs and chunky three-fingered mitten hands. He wears a floppy FOREST-GREEN pointed cap with a white pom-pom on the end, a mustard-yellow scarf, and brown ankle boots with turned-up toes.

He must NOT be tall, lanky or spindly. NO fur anywhere. NO long snout and NO long grinning muzzle. NO pointed ears. NO yellow eyes. NO red-and-white Santa hat or Santa suit on him. He must not resemble any existing film, television or book character.

He stands on the RIGHT, a FULL FIGURE head to foot planted firmly on the same ground line as Santa, facing him across the middle of the rectangle like a fencer, gripping his huge red-and-white striped CANDY CANE two-handed in his chunky mitten hands, leaning in just as hard with his front knee bent deep and his back leg braced straight behind, weight thrown forward, mouth wide open in a snarling grin. Held exactly one frame before one of them gives way. The two figures and the two candy canes are the ONLY things in the picture — no third character, no crowd inside the lights, no confetti, no arcs, no debris, no speed lines, no stars, no floating hearts, no falling snowflakes.

BOTH CHARACTERS SIT WHOLLY INSIDE THE RECTANGLE. Together they fill about two thirds of the height of the curtain rectangle, with a clear margin of the pastel background all the way around — heads well below the top edge, boots well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the garage frame, the stucco, the timber beams, the lantern, the sky or the driveway. ABSOLUTELY NO text, letters, numbers or writing anywhere in the photograph.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, every bulb crisply resolved, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no CGI or 3D-render look, no illustration, no painting.
````

#### Video prompt — `clips/v35_c08_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `3394f962-722a-4154-b92a-2aee0de63574`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260918_190004_3394f962-722a-4154-b92a-2aee0de63574.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v35_c08_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_35_assets/starting_frames/v35_c08_g2.png` · Higgsfield media `a8c877e2-2ef5-437f-a1ff-ce7b7a9228ff`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same CREAM STUCCO house with dark chocolate-brown TUDOR HALF-TIMBER BEAMS crossing the projecting gable over the garage, same small BLACK PENDANT LANTERN hanging in the peak, same warm lit leaded window off to the left, same BARE WINTER TREE at the right edge of frame, same wet glossy driveway throwing the coloured light back in long smeared reflections, same crowd of neighbours in winter coats and bobble hats seen FROM BEHIND in the near foreground, adults and children together, their heads and shoulders filling the bottom third of the frame at a range of heights, same lit LED curtain covering the whole double garage door showing THE CANDY-CANE DUEL: at the LEFT SANTA in a deep saturated red coat with white fur trim, a black belt and big black boots, gripping a huge RED-AND-WHITE STRIPED CANDY CANE two-handed like a sword, front knee bent deep and back leg braced straight behind him, weight thrown forward, teeth gritted and one eye squeezed shut with effort; at the RIGHT the green character — a short, chunky, stocky green cartoon goblin with SMOOTH hairless kelly-green skin, a big round ball head with fat cheeks and no muzzle, a small round button nose, big round white eyes with small black pupils, short ROUNDED ears, short stubby arms and short bandy legs, chunky three-fingered mitten hands, a floppy FOREST-GREEN pointed cap with a white pom-pom, a mustard-yellow scarf and brown ankle boots — not tall, not lanky, no fur, no long muzzle, no pointed ears, NEVER named, simply the green character — gripping his own huge red-and-white striped candy cane two-handed in both mitten hands, leaning in just as hard with his front knee bent deep and his back leg braced straight, mouth wide open in a snarling grin; the two canes crossed and locked hard against each other in the centre between them.

ABSOLUTE FIRST RULE — THE LIT PICTURE IS TRAPPED INSIDE THE CURTAIN RECTANGLE. In the reference image the lit LED curtain is a rectangle hanging across the double garage door only, and it stops short of the door's edges. That rectangle is FIXED for the whole four seconds: it never grows, never widens, never rises, never rescales, never warps, never drifts, and the camera never changes size on it. Santa, the green character and the two crossed candy canes are drawn INSIDE that rectangle with a clear band left all the way round — a generous margin at the top, and margins at the left, right and bottom.
NOTHING LIT EVER CROSSES AN EDGE, AND THE BIGGER THE MOTION GETS THE MORE STRICTLY THIS APPLIES. No arm, no black boot, no brown ankle boot, no red hat, no floppy green cap and neither candy cane ever touches or crosses the edge of the curtain, and nothing lit ever appears on the cream stucco, the dark chocolate Tudor half-timber beams, the projecting gable, the black pendant lantern, the bare winter tree or the sky. At every instant, in every pose, every figure keeps a clear margin of at least two full unlit strands inside every edge of the curtain. If a pose would take a limb or a swinging candy cane out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. The duel stays low and contained: both figures keep their feet on the same ground line, and neither they nor a knocked-away cane is ever launched up toward the top edge. Every surface outside the curtain stays exactly as lit as it is in the reference image for the whole four seconds.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, filmed from behind the group at the bottom of the driveway. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE. The house and the garage door stay exactly the same size in frame from the first frame to the last.

THE CROWD IS CASUAL, RELAXED AND ALREADY HAPPY — AND ALREADY MOVING IN THE VERY FIRST FRAME. This is not an audience waiting for something to happen. Nobody is standing frozen staring at the garage in anticipation, nobody holds still and then reacts, there is no build-up and no big synchronised cheer. They are neighbours hanging about on a driveway on a cold night, chatting to each other, laughing at each other, sipping drinks, glancing over at the lights and then back at their friends. Their attention drifts on and off the garage the whole time. They are ALL seen FROM BEHIND — no face is ever turned toward camera.
AT 0.0s, IN THE VERY FIRST FRAME, EVERY PERSON IS ALREADY MID-MOVEMENT. There is NO still opening frame, NO frozen first beat, NO pause before the motion starts, NO moment where the group holds and waits. Someone is already mid-laugh, someone is already turning, someone is already raising a cup, a child is already bouncing on the spot. The clip starts in the middle of the action and never settles.
CONTINUOUS OVERLAPPING MOTION, EVERY HALF SECOND, NEVER IN UNISON — at any instant several different people are doing several different things, and their little actions start and stop at different times so the group always looks alive:
0.0-0.5s — two adults near the front are mid-conversation, heads turned to each other, one shrugging; a child at the left bounces twice on the spot and tugs at the sleeve of the adult beside them.
0.5-1.0s — a woman in the centre laughs and rocks back on her heels, shoulders shaking; a man at the right shifts his weight to his other foot; someone lifts a takeaway cup and drinks.
1.0-1.5s — someone in the front leans into the person beside them and points lazily at the lights without turning round; a teenager at the left shoves both hands deeper into their pockets, hunches, and blows out a long fog of breath.
1.5-2.0s — a woman at the left leans sideways into the person next to her and says something; they both laugh; another person scratches under their bobble hat and looks away from the garage entirely.
2.0-2.5s — two people knock shoulders and one claps once, casually; a small child is lifted up onto an adult's hip and settles there, bobble hat wobbling.
2.5-3.0s — scattered easy laughter ripples through the group, a few loose claps at different moments, not together; one adult crouches down to a child's height and points up at the lights; another points out at them with a cup still in hand.
3.0-3.5s — the man at the right wipes his eyes laughing and says something sideways; two heads tip together; a bobble hat bobs as someone nods along.
3.5-4.0s — a few people applaud loosely, hats bobbing, breath fogging, someone waves an arm overhead at a neighbour further down the drive, someone else is already turning to talk to the person behind them.
Coats crease, bobble hats bob, breath fogs, boots shift on the wet driveway, shoulders shake with laughter. NOBODY IS EVER STILL and nobody is waiting.

THE ARTWORK IS THE MAIN EVENT AND IT IS FRANTIC. THE VERY FIRST FRAME OF THE CLIP IS ALREADY MID-ACTION — THE LIT PICTURE DOES NOT HOLD, DOES NOT PAUSE, DOES NOT SETTLE AND DOES NOT EASE IN. There is NO still opening frame on the garage door, NO frozen first beat, NO moment at the start where Santa and the green character hold their reference pose while only the crowd moves. THE FIRST POSE CHANGE IN THE ARTWORK LANDS BEFORE 0.15s AND IS AS BIG AS EVERY LATER ONE. The picture redraws COMPLETELY EVERY QUARTER SECOND. SEVENTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each a big obvious physical change, never a small twitch. NO BEAT IS EVER A BRIGHTNESS CHANGE: every single beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.
0.00s — it lands out of the first frame already mid-move: the two crossed candy canes are already grinding hard against each other and snapping back apart, Santa already skidding a half-step to the right with both boots sliding on the ground line while the green character drives forward off his braced back boot.
0.25s — the canes break apart and both figures rock back, each cane swung out wide to its own side.
0.50s — they clash together again in the centre, the two canes cracking against each other, both heads jerking with the impact.
0.75s — the green character swings low at Santa's legs and Santa hops both black boots clear of the ground line.
1.00s — Santa counters with a hard swing at the middle and the green character parries it two-handed above his head, knees dipping.
1.25s — the canes lock again and the two of them push in until their faces almost touch, both leaning at a steep angle.
1.50s — Santa's red hat tips down over one eye and he shoves it back up with one white glove, his cane held off in the other fist.
1.75s — the green character's floppy green cap flops down over his face and he blows it back up out of his eyes, both mitten hands still clamped on his cane.
2.00s — both canes whip round in a fast figure-of-eight between them, elbows flying wide.
2.25s — they double-parry, the two canes crossed overhead, both pairs of boots skidding apart along the ground line.
2.50s — Santa lunges forward off his back boot, cane thrust straight out, his white beard streaming back.
2.75s — the green character twists aside, knees dipping deep, and hooks his own cane round Santa's.
3.00s — he twists Santa's cane clean out of both white gloves and it clatters down onto the ground line between them.
3.25s — Santa rocks right back on his heels, both empty gloves flying up wide, mouth open in a yell.
3.50s — the green character scoops the fallen cane up off the ground line and comes on with one in each mitten hand, waggling both at him.
3.75s — Santa backs off a step with both gloves up in surrender, boots skidding, knees bent.
4.00s — everything peaks together: the green character planted wide with both candy canes brandished overhead and his mouth open in a howl, Santa bent right back on his heels with both gloves flung up and his mouth wide open — every limb still well inside the lit rectangle.
Every pose change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing. The coloured reflections on the wet driveway shift and ripple with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — Santa's arms, his boots, his red hat, his beard, his face, the green character's arms, his legs, his brown ankle boots, his ears, his eyes, his grin, his floppy green cap and the two striped candy canes. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE. This must read as frantic, laugh-out-loud cartoon slapstick with something big happening everywhere you look.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
BACKGROUND OVERRIDE, READ THIS FIRST: in this reference image the curtain carries a SOFT PASTEL BLUE, VIOLET AND PINK BACKGROUND FIELD filling the whole rectangle behind the two figures. That coloured background is part of the start image and it STAYS exactly as it is — it is the one and only exception to the line further down about solid saturated background fields. But it is still built out of individual countable bulbs on see-through vertical strands, never a smooth colour wash, never a flat painted panel and never a screen. Its colours may shift and ripple with the animation, but the field itself never becomes a solid glowing surface, and it never turns into a dirty grey haze or a muddy fog. Everything else in the block below applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its horizontal panel seams, its trim, the faint shadows of the wires falling on it. Away from the coloured field the areas are NOT a solid painted surface — the unlit bulbs show as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the wet driveway in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE GARAGE DOOR IS THE ONLY LIT SURFACE. The artwork is hard-cropped at all four edges of the curtain. It NEVER grows, shrinks, shifts, warps or drifts. Nothing spills onto the cream stucco, the dark chocolate Tudor half-timber beams, the projecting gable, the roof, the black pendant lantern, the bare winter tree or the sky.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame, and nobody leaves. No cars and no pets enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, the odd loose clap, boots on wet tarmac, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C08 on disk (1)**

#### Image prompt — `starting_frames/v35_c08_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `cbd75703-07a7-4b2d-8dc1-7e4969d83bac`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_175637_cbd75703-07a7-4b2d-8dc1-7e4969d83bac.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_33_assets/starting_frames/v33_c06_g2.png` · Higgsfield media `08a6fdc9-6e1f-475c-a1ad-4a5740d54085`
- @Image 2: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `40058517-9846-48c1-88e3-d48519a63b52`

````text
A real iPhone photo, vertical 9:16, shot outdoors at NIGHT on a suburban driveway.

COPY THE COMPOSITION OF REFERENCE IMAGE 1 EXACTLY — THIS IS THE MOST IMPORTANT INSTRUCTION. Reproduce its camera position, its framing, its proportions and above all WHERE THE LIGHT CURTAIN HANGS. Change only the house and the picture shown in the lights.

WHERE THE CURTAIN HANGS — CRITICAL. The light curtain hangs across the DOUBLE GARAGE DOOR and nowhere else. It completely fills the garage door opening: one clean bright rectangle, noticeably wider than it is tall, sitting squarely inside the garage door frame, its top edge tucked right under the garage lintel and its left and right edges running all the way out to the door jambs, its bottom edge reaching down to the driveway behind the heads of the crowd. The garage door opening is entirely covered by the lit curtain, edge to edge, corner to corner. The curtain is NOT on the gable above, NOT on the upper wall, NOT on the roof, NOT floating in the middle of a blank wall — it is ON THE GARAGE DOOR, exactly as in REFERENCE IMAGE 1.

THE HOUSE — same layout as REFERENCE IMAGE 1 but a DIFFERENT house: CREAM STUCCO with dark chocolate-brown TUDOR HALF-TIMBER BEAMS crossing the projecting gable above the garage, a small black pendant lantern hanging in the peak, a warm lit leaded window off to the left, and a bare winter tree at the right edge. Snow on the ground. NOT clapboard, NOT yellow, NOT blue, NOT green.

THE FOREGROUND — exactly as in REFERENCE IMAGE 1. A group of neighbours in winter coats and bobble hats stands in the near foreground with their BACKS to the camera, in dark silhouette, watching the display. Their heads and shoulders fill the bottom third of the frame at a range of heights, adults and children together. The snowy driveway between them and the garage is wet and glossy and throws a long smeared multicoloured reflection of the lit curtain back toward the camera.

CRITICAL — HOW THE LIGHTS ARE BUILT. This is NOT an LED video wall, NOT a TV screen, NOT a projection, NOT a printed banner. It is a hanging curtain of string lights: many separate thin BLACK wires hung close together side by side from a header cable under the lintel, each wire carrying a close-spaced run of small round bulbs. The picture is built from VERTICAL DOTTED LINES OF LIGHT — the horizontal gap between neighbouring strands is a little wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular rather than a square matrix. The individual bulbs are clearly countable across the whole curtain, exactly as in REFERENCE IMAGE 1, and every lit bulb is a point source with a blown-out white core, a coloured halo and a small soft star flare. The strands sag slightly and the bottom hem is uneven and wavy.

HOW DETAILED AND BEAUTIFUL THE PICTURE IS — THE MOST IMPORTANT INSTRUCTION. This is a PREMIUM, EXPENSIVE, PROFESSIONALLY DESIGNED commercial Christmas light display, and the artwork must look it. The bulb grid is FINE and HIGH RESOLUTION — many hundreds of small bulbs across the width — so the characters are richly and skilfully drawn: proper expressive faces with real eyes, eyebrows and open mouths, confident clean outlines, folds and shading in the fabric, fur trim that actually reads as soft fur, highlights and shadow giving the figures roundness and volume, smooth flowing curves in the arms and body. Gorgeous, polished, eye-catching artwork. It is absolutely NOT a crude blocky 8-bit pixel sprite, NOT jagged, NOT clumsy, NOT a chunky Minecraft or cross-stitch chart, NOT low resolution, NOT a child's drawing.

THE BACKGROUND INSIDE THE CURTAIN — exactly like REFERENCE IMAGE 1: a soft, even, gently graded wash of pastel blue, violet and pink light filling the rectangle behind the characters, with the white grid of bulbs reading through it. It is a clean colourful backdrop, NOT a dirty grey haze, NOT a muddy fog, NOT a solid flat block of one colour.

BUILT TO BE ANIMATED — exactly TWO large characters and nothing else. NO crowd of little figures inside the lights, NO third character, NO confetti, NO dotted motion arcs, NO flying debris, NO speed lines, NO stars, NO floating hearts, NO scattered snowflakes. Each character is one clear shape, clearly separated from the other so you could trace its outline with a finger. Both are FULL FIGURES drawn head to foot at the same large size as each other. The joke reads from a held physical force in their bodies, one frame before it gives way.

THE PICTURE IN THE LIGHTS — the candy-cane duel. Santa on the LEFT and the Grinch on the RIGHT face each other across the middle of the rectangle like fencers, each gripping a huge red-and-white striped CANDY CANE two-handed like a sword, the two canes crossed and locked hard against each other in the centre between them, both figures leaning in with their front knee bent deep and their back leg braced straight behind, weight thrown forward, straining. Santa is in a deep saturated red coat with white fur trim, a white beard, a black belt and big black boots, teeth gritted, one eye squeezed shut with effort. The Grinch is a tall vivid lime-green figure in a red Santa hat and a red coat, leaning in just as hard, mouth wide open in a snarling grin. Held exactly one frame before one of them gives way.

BOTH CHARACTERS SIT WHOLLY INSIDE THE RECTANGLE. Together they fill about two thirds of the height of the curtain rectangle, with a clear margin of background all the way around — heads well below the top edge, boots well above the bottom edge, and neither figure touching, crossing or overhanging the left or right edge. Nothing spills onto the garage frame, the stucco, the timber beams, the lantern, the sky or the driveway.

ABSOLUTELY NO text, letters, numbers, words or writing anywhere in the lights or anywhere else in the photograph.

COLOUR IS THE POINT. Santa's coat is a deep saturated red with brilliant white fur trim, the Grinch is a vivid lime green, the two candy canes are bright red and white, and the background wash is pastel blue, violet and pink. Use REFERENCE IMAGE 2 ONLY as a guide to how finely and richly bulb artwork can be drawn — do NOT copy its subject matter and do NOT copy its single-colour warm-white palette.

Fully clothed cartoon figures, a silly slapstick pose and nothing more. No nudity, no bare skin beyond the green cartoon arms and face.

IMAGE QUALITY: a real photograph shot on a modern iPhone, tack sharp across the whole frame, every bulb crisply resolved, correct exposure, natural night colour, fine natural sensor grain. NOT blurry, NOT soft, NOT hazy, no motion blur, no heavy bloom, no vignette, no shallow depth of field, no colour grading, no CGI or 3D-render look, no illustration, no painting.
````
