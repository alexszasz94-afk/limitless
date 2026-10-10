# Video 31 — Cat vs the tree

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_31.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

**Historical initial stage:** start frames only. No clips yet, no hook shot.
**Scope:** B-roll only, the same six shots as v20 – v30 — C02 … C07.
**Date:** 2026-09-15
**Model:** `gpt_image_2` · aspect `9:16` · resolution `2k` · quality `medium` · `use_unlim false` · `count 1`
**Output:** 1520 × 2688 PNG, one generation per shot, no re-rolls.

Daniel's brief for this one:

> Now generate me the Broll for video 30 and 31. For these 2 I want funnyer animations, more engaging, also keep in mind that in the next step we need to animate them. They must look very interesting and engaging

Asked what the gag should be, he answered **"be creative"** — the choice was delegated. Asked whether C2 – C4 should change, he answered **"Keep as-is"**: straight v29 format, new cast and a new house, nothing else. **All the comedy lives in C5 – C7.**

Because the next step is animation, both new gag runs were designed around a single test: *looking at the still, can you tell exactly what the next second of motion is?* Every beat is built from a held physical force — stalk, topple, aftermath — plus in-frame motion cues the model can actually draw: dotted aim-lines and trajectory arcs, speed lines, bottled-out tail, a figure caught mid-lunge.

**The gag — cat vs the tree**, a three-beat story across C5 → C6 → C7:

| Beat | Shot | What happens | What animates next |
|---|---|---|---|
| 1 | C05 | Ginger cat crouched flat in full stalk, back end wiggling, tail straight up, one paw lifted and reaching, eyes locked on a dangling red bauble. A dotted aim-line runs paw → bauble. Dog asleep behind, oblivious. | The pounce. |
| 2 | C06 | Cat halfway up the trunk with all four legs wrapped round it, tree leaning hard left mid-topple, gold star flung off, baubles flying on dotted arcs, Santa lunging flat out to catch it, elf diving, dog bolting out of frame. | The tree hits the floor. |
| 3 | C07 | Tree flat on its side, wrecked. Cat sitting bolt upright on the trunk, smug, tail curled round his paws, the gold star crooked on his head. Santa flat on his back with boots in the air, elf gawping, dog's face poking in at the corner. | Nothing — this is the punchline, held. |

---

#### The v31 look

**The woman (C2, C3)** — late twenties, deep brown skin, BLACK BOX BRAIDS gathered into a high bun.
Indoors: mustard-yellow oversized knit jumper, light-wash wide-leg jeans.
Outdoors: cream teddy-fleece coat, dark green cargo trousers, rust-orange beanie, chocolate-brown boots.

**The room (C2)** — pale limewashed plank floor, tan leather sofa with a cream sheepskin and olive-green cushions, terracotta plaster wall behind, black iron lantern pendant, tall slim real green spruce with red gingham bows and warm white lights at the right.

**The house (C3, C4 — the same building)** — two-storey family home with an attached garage wing. **Dark charcoal-grey board-and-batten siding** with visible vertical battens, crisp white trim, soft white sectional double garage door with recessed panels and a row of small square windows across the top, black coach lanterns, white gutter and downpipe, pale grey roof, covered porch on white posts, **mustard-yellow front door**, concrete driveway with patchy snow.

**The showcase houses** — C5 white-painted brick two-storey with black trim and a black roof; C6 honey-toned cedar shingle with a **deep navy** double garage door and black iron strap hinges; C7 pale grey stone gable with white trim and a teal-blue camper van at the kerb.

**Carried over, unchanged** — the curtain wire is **BLACK** with dark unlit bulbs; the lit curtain is always **separate hanging vertical strands with dark gaps, never an LED panel**; the artwork stays inside the curtain rectangle; **absolutely no text** anywhere in the lights; every prompt closes on the explicit sharpness block.

**New for v30/v31** — the **"COLOUR IS THE POINT"** paragraph is now in **all three** lit shots, not just C6.

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

Same split-reference fix as v30: ref 1 owns the framing, **ref 2 (the new C3 job) owns the house**, with an explicit DO-NOT-COPY clause on the first image's siding colour, siding type and front-door colour.

---

## C02 — Box over the sofa

Refs: v20 C2 frame (geometry) + v29 C2 job (camera height).

**Frame:** `v31_c02_g1.png`

### Image prompt

```
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. The box is a closed rigid printed gift box with NO transparent window and NO cut-out panel anywhere on it. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: a late-twenties woman with deep brown skin and BLACK BOX BRAIDS gathered into a high bun, wearing a MUSTARD-YELLOW oversized knit jumper and LIGHT-WASH wide-leg jeans. The room has a PALE LIMEWASHED PLANK floor, a TAN LEATHER sofa with a cream sheepskin and olive-green cushions, a TERRACOTTA PLASTER wall behind, a BLACK IRON lantern pendant hanging above, and a tall slim REAL GREEN SPRUCE Christmas tree hung with red gingham bows and warm white lights standing at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the knit of her jumper and in the print on the box, clean even indoor light with no blown highlights and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur on the box or on her, NO grain, NO haze, NO soft focus anywhere. Candid UGC, no text overlay, no watermark.
```

---

## C03 — Mounting on the attached garage, day

Refs: v29 C3 g2 frame (close side-on camera, pose, black wire) + **v31 C2 job** (the woman).

**Frame:** `v31_c03_g1.png`

### Image prompt

```
COPY THE CAMERA OF THE FIRST ATTACHED IMAGE EXACTLY - its position, its angle, its height, its closeness and her pose. This is a CLOSE, SIDE-ON shot, not a wide frontal shot.

THE CAMERA IS CLOSE AND OFF TO ONE SIDE, exactly as in the first image: the camera stands near the wall and slightly behind her at roughly waist height, looking ALONG the wall, so the wall runs away from the camera DIAGONALLY - nearest at the bottom-left of the frame and receding to the right, the roof gutter line along the top sloping down towards the right as it goes away, strong oblique one-point perspective. She fills most of the frame height in the right half, her whole body in shot from her boots on the stool up to her raised hands. MUCH CLOSER than a full-house shot: only a short run of the wall is in frame, no full facade, no wide establishing view, no flat square-on frontal view.

HER POSE - copy it from the first image: she stands on a small BLACK two-step folding step stool, seen from BEHIND and slightly to the side, facing the wall, both arms raised in front of her, her hands up at the trim board along the top of the wall as she presses the LED curtain into place. Her weight is on one foot, her back slightly arched.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Long vertical strands of thin BLACK cord with small DARK unlit bulbs hang down the wall to the left of her, and because the camera is close the strands are big in the frame and clearly readable as separate cords. A BIG LOOSE TANGLE of BLACK cord is heaped on the snow at the foot of the stool, spilling out to the left - a real messy nest of wire, obviously dark against the white snow, exactly like the bundle in the first image. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - TAKE HER FROM THE SECOND ATTACHED IMAGE. Same late-twenties woman with deep brown skin and BLACK BOX BRAIDS, now gathered into a low bun spilling out from under a RUST-ORANGE beanie, wearing a CREAM TEDDY-FLEECE coat, DARK GREEN cargo trousers and CHOCOLATE-BROWN boots. It must read as literally the same person as in the second image.

A COMPLETELY NEW HOUSE - take it from this text only, NOT from either attached image. The wall she is working on is the WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR of a two-storey family home - soft WHITE with horizontal panel seams and recessed rectangular panels running away in perspective, and the row of small square windows across the top of the door visible at the far end. Around it, DARK CHARCOAL-GREY board-and-batten siding with crisp WHITE trim, a BLACK COACH LANTERN on the wall, a WHITE gutter and WHITE downpipe, a pale grey roof, and a plain CONCRETE driveway under patchy snow. At the RIGHT of the frame, further away, the corner where the garage wing meets the MAIN HOUSE BODY is visible - the two-storey wall, the covered porch on white posts and the MUSTARD-YELLOW front door - so it reads as ONE house with the garage built into it.

DO NOT COPY THE HOUSE FROM THE FIRST IMAGE: not its warm sand-beige or cream lap siding, not its dark red front door. The first image is there ONLY for the camera, the distance, the angle, the pose and the black wire.

Daytime, overcast winter light, snow on the ground.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the door panels, the texture of her teddy-fleece coat and every strand of black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

---

## C04 — Phone POV, the same house at night

Refs: v29 C4 **g6** frame (the approved framing, night light, iPhone + app) + **v31 C3 job** (the house).

**Frame:** `v31_c04_g1.png`

### Image prompt

```
COPY THE FIRST ATTACHED IMAGE'S CAMERA, FRAMING, DISTANCE, ANGLE AND FOREGROUND PHONE EXACTLY. Night, square-on frontal view of a double garage door, a phone held up big in the bottom-centre foreground. ONE THING CHANGES: it is a DIFFERENT HOUSE, taken from the second attached image.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. The camera is close to the house so the GARAGE DOOR IS BIG AND DOMINATES THE FRAME, spanning almost the full width of the picture with only a NARROW STRIP of white trim and siding visible beyond its left edge and beyond its right edge, only a SHALLOW BAND of siding above its top edge, and only a LOW STRIP of snowy concrete driveway beneath it. But the ENTIRE DOOR STAYS VISIBLE: both vertical side edges inside the frame, the complete top edge inside the frame including the WHOLE row of small square windows running all the way across it with every window visible end to end, and the bottom edge where the door meets the driveway inside the frame. Nothing about the door is cut off by any edge. Do NOT step closer and do NOT step back.

STILL SQUARE-ON FROM THE FRONT: the door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up, NO whole house, NO full facade, NO roofline.

THE HOUSE - TAKE IT FROM THE SECOND ATTACHED IMAGE, NOT FROM THE FIRST. It must read as LITERALLY THE SAME HOUSE as the second image, now seen square-on from the front at night: the same soft WHITE sectional double garage door with its recessed panels and its row of small square windows, and around it DARK CHARCOAL-GREY BOARD-AND-BATTEN siding with crisp WHITE trim and its vertical batten strips clearly visible, BLACK COACH LANTERNS glowing warm on the wall either side of the door, a WHITE gutter, and at the right edge a sliver of the covered porch on its white post with the MUSTARD-YELLOW front door cropped by the frame. The siding must read clearly as a DARK CHARCOAL GREY with vertical battens - NOT cream, NOT white, NOT beige - and it must contrast strongly against the white door and the white trim.

DO NOT COPY THE SIDING COLOUR, THE SIDING TYPE OR THE FRONT DOOR COLOUR FROM THE FIRST IMAGE. The first image is there ONLY for the camera, the framing, the night lighting and the phone.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the door in evenly spaced vertical see-through strands right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale door each strand reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen.

THE PHONE AND ITS SCREEN ARE UNCHANGED - COPY THEM EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same hand, same grip, same angle, same size and same position in the bottom-centre foreground. The screen shows the SAME APP: a dark navy-blue screen with a grid of just TWO COLUMNS of large tiles, two across and about five down, roughly ten tiles in total and no more, each tile nearly half the screen wide with softly rounded corners and a narrow gutter, each one a small photograph of a house decorated in Christmas lights - a lit roofline, a nativity, a snowman, a reindeer, a porch draped in light curtains - mostly icy blue and cool white with a couple of warm tiles, ONE tile ringed with a bright electric-blue outline, and a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE below the grid. NOT a dense grid of tiny icons, NOT three or more columns, NO glyphs or pictograms, and NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

The phone is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

---

## C05 — Lit facade — the stalk

Ref: v29 C5 frame.

**Frame:** `v31_c05_g1.png`

### Image prompt

```
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a WHITE-PAINTED BRICK two-storey with BLACK trim, black window frames and a black roof, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: THE CAT IS ABOUT TO GO FOR THE CHRISTMAS TREE. On the RIGHT of the lit area stands a big triangular GREEN CHRISTMAS TREE hung with round baubles in many bright colours and a gold star on top, a few wrapped presents at its base. Hanging low on the nearest branch, one fat round RED BAUBLE dangles on a visible thread and swings slightly.

On the LEFT, a fat GINGER CAT is crouched flat to the floor in full stalking pose - shoulders hunched, back end raised and wiggling, TAIL STRAIGHT UP with a kink at the tip, two enormous round WHITE EYES locked dead on that red bauble, whiskers forward, ONE FRONT PAW LIFTED AND REACHING with the claws just out. A dotted curved aim-line runs from the raised paw to the dangling bauble. Behind the cat a small brown DOG lies fast asleep in a curl, completely oblivious, with a couple of little sleep-puff curls above his nose. A few gold stars and snowflakes scattered around. The whole scene is one piece of light art on the wall.

3. Different foreground: a low picket fence capped with snow along the bottom left and a shovelled path with a snowbank either side leading to the house.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated. The baubles on the tree especially must be many different bright colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole picture sits within the curtain rectangle with a clear band of dark unlit wall above it, below it and at both sides. The star on the tree does not touch the top edge, the presents and the sleeping dog do not touch the bottom edge, and neither the cat nor the tree touches the side edges. Nothing lit appears on the roof, the trim, the sky or the window frames.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the white brick wall behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the painted brick texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

## C06 — Garage door + crowd — the tree goes over

Ref: v29 C6 frame.

**Frame:** `v31_c06_g1.png`

### Image prompt

```
Same shot as the attached image - same camera, same distance, same house-with-attached-double-garage-door composition, same crowd of onlookers in silhouette along the bottom, same snow, same night. Keep the camera and the staging EXACTLY.

CHANGE TWO THINGS ONLY:

A) THE HOUSE COLOURS: the house is now HONEY-TONED CEDAR SHINGLE siding with white trim, and the wide double garage door is DEEP NAVY BLUE with black iron strap hinges, instead of the colours in the reference.

B) THE PICTURE IN THE LIGHTS - throw it away completely and replace it with a much funnier, much wilder and MUCH MORE COLOURFUL cartoon scene, drawn chunky and simple out of the bulbs and filling the lit area fully.

THE NEW SCENE - THE CAT HAS GOT INTO THE CHRISTMAS TREE AND IT IS GOING OVER:

A big GREEN CHRISTMAS TREE stands off-centre, LEANING HARD OVER TO THE LEFT at a steep angle, mid-topple, its trunk bent and its branches whipping. A fat GINGER CAT clings halfway up the trunk with all four legs wrapped round it, eyes two huge round white circles, mouth open, tail bottled out fat and straight, a length of silver TINSEL wound round his body and trailing behind. The GOLD STAR has been flung off the top and tumbles through the air.

BAUBLES FLY EVERYWHERE - eight or nine of them launched off the branches in every direction on curved dotted paths, each a DIFFERENT BRIGHT COLOUR: emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - three of them bursting into white star-shaped splats where they hit.

THE PANIC AROUND IT: on the LEFT, SANTA is lunging in flat out with both arms stretched to catch the falling trunk, mouth wide open, one boot off the ground, his red hat flying off behind him. Under the tree a GREEN ELF is diving belly-first with both hands over his head. On the BOTTOM RIGHT a small brown DOG bolts out of frame at full sprint, ears flat back, legs stretched fore and aft, with three curved speed lines behind him. Wrapped presents at the base are scattering loose, each a different bright colour with a contrasting ribbon and bow.

Curved multicoloured speed lines streak behind the flying baubles, and bright stars in many colours are scattered right across the lit area so almost none of it is empty.

COLOUR IS THE POINT: this is a loud multicoloured light show - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated. It must NOT be mostly one or two colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit door above it, below it and at both sides. Nothing lit appears on the cedar siding, the roof, the sky, the hedge or the snow.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the navy garage door behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the cedar shingle texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

## C07 — Car-window POV — the cat has won

Ref: v29 C7 frame.

**Frame:** `v31_c07_g1.png`

### Image prompt

```
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a PALE GREY STONE gable with crisp white trim and white window frames, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: THE CAT HAS WON. Across the BOTTOM of the lit area the CHRISTMAS TREE lies FLAT ON ITS SIDE, wrecked - trunk horizontal, branches splayed and bent, tinsel spilling off it, baubles scattered loose around it in many bright colours with two of them cracked cleanly in half.

Sitting BOLT UPRIGHT ON TOP of the fallen trunk, right in the middle of the picture, is the fat GINGER CAT - chest out, tail curled neatly round his front paws, eyes half-closed into two smug curved slits, a tiny satisfied smile. The GOLD STAR from the top of the tree sits CROOKED ON HIS HEAD like a party hat, and a strand of silver tinsel is draped over one ear.

Beside him on the LEFT, SANTA lies FLAT ON HIS BACK in the wreckage with both boots up in the air, arms out wide, eyes as two spiral swirls, a bright bauble clutched in each hand and his red hat over one eye. On the RIGHT a GREEN ELF peers in from the edge with both hands pressed to his cheeks and a wide open mouth. A small brown DOG's face pokes in low at the bottom right corner, just his eyes and nose showing. Small gold stars scattered around. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated. The scattered baubles especially must be many different bright colours.

3. A different parked car at the kerb - a TEAL-BLUE camper van instead of the car in the reference - and a snow-covered hedge at the right edge.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit gable above it, below it and at both sides. The star on the cat's head does not touch the top edge, the fallen tree does not touch the bottom edge, and nothing touches the side edges. Nothing lit appears on the roof, the trim, the window frames or the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the pale grey stone gable behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the stone texture and the wet road reflections clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

#### Generated set

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v31_c02_g1.png` | C02 | `64297a9f-2cf8-496a-945f-19ae9e5728c8` | 310201 | completed, first attempt |
| `v31_c03_g1.png` | C03 | `5c64a1b2-4023-4b70-b3ad-949aebad8bcf` | 310301 | completed, first attempt |
| `v31_c04_g1.png` | C04 | `ad72a429-34b2-4810-b545-7cc215182d87` | 310401 | completed, first attempt |
| `v31_c05_g1.png` | C05 | `35c7fadf-a111-44a5-85bd-6dde594338e2` | 310501 | completed, first attempt |
| `v31_c06_g1.png` | C06 | `4f451b00-4d75-4018-81df-983f08b36274` | 310601 | completed, first attempt |
| `v31_c07_g1.png` | C07 | `51cc4d69-b280-4be2-86cc-86d96d35e32c` | 310701 | completed, first attempt |

All six 1520 × 2688 RGB PNG, downloaded from the result URLs into `starting_frames/`.

---

#### Submission notes

- Workspace **Oneofone1** (`b2c97bd7-fedf-489d-b211-3de4e39dc90a`).
- Submitted in three waves alongside v30: the eight independent jobs first, then both C3s off their C2 jobs, then both C4s off their C3 jobs.
- No `declined_preset_id` resubmission, no "Preset was recommended instead", no `ip_detected`. All twelve v30 + v31 jobs completed on the first attempt.

---

#### Open points for review

- **C04's siding rendered pale grey-white, not dark charcoal board-and-batten.** Same drift as v30 C04 and as v29 C04 g4/g5/g6 — the night C4 chain keeps pulling the siding towards cream no matter how the text is worded, even with the house handed over on its own reference and an explicit DO-NOT-COPY clause. C03 got the charcoal right. Next lever to try: drop the v29 framing reference entirely and chain C4 off C3 alone, or put the siding assertion before the framing block.
- **C06's curtain reads as a dense mosaic rather than separate strands**, same as v30 C06, and the deep navy garage door is completely hidden behind it. The busiest of the three gag scenes is the one that loses the strand look; C05 and C07 both hold it.
- **C05 reads a little calm** next to the other two — the stalk beat is by design the quiet one, but the cat's body and the tree sit slightly small in the rectangle with a lot of dark wall around them. Fine if the animation pushes in; worth noting if not.
- Everything else lands: the three-beat gag reads in sequence, C07 is the strongest frame of the set, C02/C03 hold the same woman, C03/C04 hold the same house geometry, the wire is black throughout, no text anywhere in the lights.

No re-runs were made. One generation per shot, then review.

---

## C01 — HOOK — night doorbell camera, man stepping out onto icy steps

**Frame:** `starting_frames/v31_c01_g1.png` (1520 x 2688)
**Job id:** `b99bfde6-3c59-432e-8ce5-1f6a4702005b`
**Model:** gpt_image_2 · 2k · quality medium · 9:16 · 1 generation
**References:** ref 1 = Daniel's night doorbell-cam snow screenshot (`6c7b9fa5-65d3-4237-b3ec-4fce6b51976b`) — camera, fisheye, composition, night lighting. ref 2 = approved packshot `product_images/box_nowindow/box_nowindow_g5.png` (`2812fa88-3367-4746-a761-4e99c42b73d1`) — the box.

This frame is the "before" state for the fall — he is mid-stride at the top of the icy steps, the slip happens in the video, not in the still.

**Prompt**

Reproduce the FIRST attached image's camera, viewpoint, lens, composition and night lighting as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a FRONT-DOOR DOORBELL CAMERA at night in deep snow. Keep the same house, the same porch, the same snowy garden, the same mood.

THE CAMERA - copy it from the first image: a doorbell camera mounted high above the front door, looking DOWN at a steep angle onto the porch, the front steps and the path below. Strong wide-angle fisheye so the straight lines bow noticeably outward at the edges and the ground falls away beneath the lens. Fixed, static, unmanned, looking-down viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE FIRST IMAGE, just re-stacked for a vertical frame:
- LEFT: the cream-painted wall and column of the covered porch, and the WHITE PANELLED FRONT DOOR standing OPEN, swung outward toward the camera, with WARM ORANGE LIGHT from inside the house spilling out through the opening and washing across the porch floor and down onto the top steps.
- BESIDE THE DOOR on the porch: a small real Christmas tree in a pot, strung with warm white fairy lights and glowing softly, and on the floor next to it a small lantern casting a soft PINK-MAGENTA glow onto the wall.
- RIGHT: a WHITE PICKET PORCH RAILING with square capped posts, its top rail and every picket capped with a ridge of fresh snow.
- CENTRE AND BOTTOM: the flight of STONE PAVER FRONT STEPS leading down from the porch, four or five wide steps, each tread carrying packed snow and a glassy sheen of ICE where the warm doorway light catches it.
- BEYOND AND ABOVE: the front garden under deep untouched snow, a curving shovelled path cut through it leading away from the foot of the steps, low snow-covered shrubs, and beyond that the dark blue-black winter night.

