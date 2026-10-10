# Video 30 — The chimney cork

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_30.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

**Historical initial stage:** start frames only. No clips yet, no hook shot.
**Scope:** B-roll only, the same six shots as v20 – v29 — C02 … C07.
**Date:** 2026-09-15
**Model:** `gpt_image_2` · aspect `9:16` · resolution `2k` · quality `medium` · `use_unlim false` · `count 1`
**Output:** 1520 × 2688 PNG, one generation per shot, no re-rolls.

Daniel's brief for this one:

> Now generate me the Broll for video 30 and 31. For these 2 I want funnyer animations, more engaging, also keep in mind that in the next step we need to animate them. They must look very interesting and engaging

Asked what the gag should be, he answered **"be creative"** — the choice was delegated. Asked whether C2 – C4 should change, he answered **"Keep as-is"**: straight v29 format, new cast and a new house, nothing else. **All the comedy lives in C5 – C7.**

Because the next step is animation, both new gag runs were designed around a single test: *looking at the still, can you tell exactly what the next second of motion is?* Every beat is built from a held physical force — strain, topple, launch — plus in-frame motion cues the model can actually draw: dotted trajectory arcs, speed lines, skid puffs, objects caught mid-air, snapped rope ends.

**The gag — the chimney cork**, a three-beat story across C5 → C6 → C7:

| Beat | Shot | What happens | What animates next |
|---|---|---|---|
| 1 | C05 | Santa has gone down the chimney head-first and is wedged; only his legs stick out, kicking, one boot already flying off. Two elves on the roof, one laughing, one horrified. | The legs thrash, the boot lands. |
| 2 | C06 | A rope is knotted round his ankles and runs bar-tight across the whole picture to three elves and four reindeer leaning back at a steep angle, heels dug in, one elf already yanked off his feet. Presents tumbling loose. | The rope strains a beat longer, then gives. |
| 3 | C07 | He fires out like a cork — upside down mid-air, arms and legs splayed, both boots gone, beard streaming up, a starburst behind him. The rope has snapped; the whole team lies flat on their backs in a heap. Presents rain down. | Everything falls. |

---

#### The v30 look

**The woman (C2, C3)** — late twenties, warm olive skin, DARK CHOCOLATE-BROWN hair in a loose low bun with a few face-framing strands escaping.
Indoors: cream cable-knit cardigan over a white tee, charcoal-grey soft joggers.
Outdoors: forest-green puffer parka with a faux-fur trimmed hood, black jeans, mustard-yellow beanie, black boots.

**The room (C2)** — pale grey-washed oak wide-plank floor, deep navy velvet sofa with blush-pink and cream cushions and a cream chunky-knit throw, warm white shiplap wall behind, brass arc floor lamp curving over from the left, slim real green spruce with red-and-white candy-cane striped baubles and warm white lights at the right.

**The house (C3, C4 — the same building)** — two-storey family home with an attached garage wing. **Soft sage-green lap siding**, crisp white trim, soft white sectional double garage door with recessed panels and a row of small square windows across the top, black coach lanterns, white gutter and downpipe, charcoal-grey roof, covered porch on white posts, **navy-blue front door**, concrete driveway with patchy snow.

**The showcase houses** — C5 brick-red painted clapboard two-storey with white trim and a charcoal roof; C6 terracotta red brick with a **deep forest-green** double garage door; C7 dark olive-green board-and-batten gable with cream trim and a cherry-red station wagon at the kerb.

**Carried over, unchanged** — the curtain wire is **BLACK** with dark unlit bulbs; the lit curtain is always **separate hanging vertical strands with dark gaps, never an LED panel**; the artwork stays inside the curtain rectangle; **absolutely no text** anywhere in the lights; every prompt closes on the explicit sharpness block.

**New for v30/v31** — the **"COLOUR IS THE POINT"** paragraph is now in **all three** lit shots, not just C6. v29's open points recorded that C5 and C7 came out thin on colour precisely because only C6 carried it.

---

#### References used

| Ref | Media / job id | What it was passed for |
|---|---|---|
| v20 C2 frame | `05989e1b-228c-432a-be58-a51cfbfa19ad` | C2 geometry — sofa **in front of her**, running diagonally into depth |
| v29 C2 frame | `07ebb15c-1e14-4ef7-b576-b0f4210e0c5b` | C2 camera height — shoulder height, only a slight downward tilt |
| v29 C3 g2 frame | `46b340e4-6caf-44c9-aa30-cc219dfe59a6` | C3 **close side-on** camera, the step-stool pose, the black wire |
| v29 C4 g6 frame | `a6bcff66-91f5-4629-be28-3ba99b78c3a7` | C4 approved close square-on framing, night light, the iPhone + 2-column app |
| v29 C5 frame | `0f0bd301-46da-449b-a256-fc8baa127215` | C5 framing — same camera, same lit span |
| v29 C6 frame | `63a2e39f-ba00-457e-b1d2-0302fbe6c6e2` | C6 camera, house-with-garage-door framing, crowd in silhouette |
| v29 C7 frame | `40058517-9846-48c1-88e3-d48519a63b52` | C7 framing — shooting out through the car side window |

---

#### Continuity chain

```
v20 C2 + v29 C2 job       ->  C2   (geometry + camera height)
v29 C3 g2 + new C2 job    ->  C3   (close side-on camera/pose/black wire + THE WOMAN)
v29 C4 g6 + new C3 job    ->  C4   (approved framing + iPhone/app + THE HOUSE, now at night)
v29 C5                    ->  C5   (standalone)
v29 C6                    ->  C6   (standalone)
v29 C7                    ->  C7   (standalone)
```

**Deliberate change from v29's C4:** in v29 the C4 reference frame owned both the framing *and* the house, and the siding colour drifted to cream across three separate prompts. Here the refs are split — ref 1 owns the framing, **ref 2 (the new C3 job) owns the house** — plus an explicit `DO NOT COPY THE SIDING COLOUR OR THE FRONT DOOR COLOUR FROM THE FIRST IMAGE` clause and a positive colour assertion.

---

## C02 — Box over the sofa

Refs: v20 C2 frame (geometry) + v29 C2 job (camera height).

**Frame:** `v30_c02_g1.png`

### Image prompt

```
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. The box is a closed rigid printed gift box with NO transparent window and NO cut-out panel anywhere on it. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: a late-twenties woman with warm olive skin and DARK CHOCOLATE-BROWN hair worn in a loose low bun with a few face-framing strands escaping, wearing a CREAM CABLE-KNIT CARDIGAN over a white tee and CHARCOAL-GREY soft joggers. The room has a PALE GREY-WASHED OAK wide-plank floor, a DEEP NAVY VELVET sofa with blush-pink and cream cushions and a cream chunky-knit throw, a WARM WHITE SHIPLAP wall behind, a BRASS ARC floor lamp curving over from the left, and a slim REAL GREEN SPRUCE Christmas tree hung with red-and-white candy-cane striped baubles and warm white lights standing at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the knit of her cardigan and in the print on the box, clean even indoor light with no blown highlights and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur on the box or on her, NO grain, NO haze, NO soft focus anywhere. Candid UGC, no text overlay, no watermark.
```

---

## C03 — Mounting on the attached garage, day

Refs: v29 C3 g2 frame (close side-on camera, pose, black wire) + **v30 C2 job** (the woman).

**Frame:** `v30_c03_g1.png`

### Image prompt

```
COPY THE CAMERA OF THE FIRST ATTACHED IMAGE EXACTLY - its position, its angle, its height, its closeness and her pose. This is a CLOSE, SIDE-ON shot, not a wide frontal shot.

THE CAMERA IS CLOSE AND OFF TO ONE SIDE, exactly as in the first image: the camera stands near the wall and slightly behind her at roughly waist height, looking ALONG the wall, so the wall runs away from the camera DIAGONALLY - nearest at the bottom-left of the frame and receding to the right, the roof gutter line along the top sloping down towards the right as it goes away, strong oblique one-point perspective. She fills most of the frame height in the right half, her whole body in shot from her boots on the stool up to her raised hands. MUCH CLOSER than a full-house shot: only a short run of the wall is in frame, no full facade, no wide establishing view, no flat square-on frontal view.

HER POSE - copy it from the first image: she stands on a small BLACK two-step folding step stool, seen from BEHIND and slightly to the side, facing the wall, both arms raised in front of her, her hands up at the trim board along the top of the wall as she presses the LED curtain into place. Her weight is on one foot, her back slightly arched.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Long vertical strands of thin BLACK cord with small DARK unlit bulbs hang down the wall to the left of her, and because the camera is close the strands are big in the frame and clearly readable as separate cords. A BIG LOOSE TANGLE of BLACK cord is heaped on the snow at the foot of the stool, spilling out to the left - a real messy nest of wire, obviously dark against the white snow, exactly like the bundle in the first image. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - TAKE HER FROM THE SECOND ATTACHED IMAGE. Same late-twenties woman with warm olive skin and DARK CHOCOLATE-BROWN hair, now worn in a low bun spilling out from under a MUSTARD-YELLOW beanie, wearing a FOREST-GREEN puffer parka with a faux-fur trimmed hood, BLACK jeans and BLACK boots. It must read as literally the same person as in the second image.

A COMPLETELY NEW HOUSE - take it from this text only, NOT from either attached image. The wall she is working on is the WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR of a two-storey family home - soft WHITE with horizontal panel seams and recessed rectangular panels running away in perspective, and the row of small square windows across the top of the door visible at the far end. Around it, SOFT SAGE-GREEN lap siding with crisp WHITE trim, a BLACK COACH LANTERN on the wall, a WHITE gutter and WHITE downpipe, a charcoal-grey roof, and a plain CONCRETE driveway under patchy snow. At the RIGHT of the frame, further away, the corner where the garage wing meets the MAIN HOUSE BODY is visible - the two-storey wall, the covered porch on white posts and the NAVY-BLUE front door - so it reads as ONE house with the garage built into it.

DO NOT COPY THE HOUSE FROM THE FIRST IMAGE: not its warm sand-beige or cream siding, not its dark red front door. The first image is there ONLY for the camera, the distance, the angle, the pose and the black wire.

Daytime, overcast winter light, snow on the ground.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the door panels, the quilting of her parka and every strand of black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

---

## C04 — Phone POV, the same house at night

Refs: v29 C4 **g6** frame (the approved framing, night light, iPhone + app) + **v30 C3 job** (the house).

**Frame:** `v30_c04_g1.png`

### Image prompt

```
COPY THE FIRST ATTACHED IMAGE'S CAMERA, FRAMING, DISTANCE, ANGLE AND FOREGROUND PHONE EXACTLY. Night, square-on frontal view of a double garage door, a phone held up big in the bottom-centre foreground. ONE THING CHANGES: it is a DIFFERENT HOUSE, taken from the second attached image.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. The camera is close to the house so the GARAGE DOOR IS BIG AND DOMINATES THE FRAME, spanning almost the full width of the picture with only a NARROW STRIP of white trim and siding visible beyond its left edge and beyond its right edge, only a SHALLOW BAND of siding above its top edge, and only a LOW STRIP of snowy concrete driveway beneath it. But the ENTIRE DOOR STAYS VISIBLE: both vertical side edges inside the frame, the complete top edge inside the frame including the WHOLE row of small square windows running all the way across it with every window visible end to end, and the bottom edge where the door meets the driveway inside the frame. Nothing about the door is cut off by any edge. Do NOT step closer and do NOT step back.

STILL SQUARE-ON FROM THE FRONT: the door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up, NO whole house, NO full facade, NO roofline.

THE HOUSE - TAKE IT FROM THE SECOND ATTACHED IMAGE, NOT FROM THE FIRST. It must read as LITERALLY THE SAME HOUSE as the second image, now seen square-on from the front at night: the same soft WHITE sectional double garage door with its recessed panels and its row of small square windows, and around it SOFT SAGE-GREEN lap siding with crisp WHITE trim, BLACK COACH LANTERNS glowing warm on the wall either side of the door, a WHITE gutter, and at the right edge a sliver of the covered porch on its white post with the NAVY-BLUE front door cropped by the frame. The siding must read clearly as a soft muted SAGE GREEN - NOT cream, NOT white, NOT beige, NOT grey - and visibly different in colour from the white door and the white trim.

DO NOT COPY THE SIDING COLOUR OR THE FRONT DOOR COLOUR FROM THE FIRST IMAGE. The first image is there ONLY for the camera, the framing, the night lighting and the phone.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the door in evenly spaced vertical see-through strands right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale door each strand reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen.

THE PHONE AND ITS SCREEN ARE UNCHANGED - COPY THEM EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same hand, same grip, same angle, same size and same position in the bottom-centre foreground. The screen shows the SAME APP: a dark navy-blue screen with a grid of just TWO COLUMNS of large tiles, two across and about five down, roughly ten tiles in total and no more, each tile nearly half the screen wide with softly rounded corners and a narrow gutter, each one a small photograph of a house decorated in Christmas lights - a lit roofline, a nativity, a snowman, a reindeer, a porch draped in light curtains - mostly icy blue and cool white with a couple of warm tiles, ONE tile ringed with a bright electric-blue outline, and a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE below the grid. NOT a dense grid of tiny icons, NOT three or more columns, NO glyphs or pictograms, and NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

The phone is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

---

## C05 — Lit facade — Santa stuck in the chimney

Ref: v29 C5 frame.

**Frame:** `v30_c05_g1.png`

### Image prompt

```
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a BRICK-RED painted clapboard two-storey with crisp white trim, white window frames and a charcoal-grey roof, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: SANTA IS STUCK IN THE CHIMNEY. In the middle of the lit area sits a fat BRICK CHIMNEY drawn in red and orange bulbs with a chunky stone cap. Santa has gone in HEAD-FIRST and is wedged: only his RED TROUSERS, his BLACK BELT with a big gold buckle and his two LEGS stick straight up out of the chimney mouth, kicked wide apart in a V, both boots mid-kick, ONE BLACK BOOT FLYING OFF above him with a red-and-white striped sock underneath. A puff of grey soot bursts out around his waist. Two chunky curved motion arcs sweep from each kicking boot to show them thrashing.

STANDING ON THE ROOF EITHER SIDE OF HIM: on the LEFT a GREEN ELF doubled over laughing, one hand on his belly, the other pointing straight at Santa's legs, mouth wide open. On the RIGHT a second elf in a blue coat with both hands on his cheeks and two huge round white eyes, and a tipped-over SACK spilling brightly coloured presents down the roof slope. A few gold stars and snowflakes scattered around. The whole scene is one piece of light art on the wall.

3. Different foreground: a low snow-capped STONE WALL along the bottom left and a shovelled path with a snowbank either side leading to the house.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated across the picture. The presents especially must be many different bright colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole picture sits within the curtain rectangle with a clear band of dark unlit wall above it, below it and at both sides. Santa's kicking boots and the flying boot do not touch the top edge, the stone wall and the spilled presents do not touch the bottom edge, and neither elf touches the side edges. Nothing lit appears on the roof, the trim, the sky or the window frames.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the brick-red clapboard wall behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the clapboard texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

## C06 — Garage door + crowd — the tug-of-war

Ref: v29 C6 frame.

**Frame:** `v30_c06_g1.png`

### Image prompt

```
Same shot as the attached image - same camera, same distance, same house-with-attached-double-garage-door composition, same crowd of onlookers in silhouette along the bottom, same snow, same night. Keep the camera and the staging EXACTLY.

CHANGE TWO THINGS ONLY:

A) THE HOUSE COLOURS: the house is now TERRACOTTA RED BRICK with white trim, and the wide double garage door is DEEP FOREST GREEN with white panel edges, instead of the colours in the reference.

B) THE PICTURE IN THE LIGHTS - throw it away completely and replace it with a much funnier, much wilder and MUCH MORE COLOURFUL cartoon scene, drawn chunky and simple out of the bulbs and filling the lit area fully.

THE NEW SCENE - A TUG-OF-WAR TO PULL SANTA OUT OF THE CHIMNEY:

On the FAR RIGHT of the lit area stands a fat BRICK CHIMNEY in red and orange bulbs. Santa's RED TROUSERS, BLACK BELT and two LEGS stick straight up out of it, stretched long and thin like elastic, both boots pointing at the sky, a puff of grey soot around his waist.

A thick ROPE is knotted round his ankles and runs in a dead straight, bar-tight diagonal all the way ACROSS THE PICTURE to the LEFT, with a couple of frayed strands popping off it. STRUNG ALONG THAT ROPE, ALL LEANING BACK AT A STEEP ANGLE, HEELS DUG IN: first THREE GREEN ELVES in different coloured coats - hot pink, turquoise, yellow - gripping the rope with both hands, teeth gritted, one with his hat over his eyes; then behind them FOUR REINDEER in a line, front legs braced, back legs skidding, bodies tilted right back, the front one with a BIG BRIGHT RED GLOWING NOSE. Little white spray puffs burst from under every skidding boot and hoof.

CHAOS AROUND THEM: six or seven PRESENTS knocked loose and tumbling through the air, each a DIFFERENT BRIGHT COLOUR - emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow, two of them burst open with little coloured shapes spilling out. One elf has been yanked clean off his feet and is flying horizontally along the rope. Curved multicoloured speed lines streak behind the tumbling presents, and bright stars in many colours are scattered right across the lit area so almost none of it is empty.

COLOUR IS THE POINT: this is a loud multicoloured light show - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated. It must NOT be mostly one or two colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit door above it, below it and at both sides. Nothing lit appears on the brickwork, the roof, the sky, the hedge or the snow.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the forest-green garage door behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the brick texture of the house and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

## C07 — Car-window POV — he pops like a cork

Ref: v29 C7 frame.

**Frame:** `v30_c07_g1.png`

### Image prompt

```
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a DARK OLIVE-GREEN board-and-batten gable with cream trim and cream window frames, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: SANTA POPS OUT OF THE CHIMNEY LIKE A CORK. High in the upper half of the lit area SANTA is blasting UPWARD out of a fat brick chimney, flipped UPSIDE DOWN in mid-air, arms and legs splayed out wide like a starfish, mouth wide open in a big round O, eyes as two white circles, his red hat gone and his white beard streaming straight up past his face, both boots off and tumbling separately. A big chunky multicoloured STARBURST of straight rays fires out behind him. A ring of grey soot puffs and loose orange BRICKS bursts outward from the chimney mouth below him.

BELOW, THE ROPE HAS SNAPPED: two frayed rope ends whip apart in opposite curls, and along the bottom of the picture the whole pulling team lies FLAT ON THEIR BACKS in a heap - THREE GREEN ELVES and FOUR REINDEER piled over each other, legs and hooves sticking straight up in the air, one elf with a present landed on his face. PRESENTS RAIN DOWN across the whole scene, eight or nine of them, each a DIFFERENT BRIGHT COLOUR - emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow, two burst open. Small gold stars scattered around. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

3. A different parked car at the kerb - a CHERRY-RED station wagon instead of the car in the reference - and a snow-covered hedge at the right edge.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit gable above it, below it and at both sides. Santa and the starburst do not touch the top edge, the pile of elves and reindeer does not touch the bottom edge, and nothing touches the side edges. Nothing lit appears on the roof, the trim, the window frames or the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the olive-green gable behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the board-and-batten texture and the wet road reflections clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

#### Generated set

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v30_c02_g1.png` | C02 | `a343259f-829e-4107-a3a8-cb9f230d5330` | 300201 | completed, first attempt |
| `v30_c03_g1.png` | C03 | `902719cb-1aab-412f-be53-6ef675c7d164` | 300301 | completed, first attempt |
| `v30_c04_g1.png` | C04 | `cee3d830-2bd2-4fbb-ae8b-bdf089de8d6b` | 300401 | completed, first attempt |
| `v30_c05_g1.png` | C05 | `591509cb-6d53-4c2e-b49b-e9df334698be` | 300501 | completed, first attempt |
| `v30_c06_g1.png` | C06 | `f5e27666-14d4-4e32-a6e1-b630a8866728` | 300601 | completed, first attempt |
| `v30_c07_g1.png` | C07 | `24b2cf14-ccee-43ca-90bc-8066b7dbc684` | 300701 | completed, first attempt |

All six 1520 × 2688 RGB PNG, downloaded from the result URLs into `starting_frames/`.

---

#### Submission notes

- Workspace **Oneofone1** (`b2c97bd7-fedf-489d-b211-3de4e39dc90a`).
- Submitted in three waves to respect the chain: the eight independent jobs first (both C2s and all six lit shots for v30 + v31 together), then both C3s off their C2 jobs, then both C4s off their C3 jobs.
- `medias[].role` for `gpt_image_2` is **`image`**. `medias[].value` accepts either a media UUID or a **prior job id**.
- None of the known failure modes fired: no `declined_preset_id` resubmission, no "Preset was recommended instead", no `ip_detected`. All twelve v30 + v31 jobs completed on the first attempt.

---

#### Open points for review

- **C04's siding rendered pale grey-white, not sage green.** The split-reference fix plus the explicit DO-NOT-COPY clause did not hold — this is the fourth prompt in a row where the C4 siding colour has drifted towards cream regardless of what the text says. C03 got the sage green right, so the drift is specific to the night C4 chain. Worth trying a different lever next time: generate C4 *first* off C3 alone with no v29 framing reference, or state the siding colour before the framing block rather than after it.
- **C06's curtain reads as a dense mosaic rather than separate strands.** The "never a screen" block is present and was ignored — it is the busiest of the three gag scenes, and the strand gaps get filled in when the artwork covers the whole rectangle. C05 and C07 both hold the strand look cleanly. If Daniel wants C06 matched to the other two, the fix is to thin the artwork, not to add more words to the curtain block.
- **C06 also loses the deep forest-green garage door** — the curtain covers it edge to edge, so the colour change is effectively invisible. Same in v31 C06.
- Everything else lands: the three-beat gag reads in sequence, C07 is the strongest frame of the set, C02/C03 hold the same woman, C03/C04 hold the same house geometry, the wire is black throughout, no text anywhere in the lights.

No re-runs were made. One generation per shot, then review.

---

## C01 — HOOK — security camera, man taping an inflatable to the house

**Frame:** `starting_frames/v30_c01_g1.png` (1520 x 2688)
**Job id:** `6740da09-550f-479b-9c08-57d5da20c03f`
**Model:** gpt_image_2 · 2k · quality medium · 9:16 · 1 generation
**References:** Daniel's security-cam ladder screenshot (`c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e`) — camera, lens, composition, location. No product in this hook by design: it is the pain-point / "there is an easier way" contrast shot.

**Prompt**

Reproduce the attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a HOUSE SECURITY CAMERA. Keep the same suburban American street, the same late-afternoon winter light, the same mood.

THE CAMERA - copy it from the attached image: a security camera bolted high under the eaves at the front corner of a house, well above head height, looking DOWN and OUT at a steep angle across the front yard and the driveway toward the street. Wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Fixed, static, unmanned, elevated viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE ATTACHED IMAGE, just re-stacked for a vertical frame:
- LEFT EDGE: the RED BRICK wall of the camera's own house in extreme close foreground, seen sharply along its length so the courses of brick and mortar run away from the lens in steep perspective, filling a tall vertical band down the whole left side of the frame.
- BOTTOM RIGHT FOREGROUND: the white roof and windscreen of a car parked close under the camera, cut off by the bottom corner of the frame, catching a hard highlight.
- CENTRE: the front lawn of the house - winter grass, a low planting bed with a string of unlit coloured lights along its edge, a slim young tree.
- MIDDLE DISTANCE: a concrete driveway with a WHITE SALOON CAR parked on it, and the neighbouring two-storey houses with pale render and stone bases and WHITE DOUBLE GARAGE DOORS.
- RIGHT: the road running away through the frame, kerbs, pavements, and more houses with garages on the far side.
- TOP: the eaves and roofline of the camera's own house, and a wide sky above the rooftops.

THE MAIN ACTION, in the middle of the frame on the lawn - exactly where the ladder stands in the attached image:

A TALL ORANGE-RED ALUMINIUM STEP LADDER is set up on the grass right against the front wall of the house. A MAN is standing high up on it, near the very top steps, in a dark navy hoodie, blue jeans and brown boots, seen from BEHIND AND ABOVE because of the camera angle - his face is not visible to the camera. He is stretched up and leaning in toward the wall with BOTH ARMS RAISED above his head, pressing a strip of SILVER DUCT TAPE onto the render with one hand while the other hand holds the thing he is taping up. His weight is off-centre, one heel lifted off the rung, the ladder tilted very slightly - it obviously should not hold.

WHAT HE IS TAPING UP: a BIG INFLATABLE CHRISTMAS DECORATION - a fat inflatable SNOWMAN about the height of a man, white with a black top hat, a red-and-green scarf and a carrot nose, fully inflated and bulging, being held flat against the house wall and stuck there with criss-crossed strips of silver duct tape across its belly and hat. It is far too big and far too round to be taped to anything, and one taped corner is already peeling away from the wall.

ON THE GROUND AT THE FOOT OF THE LADDER: a WOMAN in a teal-green fleece and black leggings stands steadying one leg of the ladder with both hands, looking up, plus a second smaller inflatable - an inflatable SANTA - lying half-deflated on its side on the grass with its power cable trailing, and a roll of duct tape and a pair of scissors dropped on the lawn beside it.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour security-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork of the foreground wall, in the fabric of the inflatable snowman and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun raking in from the side, long real shadows from the ladder and the man across the grass, bright but properly exposed - no blown-out white on the render or the car roof, no crushed black in the shadow under the eaves, correct white balance. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.


---

## C04 revision — 2026-09-16

Daniel's brief:

> C4 - I just want denser led lines on the garages
>
> Also when we try to animate this shot most of the times it's completly going wrong [...] Let's create an intermediate image with the animation that we will add as reference alongside with the starting frame when we generate the clip. Here is how it should look: exact same framing, hand and phone out of the frame, camera just a little upper (because it's a held iphone shot and the person filming tilts up the camera a little bit so the focus it's on animation), and an animation on the leds like the one in C7 in terms of how it looks, but different animation, the animation must be visible on the entire garage door

Two new frames for this shot. **`v30_c04_g2.png` replaces `v30_c04_g1.png` as the start frame.**

Asked what the animation should be, he answered **"be creative, it must be something funny"** — the scene was delegated again, one unique scene per video. Asked how much denser, he chose **roughly double**.

### Why the second image exists

C04 is the shot that keeps breaking in animation, and the break is always on the garage door — the model has to invent the lit artwork from nothing while also holding the phone, the hand and the door geometry, and it invents something different every attempt. So the lit end state is now **generated as a still first** and passed to the video model as a second reference. At clip time both images go in: `v30_c04_g2.png` is the **start frame**, `v30_c04_r1.png` is the **second reference** — the target the lights resolve to. The clip is then only a lights-on transition plus the small handheld tilt up, not an invention.

The animation frame is deliberately **not** a valid start frame on its own: the hand and phone are gone and the camera has tilted up, because that is where the shot ends, not where it begins.

### C04 g2 — denser strands

Ref: **v30 C4 g1 job** (`cee3d830-2bd2-4fbb-ae8b-bdf089de8d6b`) — the whole approved shot. One thing changes: roughly double the strand count.

**Frame:** `v30_c04_g2.png`

#### Image prompt

```
COPY THE ATTACHED IMAGE EXACTLY. Same house, same soft white sectional double garage door, same siding, same white trim, same black coach lanterns glowing warm either side, same snowy concrete driveway, same night light, same camera, same framing, same distance, same square-on angle, same foreground hand holding the same iPhone in the bottom-centre with the SAME two-column app grid and the same round blue play button. Everything is already correct and must be reproduced unchanged.

ONE SINGLE THING CHANGES: THE LED CURTAIN HAS ROUGHLY TWICE AS MANY STRANDS. In the attached image the vertical strands hanging over the garage door are spaced widely apart. Here they are packed about TWICE AS CLOSE TOGETHER - roughly double the number of strands across the same width, so the curtain reads as a much DENSER set of vertical lines running down the whole face of the door.

THE STRANDS THEMSELVES ARE UNCHANGED: each one is still a thin BLACK cord carrying small DARK unlit bulbs, the lights are OFF with no glow, and against the pale door each cord reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. They still hang from the trim board above the door, still span the full width of the door edge to edge, still have a slight natural sag and a slightly uneven bottom hem.

STILL A CURTAIN, NEVER A PANEL - CRITICAL: even at double the density these are SEPARATE HANGING VERTICAL STRANDS with clear DARK GAPS between them, and the garage door behind is plainly visible through those gaps - the recessed panel seams and the row of small square windows across the top must still read clearly through the curtain. Do NOT close the gaps. Do NOT turn it into a solid LED panel, a flat screen, a mesh, a net, a grille or a fabric sheet. Do NOT add horizontal wires. The strands run straight up and down only.

THE FRAMING IS ALREADY CORRECT - DO NOT CHANGE IT. The garage door stays big and dominant, spanning almost the full width of the picture, with the ENTIRE door visible: both vertical side edges inside the frame, the complete top edge including the WHOLE row of small square windows end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT tilt. Still square-on from the front: the panel seams run dead level and the door edges run straight up and down.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every individual black cord clearly readable and clearly separated from its neighbours, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### C04 animation reference

Refs: **v30 C4 g2 job** (`3eb2aa97-ee05-4fcd-816e-5c6b1196c73e`) for the scene + **v30 C7 g1 job** (`24b2cf14-ccee-43ca-90bc-8066b7dbc684`) for the bulb-art drawing style only.

The scene is a **conga line** — Santa leading, three elves and three reindeer kicking in unison, the last elf booted out of frame, presents bouncing along the bottom. Built the same way as the C5–C7 gags: a held physical force plus in-frame motion cues (speed lines, dotted arcs, a figure caught mid-air) so the next second of motion is unambiguous from the still.

**Frame:** `v30_c04_r1.png`

#### Image prompt

```
TAKE THE FIRST ATTACHED IMAGE AS THE SCENE. Same house, same soft white sectional double garage door with its recessed panels and its row of small square windows across the top, same siding, same white trim, same black coach lanterns glowing warm either side of the door, same snowy concrete driveway, same night. Same camera, same lens, same distance, same square-on frontal angle. TAKE THE SECOND ATTACHED IMAGE ONLY FOR THE DRAWING STYLE OF THE LIGHTS - the way the cartoon is built out of small round coloured bulbs. DO NOT COPY THE SECOND IMAGE'S HOUSE, ITS GABLE, ITS CAR, ITS ROAD OR ITS SCENE. Only its bulb-art look.

THREE THINGS CHANGE FROM THE FIRST IMAGE:

1. THE HAND AND THE PHONE ARE GONE. There is nothing at all in the foreground. No hand, no arm, no sleeve, no phone, no screen, no glow from a screen. The bottom-centre of the frame is simply the empty snowy driveway. The whole garage door is completely unobstructed from edge to edge.

2. THE CAMERA HAS TILTED UP A LITTLE. This is a handheld iPhone shot and the person filming has tipped the phone up slightly so the lights fill the frame. The framing is otherwise identical - same distance, same square-on frontal angle, the door still faces the camera flat with its horizontal panel seams dead level and its vertical edges straight up and down - but the whole frame has shifted UP: there is now only a THIN sliver of driveway along the bottom edge, and a slightly DEEPER band of siding and trim above the top of the door. The ENTIRE garage door stays inside the frame: both side edges, the complete top edge with the WHOLE row of small square windows visible end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT turn it into a low angle looking up at the roofline, do NOT show the whole house.

3. THE LED CURTAIN IS SWITCHED ON AND SHOWING A BRIGHT CARTOON ANIMATION. The same dense curtain of closely spaced vertical strands hanging over the garage door, but now every bulb is lit and together they draw a picture.