THE ONE CHANGE - SOMEONE IS COMING OUT OF THE HOUSE. A MAN has just stepped out through the open doorway onto the TOP STEP, lit from behind and from the side by the warm light pouring out of the house, seen from ABOVE and slightly behind because of the camera angle so his face is barely visible. He wears a charcoal-grey puffer jacket, dark jeans and brown boots. He is caught MID-STRIDE at the very top of the steps: his leading boot is already reaching out over the first icy tread and coming down flat on it, his other foot still on the porch, his weight thrown forward and his shoulders ahead of his hips. One boot heel skims the ice. He is looking down over what he is carrying, not at his feet.

HE IS CARRYING A STACK OF THE PRODUCT BOXES FROM THE SECOND ATTACHED IMAGE - THREE of them, copied exactly from that second image: flat MATTE BLACK rigid retail boxes, on the front a large white condensed uppercase headline, a warm gold subline under it, a small red diagonal ribbon flag in the top-right corner, one large photographic panel with a thin gold hairline border filling the middle and lower two thirds showing a night photo of a suburban house facade lit with Christmas lights, and a bottom row of five small gold line icons. Closed and sealed - NO transparent window, NO clear plastic panel, NO cutout, nothing visible inside.

THE STACK: the three boxes are stacked one on top of another and hugged against his chest with both arms wrapped under and around them, tilted back against his body so the PRINTED BLACK FRONT FACE of the top box is angled up toward the camera and clearly readable in the warm doorway light. Each box is WIDE - about 55 cm across, wider than his own shoulders - so the stack sticks out past both sides of his body and blocks his view of his own feet. Real weight, arms straining, the stack leaning. Every box is the same matte black box - NOT brown cardboard, NOT red, NOT green, NOT white, NOT generic parcels, NOT patterned Christmas packaging.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K FULL-COLOUR night doorbell-camera still, tack-sharp edge to edge, crisp fine detail in the snow crystals on the railing, in the ice sheen on the steps and in the print on the boxes. Beautiful clean night lighting: warm orange light from the open doorway as the key, the soft warm white of the little tree and the pink lantern as accents, cool deep blue moonlit snow beyond - bright, rich and properly exposed, no blown-out white where the doorway light hits the snow and no crushed black in the garden, correct white balance, real shadows thrown down the steps. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO black-and-white infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.

**Note:** the boxes are an addition beyond Daniel's brief (he only asked for "someone comes out of the house and falls down the stairs") — they give the fall something to scatter and tie the hook to the product. Say the word and it regenerates without them.


---

## C04 revision — 2026-09-16

Daniel's brief:

> C4 - I just want denser led lines on the garages
>
> Also when we try to animate this shot most of the times it's completly going wrong [...] Let's create an intermediate image with the animation that we will add as reference alongside with the starting frame when we generate the clip. Here is how it should look: exact same framing, hand and phone out of the frame, camera just a little upper (because it's a held iphone shot and the person filming tilts up the camera a little bit so the focus it's on animation), and an animation on the leds like the one in C7 in terms of how it looks, but different animation, the animation must be visible on the entire garage door

Two new frames for this shot. **`v31_c04_g2.png` replaces `v31_c04_g1.png` as the start frame.**

Asked what the animation should be, he answered **"be creative, it must be something funny"** — the scene was delegated again, one unique scene per video. Asked how much denser, he chose **roughly double**.

### Why the second image exists

C04 is the shot that keeps breaking in animation, and the break is always on the garage door — the model has to invent the lit artwork from nothing while also holding the phone, the hand and the door geometry, and it invents something different every attempt. So the lit end state is now **generated as a still first** and passed to the video model as a second reference. At clip time both images go in: `v31_c04_g2.png` is the **start frame**, `v31_c04_r1.png` is the **second reference** — the target the lights resolve to. The clip is then only a lights-on transition plus the small handheld tilt up, not an invention.

The animation frame is deliberately **not** a valid start frame on its own: the hand and phone are gone and the camera has tilted up, because that is where the shot ends, not where it begins.

### C04 g2 — denser strands

Ref: **v31 C4 g1 job** (`ad72a429-34b2-4810-b545-7cc215182d87`) — the whole approved shot. One thing changes: roughly double the strand count.

**Frame:** `v31_c04_g2.png`

#### Image prompt

```
COPY THE ATTACHED IMAGE EXACTLY. Same house, same soft white sectional double garage door, same dark charcoal-grey board-and-batten siding, same white trim, same black coach lanterns glowing warm either side, same snowy concrete driveway, same night light, same camera, same framing, same distance, same square-on angle, same foreground hand holding the same iPhone in the bottom-centre with the SAME two-column app grid and the same round blue play button. Everything is already correct and must be reproduced unchanged.

ONE SINGLE THING CHANGES: THE LED CURTAIN HAS ROUGHLY TWICE AS MANY STRANDS. In the attached image the vertical strands hanging over the garage door are spaced widely apart. Here they are packed about TWICE AS CLOSE TOGETHER - roughly double the number of strands across the same width, so the curtain reads as a much DENSER set of vertical lines running down the whole face of the door.

THE STRANDS THEMSELVES ARE UNCHANGED: each one is still a thin BLACK cord carrying small DARK unlit bulbs, the lights are OFF with no glow, and against the pale door each cord reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. They still hang from the trim board above the door, still span the full width of the door edge to edge, still have a slight natural sag and a slightly uneven bottom hem.

STILL A CURTAIN, NEVER A PANEL - CRITICAL: even at double the density these are SEPARATE HANGING VERTICAL STRANDS with clear DARK GAPS between them, and the garage door behind is plainly visible through those gaps - the recessed panel seams and the row of small square windows across the top must still read clearly through the curtain. Do NOT close the gaps. Do NOT turn it into a solid LED panel, a flat screen, a mesh, a net, a grille or a fabric sheet. Do NOT add horizontal wires. The strands run straight up and down only.

THE FRAMING IS ALREADY CORRECT - DO NOT CHANGE IT. The garage door stays big and dominant, spanning almost the full width of the picture, with the ENTIRE door visible: both vertical side edges inside the frame, the complete top edge including the WHOLE row of small square windows end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT tilt. Still square-on from the front: the panel seams run dead level and the door edges run straight up and down.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every individual black cord clearly readable and clearly separated from its neighbours, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### C04 animation reference

Refs: **v31 C4 g2 job** (`5b6ccb8c-453d-4df2-9cc5-f2973f5605ab`) for the scene + **v31 C7 g1 job** (`51cc4d69-b280-4be2-86cc-86d96d35e32c`) for the bulb-art drawing style only.

The scene is a **snowball fight** — a snowman winding up on the left, three elves behind a snow wall on the right, one taking a snowball full in the face, snowballs crossing the middle on dotted arcs. Built the same way as the C5–C7 gags: a held physical force plus in-frame motion cues (speed lines, dotted arcs, a figure caught mid-air) so the next second of motion is unambiguous from the still.

**Frame:** `v31_c04_r1.png`

#### Image prompt

```
TAKE THE FIRST ATTACHED IMAGE AS THE SCENE. Same house, same soft white sectional double garage door with its recessed panels and its row of small square windows across the top, same dark charcoal-grey board-and-batten siding, same white trim, same black coach lanterns glowing warm either side of the door, same snowy concrete driveway, same night. Same camera, same lens, same distance, same square-on frontal angle. TAKE THE SECOND ATTACHED IMAGE ONLY FOR THE DRAWING STYLE OF THE LIGHTS - the way the cartoon is built out of small round coloured bulbs. DO NOT COPY THE SECOND IMAGE'S HOUSE, ITS GABLE, ITS VAN, ITS ROAD OR ITS SCENE. Only its bulb-art look.

THREE THINGS CHANGE FROM THE FIRST IMAGE:

1. THE HAND AND THE PHONE ARE GONE. There is nothing at all in the foreground. No hand, no arm, no sleeve, no phone, no screen, no glow from a screen. The bottom-centre of the frame is simply the empty snowy driveway. The whole garage door is completely unobstructed from edge to edge.

2. THE CAMERA HAS TILTED UP A LITTLE. This is a handheld iPhone shot and the person filming has tipped the phone up slightly so the lights fill the frame. The framing is otherwise identical - same distance, same square-on frontal angle, the door still faces the camera flat with its horizontal panel seams dead level and its vertical edges straight up and down - but the whole frame has shifted UP: there is now only a THIN sliver of driveway along the bottom edge, and a slightly DEEPER band of siding and trim above the top of the door. The ENTIRE garage door stays inside the frame: both side edges, the complete top edge with the WHOLE row of small square windows visible end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT turn it into a low angle looking up at the roofline, do NOT show the whole house.

3. THE LED CURTAIN IS SWITCHED ON AND SHOWING A BRIGHT CARTOON ANIMATION. The same dense curtain of closely spaced vertical strands hanging over the garage door, but now every bulb is lit and together they draw a picture.

THE PICTURE - A SNOWBALL FIGHT, drawn chunky and simple out of the bulbs, running RIGHT ACROSS THE WHOLE GARAGE DOOR: on the LEFT a big fat three-ball SNOWMAN with a carrot nose, coal eyes and a black top hat, leaning hard into a throw with one bare twig arm cocked right back over his head holding a huge snowball and the other twig arm flung forward for balance. On the RIGHT, THREE GREEN ELVES crouched behind a low lumpy snow wall: one popping up mid-throw with his own snowball, one ducking with both hands over his pointed hat, and one who has just been hit FULL IN THE FACE - a white splat starburst across his head, his hat blown straight off and spinning away, arms flung up, legs off the ground. FOUR OR FIVE SNOWBALLS fly across the middle of the door between them, each trailing a curved dotted trajectory arc and short speed lines. Loose snow puffs burst off the top of the snow wall. Small gold stars scattered through the gaps. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

THE PICTURE FILLS THE ENTIRE GARAGE DOOR: the snowman reaches the left edge of the door, the elves and their snow wall reach the right edge, and the figures plus the flying snowballs plus the stars fill the FULL HEIGHT of the door from just under the row of square windows down to the bottom edge. Every part of the door is covered by lit artwork - no large dark empty areas anywhere on the door, and nothing is confined to a small panel in the middle. Nothing lit appears above the door, on the trim, on the siding, on the lanterns or in the sky.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. The strands are densely spaced but there are still clear DARK GAPS between them and the white garage door behind is plainly visible through those gaps, especially in the unlit areas - the recessed panel seams and the row of square windows must still read through the curtain. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the garage door panels and the snowy driveway clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v31_c04_g2.png` | C04 start frame | `5b6ccb8c-453d-4df2-9cc5-f2973f5605ab` | 310402 | completed, first attempt |
| `v31_c04_r1.png` | C04 animation ref | `d610c7e3-058c-4061-915f-bec202ac9161` | 310421 | completed, first attempt |

Both 1520 × 2688 PNG. Workspace **Oneofone1**. One generation each, no re-rolls. No `declined_preset_id`, no preset recommendation, no `ip_detected`.

### Open points for review

- **The siding is still pale grey-white, not charcoal.** g2 was generated off g1, which carried the drift, and the brief was density only — so it was left alone rather than fixed unasked. Still worth a separate pass if it matters.
- **The animation frame pulled back very slightly** — a little more siding either side of the door than in g2. The tilt up and the door's position in frame are right; the distance is a touch off. Fine as a colour/artwork reference, worth a note if the clip inherits the wider framing.
- The conga line / snowball scene is one generation, unreviewed. If either scene is wrong, it is cheap to re-run — the prompt only needs its middle paragraph swapped.

### C01 — g2 (Daniel: "the man must not be visible — he goes out the door in the animation; and the stairs don't make sense")

**Frame:** `starting_frames/v31_c01_g2.png` · **Job id:** `bf68164d-b412-4eb3-986e-9ef4e681e416` · same model/params · **ref = the night doorbell screenshot only** (packshot dropped, no product in frame now).

Two changes from g1:

1. **No person, no boxes.** Opening block is now: "THE FRAME IS COMPLETELY EMPTY OF PEOPLE. There is NO person anywhere in this image, NO figure in the doorway, NO silhouette inside the house, NO one on the porch, NO one on the steps, NO one on the path. Nobody. The porch and the steps are deserted and waiting." The whole courier + three-box stack section was deleted. The man walks out during the video.
2. **Stairs re-laid on the door axis** (Daniel's pick): "The flight of front steps runs STRAIGHT DOWN AND STRAIGHT AWAY FROM THE OPEN DOORWAY, directly in line with it... so that anyone stepping out of that door walks straight forward onto the top step and straight down the flight. The steps do NOT run off to one side, they do NOT turn, there is NO landing that makes you turn a corner." White picket railings now run down BOTH sides of the flight like banisters.

Ice on the treads promoted to "the point of the shot - make it read clearly as slick and treacherous."

**Open point on g2:** the geometry is right and the ice reads, but the front door came out closed rather than open, and the little lit Christmas tree is sitting directly in the doorway blocking the exit. If that matters for the animation, the fix is a one-clause edit: door standing wide open with the hallway light spilling out, tree moved to the side of the porch clear of the threshold.

### C01 — g3 (Daniel rejected g2 outright: "you completely messed everything… it should be something kinda like in the attached screenshot with the stairs in front of the house")

**Frame:** `starting_frames/v31_c01_g3.png` · **Job id:** `fd4ec070-be80-4dd3-9dbc-50574492a4d6`
**Model:** gpt_image_2 · 2k · quality medium · 9:16 · 1 generation
**References:** ref 1 = **Daniel's new night-porch screenshot** (`d12b3f10-6b4b-45d0-8fab-9905847f4481`) — this replaces the original doorbell screenshot and now owns the whole geometry. ref 2 = packshot `box_nowindow_g5.png` (`2812fa88-3367-4746-a761-4e99c42b73d1`).

**What was wrong with g1/g2:** both had the steps running straight DOWN AND AWAY from the door. Daniel's layout is the opposite — the steps run **along the front of the house**, parallel to it, descending across the lower right of the frame, with the porch and door off to the left. g2 also had the door closed with the tree blocking it.

**The layout, copied from his screenshot and now locked:**
- LEFT: covered porch, open front door far left with warm hallway light spilling out, doormat, shoes beside the door.
- ON THE PORCH: small potted Christmas tree with warm white fairy lights against the railing, small lantern with a faint pink-magenta glow.
- MIDDLE/RIGHT: white picket railing with square capped newel posts, snow ridged on every cap, running along the porch edge AND down the outside of the steps.
- THE STEPS RUN ALONG THE FRONT OF THE HOUSE, NOT AWAY FROM IT — wide concrete treads descending toward the bottom-right corner, packed snow and a glassy sheen of ICE on each one.
- UPPER RIGHT: snowy front yard, curving shovelled path, dark fence line, blue-black night, distant warm streetlight.
- LOWER RIGHT: a stack of three matte black boxes sitting on a snowy tread, top face angled up and readable (full packshot description + the windowless negatives carried as usual).

**No person**, per Daniel's call — he walks out of the door and slips during the video. The prompt spends a whole paragraph on it: "Remove the man who stands in the doorway in the first image… NO hand on the railing, NO shadow or reflection of a person."

### C01 — g4

Fix for Daniel's g3 note: *"It's looking very weird and fucking distorted and unnatural"*. Diagnosis: the "strong wide-angle fisheye so the straight lines bow noticeably outward" clause carried over from g1 was what warped the railings, inflated the newel post and melted the step edges. g4 drops fisheye entirely and leads the prompt with a geometry block plus an explicit list of the g3 failures as bans.

- Job id: `35ffea43-ad5d-4516-8e4b-714137e34aec`
- Model: gpt_image_2, 2k, quality medium, 9:16, count 1 → 1520x2688
- Refs: `d12b3f10-6b4b-45d0-8fab-9905847f4481` (Daniel's night-porch screenshot — governing geometry), `2812fa88-3367-4746-a761-4e99c42b73d1` (approved windowless packshot)
- Output: `starting_frames/v31_c01_g4.png`

New blocks at the head of the prompt:

> GEOMETRY AND REALISM - THIS IS THE MOST IMPORTANT INSTRUCTION. The architecture must be perfectly solid, square and believable, like a real photo taken by a real camera of a real house. Use a NORMAL wide-angle lens with only very slight barrel distortion. Straight edges stay straight. The porch railing is a straight, rigid, factory-made run of vinyl picket fence: every picket is the same width, the same length and perfectly vertical, evenly spaced, all in one flat straight plane; the newel posts are true square columns standing plumb and vertical with flat caps, all the same size. The steps are a normal concrete flight: each tread is a flat rectangle with a crisp straight front edge, all the treads the same depth and the same height, stacked in an even regular stair. The porch floor is flat and level. The door frame is square.
>
> BANNED, these ruined the last attempt: NO fisheye warping, NO bending or curving of railings, posts, steps or walls, NO melted or sagging or rubbery geometry, NO step edges that dissolve into each other, NO railing that grows out of the ground at the wrong angle, NO giant out-of-scale newel post, NO floating or unsupported parts, NO impossible or contradictory perspective, NO objects merging into one another, NO smeared or blobby surfaces. Everything obeys ordinary perspective and gravity.

Layout, no-people block, box block and quality block unchanged from g3.

**Lesson:** any "fisheye / lines bow outward" language in a doorbell-cam prompt buys authenticity at the cost of architectural collapse. Ask for a normal wide-angle with slight barrel distortion instead, and list the specific warps as bans.

### C01 — g5

Daniel on g4: *"remove that christmas tree and the boxes and it's good"*. Geometry from g4 kept verbatim; only the two removals added.

- Job id: `3f4dd818-c00a-47e8-8edf-20c32b8852db`
- Model: gpt_image_2, 2k, quality medium, 9:16, count 1 → 1520x2688
- Refs: `d12b3f10-6b4b-45d0-8fab-9905847f4481` (Daniel's night-porch screenshot) — packshot ref dropped, there is no box in this frame
- Output: `starting_frames/v31_c01_g1.png`

Blocks added vs g4 (and the whole box paragraph deleted):

> NO CHRISTMAS TREE. Remove the small potted Christmas tree that stands on the porch in the attached image - there is NO tree, NO potted plant, NO pot, NO shrub and NO string of fairy lights on the porch. Show the plain empty porch floor where it stood.
>
> NOTHING ON THE STEPS. The concrete steps are completely clear and empty - NO boxes, NO parcels, NO packages, NO bags, NO deliveries, NO decorations, NO objects of any kind on any tread. Just clean snow and ice on bare concrete.

The porch line was also trimmed to just the lantern: "a small metal lantern standing on the floor near the door throwing a faint warm glow. Otherwise the porch floor is bare and empty."

## C01 — CLIP (from v31_c01_g1.png)

Daniel's brief: *"Fix stable camera. A man walks out from the house with our boxes in his hand, kinda like the delivery guy from v29 (to know how he is carrying them), and he falls on the stairs. The man wears a christmas hat."*

- Job id: `ee39c6c7-1dce-4224-a761-b4f487b969b0`
- Model: seedance_2_5, mode omni_reference, 720p, 9:16, 5s, generate_audio true
- Start image: job `3f4dd818-c00a-47e8-8edf-20c32b8852db` (`starting_frames/v31_c01_g1.png`)
- Output: `clips/v31_c01_g1.mp4` (720x1280, 5.04s)
- **Submission note:** first attempt came back "Preset NIGHT VISION was recommended instead of submitting a job". Resubmitted identical with `declined_preset_id: 0b8cb55f-1475-4229-a8ce-974a8f369f2f` and it went through. No credits spent on the refusal.

### Timeline

| time | beat |
|---|---|
| 0.0–0.6s | porch empty, then he steps out of the lit doorway on the left |
| 0.6–1.8s | crosses the porch away from camera toward the top step, boots on concrete, breath steaming, boxes blocking his view of his own feet |
| 1.8–2.6s | reaches the top step and starts down without looking, feeling for the tread |
| 2.6–3.5s | front boot skids on the ice, both feet go at once, he lands on his back and hip and bumps down two or three treads; boxes burst out and slide into the snow; the Santa hat flies off; one arm grabs at the railing and misses |
| 3.5–5.0s | sprawled across the lower steps, legs higher than his head, props on one elbow and looks at the scattered boxes, breathing hard |

The carry is copied verbatim from the V29 clip prompt so the two men hold the stack the same way. The geometry lock from the g5 still prompt is repeated inside the video prompt as a motion rule — "the railing pickets stay perfectly vertical and evenly spaced, the posts stay plumb, the step treads keep their crisp straight front edges. Nothing bends, warps, melts or breathes" — plus a ban on the Christmas tree reappearing on the porch.

## C01 — CLIP g5b (product boxes)
Job `ac42ae8f-7dec-4aee-9182-56415cbbdb57` · seedance_2_5 · omni_reference · 720p / 9:16 / 5s
generate_audio true · use_unlim false · declined_preset_id `0b8cb55f-1475-4229-a8ce-974a8f369f2f`
medias: start_image `3f4dd818-c00a-47e8-8edf-20c32b8852db` (v31_c01_g1.png)
        image_references `2812fa88-3367-4746-a761-4e99c42b73d1` (box_nowindow_g5 packshot)
Out: `clips/v31_c01_g2.mp4` — 720x1280, 5.042s
Why: Daniel — "he must cary our boxes so add a reference with it and it's sizes". g5 only
described the boxes in prose, so they rendered as generic black blocks.
Fix = attach the packshot as image_references (seedance_2_5 medias roles are
start_image / end_image / image_references / video_references / audio_references) AND write
a "THE BOXES ARE THE PRODUCT" block: full front-panel description, 55 x 42 x 10 cm, plus a
COUNT/SCALE check — exactly THREE boxes, stacked flat, ~30 cm total, waist to mid-chest,
narrower than his shoulders — plus negatives (no person-sized boxes, no tall cubes, no
brown parcels, no unprinted boxes) and the standard windowless negatives.
Submission notes: first attempt refused with preset recommendation "NIGHT VISION"
(0b8cb55f-...) — resubmitted identical with that as declined_preset_id. Second attempt came
back `nsfw`, which is the usual transient Higgsfield glitch; resubmitting the identical
prompt went through. Neither costs credits.

## C01 — FRAME g6 (man + boxes now IN the start frame)

**Job:** `0e746074-b300-4065-8747-66d86ecbb384` — gpt_image_2, 2k, quality medium, 9:16, 1520x2688
**Refs (role `image`, NOT `image_references` — gpt_image_2 only accepts `image`):**
- `3f4dd818-c00a-47e8-8edf-20c32b8852db` — v31_c01_g1.png, layout + look
- `2812fa88-3367-4746-a761-4e99c42b73d1` — box_nowindow_g5.png, packshot

**Why:** Daniel rejected `v31_c01_g2.mp4` — "looking fake as fuck". Root cause: `v31_c01_g1.png`
is an EMPTY PORCH. The man, his body and all three boxes were invented by seedance from prose
alone, so the boxes came out door-sized and his body melted into a shapeless mass during the
fall. Same rule as the v29 door: a thing that must move has to exist in the start frame.

**Prompt:** "reproduce the FIRST attached image EXACTLY … change ONE thing only" + add the man
mid-stride crossing the porch with the three-box stack cradled in both forearms + a SCALE CHECK
block (one box = large-laptop-box slab, three stacked ~30 cm, waist to mid-chest, does not reach
his chin, narrower than his shoulders, upper arms visible either side) + banned list (not
person-sized / suitcase / door-sized / tall cubes / brown kraft / window / falling / sitting).

**Status:** awaiting Daniel. Open concern: the stack still reads as ONE oversized printed slab
held at his side rather than three flat boxes cradled in both forearms.

## C01 — CLIP g5c (pause on the first stair removed)

Job `4476886c-05f5-4586-b12b-16c6bddf8420` · seedance_2_5 · omni_reference · 720p / 9:16 / 5s
generate_audio true · use_unlim false · declined_preset_id `0b8cb55f-1475-4229-a8ce-974a8f369f2f`
medias: start_image `3f4dd818-c00a-47e8-8edf-20c32b8852db` (v31_c01_g1.png — UNCHANGED)
        image_references `2812fa88-3367-4746-a761-4e99c42b73d1` (box_nowindow_g5 packshot)
Out: `clips/v31_c01_g3.mp4` — 720x1280, 5.042s

**Daniel:** "it looked a little faked when the boxes dropped and the man kinda waited for half a
second on the first stair. These might be problems from the ai video model… Check is there is
anything wrong with your prompt, if not resumbmit the same prompt."

**Prompt bug found — one line, and it was mine.** The g5b timeline said:
> 1.8-2.6s - He reaches the top step and starts down without looking, feeling for the tread with his front boot.

"Feeling for the tread" is an explicit instruction to hesitate, given an 0.8s slot. That IS the
half-second wait. Replaced with:
> 1.8-2.6s - He walks straight over the top step and keeps going down the stairs without breaking stride and without looking down. His pace stays exactly the same as it was on the porch. He does NOT stop, does NOT pause, does NOT hesitate, does NOT slow down, does NOT stand still on the first step and does NOT test or feel for the tread - he is moving continuously the whole time.

Every other character of the prompt is byte-identical to g5b. The box-drop note had no prompt
cause — the PHYSICS block already specifies fast, heavy, rigid slabs that bounce and slide — so
that one was left to the re-roll.

**Do NOT regenerate `v31_c01_g1.png`.** Daniel explicitly ruled that out. A g6 frame was made in
error and moved to `video_31_assets/to_delete/`.

## C01 — CLIP g5d (box count locked at 3)

Job `54ca7cfa-f704-4a1c-85d9-2148a6f987f2` · seedance_2_5 · omni_reference · 720p / 9:16 / 5s
generate_audio true · use_unlim false · declined_preset_id `0b8cb55f-1475-4229-a8ce-974a8f369f2f`
medias: start_image `3f4dd818-c00a-47e8-8edf-20c32b8852db` (v31_c01_g1.png — UNCHANGED)
        image_references `2812fa88-3367-4746-a761-4e99c42b73d1` (box_nowindow_g5 packshot)
Out: `clips/v31_c01_g4.mp4` — 720x1280, 5.05s

**Daniel:** "when he gets out of the house he carry 5 boxes and when he falls are only 3, maybe
it was a problem from the model"

**Prompt cause found — stray FIVEs next to the box description.** g5c contained the word "five"
three times: "a row of **five** small gold line icons along the bottom edge" (inside the box
block itself), "one continuous unbroken **five**-second take" and "all **five** seconds". The
only number never stated up front was the box count — "exactly THREE boxes" was buried at the
bottom in the PHYSICS block. Numbers bleed across in seedance, so five won.

**Changes, all count-related:**
1. New block at the VERY TOP of the prompt: "THE BOX COUNT IS LOCKED AT THREE… 3 when he steps
   out. 3 while he walks. 3 in the air as he falls. 3 in the snow at the end. NOT 4. NOT 5. NOT 6."
2. Every "five" deleted: icons are now "a row of small gold line icons"; "five-second take" →
   "one continuous unbroken take"; "all five seconds" → "the whole shot".
3. Every spelled-out THREE changed to the numeral 3 so the count reads as a number, not prose.
4. Count repeated inside EVERY timeline beat ("Count them: 3", "Still exactly 3 boxes", "the
   same 3 boxes - exactly 3, no more", "Exactly 3 boxes lie scattered").
5. BANNED gained: "no fourth box, no extra box, no box appearing or disappearing, no change in
   the number of boxes at any point".
6. While in there, hardened the box-drop physics that Daniel called "a little faked": each box
   is now "a separate rigid object with its own weight… hits a tread, rebounds off it with a
   hard edge-first bounce, tips over and slides", plus negatives "do not float, drift, hover,
   glide, sink slowly… flutter like paper".

The no-pause stair beat from g5c is carried over unchanged.

**LESSON:** a stray numeral anywhere in a seedance prompt can capture an unrelated count. State
the count that matters first, as a numeral, and repeat it per beat. Never leave a competing
number near the object description.

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
| `clips/upscaled/v31_c01_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v31_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v31_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v31_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v31_c05_g2.mp4` | Named derivative of `../v31_c05_g2.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v31_c06_g2.mp4` | Named derivative of `../v31_c06_g2.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v31_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c01_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c01_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c05_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v31_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c06_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v31_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v31_c07_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `references/v31_c04_r1.png` | Embedded PNG `hf-job-id`: `d610c7e3-058c-4061-915f-bec202ac9161`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c01_g1.png` | Embedded PNG `hf-job-id`: `b99bfde6-3c59-432e-8ce5-1f6a4702005b`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c01_g2.png` | Embedded PNG `hf-job-id`: `bf68164d-b412-4eb3-986e-9ef4e681e416`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c01_g3.png` | Embedded PNG `hf-job-id`: `fd4ec070-be80-4dd3-9dbc-50574492a4d6`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c01_g4.png` | Embedded PNG `hf-job-id`: `35ffea43-ad5d-4516-8e4b-714137e34aec`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c01_g5.png` | Embedded PNG `hf-job-id`: `3f4dd818-c00a-47e8-8edf-20c32b8852db`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v31_c02_g1.png` | Embedded PNG `hf-job-id`: `64297a9f-2cf8-496a-945f-19ae9e5728c8`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c03_g1.png` | Embedded PNG `hf-job-id`: `5c64a1b2-4023-4b70-b3ad-949aebad8bcf`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c04_g1.png` | Embedded PNG `hf-job-id`: `ad72a429-34b2-4810-b545-7cc215182d87`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c04_g2.png` | Embedded PNG `hf-job-id`: `5b6ccb8c-453d-4df2-9cc5-f2973f5605ab`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c05_g1.png` | Embedded PNG `hf-job-id`: `35c7fadf-a111-44a5-85bd-6dde594338e2`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c06_g1.png` | Embedded PNG `hf-job-id`: `4f451b00-4d75-4018-81df-983f08b36274`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v31_c07_g1.png` | Embedded PNG `hf-job-id`: `51cc4d69-b280-4be2-86cc-86d96d35e32c`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |

### Unresolved take records

The following 5 files still need exact take provenance or verified derivative lineage. Their presence is documented; their prompts have **not** been invented. MP4 C2PA manifest and instance IDs are authenticity identifiers, not Higgsfield job IDs.

- `clips/upscaled/v31_c05_g2.mp4`
- `clips/upscaled/v31_c06_g2.mp4`
- `clips/v31_c05_g2.mp4`
- `clips/v31_c06_g2.mp4`
- `clips/v31_c07_g2.mp4`

### Recovered take — `starting_frames/v31_c01_g5.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `3f4dd818-c00a-47e8-8edf-20c32b8852db`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
Recreate the attached photograph as a REAL, NATURAL, PHYSICALLY CORRECT night photograph, in a tall vertical 9:16 frame. Keep its scene, its layout and its lighting. Make ONE change: there are NO PEOPLE and NO OBJECTS ON THE STEPS - the porch and the steps are completely empty.

GEOMETRY AND REALISM - THIS IS THE MOST IMPORTANT INSTRUCTION. The architecture must be perfectly solid, square and believable, like a real photo taken by a real camera of a real house. Use a NORMAL wide-angle lens with only very slight barrel distortion. Straight edges stay straight. The porch railing is a straight, rigid, factory-made run of vinyl picket fence: every picket is the same width, the same length and perfectly vertical, evenly spaced, all in one flat straight plane; the newel posts are true square columns standing plumb and vertical with flat caps, all the same size. The steps are a normal concrete flight: each tread is a flat rectangle with a crisp straight front edge, all the treads the same depth and the same height, stacked in an even regular stair. The porch floor is flat and level. The door frame is square.

BANNED: NO fisheye warping, NO bending or curving of railings, posts, steps or walls, NO melted or sagging or rubbery geometry, NO step edges that dissolve into each other, NO railing that grows out of the ground at the wrong angle, NO giant out-of-scale newel post, NO floating or unsupported parts, NO impossible or contradictory perspective, NO objects merging into one another, NO smeared or blobby surfaces. Everything obeys ordinary perspective and gravity.

THE CAMERA: a doorbell camera mounted beside and above the front door, looking DOWN at a moderate angle onto the porch and out over the front steps and the snowy yard, exactly the viewpoint of the attached image. Fixed, static, unmanned. NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

NO PEOPLE AT ALL. Remove the man who stands in the doorway in the attached image. NO person anywhere in this image, NO figure in or near the doorway, NO silhouette inside the house, NO one on the porch, NO one on the steps, NO one on the path, NO hand on the railing, NO shadow or reflection of a person. The porch is deserted. Show the plain porch floor and doorway that were behind him.

NO CHRISTMAS TREE. Remove the small potted Christmas tree that stands on the porch in the attached image - there is NO tree, NO potted plant, NO pot, NO shrub and NO string of fairy lights on the porch. Show the plain empty porch floor where it stood.

NOTHING ON THE STEPS. The concrete steps are completely clear and empty - NO boxes, NO parcels, NO packages, NO bags, NO deliveries, NO decorations, NO objects of any kind on any tread. Just clean snow and ice on bare concrete.

THE LAYOUT - copy it from the attached image:
- LEFT SIDE OF FRAME: the covered porch of the house seen from above. The FRONT DOOR is open on the far left with WARM ORANGE LIGHT from the hallway spilling out across the porch, a rectangular doormat on the concrete porch floor below it, a pair of shoes set neatly beside the door.
- ON THE PORCH: a small metal lantern standing on the floor near the door throwing a faint warm glow. Otherwise the porch floor is bare and empty.
- ALONG THE FRONT EDGE OF THE PORCH: a straight white vinyl picket railing between two square capped posts, a neat ridge of snow lying along the top rail and on each cap.
- THE STEPS RUN ALONG THE FRONT OF THE HOUSE, NOT AWAY FROM IT: a flight of four or five wide concrete front steps begins at the near end of the porch and descends across the lower right of the frame, parallel to the house front, dropping toward the bottom-right corner - exactly the arrangement in the attached image. A matching straight white picket railing runs down the outer side of the flight, stepping down evenly with the treads. Each tread carries packed snow and a glassy sheen of ICE catching the doorway light, with a clean straight visible nosing on every step.
- BEYOND THE RAILING, UPPER RIGHT: the front yard under deep snow, a curving shovelled path, a dark fence line, the blue-black winter night, one distant warm streetlight.

IMAGE QUALITY: a genuinely high-resolution modern 2K FULL-COLOUR night doorbell-camera photograph, tack-sharp edge to edge, crisp real detail in the snow on the railing caps and in the ice on the steps, real photographic texture in the concrete and the vinyl. Warm orange light from the open doorway as the key, cool deep blue moonlit snow beyond - bright, rich and properly exposed, no blown-out white where the light hits the snow, no crushed black in the yard, correct white balance, real cast shadows across the porch and down the steps. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO black-and-white night-vision look, NO low-resolution CCTV mush. Photorealistic - not a render, not a 3D model, not an illustration, not a painting, no cinematic colour grading.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "d12b3f10-6b4b-45d0-8fab-9905847f4481",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/d12b3f10-6b4b-45d0-8fab-9905847f4481.png"
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

- C01: the board did not show the exact image prompt of `v31_c01_g5.png`; it now does.
- C01: the board did not show the exact clip prompt of `v31_c01_g4.mp4`; it now does.
- C02: the board did not show the exact clip prompt of `v31_c02_g1.mp4`; it now does.
- C03: the board did not show the exact clip prompt of `v31_c03_g1.mp4`; it now does.
- C04: the board did not show the exact clip prompt of `v31_c04_g2.mp4`; it now does.
- C05: the board did not show the exact clip prompt of `v31_c05_g2.mp4`; it now does.
- C06: the board did not show the exact clip prompt of `v31_c06_g2.mp4`; it now does.
- C07: the board did not show the exact clip prompt of `v31_c07_g1.mp4`; it now does.

### C01 — Slips on the icy steps

**In the cut:** `starting_frames/v31_c01_g5.png` → `clips/v31_c01_g4.mp4`

#### Image prompt — `starting_frames/v31_c01_g5.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `3f4dd818-c00a-47e8-8edf-20c32b8852db`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_000919_3f4dd818-c00a-47e8-8edf-20c32b8852db.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_31_assets/starting_frames/v31_c01_g5.png` · Higgsfield media `d12b3f10-6b4b-45d0-8fab-9905847f4481`

````text
Recreate the attached photograph as a REAL, NATURAL, PHYSICALLY CORRECT night photograph, in a tall vertical 9:16 frame. Keep its scene, its layout and its lighting. Make ONE change: there are NO PEOPLE and NO OBJECTS ON THE STEPS - the porch and the steps are completely empty.

GEOMETRY AND REALISM - THIS IS THE MOST IMPORTANT INSTRUCTION. The architecture must be perfectly solid, square and believable, like a real photo taken by a real camera of a real house. Use a NORMAL wide-angle lens with only very slight barrel distortion. Straight edges stay straight. The porch railing is a straight, rigid, factory-made run of vinyl picket fence: every picket is the same width, the same length and perfectly vertical, evenly spaced, all in one flat straight plane; the newel posts are true square columns standing plumb and vertical with flat caps, all the same size. The steps are a normal concrete flight: each tread is a flat rectangle with a crisp straight front edge, all the treads the same depth and the same height, stacked in an even regular stair. The porch floor is flat and level. The door frame is square.

BANNED: NO fisheye warping, NO bending or curving of railings, posts, steps or walls, NO melted or sagging or rubbery geometry, NO step edges that dissolve into each other, NO railing that grows out of the ground at the wrong angle, NO giant out-of-scale newel post, NO floating or unsupported parts, NO impossible or contradictory perspective, NO objects merging into one another, NO smeared or blobby surfaces. Everything obeys ordinary perspective and gravity.

THE CAMERA: a doorbell camera mounted beside and above the front door, looking DOWN at a moderate angle onto the porch and out over the front steps and the snowy yard, exactly the viewpoint of the attached image. Fixed, static, unmanned. NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

NO PEOPLE AT ALL. Remove the man who stands in the doorway in the attached image. NO person anywhere in this image, NO figure in or near the doorway, NO silhouette inside the house, NO one on the porch, NO one on the steps, NO one on the path, NO hand on the railing, NO shadow or reflection of a person. The porch is deserted. Show the plain porch floor and doorway that were behind him.

NO CHRISTMAS TREE. Remove the small potted Christmas tree that stands on the porch in the attached image - there is NO tree, NO potted plant, NO pot, NO shrub and NO string of fairy lights on the porch. Show the plain empty porch floor where it stood.

NOTHING ON THE STEPS. The concrete steps are completely clear and empty - NO boxes, NO parcels, NO packages, NO bags, NO deliveries, NO decorations, NO objects of any kind on any tread. Just clean snow and ice on bare concrete.

THE LAYOUT - copy it from the attached image:
- LEFT SIDE OF FRAME: the covered porch of the house seen from above. The FRONT DOOR is open on the far left with WARM ORANGE LIGHT from the hallway spilling out across the porch, a rectangular doormat on the concrete porch floor below it, a pair of shoes set neatly beside the door.
- ON THE PORCH: a small metal lantern standing on the floor near the door throwing a faint warm glow. Otherwise the porch floor is bare and empty.
- ALONG THE FRONT EDGE OF THE PORCH: a straight white vinyl picket railing between two square capped posts, a neat ridge of snow lying along the top rail and on each cap.
- THE STEPS RUN ALONG THE FRONT OF THE HOUSE, NOT AWAY FROM IT: a flight of four or five wide concrete front steps begins at the near end of the porch and descends across the lower right of the frame, parallel to the house front, dropping toward the bottom-right corner - exactly the arrangement in the attached image. A matching straight white picket railing runs down the outer side of the flight, stepping down evenly with the treads. Each tread carries packed snow and a glassy sheen of ICE catching the doorway light, with a clean straight visible nosing on every step.
- BEYOND THE RAILING, UPPER RIGHT: the front yard under deep snow, a curving shovelled path, a dark fence line, the blue-black winter night, one distant warm streetlight.

IMAGE QUALITY: a genuinely high-resolution modern 2K FULL-COLOUR night doorbell-camera photograph, tack-sharp edge to edge, crisp real detail in the snow on the railing caps and in the ice on the steps, real photographic texture in the concrete and the vinyl. Warm orange light from the open doorway as the key, cool deep blue moonlit snow beyond - bright, rich and properly exposed, no blown-out white where the light hits the snow, no crushed black in the yard, correct white balance, real cast shadows across the porch and down the steps. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO black-and-white night-vision look, NO low-resolution CCTV mush. Photorealistic - not a render, not a 3D model, not an illustration, not a painting, no cinematic colour grading.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere.
````

#### Video prompt — `clips/v31_c01_g4.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `54ca7cfa-f704-4a1c-85d9-2148a6f987f2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_104458_54ca7cfa-f704-4a1c-85d9-2148a6f987f2.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v31_c01_g4.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c01_g5.png` · Higgsfield media `3f4dd818-c00a-47e8-8edf-20c32b8852db`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
THE BOX COUNT IS LOCKED AT THREE. The man carries exactly 3 boxes and there are exactly 3 boxes in every single frame of this clip. 3 boxes when he steps out of the door. 3 boxes while he walks. 3 boxes in the air as he falls. 3 boxes lying in the snow at the end. The same 3 boxes the whole time. NOT 4. NOT 5. NOT 6. The number never changes, no box is ever added, duplicated, split or removed.

THE CAMERA NEVER MOVES. This is the single most important rule. The shot is a fixed doorbell camera mounted beside the front door, looking down over the porch and the snowy front steps. It does not pan, tilt, zoom, dolly, orbit, shake, drift, rack focus or re-frame at any moment. The white picket railing, the square posts, the steps, the snowy yard, the fence line and the distant streetlight stay locked in exactly the same place for the whole shot and never shift by a single pixel. Everything that moves in this clip is the man and the 3 boxes. Treat the background as a still photograph. The architecture stays rigid and straight the whole time - the railing pickets stay perfectly vertical and evenly spaced, the posts stay plumb, the step treads keep their crisp straight front edges. Nothing bends, warps, melts or breathes.

Continue the attached start frame as one continuous unbroken take. No cuts, no edits, no transitions, no speed ramps, no slow motion. Same porch, same open door, same warm hallway light, same deep snow, same night as the frame.

THE BOXES ARE THE PRODUCT AND THEY MUST MATCH THE ATTACHED PACKSHOT REFERENCE EXACTLY. Every box in this clip is the flat matte black retail box in the second attached reference image: a wide flat rectangular box, MATTE BLACK on every face, with a white condensed uppercase headline across the top of the front panel, a warm gold subline beneath it, a red diagonal BEST SELLER ribbon across the top-right corner, one rectangular photo panel in the middle framed by a thin gold hairline border, and a row of small gold line icons along the bottom edge. SIZE: each box is 55 cm wide, 42 cm tall and only 10 cm deep - a flat slab, about as wide as the man's chest and only as thick as his hand. Scale check: the man carries a stack of 3 of these boxes lying flat one on top of the other; 3 stacked together are only about 30 cm tall in total, reaching from his waist to the middle of his chest, and the stack is clearly NARROWER than his shoulders. Do NOT render the boxes person-sized, do NOT render them as tall cubes, do NOT render brown cardboard parcels, do NOT render plain unprinted boxes. The printed front panel must stay readable and face the camera as they fall.
BOX NEGATIVES: NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, every box closed and sealed, no open flaps, no tape, no shipping labels, no barcodes, no brown kraft.

THE MAN: he does not exist in the first frame - he comes out of the open doorway. A grown man in a dark winter jacket, jeans and boots, wearing a red and white CHRISTMAS SANTA HAT. He carries the stack of 3 flat matte black product boxes hugged against his chest with BOTH forearms underneath and both hands clamped on the far side, the stack tipped back against his collarbone so the printed front panel of the top box faces up and out toward the camera. He has to lean back slightly to counterweight it and he cannot see his own feet past the load.