THE PICTURE - A CONGA LINE, drawn chunky and simple out of the bulbs, running RIGHT ACROSS THE WHOLE GARAGE DOOR: SANTA leads at the LEFT, one knee up and one leg kicked out sideways, one arm thrown in the air, mouth wide open in a big round O, eyes as two white circles. Behind him, all holding the shoulders of the one in front and ALL KICKING THE SAME LEG OUT THE SAME WAY, comes a line of THREE GREEN ELVES and THREE REINDEER alternating, each one leaning back at the same jaunty angle, knees and hooves flung out. At the FAR RIGHT the last little elf has been kicked clean off his feet and is flying backwards through the air upside down, arms and legs splayed, his pointed hat coming off. Curved speed lines and small puffs trail behind the kicking legs. Along the bottom a row of bouncing PRESENTS hops after them, each a DIFFERENT BRIGHT COLOUR with a contrasting ribbon and bow. Small gold stars scattered through the gaps. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

THE PICTURE FILLS THE ENTIRE GARAGE DOOR: the conga line spans the FULL WIDTH of the door from its left edge to its right edge, and the figures plus the bouncing presents plus the stars fill the FULL HEIGHT of the door from just under the row of square windows down to the bottom edge. Every part of the door is covered by lit artwork - no large dark empty areas anywhere on the door, and nothing is confined to a small panel in the middle. Nothing lit appears above the door, on the trim, on the siding, on the lanterns or in the sky.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. The strands are densely spaced but there are still clear DARK GAPS between them and the white garage door behind is plainly visible through those gaps, especially in the unlit areas - the recessed panel seams and the row of square windows must still read through the curtain. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the garage door panels and the snowy driveway clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v30_c04_g2.png` | C04 start frame | `3eb2aa97-ee05-4fcd-816e-5c6b1196c73e` | 300402 | completed, first attempt |
| `v30_c04_r1.png` | C04 animation ref | `30de064d-6194-4348-b0ef-8239e7d07791` | 300421 | completed, first attempt |

Both 1520 × 2688 PNG. Workspace **Oneofone1**. One generation each, no re-rolls. No `declined_preset_id`, no preset recommendation, no `ip_detected`.

### Open points for review

- **The siding is still pale grey-white, not sage.** g2 was generated off g1, which carried the drift, and the brief was density only — so it was left alone rather than fixed unasked. Still worth a separate pass if it matters.
- **The animation frame pulled back very slightly** — a little more siding either side of the door than in g2. The tilt up and the door's position in frame are right; the distance is a touch off. Fine as a colour/artwork reference, worth a note if the clip inherits the wider framing.
- The conga line / snowball scene is one generation, unreviewed. If either scene is wrong, it is cheap to re-run — the prompt only needs its middle paragraph swapped.

### C01 — g2 (Daniel: "it's good but I want the persons closer to the camera")

**Frame:** `starting_frames/v30_c01_g2.png` · **Job id:** `fd525a02-0fd1-4401-96af-a94bcece53ed` · same model/params/ref as g1.

Base = the g1 prompt above with one block inserted and nothing else changed:

> THE ONE CHANGE FROM THE ATTACHED IMAGE - THE PEOPLE AND THE LADDER ARE MUCH CLOSER TO THE CAMERA. The ladder is set up on the grass only a couple of metres below and in front of the camera, right at the near corner of the house rather than further along it. The man on the ladder fills roughly the upper-left third of the vertical frame and the woman below him fills roughly a quarter of the frame height - they are the unmistakable subjects, big and close, not small figures in a wide yard. The camera is looking almost straight down onto them at a steep angle from just above. The street and the neighbouring houses are pushed well back into the upper right of the frame as background only.

The ladder/snowman/duct-tape action, the woman, the deflated Santa, the brick foreground and the car in the bottom-right corner are all unchanged.

### C01 — g3 (Daniel: "I want a little space at the top so when I add the text inside CapCut it will look good")

**Frame:** `starting_frames/v30_c01_g1.png` · **Job id:** `c75c3acb-accc-4683-998a-627e4f968854` · same model/params/ref as g2.

Base = the g2 prompt with a headroom block added at the very top, above everything else:

> COMPOSITION - CRITICAL, READ FIRST. The TOP QUARTER of the vertical frame is deliberately kept CLEAN AND EMPTY as headroom for a caption that will be added later. That top band contains ONLY open sky and the plain roofline of the houses - a wide, calm, uncluttered strip of pale winter sky with nothing important happening in it, no people, no ladder, no inflatable, no busy detail. All the action sits BELOW that band, in the middle and lower three quarters of the frame. Compose so that nothing you would hate to cover ever reaches into the top quarter.

The "people close to camera" block from g2 was kept but re-worded to push them DOWN: man + inflatable in the middle of the frame with the top of the hat clear of the empty band, woman in the lower third, brick wall starting below the band.

**Caption-safe zone: the top ~25% of the frame (roughly the first 670 px of 2688).**

### C01 — g4

Fix for Daniel's g3 note: *"now the people are too far away, I want just a little more space at the top than g2"*. g3's caption band was a full quarter of the frame and the subjects shrank to fill the rest. g4 restores g2's subject scale and cuts the band to roughly one eighth.

- Job id: `85107525-50b2-40fc-9bea-05d6720eadef`
- Model: gpt_image_2, 2k, quality medium, 9:16, count 1 → 1520x2688
- Refs: `c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e` (security-cam ladder screenshot)
- Output: `starting_frames/v30_c01_g4.png`

Changed blocks vs g3 (everything else identical):

> COMPOSITION - CRITICAL. The people and the ladder are CLOSE TO THE CAMERA and BIG in the frame - they dominate the picture, they are not small figures in a wide yard. The ladder is set up on the grass only a couple of metres below and in front of the camera, right at the near corner of the house. The man on the ladder and the inflatable he is taping fill roughly a third of the frame height. The woman below him fills roughly a quarter of the frame height. The camera looks almost straight down onto them at a steep angle from just above.
>
> The ONLY concession is a NARROW STRIP OF CLEAN SKY along the very top of the frame - about one eighth of the frame height, a calm uncluttered band of pale winter sky and plain roofline, left clear for a caption. Just a small margin of breathing room at the very top: the top of the inflatable snowman's hat and the eaves of the house sit just below that strip, not squeezed down into the middle of the picture. Do NOT shrink the people to make room, do NOT pull the camera back, do NOT leave a big empty upper half - only a slim clean band at the extreme top.

## C01 — CLIP (from v30_c01_g1.png)

Daniel's brief: *"Fix stable camera, for the first second the man tries to set up the inflatable christmas decorations then he falls to the ground, his wife is screaming."* He picked **g3** as the start frame, not g4.

- Job id: `8d3901e1-07ce-4072-b9bc-6552010652ee`
- Model: seedance_2_5, mode omni_reference, 720p, 9:16, 5s, generate_audio true, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`
- Start image: job `c75c3acb-accc-4683-998a-627e4f968854` (`starting_frames/v30_c01_g1.png`)
- Output: `clips/v30_c01_g1.mp4` (720x1280, 5.04s)

### Timeline

| time | beat |
|---|---|
| 0.0–1.4s | still up the ladder taping the inflatable snowman to the wall, smoothing tape, rising onto his toes to reach higher; wife holds the ladder leg, looking up |
| 1.4–2.4s | he stretches too far sideways, weight goes outside the ladder, the two far feet lift off the grass, he scrabbles at the render and finds nothing |
| 2.4–3.4s | ladder goes over, he comes down with it onto the lawn, arms flailing; the snowman rips free of its tape and flops down the wall after him; the tape roll flies |
| 3.4–4.2s | wife lets go, jumps back, hands to her face, head thrown back — screaming |
| 4.2–5.0s | he lies still a beat, knee bends, one arm to his chest; she rushes over and drops to a crouch beside him |

Same structural blocks as the V29 clip prompt: camera lock first (brick wall locked to the left edge, car roof locked bottom right, background treated as a still photograph), timed beats, PHYSICS block (the aluminium ladder is rigid and topples as one stiff object; the inflatable is light and bounces), BANNED list, LOOK block, AUDIO block — ladder rattle, thud on grass, rubbery flap of the inflatable, his short shout, then her loud sharp scream. No music.

---

## Board metadata (archived from board.meta.json, 2026-09-18)

**Final cut order** - the order the shots appear in the edit,
which is not always the order the cards sit in on the board.

```
C02 → C03 → C04 → C05 → C06 → C07
```

**Stats trimmed off the lane panel**

| field | value |
|---|---|
| Stage | Start frames |
| Frames | gpt_image_2 · 2k · medium |
| Takes | 1 generation each |


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v30_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v30_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v30_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v30_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v30_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v30_c06_g2.mp4` | Named derivative of `../v30_c06_g2.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v30_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v30_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v30_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v30_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v30_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v30_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v30_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v30_c06_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v30_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v30_c04_r1.png` | Embedded PNG `hf-job-id`: `30de064d-6194-4348-b0ef-8239e7d07791`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c01_g1.png` | Embedded PNG `hf-job-id`: `6740da09-550f-479b-9c08-57d5da20c03f`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c01_g2.png` | Embedded PNG `hf-job-id`: `fd525a02-0fd1-4401-96af-a94bcece53ed`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c01_g3.png` | Embedded PNG `hf-job-id`: `c75c3acb-accc-4683-998a-627e4f968854`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v30_c01_g4.png` | Embedded PNG `hf-job-id`: `85107525-50b2-40fc-9bea-05d6720eadef`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c02_g1.png` | Embedded PNG `hf-job-id`: `a343259f-829e-4107-a3a8-cb9f230d5330`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c03_g1.png` | Embedded PNG `hf-job-id`: `902719cb-1aab-412f-be53-6ef675c7d164`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c04_g1.png` | Embedded PNG `hf-job-id`: `cee3d830-2bd2-4fbb-ae8b-bdf089de8d6b`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c04_g2.png` | Embedded PNG `hf-job-id`: `3eb2aa97-ee05-4fcd-816e-5c6b1196c73e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c05_g1.png` | Embedded PNG `hf-job-id`: `591509cb-6d53-4c2e-b49b-e9df334698be`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c06_g1.png` | Embedded PNG `hf-job-id`: `f5e27666-14d4-4e32-a6e1-b630a8866728`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v30_c07_g1.png` | Embedded PNG `hf-job-id`: `24b2cf14-ccee-43ca-90bc-8066b7dbc684`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |

### Unresolved take records

The following 2 files still need exact take provenance or verified derivative lineage. Their presence is documented; their prompts have **not** been invented. MP4 C2PA manifest and instance IDs are authenticity identifiers, not Higgsfield job IDs.

- `clips/upscaled/v30_c06_g2.mp4`
- `clips/v30_c06_g2.mp4`

### Recovered take — `starting_frames/v30_c01_g3.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `c75c3acb-accc-4683-998a-627e4f968854`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
Reproduce the attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a HOUSE SECURITY CAMERA. Keep the same suburban American street, the same late-afternoon winter light, the same mood.

COMPOSITION - CRITICAL, READ FIRST. The TOP QUARTER of the vertical frame is deliberately kept CLEAN AND EMPTY as headroom for a caption that will be added later. That top band contains ONLY open sky and the plain roofline of the houses - a wide, calm, uncluttered strip of pale winter sky with nothing important happening in it, no people, no ladder, no inflatable, no busy detail. All the action sits BELOW that band, in the middle and lower three quarters of the frame. Compose so that nothing you would hate to cover ever reaches into the top quarter.

THE CAMERA - copy it from the attached image: a security camera bolted high under the eaves at the front corner of a house, well above head height, looking DOWN and OUT at a steep angle across the front yard and the driveway toward the street. Wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Fixed, static, unmanned, elevated viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE ATTACHED IMAGE, re-stacked for a vertical frame:
- LEFT EDGE: the RED BRICK wall of the camera's own house in extreme close foreground, seen sharply along its length so the courses of brick and mortar run away from the lens in steep perspective, filling a tall vertical band down the left side of the frame. It starts BELOW the empty top band.
- BOTTOM RIGHT FOREGROUND: the white roof and windscreen of a car parked close under the camera, cut off by the bottom corner of the frame, catching a hard highlight.
- CENTRE: the front lawn of the house - winter grass, a low planting bed with a string of unlit coloured lights along its edge, a slim young tree.
- MIDDLE DISTANCE: a concrete driveway with a WHITE SALOON CAR parked on it, and the neighbouring two-storey houses with pale render and stone bases and WHITE DOUBLE GARAGE DOORS.
- RIGHT: the road running away through the frame, kerbs, pavements, and more houses with garages on the far side.

THE PEOPLE AND THE LADDER ARE CLOSE TO THE CAMERA, but pushed DOWN into the lower two thirds of the frame. The ladder is set up on the grass only a couple of metres below and in front of the camera, right at the near corner of the house. The man on the ladder and the inflatable he is taping sit in the MIDDLE of the frame, with the top of the inflatable's hat comfortably clear of the empty top band. The woman below him is in the lower third. They are the unmistakable subjects, big and close, not small figures in a wide yard.

THE ACTION: A TALL ORANGE-RED ALUMINIUM STEP LADDER is set up on the grass right against the front wall of the house, close under the camera. A MAN is standing high up on it, near the very top steps, in a dark navy hoodie, blue jeans and brown boots, seen from BEHIND AND ABOVE because of the camera angle - his face is not visible to the camera. He is stretched up and leaning in toward the wall with BOTH ARMS RAISED above his head, pressing a strip of SILVER DUCT TAPE onto the render with one hand while the other hand holds the thing he is taping up. His weight is off-centre, one heel lifted off the rung, the ladder tilted very slightly - it obviously should not hold.

WHAT HE IS TAPING UP: a BIG INFLATABLE CHRISTMAS DECORATION - a fat inflatable SNOWMAN about the height of a man, white with a black top hat, a red-and-green scarf and a carrot nose, fully inflated and bulging, being held flat against the house wall and stuck there with criss-crossed strips of silver duct tape across its belly and hat. It is far too big and far too round to be taped to anything, and one taped corner is already peeling away from the wall.

ON THE GROUND AT THE FOOT OF THE LADDER, close to the camera: a WOMAN in a teal-green fleece and black leggings stands steadying one leg of the ladder with both hands, looking up, plus a second smaller inflatable - an inflatable SANTA - lying half-deflated on its side on the grass with its power cable trailing, and a roll of duct tape and a pair of scissors dropped on the lawn beside it.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour security-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork of the foreground wall, in the fabric of the inflatable snowman, in the weave of their clothing and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun raking in from the side, long real shadows from the ladder and the man across the grass, bright but properly exposed - no blown-out white on the render or the car roof, no crushed black in the shadow under the eaves, correct white balance. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e.png"
      }
    }
  ],
  "width": 1520,
  "height": 2688,
  "quality": "medium",
  "resolution": "2k",
  "model": "videotape-alpha",
  "remove_bg": false,
  "reference_elements": []
}
```



---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: clips byte-identical (md5) to their Higgsfield result unless the entry says otherwise, generated images by exact byte size, and every start frame checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C01: the board did not show the exact image prompt of `v30_c01_g3.png`; it now does.
- C01: the board did not show the exact clip prompt of `v30_c01_g1.mp4`; it now does.
- C02: the board did not show the exact clip prompt of `v30_c02_g1.mp4`; it now does.
- C03: the board did not show the exact clip prompt of `v30_c03_g1.mp4`; it now does.
- C04: the board did not show the exact clip prompt of `v30_c04_g1.mp4`; it now does.
- C05: the board did not show the exact clip prompt of `v30_c05_g1.mp4`; it now does.
- C06: the board did not show the exact clip prompt of `v30_c06_g2.mp4`; it now does.
- C07: the board did not show the exact clip prompt of `v30_c07_g1.mp4`; it now does.

### C01 — Ladder goes over on the front lawn

**In the cut:** `starting_frames/v30_c01_g3.png` → `clips/v30_c01_g1.mp4`

#### Image prompt — `starting_frames/v30_c01_g3.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `c75c3acb-accc-4683-998a-627e4f968854`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_235826_c75c3acb-accc-4683-998a-627e4f968854.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e`

````text
Reproduce the attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a HOUSE SECURITY CAMERA. Keep the same suburban American street, the same late-afternoon winter light, the same mood.

COMPOSITION - CRITICAL, READ FIRST. The TOP QUARTER of the vertical frame is deliberately kept CLEAN AND EMPTY as headroom for a caption that will be added later. That top band contains ONLY open sky and the plain roofline of the houses - a wide, calm, uncluttered strip of pale winter sky with nothing important happening in it, no people, no ladder, no inflatable, no busy detail. All the action sits BELOW that band, in the middle and lower three quarters of the frame. Compose so that nothing you would hate to cover ever reaches into the top quarter.

THE CAMERA - copy it from the attached image: a security camera bolted high under the eaves at the front corner of a house, well above head height, looking DOWN and OUT at a steep angle across the front yard and the driveway toward the street. Wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Fixed, static, unmanned, elevated viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE ATTACHED IMAGE, re-stacked for a vertical frame:
- LEFT EDGE: the RED BRICK wall of the camera's own house in extreme close foreground, seen sharply along its length so the courses of brick and mortar run away from the lens in steep perspective, filling a tall vertical band down the left side of the frame. It starts BELOW the empty top band.
- BOTTOM RIGHT FOREGROUND: the white roof and windscreen of a car parked close under the camera, cut off by the bottom corner of the frame, catching a hard highlight.
- CENTRE: the front lawn of the house - winter grass, a low planting bed with a string of unlit coloured lights along its edge, a slim young tree.
- MIDDLE DISTANCE: a concrete driveway with a WHITE SALOON CAR parked on it, and the neighbouring two-storey houses with pale render and stone bases and WHITE DOUBLE GARAGE DOORS.
- RIGHT: the road running away through the frame, kerbs, pavements, and more houses with garages on the far side.

THE PEOPLE AND THE LADDER ARE CLOSE TO THE CAMERA, but pushed DOWN into the lower two thirds of the frame. The ladder is set up on the grass only a couple of metres below and in front of the camera, right at the near corner of the house. The man on the ladder and the inflatable he is taping sit in the MIDDLE of the frame, with the top of the inflatable's hat comfortably clear of the empty top band. The woman below him is in the lower third. They are the unmistakable subjects, big and close, not small figures in a wide yard.

THE ACTION: A TALL ORANGE-RED ALUMINIUM STEP LADDER is set up on the grass right against the front wall of the house, close under the camera. A MAN is standing high up on it, near the very top steps, in a dark navy hoodie, blue jeans and brown boots, seen from BEHIND AND ABOVE because of the camera angle - his face is not visible to the camera. He is stretched up and leaning in toward the wall with BOTH ARMS RAISED above his head, pressing a strip of SILVER DUCT TAPE onto the render with one hand while the other hand holds the thing he is taping up. His weight is off-centre, one heel lifted off the rung, the ladder tilted very slightly - it obviously should not hold.

WHAT HE IS TAPING UP: a BIG INFLATABLE CHRISTMAS DECORATION - a fat inflatable SNOWMAN about the height of a man, white with a black top hat, a red-and-green scarf and a carrot nose, fully inflated and bulging, being held flat against the house wall and stuck there with criss-crossed strips of silver duct tape across its belly and hat. It is far too big and far too round to be taped to anything, and one taped corner is already peeling away from the wall.

ON THE GROUND AT THE FOOT OF THE LADDER, close to the camera: a WOMAN in a teal-green fleece and black leggings stands steadying one leg of the ladder with both hands, looking up, plus a second smaller inflatable - an inflatable SANTA - lying half-deflated on its side on the grass with its power cable trailing, and a roll of duct tape and a pair of scissors dropped on the lawn beside it.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour security-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork of the foreground wall, in the fabric of the inflatable snowman, in the weave of their clothing and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun raking in from the side, long real shadows from the ladder and the man across the grass, bright but properly exposed - no blown-out white on the render or the car roof, no crushed black in the shadow under the eaves, correct white balance. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
````

#### Video prompt — `clips/v30_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `8d3901e1-07ce-4072-b9bc-6552010652ee`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_003431_8d3901e1-07ce-4072-b9bc-6552010652ee.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v30_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c01_g3.png` · Higgsfield media `c75c3acb-accc-4683-998a-627e4f968854`

````text
THE CAMERA NEVER MOVES. This is the single most important rule. The shot is a fixed security camera bolted high under the eaves at the corner of the house, looking down at the front yard. It does not pan, tilt, zoom, dolly, orbit, shake, drift, rack focus or re-frame at any moment. The brick wall stays locked along the left edge of the frame for all five seconds, the white car roof stays locked in the bottom right corner, the houses and the street across the yard never shift by a single pixel. Everything that moves in this clip is the two people and the ladder. Treat the background as a still photograph.

Continue the attached start frame as one continuous unbroken five-second take. No cuts, no edits, no transitions, no speed ramps, no slow motion. Same two people, same clothes, same orange step ladder, same inflatable snowman, same late-afternoon winter light as the frame.

THE ACTION, as a timeline:
0.0-1.4s - The man stays high on the orange step ladder with both arms stretched above his head, working. He presses a strip of silver duct tape onto the house wall with his right hand while his left hand holds the big inflatable snowman flat against the render. He smooths the tape down, leans further in, rises up onto his toes on the rung to reach a little higher. The inflatable bulges and shifts against his hand. The woman below stands holding the ladder leg with both hands, looking up at him.
1.4-2.4s - He stretches too far sideways. His weight goes outside the ladder. The ladder tips - the two far feet lift off the grass and it leans away from the wall. He grabs at the wall, fingers scrabbling on the render, finds nothing.
2.4-3.4s - HE FALLS. The ladder goes over and he comes down with it, fast and heavy, tumbling backwards and sideways onto the grass below, arms flailing. The orange ladder clatters down beside him. The inflatable snowman rips free of its tape and flops down the wall after him, bouncing once on the lawn. The roll of duct tape flies out of his hand.
3.4-4.2s - The woman lets go and jumps back out of the way, both hands flying up to her face, her whole body recoiling, head thrown back - she is screaming. The man is flat on his back on the grass with the ladder across his legs.
4.2-5.0s - The man lies still for a beat, then his knee bends and one arm comes up to his chest. The woman rushes the two steps to him and drops to a crouch beside him, hands out. The deflating snowman settles beside them on the lawn.

PHYSICS AND REALISM: real people with real weight, filmed by a real camera. Gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down. The aluminium ladder is rigid and heavy and it topples as one stiff object. The inflatable is light and air-filled and it bounces and wobbles. Clothing creases and flaps. Both bodies stay whole and correctly proportioned throughout - arms and legs bend only at real joints and only the way real joints bend.

BANNED: no camera movement of any kind, no zoom, no push in, no handheld shake, no third person appearing, no ladder bending or melting, no rubbery or elastic limbs, no impossible bends, no morphing faces, no extra arms or hands, no objects vanishing or duplicating, no slow motion, no cinematic grade, no lens flare, no text, no timestamp, no watermark, no logos, no captions, no UI.

LOOK: a genuinely sharp modern 2K colour security-camera recording, bright and correctly exposed in the low warm winter sun, natural colour, crisp detail, real cast shadows on the grass. Not a movie, not a render, not an illustration.

AUDIO: natural outdoor sound only - the rattle and scrape of the aluminium ladder going over, the thud of his body on the grass, the rubbery flap of the inflatable, one short shout from him as he goes, then the woman's loud sharp scream of fright and her voice calling out in alarm. Cold wind and a distant car underneath. No music, no score, no background song, no narration, no sound effects library stings.
````

**Other takes of C01 on disk (3)**

#### Image prompt — `starting_frames/v30_c01_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `6740da09-550f-479b-9c08-57d5da20c03f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_232727_6740da09-550f-479b-9c08-57d5da20c03f.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e`

````text
Reproduce the attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a HOUSE SECURITY CAMERA. Keep the same suburban American street, the same late-afternoon winter light, the same mood.

THE CAMERA - copy it from the attached image: a security camera bolted high under the eaves at the front corner of a house, well above head height, looking DOWN and OUT at a steep angle across the front yard and the driveway toward the street. Wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Fixed, static, unmanned, elevated viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE ATTACHED IMAGE, just re-stacked for a vertical frame:
- LEFT EDGE: the RED BRICK wall of the camera's own house in extreme close foreground, seen sharply along its length so the courses of brick and mortar run away from the lens in steep perspective, filling a tall vertical band down the whole left side of the frame.
- BOTTOM RIGHT FOREGROUND: the white roof and windscreen of a car parked close under the camera, cut off by the bottom corner of the frame, catching a hard highlight.
- CENTRE: the front lawn of the house - winter grass, a low planting bed with a string of unlit coloured lights along its edge, a slim young tree.
- MIDDLE DISTANCE: a concrete driveway with a WHITE SALOON CAR parked on it, and the neighbouring two-storey houses with pale render and stone bases and WHITE DOUBLE GARAGE DOORS.
- RIGHT: the road running away through the frame, kerbs, pavements, and more houses with garages on the far side.
- TOP: the eaves and roofline of the camera's own house, and a wide sky above the rooftops.

THE MAIN ACTION, in the middle of the frame on the lawn - exactly where the ladder stands in the attached image:

A TALL ORANGE-RED ALUMINIUM STEP LADDER is set up on the grass right against the front wall of the house. A MAN is standing high up on it, near the very top steps, in a dark navy hoodie, blue jeans and brown boots, seen from BEHIND AND ABOVE because of the camera angle - his face is not visible to the camera. He is stretched up and leaning in toward the wall with BOTH ARMS RAISED above his head, pressing a strip of SILVER DUCT TAPE onto the render with one hand while the other hand holds the thing he is taping up. His weight is off-centre, one heel lifted off the rung, the ladder tilted very slightly - it obviously should not hold.

WHAT HE IS TAPING UP: a BIG INFLATABLE CHRISTMAS DECORATION - a fat inflatable SNOWMAN about the height of a man, white with a black top hat, a red-and-green scarf and a carrot nose, fully inflated and bulging, being held flat against the house wall and stuck there with criss-crossed strips of silver duct tape across its belly and hat. It is far too big and far too round to be taped to anything, and one taped corner is already peeling away from the wall.

ON THE GROUND AT THE FOOT OF THE LADDER: a WOMAN in a teal-green fleece and black leggings stands steadying one leg of the ladder with both hands, looking up, plus a second smaller inflatable - an inflatable SANTA - lying half-deflated on its side on the grass with its power cable trailing, and a roll of duct tape and a pair of scissors dropped on the lawn beside it.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour security-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork of the foreground wall, in the fabric of the inflatable snowman and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun raking in from the side, long real shadows from the ladder and the man across the grass, bright but properly exposed - no blown-out white on the render or the car roof, no crushed black in the shadow under the eaves, correct white balance. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
````

#### Image prompt — `starting_frames/v30_c01_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `fd525a02-0fd1-4401-96af-a94bcece53ed`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_234738_fd525a02-0fd1-4401-96af-a94bcece53ed.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e`

````text
Reproduce the attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a HOUSE SECURITY CAMERA. Keep the same suburban American street, the same late-afternoon winter light, the same mood.

THE CAMERA - copy it from the attached image: a security camera bolted high under the eaves at the front corner of a house, well above head height, looking DOWN and OUT at a steep angle across the front yard and the driveway toward the street. Wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Fixed, static, unmanned, elevated viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE ATTACHED IMAGE, just re-stacked for a vertical frame:
- LEFT EDGE: the RED BRICK wall of the camera's own house in extreme close foreground, seen sharply along its length so the courses of brick and mortar run away from the lens in steep perspective, filling a tall vertical band down the whole left side of the frame.
- BOTTOM RIGHT FOREGROUND: the white roof and windscreen of a car parked close under the camera, cut off by the bottom corner of the frame, catching a hard highlight.
- CENTRE: the front lawn of the house - winter grass, a low planting bed with a string of unlit coloured lights along its edge, a slim young tree.
- MIDDLE DISTANCE: a concrete driveway with a WHITE SALOON CAR parked on it, and the neighbouring two-storey houses with pale render and stone bases and WHITE DOUBLE GARAGE DOORS.
- RIGHT: the road running away through the frame, kerbs, pavements, and more houses with garages on the far side.
- TOP: the eaves and roofline of the camera's own house.

THE ONE CHANGE FROM THE ATTACHED IMAGE - THE PEOPLE AND THE LADDER ARE MUCH CLOSER TO THE CAMERA. The ladder is set up on the grass only a couple of metres below and in front of the camera, right at the near corner of the house rather than further along it. The man on the ladder fills roughly the upper-left third of the vertical frame and the woman below him fills roughly a quarter of the frame height - they are the unmistakable subjects, big and close, not small figures in a wide yard. The camera is looking almost straight down onto them at a steep angle from just above. The street and the neighbouring houses are pushed well back into the upper right of the frame as background only.

THE ACTION: A TALL ORANGE-RED ALUMINIUM STEP LADDER is set up on the grass right against the front wall of the house, close under the camera. A MAN is standing high up on it, near the very top steps, in a dark navy hoodie, blue jeans and brown boots, seen from BEHIND AND ABOVE because of the camera angle - his face is not visible to the camera. He is stretched up and leaning in toward the wall with BOTH ARMS RAISED above his head, pressing a strip of SILVER DUCT TAPE onto the render with one hand while the other hand holds the thing he is taping up. His weight is off-centre, one heel lifted off the rung, the ladder tilted very slightly - it obviously should not hold.

WHAT HE IS TAPING UP: a BIG INFLATABLE CHRISTMAS DECORATION - a fat inflatable SNOWMAN about the height of a man, white with a black top hat, a red-and-green scarf and a carrot nose, fully inflated and bulging, being held flat against the house wall and stuck there with criss-crossed strips of silver duct tape across its belly and hat. It is far too big and far too round to be taped to anything, and one taped corner is already peeling away from the wall.

ON THE GROUND AT THE FOOT OF THE LADDER, close to the camera: a WOMAN in a teal-green fleece and black leggings stands steadying one leg of the ladder with both hands, looking up, plus a second smaller inflatable - an inflatable SANTA - lying half-deflated on its side on the grass with its power cable trailing, and a roll of duct tape and a pair of scissors dropped on the lawn beside it.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour security-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork of the foreground wall, in the fabric of the inflatable snowman, in the weave of their clothing and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun raking in from the side, long real shadows from the ladder and the man across the grass, bright but properly exposed - no blown-out white on the render or the car roof, no crushed black in the shadow under the eaves, correct white balance. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
````

#### Image prompt — `starting_frames/v30_c01_g4.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `85107525-50b2-40fc-9bea-05d6720eadef`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_000339_85107525-50b2-40fc-9bea-05d6720eadef.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `c921e1b2-8e69-4778-8b3f-3fb5a62dbf1e`

````text
Reproduce the attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a HOUSE SECURITY CAMERA. Keep the same suburban American street, the same late-afternoon winter light, the same mood.

COMPOSITION - CRITICAL. The people and the ladder are CLOSE TO THE CAMERA and BIG in the frame - they dominate the picture, they are not small figures in a wide yard. The ladder is set up on the grass only a couple of metres below and in front of the camera, right at the near corner of the house. The man on the ladder and the inflatable he is taping fill roughly a third of the frame height. The woman below him fills roughly a quarter of the frame height. The camera looks almost straight down onto them at a steep angle from just above.

The ONLY concession is a NARROW STRIP OF CLEAN SKY along the very top of the frame - about one eighth of the frame height, a calm uncluttered band of pale winter sky and plain roofline, left clear for a caption. Just a small margin of breathing room at the very top: the top of the inflatable snowman's hat and the eaves of the house sit just below that strip, not squeezed down into the middle of the picture. Do NOT shrink the people to make room, do NOT pull the camera back, do NOT leave a big empty upper half - only a slim clean band at the extreme top.

THE CAMERA - copy it from the attached image: a security camera bolted high under the eaves at the front corner of a house, well above head height, looking DOWN and OUT at a steep angle across the front yard and the driveway toward the street. Wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Fixed, static, unmanned, elevated viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE ATTACHED IMAGE, re-stacked for a vertical frame:
- LEFT EDGE: the RED BRICK wall of the camera's own house in extreme close foreground, seen sharply along its length so the courses of brick and mortar run away from the lens in steep perspective, filling a tall vertical band down the left side of the frame.
- BOTTOM RIGHT FOREGROUND: the white roof and windscreen of a car parked close under the camera, cut off by the bottom corner of the frame, catching a hard highlight.
- CENTRE: the front lawn - winter grass, a low planting bed with a string of unlit coloured lights along its edge, a slim young tree.
- MIDDLE DISTANCE: a concrete driveway with a WHITE SALOON CAR parked on it, and the neighbouring two-storey houses with pale render and stone bases and WHITE DOUBLE GARAGE DOORS.
- RIGHT: the road running away through the frame, kerbs, pavements, and more houses with garages on the far side.