THE ACTION, as a timeline:
0.0-0.6s - The porch is empty. Then the man steps out through the open doorway on the left into the warm spill of hallway light, carrying a stack of exactly 3 black product boxes in both arms as described. Count them: 3.
0.6-1.8s - He crosses the porch from the door toward the top of the steps, walking away from the camera and to the right, his boots on the concrete, his breath steaming in the cold. His shadow swings across the porch floor. The gold and white printing on the top box catches the warm doorway light. Still exactly 3 boxes in his arms.
1.8-2.6s - He walks straight over the top step and keeps going down the stairs without breaking stride and without looking down. His pace stays exactly the same as it was on the porch. He does NOT stop, does NOT pause, does NOT hesitate, does NOT slow down, does NOT stand still on the first step and does NOT test or feel for the tread - he is moving continuously the whole time. Still exactly 3 boxes.
2.6-3.5s - HE FALLS. His front boot skids straight out on the ice. Both feet go from under him at once. He drops fast and heavily onto the steps, landing on his back and hip, and slides and bumps down two or three treads. The same 3 black product boxes - exactly 3, no more - burst out of his arms and tumble, flip, bounce and slide down the steps and out into the snow, their printed front panels flashing white and gold as they turn. Each box behaves like a separate rigid object with its own weight: it hits a tread, rebounds off it with a hard edge-first bounce, tips over and slides. His Santa hat flies off and lands on a lower step. One arm shoots up and grabs at the picket railing and misses.
3.5-5.0s - He comes to rest sprawled across the lower steps in the snow, on his back, one knee up, legs higher than his head. Exactly 3 boxes lie scattered around him on the steps and in the snow, one of them face-up with its printed front panel clearly visible to the camera. He lies still for a beat, then lifts his head, props himself on one elbow and looks at the scattered boxes, breathing hard, his breath clouding. He does not get up.

PHYSICS AND REALISM: a real man with real weight, filmed by a real camera. Gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down. The steps are icy and hard. Clothing creases and flaps. The boxes are light, rigid, flat cardboard slabs with hard corners and sharp edges - they bounce off the treads, clatter, tumble end over end and slide to a stop in the snow. They do not float, drift, hover, glide, sink slowly, melt, stretch, bend, flutter like paper, multiply or vanish. They stay rigid and keep their exact shape and size from the moment they leave his arms to the moment they stop. His body stays whole and correctly proportioned throughout - arms and legs bend only at real joints and only the way real joints bend.

BANNED: no fourth box, no extra box, no box appearing or disappearing, no change in the number of boxes at any point, no camera movement of any kind, no zoom, no push in, no handheld shake, no second person appearing, no one else in the doorway, no Christmas tree or potted plant appearing on the porch, no railing or step bending, warping, melting or moving, no rubbery or elastic limbs, no impossible bends, no morphing faces, no extra arms or hands, no floating or hovering boxes, no person-sized boxes, no brown cardboard parcels, no pausing or hesitating on the stairs, no slow motion, no cinematic grade, no lens flare, no text, no timestamp, no watermark, no logos, no captions, no UI.

LOOK: a genuinely sharp modern 2K FULL-COLOUR night doorbell-camera recording, warm orange key light from the open doorway, cool deep blue moonlit snow beyond, bright and correctly exposed, natural colour, crisp detail. Not black-and-white night vision, not low-resolution CCTV mush, not a movie, not a render, not an illustration.

AUDIO: natural outdoor night sound only - his boots on the concrete porch, the scrape of the skid, the heavy thud and bump of his body down the icy steps, the cardboard boxes clattering and sliding, one short involuntary shout from him as he goes down, then his breathing. Cold still winter air underneath. No music, no score, no background song, no narration, no sound effects library stings.
````

**Other takes of C01 on disk (7)**

#### Image prompt — `starting_frames/v31_c01_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `b99bfde6-3c59-432e-8ce5-1f6a4702005b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_232728_b99bfde6-3c59-432e-8ce5-1f6a4702005b.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `6c7b9fa5-65d3-4237-b3ec-4fce6b51976b`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
Reproduce the FIRST attached image's camera, viewpoint, lens, composition and night lighting as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a FRONT-DOOR DOORBELL CAMERA at night in deep snow. Keep the same house, the same porch, the same snowy garden, the same mood.

THE CAMERA - copy it from the first image: a doorbell camera mounted high above the front door, looking DOWN at a steep angle onto the porch, the front steps and the path below. Strong wide-angle fisheye so the straight lines bow noticeably outward at the edges and the ground falls away beneath the lens. Fixed, static, unmanned, looking-down viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

EVERYTHING BELOW STAYS AS IN THE FIRST IMAGE, just re-stacked for a vertical frame:
- LEFT: the cream-painted wall and column of the covered porch, and the WHITE PANELLED FRONT DOOR standing OPEN, swung outward toward the camera, with WARM ORANGE LIGHT from inside the house spilling out through the opening and washing across the porch floor and down onto the top steps.
- BESIDE THE DOOR on the porch: a small real Christmas tree in a pot, strung with warm white fairy lights and glowing softly, and on the floor next to it a small lantern casting a soft PINK-MAGENTA glow onto the wall.
- RIGHT: a WHITE PICKET PORCH RAILING with square capped posts, its top rail and every picket capped with a ridge of fresh snow.
- CENTRE AND BOTTOM: the flight of STONE PAVER FRONT STEPS leading down from the porch, four or five wide steps, each tread carrying packed snow and a glassy sheen of ICE where the warm doorway light catches it.
- BEYOND AND ABOVE: the front garden under deep untouched snow, a curving shovelled path cut through it leading away from the foot of the steps, low snow-covered shrubs, and beyond that the dark blue-black winter night.

THE ONE CHANGE - SOMEONE IS COMING OUT OF THE HOUSE. A MAN has just stepped out through the open doorway onto the TOP STEP, lit from behind and from the side by the warm light pouring out of the house, seen from ABOVE and slightly behind because of the camera angle so his face is barely visible. He wears a charcoal-grey puffer jacket, dark jeans and brown boots. He is caught MID-STRIDE at the very top of the steps: his leading boot is already reaching out over the first icy tread and coming down flat on it, his other foot still on the porch, his weight thrown forward and his shoulders ahead of his hips. One boot heel skims the ice. He is looking down over what he is carrying, not at his feet.

HE IS CARRYING A STACK OF THE PRODUCT BOXES FROM THE SECOND ATTACHED IMAGE - THREE of them, copied exactly from that second image: flat MATTE BLACK rigid retail boxes, on the front a large white condensed uppercase headline, a warm gold subline under it, a small red diagonal ribbon flag in the top-right corner, one large photographic panel with a thin gold hairline border filling the middle and lower two thirds showing a night photo of a suburban house facade lit with Christmas lights, and a bottom row of five small gold line icons. Closed and sealed - NO transparent window, NO clear plastic panel, NO cutout, nothing visible inside.

THE STACK: the three boxes are stacked one on top of another and hugged against his chest with both arms wrapped under and around them, tilted back against his body so the PRINTED BLACK FRONT FACE of the top box is angled up toward the camera and clearly readable in the warm doorway light. Each box is WIDE - about 55 cm across, wider than his own shoulders - so the stack sticks out past both sides of his body and blocks his view of his own feet. Real weight, arms straining, the stack leaning. Every box is the same matte black box - NOT brown cardboard, NOT red, NOT green, NOT white, NOT generic parcels, NOT patterned Christmas packaging.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K FULL-COLOUR night doorbell-camera still, tack-sharp edge to edge, crisp fine detail in the snow crystals on the railing, in the ice sheen on the steps and in the print on the boxes. Beautiful clean night lighting: warm orange light from the open doorway as the key, the soft warm white of the little tree and the pink lantern as accents, cool deep blue moonlit snow beyond - bright, rich and properly exposed, no blown-out white where the doorway light hits the snow and no crushed black in the garden, correct white balance, real shadows thrown down the steps. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO black-and-white infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
````

#### Image prompt — `starting_frames/v31_c01_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `bf68164d-b412-4eb3-986e-9ef4e681e416`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_234738_bf68164d-b412-4eb3-986e-9ef4e681e416.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `6c7b9fa5-65d3-4237-b3ec-4fce6b51976b`

````text
Reproduce the attached image's camera, viewpoint, lens, composition and night lighting as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a FRONT-DOOR DOORBELL CAMERA at night in deep snow. Keep the same house, the same porch, the same snowy garden, the same mood.

THE FRAME IS COMPLETELY EMPTY OF PEOPLE. There is NO person anywhere in this image, NO figure in the doorway, NO silhouette inside the house, NO one on the porch, NO one on the steps, NO one on the path. Nobody. The porch and the steps are deserted and waiting.

THE CAMERA - copy it from the attached image: a doorbell camera mounted high above the front door, looking DOWN at a steep angle onto the porch, the front steps and the path below. Strong wide-angle fisheye so the straight lines bow noticeably outward at the edges and the ground falls away beneath the lens. Fixed, static, unmanned, looking-down viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

THE ONE THING THAT CHANGES FROM THE ATTACHED IMAGE - THE GEOMETRY OF THE STEPS. The flight of front steps runs STRAIGHT DOWN AND STRAIGHT AWAY FROM THE OPEN DOORWAY, directly in line with it, falling away from the camera down the centre of the vertical frame. The open door, the porch threshold, the top step and the whole flight below it are all on one straight axis pointing away from the lens, so that anyone stepping out of that door walks straight forward onto the top step and straight down the flight. The steps do NOT run off to one side, they do NOT turn, there is NO landing that makes you turn a corner, and the door does NOT open onto a walkway parallel to the house.

EVERYTHING ELSE STAYS AS IN THE ATTACHED IMAGE, re-stacked for a vertical frame:
- TOP OF FRAME, directly under the camera: the cream-painted covered porch and the WHITE PANELLED FRONT DOOR standing OPEN, swung back into the house, facing the camera square-on, with WARM ORANGE LIGHT from inside spilling out through the empty doorway and washing forward across the porch floor and down over the top steps. The lit hallway is visible through the opening and it is empty.
- BESIDE THE DOOR on the porch: a small real Christmas tree in a pot strung with warm white fairy lights glowing softly, and on the floor next to it a small lantern casting a soft PINK-MAGENTA glow onto the wall.
- BOTH SIDES: WHITE PICKET PORCH RAILINGS with square capped posts running down either side of the flight of steps like banisters, every picket and top rail capped with a ridge of fresh snow.
- CENTRE AND BOTTOM: the flight of STONE PAVER FRONT STEPS, four or five wide steps, dropping straight away from the doorway down the middle of the frame, each tread carrying packed snow and a glassy sheen of ICE where the warm doorway light catches it. The ice is the point of the shot - make it read clearly as slick and treacherous.
- BEYOND: the front garden under deep untouched snow, a shovelled path cut through it leading straight on from the foot of the steps, low snow-covered shrubs, and beyond that the dark blue-black winter night.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K FULL-COLOUR night doorbell-camera still, tack-sharp edge to edge, crisp fine detail in the snow crystals on the railing and in the ice sheen on the steps. Beautiful clean night lighting: warm orange light from the open doorway as the key, the soft warm white of the little tree and the pink lantern as accents, cool deep blue moonlit snow beyond - bright, rich and properly exposed, no blown-out white where the doorway light hits the snow and no crushed black in the garden, correct white balance, real shadows thrown down the steps. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO black-and-white infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
````

#### Image prompt — `starting_frames/v31_c01_g3.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `fd4ec070-be80-4dd3-9dbc-50574492a4d6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_235826_fd4ec070-be80-4dd3-9dbc-50574492a4d6.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_31_assets/starting_frames/v31_c01_g5.png` · Higgsfield media `d12b3f10-6b4b-45d0-8fab-9905847f4481`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
Reproduce the FIRST attached image as faithfully as possible - its camera, viewpoint, lens, porch, steps, railing, snow and night lighting - as a TALL VERTICAL 9:16 photograph. This is a still frame from a FRONT-DOOR DOORBELL CAMERA at night in snow. WITH ONE CHANGE, described at the end: there is NO PERSON in the picture.

THE FRAME IS COMPLETELY EMPTY OF PEOPLE. Remove the man who stands in the doorway in the first image. There is NO person anywhere in this image, NO figure in or near the doorway, NO silhouette inside the house, NO one on the porch, NO one on the steps, NO one on the path, NO hand on the railing, NO shadow or reflection of a person. Nobody. The porch is deserted and waiting. Everything else in the first image stays exactly where it is - simply erase the man and show the porch floor and doorway that were behind him.

THE CAMERA - copy it exactly from the first image: a doorbell camera mounted high beside and above the front door, looking DOWN at a steep angle onto the porch and out over the front steps and the snowy yard. Strong wide-angle fisheye so the straight lines bow noticeably outward at the edges and the ground falls away beneath the lens. Fixed, static, unmanned, looking-down viewpoint - NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

THE LAYOUT - copy it exactly from the first image, this is the whole point:
- LEFT SIDE OF FRAME: the covered porch of the house, seen from above. The open FRONT DOOR is on the far left with WARM ORANGE LIGHT from the hallway spilling out of it across the porch, a doormat on the concrete porch floor below it, and a pair of shoes set down beside the door.
- ON THE PORCH beside the door: a small real Christmas tree in a black pot, strung with warm white fairy lights and glowing softly, standing against the porch railing, and a small lantern on the floor throwing a faint pink-magenta glow.
- RUNNING DOWN THE MIDDLE AND RIGHT OF THE FRAME: the WHITE PICKET PORCH RAILING with square capped newel posts, every picket and cap wearing a ridge of fresh snow, running along the front edge of the porch AND continuing down the outside of the front steps.
- THE STEPS RUN ALONG THE FRONT OF THE HOUSE, NOT AWAY FROM IT: the flight of wide concrete front steps starts at the near end of the porch and descends across the lower right of the frame, parallel to the house front, dropping toward the bottom-right corner - exactly the arrangement in the first image. Each tread carries packed snow and a glassy sheen of ICE catching the light from the doorway. Make the ice read clearly as slick and treacherous.
- BEYOND THE RAILING, UPPER RIGHT: the front yard under deep snow, a curving shovelled path, a dark hedge or fence line, and the blue-black winter night with a distant warm streetlight.

ONE ADDITION, copied from the SECOND attached image: a short STACK OF PRODUCT BOXES sitting on one of the snowy steps in the lower right of the frame, exactly where the boxes sit in the first image - THREE flat MATTE BLACK rigid retail boxes stacked neatly on the tread, the top one's PRINTED FRONT FACE angled up toward the camera and readable in the doorway light: a large white condensed uppercase headline, a warm gold subline, a small red diagonal ribbon flag in the top-right corner, one large photographic panel with a thin gold hairline border showing a night photo of a house facade lit with Christmas lights, and a bottom row of five small gold line icons. Closed and sealed - NO transparent window, NO clear plastic panel, NO cutout, nothing visible inside. Matte black only - NOT brown cardboard, NOT red, NOT green, NOT white, NOT generic parcels.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K FULL-COLOUR night doorbell-camera still, tack-sharp edge to edge, crisp fine detail in the snow on the railing caps, in the ice sheen on the steps and in the print on the boxes. Beautiful clean night lighting: warm orange light from the open doorway as the key, the soft warm white of the little tree as an accent, cool deep blue moonlit snow beyond - bright, rich and properly exposed, no blown-out white where the doorway light hits the snow and no crushed black in the yard, correct white balance, real shadows across the porch and down the steps. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO black-and-white infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere. Not a render, not an illustration, no cinematic colour grading.
````

#### Image prompt — `starting_frames/v31_c01_g4.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `35ffea43-ad5d-4516-8e4b-714137e34aec`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_000339_35ffea43-ad5d-4516-8e4b-714137e34aec.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_31_assets/starting_frames/v31_c01_g5.png` · Higgsfield media `d12b3f10-6b4b-45d0-8fab-9905847f4481`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
Recreate the FIRST attached photograph as a REAL, NATURAL, PHYSICALLY CORRECT night photograph, in a tall vertical 9:16 frame. Keep its scene, its layout and its lighting. Make ONE change: there is NO PERSON in the picture.

GEOMETRY AND REALISM - THIS IS THE MOST IMPORTANT INSTRUCTION. The architecture must be perfectly solid, square and believable, like a real photo taken by a real camera of a real house. Use a NORMAL wide-angle lens with only very slight barrel distortion. Straight edges stay straight. The porch railing is a straight, rigid, factory-made run of vinyl picket fence: every picket is the same width, the same length and perfectly vertical, evenly spaced, all in one flat straight plane; the newel posts are true square columns standing plumb and vertical with flat caps, all the same size. The steps are a normal concrete flight: each tread is a flat rectangle with a crisp straight front edge, all the treads the same depth and the same height, stacked in an even regular stair. The porch floor is flat and level. The door frame is square.

BANNED, these ruined the last attempt: NO fisheye warping, NO bending or curving of railings, posts, steps or walls, NO melted or sagging or rubbery geometry, NO step edges that dissolve into each other, NO railing that grows out of the ground at the wrong angle, NO giant out-of-scale newel post, NO floating or unsupported parts, NO impossible or contradictory perspective, NO objects merging into one another, NO smeared or blobby surfaces. Everything obeys ordinary perspective and gravity.

THE CAMERA: a doorbell camera mounted beside and above the front door, looking DOWN at a moderate angle onto the porch and out over the front steps and the snowy yard, exactly the viewpoint of the first image. Fixed, static, unmanned. NOT a handheld phone shot, NOT a cinematic camera, NOT eye level.

NO PEOPLE AT ALL. Remove the man who stands in the doorway in the first image. NO person anywhere in this image, NO figure in or near the doorway, NO silhouette inside the house, NO one on the porch, NO one on the steps, NO one on the path, NO hand on the railing, NO shadow or reflection of a person. The porch is deserted. Show the plain porch floor and doorway that were behind him.

THE LAYOUT - copy it from the first image:
- LEFT SIDE OF FRAME: the covered porch of the house seen from above. The FRONT DOOR is open on the far left with WARM ORANGE LIGHT from the hallway spilling out across the porch, a rectangular doormat on the concrete porch floor below it, a pair of shoes set neatly beside the door.
- ON THE PORCH beside the door: one small real Christmas tree in a black pot, strung with warm white fairy lights, standing upright on the porch floor at normal scale - about knee to waist height, clearly a small potted tree and not fused into the railing behind it. A small metal lantern on the floor nearby throwing a faint pink glow.
- ALONG THE FRONT EDGE OF THE PORCH: a straight white vinyl picket railing between two square capped posts, a neat ridge of snow lying along the top rail and on each cap.
- THE STEPS RUN ALONG THE FRONT OF THE HOUSE, NOT AWAY FROM IT: a flight of four or five wide concrete front steps begins at the near end of the porch and descends across the lower right of the frame, parallel to the house front, dropping toward the bottom-right corner - exactly the arrangement in the first image. A matching straight white picket railing runs down the outer side of the flight, stepping down evenly with the treads. Each tread carries packed snow and a glassy sheen of ICE catching the doorway light, with a clean straight visible nosing on every step.
- BEYOND THE RAILING, UPPER RIGHT: the front yard under deep snow, a curving shovelled path, a dark fence line, the blue-black winter night, one distant warm streetlight.

ONE ADDITION, copied from the SECOND attached image: a short stack of THREE flat MATTE BLACK rigid retail boxes sitting squarely on one of the snowy treads in the lower right, stacked neatly and level, the top one's printed front face angled up toward the camera and readable in the doorway light: a large white condensed uppercase headline, a warm gold subline, a small red diagonal ribbon flag in the top-right corner, one large photographic panel with a thin gold hairline border showing a night photo of a house facade lit with Christmas lights, and a bottom row of five small gold line icons. Closed and sealed - NO transparent window, NO clear plastic panel, NO cutout, nothing visible inside. Matte black only - NOT brown cardboard, NOT red, NOT green, NOT white, NOT generic parcels.

IMAGE QUALITY: a genuinely high-resolution modern 2K FULL-COLOUR night doorbell-camera photograph, tack-sharp edge to edge, crisp real detail in the snow on the railing caps, in the ice on the steps and in the print on the boxes, real photographic texture in the concrete and the vinyl. Warm orange light from the open doorway as the key, the warm white tree as an accent, cool deep blue moonlit snow beyond - bright, rich and properly exposed, no blown-out white where the light hits the snow, no crushed black in the yard, correct white balance, real cast shadows across the porch and down the steps. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO black-and-white night-vision look, NO low-resolution CCTV mush. Photorealistic - not a render, not a 3D model, not an illustration, not a painting, no cinematic colour grading.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos anywhere.
````

#### Video prompt — `clips/v31_c01_g1.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `ee39c6c7-1dce-4224-a761-b4f487b969b0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_003455_ee39c6c7-1dce-4224-a761-b4f487b969b0.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c01_g5.png` · Higgsfield media `3f4dd818-c00a-47e8-8edf-20c32b8852db`

````text
THE CAMERA NEVER MOVES. This is the single most important rule. The shot is a fixed doorbell camera mounted beside the front door, looking down over the porch and the snowy front steps. It does not pan, tilt, zoom, dolly, orbit, shake, drift, rack focus or re-frame at any moment. The white picket railing, the square posts, the steps, the snowy yard, the fence line and the distant streetlight stay locked in exactly the same place for all five seconds and never shift by a single pixel. Everything that moves in this clip is the man. Treat the background as a still photograph. The architecture stays rigid and straight the whole time - the railing pickets stay perfectly vertical and evenly spaced, the posts stay plumb, the step treads keep their crisp straight front edges. Nothing bends, warps, melts or breathes.

Continue the attached start frame as one continuous unbroken five-second take. No cuts, no edits, no transitions, no speed ramps, no slow motion. Same porch, same open door, same warm hallway light, same deep snow, same night as the frame.

THE MAN: he does not exist in the first frame - he comes out of the open doorway. A grown man in a dark winter jacket, jeans and boots, wearing a red and white CHRISTMAS SANTA HAT. He carries a tall stack of matte black rigid retail boxes hugged against his chest with BOTH forearms underneath and both hands clamped on the far side, the stack tipped back against his collarbone, the top box level with his chin so it half hides his lower face - exactly the way a delivery courier carries a load he cannot see over. He has to lean back slightly to counterweight it.