THE ACTION: A TALL ORANGE-RED ALUMINIUM STEP LADDER is set up on the grass right against the front wall of the house, close under the camera. A MAN is standing high up on it, near the very top steps, in a dark navy hoodie, blue jeans and brown boots, seen from BEHIND AND ABOVE because of the camera angle - his face is not visible to the camera. He is stretched up and leaning in toward the wall with BOTH ARMS RAISED above his head, pressing a strip of SILVER DUCT TAPE onto the render with one hand while the other hand holds the thing he is taping up. His weight is off-centre, one heel lifted off the rung, the ladder tilted very slightly - it obviously should not hold.

WHAT HE IS TAPING UP: a BIG INFLATABLE CHRISTMAS DECORATION - a fat inflatable SNOWMAN about the height of a man, white with a black top hat, a red-and-green scarf and a carrot nose, fully inflated and bulging, held flat against the house wall and stuck there with criss-crossed strips of silver duct tape across its belly and hat. It is far too big and far too round to be taped to anything, and one taped corner is already peeling away from the wall.

ON THE GROUND AT THE FOOT OF THE LADDER, close to the camera: a WOMAN in a teal-green fleece and black leggings stands steadying one leg of the ladder with both hands, looking up, plus a second smaller inflatable - an inflatable SANTA - lying half-deflated on its side on the grass with its power cable trailing, and a roll of duct tape and a pair of scissors dropped on the lawn beside it.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour security-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork, in the fabric of the inflatable snowman, in the weave of their clothing and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun raking in from the side, long real shadows from the ladder and the man across the grass, bright but properly exposed - no blown-out white on the render or the car roof, no crushed black in the shadow under the eaves, correct white balance. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
````

### C02 — Box over the sofa

**In the cut:** `starting_frames/v30_c02_g1.png` → `clips/v30_c02_g1.mp4`

#### Image prompt — `starting_frames/v30_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `a343259f-829e-4107-a3a8-cb9f230d5330`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210916_a343259f-829e-4107-a3a8-cb9f230d5330.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_20_assets/starting_frames/v20_c02_g5.png` · Higgsfield media `05989e1b-228c-432a-be58-a51cfbfa19ad`
- @Image 2: `content/video_29_assets/starting_frames/v29_c02_g1.png` · Higgsfield media `07ebb15c-1e14-4ef7-b576-b0f4210e0c5b`

````text
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. The box is a closed rigid printed gift box with NO transparent window and NO cut-out panel anywhere on it. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: a late-twenties woman with warm olive skin and DARK CHOCOLATE-BROWN hair worn in a loose low bun with a few face-framing strands escaping, wearing a CREAM CABLE-KNIT CARDIGAN over a white tee and CHARCOAL-GREY soft joggers. The room has a PALE GREY-WASHED OAK wide-plank floor, a DEEP NAVY VELVET sofa with blush-pink and cream cushions and a cream chunky-knit throw, a WARM WHITE SHIPLAP wall behind, a BRASS ARC floor lamp curving over from the left, and a slim REAL GREEN SPRUCE Christmas tree hung with red-and-white candy-cane striped baubles and warm white lights standing at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the knit of her cardigan and in the print on the box, clean even indoor light with no blown highlights and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur on the box or on her, NO grain, NO haze, NO soft focus anywhere. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v30_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `fc90aca7-61ca-4f55-975c-d455f8ac67c2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013134_fc90aca7-61ca-4f55-975c-d455f8ac67c2.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v30_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c02_g1.png` · Higgsfield media `a343259f-829e-4107-a3a8-cb9f230d5330`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `ffaa8801-8e71-43f0-ae24-461104cf30f2`
- image ref 2: `product_images/box_nowindow/box_interior_g5.png` · Higgsfield media `f01fecfe-9cbe-44a5-a617-63193a1108b0`

````text
TWO SCENES IN ONE CLIP, JOINED BY ONE HARD CUT AT EXACTLY 2.5s. No dissolve, no fade, no whip pan, no transition effect — a straight in-camera cut, exactly like a creator cutting two takes together.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she walks at a walking pace, she kneels at the speed a body really kneels, the lid swings open at the speed heavy cardboard really swings. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in five seconds — one slow lowering, one slow kneel, one slow lid. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still settling as the clip ends than that any part of it looks fast-forwarded.

REFERENCE IMAGES. Reference image 1 is the first frame of scene 1 — start there, unchanged, and it owns the room, the woman, the camera angle and the geometry. Reference image 2 is the CLOSED PRODUCT BOX: the artwork on the box in this video must match it exactly. Reference image 3 is the OPEN BOX INTERIOR: what she reveals in scene 2 must match it exactly.

THE WOMAN — she is exactly the woman in reference image 1 and never changes: a late-twenties woman with warm olive skin and DARK CHOCOLATE-BROWN hair worn in a loose low bun with a few face-framing strands escaping, in a CREAM CABLE-KNIT CARDIGAN over a white tee and CHARCOAL-GREY soft joggers. Same hair, same skin, same clothes, first frame to last.

BOX SPEC — TRUE IN EVERY FRAME. A matte black rigid retail box, 55 cm wide x 42 cm tall x 10 cm deep. It is BIG — much wider than the span of two outstretched hands; each of her hands covers less than a quarter of the box width, and laid on the sofa seat it spans most of one cushion. Front panel top to bottom: a large white condensed uppercase headline LED CURTAIN LIGHTS; a warm gold subline Create Your Own Magic; a red diagonal BEST SELLER ribbon flag in the top-right corner; one large photographic panel with a thin gold hairline border showing a night house facade with a glowing pixel LED Christmas tree on the garage door; a bottom row of five small gold line icons with white captions. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible through the front, NO glowing lights showing through the cardboard. The box is closed and sealed until the moment she opens it in scene 2.

SCENE 1 — 0.0 to 2.5s. CAMERA: HELD IPHONE, LOCKED FOCAL LENGTH, portrait, a friend filming from just behind her left shoulder at HER SHOULDER HEIGHT, tilted down only very slightly — exactly where reference image 1 was taken. NOT above her head, NOT a top-down shot. NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO DOLLY. Handheld micro-shake only. She is at the LEFT EDGE of frame, partly cut off by it; the DEEP NAVY VELVET sofa is directly IN FRONT of her, running diagonally away into depth and filling the right and bottom-right of frame, its empty seat cushions facing up. The room behind her — the PALE GREY-WASHED OAK wide-plank floor, the WARM WHITE SHIPLAP wall, the BRASS ARC floor lamp curving over from the left, the blush-pink and cream cushions, the cream chunky-knit throw and the slim green spruce Christmas tree hung with red-and-white candy-cane striped baubles and warm white lights at the right — stays exactly as it is and never changes.
THE WHOLE POINT OF SCENE 1: she carries the box round in front of the sofa, sets it flat on the seat cushion AND drops to her knees IN THE SAME CONTINUOUS MOTION. These are not two separate steps — the box going down and her body going down are one move.
0.0-0.9s — one unhurried step forward and to her right, her shoulders turning, the heavy box swinging slowly out in front of her; the loose strands at her temple swing across and settle, her cream cardigan sleeve creases with the weight.
0.9-1.8s — she steps in front of the sofa and leans forward from the hips, lowering the box steadily toward the empty deep navy velvet seat cushion, arms extending, knees already bending underneath her. This lowering is SLOW and heavy — the box is big and awkward and she is being careful with it.
1.8-2.5s — the box settles flat and printed-side-up on the cushion with a soft compression of the navy velvet, her hands still on it, and in the same continuous motion her knees come down onto the pale grey-washed oak floor one after the other, her weight settling and her back rounding forward; she tucks a loose strand behind one ear and plants both palms flat on the box lid, chest rising with one excited breath.

HARD CUT AT 2.5s.

SCENE 2 — 2.5 to 5.0s. Direct continuation, same room, same second, same woman, same cream cable-knit cardigan, same box in exactly the same place on the same deep navy velvet cushion. The camera has moved about 30 degrees round to her side — a slightly more side-on three-quarter angle, a little lower, closer to the level of the sofa seat, so we now see the lid edge in profile and read the pivot clearly. Still HELD IPHONE, LOCKED FOCAL LENGTH, handheld micro-shake only, NO ZOOM.
LID MECHANISM, GEOMETRICALLY. The box is a magnetic-closure flip-top. The hinge runs along the TOP LONG EDGE of the box — the far edge away from her, at the back. The lid pivots UP and BACK on that hinge, rotating away from her and toward the back of the sofa, keeping its printed front face turned toward the camera as it rises. The inside of the lid is matte black. The lid is NEVER lifted off, NEVER removed, NEVER carried aside, NEVER set down, NEVER folded flat instantly, NEVER slid out like a drawer.
2.5-3.1s — she hooks her fingertips under the near front edge of the lid; a small snap as the magnets release and the front edge lifts a centimetre, a thin black shadow line opening slowly across the whole 55 cm width.
3.1-4.3s — she pivots the big printed lid UP and BACK on its hinge in ONE slow continuous arc with real cardboard weight, her elbows rising and her shoulders lifting with the effort, until it stands roughly vertical. This arc takes well over a full second of screen time — it travels heavily and never flips or snaps open.
4.3-5.0s — the interior is revealed exactly as reference image 3: the neatly folded BLACK LED mesh curtain lying in its tray, the coiled black lead and the small accessory items beside it, all against a matte black interior. She reaches in with both hands and touches the folded black mesh, fingers spreading it slightly, then lifts her chin, looks off toward the spruce tree and breaks into a big open-mouthed grin, eyebrows up.

MOVEMENT RULE FOR BOTH SCENES: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole clip — weight shifting, chest breathing, loose strands and sleeves swinging and settling, the cushion compressing under the box — and her face keeps changing, eyes, eyebrows and mouth reading differently moment to moment. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses.

HARD RULES: exactly ONE cut, at 2.5s. The box never changes size, never changes artwork, never gains a window or a cutout. The curtain inside the box is BLACK cord with small dark bulbs — never white wire, never clear wire, never silver wire. Nobody else enters frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Quiet warm living-room ambience, the soft thump of a heavy box on a cushion, knees on the floor, the click of magnets releasing, stiff cardboard flexing, plastic mesh rustling, one small delighted exhale.

LOOK: real iPhone UGC indoors at night. Warm mixed lamp and fairy light, slight sensor noise in the shadows, natural skin, no cinematic grade, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
````

### C03 — Mounting on the attached garage, day

**In the cut:** `starting_frames/v30_c03_g1.png` → `clips/v30_c03_g1.mp4`

#### Image prompt — `starting_frames/v30_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `902719cb-1aab-412f-be53-6ef675c7d164`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_211053_902719cb-1aab-412f-be53-6ef675c7d164.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c03_g2.png` · Higgsfield media `46b340e4-6caf-44c9-aa30-cc219dfe59a6`
- @Image 2: `content/video_30_assets/starting_frames/v30_c02_g1.png` · Higgsfield media `a343259f-829e-4107-a3a8-cb9f230d5330`

````text
COPY THE CAMERA OF THE FIRST ATTACHED IMAGE EXACTLY - its position, its angle, its height, its closeness and her pose. This is a CLOSE, SIDE-ON shot, not a wide frontal shot.

THE CAMERA IS CLOSE AND OFF TO ONE SIDE, exactly as in the first image: the camera stands near the wall and slightly behind her at roughly waist height, looking ALONG the wall, so the wall runs away from the camera DIAGONALLY - nearest at the bottom-left of the frame and receding to the right, the roof gutter line along the top sloping down towards the right as it goes away, strong oblique one-point perspective. She fills most of the frame height in the right half, her whole body in shot from her boots on the stool up to her raised hands. MUCH CLOSER than a full-house shot: only a short run of the wall is in frame, no full facade, no wide establishing view, no flat square-on frontal view.

HER POSE - copy it from the first image: she stands on a small BLACK two-step folding step stool, seen from BEHIND and slightly to the side, facing the wall, both arms raised in front of her, her hands up at the trim board along the top of the wall as she presses the LED curtain into place. Her weight is on one foot, her back slightly arched.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Long vertical strands of thin BLACK cord with small DARK unlit bulbs hang down the wall to the left of her, and because the camera is close the strands are big in the frame and clearly readable as separate cords. A BIG LOOSE TANGLE of BLACK cord is heaped on the snow at the foot of the stool, spilling out to the left - a real messy nest of wire, obviously dark against the white snow, exactly like the bundle in the first image. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - TAKE HER FROM THE SECOND ATTACHED IMAGE. Same late-twenties woman with warm olive skin and DARK CHOCOLATE-BROWN hair, now worn in a low bun spilling out from under a MUSTARD-YELLOW beanie, wearing a FOREST-GREEN puffer parka with a faux-fur trimmed hood, BLACK jeans and BLACK boots. It must read as literally the same person as in the second image.

A COMPLETELY NEW HOUSE - take it from this text only, NOT from either attached image. The wall she is working on is the WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR of a two-storey family home - soft WHITE with horizontal panel seams and recessed rectangular panels running away in perspective, and the row of small square windows across the top of the door visible at the far end. Around it, SOFT SAGE-GREEN lap siding with crisp WHITE trim, a BLACK COACH LANTERN on the wall, a WHITE gutter and WHITE downpipe, a charcoal-grey roof, and a plain CONCRETE driveway under patchy snow. At the RIGHT of the frame, further away, the corner where the garage wing meets the MAIN HOUSE BODY is visible - the two-storey wall, the covered porch on white posts and the NAVY-BLUE front door - so it reads as ONE house with the garage built into it.

DO NOT COPY THE HOUSE FROM THE FIRST IMAGE: not its warm sand-beige or cream siding, not its dark red front door. The first image is there ONLY for the camera, the distance, the angle, the pose and the black wire.

Daytime, overcast winter light, snow on the ground.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the door panels, the quilting of her parka and every strand of black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v30_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `29bb5d7f-5250-4960-a8e0-e958f5dfa3fe`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013134_29bb5d7f-5250-4960-a8e0-e958f5dfa3fe.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v30_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c03_g1.png` · Higgsfield media `902719cb-1aab-412f-be53-6ef675c7d164`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same overcast winter day, same CLOSE SIDE-ON camera at waist height looking ALONG the wall so it recedes diagonally from the bottom-left of frame away to the right, same WIDE SOFT WHITE SECTIONAL DOUBLE GARAGE DOOR with its horizontal panel seams and recessed panels running away in perspective and its row of small square windows across the top at the far end, same SOFT SAGE-GREEN lap siding with crisp white trim around the door, same black coach lantern, same white gutter and white downpipe, same charcoal-grey roof, same concrete driveway under patchy snow, same corner of the main house body with its covered porch on white posts and its navy-blue front door further away at the right, same black two-step folding step stool, same woman seen from behind in the FOREST-GREEN puffer parka with the faux-fur trimmed hood, black jeans, black boots and the mustard-yellow beanie with her dark chocolate-brown bun spilling out from under it, standing on the stool with both arms raised pinning the gathered fistful of unlit net up under the trim board above the door, same LED net already hung flat across the door to her left, same loose tangled coil of curtain heaped on the snow at the foot of the stool.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she reaches at the speed an arm really reaches, she shakes the net out at the speed a heavy tangled net really swings, she shifts her weight at the speed a body really balances on a step stool. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in four seconds — one slow shake, one slow reach, one slow sideways press. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still mid-reach as the clip ends than that any part of it looks fast-forwarded.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH. Portrait, exactly the framing and the angle of the reference image — close, side-on, at waist height, looking along the garage door so it recedes diagonally into the frame. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT. The garage door, the white trim, the coach lantern and the stool stay exactly the same size in frame from the first frame to the last, the perspective never flattens, and the camera never swings round to a flat square-on frontal view of the door and never pulls back to a wide establishing shot of the whole house.

MOVEMENT RULE: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole four seconds — weight shifting on the stool, shoulders rolling, ribs breathing, the bun and loose strands swinging and settling, the puffer parka creasing and rustling, the strands swaying on after every touch. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses, and no limb ever travels faster than a real arm travels.

ACTION TIMELINE (4 seconds, one continuous take, no cuts) — ONLY TWO THINGS HAPPEN, AND BOTH ARE SLOW:
0.0-2.0s — she lifts the gathered bundle in her right hand and shakes it out ONCE, slowly and heavily. The shake takes well over a full second of screen time: her arm swings out and down, the tangled net lets go in stages rather than all at once, and a long sheet of black strands falls open down the white door panels and swings for a moment before it settles. The loose coil on the snow drags and shifts with it.
2.0-4.0s — still up on the stool, she stretches both arms high and presses the header wire UP UNDER THE LIP OF THE WHITE TRIM BOARD ABOVE THE DOOR, her thumbs working slowly along it, then walks her hands a short way sideways along that trim board, away from the camera into the depth of the frame, onto the bare stretch of door beyond the strands she has already hung, pressing and tucking as she goes, her torso twisting and her heels lifting and dropping on the tread. She is STILL tucking when the clip ends. The curtain sways gently against the door panels and is still settling on the last frame.
THAT IS THE WHOLE CLIP. She does NOT step down off the stool, does NOT step back, does NOT plant her hands on her hips and does NOT tilt her head back to look at her work. There is no time for any of that at real speed, and cramming it in is exactly what would force the footage to look sped up. She stays on the stool from the first frame to the last.

THE LED CURTAIN IS BLACK — CRITICAL. The wire is BLACK, not white and not clear. Every vertical strand hanging down the door is a thin BLACK cord and the unlit bulbs on it are small and DARK. Against the soft white door panels the strands read as thin dark lines, clearly and obviously dark. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire appears at any moment.

HARD RULES: the curtain is COMPLETELY OFF the entire time — not one bulb lights, no glow, no colour, no animation on the door. The garage door never gains new panels or features, the row of small square windows across the top never moves, the white trim, the coach lantern, the gutter and the downpipe never move, and the covered porch and navy-blue front door further away at the right never change. The strands are separate vertical strands obeying gravity, sagging slightly, with an uneven wavy bottom hem — never a flat sheet, never a panel, never a screen, never a mesh stretched tight. The loose coil rests in the snow with real contact shadows. Her face is never shown; she stays turned away from camera throughout. No other people enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor winter ambience, thin plastic strands rattling and clicking against the metal door panels, a step-stool creak, boots on a metal tread, boots compressing snow, one quiet effortful breath. No voice.

LOOK: real iPhone UGC. Flat overcast winter daylight, slightly cool white balance, mild sensor noise, natural skin, no cinematic grade, no lens flare, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
````

### C04 — Phone POV, the same house at night

**In the cut:** `starting_frames/v30_c04_g2.png`, `references/v30_c04_r1.png` → `clips/v30_c04_g1.mp4`

#### Image prompt — `starting_frames/v30_c04_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `3eb2aa97-ee05-4fcd-816e-5c6b1196c73e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_233056_3eb2aa97-ee05-4fcd-816e-5c6b1196c73e.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_30_assets/starting_frames/v30_c04_g1.png` · Higgsfield media `cee3d830-2bd2-4fbb-ae8b-bdf089de8d6b`

````text
COPY THE ATTACHED IMAGE EXACTLY. Same house, same soft white sectional double garage door, same siding, same white trim, same black coach lanterns glowing warm either side, same snowy concrete driveway, same night light, same camera, same framing, same distance, same square-on angle, same foreground hand holding the same iPhone in the bottom-centre with the SAME two-column app grid and the same round blue play button. Everything is already correct and must be reproduced unchanged.

ONE SINGLE THING CHANGES: THE LED CURTAIN HAS ROUGHLY TWICE AS MANY STRANDS. In the attached image the vertical strands hanging over the garage door are spaced widely apart. Here they are packed about TWICE AS CLOSE TOGETHER - roughly double the number of strands across the same width, so the curtain reads as a much DENSER set of vertical lines running down the whole face of the door.

THE STRANDS THEMSELVES ARE UNCHANGED: each one is still a thin BLACK cord carrying small DARK unlit bulbs, the lights are OFF with no glow, and against the pale door each cord reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. They still hang from the trim board above the door, still span the full width of the door edge to edge, still have a slight natural sag and a slightly uneven bottom hem.

STILL A CURTAIN, NEVER A PANEL - CRITICAL: even at double the density these are SEPARATE HANGING VERTICAL STRANDS with clear DARK GAPS between them, and the garage door behind is plainly visible through those gaps - the recessed panel seams and the row of small square windows across the top must still read clearly through the curtain. Do NOT close the gaps. Do NOT turn it into a solid LED panel, a flat screen, a mesh, a net, a grille or a fabric sheet. Do NOT add horizontal wires. The strands run straight up and down only.

THE FRAMING IS ALREADY CORRECT - DO NOT CHANGE IT. The garage door stays big and dominant, spanning almost the full width of the picture, with the ENTIRE door visible: both vertical side edges inside the frame, the complete top edge including the WHOLE row of small square windows end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT tilt. Still square-on from the front: the panel seams run dead level and the door edges run straight up and down.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every individual black cord clearly readable and clearly separated from its neighbours, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `references/v30_c04_r1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `30de064d-6194-4348-b0ef-8239e7d07791`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_233258_30de064d-6194-4348-b0ef-8239e7d07791.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_30_assets/starting_frames/v30_c04_g2.png` · Higgsfield media `3eb2aa97-ee05-4fcd-816e-5c6b1196c73e`
- @Image 2: `content/video_30_assets/starting_frames/v30_c07_g1.png` · Higgsfield media `24b2cf14-ccee-43ca-90bc-8066b7dbc684`

````text
TAKE THE FIRST ATTACHED IMAGE AS THE SCENE. Same house, same soft white sectional double garage door with its recessed panels and its row of small square windows across the top, same siding, same white trim, same black coach lanterns glowing warm either side of the door, same snowy concrete driveway, same night. Same camera, same lens, same distance, same square-on frontal angle. TAKE THE SECOND ATTACHED IMAGE ONLY FOR THE DRAWING STYLE OF THE LIGHTS - the way the cartoon is built out of small round coloured bulbs. DO NOT COPY THE SECOND IMAGE'S HOUSE, ITS GABLE, ITS CAR, ITS ROAD OR ITS SCENE. Only its bulb-art look.

THREE THINGS CHANGE FROM THE FIRST IMAGE:

1. THE HAND AND THE PHONE ARE GONE. There is nothing at all in the foreground. No hand, no arm, no sleeve, no phone, no screen, no glow from a screen. The bottom-centre of the frame is simply the empty snowy driveway. The whole garage door is completely unobstructed from edge to edge.

2. THE CAMERA HAS TILTED UP A LITTLE. This is a handheld iPhone shot and the person filming has tipped the phone up slightly so the lights fill the frame. The framing is otherwise identical - same distance, same square-on frontal angle, the door still faces the camera flat with its horizontal panel seams dead level and its vertical edges straight up and down - but the whole frame has shifted UP: there is now only a THIN sliver of driveway along the bottom edge, and a slightly DEEPER band of siding and trim above the top of the door. The ENTIRE garage door stays inside the frame: both side edges, the complete top edge with the WHOLE row of small square windows visible end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT turn it into a low angle looking up at the roofline, do NOT show the whole house.

3. THE LED CURTAIN IS SWITCHED ON AND SHOWING A BRIGHT CARTOON ANIMATION. The same dense curtain of closely spaced vertical strands hanging over the garage door, but now every bulb is lit and together they draw a picture.

THE PICTURE - A CONGA LINE, drawn chunky and simple out of the bulbs, running RIGHT ACROSS THE WHOLE GARAGE DOOR: SANTA leads at the LEFT, one knee up and one leg kicked out sideways, one arm thrown in the air, mouth wide open in a big round O, eyes as two white circles. Behind him, all holding the shoulders of the one in front and ALL KICKING THE SAME LEG OUT THE SAME WAY, comes a line of THREE GREEN ELVES and THREE REINDEER alternating, each one leaning back at the same jaunty angle, knees and hooves flung out. At the FAR RIGHT the last little elf has been kicked clean off his feet and is flying backwards through the air upside down, arms and legs splayed, his pointed hat coming off. Curved speed lines and small puffs trail behind the kicking legs. Along the bottom a row of bouncing PRESENTS hops after them, each a DIFFERENT BRIGHT COLOUR with a contrasting ribbon and bow. Small gold stars scattered through the gaps. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

THE PICTURE FILLS THE ENTIRE GARAGE DOOR: the conga line spans the FULL WIDTH of the door from its left edge to its right edge, and the figures plus the bouncing presents plus the stars fill the FULL HEIGHT of the door from just under the row of square windows down to the bottom edge. Every part of the door is covered by lit artwork - no large dark empty areas anywhere on the door, and nothing is confined to a small panel in the middle. Nothing lit appears above the door, on the trim, on the siding, on the lanterns or in the sky.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. The strands are densely spaced but there are still clear DARK GAPS between them and the white garage door behind is plainly visible through those gaps, especially in the unlit areas - the recessed panel seams and the row of square windows must still read through the curtain. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the garage door panels and the snowy driveway clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v30_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `71f258a7-3fac-4eee-94ca-70545b840ad0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013134_71f258a7-3fac-4eee-94ca-70545b840ad0.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v30_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c04_g2.png` · Higgsfield media `3eb2aa97-ee05-4fcd-816e-5c6b1196c73e`
- image ref 1: `content/video_30_assets/references/v30_c04_r1.png` · Higgsfield media `30de064d-6194-4348-b0ef-8239e7d07791`

````text
THE FIRST FRAME OF THIS VIDEO IS THE START IMAGE, PIXEL FOR PIXEL, UNCHANGED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT.

WHAT IS IN THE START IMAGE, AND WHAT MUST THEREFORE BE IN FRAME 1: night, a suburban driveway shot on a held iPhone in portrait; a soft white sectional double garage door with recessed panels and a row of small square windows across the top; pale siding with white trim; two black coach lanterns glowing warm either side of the door; a snowy concrete driveway; the unlit BLACK LED curtain hanging flat across the garage door with its thin black cords and small dark bulbs; and AT THE BOTTOM-CENTRE OF FRAME, A HAND HOLDING AN IPHONE, screen toward camera, showing a simple two-column app grid and a large round blue PLAY BUTTON. Do NOT start on an empty driveway. Do NOT start on a bare garage door. Do NOT have the hand enter frame later. The hand and the phone are ALREADY THERE in frame 1, exactly as in the start image.

THE SECOND ATTACHED IMAGE IS NOT A FRAME OF THIS VIDEO. It is only a style guide showing what the lit artwork must look like once the lights come on. Never cut to it, never start on it, never copy its framing, never copy its camera height, never copy its distance. Take from it ONLY the drawing that appears in the bulbs.

THE ARTWORK THAT APPEARS IN THE LIGHTS — a CONGA LINE. SANTA leads at the LEFT, one knee up and one leg kicked out sideways, one arm thrown in the air, mouth wide open in a big round O, eyes as two white circles. Behind him, all holding the shoulders of the one in front and ALL KICKING THE SAME LEG OUT THE SAME WAY, comes a line of THREE GREEN ELVES and THREE REINDEER alternating, each one leaning back at the same jaunty angle, knees and hooves flung out. At the FAR RIGHT the last little elf has been kicked clean off his feet and is flying backwards through the air upside down, arms and legs splayed, his pointed hat coming off. Curved speed lines and small puffs trail behind the kicking legs. Along the bottom a row of bouncing PRESENTS hops after them, each a DIFFERENT BRIGHT COLOUR with a contrasting ribbon and bow. Small gold stars scattered through the gaps. Do NOT invent a different picture.

HOW THE LIGHTS MUST STAY BUILT. The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the lintel, each wire carrying small round bulbs. The whole picture is built out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix. The curtain is SEE-THROUGH: through the gaps between strands you clearly read the white garage door behind it, its horizontal panel seams and its row of small square windows, and the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark door, with unlit bulbs as tiny dull grey dots and the thin BLACK wires as faint vertical lines. Every lit bulb is a tiny point source: blown-out white core, coloured halo, small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing. The strands sag slightly, each ends at a slightly different height so the bottom hem is uneven and wavy, and the glow bounces back off the door as a soft halo and spills onto the snowy driveway in a speckled uneven pattern.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH, portrait, exactly the framing of the start image. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO CUT. The garage door stays the same size in frame throughout. The ONLY permitted camera move is a small gentle TILT UP in the second half of the clip, a few degrees, as if the person filming lifts their phone slightly to take in the whole door.

REAL TIME — NORMAL 1x SPEED. No fast motion, no sped-up playback, no time-lapse, no speed ramp.

THE ANIMATION IN THE LIGHTS MUST BE WILDLY ALIVE. A STATIC OR BARELY-MOVING PICTURE IS A TOTAL FAILURE.

TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.5s — exactly the start image. The curtain is dark and unlit. The thumb is already moving, scrolling on the phone screen.
0.5-0.8s — the thumb presses the big round blue PLAY BUTTON on the phone screen.
0.8-1.0s — IN THE SAME FRAME, without any cut, the whole LED curtain snaps ON at once, the conga line appearing all together in chunky bulbs, and warm coloured light floods across the snowy driveway.
1.0-1.6s — the hand lowers slowly out of the bottom of frame. By 1.6s the hand and the phone are COMPLETELY GONE and never return.
1.6-4.0s — the camera drifts gently upward a few degrees and the conga line runs at full tilt: the kick ripples down the line from left to right twice a second, every elf and reindeer flinging the same leg out in sequence; Santa's raised arm pumps up and down and his knee drives higher; the flying elf at the right tumbles over and over in the air with his pointed hat spinning away separately; the row of presents along the bottom hops out of step with one another and each one CHANGES COLOUR as it lands; the curved speed lines redraw behind every kicking leg; the scattered gold stars twinkle out and back in rolling waves. Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment from 1.0s onward, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once. The picture is never still for even one tenth of a second.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER LEAVES THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the door. No kicking leg, no thrown arm, no hat, no present and no star ever crosses outside the curtain rectangle. If a pose would take a limb out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Nothing lit ever appears on the white trim, the siding, the roof, the sky or the driveway except as reflected spill.

EVERYTHING ELSE IS UNCHANGED: the house, the door, the coach lanterns, the siding, the snow and the camera position are identical from first frame to last. No people, no cars, no pets enter frame.

NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural sound only — no music, no score, no background song. Cold quiet suburban night ambience, a soft phone tap, a faint electrical hum and tick from the lights, a distant car, light wind. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C04 on disk (1)**

#### Image prompt — `starting_frames/v30_c04_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `cee3d830-2bd2-4fbb-ae8b-bdf089de8d6b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_211224_cee3d830-2bd2-4fbb-ae8b-bdf089de8d6b.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g6.png` · Higgsfield media `a6bcff66-91f5-4629-be28-3ba99b78c3a7`
- @Image 2: `content/video_30_assets/starting_frames/v30_c03_g1.png` · Higgsfield media `902719cb-1aab-412f-be53-6ef675c7d164`

````text
COPY THE FIRST ATTACHED IMAGE'S CAMERA, FRAMING, DISTANCE, ANGLE AND FOREGROUND PHONE EXACTLY. Night, square-on frontal view of a double garage door, a phone held up big in the bottom-centre foreground. ONE THING CHANGES: it is a DIFFERENT HOUSE, taken from the second attached image.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. The camera is close to the house so the GARAGE DOOR IS BIG AND DOMINATES THE FRAME, spanning almost the full width of the picture with only a NARROW STRIP of white trim and siding visible beyond its left edge and beyond its right edge, only a SHALLOW BAND of siding above its top edge, and only a LOW STRIP of snowy concrete driveway beneath it. But the ENTIRE DOOR STAYS VISIBLE: both vertical side edges inside the frame, the complete top edge inside the frame including the WHOLE row of small square windows running all the way across it with every window visible end to end, and the bottom edge where the door meets the driveway inside the frame. Nothing about the door is cut off by any edge. Do NOT step closer and do NOT step back.