THE ACTION, as a timeline:
0.0-0.6s - The porch is empty. Then the man steps out through the open doorway on the left into the warm spill of hallway light, carrying the stack of black boxes in both arms as described.
0.6-1.8s - He crosses the porch from the door toward the top of the steps, walking away from the camera and to the right, his boots on the concrete, his breath steaming in the cold. The stack of boxes blocks his view of his own feet. His shadow swings across the porch floor.
1.8-2.6s - He reaches the top step and starts down without looking, feeling for the tread with his front boot.
2.6-3.5s - HE FALLS. His front boot skids straight out on the ice. Both feet go from under him at once. He drops fast and heavily onto the steps, landing on his back and hip, and slides and bumps down two or three treads. The stack of black boxes bursts out of his arms and the boxes tumble, bounce and slide down the steps and out into the snow. His Santa hat flies off and lands on a lower step. One arm shoots up and grabs at the picket railing and misses.
3.5-5.0s - He comes to rest sprawled across the lower steps in the snow, on his back, one knee up, legs higher than his head. He lies still for a beat, then lifts his head, props himself on one elbow and looks at the scattered boxes around him, breathing hard, his breath clouding. He does not get up.

PHYSICS AND REALISM: a real man with real weight, filmed by a real camera. Gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down. The steps are icy and hard. Clothing creases and flaps. The boxes are light, rigid cardboard and they bounce and slide down the treads and stop in the snow; they do not float, melt, stretch, multiply or vanish. His body stays whole and correctly proportioned throughout - arms and legs bend only at real joints and only the way real joints bend.

BANNED: no camera movement of any kind, no zoom, no push in, no handheld shake, no second person appearing, no one else in the doorway, no Christmas tree or potted plant appearing on the porch, no railing or step bending, warping, melting or moving, no rubbery or elastic limbs, no impossible bends, no morphing faces, no extra arms or hands, no boxes vanishing or duplicating, no slow motion, no cinematic grade, no lens flare, no text, no timestamp, no watermark, no logos, no captions, no UI.

LOOK: a genuinely sharp modern 2K FULL-COLOUR night doorbell-camera recording, warm orange key light from the open doorway, cool deep blue moonlit snow beyond, bright and correctly exposed, natural colour, crisp detail. Not black-and-white night vision, not low-resolution CCTV mush, not a movie, not a render, not an illustration.

AUDIO: natural outdoor night sound only - his boots on the concrete porch, the scrape of the skid, the heavy thud and bump of his body down the icy steps, the cardboard boxes clattering and sliding, one short involuntary shout from him as he goes down, then his breathing. Cold still winter air underneath. No music, no score, no background song, no narration, no sound effects library stings.
````

#### Video prompt — `clips/v31_c01_g2.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `ac42ae8f-7dec-4aee-9182-56415cbbdb57`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_005915_ac42ae8f-7dec-4aee-9182-56415cbbdb57.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c01_g5.png` · Higgsfield media `3f4dd818-c00a-47e8-8edf-20c32b8852db`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
THE CAMERA NEVER MOVES. This is the single most important rule. The shot is a fixed doorbell camera mounted beside the front door, looking down over the porch and the snowy front steps. It does not pan, tilt, zoom, dolly, orbit, shake, drift, rack focus or re-frame at any moment. The white picket railing, the square posts, the steps, the snowy yard, the fence line and the distant streetlight stay locked in exactly the same place for all five seconds and never shift by a single pixel. Everything that moves in this clip is the man and the boxes. Treat the background as a still photograph. The architecture stays rigid and straight the whole time - the railing pickets stay perfectly vertical and evenly spaced, the posts stay plumb, the step treads keep their crisp straight front edges. Nothing bends, warps, melts or breathes.

Continue the attached start frame as one continuous unbroken five-second take. No cuts, no edits, no transitions, no speed ramps, no slow motion. Same porch, same open door, same warm hallway light, same deep snow, same night as the frame.

THE BOXES ARE THE PRODUCT AND THEY MUST MATCH THE ATTACHED PACKSHOT REFERENCE EXACTLY. Every box in this clip is the flat matte black retail box in the second attached reference image: a wide flat rectangular box, MATTE BLACK on every face, with a white condensed uppercase headline across the top of the front panel, a warm gold subline beneath it, a red diagonal BEST SELLER ribbon across the top-right corner, one rectangular photo panel in the middle framed by a thin gold hairline border, and a row of five small gold line icons along the bottom edge. SIZE: each box is 55 cm wide, 42 cm tall and only 10 cm deep - a flat slab, about as wide as the man's chest and only as thick as his hand. Scale check: the man carries a stack of THREE of these boxes lying flat one on top of the other; three stacked together are only about 30 cm tall in total, reaching from his waist to the middle of his chest, and the stack is clearly NARROWER than his shoulders. Do NOT render the boxes person-sized, do NOT render them as tall cubes, do NOT render brown cardboard parcels, do NOT render plain unprinted boxes. The printed front panel must stay readable and face the camera as they fall.
BOX NEGATIVES: NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, every box closed and sealed, no open flaps, no tape, no shipping labels, no barcodes, no brown kraft.

THE MAN: he does not exist in the first frame - he comes out of the open doorway. A grown man in a dark winter jacket, jeans and boots, wearing a red and white CHRISTMAS SANTA HAT. He carries the stack of three flat matte black product boxes hugged against his chest with BOTH forearms underneath and both hands clamped on the far side, the stack tipped back against his collarbone so the printed front panel of the top box faces up and out toward the camera. He has to lean back slightly to counterweight it and he cannot see his own feet past the load.

THE ACTION, as a timeline:
0.0-0.6s - The porch is empty. Then the man steps out through the open doorway on the left into the warm spill of hallway light, carrying the stack of black product boxes in both arms as described.
0.6-1.8s - He crosses the porch from the door toward the top of the steps, walking away from the camera and to the right, his boots on the concrete, his breath steaming in the cold. His shadow swings across the porch floor. The gold and white printing on the top box catches the warm doorway light.
1.8-2.6s - He reaches the top step and starts down without looking, feeling for the tread with his front boot.
2.6-3.5s - HE FALLS. His front boot skids straight out on the ice. Both feet go from under him at once. He drops fast and heavily onto the steps, landing on his back and hip, and slides and bumps down two or three treads. The three black product boxes burst out of his arms and tumble, flip, bounce and slide down the steps and out into the snow, their printed front panels flashing white and gold as they turn. His Santa hat flies off and lands on a lower step. One arm shoots up and grabs at the picket railing and misses.
3.5-5.0s - He comes to rest sprawled across the lower steps in the snow, on his back, one knee up, legs higher than his head. The three boxes lie scattered around him on the steps and in the snow, one of them face-up with its printed front panel clearly visible to the camera. He lies still for a beat, then lifts his head, props himself on one elbow and looks at the scattered boxes, breathing hard, his breath clouding. He does not get up.

PHYSICS AND REALISM: a real man with real weight, filmed by a real camera. Gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down. The steps are icy and hard. Clothing creases and flaps. The boxes are light, rigid, flat cardboard slabs and they bounce, flip and slide down the treads and stop in the snow; they do not float, melt, stretch, bend, multiply or vanish. There are exactly THREE boxes at every moment of the clip. His body stays whole and correctly proportioned throughout - arms and legs bend only at real joints and only the way real joints bend.

BANNED: no camera movement of any kind, no zoom, no push in, no handheld shake, no second person appearing, no one else in the doorway, no Christmas tree or potted plant appearing on the porch, no railing or step bending, warping, melting or moving, no rubbery or elastic limbs, no impossible bends, no morphing faces, no extra arms or hands, no boxes vanishing or duplicating, no person-sized boxes, no brown cardboard parcels, no slow motion, no cinematic grade, no lens flare, no text, no timestamp, no watermark, no logos, no captions, no UI.

LOOK: a genuinely sharp modern 2K FULL-COLOUR night doorbell-camera recording, warm orange key light from the open doorway, cool deep blue moonlit snow beyond, bright and correctly exposed, natural colour, crisp detail. Not black-and-white night vision, not low-resolution CCTV mush, not a movie, not a render, not an illustration.

AUDIO: natural outdoor night sound only - his boots on the concrete porch, the scrape of the skid, the heavy thud and bump of his body down the icy steps, the cardboard boxes clattering and sliding, one short involuntary shout from him as he goes down, then his breathing. Cold still winter air underneath. No music, no score, no background song, no narration, no sound effects library stings.
````

#### Video prompt — `clips/v31_c01_g3.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `4476886c-05f5-4586-b12b-16c6bddf8420`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_103918_4476886c-05f5-4586-b12b-16c6bddf8420.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c01_g5.png` · Higgsfield media `3f4dd818-c00a-47e8-8edf-20c32b8852db`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
THE CAMERA NEVER MOVES. This is the single most important rule. The shot is a fixed doorbell camera mounted beside the front door, looking down over the porch and the snowy front steps. It does not pan, tilt, zoom, dolly, orbit, shake, drift, rack focus or re-frame at any moment. The white picket railing, the square posts, the steps, the snowy yard, the fence line and the distant streetlight stay locked in exactly the same place for all five seconds and never shift by a single pixel. Everything that moves in this clip is the man and the boxes. Treat the background as a still photograph. The architecture stays rigid and straight the whole time - the railing pickets stay perfectly vertical and evenly spaced, the posts stay plumb, the step treads keep their crisp straight front edges. Nothing bends, warps, melts or breathes.

Continue the attached start frame as one continuous unbroken five-second take. No cuts, no edits, no transitions, no speed ramps, no slow motion. Same porch, same open door, same warm hallway light, same deep snow, same night as the frame.

THE BOXES ARE THE PRODUCT AND THEY MUST MATCH THE ATTACHED PACKSHOT REFERENCE EXACTLY. Every box in this clip is the flat matte black retail box in the second attached reference image: a wide flat rectangular box, MATTE BLACK on every face, with a white condensed uppercase headline across the top of the front panel, a warm gold subline beneath it, a red diagonal BEST SELLER ribbon across the top-right corner, one rectangular photo panel in the middle framed by a thin gold hairline border, and a row of five small gold line icons along the bottom edge. SIZE: each box is 55 cm wide, 42 cm tall and only 10 cm deep - a flat slab, about as wide as the man's chest and only as thick as his hand. Scale check: the man carries a stack of THREE of these boxes lying flat one on top of the other; three stacked together are only about 30 cm tall in total, reaching from his waist to the middle of his chest, and the stack is clearly NARROWER than his shoulders. Do NOT render the boxes person-sized, do NOT render them as tall cubes, do NOT render brown cardboard parcels, do NOT render plain unprinted boxes. The printed front panel must stay readable and face the camera as they fall.
BOX NEGATIVES: NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible inside, every box closed and sealed, no open flaps, no tape, no shipping labels, no barcodes, no brown kraft.

THE MAN: he does not exist in the first frame - he comes out of the open doorway. A grown man in a dark winter jacket, jeans and boots, wearing a red and white CHRISTMAS SANTA HAT. He carries the stack of three flat matte black product boxes hugged against his chest with BOTH forearms underneath and both hands clamped on the far side, the stack tipped back against his collarbone so the printed front panel of the top box faces up and out toward the camera. He has to lean back slightly to counterweight it and he cannot see his own feet past the load.

THE ACTION, as a timeline:
0.0-0.6s - The porch is empty. Then the man steps out through the open doorway on the left into the warm spill of hallway light, carrying the stack of black product boxes in both arms as described.
0.6-1.8s - He crosses the porch from the door toward the top of the steps, walking away from the camera and to the right, his boots on the concrete, his breath steaming in the cold. His shadow swings across the porch floor. The gold and white printing on the top box catches the warm doorway light.
1.8-2.6s - He walks straight over the top step and keeps going down the stairs without breaking stride and without looking down. His pace stays exactly the same as it was on the porch. He does NOT stop, does NOT pause, does NOT hesitate, does NOT slow down, does NOT stand still on the first step and does NOT test or feel for the tread - he is moving continuously the whole time.
2.6-3.5s - HE FALLS. His front boot skids straight out on the ice. Both feet go from under him at once. He drops fast and heavily onto the steps, landing on his back and hip, and slides and bumps down two or three treads. The three black product boxes burst out of his arms and tumble, flip, bounce and slide down the steps and out into the snow, their printed front panels flashing white and gold as they turn. His Santa hat flies off and lands on a lower step. One arm shoots up and grabs at the picket railing and misses.
3.5-5.0s - He comes to rest sprawled across the lower steps in the snow, on his back, one knee up, legs higher than his head. The three boxes lie scattered around him on the steps and in the snow, one of them face-up with its printed front panel clearly visible to the camera. He lies still for a beat, then lifts his head, props himself on one elbow and looks at the scattered boxes, breathing hard, his breath clouding. He does not get up.

PHYSICS AND REALISM: a real man with real weight, filmed by a real camera. Gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down. The steps are icy and hard. Clothing creases and flaps. The boxes are light, rigid, flat cardboard slabs and they bounce, flip and slide down the treads and stop in the snow; they do not float, melt, stretch, bend, multiply or vanish. There are exactly THREE boxes at every moment of the clip. His body stays whole and correctly proportioned throughout - arms and legs bend only at real joints and only the way real joints bend.

BANNED: no camera movement of any kind, no zoom, no push in, no handheld shake, no second person appearing, no one else in the doorway, no Christmas tree or potted plant appearing on the porch, no railing or step bending, warping, melting or moving, no rubbery or elastic limbs, no impossible bends, no morphing faces, no extra arms or hands, no boxes vanishing or duplicating, no person-sized boxes, no brown cardboard parcels, no slow motion, no cinematic grade, no lens flare, no text, no timestamp, no watermark, no logos, no captions, no UI.

LOOK: a genuinely sharp modern 2K FULL-COLOUR night doorbell-camera recording, warm orange key light from the open doorway, cool deep blue moonlit snow beyond, bright and correctly exposed, natural colour, crisp detail. Not black-and-white night vision, not low-resolution CCTV mush, not a movie, not a render, not an illustration.

AUDIO: natural outdoor night sound only - his boots on the concrete porch, the scrape of the skid, the heavy thud and bump of his body down the icy steps, the cardboard boxes clattering and sliding, one short involuntary shout from him as he goes down, then his breathing. Cold still winter air underneath. No music, no score, no background song, no narration, no sound effects library stings.
````

### C02 — Box over the sofa

**In the cut:** `starting_frames/v31_c02_g1.png` → `clips/v31_c02_g1.mp4`

#### Image prompt — `starting_frames/v31_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `64297a9f-2cf8-496a-945f-19ae9e5728c8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210916_64297a9f-2cf8-496a-945f-19ae9e5728c8.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_20_assets/starting_frames/v20_c02_g5.png` · Higgsfield media `05989e1b-228c-432a-be58-a51cfbfa19ad`
- @Image 2: `content/video_29_assets/starting_frames/v29_c02_g1.png` · Higgsfield media `07ebb15c-1e14-4ef7-b576-b0f4210e0c5b`

````text
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. The box is a closed rigid printed gift box with NO transparent window and NO cut-out panel anywhere on it. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: a late-twenties woman with deep brown skin and BLACK BOX BRAIDS gathered into a high bun, wearing a MUSTARD-YELLOW oversized knit jumper and LIGHT-WASH wide-leg jeans. The room has a PALE LIMEWASHED PLANK floor, a TAN LEATHER sofa with a cream sheepskin and olive-green cushions, a TERRACOTTA PLASTER wall behind, a BLACK IRON lantern pendant hanging above, and a tall slim REAL GREEN SPRUCE Christmas tree hung with red gingham bows and warm white lights standing at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the knit of her jumper and in the print on the box, clean even indoor light with no blown highlights and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur on the box or on her, NO grain, NO haze, NO soft focus anywhere. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v31_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `aaf53494-481e-4721-b17e-fafc02b020b0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013614_aaf53494-481e-4721-b17e-fafc02b020b0.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v31_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c02_g1.png` · Higgsfield media `64297a9f-2cf8-496a-945f-19ae9e5728c8`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `ffaa8801-8e71-43f0-ae24-461104cf30f2`
- image ref 2: `product_images/box_nowindow/box_interior_g5.png` · Higgsfield media `f01fecfe-9cbe-44a5-a617-63193a1108b0`

````text
TWO SCENES IN ONE CLIP, JOINED BY ONE HARD CUT AT EXACTLY 2.5s. No dissolve, no fade, no whip pan, no transition effect — a straight in-camera cut, exactly like a creator cutting two takes together.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she walks at a walking pace, she kneels at the speed a body really kneels, the lid swings open at the speed heavy cardboard really swings. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in five seconds — one slow lowering, one slow kneel, one slow lid. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still settling as the clip ends than that any part of it looks fast-forwarded.

REFERENCE IMAGES. Reference image 1 is the first frame of scene 1 — start there, unchanged, and it owns the room, the woman, the camera angle and the geometry. Reference image 2 is the CLOSED PRODUCT BOX: the artwork on the box in this video must match it exactly. Reference image 3 is the OPEN BOX INTERIOR: what she reveals in scene 2 must match it exactly.

THE WOMAN — she is exactly the woman in reference image 1 and never changes: a late-twenties woman with deep brown skin and BLACK BOX BRAIDS gathered into a HIGH BUN, wearing a MUSTARD-YELLOW oversized knit jumper and LIGHT-WASH wide-leg jeans. Same hair, same skin, same clothes, first frame to last.

BOX SPEC — TRUE IN EVERY FRAME. A matte black rigid retail box, 55 cm wide x 42 cm tall x 10 cm deep. It is BIG — much wider than the span of two outstretched hands; each of her hands covers less than a quarter of the box width, and laid on the sofa seat it spans most of one cushion. Front panel top to bottom: a large white condensed uppercase headline LED CURTAIN LIGHTS; a warm gold subline Create Your Own Magic; a red diagonal BEST SELLER ribbon flag in the top-right corner; one large photographic panel with a thin gold hairline border showing a night house facade with a glowing pixel LED Christmas tree on the garage door; a bottom row of five small gold line icons with white captions. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible through the front, NO glowing lights showing through the cardboard. The box is closed and sealed until the moment she opens it in scene 2.

SCENE 1 — 0.0 to 2.5s. CAMERA: HELD IPHONE, LOCKED FOCAL LENGTH, portrait, a friend filming from just behind her left shoulder at HER SHOULDER HEIGHT, tilted down only very slightly — exactly where reference image 1 was taken. NOT above her head, NOT a top-down shot. NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO DOLLY. Handheld micro-shake only. She is at the LEFT EDGE of frame, partly cut off by it; the TAN LEATHER sofa is directly IN FRONT of her, running diagonally away into depth and filling the right and bottom-right of frame, its empty seat cushions facing up. The room behind her — the PALE LIMEWASHED PLANK floor, the TERRACOTTA PLASTER wall, the BLACK IRON lantern pendant hanging above, the cream sheepskin and olive-green cushions, and the tall slim REAL GREEN SPRUCE Christmas tree hung with red gingham bows and warm white lights at the right — stays exactly as it is and never changes.
THE WHOLE POINT OF SCENE 1: she carries the box round in front of the sofa, sets it flat on the seat cushion AND drops to her knees IN THE SAME CONTINUOUS MOTION. These are not two separate steps — the box going down and her body going down are one move.
0.0-0.9s — one unhurried step forward and to her right, her shoulders turning, the heavy box swinging slowly out in front of her; the braids in her high bun swing across and settle, her mustard-yellow jumper sleeve creases with the weight.
0.9-1.8s — she steps in front of the sofa and leans forward from the hips, lowering the box steadily toward the empty tan leather seat cushion, arms extending, knees already bending underneath her. This lowering is SLOW and heavy — the box is big and awkward and she is being careful with it.
1.8-2.5s — the box settles flat and printed-side-up on the cushion with a soft creak of the tan leather, her hands still on it, and in the same continuous motion her knees come down onto the pale limewashed plank floor one after the other, her weight settling and her back rounding forward; she pushes a loose braid back off her shoulder and plants both palms flat on the box lid, chest rising with one excited breath.

HARD CUT AT 2.5s.

SCENE 2 — 2.5 to 5.0s. Direct continuation, same room, same second, same woman, same mustard-yellow jumper, same box in exactly the same place on the same tan leather cushion. The camera has moved about 30 degrees round to her side — a slightly more side-on three-quarter angle, a little lower, closer to the level of the sofa seat, so we now see the lid edge in profile and read the pivot clearly. Still HELD IPHONE, LOCKED FOCAL LENGTH, handheld micro-shake only, NO ZOOM.
LID MECHANISM, GEOMETRICALLY. The box is a magnetic-closure flip-top. The hinge runs along the TOP LONG EDGE of the box — the far edge away from her, at the back. The lid pivots UP and BACK on that hinge, rotating away from her and toward the back of the sofa, keeping its printed front face turned toward the camera as it rises. The inside of the lid is matte black. The lid is NEVER lifted off, NEVER removed, NEVER carried aside, NEVER set down, NEVER folded flat instantly, NEVER slid out like a drawer.
2.5-3.1s — she hooks her fingertips under the near front edge of the lid; a small snap as the magnets release and the front edge lifts a centimetre, a thin black shadow line opening slowly across the whole 55 cm width.
3.1-4.3s — she pivots the big printed lid UP and BACK on its hinge in ONE slow continuous arc with real cardboard weight, her elbows rising and her shoulders lifting with the effort, until it stands roughly vertical. This arc takes well over a full second of screen time — it travels heavily and never flips or snaps open.
4.3-5.0s — the interior is revealed exactly as reference image 3: the neatly folded BLACK LED mesh curtain lying in its tray, the coiled black lead and the small accessory items beside it, all against a matte black interior. She reaches in with both hands and touches the folded black mesh, fingers spreading it slightly, then lifts her chin, looks off toward the spruce tree and breaks into a big open-mouthed grin, eyebrows up.

MOVEMENT RULE FOR BOTH SCENES: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole clip — weight shifting, chest breathing, braids and sleeves swinging and settling, the cushion compressing under the box — and her face keeps changing, eyes, eyebrows and mouth reading differently moment to moment. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses.

HARD RULES: exactly ONE cut, at 2.5s. The box never changes size, never changes artwork, never gains a window or a cutout. The curtain inside the box is BLACK cord with small dark bulbs — never white wire, never clear wire, never silver wire. Nobody else enters frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Quiet warm living-room ambience, the soft thump of a heavy box on a leather cushion, knees on the floor, the click of magnets releasing, stiff cardboard flexing, plastic mesh rustling, one small delighted exhale.