STILL SQUARE-ON FROM THE FRONT: the door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up, NO whole house, NO full facade, NO roofline.

THE HOUSE - TAKE IT FROM THE SECOND ATTACHED IMAGE, NOT FROM THE FIRST. It must read as LITERALLY THE SAME HOUSE as the second image, now seen square-on from the front at night: the same soft WHITE sectional double garage door with its recessed panels and its row of small square windows, and around it SOFT SAGE-GREEN lap siding with crisp WHITE trim, BLACK COACH LANTERNS glowing warm on the wall either side of the door, a WHITE gutter, and at the right edge a sliver of the covered porch on its white post with the NAVY-BLUE front door cropped by the frame. The siding must read clearly as a soft muted SAGE GREEN - NOT cream, NOT white, NOT beige, NOT grey - and visibly different in colour from the white door and the white trim.

DO NOT COPY THE SIDING COLOUR OR THE FRONT DOOR COLOUR FROM THE FIRST IMAGE. The first image is there ONLY for the camera, the framing, the night lighting and the phone.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the door in evenly spaced vertical see-through strands right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale door each strand reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen.

THE PHONE AND ITS SCREEN ARE UNCHANGED - COPY THEM EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same hand, same grip, same angle, same size and same position in the bottom-centre foreground. The screen shows the SAME APP: a dark navy-blue screen with a grid of just TWO COLUMNS of large tiles, two across and about five down, roughly ten tiles in total and no more, each tile nearly half the screen wide with softly rounded corners and a narrow gutter, each one a small photograph of a house decorated in Christmas lights - a lit roofline, a nativity, a snowman, a reindeer, a porch draped in light curtains - mostly icy blue and cool white with a couple of warm tiles, ONE tile ringed with a bright electric-blue outline, and a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE below the grid. NOT a dense grid of tiny icons, NOT three or more columns, NO glyphs or pictograms, and NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

The phone is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

### C05 — Lit facade — Santa stuck in the chimney

**In the cut:** `starting_frames/v30_c05_g1.png` → `clips/v30_c05_g1.mp4`

#### Image prompt — `starting_frames/v30_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `591509cb-6d53-4c2e-b49b-e9df334698be`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210916_591509cb-6d53-4c2e-b49b-e9df334698be.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c05_g1.png` · Higgsfield media `0f0bd301-46da-449b-a256-fc8baa127215`

````text
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a BRICK-RED painted clapboard two-storey with crisp white trim, white window frames and a charcoal-grey roof, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: SANTA IS STUCK IN THE CHIMNEY. In the middle of the lit area sits a fat BRICK CHIMNEY drawn in red and orange bulbs with a chunky stone cap. Santa has gone in HEAD-FIRST and is wedged: only his RED TROUSERS, his BLACK BELT with a big gold buckle and his two LEGS stick straight up out of the chimney mouth, kicked wide apart in a V, both boots mid-kick, ONE BLACK BOOT FLYING OFF above him with a red-and-white striped sock underneath. A puff of grey soot bursts out around his waist. Two chunky curved motion arcs sweep from each kicking boot to show them thrashing.

STANDING ON THE ROOF EITHER SIDE OF HIM: on the LEFT a GREEN ELF doubled over laughing, one hand on his belly, the other pointing straight at Santa's legs, mouth wide open. On the RIGHT a second elf in a blue coat with both hands on his cheeks and two huge round white eyes, and a tipped-over SACK spilling brightly coloured presents down the roof slope. A few gold stars and snowflakes scattered around. The whole scene is one piece of light art on the wall.

3. Different foreground: a low snow-capped STONE WALL along the bottom left and a shovelled path with a snowbank either side leading to the house.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated across the picture. The presents especially must be many different bright colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole picture sits within the curtain rectangle with a clear band of dark unlit wall above it, below it and at both sides. Santa's kicking boots and the flying boot do not touch the top edge, the stone wall and the spilled presents do not touch the bottom edge, and neither elf touches the side edges. Nothing lit appears on the roof, the trim, the sky or the window frames.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the brick-red clapboard wall behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the clapboard texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v30_c05_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `7b545f4b-bf63-43aa-8346-b41be0b67652`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013132_7b545f4b-bf63-43aa-8346-b41be0b67652.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v30_c05_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c05_g1.png` · Higgsfield media `591509cb-6d53-4c2e-b49b-e9df334698be`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same BRICK-RED painted clapboard two-storey house with crisp white trim and white window frames and a charcoal-grey roof, same low snow-capped STONE WALL at the bottom-left, same shovelled path with a snowbank either side, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing a fat brick CHIMNEY in red and orange bulbs with a chunky stone cap and SANTA STUCK HEAD-FIRST IN IT — only his RED TROUSERS with a BLACK BELT and gold buckle and his two LEGS sticking up, kicked apart in a V, both boots mid-kick, ONE BLACK BOOT FLYING OFF with a red-and-white striped sock underneath, a grey soot puff around his waist and two chunky curved motion arcs; at the LEFT a green ELF doubled over laughing with one hand on his belly and the other pointing at Santa's legs; at the RIGHT an elf in a blue coat with both hands on his cheeks and two huge round white eyes, a tipped-over SACK spilling coloured presents down the roof slope beside him.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the stone wall, the snowbanks and the shrubs at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

MOVEMENT — the animation on the wall is already ON and running at full speed in the very first frame and is STILL running in the last frame. A CLEARLY DIFFERENT POSE EVERY HALF SECOND, the figures fully redrawing between beats like a hand-drawn light-bulb sign:
0.0-0.5s — Santa's two legs scissor open and closed hard, the striped sock whipping, the grey soot puff around his waist bursting bigger.
0.5-1.0s — both legs swing hard to the LEFT together, knees bent, the motion arcs redrawing on that side; the laughing elf slaps his knee.
1.0-1.5s — both legs swing hard to the RIGHT, the flying boot tumbling end over end higher up; the blue-coated elf's hands fly off his cheeks and up over his head.
1.5-2.0s — one knee drives down and STAMPS the stone chimney cap so three orange bricks pop loose and jump, soot bursting out in a ring.
2.0-2.5s — both legs snap bolt upright together, straight and stiff, the striped sock wobbling on the end of the foot and every scattered star twinkling out and back in a rolling wave.
2.5-3.0s — the laughing elf falls right over onto his back, both arms windmilling and both boots in the air, while Santa's legs bicycle furiously.
3.0-3.5s — the SECOND boot is kicked clean off and tumbles away, and the spilled presents bounce down the roof slope, each one CHANGING COLOUR as it lands.
3.5-4.0s — one huge final double kick, both legs flung out into the widest V of the whole clip, both elves' arms thrown straight up, soot bursting, and the whole picture flashing brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once — the legs, a boot, the soot, an elf, the presents, the stars. The picture is never still for even one tenth of a second. A static or barely-moving picture is a total failure.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the brick-red clapboard front facade wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No leg, no boot, no elf's arm, no brick, no present and no star ever crosses outside the curtain rectangle. If a pose would take a limb out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Nothing spills onto the white trim, the window frames, the roof, the sky or the neighbouring houses. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail.

HARD RULES: no people, no cars, no pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C06 — Garage door + crowd — the tug-of-war

**In the cut:** `starting_frames/v30_c06_g1.png` → `clips/v30_c06_g2.mp4`

#### Image prompt — `starting_frames/v30_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `f5e27666-14d4-4e32-a6e1-b630a8866728`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210915_f5e27666-14d4-4e32-a6e1-b630a8866728.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c06_g1.png` · Higgsfield media `63a2e39f-ba00-457e-b1d2-0302fbe6c6e2`

````text
Same shot as the attached image - same camera, same distance, same house-with-attached-double-garage-door composition, same crowd of onlookers in silhouette along the bottom, same snow, same night. Keep the camera and the staging EXACTLY.

CHANGE TWO THINGS ONLY:

A) THE HOUSE COLOURS: the house is now TERRACOTTA RED BRICK with white trim, and the wide double garage door is DEEP FOREST GREEN with white panel edges, instead of the colours in the reference.

B) THE PICTURE IN THE LIGHTS - throw it away completely and replace it with a much funnier, much wilder and MUCH MORE COLOURFUL cartoon scene, drawn chunky and simple out of the bulbs and filling the lit area fully.

THE NEW SCENE - A TUG-OF-WAR TO PULL SANTA OUT OF THE CHIMNEY:

On the FAR RIGHT of the lit area stands a fat BRICK CHIMNEY in red and orange bulbs. Santa's RED TROUSERS, BLACK BELT and two LEGS stick straight up out of it, stretched long and thin like elastic, both boots pointing at the sky, a puff of grey soot around his waist.

A thick ROPE is knotted round his ankles and runs in a dead straight, bar-tight diagonal all the way ACROSS THE PICTURE to the LEFT, with a couple of frayed strands popping off it. STRUNG ALONG THAT ROPE, ALL LEANING BACK AT A STEEP ANGLE, HEELS DUG IN: first THREE GREEN ELVES in different coloured coats - hot pink, turquoise, yellow - gripping the rope with both hands, teeth gritted, one with his hat over his eyes; then behind them FOUR REINDEER in a line, front legs braced, back legs skidding, bodies tilted right back, the front one with a BIG BRIGHT RED GLOWING NOSE. Little white spray puffs burst from under every skidding boot and hoof.

CHAOS AROUND THEM: six or seven PRESENTS knocked loose and tumbling through the air, each a DIFFERENT BRIGHT COLOUR - emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow, two of them burst open with little coloured shapes spilling out. One elf has been yanked clean off his feet and is flying horizontally along the rope. Curved multicoloured speed lines streak behind the tumbling presents, and bright stars in many colours are scattered right across the lit area so almost none of it is empty.

COLOUR IS THE POINT: this is a loud multicoloured light show - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated. It must NOT be mostly one or two colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit door above it, below it and at both sides. Nothing lit appears on the brickwork, the roof, the sky, the hedge or the snow.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the forest-green garage door behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the brick texture of the house and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v30_c06_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `38e18b4d-f979-4215-92fa-cfd6c0f001bb`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_104612_38e18b4d-f979-4215-92fa-cfd6c0f001bb.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v30_c06_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c06_g1.png` · Higgsfield media `f5e27666-14d4-4e32-a6e1-b630a8866728`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same TERRACOTTA RED BRICK house with white trim, same DEEP FOREST-GREEN double garage door with white panel edges, same driveway throwing coloured light back, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing THE TUG-OF-WAR: at the FAR RIGHT a fat brick CHIMNEY with Santa's RED TROUSERS, BLACK BELT and two LEGS stretched long and thin like elastic, both boots to the sky and a grey soot puff round his waist; a thick ROPE knotted round his ankles running dead straight and bar-tight diagonally across to the LEFT with frayed strands popping off it; along that rope, leaning back steeply with their heels dug in, THREE GREEN ELVES in hot pink, turquoise and yellow coats, one with his hat pulled down over his eyes, and then FOUR REINDEER with front legs braced and back legs skidding, the lead one with a BIG BRIGHT RED GLOWING NOSE; white spray puffs under every boot and hoof; six or seven PRESENTS tumbling loose, each a different bright colour, two burst open; one elf yanked off his feet flying horizontally along the rope; curved multicoloured speed lines and stars scattered across.

ABSOLUTELY NO FLASHING — HARD BAN, AND THE MOST IMPORTANT RULE IN THIS PROMPT ALONGSIDE THE MOTION RULE. Nothing in this video flashes, strobes, blinks, twinkles, pulses, sparkles, shimmers or changes brightness. The lit picture holds ONE SINGLE STEADY BRIGHTNESS for the entire four seconds. There is no brightness pulse, no flash on the last beat, no flashing or blinking red nose, no twinkling stars or presents, no bulbs winking on and off decoratively, no chase effect, no sparkle effect, no glow-up, no fade in and no fade out. The lead reindeer's red nose stays CONSTANTLY and EVENLY lit and never blinks. EVERY BIT OF MOTION IN THIS VIDEO COMES FROM THE FIGURES PHYSICALLY MOVING AND REDRAWING INTO NEW POSES — never from lights changing brightness. Bulbs switch on or off ONLY in order to draw a figure in a new position.

ABSOLUTE FIRST RULE — THE LIT PICTURE IS TRAPPED INSIDE THE CURTAIN RECTANGLE. In the reference image the lit LED curtain is a rectangle hanging across the forest-green garage door only, and it stops short of the door's edges. That rectangle is FIXED for the whole four seconds: it never grows, never widens, never rises, never rescales, never warps, never drifts, and the camera never changes size on it. Santa's legs, the rope, every elf, every reindeer, every present and every star are drawn INSIDE that rectangle with a clear band of unlit dark door left all the way round — a generous margin at the top, and margins at the left, right and bottom.
NOTHING LIT EVER CROSSES AN EDGE. No boot, no hoof, no rope end, no present and no star ever touches or crosses the edge of the curtain, and nothing lit ever appears on the terracotta brick, the white trim, the gables, the roof or the sky. At every instant every figure keeps a clear margin of at least two full unlit strands of dark door inside every edge of the curtain. If a pose would take a limb or a prop out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, filmed from behind the group at the bottom of the driveway. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE. The house and the garage door stay exactly the same size in frame from the first frame to the last.

THE CROWD IS CASUAL, RELAXED AND ALREADY HAPPY — AND ALREADY MOVING IN THE VERY FIRST FRAME. This is not an audience waiting for something to happen. Nobody is standing frozen staring at the garage in anticipation, nobody holds still and then reacts, there is no build-up and no big synchronised cheer. They are neighbours hanging about on a driveway on a cold night, chatting to each other, laughing at each other, sipping drinks, glancing over at the lights and then back at their friends. Their attention drifts on and off the garage the whole time. They are ALL seen FROM BEHIND — no face is ever turned toward camera.
AT 0.0s, IN THE VERY FIRST FRAME, EVERY PERSON IS ALREADY MID-MOVEMENT. There is NO still opening frame, NO frozen first beat, NO pause before the motion starts, NO moment where the group holds and waits. Someone is already mid-laugh, someone is already turning, someone is already raising a cup, a child is already bouncing. The clip starts in the middle of the action and never settles.
CONTINUOUS OVERLAPPING MOTION, EVERY HALF SECOND, NEVER IN UNISON — at any instant several different people are doing several different things, and their little actions start and stop at different times so the group always looks alive:
0.0-0.5s — a child near the front is already bouncing on the spot and swings an arm up toward the garage mid-bounce; two adults beside them are mid-conversation, heads turned to each other, one shrugging.
0.5-1.0s — a woman in the centre laughs and rocks back on her heels, shoulders shaking; a man at the right is already filming on his phone and shifts his weight to his other foot; someone lifts a takeaway cup and drinks.
1.0-1.5s — the kids in the front row lean into each other and one points lazily at the lights without turning round; a teenager at the left shoves both hands deeper into their pockets, hunches, and blows out a long fog of breath.
1.5-2.0s — a woman at the left leans sideways into the person beside her and says something; they both laugh; another person scratches under their bobble hat and looks away from the garage entirely.
2.0-2.5s — two people knock shoulders and one claps once, casually; a child in a bobble hat twists round to tug a sleeve, then swings back; a couple sway slightly, arms linked.
2.5-3.0s — scattered easy laughter ripples through the group, a few loose claps at different moments, not together; one adult crouches down to say something to a kid; another points out at the lights with a cup still in hand.
3.0-3.5s — the man at the right lowers his phone, wipes his eyes laughing and says something sideways; a kid scrambles up onto their knees; two heads tip together.
3.5-4.0s — a few people applaud loosely, hats bobbing, breath fogging, someone waves an arm overhead at a neighbour, someone else is already turning to talk to the person behind them.
Coats crease, hats bob, breath fogs, snow compresses under boots, shoulders shake with laughter. NOBODY IS EVER STILL and nobody is waiting.

THE ARTWORK IS THE MAIN EVENT AND IT IS FRANTIC. It is already animating in the very first frame — mid-cycle at 0.0s, not switching on and not holding still — and it redraws COMPLETELY EVERY QUARTER SECOND. SIXTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each one a big obvious physical change, never a small twitch:
0.25s — the whole team heaves back in one huge pull, every elf and reindeer leaning much further over, white spray bursting up under all their feet.
0.50s — the rope twangs bar-tight and vibrates along its whole length, frayed strands whipping off it, and Santa's legs stretch visibly longer.
0.75s — Santa's boots scissor apart into a wide V and swing back together, and the soot ring round his waist puffs outward.
1.00s — the hot-pink elf loses his footing, his legs shoot out from under him and he swings up off the ground hanging from the rope by both hands.
1.25s — all four reindeer plant their front hooves and skid backwards a full body-length, snow spraying up in long arcs behind them.
1.50s — the yanked elf tumbles over and over horizontally along the rope, his pointed hat spinning away separately end over end.
1.75s — the lead reindeer throws his head back, tosses his antlers, then shakes his whole body from nose to tail.
2.00s — the turquoise elf's boots gouge two deep furrows in the snow and he drops onto one knee, hauling hand over hand.
2.25s — the chimney leans over with the strain, three orange bricks popping loose and tumbling, and Santa's legs stretch to their longest.
2.50s — Santa's legs SNAP back shorter, hauling the whole team forward two staggering steps, everybody stumbling the same way.
2.75s — two of the tumbling presents burst open into white star-shaped splats and their ribbons unspool into long curls.
3.00s — the remaining presents all CHANGE COLOUR at once and their curved dotted paths redraw at new angles.
3.25s — the yellow-coated elf is hauled clean off his feet and flies horizontally, boots kicking, and the rope slackens into a deep curve for a beat.
3.50s — all four reindeer rear up on their hind legs together, front hooves pawing the air, and the rope whips taut again.
3.75s — every scattered star spins on the spot and changes colour as it turns, and the soot ring bursts wider.
4.00s — one huge final combined heave: rope bar-tight, every boot and hoof braced, Santa's legs at full stretch, the chimney at its steepest lean of the whole clip.
Every pose change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing, never a crossfade. The coloured reflections on the driveway shift and ripple with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — the rope, Santa's legs, each of the three elves separately, each of the four reindeer, the presents, the bricks, the stars. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE. This must read as frantic, chaotic, laugh-out-loud cartoon slapstick with something big happening everywhere you look.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the deep forest-green garage door behind it: its horizontal panel seams, its white panel edges, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE GARAGE DOOR IS THE ONLY LIT SURFACE. The artwork is hard-cropped at all four edges of the curtain. It NEVER grows, shrinks, shifts, warps or drifts. Nothing spills onto the terracotta brick, the white trim, the gables, the roof or the sky.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C06 on disk (1)**

#### Video prompt — `clips/v30_c06_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `94487f23-dc7a-4716-9dd7-fb34ff094cc6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013134_94487f23-dc7a-4716-9dd7-fb34ff094cc6.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c06_g1.png` · Higgsfield media `f5e27666-14d4-4e32-a6e1-b630a8866728`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same TERRACOTTA RED BRICK house with white trim, same DEEP FOREST-GREEN double garage door with white panel edges, same driveway throwing coloured light back, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing THE TUG-OF-WAR: at the FAR RIGHT a fat brick CHIMNEY with Santa's RED TROUSERS, BLACK BELT and two LEGS stretched long and thin like elastic, both boots to the sky and a grey soot puff round his waist; a thick ROPE knotted round his ankles running dead straight and bar-tight diagonally across to the LEFT with frayed strands popping off it; along that rope, leaning back steeply with their heels dug in, THREE GREEN ELVES in hot pink, turquoise and yellow coats, one with his hat pulled down over his eyes, and then FOUR REINDEER with front legs braced and back legs skidding, the lead one with a BIG BRIGHT RED GLOWING NOSE; white spray puffs under every boot and hoof; six or seven PRESENTS tumbling loose, each a different bright colour, two burst open; one elf yanked off his feet flying horizontally along the rope; curved multicoloured speed lines and stars scattered across.