LOOK: real iPhone UGC indoors at night. Warm mixed lamp and fairy light, slight sensor noise in the shadows, natural skin, no cinematic grade, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
````

### C03 — Mounting on the attached garage, day

**In the cut:** `starting_frames/v31_c03_g1.png` → `clips/v31_c03_g1.mp4`

#### Image prompt — `starting_frames/v31_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `5c64a1b2-4023-4b70-b3ad-949aebad8bcf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_211053_5c64a1b2-4023-4b70-b3ad-949aebad8bcf.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c03_g2.png` · Higgsfield media `46b340e4-6caf-44c9-aa30-cc219dfe59a6`
- @Image 2: `content/video_31_assets/starting_frames/v31_c02_g1.png` · Higgsfield media `64297a9f-2cf8-496a-945f-19ae9e5728c8`

````text
COPY THE CAMERA OF THE FIRST ATTACHED IMAGE EXACTLY - its position, its angle, its height, its closeness and her pose. This is a CLOSE, SIDE-ON shot, not a wide frontal shot.

THE CAMERA IS CLOSE AND OFF TO ONE SIDE, exactly as in the first image: the camera stands near the wall and slightly behind her at roughly waist height, looking ALONG the wall, so the wall runs away from the camera DIAGONALLY - nearest at the bottom-left of the frame and receding to the right, the roof gutter line along the top sloping down towards the right as it goes away, strong oblique one-point perspective. She fills most of the frame height in the right half, her whole body in shot from her boots on the stool up to her raised hands. MUCH CLOSER than a full-house shot: only a short run of the wall is in frame, no full facade, no wide establishing view, no flat square-on frontal view.

HER POSE - copy it from the first image: she stands on a small BLACK two-step folding step stool, seen from BEHIND and slightly to the side, facing the wall, both arms raised in front of her, her hands up at the trim board along the top of the wall as she presses the LED curtain into place. Her weight is on one foot, her back slightly arched.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Long vertical strands of thin BLACK cord with small DARK unlit bulbs hang down the wall to the left of her, and because the camera is close the strands are big in the frame and clearly readable as separate cords. A BIG LOOSE TANGLE of BLACK cord is heaped on the snow at the foot of the stool, spilling out to the left - a real messy nest of wire, obviously dark against the white snow, exactly like the bundle in the first image. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - TAKE HER FROM THE SECOND ATTACHED IMAGE. Same late-twenties woman with deep brown skin and BLACK BOX BRAIDS, now gathered into a low bun spilling out from under a RUST-ORANGE beanie, wearing a CREAM TEDDY-FLEECE coat, DARK GREEN cargo trousers and CHOCOLATE-BROWN boots. It must read as literally the same person as in the second image.

A COMPLETELY NEW HOUSE - take it from this text only, NOT from either attached image. The wall she is working on is the WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR of a two-storey family home - soft WHITE with horizontal panel seams and recessed rectangular panels running away in perspective, and the row of small square windows across the top of the door visible at the far end. Around it, DARK CHARCOAL-GREY board-and-batten siding with crisp WHITE trim, a BLACK COACH LANTERN on the wall, a WHITE gutter and WHITE downpipe, a pale grey roof, and a plain CONCRETE driveway under patchy snow. At the RIGHT of the frame, further away, the corner where the garage wing meets the MAIN HOUSE BODY is visible - the two-storey wall, the covered porch on white posts and the MUSTARD-YELLOW front door - so it reads as ONE house with the garage built into it.

DO NOT COPY THE HOUSE FROM THE FIRST IMAGE: not its warm sand-beige or cream lap siding, not its dark red front door. The first image is there ONLY for the camera, the distance, the angle, the pose and the black wire.

Daytime, overcast winter light, snow on the ground.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the door panels, the texture of her teddy-fleece coat and every strand of black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v31_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `67fd3e3e-00c8-44fe-af14-52a68107e6d5`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013614_67fd3e3e-00c8-44fe-af14-52a68107e6d5.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v31_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c03_g1.png` · Higgsfield media `5c64a1b2-4023-4b70-b3ad-949aebad8bcf`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same overcast winter day, same CLOSE SIDE-ON camera at waist height looking ALONG the wall so it recedes diagonally from the bottom-left of frame away to the right, same WIDE SOFT WHITE SECTIONAL DOUBLE GARAGE DOOR with its horizontal panel seams and recessed panels running away in perspective and its row of small square windows across the top at the far end, same DARK CHARCOAL-GREY board-and-batten siding with its vertical batten strips and crisp white trim around the door, same black coach lantern, same white gutter and white downpipe, same pale grey roof, same concrete driveway under patchy snow, same corner of the main house body with its covered porch on white posts and its mustard-yellow front door further away at the right, same black two-step folding step stool, same woman seen from behind in the CREAM TEDDY-FLEECE coat, DARK GREEN cargo trousers, CHOCOLATE-BROWN boots and the RUST-ORANGE beanie with her black box braids gathered in a low bun spilling out from under it, standing on the stool with both arms raised pinning the gathered fistful of unlit net up under the trim board above the door, same LED net already hung flat across the door to her left, same loose tangled coil of curtain heaped on the snow at the foot of the stool.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she reaches at the speed an arm really reaches, she shakes the net out at the speed a heavy tangled net really swings, she shifts her weight at the speed a body really balances on a step stool. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in four seconds — one slow shake, one slow reach, one slow sideways press. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still mid-reach as the clip ends than that any part of it looks fast-forwarded.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH. Portrait, exactly the framing and the angle of the reference image — close, side-on, at waist height, looking along the garage door so it recedes diagonally into the frame. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT. The garage door, the white trim, the coach lantern and the stool stay exactly the same size in frame from the first frame to the last, the perspective never flattens, and the camera never swings round to a flat square-on frontal view of the door and never pulls back to a wide establishing shot of the whole house.

MOVEMENT RULE: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole four seconds — weight shifting on the stool, shoulders rolling, ribs breathing, the braids and the bun swinging and settling, the teddy-fleece coat creasing and rustling, the strands swaying on after every touch. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses, and no limb ever travels faster than a real arm travels.

ACTION TIMELINE (4 seconds, one continuous take, no cuts) — ONLY TWO THINGS HAPPEN, AND BOTH ARE SLOW:
0.0-2.0s — she lifts the gathered bundle in her right hand and shakes it out ONCE, slowly and heavily. The shake takes well over a full second of screen time: her arm swings out and down, the tangled net lets go in stages rather than all at once, and a long sheet of black strands falls open down the white door panels and swings for a moment before it settles. The loose coil on the snow drags and shifts with it.
2.0-4.0s — still up on the stool, she stretches both arms high and presses the header wire UP UNDER THE LIP OF THE WHITE TRIM BOARD ABOVE THE DOOR, her thumbs working slowly along it, then walks her hands a short way sideways along that trim board, away from the camera into the depth of the frame, onto the bare stretch of door beyond the strands she has already hung, pressing and tucking as she goes, her torso twisting and her heels lifting and dropping on the tread. She is STILL tucking when the clip ends. The curtain sways gently against the door panels and is still settling on the last frame.
THAT IS THE WHOLE CLIP. She does NOT step down off the stool, does NOT step back, does NOT plant her hands on her hips and does NOT tilt her head back to look at her work. There is no time for any of that at real speed, and cramming it in is exactly what would force the footage to look sped up. She stays on the stool from the first frame to the last.

THE LED CURTAIN IS BLACK — CRITICAL. The wire is BLACK, not white and not clear. Every vertical strand hanging down the door is a thin BLACK cord and the unlit bulbs on it are small and DARK. Against the soft white door panels the strands read as thin dark lines, clearly and obviously dark. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire appears at any moment.

HARD RULES: the curtain is COMPLETELY OFF the entire time — not one bulb lights, no glow, no colour, no animation on the door. The garage door never gains new panels or features, the row of small square windows across the top never moves, the white trim, the coach lantern, the gutter and the downpipe never move, the dark charcoal-grey board-and-batten siding never changes colour, and the covered porch and mustard-yellow front door further away at the right never change. The strands are separate vertical strands obeying gravity, sagging slightly, with an uneven wavy bottom hem — never a flat sheet, never a panel, never a screen, never a mesh stretched tight. The loose coil rests in the snow with real contact shadows. Her face is never shown; she stays turned away from camera throughout. No other people enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor winter ambience, thin plastic strands rattling and clicking against the metal door panels, a step-stool creak, boots on a metal tread, boots compressing snow, one quiet effortful breath. No voice.

LOOK: real iPhone UGC. Flat overcast winter daylight, slightly cool white balance, mild sensor noise, natural skin, no cinematic grade, no lens flare, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
````

### C04 — Phone POV, the same house at night

**In the cut:** `starting_frames/v31_c04_g2.png`, `references/v31_c04_r1.png` → `clips/v31_c04_g2.mp4`

#### Image prompt — `starting_frames/v31_c04_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `5b6ccb8c-453d-4df2-9cc5-f2973f5605ab`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_233056_5b6ccb8c-453d-4df2-9cc5-f2973f5605ab.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_31_assets/starting_frames/v31_c04_g1.png` · Higgsfield media `ad72a429-34b2-4810-b545-7cc215182d87`

````text
COPY THE ATTACHED IMAGE EXACTLY. Same house, same soft white sectional double garage door, same dark charcoal-grey board-and-batten siding, same white trim, same black coach lanterns glowing warm either side, same snowy concrete driveway, same night light, same camera, same framing, same distance, same square-on angle, same foreground hand holding the same iPhone in the bottom-centre with the SAME two-column app grid and the same round blue play button. Everything is already correct and must be reproduced unchanged.

ONE SINGLE THING CHANGES: THE LED CURTAIN HAS ROUGHLY TWICE AS MANY STRANDS. In the attached image the vertical strands hanging over the garage door are spaced widely apart. Here they are packed about TWICE AS CLOSE TOGETHER - roughly double the number of strands across the same width, so the curtain reads as a much DENSER set of vertical lines running down the whole face of the door.

THE STRANDS THEMSELVES ARE UNCHANGED: each one is still a thin BLACK cord carrying small DARK unlit bulbs, the lights are OFF with no glow, and against the pale door each cord reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. They still hang from the trim board above the door, still span the full width of the door edge to edge, still have a slight natural sag and a slightly uneven bottom hem.

STILL A CURTAIN, NEVER A PANEL - CRITICAL: even at double the density these are SEPARATE HANGING VERTICAL STRANDS with clear DARK GAPS between them, and the garage door behind is plainly visible through those gaps - the recessed panel seams and the row of small square windows across the top must still read clearly through the curtain. Do NOT close the gaps. Do NOT turn it into a solid LED panel, a flat screen, a mesh, a net, a grille or a fabric sheet. Do NOT add horizontal wires. The strands run straight up and down only.

THE FRAMING IS ALREADY CORRECT - DO NOT CHANGE IT. The garage door stays big and dominant, spanning almost the full width of the picture, with the ENTIRE door visible: both vertical side edges inside the frame, the complete top edge including the WHOLE row of small square windows end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT tilt. Still square-on from the front: the panel seams run dead level and the door edges run straight up and down.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every individual black cord clearly readable and clearly separated from its neighbours, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `references/v31_c04_r1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `d610c7e3-058c-4061-915f-bec202ac9161`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_233258_d610c7e3-058c-4061-915f-bec202ac9161.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_31_assets/starting_frames/v31_c04_g2.png` · Higgsfield media `5b6ccb8c-453d-4df2-9cc5-f2973f5605ab`
- @Image 2: `content/video_31_assets/starting_frames/v31_c07_g1.png` · Higgsfield media `51cc4d69-b280-4be2-86cc-86d96d35e32c`

````text
TAKE THE FIRST ATTACHED IMAGE AS THE SCENE. Same house, same soft white sectional double garage door with its recessed panels and its row of small square windows across the top, same dark charcoal-grey board-and-batten siding, same white trim, same black coach lanterns glowing warm either side of the door, same snowy concrete driveway, same night. Same camera, same lens, same distance, same square-on frontal angle. TAKE THE SECOND ATTACHED IMAGE ONLY FOR THE DRAWING STYLE OF THE LIGHTS - the way the cartoon is built out of small round coloured bulbs. DO NOT COPY THE SECOND IMAGE'S HOUSE, ITS GABLE, ITS VAN, ITS ROAD OR ITS SCENE. Only its bulb-art look.

THREE THINGS CHANGE FROM THE FIRST IMAGE:

1. THE HAND AND THE PHONE ARE GONE. There is nothing at all in the foreground. No hand, no arm, no sleeve, no phone, no screen, no glow from a screen. The bottom-centre of the frame is simply the empty snowy driveway. The whole garage door is completely unobstructed from edge to edge.

2. THE CAMERA HAS TILTED UP A LITTLE. This is a handheld iPhone shot and the person filming has tipped the phone up slightly so the lights fill the frame. The framing is otherwise identical - same distance, same square-on frontal angle, the door still faces the camera flat with its horizontal panel seams dead level and its vertical edges straight up and down - but the whole frame has shifted UP: there is now only a THIN sliver of driveway along the bottom edge, and a slightly DEEPER band of siding and trim above the top of the door. The ENTIRE garage door stays inside the frame: both side edges, the complete top edge with the WHOLE row of small square windows visible end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT turn it into a low angle looking up at the roofline, do NOT show the whole house.

3. THE LED CURTAIN IS SWITCHED ON AND SHOWING A BRIGHT CARTOON ANIMATION. The same dense curtain of closely spaced vertical strands hanging over the garage door, but now every bulb is lit and together they draw a picture.

THE PICTURE - A SNOWBALL FIGHT, drawn chunky and simple out of the bulbs, running RIGHT ACROSS THE WHOLE GARAGE DOOR: on the LEFT a big fat three-ball SNOWMAN with a carrot nose, coal eyes and a black top hat, leaning hard into a throw with one bare twig arm cocked right back over his head holding a huge snowball and the other twig arm flung forward for balance. On the RIGHT, THREE GREEN ELVES crouched behind a low lumpy snow wall: one popping up mid-throw with his own snowball, one ducking with both hands over his pointed hat, and one who has just been hit FULL IN THE FACE - a white splat starburst across his head, his hat blown straight off and spinning away, arms flung up, legs off the ground. FOUR OR FIVE SNOWBALLS fly across the middle of the door between them, each trailing a curved dotted trajectory arc and short speed lines. Loose snow puffs burst off the top of the snow wall. Small gold stars scattered through the gaps. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

THE PICTURE FILLS THE ENTIRE GARAGE DOOR: the snowman reaches the left edge of the door, the elves and their snow wall reach the right edge, and the figures plus the flying snowballs plus the stars fill the FULL HEIGHT of the door from just under the row of square windows down to the bottom edge. Every part of the door is covered by lit artwork - no large dark empty areas anywhere on the door, and nothing is confined to a small panel in the middle. Nothing lit appears above the door, on the trim, on the siding, on the lanterns or in the sky.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. The strands are densely spaced but there are still clear DARK GAPS between them and the white garage door behind is plainly visible through those gaps, especially in the unlit areas - the recessed panel seams and the row of square windows must still read through the curtain. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the garage door panels and the snowy driveway clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v31_c04_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `1f474bdc-75a5-49c1-80bf-35d969b94b8a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_105142_1f474bdc-75a5-49c1-80bf-35d969b94b8a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v31_c04_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c04_g2.png` · Higgsfield media `5b6ccb8c-453d-4df2-9cc5-f2973f5605ab`
- image ref 1: `content/video_31_assets/references/v31_c04_r1.png` · Higgsfield media `d610c7e3-058c-4061-915f-bec202ac9161`

````text
THE FIRST FRAME OF THIS VIDEO IS THE START IMAGE, PIXEL FOR PIXEL, UNCHANGED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT.

WHAT IS IN THE START IMAGE, AND WHAT MUST THEREFORE BE IN FRAME 1: night, a suburban driveway shot on a held iPhone in portrait; a soft white sectional double garage door with recessed panels and a row of small square windows across the top; DARK CHARCOAL-GREY board-and-batten siding with vertical battens and crisp white trim; two black coach lanterns glowing warm either side of the door; a snowy concrete driveway; the unlit BLACK LED curtain hanging flat across the garage door with its thin black cords and small dark bulbs; and AT THE BOTTOM-CENTRE OF FRAME, A HAND HOLDING AN IPHONE, screen toward camera, showing a simple two-column app grid and a large round blue PLAY BUTTON. Do NOT start on an empty driveway. Do NOT start on a bare garage door. Do NOT have the hand enter frame later. The hand and the phone are ALREADY THERE in frame 1, exactly as in the start image.

THE SECOND ATTACHED IMAGE IS NOT A FRAME OF THIS VIDEO. It is only a style guide showing what the lit artwork must look like once the lights come on. Never cut to it, never start on it, never copy its framing, never copy its camera height, never copy its distance. Take from it ONLY the drawing that appears in the bulbs.

THE ARTWORK THAT APPEARS IN THE LIGHTS — a SNOWBALL FIGHT. On the LEFT a big fat three-ball SNOWMAN with a carrot nose, coal eyes and a black top hat, leaning hard into a throw with one bare twig arm cocked right back over his head holding a huge snowball and the other twig arm flung forward for balance. On the RIGHT, THREE GREEN ELVES crouched behind a low lumpy snow wall: one popping up mid-throw with his own snowball, one ducking with both hands over his pointed hat, and one who has just been hit FULL IN THE FACE — a white splat starburst across his head, his hat blown straight off and spinning away, arms flung up, legs off the ground. FOUR OR FIVE SNOWBALLS fly across the middle of the door between them, each trailing a curved dotted trajectory arc and short speed lines. Loose snow puffs burst off the top of the snow wall. Do NOT invent a different picture.

HOW THE LIGHTS MUST STAY BUILT. The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the lintel, each wire carrying small round bulbs. The whole picture is built out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix. The curtain is SEE-THROUGH: through the gaps between strands you clearly read the white garage door behind it, its horizontal panel seams and its row of small square windows, and the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark door, with unlit bulbs as tiny dull grey dots and the thin BLACK wires as faint vertical lines. Every lit bulb is a tiny point source: blown-out white core, coloured halo, small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing. The strands sag slightly, each ends at a slightly different height so the bottom hem is uneven and wavy, and the glow bounces back off the door as a soft halo and spills onto the snowy driveway in a speckled uneven pattern.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH, portrait, exactly the framing of the start image. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO CUT. The garage door stays the same size in frame throughout. The ONLY permitted camera move is a small gentle TILT UP in the second half of the clip, a few degrees, as if the person filming lifts their phone slightly to take in the whole door.

REAL TIME — NORMAL 1x SPEED. No fast motion, no sped-up playback, no time-lapse, no speed ramp.

THE PHONE SCREEN MUST VISIBLY SCROLL BEFORE THE PLAY BUTTON IS PRESSED. THIS IS A REQUIRED, UNMISTAKABLE ACTION, NOT A SUGGESTION. The two-column app grid on the phone screen physically TRAVELS UP THE GLASS under the moving thumb: whole rows of app icons slide upward, disappear off the top edge of the screen, and fresh rows rise into view from the bottom edge. The icons must clearly change position on the screen — a thumb moving over a frozen, unmoving grid is a FAILURE. The scroll happens twice, and only after it settles does the thumb press play.

THE ANIMATION IN THE LIGHTS MUST BE WILDLY ALIVE. A STATIC OR BARELY-MOVING PICTURE IS A TOTAL FAILURE.

TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.35s — exactly the start image, the curtain dark and unlit. The thumb is already pressed against the glass and SWIPES UP: the whole two-column app grid scrolls upward with it, the top row sliding up and off the top edge of the screen while a new row of icons rises in from the bottom edge.
0.35-0.7s — the thumb lifts, comes back down and SWIPES UP A SECOND TIME, faster. Several rows of icons scroll past in quick succession, then decelerate and settle, leaving the big round blue PLAY BUTTON sitting in the middle of the screen.
0.7-0.9s — the thumb slides onto the blue PLAY BUTTON and presses it. The button dips and highlights under the press.
0.9-1.1s — IN THE SAME FRAME, without any cut, the whole LED curtain snaps ON at once, the snowball fight appearing all together in chunky bulbs, and warm coloured light floods across the snowy driveway.
1.1-1.5s — the hand lowers steadily out of the bottom of frame. By 1.5s the hand and the phone are COMPLETELY GONE and never return.
1.5-4.0s — the camera drifts gently upward a few degrees and the snowball fight runs at absolute full tilt, redrawing completely EVERY QUARTER SECOND:
1.6s — the snowman whips his cocked twig arm forward and hurls his huge snowball; his black top hat jumps clean off his head.
1.85s — the hurled snowball travels along its dotted arc, the snowman's other twig arm swings round for balance and his top hat drops back on crooked.
2.1s — the elf popping up over the wall launches his own snowball two-handed, both feet leaving the ground.
2.35s — two snowballs burst in mid-air into white star-shaped splats and loose snow puffs off the top of the wall.
2.6s — the hit elf flails all four limbs at once, the white splat across his face bursts bigger and his spinning hat tumbles another full turn.
2.85s — the ducking elf peeks up over the wall, then slams both hands back over his pointed hat and drops out of sight.
3.1s — the snowman scoops a fresh snowball off the ground with both twig arms and cocks right back over his head again.
3.35s — three new snowballs launch at once from both sides and every dotted trajectory arc redraws at a new angle.
3.6s — a snowball smacks into the snow wall and knocks two lumps clean off it; the ducking elf is knocked sideways.
3.85s — everything at once: the snowman mid-hurl, the hit elf upside down in the air, the throwing elf at full stretch, four snowballs crossing the door and two hats spinning.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment from 1.1s onward, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — the snowman's arms, his hat, each of the three elves separately, every snowball, the trajectory arcs, the snow wall. The picture is never still for even one twentieth of a second.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER LEAVES THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the door. No twig arm, no snowball, no trajectory arc, no flying hat and no elf's boot ever crosses outside the curtain rectangle. At every instant every figure keeps a clear margin of at least two full unlit strands of dark door inside every edge of the curtain. If a pose would take a limb or a snowball out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Nothing lit ever appears on the white trim, the charcoal siding, the roof, the sky or the driveway except as reflected spill.

EVERYTHING ELSE IS UNCHANGED: the house, the door, the coach lanterns, the charcoal board-and-batten siding, the snow and the camera position are identical from first frame to last. No people, no cars, no pets enter frame.

NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural sound only — no music, no score, no background song. Cold quiet suburban night ambience, a soft phone tap, a faint electrical hum and tick from the lights, a distant car, light wind. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C04 on disk (2)**

#### Image prompt — `starting_frames/v31_c04_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `ad72a429-34b2-4810-b545-7cc215182d87`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_211224_ad72a429-34b2-4810-b545-7cc215182d87.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g6.png` · Higgsfield media `a6bcff66-91f5-4629-be28-3ba99b78c3a7`
- @Image 2: `content/video_31_assets/starting_frames/v31_c03_g1.png` · Higgsfield media `5c64a1b2-4023-4b70-b3ad-949aebad8bcf`

````text
COPY THE FIRST ATTACHED IMAGE'S CAMERA, FRAMING, DISTANCE, ANGLE AND FOREGROUND PHONE EXACTLY. Night, square-on frontal view of a double garage door, a phone held up big in the bottom-centre foreground. ONE THING CHANGES: it is a DIFFERENT HOUSE, taken from the second attached image.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. The camera is close to the house so the GARAGE DOOR IS BIG AND DOMINATES THE FRAME, spanning almost the full width of the picture with only a NARROW STRIP of white trim and siding visible beyond its left edge and beyond its right edge, only a SHALLOW BAND of siding above its top edge, and only a LOW STRIP of snowy concrete driveway beneath it. But the ENTIRE DOOR STAYS VISIBLE: both vertical side edges inside the frame, the complete top edge inside the frame including the WHOLE row of small square windows running all the way across it with every window visible end to end, and the bottom edge where the door meets the driveway inside the frame. Nothing about the door is cut off by any edge. Do NOT step closer and do NOT step back.

STILL SQUARE-ON FROM THE FRONT: the door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up, NO whole house, NO full facade, NO roofline.

THE HOUSE - TAKE IT FROM THE SECOND ATTACHED IMAGE, NOT FROM THE FIRST. It must read as LITERALLY THE SAME HOUSE as the second image, now seen square-on from the front at night: the same soft WHITE sectional double garage door with its recessed panels and its row of small square windows, and around it DARK CHARCOAL-GREY BOARD-AND-BATTEN siding with crisp WHITE trim and its vertical batten strips clearly visible, BLACK COACH LANTERNS glowing warm on the wall either side of the door, a WHITE gutter, and at the right edge a sliver of the covered porch on its white post with the MUSTARD-YELLOW front door cropped by the frame. The siding must read clearly as a DARK CHARCOAL GREY with vertical battens - NOT cream, NOT white, NOT beige - and it must contrast strongly against the white door and the white trim.

DO NOT COPY THE SIDING COLOUR, THE SIDING TYPE OR THE FRONT DOOR COLOUR FROM THE FIRST IMAGE. The first image is there ONLY for the camera, the framing, the night lighting and the phone.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the door in evenly spaced vertical see-through strands right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale door each strand reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen.

THE PHONE AND ITS SCREEN ARE UNCHANGED - COPY THEM EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same hand, same grip, same angle, same size and same position in the bottom-centre foreground. The screen shows the SAME APP: a dark navy-blue screen with a grid of just TWO COLUMNS of large tiles, two across and about five down, roughly ten tiles in total and no more, each tile nearly half the screen wide with softly rounded corners and a narrow gutter, each one a small photograph of a house decorated in Christmas lights - a lit roofline, a nativity, a snowman, a reindeer, a porch draped in light curtains - mostly icy blue and cool white with a couple of warm tiles, ONE tile ringed with a bright electric-blue outline, and a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE below the grid. NOT a dense grid of tiny icons, NOT three or more columns, NO glyphs or pictograms, and NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

The phone is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v31_c04_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `c377c5a9-1048-4ebf-895e-621dc86aa5de`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013614_c377c5a9-1048-4ebf-895e-621dc86aa5de.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c04_g2.png` · Higgsfield media `5b6ccb8c-453d-4df2-9cc5-f2973f5605ab`
- image ref 1: `content/video_31_assets/references/v31_c04_r1.png` · Higgsfield media `d610c7e3-058c-4061-915f-bec202ac9161`

````text
THE FIRST FRAME OF THIS VIDEO IS THE START IMAGE, PIXEL FOR PIXEL, UNCHANGED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT.

WHAT IS IN THE START IMAGE, AND WHAT MUST THEREFORE BE IN FRAME 1: night, a suburban driveway shot on a held iPhone in portrait; a soft white sectional double garage door with recessed panels and a row of small square windows across the top; DARK CHARCOAL-GREY board-and-batten siding with vertical battens and crisp white trim; two black coach lanterns glowing warm either side of the door; a snowy concrete driveway; the unlit BLACK LED curtain hanging flat across the garage door with its thin black cords and small dark bulbs; and AT THE BOTTOM-CENTRE OF FRAME, A HAND HOLDING AN IPHONE, screen toward camera, showing a simple two-column app grid and a large round blue PLAY BUTTON. Do NOT start on an empty driveway. Do NOT start on a bare garage door. Do NOT have the hand enter frame later. The hand and the phone are ALREADY THERE in frame 1, exactly as in the start image.

THE SECOND ATTACHED IMAGE IS NOT A FRAME OF THIS VIDEO. It is only a style guide showing what the lit artwork must look like once the lights come on. Never cut to it, never start on it, never copy its framing, never copy its camera height, never copy its distance. Take from it ONLY the drawing that appears in the bulbs.

THE ARTWORK THAT APPEARS IN THE LIGHTS — a SNOWBALL FIGHT. On the LEFT a big fat three-ball SNOWMAN with a carrot nose, coal eyes and a black top hat, leaning hard into a throw with one bare twig arm cocked right back over his head holding a huge snowball and the other twig arm flung forward for balance. On the RIGHT, THREE GREEN ELVES crouched behind a low lumpy snow wall: one popping up mid-throw with his own snowball, one ducking with both hands over his pointed hat, and one who has just been hit FULL IN THE FACE — a white splat starburst across his head, his hat blown straight off and spinning away, arms flung up, legs off the ground. FOUR OR FIVE SNOWBALLS fly across the middle of the door between them, each trailing a curved dotted trajectory arc and short speed lines. Loose snow puffs burst off the top of the snow wall. Do NOT invent a different picture.

HOW THE LIGHTS MUST STAY BUILT. The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the lintel, each wire carrying small round bulbs. The whole picture is built out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix. The curtain is SEE-THROUGH: through the gaps between strands you clearly read the white garage door behind it, its horizontal panel seams and its row of small square windows, and the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark door, with unlit bulbs as tiny dull grey dots and the thin BLACK wires as faint vertical lines. Every lit bulb is a tiny point source: blown-out white core, coloured halo, small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing. The strands sag slightly, each ends at a slightly different height so the bottom hem is uneven and wavy, and the glow bounces back off the door as a soft halo and spills onto the snowy driveway in a speckled uneven pattern.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH, portrait, exactly the framing of the start image. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO CUT. The garage door stays the same size in frame throughout. The ONLY permitted camera move is a small gentle TILT UP in the second half of the clip, a few degrees, as if the person filming lifts their phone slightly to take in the whole door.

REAL TIME — NORMAL 1x SPEED. No fast motion, no sped-up playback, no time-lapse, no speed ramp.

THE ANIMATION IN THE LIGHTS MUST BE WILDLY ALIVE. A STATIC OR BARELY-MOVING PICTURE IS A TOTAL FAILURE.

TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.5s — exactly the start image. The curtain is dark and unlit. The thumb is already moving, scrolling on the phone screen.
0.5-0.8s — the thumb presses the big round blue PLAY BUTTON on the phone screen.
0.8-1.0s — IN THE SAME FRAME, without any cut, the whole LED curtain snaps ON at once, the snowball fight appearing all together in chunky bulbs, and warm coloured light floods across the snowy driveway.
1.0-1.6s — the hand lowers slowly out of the bottom of frame. By 1.6s the hand and the phone are COMPLETELY GONE and never return.
1.6-4.0s — the camera drifts gently upward a few degrees and the snowball fight runs at full tilt: the snowman whips his cocked twig arm forward and hurls his huge snowball, then cocks back again for another, his top hat jumping off his head and dropping back on with every throw; the four or five flying snowballs travel along their dotted arcs and burst in white star-shaped splats, and new snowballs launch from both sides to replace them; the elf popping up over the wall throws, ducks and pops up again; the ducking elf peeks out and claps his hands back over his pointed hat; the elf hit in the face flails his arms and legs in the air while the white splat on his head bursts bigger and his spinning hat tumbles; snow puffs burst off the top of the snow wall each time a ball lands, and the wall loses and regains lumps. Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment from 1.0s onward, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once. The picture is never still for even one tenth of a second.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER LEAVES THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the door. No twig arm, no snowball, no trajectory arc, no flying hat and no elf's boot ever crosses outside the curtain rectangle. If a pose would take a limb or a snowball out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Nothing lit ever appears on the white trim, the charcoal siding, the roof, the sky or the driveway except as reflected spill.

EVERYTHING ELSE IS UNCHANGED: the house, the door, the coach lanterns, the charcoal board-and-batten siding, the snow and the camera position are identical from first frame to last. No people, no cars, no pets enter frame.

NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural sound only — no music, no score, no background song. Cold quiet suburban night ambience, a soft phone tap, a faint electrical hum and tick from the lights, a distant car, light wind. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C05 — Lit facade — the stalk

**In the cut:** `starting_frames/v31_c05_g1.png` → `clips/v31_c05_g2.mp4`

#### Image prompt — `starting_frames/v31_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `35c7fadf-a111-44a5-85bd-6dde594338e2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210915_35c7fadf-a111-44a5-85bd-6dde594338e2.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c05_g1.png` · Higgsfield media `0f0bd301-46da-449b-a256-fc8baa127215`

````text
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a WHITE-PAINTED BRICK two-storey with BLACK trim, black window frames and a black roof, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: THE CAT IS ABOUT TO GO FOR THE CHRISTMAS TREE. On the RIGHT of the lit area stands a big triangular GREEN CHRISTMAS TREE hung with round baubles in many bright colours and a gold star on top, a few wrapped presents at its base. Hanging low on the nearest branch, one fat round RED BAUBLE dangles on a visible thread and swings slightly.

On the LEFT, a fat GINGER CAT is crouched flat to the floor in full stalking pose - shoulders hunched, back end raised and wiggling, TAIL STRAIGHT UP with a kink at the tip, two enormous round WHITE EYES locked dead on that red bauble, whiskers forward, ONE FRONT PAW LIFTED AND REACHING with the claws just out. A dotted curved aim-line runs from the raised paw to the dangling bauble. Behind the cat a small brown DOG lies fast asleep in a curl, completely oblivious, with a couple of little sleep-puff curls above his nose. A few gold stars and snowflakes scattered around. The whole scene is one piece of light art on the wall.

3. Different foreground: a low picket fence capped with snow along the bottom left and a shovelled path with a snowbank either side leading to the house.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated. The baubles on the tree especially must be many different bright colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole picture sits within the curtain rectangle with a clear band of dark unlit wall above it, below it and at both sides. The star on the tree does not touch the top edge, the presents and the sleeping dog do not touch the bottom edge, and neither the cat nor the tree touches the side edges. Nothing lit appears on the roof, the trim, the sky or the window frames.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the white brick wall behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the painted brick texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v31_c05_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `b2c4d7c9-aeea-4a28-9ff1-f399a1f05b8e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_104614_b2c4d7c9-aeea-4a28-9ff1-f399a1f05b8e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v31_c05_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c05_g1.png` · Higgsfield media `35c7fadf-a111-44a5-85bd-6dde594338e2`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same WHITE-PAINTED BRICK two-storey house with BLACK trim, black window frames and a black roof, same low snow-capped PICKET FENCE at the bottom-left, same shovelled path with a snowbank either side, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing THE STALK: at the RIGHT a big triangular GREEN CHRISTMAS TREE with multicoloured baubles and a gold star on top and presents at its base, with one fat round RED BAUBLE dangling on a visible thread from the nearest branch; at the LEFT a fat GINGER CAT crouched flat in full stalking pose, shoulders hunched, back end raised and wiggling, TAIL STRAIGHT UP with a kink at the tip, two enormous round WHITE EYES locked on the bauble, whiskers forward, ONE FRONT PAW LIFTED with the claws just out; a dotted curved aim-line running from his paw to the bauble; and behind the cat a small brown DOG fast asleep in a curl with sleep-puff curls above his nose.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the picket fence, the snowbanks and the shrubs at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

MOVEMENT — THE ANIMATION IS THE WHOLE POINT AND IT NEVER RESTS. It is already ON and running at full speed in the very first frame and is STILL running flat out in the last frame. THE FIGURES REDRAW COMPLETELY EVERY QUARTER SECOND — SIXTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each a big obvious physical movement, never a small twitch. NO BEAT IS EVER A BRIGHTNESS CHANGE: every single beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.
0.25s — the cat's raised back end wiggles hard side to side and his straight-up tail lashes right over, the kink at the tip flicking.
0.50s — the red bauble swings out wide on its thread and back again; the cat's whole head tracks it, whiskers fanning.
0.75s — his lifted front paw bats out at the air twice in quick succession, claws extending further each time.
1.00s — the dotted aim-line redraws as a completely new curve, and the dog's sleep puffs rise off his nose and pop.
1.25s — the cat flattens right down to the ground, ears pinning flat back, both huge white eyes blinking shut and snapping open.
1.50s — his haunches pump up and down twice, shoulders rolling, winding up to spring.
1.75s — his tail whips over to the other side and vibrates along its whole length.
2.00s — he swipes the air with BOTH front paws one after the other, his whole body twisting with each swipe.
2.25s — the red bauble swings its widest arc and knocks into a neighbouring bauble, setting that one swinging too.
2.50s — the whole tree shivers, every branch bouncing once, and three more baubles start swinging on their branches.
2.75s — the dog rolls right over in his sleep, all four legs going up in the air, and a fresh row of bigger sleep puffs curls up.
3.00s — the cat's ears swivel back toward the dog then snap forward again, and his nose twitches hard.
3.25s — he rises up on his back legs, both front paws swiping in the air above his head.
3.50s — the presents at the foot of the tree hop off the ground one after another and each CHANGES COLOUR as it lands.
3.75s — he drops into the deepest crouch of the whole clip, tail bolt upright and vibrating, eyes at their very widest.
4.00s — his front half lifts off the ground and stretches forward toward the bauble, back legs still planted, paws reaching — staying well inside the lit rectangle.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — the cat's tail, his paws, his ears, his eyes, the swinging red bauble, the tree's branches, the other baubles, the sleeping dog, the presents. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the white-painted brick front facade wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. THE BIGGER THE MOTION GETS, THE MORE STRICTLY THIS APPLIES. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No tail, no paw, no claw, no whisker, no branch, no bauble, no present and no sleep puff ever touches or crosses outside the curtain rectangle. At every instant, in every pose, every figure keeps a clear margin of at least two full unlit strands of dark wall inside every edge of the curtain — top, bottom, left and right. If a swipe, a leap, a lashing tail or a swinging bauble would reach an edge, THE POSE IS DRAWN SMALLER so it stays inside — the rectangle is never made bigger to fit it. Nothing spills onto the black trim, the window frames, the roof, the sky or the neighbouring houses. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail and does not gain size.

HARD RULES: no people, no cars, no real pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C05 on disk (1)**

#### Video prompt — `clips/v31_c05_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `380d11df-bf24-41b2-a225-576d505f9b18`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013614_380d11df-bf24-41b2-a225-576d505f9b18.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c05_g1.png` · Higgsfield media `35c7fadf-a111-44a5-85bd-6dde594338e2`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same WHITE-PAINTED BRICK two-storey house with BLACK trim, black window frames and a black roof, same low snow-capped PICKET FENCE at the bottom-left, same shovelled path with a snowbank either side, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing THE STALK: at the RIGHT a big triangular GREEN CHRISTMAS TREE with multicoloured baubles and a gold star on top and presents at its base, with one fat round RED BAUBLE dangling on a visible thread from the nearest branch; at the LEFT a fat GINGER CAT crouched flat in full stalking pose, shoulders hunched, back end raised and wiggling, TAIL STRAIGHT UP with a kink at the tip, two enormous round WHITE EYES locked on the bauble, whiskers forward, ONE FRONT PAW LIFTED with the claws just out; a dotted curved aim-line running from his paw to the bauble; and behind the cat a small brown DOG fast asleep in a curl with sleep-puff curls above his nose.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the picket fence, the snowbanks and the shrubs at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

MOVEMENT — the animation on the wall is already ON and running at full speed in the very first frame and is STILL running in the last frame. A CLEARLY DIFFERENT POSE EVERY HALF SECOND, the figures fully redrawing between beats like a hand-drawn light-bulb sign:
0.0-0.5s — the cat's raised back end wiggles hard side to side and his straight-up tail lashes over, the kink at the tip flicking; the red bauble swings on its thread.
0.5-1.0s — his lifted front paw bats out at the air twice, claws flashing brighter, and the dotted aim-line redraws as a new curve; the dog's sleep puffs rise and pop above his nose.
1.0-1.5s — he flattens right down to the ground, ears pinning back, his two huge white eyes blinking shut and snapping open again, whiskers fanning wide.
1.5-2.0s — his haunches pump up and down twice getting ready to spring, tail whipping the other way, and every bauble on the tree twinkles out and back in a rolling wave.
2.0-2.5s — he swipes the air with BOTH front paws in quick succession, the red bauble swinging wide on its thread and the gold star on the treetop flashing double-bright.
2.5-3.0s — the dog rolls over in his sleep, all four legs going up in the air, and a fresh row of bigger sleep puffs curls up; the cat's ears swivel back toward him and then snap forward again.
3.0-3.5s — the cat rises up on his back legs, both front paws in the air, and the presents at the foot of the tree hop once and each CHANGE COLOUR as they land.
3.5-4.0s — he drops back into the deepest crouch of the whole clip, tail bolt upright and vibrating, eyes at their widest, the red bauble swinging its biggest arc and the whole tree flashing brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once — the cat's tail, his paw, his eyes, the swinging bauble, the tree lights, the sleeping dog, the presents. The picture is never still for even one tenth of a second. A static or barely-moving picture is a total failure.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the white-painted brick front facade wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No tail, no paw, no whisker, no branch, no bauble, no present and no sleep puff ever crosses outside the curtain rectangle. If a pose would take a limb or a prop out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Nothing spills onto the black trim, the window frames, the roof, the sky or the neighbouring houses. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail.

HARD RULES: no people, no cars, no real pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C06 — Garage door + crowd — the tree goes over

**In the cut:** `starting_frames/v31_c06_g1.png` → `clips/v31_c06_g2.mp4`

#### Image prompt — `starting_frames/v31_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `4f451b00-4d75-4018-81df-983f08b36274`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210916_4f451b00-4d75-4018-81df-983f08b36274.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c06_g1.png` · Higgsfield media `63a2e39f-ba00-457e-b1d2-0302fbe6c6e2`

````text
Same shot as the attached image - same camera, same distance, same house-with-attached-double-garage-door composition, same crowd of onlookers in silhouette along the bottom, same snow, same night. Keep the camera and the staging EXACTLY.

CHANGE TWO THINGS ONLY:

A) THE HOUSE COLOURS: the house is now HONEY-TONED CEDAR SHINGLE siding with white trim, and the wide double garage door is DEEP NAVY BLUE with black iron strap hinges, instead of the colours in the reference.

B) THE PICTURE IN THE LIGHTS - throw it away completely and replace it with a much funnier, much wilder and MUCH MORE COLOURFUL cartoon scene, drawn chunky and simple out of the bulbs and filling the lit area fully.

THE NEW SCENE - THE CAT HAS GOT INTO THE CHRISTMAS TREE AND IT IS GOING OVER:

A big GREEN CHRISTMAS TREE stands off-centre, LEANING HARD OVER TO THE LEFT at a steep angle, mid-topple, its trunk bent and its branches whipping. A fat GINGER CAT clings halfway up the trunk with all four legs wrapped round it, eyes two huge round white circles, mouth open, tail bottled out fat and straight, a length of silver TINSEL wound round his body and trailing behind. The GOLD STAR has been flung off the top and tumbles through the air.

BAUBLES FLY EVERYWHERE - eight or nine of them launched off the branches in every direction on curved dotted paths, each a DIFFERENT BRIGHT COLOUR: emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - three of them bursting into white star-shaped splats where they hit.

THE PANIC AROUND IT: on the LEFT, SANTA is lunging in flat out with both arms stretched to catch the falling trunk, mouth wide open, one boot off the ground, his red hat flying off behind him. Under the tree a GREEN ELF is diving belly-first with both hands over his head. On the BOTTOM RIGHT a small brown DOG bolts out of frame at full sprint, ears flat back, legs stretched fore and aft, with three curved speed lines behind him. Wrapped presents at the base are scattering loose, each a different bright colour with a contrasting ribbon and bow.

Curved multicoloured speed lines streak behind the flying baubles, and bright stars in many colours are scattered right across the lit area so almost none of it is empty.

COLOUR IS THE POINT: this is a loud multicoloured light show - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated. It must NOT be mostly one or two colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit door above it, below it and at both sides. Nothing lit appears on the cedar siding, the roof, the sky, the hedge or the snow.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the navy garage door behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the cedar shingle texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v31_c06_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `31d32f03-5f02-40de-bb0b-412488e173b2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_104613_31d32f03-5f02-40de-bb0b-412488e173b2.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v31_c06_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c06_g1.png` · Higgsfield media `4f451b00-4d75-4018-81df-983f08b36274`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same HONEY-TONED CEDAR SHINGLE house with white trim, same DEEP NAVY BLUE double garage door with black iron strap hinges, same driveway throwing coloured light back, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing THE TREE GOING OVER: a big GREEN CHRISTMAS TREE off-centre LEANING HARD LEFT mid-topple, its trunk bent and its branches whipping; a fat GINGER CAT clinging halfway up the trunk with all four legs, his eyes two huge round white circles, his mouth open, his tail bottled out fat and straight, silver TINSEL wound round his body and trailing behind him; the GOLD STAR flung off the top and tumbling; eight or nine BAUBLES launched in every direction on curved dotted paths, each a different bright colour, three of them bursting into white star-shaped splats; at the LEFT SANTA lunging flat out with both arms stretched to catch the trunk, mouth wide open, one boot off the ground and his red hat flying off behind him; under the tree a GREEN ELF diving belly-first with both hands over his head; at the BOTTOM RIGHT a small brown DOG bolting out of frame at full sprint, ears flat back, legs stretched fore and aft, three curved speed lines behind him; and the presents at the base scattering loose.