ABSOLUTE FIRST RULE — THE LIT PICTURE IS TRAPPED INSIDE THE CURTAIN RECTANGLE. In the reference image the lit LED curtain is a rectangle hanging across the forest-green garage door only, and it stops short of the door's edges. That rectangle is FIXED for the whole four seconds: it never grows, never widens, never rises, never rescales, never warps, never drifts, and the camera never changes size on it. Santa's legs, the rope, every elf, every reindeer, every present and every star are drawn INSIDE that rectangle with a clear band of unlit dark door left all the way round — a generous margin at the top, and margins at the left, right and bottom.
NOTHING LIT EVER CROSSES AN EDGE. No boot, no hoof, no rope end, no present and no star ever touches or crosses the edge of the curtain, and nothing lit ever appears on the terracotta brick, the white trim, the gables, the roof or the sky. If a pose would take a limb or a prop out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, filmed from behind the group at the bottom of the driveway. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE. The house and the garage door stay exactly the same size in frame from the first frame to the last.

THE CROWD IS CASUAL, RELAXED AND ALREADY HAPPY — AND ALREADY MOVING IN THE VERY FIRST FRAME. This is not an audience waiting for something to happen. Nobody is standing frozen staring at the garage in anticipation, nobody holds still and then reacts, there is no build-up and no big synchronised cheer. They are neighbours hanging about on a driveway on a cold night, chatting to each other, laughing at each other, sipping drinks, glancing over at the lights and then back at their friends. Their attention drifts on and off the garage the whole time. They are ALL seen FROM BEHIND — no face is ever turned toward camera.
AT 0.0s, IN THE VERY FIRST FRAME, EVERY PERSON IS ALREADY MID-MOVEMENT. There is NO still opening frame, NO frozen first beat, NO pause before the motion starts, NO moment where the group holds and waits. Someone is already mid-laugh, someone is already turning, someone is already raising a cup, a child is already bouncing. The clip starts in the middle of the action and never settles.
CONTINUOUS OVERLAPPING MOTION, EVERY HALF SECOND, NEVER IN UNISON — at any instant several different people are doing several different things, and their little actions start and stop at different times so the group always looks alive:
0.0-0.5s — a child near the front is already bouncing on the spot and swings an arm up toward the garage mid-bounce; two adults beside them are mid-conversation, heads turned to each other, one shrugging.
0.5-1.0s — a woman in the centre laughs and rocks back on her heels, shoulders shaking; a man at the right is already filming on his phone and shifts his weight to his other foot; someone lifts a takeaway cup and drinks.
1.0-1.5s — the kids in the front row lean into each other and one points lazily at the lights without turning round; a teenager at the left shoves both hands deeper into their pockets, hunches, and blows out a long fog of breath.
1.5-2.0s — a woman at the left leans sideways into the person beside her and says something; they both laugh; another person scratches under their bobble hat and looks away from the garage entirely.
2.0-2.5s — two people knock shoulders and one claps once, casually; a child in a bobble hat twists round to tug a sleeve, then swings back; a couple sway slightly, arms linked.
2.5-3.0s — scattered easy laughter ripples through the group, a few loose claps at different moments, not together; one adult crouches down to say something to a kid; another points out at the lights with a cup still in hand.
3.0-3.5s — the man at the right lowers his phone, wipes his eyes laughing and says something sideways; a kid scrambles up onto their knees; two heads tip together.
3.5-4.0s — a few people applaud loosely, hats bobbing, breath fogging, someone waves an arm overhead at a neighbour, someone else is already turning to talk to the person behind them.
Coats crease, hats bob, breath fogs, snow compresses under boots, shoulders shake with laughter. NOBODY IS EVER STILL and nobody is waiting.

THE ARTWORK IS ALREADY ANIMATING IN THE FIRST FRAME — it is mid-cycle at 0.0s, not switching on and not holding still, and it changes again at 0.2s. THE ARTWORK ANIMATES THROUGHOUT, redrawing fully between beats:
0.2s — the whole team heaves back together in one big pull, every elf and reindeer leaning further, spray puffs bursting under all their feet.
0.6s — the rope twangs bar-tight and vibrates, frayed strands popping off it, and Santa's legs stretch visibly longer.
1.0s — Santa's boots kick apart into a wide V and the soot puff around his waist bursts out in a ring.
1.4s — the elf yanked off his feet tumbles over and over horizontally along the rope, his pointed hat spinning away separately.
1.8s — the lead reindeer's big red nose FLASHES three times in quick succession and he tosses his antlers.
2.2s — the elf with his hat over his eyes loses his grip and all three elves slip backwards a step together, heels skidding, spray flying.
2.6s — Santa's legs stretch to their longest and SNAP back shorter, the chimney leaning over with the strain and three orange bricks popping loose.
3.0s — two of the tumbling presents burst open in white star-shaped splats and the rest all CHANGE COLOUR at once.
3.4s — all four reindeer rear up on their hind legs, the rope slackens into a curve for a beat, and every scattered star twinkles out and back.
3.8s — one huge final combined heave, rope bar-tight again, every boot and hoof braced, and the whole picture flashes brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing. The coloured reflections on the driveway shift and ripple with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once — the rope, Santa's legs, an elf, a reindeer, a present, the stars. The picture is never still for even one tenth of a second. A static or barely-moving picture is a total failure.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the deep forest-green garage door behind it: its horizontal panel seams, its white panel edges, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE GARAGE DOOR IS THE ONLY LIT SURFACE. The artwork is hard-cropped at all four edges of the curtain. It NEVER grows, shrinks, shifts, warps or drifts. Nothing spills onto the terracotta brick, the white trim, the gables, the roof or the sky.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C07 — Car-window POV — he pops like a cork

**In the cut:** `starting_frames/v30_c07_g1.png` → `clips/v30_c07_g1.mp4`

#### Image prompt — `starting_frames/v30_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `24b2cf14-ccee-43ca-90bc-8066b7dbc684`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210915_24b2cf14-ccee-43ca-90bc-8066b7dbc684.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `40058517-9846-48c1-88e3-d48519a63b52`

````text
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a DARK OLIVE-GREEN board-and-batten gable with cream trim and cream window frames, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: SANTA POPS OUT OF THE CHIMNEY LIKE A CORK. High in the upper half of the lit area SANTA is blasting UPWARD out of a fat brick chimney, flipped UPSIDE DOWN in mid-air, arms and legs splayed out wide like a starfish, mouth wide open in a big round O, eyes as two white circles, his red hat gone and his white beard streaming straight up past his face, both boots off and tumbling separately. A big chunky multicoloured STARBURST of straight rays fires out behind him. A ring of grey soot puffs and loose orange BRICKS bursts outward from the chimney mouth below him.

BELOW, THE ROPE HAS SNAPPED: two frayed rope ends whip apart in opposite curls, and along the bottom of the picture the whole pulling team lies FLAT ON THEIR BACKS in a heap - THREE GREEN ELVES and FOUR REINDEER piled over each other, legs and hooves sticking straight up in the air, one elf with a present landed on his face. PRESENTS RAIN DOWN across the whole scene, eight or nine of them, each a DIFFERENT BRIGHT COLOUR - emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow, two burst open. Small gold stars scattered around. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

3. A different parked car at the kerb - a CHERRY-RED station wagon instead of the car in the reference - and a snow-covered hedge at the right edge.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit gable above it, below it and at both sides. Santa and the starburst do not touch the top edge, the pile of elves and reindeer does not touch the bottom edge, and nothing touches the side edges. Nothing lit appears on the roof, the trim, the window frames or the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the olive-green gable behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the board-and-batten texture and the wet road reflections clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v30_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `d1e50146-528b-4cf9-9734-ec147f60a00f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013219_d1e50146-528b-4cf9-9734-ec147f60a00f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v30_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_30_assets/starting_frames/v30_c07_g1.png` · Higgsfield media `24b2cf14-ccee-43ca-90bc-8066b7dbc684`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same view shot from inside a moving car through the open passenger side window with the dark window frame framing the bottom-left corner, same wet reflective road throwing long smeared coloured reflections, same snowy verge, same street lamp, same row of neighbouring houses glowing down the street, same CHERRY-RED STATION WAGON parked at the kerb, same snow-covered hedge at the right edge, same DARK OLIVE-GREEN board-and-batten gable with cream trim and cream window frames carrying the lit LED curtain, which shows SANTA POPPING OUT OF THE CHIMNEY LIKE A CORK: Santa blasting UPWARD out of the chimney, flipped UPSIDE DOWN, arms and legs splayed like a starfish, his mouth a big round O and his eyes two white circles, his red hat gone, his white beard streaming straight up, both boots off and tumbling separately; a big chunky multicoloured STARBURST of straight rays behind him; a ring of grey soot puffs and loose orange BRICKS bursting out of the chimney mouth; and below him the rope SNAPPED with two frayed ends whipping apart in opposite curls, THREE GREEN ELVES and FOUR REINDEER flat on their backs in a heap with legs and hooves in the air, one elf with a present landed on his face, eight or nine PRESENTS raining down each a different bright colour with two burst open, and gold stars scattered around.

CAMERA — HANDHELD VERTICAL PHONE VIDEO SHOT OUT OF A MOVING CAR SIDE WINDOW AT NIGHT. THE CAR IS DRIVING FORWARD and closing in on the house, so the gable wall grows steadily and continuously LARGER across the four seconds and NEVER recedes. Real vehicle motion: the road surface and the snow verge flow past the bottom of frame at speed, roadside objects sweep past with strong parallax, the frame rocks gently with the suspension. As the car advances the operator slowly pans right to hold the lit wall in frame. THIS IS DRIVING, NOT ZOOMING: no focal length change, no digital zoom, no gimbal glide, no drone move, and the car never stops, never rolls to a halt and never reverses.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove and no device anywhere in the foreground. Only the car's own dark window frame, exactly as in the reference image, sits at the bottom-left.

MOVEMENT — THE PICTURE MUST NOT STAND STILL. Santa stays in the same place in the upper half of the picture and never drifts across the curtain, but nothing in the artwork is static for even one beat. This is the most important instruction in this prompt: a CLEARLY DIFFERENT POSE EVERY HALF SECOND, the figures fully redrawing between beats like an animated light-bulb sign.
0.0-0.5s — Santa half-spins in the air, his splayed limbs swinging round, and the starburst behind him refires with its rays at completely new angles.
0.5-1.0s — his two loose boots tumble away in opposite directions, fresh soot bursts from the chimney mouth and three more orange bricks pop loose and jump.
1.0-1.5s — his arms and legs snap in tight to his body and then fling back out into the widest starfish of the clip, the starburst double-flashing behind him.
1.5-2.0s — the two snapped rope ends whip apart bigger and curl, and three sets of elf legs kick in the heap below while one reindeer rolls right over onto his side.
2.0-2.5s — the raining presents drop a full row down the picture, two of them bursting open in white star splats and the rest all CHANGING COLOUR at once.
2.5-3.0s — Santa turns a full slow somersault upside down, his beard streaming round with him, and every gold star twinkles out and back in a rolling wave from left to right.
3.0-3.5s — the elf with the present on his face kicks it off and it spins away, more bricks pop out of the chimney, and two reindeer wave all four hooves in the air.
3.5-4.0s — Santa flings into the widest starfish of all, the starburst blazes at full size with every ray extended, every hoof and boot in the heap kicks at once, soot bursts, and the whole picture flashes brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. The coloured reflections on the wet road shift and streak with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once — Santa, the starburst, the bricks and soot, the rope ends, the heap of elves and reindeer, the falling presents, the stars. The picture is never still for even one tenth of a second. A static or barely-moving picture is a total failure.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the dark olive-green board-and-batten gable wall". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the wall behind it: its board seams, its cream trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No boot, no splayed arm, no starburst ray, no brick, no rope end, no present and no star ever crosses the roof edge or the corner of the wall — every pose keeps a clear margin of dark wall inside the rectangle. If a pose would take a limb or a ray out to an edge, THE POSE IS MADE SMALLER so it stays inside; the rectangle is never made bigger to fit it. Nothing spills onto the roof, the cream trim, the sky, the verge, the parked cherry-red station wagon, the snow-covered hedge or the neighbouring houses. As the car gets closer the bulb grid simply becomes coarser and the individual bulbs bigger and more countable — the artwork does not gain detail.

HARD RULES: no people and no other vehicles enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Tyres on wet road, a low engine hum, cold air rushing past the open window, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night from a car. Noisy shadows, blown highlights around the bulbs, slight rolling-shutter wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````