ABSOLUTE FIRST RULE — THE LIT PICTURE IS TRAPPED INSIDE THE CURTAIN RECTANGLE. In the reference image the lit LED curtain is a rectangle hanging across the deep navy blue garage door only, and it stops short of the door's edges. That rectangle is FIXED for the whole four seconds: it never grows, never widens, never rises, never rescales, never warps, never drifts, and the camera never changes size on it. The tree, the cat, Santa, the elf, the dog, every bauble and every star are drawn INSIDE that rectangle with a clear band of unlit dark door left all the way round — a generous margin at the top, and margins at the left, right and bottom.
NOTHING LIT EVER CROSSES AN EDGE, AND THE BIGGER THE MOTION GETS THE MORE STRICTLY THIS APPLIES. No branch, no tail, no boot, no bauble, no speed line and no star ever touches or crosses the edge of the curtain, and nothing lit ever appears on the honey-toned cedar shingles, the white trim, the black iron strap hinges, the gables, the roof or the sky. At every instant, in every pose, every figure keeps a clear margin of at least two full unlit strands of dark door inside every edge of the curtain. If a pose would take a limb or a prop out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

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

THE ARTWORK IS THE MAIN EVENT AND IT IS FRANTIC. It is already animating in the very first frame — mid-cycle at 0.0s, not switching on and not holding still — and it redraws COMPLETELY EVERY QUARTER SECOND. SIXTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each a big obvious physical change, never a small twitch. NO BEAT IS EVER A BRIGHTNESS CHANGE: every single beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.
0.25s — the tree lurches further over to the left, every branch whipping the other way, and a fresh spray of baubles launches off it.
0.50s — the cat scrambles a whole body-length higher up the bent trunk, all four legs pumping.
0.75s — his bottled tail lashes right over and the tinsel unwinds another loop, trailing out behind him.
1.00s — the tumbling gold star spins over twice end over end and drops lower through the frame.
1.25s — three of the flying baubles burst into white star-shaped splats and their fragments scatter outward.
1.50s — the remaining baubles all CHANGE COLOUR at once and their dotted paths redraw at new angles.
1.75s — Santa stretches even further, both arms lengthening, his second boot leaving the ground entirely.
2.00s — his flying red hat tumbles end over end and the pom-pom whips round behind it.
2.25s — the tree rocks briefly back to the right and the cat is flung right round the trunk, legs flailing.
2.50s — the cat's eyes bulge wider and his mouth opens bigger as he scrabbles for grip, claws right out.
2.75s — the diving elf's legs kick up behind him and he slides forward on his belly.
3.00s — the scattered presents at the base all hop and tumble outward, the lids popping off two of them.
3.25s — the sprinting dog's legs redraw at full stretch and his three curved speed lines double in length.
3.50s — the tree lurches to its steepest lean of the whole clip, the trunk visibly bending.
3.75s — every branch sheds another burst of baubles and the whole tree shudders along its length.
4.00s — everything peaks at once: the cat at the very top of the trunk, Santa at full stretch flat out in the air, the elf sliding, and a fresh volley of baubles crossing the picture.
Every pose change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing. The coloured reflections on the driveway shift and ripple with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — the tree, the cat, the tinsel, Santa, the elf, the dog, the baubles, the star, the presents. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE. This must read as frantic, chaotic, laugh-out-loud cartoon slapstick with something big happening everywhere you look.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the deep navy blue garage door behind it: its horizontal panel seams, its black iron strap hinges, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE GARAGE DOOR IS THE ONLY LIT SURFACE. The artwork is hard-cropped at all four edges of the curtain. It NEVER grows, shrinks, shifts, warps or drifts. Nothing spills onto the honey-toned cedar shingles, the white trim, the gables, the roof or the sky.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C06 on disk (1)**

#### Video prompt — `clips/v31_c06_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `55ebcd13-cd5f-48c7-ad90-7924b972b236`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013614_55ebcd13-cd5f-48c7-ad90-7924b972b236.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c06_g1.png` · Higgsfield media `4f451b00-4d75-4018-81df-983f08b36274`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same HONEY-TONED CEDAR SHINGLE house with white trim, same DEEP NAVY BLUE double garage door with black iron strap hinges, same driveway throwing coloured light back, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing THE TREE GOING OVER: a big GREEN CHRISTMAS TREE off-centre LEANING HARD LEFT mid-topple, its trunk bent and its branches whipping; a fat GINGER CAT clinging halfway up the trunk with all four legs, his eyes two huge round white circles, his mouth open, his tail bottled out fat and straight, silver TINSEL wound round his body and trailing behind him; the GOLD STAR flung off the top and tumbling; eight or nine BAUBLES launched in every direction on curved dotted paths, each a different bright colour, three of them bursting into white star-shaped splats; at the LEFT SANTA lunging flat out with both arms stretched to catch the trunk, mouth wide open, one boot off the ground and his red hat flying off behind him; under the tree a GREEN ELF diving belly-first with both hands over his head; at the BOTTOM RIGHT a small brown DOG bolting out of frame at full sprint, ears flat back, legs stretched fore and aft, three curved speed lines behind him; and the presents at the base scattering loose.

ABSOLUTE FIRST RULE — THE LIT PICTURE IS TRAPPED INSIDE THE CURTAIN RECTANGLE. In the reference image the lit LED curtain is a rectangle hanging across the deep navy blue garage door only, and it stops short of the door's edges. That rectangle is FIXED for the whole four seconds: it never grows, never widens, never rises, never rescales, never warps, never drifts, and the camera never changes size on it. The tree, the cat, Santa, the elf, the dog, every bauble and every star are drawn INSIDE that rectangle with a clear band of unlit dark door left all the way round — a generous margin at the top, and margins at the left, right and bottom.
NOTHING LIT EVER CROSSES AN EDGE. No branch, no tail, no boot, no bauble, no speed line and no star ever touches or crosses the edge of the curtain, and nothing lit ever appears on the honey-toned cedar shingles, the white trim, the black iron strap hinges, the gables, the roof or the sky. If a pose would take a limb or a prop out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

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
0.2s — the tree lurches further over to the left, every branch whipping the other way, and a fresh spray of baubles launches off it.
0.6s — the cat scrambles a body-length higher up the bent trunk, all four legs pumping, his bottled tail lashing and the tinsel unwinding another loop behind him.
1.0s — the tumbling gold star spins over twice and FLASHES double-bright at the top of its arc.
1.4s — three of the flying baubles burst into white star-shaped splats and the rest all CHANGE COLOUR at once, their dotted paths redrawing at new angles.
1.8s — Santa stretches even further, both arms lengthening, his second boot leaving the ground, his flying red hat tumbling end over end behind him.
2.2s — the tree rocks briefly back to the right and the cat is flung round the trunk, eyes bulging wider, mouth opening bigger.
2.6s — the diving elf's legs kick up behind him and he slides, and the scattered presents at the base all hop and tumble outward.
3.0s — the sprinting dog's legs redraw at full stretch and his three curved speed lines double in length; his ears flatten harder.
3.4s — the tree lurches to its steepest lean of the whole clip, the trunk bending visibly, and every branch sheds another burst of baubles.
3.8s — everything peaks at once: the cat at the very top of the trunk, Santa at full stretch, the elf flat out, a whole fresh volley of baubles in the air, and the picture flashing brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing. The coloured reflections on the driveway shift and ripple with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once — the tree, the cat, Santa, the elf, the dog, a bauble, the star. The picture is never still for even one tenth of a second. A static or barely-moving picture is a total failure.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the deep navy blue garage door behind it: its horizontal panel seams, its black iron strap hinges, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE GARAGE DOOR IS THE ONLY LIT SURFACE. The artwork is hard-cropped at all four edges of the curtain. It NEVER grows, shrinks, shifts, warps or drifts. Nothing spills onto the honey-toned cedar shingles, the white trim, the gables, the roof or the sky.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C07 — Car-window POV — the cat has won

**In the cut:** `starting_frames/v31_c07_g1.png` → `clips/v31_c07_g1.mp4`

#### Image prompt — `starting_frames/v31_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `51cc4d69-b280-4be2-86cc-86d96d35e32c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_210916_51cc4d69-b280-4be2-86cc-86d96d35e32c.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `40058517-9846-48c1-88e3-d48519a63b52`

````text
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a PALE GREY STONE gable with crisp white trim and white window frames, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: THE CAT HAS WON. Across the BOTTOM of the lit area the CHRISTMAS TREE lies FLAT ON ITS SIDE, wrecked - trunk horizontal, branches splayed and bent, tinsel spilling off it, baubles scattered loose around it in many bright colours with two of them cracked cleanly in half.

Sitting BOLT UPRIGHT ON TOP of the fallen trunk, right in the middle of the picture, is the fat GINGER CAT - chest out, tail curled neatly round his front paws, eyes half-closed into two smug curved slits, a tiny satisfied smile. The GOLD STAR from the top of the tree sits CROOKED ON HIS HEAD like a party hat, and a strand of silver tinsel is draped over one ear.

Beside him on the LEFT, SANTA lies FLAT ON HIS BACK in the wreckage with both boots up in the air, arms out wide, eyes as two spiral swirls, a bright bauble clutched in each hand and his red hat over one eye. On the RIGHT a GREEN ELF peers in from the edge with both hands pressed to his cheeks and a wide open mouth. A small brown DOG's face pokes in low at the bottom right corner, just his eyes and nose showing. Small gold stars scattered around. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated. The scattered baubles especially must be many different bright colours.

3. A different parked car at the kerb - a TEAL-BLUE camper van instead of the car in the reference - and a snow-covered hedge at the right edge.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit gable above it, below it and at both sides. The star on the cat's head does not touch the top edge, the fallen tree does not touch the bottom edge, and nothing touches the side edges. Nothing lit appears on the roof, the trim, the window frames or the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the pale grey stone gable behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the stone texture and the wet road reflections clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v31_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `d08d67c6-9a01-44bc-ba30-8c0228490fc6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_013614_d08d67c6-9a01-44bc-ba30-8c0228490fc6.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v31_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c07_g1.png` · Higgsfield media `51cc4d69-b280-4be2-86cc-86d96d35e32c`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same view shot from inside a moving car through the open passenger side window with the dark window frame framing the bottom-left corner, same wet reflective road throwing long smeared coloured reflections, same snowy verge, same street lamp, same row of neighbouring houses glowing down the street, same TEAL-BLUE CAMPER VAN parked at the kerb, same snow-covered hedge at the right edge, same PALE GREY STONE gable with crisp white trim and white window frames carrying the lit LED curtain, which shows THE CAT HAS WON: across the BOTTOM the CHRISTMAS TREE lies FLAT ON ITS SIDE, wrecked — trunk horizontal, branches splayed and bent, tinsel spilling, baubles scattered loose in many bright colours with two of them cracked cleanly in half; sitting BOLT UPRIGHT on the fallen trunk in the middle, the fat GINGER CAT, chest out, tail curled neatly round his front paws, eyes half-closed into two smug curved slits, a tiny satisfied smile, the GOLD STAR sitting CROOKED ON HIS HEAD like a party hat and a strand of silver tinsel draped over one ear; at the LEFT SANTA flat on his back in the wreckage, both boots up, arms out wide, his eyes two spiral swirls, a bright bauble clutched in each hand and his red hat over one eye; at the RIGHT a GREEN ELF peering in from the edge with both hands pressed to his cheeks and his mouth wide open; and in the BOTTOM RIGHT CORNER the small brown DOG's face poking in, just his eyes and his nose.

CAMERA — HANDHELD VERTICAL PHONE VIDEO SHOT OUT OF A MOVING CAR SIDE WINDOW AT NIGHT. THE CAR IS DRIVING FORWARD and closing in on the house, so the gable wall grows steadily and continuously LARGER across the four seconds and NEVER recedes. Real vehicle motion: the road surface and the snow verge flow past the bottom of frame at speed, roadside objects sweep past with strong parallax, the frame rocks gently with the suspension. As the car advances the operator slowly pans right to hold the lit wall in frame. THIS IS DRIVING, NOT ZOOMING: no focal length change, no digital zoom, no gimbal glide, no drone move, and the car never stops, never rolls to a halt and never reverses.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove and no device anywhere in the foreground. Only the car's own dark window frame, exactly as in the reference image, sits at the bottom-left.

MOVEMENT — THE PICTURE MUST NOT STAND STILL. Every character stays in the same place in the picture and nothing drifts across the curtain, but nothing in the artwork is static for even one beat. This is the most important instruction in this prompt: a CLEARLY DIFFERENT POSE EVERY HALF SECOND, the figures fully redrawing between beats like an animated light-bulb sign.
0.0-0.5s — the cat's curled tail flicks up off his paws and sweeps side to side, the crooked gold star on his head wobbling and flashing, his ears swivelling.
0.5-1.0s — Santa's two boots kick up in the air and drop back, his spiral eyes spin round, and the two baubles clutched in his hands flash alternately.
1.0-1.5s — the cat's smug eyes open into two huge round circles for a beat then narrow back to slits, and he licks one front paw and smooths it over his ear, the tinsel strand swinging.
1.5-2.0s — the elf's hands flap on and off his cheeks and his mouth opens and shuts three times; the dog's face in the corner ducks out of frame and pops straight back in.
2.0-2.5s — the loose scattered baubles roll along the fallen trunk, each one CHANGING COLOUR as it goes, and the two cracked halves rock on the spot.
2.5-3.0s — the fallen tree's splayed branches spring and settle, the spilled tinsel ripples along its length in a wave, and Santa's red hat slides further down over his eye.
3.0-3.5s — the cat puffs his chest out bigger, raises his chin and his whiskers fan wide; the star on his head tips to the other side; the dog's eyes blink.
3.5-4.0s — everything peaks together: the cat's tail lashes its widest, Santa kicks both boots high and his spiral eyes spin fastest, the elf throws both hands over his head, the dog's whole face pushes further into the corner, every loose bauble flashes, and the whole picture flashes brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. The coloured reflections on the wet road shift and streak with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST FOUR DIFFERENT THINGS in the artwork are changing at once — the cat's tail, his eyes, the star on his head, Santa's boots, his spiral eyes, the elf's hands, the dog's face, the rolling baubles, the tinsel. The picture is never still for even one tenth of a second. A static or barely-moving picture is a total failure.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the pale grey stone gable wall". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the wall behind it: its stone courses, its white trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No tail, no boot, no branch, no bauble, no tinsel strand, no elf's hand and no dog's ear ever crosses the roof edge or the corner of the wall — every pose keeps a clear margin of dark wall inside the rectangle. If a pose would take a limb or a prop out to an edge, THE POSE IS MADE SMALLER so it stays inside; the rectangle is never made bigger to fit it. Nothing spills onto the roof, the white trim, the white window frames, the sky, the verge, the parked teal-blue camper van, the snow-covered hedge or the neighbouring houses. As the car gets closer the bulb grid simply becomes coarser and the individual bulbs bigger and more countable — the artwork does not gain detail.

HARD RULES: no people and no other vehicles enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Tyres on wet road, a low engine hum, cold air rushing past the open window, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night from a car. Noisy shadows, blown highlights around the bulbs, slight rolling-shutter wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C07 on disk (1)**

#### Video prompt — `clips/v31_c07_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `7b33451f-4180-43f5-a850-66982e12566a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260917_104613_7b33451f-4180-43f5-a850-66982e12566a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_31_assets/starting_frames/v31_c07_g1.png` · Higgsfield media `51cc4d69-b280-4be2-86cc-86d96d35e32c`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same view shot from inside a moving car through the open passenger side window with the dark window frame framing the bottom-left corner, same wet reflective road throwing long smeared coloured reflections, same snowy verge, same street lamp, same row of neighbouring houses glowing down the street, same TEAL-BLUE CAMPER VAN parked at the kerb, same snow-covered hedge at the right edge, same PALE GREY STONE gable with crisp white trim and white window frames carrying the lit LED curtain, which shows THE CAT HAS WON: across the BOTTOM the CHRISTMAS TREE lies FLAT ON ITS SIDE, wrecked — trunk horizontal, branches splayed and bent, tinsel spilling, baubles scattered loose in many bright colours with two of them cracked cleanly in half; sitting BOLT UPRIGHT on the fallen trunk in the middle, the fat GINGER CAT, chest out, tail curled neatly round his front paws, eyes half-closed into two smug curved slits, a tiny satisfied smile, the GOLD STAR sitting CROOKED ON HIS HEAD like a party hat and a strand of silver tinsel draped over one ear; at the LEFT SANTA flat on his back in the wreckage, both boots up, arms out wide, his eyes two spiral swirls, a bright bauble clutched in each hand and his red hat over one eye; at the RIGHT a GREEN ELF peering in from the edge with both hands pressed to his cheeks and his mouth wide open; and in the BOTTOM RIGHT CORNER the small brown DOG's face poking in, just his eyes and his nose.

CAMERA — HANDHELD VERTICAL PHONE VIDEO SHOT OUT OF A MOVING CAR SIDE WINDOW AT NIGHT. THE CAR IS DRIVING FORWARD and closing in on the house, so the gable wall grows steadily and continuously LARGER across the four seconds and NEVER recedes. Real vehicle motion: the road surface and the snow verge flow past the bottom of frame at speed, roadside objects sweep past with strong parallax, the frame rocks gently with the suspension. As the car advances the operator slowly pans right to hold the lit wall in frame. THIS IS DRIVING, NOT ZOOMING: no focal length change, no digital zoom, no gimbal glide, no drone move, and the car never stops, never rolls to a halt and never reverses.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove and no device anywhere in the foreground. Only the car's own dark window frame, exactly as in the reference image, sits at the bottom-left.

MOVEMENT — THE PICTURE MUST NEVER STAND STILL, NOT FOR A SINGLE BEAT. Every character stays in the same place in the picture and nothing drifts across the curtain, but nothing in the artwork is static for even one beat. This is the most important instruction in this prompt: THE FIGURES REDRAW COMPLETELY EVERY QUARTER SECOND — SIXTEEN DISTINCT POSE CHANGES ACROSS THE FOUR SECONDS, each a big obvious physical movement, never a small twitch. NO BEAT IS EVER A BRIGHTNESS CHANGE: every single beat is a figure physically moving into a new pose. Nothing flashes, strobes, blinks, twinkles or pulses.
0.25s — the cat's curled tail flicks up off his paws and sweeps side to side; the crooked gold star on his head wobbles and slides an inch.
0.50s — his ears swivel out wide and back, and the tinsel strand draped over one ear swings loose.
0.75s — Santa's two boots kick high up in the air and drop back down into the wreckage.
1.00s — Santa's spiral eyes spin round twice and the two baubles clutched in his fists shake hard.
1.25s — the cat's smug eyes open into two huge round circles for a beat, then narrow back to slits.
1.50s — he licks one front paw and smooths it right over his ear, the tinsel swinging with the movement.
1.75s — the elf's hands flap on and off his cheeks and his mouth opens and shuts twice.
2.00s — the dog's face in the corner ducks out of frame and pops straight back in, ears flapping.
2.25s — the loose baubles roll along the fallen trunk, each one CHANGING COLOUR as it goes.
2.50s — the two cracked halves rock on the spot and one tips right over; a bauble rolls off the trunk.
2.75s — the fallen tree's splayed branches spring up and settle back down, shedding tinsel.
3.00s — the spilled tinsel ripples along the trunk's whole length in a travelling wave.
3.25s — Santa's red hat slides further down over his eye and he waggles both boots in the air.
3.50s — the cat puffs his chest out bigger, raises his chin and his whiskers fan wide; the star tips to the other side.
3.75s — the dog's whole face pushes further into the corner and his nose twitches; the elf throws both hands up over his head.
4.00s — everything peaks together: the cat's tail lashing its widest, Santa kicking both boots high with his spiral eyes spinning fastest, the elf's hands above his head, the dog's face at its furthest in, every loose bauble rolling.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. The coloured reflections on the wet road shift and streak with every change.

DENSITY OF MOTION — HARD RULE: at every single moment of the four seconds, AT LEAST SIX DIFFERENT THINGS in the artwork are changing at once — the cat's tail, his eyes, his ears, the star on his head, Santa's boots, his spiral eyes, the elf's hands, the dog's face, the rolling baubles, the tinsel, the branches. The picture is never still for even one twentieth of a second. A calm, slow, sparse or barely-moving picture is a TOTAL FAILURE.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the pale grey stone gable wall". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the wall behind it: its stone courses, its white trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. THE BIGGER THE MOTION GETS, THE MORE STRICTLY THIS APPLIES. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No tail, no boot, no branch, no bauble, no tinsel strand, no elf's hand and no dog's ear ever crosses the roof edge or the corner of the wall. At every instant, in every pose, every figure keeps a clear margin of at least two full unlit strands of dark wall inside every edge of the curtain — top, bottom, left and right. If a kicking boot, a lashing tail, a rolling bauble or a thrown-up hand would reach an edge, THE POSE IS DRAWN SMALLER so it stays inside; the rectangle is never made bigger to fit it. Nothing spills onto the roof, the white trim, the white window frames, the sky, the verge, the parked teal-blue camper van, the snow-covered hedge or the neighbouring houses. As the car gets closer the bulb grid simply becomes coarser and the individual bulbs bigger and more countable — the artwork does not gain detail and does not gain size.

HARD RULES: no people and no other vehicles enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Tyres on wet road, a low engine hum, cold air rushing past the open window, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night from a car. Noisy shadows, blown highlights around the bulbs, slight rolling-shutter wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````
