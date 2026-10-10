# Video 29 — The snowball war

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_29.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

**Historical initial stage:** start frames only. No clips yet, no hook shot.
**Scope:** B-roll only, the same six shots as v20 – v28 — C02 … C07.
**Date:** 2026-09-15
**Model:** `gpt_image_2` · aspect `9:16` · resolution `2k` · quality `medium` · `use_unlim false` · `count 1`
**Output:** 1520 × 2688 PNG, one generation per shot, no re-rolls.

Daniel's brief for this one:

- One improvement — **for C3 and C4 use a garage that is incorporated into a house**, like the one used in C6, instead of the detached two-car garage used in v20 – v28.
- **C2 and C3 must be the same woman.**
- **C3 and C4 must be the same garage, house and background**, just a different angle (from the front), with all the lights set up, at night.
- All frames **extremely high quality, perfect light, iPhone shots, nothing blurish.**

The gag run is new — v20 "Santa Won't Inflate" through v28 "The reindeer mutiny" each had their own; this one is **the snowball war**, a three-beat story across C5 → C6 → C7: the ambush, the all-out war, and the snowman winning.

---

#### The v29 look

**The woman (C2, C3)** — late twenties, fair skin, COPPER-RED hair in a high ponytail.
Indoors: forest-green ribbed knit jumper, camel wide-leg trousers.
Outdoors: burgundy puffer jacket, dark blue jeans, cream beanie, tan boots.

**The room (C2)** — warm oak herringbone floor, cream bouclé sofa with rust and mustard cushions and an oatmeal chunky-knit throw, sage-green panelled wainscot behind, woven rattan dome pendant, flocked white fir with gold baubles and red berry sprigs at the right.

**The house (C3, C4 — the same building)** — two-storey family home, **attached garage wing projecting forward on the left**, main house body continuing to the right and set slightly back in the same building. Warm sand-beige lap siding, crisp white trim. Soft white sectional double garage door with recessed panels and a row of small square windows across the top. Gable above the garage with a round white louvre vent, roofline running continuously into the house roofline. Covered front porch on white posts, dark red front door, two upstairs windows with white frames glowing warm. Black coach lanterns either side of the garage door. White gutter and white downpipe on the left. Concrete driveway with patchy snow, clipped boxwood hedge at the foot of the porch, bare white birch at the left edge.

**The showcase houses** — C5 buttermilk-yellow clapboard two-storey; C6 deep slate-blue board-and-batten with a natural oak double garage door; C7 warm cream stone gable with dark bronze trim.

**Carried over from v28, unchanged** — the approved iPhone is *copied* from the v28 C4 frame rather than described from scratch; the curtain wire is **BLACK** with dark unlit bulbs; the lit curtain is always **separate hanging vertical strands with dark gaps, never an LED panel**; the artwork stays inside the curtain rectangle; **absolutely no text** anywhere in the lights.

**New for v29** — every prompt ends on an explicit sharpness block: tack-sharp edge to edge, no motion blur, no depth-of-field blur, no soft focus, no grain, no haze. This is the answer to "nothing blurish".

---

#### References used

| Ref | Media / job id | What it was passed for |
|---|---|---|
| v20 C2 frame | `05989e1b-228c-432a-be58-a51cfbfa19ad` | C2 geometry — sofa **in front of her**, running diagonally into depth |
| v28 C2 frame | `b870ee3e-2453-4d24-8dab-4909ce45bd14` | C2 camera height — shoulder height, only a slight downward tilt |
| v28 C3 frame | `d4281baa-e62d-413c-b416-f7b09157d9fd` | C3 flat frontal framing, the step-stool staging, the black wire |
| v28 C4 frame | `a734b552-ed83-4ab2-84c6-e9b3d4d1d833` | C4 pulled-back framing, **the approved iPhone**, the app screen |
| v28 C5 frame | `a33527ab-d0c8-4c72-8795-00dcffb907ec` | C5 framing — same camera, same lit span |
| v28 C6 g2 frame | `77e2f041-136e-4c3e-ba53-fd386899e071` | C6 camera, house-with-garage-door framing, crowd in silhouette |
| v28 C7 frame | `058a0783-9754-481c-a79a-04c0deb1154c` | C7 framing — shooting out through the car side window |

---

#### Continuity chain

Each link passes the **previous job id** as a reference, so the model sees the actual generated frame, not a description of it.

```
v20 C2 + v28 C2  ->  C2   (geometry + camera height)
v28 C3 + C2 job  ->  C3   (framing + THE WOMAN)
v28 C4 + C3 job  ->  C4   (iPhone/app + THE HOUSE, now at night)
v28 C5           ->  C5   (standalone)
v28 C6 g2        ->  C6   (standalone)
v28 C7           ->  C7   (standalone)
```

`C2 job -> C3` locks the woman. `C3 job -> C4` locks the house, the garage, the driveway and the street.

The attached-garage change was made **in text on C3**, not by attaching the v28 C6 frame as a third reference — C6 is a night shot with a lit curtain and a crowd, and passing it into a daytime install shot would have dragged that contamination in. It rendered correctly: an attached garage wing with the house body and porch carrying on to the right.

---

## C02 — Box over the sofa

Refs: v20 C2 frame (geometry) + v28 C2 frame (camera height).

**Frame:** `v29_c02_g1.png`

### Image prompt

```
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. The box is a closed rigid printed gift box with NO transparent window and NO cut-out panel anywhere on it. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: a late-twenties woman with fair skin and COPPER-RED hair worn in a high ponytail, wearing a FOREST-GREEN ribbed knit jumper and CAMEL wide-leg trousers. The room has a warm oak HERRINGBONE floor, a CREAM BOUCLE sofa with rust and mustard cushions and an oatmeal chunky-knit throw, a SAGE-GREEN panelled wainscot wall behind, a woven RATTAN dome pendant lamp hanging above, and a FLOCKED WHITE fir Christmas tree with gold baubles and red berry sprigs at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the knit of her jumper and in the print on the box, clean even indoor light with no blown highlights and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur on the box or on her, NO grain, NO haze, NO soft focus anywhere. Candid UGC, no text overlay, no watermark.
```

---

## C03 — Mounting on the attached garage, day

Refs: v28 C3 frame (framing, staging, black wire) + **v29 C2 job** (the woman).

**Frame:** `v29_c03_g1.png`

### Image prompt

```
Same shot as the FIRST attached image - copy its camera, its framing and its staging EXACTLY. Daytime, overcast winter light, snow on the ground. A woman stands on a black folding step stool, seen from BEHIND, facing the wall, both arms raised in front of her, her hands up at the trim board above the garage door as she fixes the LED curtain to it. The big bundle of unlit LED curtain strands is heaped on the snow at the foot of the stool. The wide sectional DOUBLE GARAGE DOOR with horizontal panel seams, recessed rectangular panels and a row of small square windows across the top fills most of the frame behind her, and the curtain hangs DOWN OVER THE GARAGE DOOR ITSELF.

THE ONE BIG CHANGE - THIS IS NOT A DETACHED GARAGE ANY MORE. It is an ATTACHED GARAGE THAT IS PART OF A HOUSE: a single two-storey family home whose garage wing projects forward on the LEFT, with the MAIN HOUSE BODY clearly continuing to the RIGHT and set slightly back in the same building - two storeys tall, with a covered front porch on white posts, a DARK RED front door, and two upstairs windows with white frames and warm light inside. Above the garage door there is a gable with a round white louvre vent, and the roofline of the garage runs continuously into the roofline of the house. It must read unmistakably as ONE house with its garage built into it, NOT a separate garage building standing on its own in a yard. Do not leave empty sky or open yard where the house body should be.

THE CAMERA ANGLE IS FLAT AND FRONTAL, exactly as in the first image: the garage door faces the camera almost square-on and fills the frame, its horizontal seams run dead level and its vertical edges run straight up and down. The garage is NOT turned away at an angle, NOT receding steeply into the distance, NO strong oblique perspective, NO wide-angle corner view. The house body is visible along the right side of the frame in the same flat perspective.

THE HOUSE ITSELF - take it from this text only and NOT from the first attached image: WARM SAND-BEIGE lap siding with crisp WHITE trim; the garage door is soft WHITE with recessed panels and its row of small square windows; a BLACK COACH LANTERN with a lantern-shaped glass housing mounted either side of the garage door; the gutter along the roof edge and the downpipe are WHITE and the downpipe runs down the LEFT side; a plain CONCRETE driveway showing through patchy snow; a clipped boxwood hedge along the foot of the porch at the right; a bare white BIRCH tree at the left edge. Do NOT copy the navy board-and-batten, the cream door, the brass barn lights, the gravel driveway, the firewood stack or the spruce from the first image.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand hanging down the garage door is a thin BLACK cord with small DARK unlit bulbs on it, and against the white door the strands read as obvious thin dark lines. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - take her from the SECOND attached image: the same late-twenties woman with fair skin and COPPER-RED hair, here worn in a high ponytail spilling out from under a cream beanie. Outdoors she wears a BURGUNDY puffer jacket, dark blue jeans and tan boots. Same face, same hair colour, same person as in the second image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the siding boards, the door panels and the black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

---

## C04 — Phone POV, the same house at night

Refs: v28 C4 frame (iPhone + app screen + pulled-back framing) + **v29 C3 job** (the house).

**Frame:** `v29_c04_g1.png`

### Image prompt

```
Same shot as the FIRST attached image - copy its staging, its camera distance and its content EXACTLY. Night. The camera is a long way back so the WHOLE building is in frame, complete and large, with the LED curtain hanging down the garage door and a hand holding a phone up big in the bottom-centre foreground.

THE PHONE - COPY IT EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same size in frame, same position at the bottom centre, same hand, same grip, same angle. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline. Pulling the camera back must NOT shrink this phone; it stays big in the foreground.

THE SCREEN SHOWS THE SAME APP as the first image: a dark navy-blue app screen filled with a neat grid of small square scene thumbnails, each one a tiny colourful Christmas light picture on a dark background, one of them ringed with a bright highlight, and a BIG ROUND BLUE PLAY BUTTON centred near the bottom of the screen. The screen glows and throws its light up onto the fingers and the palm. NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is just the grid of thumbnails and the round play button.

THE BUILDING - TAKE IT FROM THE SECOND ATTACHED IMAGE. It must read as LITERALLY THE SAME HOUSE, the same property and the same street as the second image, now at night and seen whole from much further back: the SAME two-storey family home with its ATTACHED GARAGE WING projecting forward on the LEFT and the MAIN HOUSE BODY continuing to the RIGHT and set slightly back in the same building, the same WARM SAND-BEIGE lap siding with WHITE trim, the same soft WHITE sectional double garage door with its panel seams and its row of small square windows across the top, the same gable with the round white louvre vent above the garage, the same covered front porch on white posts with the DARK RED front door, the same two upstairs windows with white frames glowing warm inside, the same BLACK COACH LANTERN either side of the garage door, the same WHITE gutter and WHITE downpipe on the LEFT, the same CONCRETE driveway with patchy snow, the same clipped boxwood hedge at the foot of the porch and the same bare white BIRCH at the left edge. Do NOT copy the house, the siding, the door colour, the lamps or the driveway from the first image.

THE CAMERA - A DIFFERENT, WIDER ANGLE THAN THE SECOND IMAGE BUT STILL FROM THE FRONT: pulled right back and standing square on to the front of the house from the end of the driveway, so the garage wing AND the whole house body, the porch and the roofline are all inside the frame with room around them. The facade faces the camera flat, the horizontal lines run dead level and the vertical edges run straight up and down. NOT turned away at an angle, NOT receding into the distance, NO strong oblique perspective, NO corner view, NOT a low worm's-eye tilt looking up.

THE LED CURTAIN IS ALREADY FULLY MOUNTED AND IT IS BLACK - CRITICAL: it hangs from the trim board above the garage door in evenly spaced vertical see-through strands, down across the full width of the door, with slight natural sag and an uneven bottom hem. The wire is BLACK, not white and not clear, every strand a thin BLACK cord with small DARK unlit bulbs on it, no glow. Against the white door the strands read as clear thin dark vertical lines. No white wire, no clear wire, no silver wire anywhere.

Lighting: the two black coach lanterns glowing warm either side of the garage door, the porch light on, the upstairs windows warm, a street lamp glow from the left, snow on the driveway catching the light.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved and the whole facade in focus, the siding boards and the door panels clearly readable, correct exposure with no blown-out highlights around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

---

## C05 — Lit facade — the ambush

Ref: v28 C5 frame. Beat one of the snowball war.

**Frame:** `v29_c05_g1.png`

### Image prompt

```
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a BUTTERMILK-YELLOW clapboard two-storey with crisp white trim, white window frames and a charcoal-grey roof, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: SANTA IS AMBUSHED IN A SNOWBALL FIGHT. On the RIGHT of the lit area a big three-ball SNOWMAN with a black top hat, a bright orange carrot nose, coal eyes and a red scarf is winding up, twisted right back, holding a GIANT snowball high over his head with both twiggy stick arms, one stick arm cocked, grinning with a wide mouth of coal teeth. On the LEFT, SANTA is crouched down low behind a white snowbank, only his red hat, his white eyebrows and two round white eyes showing over the top of it, a little snowball clutched in one raised hand and a stack of presents piled beside him like a barricade. Between them, two small snowballs are already flying across the middle of the picture on curved dotted paths, one bursting into a little white splat. A few small gold stars and snowflakes scattered around. The whole scene is one piece of light art on the wall.

3. Different foreground: a low picket fence capped with snow along the bottom left and a shovelled path with a snowbank either side leading to the house.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole picture sits within the curtain rectangle with a clear band of dark unlit wall above it, below it and at both sides. The snowman's hat and the raised snowball do not touch the top edge, the snowbank and the presents do not touch the bottom edge, and neither figure touches the side edges. Nothing lit appears on the roof, the trim, the sky or the window frames.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the buttermilk-yellow clapboard wall behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the clapboard texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

## C06 — Garage door + crowd — the snowball war

Ref: v28 C6 g2 frame. Beat two — the all-out war, and the loudest colour shot in the ad.

**Frame:** `v29_c06_g1.png`

### Image prompt

```
Same shot as the attached image - same camera, same distance, same house-with-attached-double-garage-door composition, same crowd of onlookers in silhouette along the bottom, same snow, same night. Keep the camera and the staging EXACTLY.

CHANGE TWO THINGS ONLY:

A) THE HOUSE COLOURS: the house is now DEEP SLATE-BLUE board-and-batten siding with white trim, and the wide double garage door is NATURAL OAK WOOD with dark iron strap hinges, instead of terracotta stucco with a white door.

B) THE PICTURE IN THE LIGHTS - throw it away completely and replace it with a much funnier, much wilder and MUCH MORE COLOURFUL cartoon scene, drawn chunky and simple out of the bulbs and filling the lit area fully.

THE NEW SCENE - AN ALL-OUT SNOWBALL WAR, SANTA AND THE ELVES AGAINST THE SNOWMEN:

Across the RIGHT of the lit area, THREE SNOWMEN in a ragged line are firing: the first winding up a giant snowball over his head, the second flinging one sidearm with his twiggy stick arm blurred into a curved motion arc, the third loading a huge home-made CATAPULT built out of candy canes, its bucket loaded with a stack of snowballs. All three have black top hats, bright orange carrot noses and scarves in different colours - red, turquoise and hot pink.

On the LEFT, SANTA is diving flat out through the air horizontally, both arms forward, mouth wide open, eyes as two white circles, his red hat blown off above him and his white beard streaming sideways, one boot flying off. Behind him TWO GREEN ELVES crouch behind a barricade of stacked presents, one popping up to throw, the other holding a saucepan lid over his head as a shield.

SNOWBALLS AND PRESENTS FILL THE AIR - eight or nine snowballs streaking across the middle on curved dotted paths, three of them bursting into white star-shaped splats, and five or six presents knocked loose and tumbling, each a DIFFERENT BRIGHT COLOUR: emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow. Two presents have burst open with little coloured shapes spilling out.

Curved multicoloured speed lines streak behind the thrown snowballs, and bright stars in many colours are scattered right across the lit area so almost none of it is empty.

COLOUR IS THE POINT: this is a loud multicoloured light show - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated. It must NOT be mostly one or two colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit door above it, below it and at both sides. Nothing lit appears on the siding, the roof, the sky, the hedge or the snow.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the oak garage door behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the wood grain of the garage door and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

## C07 — Car-window POV — the snowman wins

Ref: v28 C7 frame. Beat three, the payoff.

**Frame:** `v29_c07_g1.png`

### Image prompt

```
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a WARM CREAM STONE gable with dark bronze trim and dark bronze window frames, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: THE SNOWMAN HAS WON. A GIANT THREE-BALL SNOWMAN fills the full height of the lit area, standing square to us, both twiggy stick arms thrown up in the air in victory, a black top hat tipped back on his head, a bright orange carrot nose, coal eyes and a wide grin of coal teeth, a turquoise scarf flapping out to one side. SANTA IS STUCK HEAD-FIRST IN THE SNOWMAN'S BELLY - only his red trousers, his black belt and his two legs stick straight out of the middle snowball, boots kicking apart in the air, one boot flying off and a red-and-white striped sock showing underneath. Santa's red hat lies fallen in the snow at the snowman's base. Two chunky curved motion arcs sweep out from Santa's kicking legs and a small puff of snow bursts out around his waist. Small gold stars scattered around the pair. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

3. A different parked car at the kerb - a mustard-yellow pickup truck instead of the car in the reference - and a snow-covered hedge at the right edge.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit gable above it, below it and at both sides. The snowman's hat and raised stick arms do not touch the top edge, his base does not touch the bottom edge, and nothing touches the side edges. Nothing lit appears on the roof, the trim, the window frames or the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the cream stone gable behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the stone texture and the wet road reflections clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
```

---

#### Generated set

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v29_c02_g1.png` | C02 | `07ebb15c-1e14-4ef7-b576-b0f4210e0c5b` | 290201 | completed, first attempt |
| `v29_c03_g1.png` | C03 | `169ef4c8-94f6-48cc-8693-ebf981b6262f` | 290301 | completed, first attempt |
| `v29_c04_g1.png` | C04 | `271193cf-e71e-4035-8a7d-9eb0dd0f53ec` | 290401 | completed, first attempt |
| `v29_c05_g1.png` | C05 | `0f0bd301-46da-449b-a256-fc8baa127215` | 290501 | completed, first attempt |
| `v29_c06_g1.png` | C06 | `63a2e39f-ba00-457e-b1d2-0302fbe6c6e2` | 290601 | completed, first attempt |
| `v29_c07_g1.png` | C07 | `40058517-9846-48c1-88e3-d48519a63b52` | 290701 | completed, first attempt |

All six 1520 × 2688 RGB PNG, downloaded from the result URLs into `starting_frames/`.

---

#### Submission notes

- Workspace **Oneofone1** (`b2c97bd7-fedf-489d-b211-3de4e39dc90a`) — the private workspace is out of credits.
- Every shot submitted as **its own single-item batch**. A partial batch failure can't be retried wholesale, so one shot per call keeps a refusal from costing the rest.
- `medias[].role` for `gpt_image_2` is **`image`**. `medias[].value` accepts either a media UUID or a **prior job id** — that is what makes the continuity chain work.
- C2 → C3 → C4 had to run **in sequence** (each needs the previous job id). C5, C6 and C7 have no chain dependency and were fired in parallel with C2.
- None of the known v28 failure modes fired this run: no `declined_preset_id` resubmission, no "Preset was recommended instead", no `ip_detected`. All six completed on the first attempt.

---

#### Open points for review

- **C4's curtain is mounted but unlit.** That follows the v20 – v28 narrative — C4 is the phone-app beat immediately *before* she presses play, and C5 is the lit payoff. Daniel's brief said "with all the lights set up", which reads as *mounted*; if he meant *glowing*, C4 is the one to re-run.
- **C5 and C7 came out mostly cool/warm white** and thin on colour next to C6. C6 got an explicit "colour is the point" paragraph and C5/C7 did not.
- **C6's house rendered darker than the specified slate-blue**, and its garage door reads brown/wood rather than the intended natural oak with iron strap hinges.

No re-runs were made. One generation per shot, then review.


---

## Regenerations - 2026-09-15

Daniel reviewed the six g1 frames and asked for two changes, with a reference photo attached:

> They camed out good but we need to make some modifications.
> C3 - I want a much closer look and sideway, exactly like this image attached
> C4 - It's good but I want a much closer look, kinda like in C3, even a little more closer

The attached photo showed a woman on a black step stool mounting a black LED curtain to a wall, shot close and at an oblique side angle. It was uploaded to Higgsfield as media `9894c57e-8d7f-4754-9b39-357f18277863`.

This **overrides** the original C03 direction, which had insisted on a flat frontal camera with "NO strong oblique perspective, NO wide-angle corner view". C04 keeps its frontal angle but is pulled right in.

### C03 g2 - close, side-on install

References attached, in order:

| # | What it owns | Value |
|---|---|---|
| 1 | Camera position, angle, height, closeness, her pose - **and nothing else** | media `9894c57e-8d7f-4754-9b39-357f18277863` (Daniel's photo) |
| 2 | The house, the woman, the wardrobe, the garage door | job `169ef4c8-94f6-48cc-8693-ebf981b6262f` (C03 g1) |

Because the reference photo carries a completely different house and a completely different woman, the prompt needed an explicit **DO NOT COPY** list to stop the slate-blue board-and-batten siding, the shingled neighbour, the brick wall, the hedge, the mustard jacket, the dark curly hair, the black trousers and the white boots bleeding across. This is the "attach the frame that owns the geometry" rule with the geometry and the look split across two refs.

Prompt as submitted - 688 words:

```
COPY THE CAMERA OF THE FIRST ATTACHED IMAGE EXACTLY - its position, its angle, its height, its closeness and her pose. This is a CLOSE, SIDE-ON shot, not the wide frontal shot.

THE CAMERA IS CLOSE AND OFF TO ONE SIDE, exactly as in the first image: the camera stands near the wall and slightly behind her at roughly waist height, looking ALONG the wall, so the wall runs away from the camera DIAGONALLY - nearest at the bottom-left of the frame and receding to the right, the roof gutter line along the top sloping down towards the right as it goes away, strong oblique one-point perspective. She fills most of the frame height in the right half, her whole body in shot from her boots on the stool up to her raised hands. MUCH CLOSER than a full-house shot: only a short run of the wall is in frame, no full facade, no wide establishing view, no flat square-on frontal view.

HER POSE - copy it from the first image: she stands on a small BLACK two-step folding step stool, seen from BEHIND and slightly to the side, facing the wall, both arms raised in front of her, her hands up at the trim board along the top of the wall as she presses the LED curtain into place. Her weight is on one foot, her back slightly arched.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Long vertical strands of thin BLACK cord with small DARK unlit bulbs hang down the wall to the left of her, and because the camera is close the strands are big in the frame and clearly readable as separate cords. A BIG LOOSE TANGLE of BLACK cord is heaped on the snow at the foot of the stool, spilling out to the left - a real messy nest of wire, obviously dark against the white snow, exactly like the bundle in the first image. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE HOUSE AND THE WOMAN - TAKE THEM FROM THE SECOND ATTACHED IMAGE, NOT FROM THE FIRST. It must read as LITERALLY THE SAME HOUSE and the SAME WOMAN as the second image, now seen close up from the side. The wall she is working on is the WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR of that house - soft WHITE with horizontal panel seams and recessed rectangular panels running away in perspective, and the row of small square windows across the top of the door visible at the far end. Around it the same WARM SAND-BEIGE lap siding with crisp WHITE trim, the same BLACK COACH LANTERN on the wall, the same WHITE gutter and WHITE downpipe, the same plain CONCRETE driveway under patchy snow. At the RIGHT of the frame, further away, the corner where the garage wing meets the MAIN HOUSE BODY is visible - the two-storey wall, the covered porch on white posts and the DARK RED front door - so it still reads as ONE house with the garage built into it. Same late-twenties woman with fair skin and COPPER-RED hair in a high ponytail spilling out from under a cream beanie, BURGUNDY puffer jacket, dark blue jeans, tan boots.

DO NOT COPY FROM THE FIRST IMAGE: not the dark slate-blue board-and-batten siding, not the shingled neighbouring house, not the brick wall, not the hedge, not her mustard-yellow jacket, not her dark curly hair, not her black trousers and not her white boots. The first image is there ONLY for the camera, the distance, the angle and the pose.

Daytime, overcast winter light, snow on the ground.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the door panels, the quilting of her jacket and every strand of black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### C04 g2 - same frontal angle, much tighter

References attached, in order:

| # | What it owns | Value |
|---|---|---|
| 1 | The phone, the hand, the grip, the app screen, the night house | job `271193cf-e71e-4035-8a7d-9eb0dd0f53ec` (C04 g1) |
| 2 | The closeness only - explicitly **not** the side angle | job `46b340e4-6caf-44c9-aa30-cc219dfe59a6` (C03 g2) |

The risk here was that attaching C03 g2 for closeness would drag its oblique receding perspective along with it, so the prompt names that trap directly: "STILL SHOT FROM THE FRONT, not from the side ... take only the CLOSENESS from the second image, not its side angle." The approved-iPhone block and the app-screen block are carried over verbatim from C04 g1 so the handset does not drift.

Prompt as submitted - 824 words:

```
Same shot as the FIRST attached image - same night, same house, same phone held up in the bottom-centre foreground, same app on the screen. ONE THING CHANGES: THE CAMERA IS MUCH, MUCH CLOSER.

THE NEW FRAMING - THIS IS THE WHOLE POINT: step right up to the house, close enough that the SECOND attached image's distance is the reference. Even a little CLOSER than the second image. The WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR with the LED curtain hanging down it FILLS THE FRAME - the curtain strands and the door panels run from the top of the frame to the bottom and from edge to edge. We are near enough to read every panel seam, every recessed panel and every individual bulb on the cord. NO full facade, NO whole house, NO roofline, NO establishing shot, NO wide view from the end of the driveway. Only the garage bay and a narrow sliver of what is immediately beside it is in frame.

STILL SHOT FROM THE FRONT, not from the side: the garage door faces the camera square-on and flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. Do not turn it away at an angle and do not use the oblique receding perspective of the second image - take only the CLOSENESS from the second image, not its side angle.

WHAT STAYS IN FRAME AROUND THE DOOR: just the edge of the WARM SAND-BEIGE lap siding and the WHITE trim down one side, ONE BLACK COACH LANTERN glowing warm beside the door, and at the far right edge a small slice of the covered porch with its white post and the DARK RED front door, cropped by the frame. The concrete driveway with patchy snow across the very bottom.

THE PHONE - COPY IT EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same hand, same grip, same angle, held up big in the bottom-centre foreground. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

THE SCREEN SHOWS THE SAME APP as the first image: a dark navy-blue app screen filled with a neat grid of small square scene thumbnails, each one a tiny colourful Christmas light picture on a dark background, one of them ringed with a bright highlight, and a BIG ROUND BLUE PLAY BUTTON centred near the bottom of the screen. The screen glows and throws its light up onto the fingers and the palm. NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is just the grid of thumbnails and the round play button.

THE LED CURTAIN IS FULLY MOUNTED AND IT IS BLACK - CRITICAL: it hangs from the trim board above the garage door in evenly spaced vertical see-through strands, down across the full width of the door, with slight natural sag and an uneven bottom hem. The wire is BLACK, not white and not clear, every strand a thin BLACK cord with small DARK unlit bulbs on it, no glow. Against the white door the strands read as clear thin dark vertical lines, and at this close range each strand is thick and obvious in the frame. No white wire, no clear wire, no silver wire anywhere.

THE HOUSE MUST BE THE SAME HOUSE as both attached images - same warm sand-beige lap siding, same white trim, same soft white sectional door with its recessed panels and its row of small square windows across the top, same black coach lantern, same white gutter, same concrete driveway.

Lighting: night, the coach lantern glowing warm beside the door, a street lamp glow spilling in from one side, snow on the driveway catching the light, the phone screen the brightest thing in the foreground.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the garage door behind it equally in focus, the panel seams and the black cord clearly readable, correct exposure with no blown-out highlight around the lantern and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set - regens

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v29_c03_g1.png` | C03 | `46b340e4-6caf-44c9-aa30-cc219dfe59a6` | 290302 | completed, first attempt |
| `v29_c04_g2.png` | C04 | `74f96513-1d68-4eaa-9df1-a61c1942df84` | 290402 | completed, first attempt |

Both 1520 x 2688 RGB PNG, `gpt_image_2`, 9:16, 2k, quality `medium`, `count 1`, workspace **Oneofone1**. One generation each, no re-rolls. The g1 files are kept alongside - nothing was overwritten.

### What came out

**C03 g2 is on target.** Close side-on view, the white sectional garage door with its square windows receding to the right, the same copper-ponytail woman in cream beanie / burgundy puffer / tan boots up on a black step stool with both arms raised, a big black cord tangle heaped on the snow at her feet, and the porch with white posts and the dark red door still readable at the right so the garage still reads as built into the house. None of the do-not-copy elements came through.

**C04 g2 is much tighter and frontal as asked** - the garage door and curtain fill the frame, the coach lantern glows at the right, a sliver of the dark front door and porch is cropped at the right edge, and the iPhone sits big in the bottom-centre with the navy thumbnail grid and the round blue play button.

Two things to flag on C04 g2, not re-rolled:

- The **curtain wire reads pale / white against the white door** rather than black, despite the black-wire block being stated twice. Low contrast between a black cord and a white door at this range is a hard ask for the model.
- The **siding reads cream / white** rather than the established warm sand-beige, so it is a shade off the C05 - C07 house.

Both are one-line fixes on a re-run if Daniel wants them.


---

## C04 g3 - 2026-09-15

Daniel reviewed C04 g2:

> C4 - It's too close, the entire garage door must be visible. Also I want a better app ui, more clear.

Two changes only: step the camera back until the **whole** garage door fits in frame, and redraw the app screen so it reads cleanly.

References attached, in order:

| # | What it owns | Value |
|---|---|---|
| 1 | The base plate - night, square-on frontal angle, the house, the phone's position and size | job `74f96513-1d68-4eaa-9df1-a61c1942df84` (C04 g2) |
| 2 | The approved iPhone hardware and the hand | job `271193cf-e71e-4035-8a7d-9eb0dd0f53ec` (C04 g1) |

The framing had to be pinned by what is *inside* the frame rather than by a distance, because "a bit wider" is not something the model can measure: both vertical door edges with siding beyond them, the complete top window row, and the bottom edge meeting the driveway - with an explicit ceiling on how far back to go (still no full facade, no roofline, no driveway-end establishing shot).

The app screen was respecified from scratch: a fixed **3 x 3 grid of nine large tiles** with named colours, generous gutters, rounded corners, one tile ringed in electric blue, and a big round solid blue play button with a **white triangle** in it. g1 and g2 both asked only for "a neat grid of small square scene thumbnails", which the model rendered as illegible mush. The no-text rule is unchanged.

Two corrections were also folded in, calling out the g2 output by name so the model knew what to fix: the curtain wire, which read pale against the white door despite the black-wire block, and the siding, which drifted to cream.

Prompt as submitted - 1126 words:

```
Same shot as the FIRST attached image - same night, same house, same square-on frontal angle, same phone held up big in the bottom-centre foreground. TWO THINGS CHANGE: the camera steps back a little, and the app on the screen is drawn much more clearly.

CHANGE 1 - THE ENTIRE GARAGE DOOR MUST BE VISIBLE. The first image is cropped too tight and cuts the door off. Step the camera BACK just far enough that the WHOLE double garage door fits inside the frame with a little breathing room around it: BOTH vertical side edges of the door are inside the frame with siding visible beyond them on each side, the COMPLETE top edge of the door is in frame including the entire row of small square windows running all the way across it, and the BOTTOM edge where the door meets the concrete driveway is in frame too. Nothing about the door is cut off by any edge of the picture. Step back ONLY this far - this is still a CLOSE shot of the garage bay, MUCH closer than a full-facade view: NO whole house, NO full two-storey facade, NO roofline, NO establishing shot from the end of the driveway. The garage door is still the dominant object and fills most of the frame.

STILL SHOT SQUARE-ON FROM THE FRONT: the garage door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low worm's-eye tilt.

WHAT IS AROUND THE DOOR: a strip of WARM SAND-BEIGE lap siding with crisp WHITE trim down each side of the door and a band of it above - the siding is a clear WARM SANDY BEIGE, NOT white, NOT cream, NOT grey, and it must read visibly warmer and darker than the soft white of the garage door so the two are obviously different colours. ONE BLACK COACH LANTERN glowing warm on the siding beside the door. At the far right edge a small slice of the covered porch with its white post and the DARK RED front door, cropped by the frame. The concrete driveway with patchy snow across the bottom.

CHANGE 2 - THE APP SCREEN, DRAWN MUCH MORE CLEARLY AND CLEANLY. Same app idea as both attached images but rendered sharp, bold and easy to read at a glance instead of a mushy grid of tiny tiles. The screen is a deep NAVY-BLUE app background. On it: a neat grid of exactly NINE large square scene tiles, three across and three down, generously spaced apart with clear dark gutters between them and soft rounded corners on every tile. Each tile is a small crisp picture of a differently coloured Christmas light pattern on a dark background - one warm white, one red-and-green, one icy blue, one multicolour, one purple-and-pink, and so on - each one a distinct saturated colour so the grid reads as a colourful, clearly organised palette of scenes. ONE tile is selected and is ringed with a bright, obvious 3-pixel electric-blue border and a soft glow. Below the grid, centred, a BIG ROUND SOLID BRIGHT-BLUE PLAY BUTTON, large and unmistakable, with a clean WHITE TRIANGLE pointing right in the middle of it, crisp edges, no blur. Above the grid a simple empty header bar. EVERY element on the screen is tack-sharp, high contrast and cleanly separated - no mush, no smearing, no tiny illegible clutter. ABSOLUTELY NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is only the header bar, the nine picture tiles and the round play button. The screen glows and throws its light up onto the fingers and the palm.

THE PHONE - COPY IT EXACTLY FROM THE SECOND ATTACHED IMAGE. Same handset, same hand, same grip, same angle, held up big in the bottom-centre foreground, roughly the same size in frame as in the first image. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK - CRITICAL, AND THE FIRST IMAGE GETS THIS WRONG. In the first image the strands came out pale and washed out against the white door. They must be BLACK. The curtain hangs from the trim board above the garage door in evenly spaced vertical see-through strands, right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the soft white garage door each strand must read as a CLEARLY DARK, high-contrast vertical line, obviously black, easy to trace from top to bottom. NO white wire, NO clear wire, NO silver wire, NO pale grey wire anywhere. There are clear gaps between the strands and the door panels are plainly visible through them - it is a hanging curtain of separate strands, never a solid panel or a mesh screen.

THE HOUSE MUST BE THE SAME HOUSE as both attached images - same warm sand-beige lap siding, same white trim, same soft white sectional door with its recessed panels and its row of small square windows across the top, same black coach lantern, same white gutter, same concrete driveway.

Lighting: night, the coach lantern glowing warm beside the door, a street lamp glow spilling in from one side, snow on the driveway catching the light, the phone screen the brightest thing in the foreground.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lantern and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set - C04 g3

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v29_c04_g3.png` | C04 | `7da86a25-4fc3-4f5a-b61c-17d596c8f6ac` | 290403 | completed, first attempt |

1520 x 2688 RGB PNG, `gpt_image_2`, 9:16, 2k, quality `medium`, `count 1`, workspace **Oneofone1**. One generation, no re-rolls. `v29_c04_g1.png` and `v29_c04_g2.png` are both kept.

### What came out

The framing is right: the entire door is inside the frame - both side edges with trim and siding beyond them, the full row of square windows across the top, and the bottom edge meeting the snowy driveway - and it is still clearly a close shot of the garage bay, not a facade shot. The app UI is the big win: nine cleanly separated tiles in distinct colours, one ringed in blue, and a large solid blue play button with a crisp white triangle.

Still off, not re-rolled:

- **The siding is still cream / off-white**, not the warm sand-beige of C05 - C07. Two prompts in a row have failed to move it, so the next attempt should probably lead with the siding colour rather than bury it mid-prompt, or chain off a C05 - C07 job for the house instead.
- **Two coach lanterns rendered instead of one**, one either side of the door. Harmless and it matches the C04 g1 house, but it is not what this prompt asked for.
- **The strands are dark but thin** - readable, though not as heavy and obviously black as specified.


---

## C04 g4 - 2026-09-15

Daniel reviewed C04 g3:

> The angle looks right now, just keep the old phone app ui, just make it more sharper, clearer

So the g3 framing is locked and the nine-tile redesign is reverted. The original dense-thumbnail app layout comes back, rendered properly this time. The redesign was the wrong read of "better UI" - Daniel wanted the same UI drawn well, not a different UI.

References attached, in order:

| # | What it owns | Value |
|---|---|---|
| 1 | Everything except the screen - camera, framing, distance, angle, lighting, house, phone position and size | job `7da86a25-4fc3-4f5a-b61c-17d596c8f6ac` (C04 g3) |
| 2 | The app layout to restore - the dense grid of small thumbnails and the round play button | job `271193cf-e71e-4035-8a7d-9eb0dd0f53ec` (C04 g1) |

Two traps to avoid here. First, re-attaching g1 for the app risks dragging its wide full-facade framing back in, so the prompt opens by locking the g3 framing in full and spells out the whole-door-in-frame test again before it ever mentions the screen. Second, "put back the old UI" on its own would just reproduce the mush, so the layout instruction (same dense packing, same small thumbnails, same proportions) is kept separate from the quality instruction (crisp edges, even gutters, aligned rows, distinct saturated colours, a clean electric-blue selection ring, a solid blue disc with a white triangle, no moire).

Prompt as submitted - 944 words:

```
Same shot as the FIRST attached image. Copy its camera, its framing, its distance, its angle, its lighting, its house and the position and size of the phone in the foreground EXACTLY. ONE THING CHANGES: the app on the phone screen goes back to the design in the SECOND attached image, just drawn much sharper.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. Square-on frontal view of the double garage door at night, the camera close to the house so the garage bay dominates the frame, and the ENTIRE garage door inside the picture with a little breathing room around it: both vertical side edges of the door in frame with white trim and siding visible beyond them on each side, the complete top edge in frame including the whole row of small square windows running across it, and the bottom edge where the door meets the concrete driveway in frame too. Nothing about the door cut off by any edge. Do NOT step closer and do NOT step further back. NO whole house, NO full two-storey facade, NO roofline, NO establishing shot from the end of the driveway. The door faces the camera flat, its horizontal panel seams dead level and its vertical edges straight up and down - NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up.

Everything around the door stays exactly as in the first image: the lap siding and white trim either side of the door, the black coach lanterns glowing warm on the wall, the sliver of the covered porch and dark front door cropped at the right edge, the concrete driveway with patchy snow across the bottom, the night sky, the same warm lantern light and street-lamp spill.

THE ONE CHANGE - THE APP SCREEN. Discard the nine big square tiles on the phone in the first image. Instead put back the app design from the SECOND attached image, exactly that layout: a dark NAVY-BLUE app screen filled with a DENSE grid of MANY SMALL square scene thumbnails packed close together in even rows and columns, each thumbnail a tiny picture of a differently coloured Christmas light pattern on a dark background, ONE of them ringed with a bright highlight border, and a BIG ROUND BLUE PLAY BUTTON centred near the bottom of the screen below the grid. Same number of thumbnails, same small size, same dense packing, same overall layout and proportions as the second image.

RENDER THAT SCREEN MUCH SHARPER AND CLEANER THAN THE SECOND IMAGE - this is the whole point of the change. Every thumbnail has crisp clean edges and neat even gutters between it and its neighbours, perfectly aligned rows and columns, and a clearly readable little light pattern inside it in a distinct saturated colour. The highlighted thumbnail's ring is a clean bright electric-blue outline, not a smear. The round play button is a solid, evenly circular bright blue disc with a clean WHITE TRIANGLE pointing right in the middle of it, crisp edges. The screen is in perfect focus, high contrast, no mush, no smearing, no blur, no moire, no warped or melted tiles. ABSOLUTELY NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is only the grid of picture thumbnails and the round play button. The screen glows and throws its light up onto the fingers and the palm.

THE PHONE ITSELF IS UNCHANGED - same handset, same hand, same grip, same angle, same size and position in the bottom-centre foreground as in the first image. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the garage door in evenly spaced vertical see-through strands, right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale garage door each strand must read as a clearly dark, high-contrast vertical line, obviously black and easy to trace from top to bottom. NO white wire, NO clear wire, NO silver wire, NO pale grey wire anywhere. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set - C04 g4

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v29_c04_g4.png` | C04 | `47ab5ef5-d6af-455c-b06c-fba3cc3025de` | 290404 | completed, first attempt |

1520 x 2688 RGB PNG, `gpt_image_2`, 9:16, 2k, quality `medium`, `count 1`, workspace **Oneofone1**. One generation, no re-rolls. g1, g2 and g3 are all kept.

### What came out

The g3 framing survived intact - square-on, the whole garage door in frame with its full window row and both side edges, still a close garage-bay shot. The screen is the original dense layout again: many small square thumbnails packed in even rows and columns, each carrying a small readable light motif in a distinct saturated colour, one ringed in bright electric blue, and the big round blue play button with a clean white triangle below the grid. It is noticeably sharper and better aligned than g1 and g2.

The siding is still reading cream rather than warm sand-beige, and there are still two coach lanterns rather than one. Both carried over from g3 by design - the prompt deliberately told it not to change anything outside the screen.


---

## C04 g5 - 2026-09-15

Daniel reviewed C04 g4:

> It's not the same ui as the older one, this one has a lot more pannels

Correct. I had described the g1 / g2 screen from memory as "a DENSE grid of MANY SMALL square scene thumbnails", and the model did exactly that - five or six columns of tiny glyphs. Cropping into the g1 and g2 phones and actually looking settled it: **the original UI is a TWO-COLUMN grid of large photographic tiles**, roughly five rows, each tile nearly half the screen wide and carrying a real photo of a lit house, a nativity, a snowman or a reindeer, mostly icy blue and white, with the round blue play button below the grid.

Lesson worth keeping: when a reference detail is small in the frame, crop into it and look before writing the prompt. Describing it from the thumbnail produced two wasted generations.

References attached, in order:

| # | What it owns | Value |
|---|---|---|
| 1 | Everything except the screen - camera, framing, distance, angle, lighting, house, curtain, phone position and grip | job `47ab5ef5-d6af-455c-b06c-fba3cc3025de` (C04 g4) |
| 2 | The app screen layout only - the two-column grid of big photographic tiles | job `74f96513-1d68-4eaa-9df1-a61c1942df84` (C04 g2) |

g2 carries the rejected too-close framing, so the prompt locks the g4 framing in full first and then says outright: "Ignore the framing of the SECOND attached image completely - it is cropped too tight and it is here ONLY for its phone screen."

The layout is also pinned numerically rather than adjectivally - two columns, about five rows, roughly ten tiles and no more, each nearly half the screen wide - with an explicit ban on three, four, five or six columns and on any glyph or app-icon look. "Fewer, bigger panels" on its own is not something the model can count.

Prompt as submitted - 952 words:

```
Same shot as the FIRST attached image. Copy its camera, its framing, its distance, its angle, its lighting, its house, its garage door, its curtain and the position, size and grip of the phone in the foreground EXACTLY. ONE THING CHANGES: the layout of the app on the phone screen.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. Square-on frontal view of the double garage door at night, the camera close to the house so the garage bay dominates the frame, and the ENTIRE garage door inside the picture with a little breathing room around it: both vertical side edges of the door in frame with white trim and siding visible beyond them on each side, the complete top edge in frame including the whole row of small square windows running across it, and the bottom edge where the door meets the concrete driveway in frame too. Nothing about the door cut off by any edge. Do NOT step closer and do NOT step further back. NO whole house, NO full two-storey facade, NO roofline, NO establishing shot from the end of the driveway. The door faces the camera flat, its horizontal panel seams dead level and its vertical edges straight up and down - NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up. Ignore the framing of the SECOND attached image completely - it is cropped too tight and it is here ONLY for its phone screen.

Everything around the door stays exactly as in the first image: the lap siding and white trim either side of the door, the black coach lanterns glowing warm on the wall, the sliver of the covered porch and dark front door cropped at the right edge, the concrete driveway with patchy snow across the bottom, the night sky, the same warm lantern light and street-lamp spill. The LED curtain stays fully mounted, hanging in evenly spaced vertical see-through BLACK strands with small dark unlit bulbs across the full width of the door, lights OFF, the door panels plainly visible through the gaps between strands.

THE ONE CHANGE - THE APP SCREEN LAYOUT. The first image has far too many panels: a dense grid of many tiny icons crammed across the screen. That is WRONG. Use the layout of the SECOND attached image's screen instead, which has FEWER and MUCH BIGGER panels.

EXACTLY WHAT THE SCREEN MUST SHOW: a dark navy-blue app screen carrying a grid of just TWO COLUMNS of large tiles - two tiles across the width of the screen, about five tiles down, so roughly TEN tiles in total and no more. Each tile is BIG - nearly half the width of the screen - with softly rounded corners and only a narrow gutter between it and its neighbour. Each tile is a small PHOTOGRAPH of a real house decorated in Christmas lights: a snow-covered roofline picked out in icy white and blue lights, a lit nativity scene, a glowing snowman, a reindeer outline in lights, a porch draped in blue and white light curtains. The palette across the grid is mostly ICY BLUE and cool WHITE with a couple of warm amber and red-green tiles mixed in. ONE tile is selected and is ringed with a bright electric-blue outline. Near the BOTTOM of the screen, below the grid, sits a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE pointing right in the middle of it.

ABSOLUTELY NOT on the screen: no dense grid of tiny icons, no three, four, five or six columns, no rows of little symbols or pictograms, no snowflake or Christmas-tree glyphs, no app-icon look. Only TWO COLUMNS of big photographic tiles. And NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

RENDER THAT SCREEN TACK-SHARP: crisp clean tile edges, perfectly aligned columns and rows, each photograph inside its tile clearly readable, the selection ring a clean bright outline and the play button a solid even circle with a crisp white triangle. In perfect focus, high contrast, no mush, no smearing, no blur, no moire, no warped or melted tiles. The screen glows and throws its light up onto the fingers and the palm, and it is the brightest thing in the foreground.

THE PHONE ITSELF IS UNCHANGED - same handset, same hand, same grip, same angle, same size and position in the bottom-centre foreground as in the first image. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set - C04 g5

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v29_c04_g5.png` | C04 | `da8d1a05-5120-4508-96dc-c55f9c491d16` | 290405 | completed, first attempt |

1520 x 2688 RGB PNG, `gpt_image_2`, 9:16, 2k, quality `medium`, `count 1`, workspace **Oneofone1**. One generation, no re-rolls. g1 - g4 all kept.

### What came out

The screen is right: two columns of large tiles, five rows, each one a readable icy-blue scene - a lit house, a nativity, a reindeer, a snowman, a decorated porch - one ringed in bright blue, and the round blue play button with a white triangle sitting below the grid. It matches the g1 / g2 layout and it is far sharper than either.

The g4 framing survived untouched - square-on, whole garage door in frame with its full window row and both side edges, curtain mounted and unlit.

Still carried over and deliberately untouched: the siding reads cream rather than warm sand-beige, and there are two coach lanterns rather than one.

## C04 g6 - 2026-09-15

Daniel reviewed C04 g5:

> Now it's good, But in C3 the garage door looks bigger, so I think you need to make it bigger in C4 too

The app screen and the angle are settled - the only note is scale. C03 is a close side-on install shot where the wall fills the picture; next to it the g5 garage door sits small with a lot of dead driveway and siding around it. So this take changes nothing but the camera distance.

References attached, in order:

| # | What it owns | Value |
|---|---|---|
| 1 | Everything - camera angle, house, door, curtain, lighting, phone and its approved app screen | job `da8d1a05-5120-4508-96dc-c55f9c491d16` (C04 g5) |

One reference on purpose. g5 is the first C04 take where framing, angle and screen are all approved at once, so there is nothing left to borrow from another frame - and attaching a second image would only give a rejected framing or the daytime side-on C03 a way back in.

The push-in is bounded by a **test**, not by a distance. "Make it bigger" is not something the model can act on, and "step forward two feet" means nothing to it either. So the prompt states the target as what sits inside the frame - the door spanning almost the full width with only a narrow strip of trim and siding beyond each side edge, a shallow band of siding above, a low strip of driveway below - and then states the hard limit as the thing that must survive: both side edges in frame, the whole row of small square windows visible end to end, the bottom edge where the door meets the concrete in frame. "Push in exactly as far as that allows and no further."

The phone is the other risk. Pushing the camera toward the house would normally change the foreground too, so the prompt says outright that the handset must neither shrink nor grow, and restates the full two-column app-grid spec rather than trusting "unchanged" to carry it.

Prompt as submitted - 934 words:

```
Same shot as the attached image - same night, same house, same square-on frontal angle, same garage door, same curtain, same lanterns, same phone, same hand, same app screen. ONE THING CHANGES: THE GARAGE DOOR IS BIGGER IN THE FRAME.

THE CHANGE - PUSH IN SO THE GARAGE DOOR IS MUCH BIGGER. In the attached image the door sits too small with too much empty space around it. Move the camera closer to the house so the door grows to fill the picture: the door must now span almost the FULL WIDTH of the frame, with only a NARROW STRIP of white trim and siding left visible beyond its left edge and beyond its right edge, and only a SHALLOW BAND of siding above its top edge. Cut down the empty driveway at the bottom so only a low strip of snowy concrete remains under the door. The garage door should be by far the dominant object in the picture, big and imposing, reading at the same large scale as the wall does in the daytime install shot.

BUT THE ENTIRE DOOR MUST STILL BE VISIBLE - THIS IS THE LIMIT ON HOW FAR TO PUSH IN. Both vertical side edges of the door stay inside the frame with that narrow strip of trim and siding beyond each one. The complete top edge stays inside the frame, including the WHOLE row of small square windows running all the way across it, every window visible end to end. The bottom edge where the door meets the concrete driveway stays inside the frame. Nothing about the door is cut off by any edge of the picture. Push in exactly as far as that allows and no further.

STILL SQUARE-ON FROM THE FRONT: the door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up, NO whole house, NO full facade, NO roofline.

EVERYTHING ELSE IS UNCHANGED from the attached image. The same warm-lit lap siding and white trim around the door, the same black coach lanterns glowing warm on the wall either side, the sliver of covered porch and dark front door cropped at the right edge, the snowy concrete driveway, the night sky, the same warm lantern light and street-lamp spill.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the door in evenly spaced vertical see-through strands right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale door each strand reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen. At this closer range the strands and the bulbs are bigger and even easier to read.

THE PHONE AND ITS SCREEN ARE UNCHANGED - COPY THEM EXACTLY FROM THE ATTACHED IMAGE. Same handset, same hand, same grip, same angle, same size and same position in the bottom-centre foreground. Pushing the camera in must NOT shrink the phone and must NOT enlarge it. The screen shows the SAME app: a dark navy-blue screen with a grid of just TWO COLUMNS of large tiles, two across and about five down, roughly ten tiles in total and no more, each tile nearly half the screen wide with softly rounded corners and a narrow gutter, each one a small photograph of a house decorated in Christmas lights - a lit roofline, a nativity, a snowman, a reindeer, a porch draped in light curtains - mostly icy blue and cool white with a couple of warm tiles, ONE tile ringed with a bright electric-blue outline, and a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE below the grid. NOT a dense grid of tiny icons, NOT three or more columns, NO glyphs or pictograms, and NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

The phone is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set - C04 g6

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v29_c04_g1.png` | C04 | `a6bcff66-91f5-4629-be28-3ba99b78c3a7` | 290406 | completed, first attempt |

1520 x 2688 RGB PNG, `gpt_image_2`, 9:16, 2k, quality `medium`, `count 1`, workspace **Oneofone1**. One generation, no re-rolls. g1 - g5 all kept.

### What came out

The door is much larger and now dominates the frame, spanning nearly its full width with only a narrow strip of white trim and siding beyond each side edge and a shallow band above. The whole row of small square windows is visible end to end, both vertical edges are inside the picture, and the bottom edge meeting the snowy driveway is in frame - the push-in stopped where it was supposed to. The driveway is cut back to a low strip.

The phone survived the push-in at the same size and position, and its screen still carries the approved two-column grid - lit house, nativity, reindeer, snowman in icy blue, one tile ringed, round blue play button with a white triangle below the grid.

Curtain still reads as separate black see-through strands across the full width of the door, unlit, panels visible through the gaps - and at this closer range the cords are easier to trace.

Still carried over and deliberately untouched: the siding reads cream rather than warm sand-beige, and there are two coach lanterns rather than one. Both have now resisted three explicit prompts. If they matter, the fix is probably to chain a C04 take off one of the C05 - C07 jobs so the house itself comes in as a reference, rather than describing the colour again.

---

## C01 — HOOK — doorbell camera, courier carrying a stack of boxes

**Frame:** `starting_frames/v29_c01_g1.png` (1520 x 2688)
**Job id:** `2fdc74d9-a1d0-4380-b04a-bfb2b7c58410`
**Model:** gpt_image_2 · 2k · quality medium · 9:16 · 1 generation
**References:** ref 1 = Daniel's doorbell-cam courier screenshot (`7e07b8cb-69b5-4076-bf41-412c058391a1`) — camera, lens, composition, location. ref 2 = approved packshot `product_images/box_nowindow/box_nowindow_g5.png` (`2812fa88-3367-4746-a761-4e99c42b73d1`) — the box.

**Prompt**

Reproduce the FIRST attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a FRONT-DOOR DOORBELL CAMERA. Keep the same suburban American street, the same bright winter afternoon, the same mood.

THE CAMERA - copy it from the first image: a doorbell camera fixed to the wall beside a front door, about 1.2 metres off the ground, looking straight out across the porch and the front lawn toward the street. Very wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Slightly low, flat, static, unmanned viewpoint - NOT a handheld phone shot, NOT a cinematic camera.

EVERYTHING BELOW STAYS AS IN THE FIRST IMAGE, just re-stacked for a vertical frame:
- RIGHT EDGE: a RED BRICK porch pillar in extreme close foreground, very near the lens, filling a tall vertical band down the whole right side of the frame, its brick and mortar texture large and soft, a pale cast-stone cap at the top. It frames the shot like a curtain.
- LEFT EDGE: the corner of the house in white lap siding, running away from the camera, and below it a low RED BRICK porch wall along the bottom-left with a green pine garland and a few red baubles laid along its top.
- CENTRE: a pale CONCRETE WALKWAY running from the bottom of the frame away from the porch, out across the lawn to the driveway. Neat winter grass either side, a bare flowerbed at the bottom left with a red-and-white candy-cane stake pushed into the soil.
- MIDDLE DISTANCE: a concrete driveway with a white SUV and a dark grey car parked nose-in, a pavement, then the street.
- BACKGROUND: the row of houses on the opposite side of the street - beige and grey two-storey homes with white double garage doors, a red car sitting in one of the driveways, leafless winter trees, a green lawn.
- SKY: a big clean blue winter sky with bright white cumulus clouds, filling the upper part of the vertical frame.

THE ONE CHANGE - THE COURIER AND WHAT HE IS CARRYING. In the middle ground, on the walkway where the delivery man stands in the first image, a DELIVERY COURIER is walking toward the front door - a man in a plain RED delivery polo shirt and dark grey work trousers with black trainers, no company logo of any kind, caught mid-stride in profile with one leg forward, leaning back slightly under the weight. He is a whole figure, medium-sized in the frame, roughly the height of the walkway width, clearly readable but not close up.

HE IS CARRYING A BIG STACK OF THE PRODUCT BOXES FROM THE SECOND ATTACHED IMAGE - FIVE of them, and they must be copied exactly from that second image: flat MATTE BLACK rigid retail boxes, on the front a large white condensed uppercase headline, a warm gold subline under it, a small red diagonal ribbon flag in the top-right corner, one large photographic panel with a thin gold hairline border filling the middle and lower two thirds showing a night photo of a suburban house facade lit with Christmas lights, and a bottom row of five small gold line icons. Closed and sealed - NO transparent window, NO clear plastic panel, NO cutout, nothing visible inside.

THE STACK: the five boxes are stacked one on top of another and hugged against his chest with both arms wrapped underneath and around them, tilted back against his body so the PRINTED BLACK FRONT FACE of the nearest box is angled toward the camera and clearly readable, the other four stacked behind it with their black edges visible. Each box is WIDE - about 55 cm across, wider than his own shoulders - so the stack sticks out well past both sides of his body and the top of it reaches his chin and he is peering over the corner of it. Real weight: his arms strain, his back leans back, the stack sags slightly to one side. Every box is the same matte black box - NOT brown cardboard, NOT red, NOT green, NOT white, NOT generic parcels, NOT patterned Christmas packaging.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour doorbell-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork, in the print on the boxes and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun coming in from the left, bright but properly exposed - no blown-out white in the sky or on the concrete, no crushed black in the porch shadow, correct white balance, real contact shadows on the ground. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos on his shirt or on the vehicles. Not a render, not an illustration, no cinematic colour grading.

**Open point:** the stack came out carried side-on and reads smaller than the ~55 cm spec — the boxes are legible but not the "wider than his shoulders" scale. If Daniel wants the scale, regenerate with the stack turned face-on to the camera and the courier brought a step closer.


---

## C04 revision — 2026-09-16

Daniel's brief, given first for videos 30 and 31, then extended: *"They are looking weird, like it's a different garage but we will keep them as are, do the same for video 29."*

> C4 - I just want denser led lines on the garages
>
> Also when we try to animate this shot most of the times it's completly going wrong [...] Let's create an intermediate image with the animation that we will add as reference alongside with the starting frame when we generate the clip. Here is how it should look: exact same framing, hand and phone out of the frame, camera just a little upper (because it's a held iphone shot and the person filming tilts up the camera a little bit so the focus it's on animation), and an animation on the leds like the one in C7 in terms of how it looks, but different animation, the animation must be visible on the entire garage door

Two new frames for this shot. **`v29_c04_g5.png` replaces `v29_c04_g1.png` as the start frame.**

Scene delegated — *"be creative, it must be something funny"* — one unique scene per video, so v29 gets a different gag from v30 (conga line) and v31 (snowball fight). Density: **roughly double**.

### Why the second image exists

C04 is the shot that keeps breaking in animation, and the break is always on the garage door — the model has to invent the lit artwork from nothing while also holding the phone, the hand and the door geometry, and it invents something different every attempt. So the lit end state is now **generated as a still first** and passed to the video model as a second reference. At clip time both images go in: `v29_c04_g5.png` is the **start frame**, `v29_c04_r1.png` is the **second reference** — the target the lights resolve to. The clip is then only a lights-on transition plus the small handheld tilt up, not an invention.

The animation frame is deliberately **not** a valid start frame on its own: the hand and phone are gone and the camera has tilted up, because that is where the shot ends, not where it begins.

### What changed in the prompt for v29

v30 and v31 came back reading as a *different garage* — the C7 style reference bled its own house in, and the frame drifted slightly wider. Daniel accepted those two as-is, so the fix lives only in v29's prompt. Three additions, all up front:

- **"THE HOUSE IS NOT ALLOWED TO CHANGE - THIS IS THE MOST IMPORTANT INSTRUCTION"** — names the pale cream lap siding, the soft white sectional door, the row of small square windows in the **same four groups of four**, the two black coach lanterns, the same tyre tracks, with an explicit not-list (*not brick, not stone, not board-and-batten, not stucco, not shingle, not green, not grey*).
- **The style swatch is fenced off** — *"DO NOT TAKE ANYTHING ELSE FROM IT - not its brick wall, not its gable, not its snowman, not its truck, not its street, not its wet road, not its mostly-white palette, not its camera position."*
- **"THE CAMERA HAS TILTED UP A LITTLE - IT HAS NOT MOVED"** — the door must be *exactly the same SIZE* in the picture; only the vertical framing shifts.

It worked: v29's cream siding, both lanterns and all four window groups survive the regeneration where v30/v31's did not.

### C04 g7 — denser strands

Ref: **v29 C4 g6** (`a6bcff66-91f5-4629-be28-3ba99b78c3a7`) — the whole approved shot. One thing changes: roughly double the strand count.

**Frame:** `v29_c04_g5.png`

#### Image prompt

```
COPY THE ATTACHED IMAGE EXACTLY. Same house, same soft white sectional double garage door, same pale cream lap siding, same white trim, same black coach lanterns glowing warm either side, same snowy concrete driveway, same night light, same camera, same framing, same distance, same square-on angle, same foreground hand holding the same iPhone in the bottom-centre with the SAME two-column app grid and the same round blue play button. Everything is already correct and must be reproduced unchanged.

ONE SINGLE THING CHANGES: THE LED CURTAIN HAS ROUGHLY TWICE AS MANY STRANDS. In the attached image the vertical strands hanging over the garage door are spaced widely apart. Here they are packed about TWICE AS CLOSE TOGETHER - roughly double the number of strands across the same width, so the curtain reads as a much DENSER set of vertical lines running down the whole face of the door.

THE STRANDS THEMSELVES ARE UNCHANGED: each one is still a thin BLACK cord carrying small DARK unlit bulbs, the lights are OFF with no glow, and against the pale door each cord reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. They still hang from the trim board above the door, still span the full width of the door edge to edge, still have a slight natural sag and a slightly uneven bottom hem.

STILL A CURTAIN, NEVER A PANEL - CRITICAL: even at double the density these are SEPARATE HANGING VERTICAL STRANDS with clear DARK GAPS between them, and the garage door behind is plainly visible through those gaps - the recessed panel seams and the row of small square windows across the top must still read clearly through the curtain. Do NOT close the gaps. Do NOT turn it into a solid LED panel, a flat screen, a mesh, a net, a grille or a fabric sheet. Do NOT add horizontal wires. The strands run straight up and down only.

THE FRAMING IS ALREADY CORRECT - DO NOT CHANGE IT. The garage door stays big and dominant, spanning almost the full width of the picture, with the ENTIRE door visible: both vertical side edges inside the frame, the complete top edge including the WHOLE row of small square windows end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT tilt. Still square-on from the front: the panel seams run dead level and the door edges run straight up and down.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every individual black cord clearly readable and clearly separated from its neighbours, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### C04 animation reference

Refs: **v29 C4 g7 job** (`e128771f-0b9b-4145-aa16-e6e71f5ca6f3`) for the scene + **v29 C7 g1 job** (`40058517-9846-48c1-88e3-d48519a63b52`) for the bulb-art drawing style only.

The scene is **the runaway sleigh** — four reindeer flat out in a gallop, the sleigh tipped up on one runner, Santa hanging on by one hand with his hat blown off, presents bouncing out the back. Deliberately not a snowman: v29's C7 already is one, and reusing it would have invited the style reference to copy its whole scene.

**Frame:** `v29_c04_r1.png`

#### Image prompt

```
THE FIRST ATTACHED IMAGE IS THE SCENE AND IT MUST NOT CHANGE. THE SECOND ATTACHED IMAGE IS A STYLE SWATCH ONLY.

THE HOUSE IS NOT ALLOWED TO CHANGE - THIS IS THE MOST IMPORTANT INSTRUCTION. It must read as LITERALLY THE SAME GARAGE, photographed from the same spot a moment later. Identical PALE CREAM LAP SIDING with its fine horizontal board lines - not brick, not stone, not board-and-batten, not stucco, not shingle, not green, not grey. Identical SOFT WHITE SECTIONAL DOUBLE GARAGE DOOR, the same pale off-white colour, the same wide recessed rectangular panels, the same horizontal seams in the same places, and across the top the same row of small square windows in the SAME FOUR GROUPS OF FOUR with the same spacing. Identical crisp WHITE TRIM boards framing the door and the same white surround. Identical TWO BLACK COACH LANTERNS, one on the wall either side of the door at the same height, glowing the same warm amber. Identical snowy concrete driveway with the same tyre tracks. Identical night sky and the same cool ambient light. Do NOT restyle the door, do NOT change its proportions, do NOT change its colour, do NOT re-texture the siding, do NOT move the lanterns, do NOT add windows or trim or brickwork that is not already there.

THE SECOND ATTACHED IMAGE IS FOR ONE THING ONLY: how a cartoon is drawn out of small round lit bulbs strung on a curtain. DO NOT TAKE ANYTHING ELSE FROM IT - not its brick wall, not its gable, not its snowman, not its truck, not its street, not its wet road, not its mostly-white palette, not its camera position. Style of the bulbs only.

THREE THINGS CHANGE FROM THE FIRST IMAGE:

1. THE HAND AND THE PHONE ARE GONE. There is nothing at all in the foreground. No hand, no arm, no sleeve, no phone, no screen, no glow from a screen. The bottom of the frame is simply the empty snowy driveway. The whole garage door is completely unobstructed from edge to edge.

2. THE CAMERA HAS TILTED UP A LITTLE - IT HAS NOT MOVED. This is a handheld iPhone shot and the person filming has tipped the phone up slightly so the lights fill the frame. The camera stays in exactly the same place at exactly the same distance: the garage door must be exactly the same SIZE in the picture as it is in the first image, spanning almost the full width with only a narrow strip of trim and siding beyond each side edge. Do NOT step back, do NOT step closer, do NOT zoom out, do NOT add more siding to the left or right. Only the vertical framing shifts: there is now just a THIN sliver of driveway along the bottom edge and a slightly deeper band of siding above the top of the door. Still square-on from the front - the panel seams run dead level and the door edges run straight up and down. The ENTIRE door stays inside the frame: both side edges, the complete top edge with the whole row of square windows end to end, and the bottom edge where the door meets the driveway.

3. THE LED CURTAIN IS SWITCHED ON AND SHOWING A BRIGHT CARTOON ANIMATION. The same dense curtain of closely spaced vertical strands hanging over the garage door, but now every bulb is lit and together they draw a picture.

THE PICTURE - THE RUNAWAY SLEIGH, drawn chunky and simple out of the bulbs, running RIGHT ACROSS THE WHOLE GARAGE DOOR from left to right: FOUR REINDEER stretched out flat in a full-tilt gallop fill the left and centre of the door, legs kicked straight out fore and aft, antlers back, tongues out, eyes as wide white circles, the lead reindeer looking back over his shoulder in alarm. Behind them at the RIGHT the SLEIGH is tipped up on one runner, skidding at a steep angle, a fan of snow spraying off the runner. SANTA has been thrown half out of the seat and clings on by ONE HAND, body streaming horizontally behind the sleigh, legs kicking in the air, mouth wide open in a big round O, his red hat already blown off and tumbling away. Curved speed lines and dotted trajectory arcs trail the whole team. PRESENTS bounce out of the back of the sleigh, seven or eight of them, each a DIFFERENT BRIGHT COLOUR - emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow, two burst open. Small gold stars scattered through the gaps. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

THE PICTURE FILLS THE ENTIRE GARAGE DOOR: the team spans the FULL WIDTH of the door from its left edge to its right edge, and the reindeer plus the sleigh plus the bouncing presents plus the stars fill the FULL HEIGHT of the door from just under the row of square windows down to the bottom edge. Every part of the door is covered by lit artwork - no large dark empty areas anywhere on the door, and nothing is confined to a small panel in the middle. Nothing lit appears above the door, on the trim, on the siding, on the lanterns or in the sky.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. The strands are densely spaced but there are still clear DARK GAPS between them and the white garage door behind is plainly visible through those gaps, especially in the unlit areas - the recessed panel seams and the row of square windows must still read through the curtain. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the cream lap siding, the garage door panels and the snowy driveway clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

### Generated set

| Frame | Shot | Job id | Index | Status |
|---|---|---|---|---|
| `v29_c04_g5.png` | C04 start frame | `e128771f-0b9b-4145-aa16-e6e71f5ca6f3` | 290407 | completed, first attempt |
| `v29_c04_r1.png` | C04 animation ref | `e6ce481d-4efe-4398-81b6-56f0958caa61` | 290421 | completed, first attempt |

Both 1520 × 2688 PNG, `gpt_image_2`, 9:16, 2k, quality `medium`. Workspace **Oneofone1**. One generation each, no re-rolls. No `declined_preset_id`, no preset recommendation, no `ip_detected`.

### Open points for review

- **The siding still reads cream rather than the warm sand-beige of the spec.** Inherited from g6 and earlier; the brief was density only, so it was left alone rather than fixed unasked. Same drift as v30/v31. Worth a separate pass across all three if it matters.
- The runaway-sleigh scene is one generation, unreviewed. If the gag is wrong it is cheap to re-run — only the middle paragraph of the prompt needs swapping.

### C01 — g2 (Daniel: "it's winter outside so the delivery guy must be dressed properly and not so sunny outside")

**Frame:** `starting_frames/v29_c01_g1.png` · **Job id:** `67161458-5765-467e-b459-f4f763c6e5d5` · same model/params/refs as g1.

Base = the g1 prompt above with exactly two clauses swapped:

1. **SKY bullet** → "a flat OVERCAST WINTER SKY - an even soft pale grey cloud deck filling the upper part of the vertical frame. NO blue sky, NO sunshine, NO bright white cumulus clouds, NO sun flare." Grass/trees also described as bare winter, and the lighting line became "soft even diffuse overcast daylight from the whole sky, cool neutral white balance, gentle soft-edged shadows on the ground rather than hard ones, bright and properly exposed with full rich detail - no murk, no gloom."
2. **Courier wardrobe** → "HE IS DRESSED FOR REAL WINTER COLD... a thick padded RED delivery WINTER JACKET zipped to the chin with the collar up, a dark grey fleece or hoodie showing at the neck, heavy dark grey insulated work trousers, thick black winter boots, a plain dark knitted BEANIE pulled down over his ears and dark work GLOVES on his hands. His breath is faintly visible in the cold air. NOT a short-sleeved polo, NOT summer clothing, NOT bare arms."

Everything else — camera, brick pillar, walkway, cars, houses, the five-box stack — left untouched.

## C01 — CLIP (from v29_c01_g1.png)

Daniel's brief: *"Like this video attached, so you need to analyze it frame by frame. Fix stable doorbell camera, the man walks with the packages, when he arrives in front of the door tries to open the door then falls on the ground."*

- Job id: `8847dd79-de9d-466b-8d5e-cbf0e83d7f40`
- Model: seedance_2_5, mode omni_reference, 720p, 9:16, 5s, generate_audio true, declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`
- Start image: job `67161458-5765-467e-b459-f4f763c6e5d5` (`starting_frames/v29_c01_g1.png`)
- Output: `clips/v29_c01_g1.mp4` (720x1280, 5.04s)

### Reference video analysis — `0916-1.mp4` (9.45s, 30fps, 4K doorbell cam)

Beat map read off a 4fps contact sheet plus full-res transition frames:

| time | beat |
|---|---|
| 0.0–2.5s | courier in a salmon tee walks up the concrete walkway toward the door, growing in frame, hugging a stack of parcels with both forearms underneath, top parcel at chin height |
| 2.5–4.5s | steps onto the doorstep, now filling most of the frame, quarter-turns to the door, shifts the whole stack onto his left arm to free his right hand |
| 4.5–5.4s | right hand on the handle, shoulder leaning in, weight on the ball of one foot |
| 5.4–5.8s | feet skid, he drops backwards and sideways, right arm shoots up and grabs at nothing, parcels burst out and skitter across the step |
| 5.8–7.0s | down on the concrete on his side, legs splayed, low in the frame |
| 7.0–9.4s | props up on one elbow, looks at the mess, does not get up |

Retimed to 5s as 1.6 / 1.0 / 0.8 / 0.8 / 0.8.

### Prompt

The prompt opens with a hard camera lock ("THE CAMERA NEVER MOVES... the red brick pillar stays locked in exactly the same place along the right edge for all five seconds... treat the background as a still photograph"), then the timeline above with explicit time ranges, then a PHYSICS AND REALISM block ("gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down"), a BANNED list (camera movement, second person, door opening, rubbery limbs, morphing faces, boxes vanishing or duplicating, slow motion, text/timestamp/watermark), a LOOK block (sharp modern 2K colour doorbell recording, not a movie/render), and an AUDIO block: footsteps, cold wind, the scuff and thud, cardboard clattering, one involuntary grunt — no music, Daniel scores in CapCut.

The carry is described mechanically so it matches the reference: "both forearms underneath and both hands clamped on the far side, the stack tipped back against his collarbone, the top box level with his chin so it half hides his lower face."

## C01 — FRAME g3 (door added)
Job `939fbf50-ac73-47ea-9c13-42f57a92f455` · gpt_image_2 · 2k / medium / 9:16 · 1520x2688
Refs: `67161458-...` (v29_c01_g1 frame, layout+look) + `2812fa88-...` (box packshot)
Out: `starting_frames/v29_c01_g3.png`
Why: Daniel — "the door looks like appear out of nowhere and it looks extremly fake".
g2 had NO door anywhere in frame, so seedance had to invent one mid-clip and it popped in.
Fix = put the CLOSED glass storm door + dark panelled inner door with wreath into the
START FRAME, down the left edge (mirroring the brick pillar on the right). Prompt was
"reproduce the first image exactly, change ONE thing only" + a GEOMETRY block (rigid,
plumb, square, only very slight barrel distortion) + BANNED (not open, not ajar, nobody
in the doorway, no fisheye, no arched head).

## C01 — CLIP g3
Job `275b433d-2f63-4b85-8818-20839db6440c` · seedance_2_5 · omni_reference · 720p / 9:16 / 5s
generate_audio true · use_unlim false · declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612`
start_image `939fbf50-ac73-47ea-9c13-42f57a92f455` (v29_c01_g3.png)
Out: `clips/v29_c01_g3.mp4` — 720x1280, 5.042s
Key change vs g2b: a "THE DOOR IS ALREADY THERE IN FRAME ONE" block — do NOT invent a
door, do NOT make one appear/fade/pop/slide in; only the storm-door LEAF moves, pivoting
on one vertical edge like a real door. Open arc given its own beat (2.5-3.4s) so it takes
most of a second instead of snapping. BANNED gained: no door appearing out of nowhere, no
door materialising/fading/popping/sliding into frame, no second door, no ghosting or
transparency on the door frame.
Superseded: `clips/v29_c01_g2.mp4` (job f2669561-95f3-44e2-9e91-ef0067aade6d) — same
door beat but animated from the doorless g2 frame; rejected for the pop-in.
Also note: job 4d8dbe86 failed instantly because start_image was passed the VIDEO job id
instead of the image job id. Always pass the gpt_image_2 job id.

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
| `clips/upscaled/v29_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v29_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v29_c03_g4.mp4` | Named derivative of `../v29_c03_g4.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v29_c04_g7.mp4` | Named derivative of `../v29_c04_g7.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v29_c05_g2.mp4` | Named derivative of `../v29_c05_g2.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v29_c06_g3.mp4` | Named derivative of `../v29_c06_g3.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v29_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c01_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c03_g3.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v29_c03_g4.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v29_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c04_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c04_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c04_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c04_g7.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v29_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c05_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v29_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v29_c06_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v29_c06_g3.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v29_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v29_c04_r1.png` | Embedded PNG `hf-job-id`: `e6ce481d-4efe-4398-81b6-56f0958caa61`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c01_g1.png` | Embedded PNG `hf-job-id`: `2fdc74d9-a1d0-4380-b04a-bfb2b7c58410`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c01_g2.png` | Embedded PNG `hf-job-id`: `67161458-5765-467e-b459-f4f763c6e5d5`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c01_g3.png` | Embedded PNG `hf-job-id`: `939fbf50-ac73-47ea-9c13-42f57a92f455`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c02_g1.png` | Embedded PNG `hf-job-id`: `07ebb15c-1e14-4ef7-b576-b0f4210e0c5b`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c03_g1.png` | Embedded PNG `hf-job-id`: `169ef4c8-94f6-48cc-8693-ebf981b6262f`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c03_g2.png` | Embedded PNG `hf-job-id`: `46b340e4-6caf-44c9-aa30-cc219dfe59a6`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v29_c04_g1.png` | Embedded PNG `hf-job-id`: `271193cf-e71e-4035-8a7d-9eb0dd0f53ec`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c04_g2.png` | Embedded PNG `hf-job-id`: `74f96513-1d68-4eaa-9df1-a61c1942df84`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c04_g3.png` | Embedded PNG `hf-job-id`: `7da86a25-4fc3-4f5a-b61c-17d596c8f6ac`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c04_g4.png` | Embedded PNG `hf-job-id`: `47ab5ef5-d6af-455c-b06c-fba3cc3025de`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c04_g5.png` | Embedded PNG `hf-job-id`: `da8d1a05-5120-4508-96dc-c55f9c491d16`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c04_g6.png` | Embedded PNG `hf-job-id`: `a6bcff66-91f5-4629-be28-3ba99b78c3a7`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v29_c04_g7.png` | Embedded PNG `hf-job-id`: `e128771f-0b9b-4145-aa16-e6e71f5ca6f3`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v29_c05_g1.png` | Embedded PNG `hf-job-id`: `0f0bd301-46da-449b-a256-fc8baa127215`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c06_g1.png` | Embedded PNG `hf-job-id`: `63a2e39f-ba00-457e-b1d2-0302fbe6c6e2`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v29_c07_g1.png` | Embedded PNG `hf-job-id`: `40058517-9846-48c1-88e3-d48519a63b52`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |

### Unresolved take records

The following 10 files still need exact take provenance or verified derivative lineage. Their presence is documented; their prompts have **not** been invented. MP4 C2PA manifest and instance IDs are authenticity identifiers, not Higgsfield job IDs.

- `clips/upscaled/v29_c03_g4.mp4`
- `clips/upscaled/v29_c04_g7.mp4`
- `clips/upscaled/v29_c05_g2.mp4`
- `clips/upscaled/v29_c06_g3.mp4`
- `clips/v29_c03_g3.mp4`
- `clips/v29_c03_g4.mp4`
- `clips/v29_c04_g7.mp4`
- `clips/v29_c05_g2.mp4`
- `clips/v29_c06_g2.mp4`
- `clips/v29_c06_g3.mp4`

### Recovered take — `starting_frames/v29_c03_g2.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `46b340e4-6caf-44c9-aa30-cc219dfe59a6`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
COPY THE CAMERA OF THE FIRST ATTACHED IMAGE EXACTLY - its position, its angle, its height, its closeness and her pose. This is a CLOSE, SIDE-ON shot, not the wide frontal shot.

THE CAMERA IS CLOSE AND OFF TO ONE SIDE, exactly as in the first image: the camera stands near the wall and slightly behind her at roughly waist height, looking ALONG the wall, so the wall runs away from the camera DIAGONALLY - nearest at the bottom-left of the frame and receding to the right, the roof gutter line along the top sloping down towards the right as it goes away, strong oblique one-point perspective. She fills most of the frame height in the right half, her whole body in shot from her boots on the stool up to her raised hands. MUCH CLOSER than a full-house shot: only a short run of the wall is in frame, no full facade, no wide establishing view, no flat square-on frontal view.

HER POSE - copy it from the first image: she stands on a small BLACK two-step folding step stool, seen from BEHIND and slightly to the side, facing the wall, both arms raised in front of her, her hands up at the trim board along the top of the wall as she presses the LED curtain into place. Her weight is on one foot, her back slightly arched.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Long vertical strands of thin BLACK cord with small DARK unlit bulbs hang down the wall to the left of her, and because the camera is close the strands are big in the frame and clearly readable as separate cords. A BIG LOOSE TANGLE of BLACK cord is heaped on the snow at the foot of the stool, spilling out to the left - a real messy nest of wire, obviously dark against the white snow, exactly like the bundle in the first image. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE HOUSE AND THE WOMAN - TAKE THEM FROM THE SECOND ATTACHED IMAGE, NOT FROM THE FIRST. It must read as LITERALLY THE SAME HOUSE and the SAME WOMAN as the second image, now seen close up from the side. The wall she is working on is the WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR of that house - soft WHITE with horizontal panel seams and recessed rectangular panels running away in perspective, and the row of small square windows across the top of the door visible at the far end. Around it the same WARM SAND-BEIGE lap siding with crisp WHITE trim, the same BLACK COACH LANTERN on the wall, the same WHITE gutter and WHITE downpipe, the same plain CONCRETE driveway under patchy snow. At the RIGHT of the frame, further away, the corner where the garage wing meets the MAIN HOUSE BODY is visible - the two-storey wall, the covered porch on white posts and the DARK RED front door - so it still reads as ONE house with the garage built into it. Same late-twenties woman with fair skin and COPPER-RED hair in a high ponytail spilling out from under a cream beanie, BURGUNDY puffer jacket, dark blue jeans, tan boots.

DO NOT COPY FROM THE FIRST IMAGE: not the dark slate-blue board-and-batten siding, not the shingled neighbouring house, not the brick wall, not the hedge, not her mustard-yellow jacket, not her dark curly hair, not her black trousers and not her white boots. The first image is there ONLY for the camera, the distance, the angle and the pose.

Daytime, overcast winter light, snow on the ground.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the door panels, the quilting of her jacket and every strand of black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "9894c57e-8d7f-4754-9b39-357f18277863",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/9894c57e-8d7f-4754-9b39-357f18277863.png"
      }
    },
    {
      "role": "image",
      "data": {
        "id": "169ef4c8-94f6-48cc-8693-ebf981b6262f",
        "type": "image_job",
        "url": "https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_201304_169ef4c8-94f6-48cc-8693-ebf981b6262f.png"
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


### Recovered take — `starting_frames/v29_c04_g6.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `a6bcff66-91f5-4629-be28-3ba99b78c3a7`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
Same shot as the attached image - same night, same house, same square-on frontal angle, same garage door, same curtain, same lanterns, same phone, same hand, same app screen. ONE THING CHANGES: THE GARAGE DOOR IS BIGGER IN THE FRAME.

THE CHANGE - PUSH IN SO THE GARAGE DOOR IS MUCH BIGGER. In the attached image the door sits too small with too much empty space around it. Move the camera closer to the house so the door grows to fill the picture: the door must now span almost the FULL WIDTH of the frame, with only a NARROW STRIP of white trim and siding left visible beyond its left edge and beyond its right edge, and only a SHALLOW BAND of siding above its top edge. Cut down the empty driveway at the bottom so only a low strip of snowy concrete remains under the door. The garage door should be by far the dominant object in the picture, big and imposing, reading at the same large scale as the wall does in the daytime install shot.

BUT THE ENTIRE DOOR MUST STILL BE VISIBLE - THIS IS THE LIMIT ON HOW FAR TO PUSH IN. Both vertical side edges of the door stay inside the frame with that narrow strip of trim and siding beyond each one. The complete top edge stays inside the frame, including the WHOLE row of small square windows running all the way across it, every window visible end to end. The bottom edge where the door meets the concrete driveway stays inside the frame. Nothing about the door is cut off by any edge of the picture. Push in exactly as far as that allows and no further.

STILL SQUARE-ON FROM THE FRONT: the door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up, NO whole house, NO full facade, NO roofline.

EVERYTHING ELSE IS UNCHANGED from the attached image. The same warm-lit lap siding and white trim around the door, the same black coach lanterns glowing warm on the wall either side, the sliver of covered porch and dark front door cropped at the right edge, the snowy concrete driveway, the night sky, the same warm lantern light and street-lamp spill.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the door in evenly spaced vertical see-through strands right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale door each strand reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen. At this closer range the strands and the bulbs are bigger and even easier to read.

THE PHONE AND ITS SCREEN ARE UNCHANGED - COPY THEM EXACTLY FROM THE ATTACHED IMAGE. Same handset, same hand, same grip, same angle, same size and same position in the bottom-centre foreground. Pushing the camera in must NOT shrink the phone and must NOT enlarge it. The screen shows the SAME app: a dark navy-blue screen with a grid of just TWO COLUMNS of large tiles, two across and about five down, roughly ten tiles in total and no more, each tile nearly half the screen wide with softly rounded corners and a narrow gutter, each one a small photograph of a house decorated in Christmas lights - a lit roofline, a nativity, a snowman, a reindeer, a porch draped in light curtains - mostly icy blue and cool white with a couple of warm tiles, ONE tile ringed with a bright electric-blue outline, and a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE below the grid. NOT a dense grid of tiny icons, NOT three or more columns, NO glyphs or pictograms, and NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

The phone is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "da8d1a05-5120-4508-96dc-c55f9c491d16",
        "type": "image_job",
        "url": "https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_205200_da8d1a05-5120-4508-96dc-c55f9c491d16.png"
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


### Recovered take — `starting_frames/v29_c04_g7.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `e128771f-0b9b-4145-aa16-e6e71f5ca6f3`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
COPY THE ATTACHED IMAGE EXACTLY. Same house, same soft white sectional double garage door, same pale cream lap siding, same white trim, same black coach lanterns glowing warm either side, same snowy concrete driveway, same night light, same camera, same framing, same distance, same square-on angle, same foreground hand holding the same iPhone in the bottom-centre with the SAME two-column app grid and the same round blue play button. Everything is already correct and must be reproduced unchanged.

ONE SINGLE THING CHANGES: THE LED CURTAIN HAS ROUGHLY TWICE AS MANY STRANDS. In the attached image the vertical strands hanging over the garage door are spaced widely apart. Here they are packed about TWICE AS CLOSE TOGETHER - roughly double the number of strands across the same width, so the curtain reads as a much DENSER set of vertical lines running down the whole face of the door.

THE STRANDS THEMSELVES ARE UNCHANGED: each one is still a thin BLACK cord carrying small DARK unlit bulbs, the lights are OFF with no glow, and against the pale door each cord reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. They still hang from the trim board above the door, still span the full width of the door edge to edge, still have a slight natural sag and a slightly uneven bottom hem.

STILL A CURTAIN, NEVER A PANEL - CRITICAL: even at double the density these are SEPARATE HANGING VERTICAL STRANDS with clear DARK GAPS between them, and the garage door behind is plainly visible through those gaps - the recessed panel seams and the row of small square windows across the top must still read clearly through the curtain. Do NOT close the gaps. Do NOT turn it into a solid LED panel, a flat screen, a mesh, a net, a grille or a fabric sheet. Do NOT add horizontal wires. The strands run straight up and down only.

THE FRAMING IS ALREADY CORRECT - DO NOT CHANGE IT. The garage door stays big and dominant, spanning almost the full width of the picture, with the ENTIRE door visible: both vertical side edges inside the frame, the complete top edge including the WHOLE row of small square windows end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT tilt. Still square-on from the front: the panel seams run dead level and the door edges run straight up and down.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every individual black cord clearly readable and clearly separated from its neighbours, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "a6bcff66-91f5-4629-be28-3ba99b78c3a7",
        "type": "image_job",
        "url": "https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_205622_a6bcff66-91f5-4629-be28-3ba99b78c3a7.png"
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

- C01: the board did not show the exact image prompt of `v29_c01_g2.png`; it now does.
- C01: the board did not show the exact clip prompt of `v29_c01_g1.mp4`; it now does.
- C02: the board did not show the exact clip prompt of `v29_c02_g1.mp4`; it now does.
- C03: the board showed `v29_c03_g1.png` as the start frame, but the clip in the cut was animated from `v29_c03_g2.png` (the Higgsfield start image). Card corrected.
- C03: the board did not show the exact clip prompt of `v29_c03_g4.mp4`; it now does.
- C04: the board did not show the exact image prompt of `v29_c04_g5.png`; it now does.
- C05: the board did not show the exact clip prompt of `v29_c05_g2.mp4`; it now does.
- C06: the board did not show the exact clip prompt of `v29_c06_g3.mp4`; it now does.
- C07: the board did not show the exact clip prompt of `v29_c07_g1.mp4`; it now does.

### C01 — Courier goes down on the walkway

**In the cut:** `starting_frames/v29_c01_g2.png` → `clips/v29_c01_g1.mp4`

#### Image prompt — `starting_frames/v29_c01_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `67161458-5765-467e-b459-f4f763c6e5d5`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_234738_67161458-5765-467e-b459-f4f763c6e5d5.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `7e07b8cb-69b5-4076-bf41-412c058391a1`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
Reproduce the FIRST attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a FRONT-DOOR DOORBELL CAMERA. Keep the same suburban American street, the same location, but a COLD OVERCAST WINTER DAY.

THE CAMERA - copy it from the first image: a doorbell camera fixed to the wall beside a front door, about 1.2 metres off the ground, looking straight out across the porch and the front lawn toward the street. Very wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Slightly low, flat, static, unmanned viewpoint - NOT a handheld phone shot, NOT a cinematic camera.

EVERYTHING BELOW STAYS AS IN THE FIRST IMAGE, just re-stacked for a vertical frame:
- RIGHT EDGE: a RED BRICK porch pillar in extreme close foreground, very near the lens, filling a tall vertical band down the whole right side of the frame, its brick and mortar texture large and soft, a pale cast-stone cap at the top. It frames the shot like a curtain.
- LEFT EDGE: the corner of the house in white lap siding, running away from the camera, and below it a low RED BRICK porch wall along the bottom-left with a green pine garland and a few red baubles laid along its top.
- CENTRE: a pale CONCRETE WALKWAY running from the bottom of the frame away from the porch, out across the lawn to the driveway. Winter grass either side, a bare flowerbed at the bottom left with a red-and-white candy-cane stake pushed into the soil.
- MIDDLE DISTANCE: a concrete driveway with a white SUV and a dark grey car parked nose-in, a pavement, then the street.
- BACKGROUND: the row of houses on the opposite side of the street - beige and grey two-storey homes with white double garage doors, a red car sitting in one of the driveways, bare leafless winter trees, a lawn.
- SKY: a flat OVERCAST WINTER SKY - an even soft pale grey cloud deck filling the upper part of the vertical frame. NO blue sky, NO sunshine, NO bright white cumulus clouds, NO sun flare.

THE COURIER AND WHAT HE IS CARRYING. In the middle ground, on the walkway where the delivery man stands in the first image, a DELIVERY COURIER is walking toward the front door, caught mid-stride in profile with one leg forward, leaning back slightly under the weight. He is a whole figure, medium-sized in the frame, clearly readable but not close up.

HE IS DRESSED FOR REAL WINTER COLD, because it is a freezing overcast winter day: a thick padded RED delivery WINTER JACKET zipped to the chin with the collar up, a dark grey fleece or hoodie showing at the neck, heavy dark grey insulated work trousers, thick black winter boots, a plain dark knitted BEANIE pulled down over his ears and dark work GLOVES on his hands. His breath is faintly visible in the cold air. No company logo of any kind anywhere on him. NOT a short-sleeved polo, NOT summer clothing, NOT bare arms.

HE IS CARRYING A BIG STACK OF THE PRODUCT BOXES FROM THE SECOND ATTACHED IMAGE - FIVE of them, and they must be copied exactly from that second image: flat MATTE BLACK rigid retail boxes, on the front a large white condensed uppercase headline, a warm gold subline under it, a small red diagonal ribbon flag in the top-right corner, one large photographic panel with a thin gold hairline border filling the middle and lower two thirds showing a night photo of a suburban house facade lit with Christmas lights, and a bottom row of five small gold line icons. Closed and sealed - NO transparent window, NO clear plastic panel, NO cutout, nothing visible inside.

THE STACK: the five boxes are stacked one on top of another and hugged against his chest with both gloved arms wrapped underneath and around them, tilted back against his body so the PRINTED BLACK FRONT FACE of the nearest box is angled toward the camera and clearly readable, the other four stacked behind it with their black edges visible. Each box is WIDE - about 55 cm across, wider than his own shoulders - so the stack sticks out well past both sides of his body and the top of it reaches his chin and he is peering over the corner of it. Real weight: his arms strain, his back leans back, the stack sags slightly to one side. Every box is the same matte black box - NOT brown cardboard, NOT red, NOT green, NOT white, NOT generic parcels, NOT patterned Christmas packaging.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour doorbell-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork, in the print on the boxes and in the houses across the street. Beautiful clean lighting even though the day is grey: soft even diffuse overcast daylight from the whole sky, cool neutral white balance, gentle soft-edged shadows on the ground rather than hard ones, bright and properly exposed with full rich detail - no murk, no gloom, no blown-out white in the sky, no crushed black in the porch shadow. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos on his jacket or on the vehicles. Not a render, not an illustration, no cinematic colour grading.
````

#### Video prompt — `clips/v29_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `f2669561-95f3-44e2-9e91-ef0067aade6d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_005206_f2669561-95f3-44e2-9e91-ef0067aade6d.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v29_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c01_g2.png` · Higgsfield media `67161458-5765-467e-b459-f4f763c6e5d5`

````text
THE CAMERA NEVER MOVES. This is the single most important rule. The shot is a fixed doorbell camera screwed to the brick pillar beside the front door. It does not pan, tilt, zoom, dolly, orbit, shake, drift, rack focus or re-frame at any moment. The red brick pillar stays locked in exactly the same place along the right edge of the frame for all five seconds, the white siding stays locked along the left edge, the horizon and the parked white car and the houses across the street never shift by a single pixel. Everything that moves in this clip is the man and the door. Treat the background as a still photograph.

Continue the attached start frame as one continuous unbroken five-second take. No cuts, no edits, no transitions, no speed ramps, no slow motion. Same courier, same clothes, same winter light, same street as the frame.

THE DOOR MUST BE CLEARLY VISIBLE AND IT MUST OPEN. The house has an outward-opening glass STORM DOOR in front of the main door: a full-height sheet of clear glass in a slim aluminium frame with a horizontal lever handle. When the courier pulls that handle the storm door swings OUTWARD toward the camera and toward him, hinged on its far side, so the lit aluminium frame arcs across the frame and the open glass panel stays plainly visible, propped open, for the whole rest of the clip. The viewer must be able to see without any doubt that a door has been opened and is standing open. The door never closes again, never disappears, never swings back, and is never hidden.

THE ACTION, as a timeline:
0.0-1.6s - The courier walks up the concrete front walkway toward the door, coming steadily TOWARD the camera so he grows larger in frame. He is hugging the tall stack of matte black boxes against his chest with BOTH forearms underneath and both hands clamped on the far side, the stack tipped back against his collarbone, the top box level with his chin so it half hides his lower face. He has to lean back slightly to counterweight it. Normal walking pace, three or four real steps, his weight rolling heel to toe, his shoulders swaying a little with the load, his breath faintly visible in the cold.
1.6-2.4s - He reaches the doorstep and steps up onto it, now CLOSE to the camera and BIG in the frame, filling most of its height. He turns his body a quarter turn to face the door, shifting the whole stack across onto his LEFT forearm and hip so his right hand comes free. The stack sags and he clamps his left arm tighter.
2.4-3.4s - His right hand closes on the lever handle of the glass storm door and he PULLS. The storm door swings open outward toward him, its aluminium frame sweeping into the frame and its clear glass panel catching the daylight, revealing the dark inner door behind it. He steps back a half pace to let it past him, still hugging the boxes on his left arm, and ends up off balance on the ball of one foot with the door standing wide open beside him.
3.4-4.2s - HE FALLS. His front foot skids out from under him on the doorstep. He drops fast and heavily, straight down and backwards, twisting as he goes. His right hand slips off the door handle and his arm shoots up and out and grabs at nothing. The stack of boxes bursts out of his left arm and the boxes tumble and slide away across the step and the walkway, bouncing and skittering. He lands hard on his hip and shoulder on the concrete, low in the frame, legs splayed. The storm door stays standing open above him, still clearly in shot.
4.2-5.0s - He is down on the ground at the bottom of the frame, on his side, one knee up, breathing hard. He lifts his head and props himself on one elbow, looking at the scattered boxes. He does not get up. Small real movements only - his chest rising, one hand flexing. The open glass door remains visible and motionless.

PHYSICS AND REALISM: a real man with real weight, filmed by a real camera. Gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down. Clothing creases and flaps. The boxes are light, rigid cardboard and they bounce and slide, they do not float, melt, stretch, multiply or vanish. The door is a rigid flat rectangle on real hinges - it swings on one edge only, it does not bend, stretch, flap, ripple or pass through anything. His body stays whole and correctly proportioned throughout - arms and legs bend only at real joints and only the way real joints bend. Feet stay on the ground until he slips.

BANNED: no camera movement of any kind, no zoom, no push in, no handheld shake, no second person appearing, no one inside the house, no one in the doorway, no boxes disappearing or duplicating, no door vanishing or closing itself, no rubbery or elastic limbs, no impossible bends, no morphing faces, no extra arms or hands, no sliding feet, no slow motion, no cinematic grade, no lens flare, no text, no timestamp, no watermark, no logos, no captions, no UI.

LOOK: a genuinely sharp modern 2K colour doorbell-camera recording, bright and correctly exposed in the winter afternoon light, natural colour, crisp detail. Not a movie, not a render, not an illustration.

AUDIO: natural outdoor sound only - his footsteps on the concrete, cold wind, a distant car, the rattle and creak of the aluminium storm door swinging open, the scuff and thud of the fall, the cardboard boxes clattering onto the step, one short involuntary grunt from him as he lands. No music, no score, no background song, no narration, no sound effects library stings.
````

**Other takes of C01 on disk (3)**

#### Image prompt — `starting_frames/v29_c01_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `2fdc74d9-a1d0-4380-b04a-bfb2b7c58410`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_232727_2fdc74d9-a1d0-4380-b04a-bfb2b7c58410.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `7e07b8cb-69b5-4076-bf41-412c058391a1`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
Reproduce the FIRST attached image's camera, viewpoint, lens and composition as faithfully as possible, but as a TALL VERTICAL 9:16 photograph instead of a widescreen one. This is a still frame from a FRONT-DOOR DOORBELL CAMERA. Keep the same suburban American street, the same bright winter afternoon, the same mood.

THE CAMERA - copy it from the first image: a doorbell camera fixed to the wall beside a front door, about 1.2 metres off the ground, looking straight out across the porch and the front lawn toward the street. Very wide-angle lens with mild barrel distortion so the straight lines near the edges bow gently. Slightly low, flat, static, unmanned viewpoint - NOT a handheld phone shot, NOT a cinematic camera.

EVERYTHING BELOW STAYS AS IN THE FIRST IMAGE, just re-stacked for a vertical frame:
- RIGHT EDGE: a RED BRICK porch pillar in extreme close foreground, very near the lens, filling a tall vertical band down the whole right side of the frame, its brick and mortar texture large and soft, a pale cast-stone cap at the top. It frames the shot like a curtain.
- LEFT EDGE: the corner of the house in white lap siding, running away from the camera, and below it a low RED BRICK porch wall along the bottom-left with a green pine garland and a few red baubles laid along its top.
- CENTRE: a pale CONCRETE WALKWAY running from the bottom of the frame away from the porch, out across the lawn to the driveway. Neat winter grass either side, a bare flowerbed at the bottom left with a red-and-white candy-cane stake pushed into the soil.
- MIDDLE DISTANCE: a concrete driveway with a white SUV and a dark grey car parked nose-in, a pavement, then the street.
- BACKGROUND: the row of houses on the opposite side of the street - beige and grey two-storey homes with white double garage doors, a red car sitting in one of the driveways, leafless winter trees, a green lawn.
- SKY: a big clean blue winter sky with bright white cumulus clouds, filling the upper part of the vertical frame.

THE ONE CHANGE - THE COURIER AND WHAT HE IS CARRYING. In the middle ground, on the walkway where the delivery man stands in the first image, a DELIVERY COURIER is walking toward the front door - a man in a plain RED delivery polo shirt and dark grey work trousers with black trainers, no company logo of any kind, caught mid-stride in profile with one leg forward, leaning back slightly under the weight. He is a whole figure, medium-sized in the frame, roughly the height of the walkway width, clearly readable but not close up.

HE IS CARRYING A BIG STACK OF THE PRODUCT BOXES FROM THE SECOND ATTACHED IMAGE - FIVE of them, and they must be copied exactly from that second image: flat MATTE BLACK rigid retail boxes, on the front a large white condensed uppercase headline, a warm gold subline under it, a small red diagonal ribbon flag in the top-right corner, one large photographic panel with a thin gold hairline border filling the middle and lower two thirds showing a night photo of a suburban house facade lit with Christmas lights, and a bottom row of five small gold line icons. Closed and sealed - NO transparent window, NO clear plastic panel, NO cutout, nothing visible inside.

THE STACK: the five boxes are stacked one on top of another and hugged against his chest with both arms wrapped underneath and around them, tilted back against his body so the PRINTED BLACK FRONT FACE of the nearest box is angled toward the camera and clearly readable, the other four stacked behind it with their black edges visible. Each box is WIDE - about 55 cm across, wider than his own shoulders - so the stack sticks out well past both sides of his body and the top of it reaches his chin and he is peering over the corner of it. Real weight: his arms strain, his back leans back, the stack sags slightly to one side. Every box is the same matte black box - NOT brown cardboard, NOT red, NOT green, NOT white, NOT generic parcels, NOT patterned Christmas packaging.

IMAGE QUALITY - CRITICAL: a genuinely high-resolution modern 2K colour doorbell-camera still, tack-sharp edge to edge, crisp fine detail in the brickwork, in the print on the boxes and in the houses across the street. Beautiful clean lighting: low warm late-afternoon winter sun coming in from the left, bright but properly exposed - no blown-out white in the sky or on the concrete, no crushed black in the porch shadow, correct white balance, real contact shadows on the ground. NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze, NO infrared or night-vision look, NO low-resolution CCTV mush.

ABSOLUTELY NO TEXT OR GRAPHICS OVERLAID ON THE IMAGE: no timestamp, no date, no camera label, no recording dot, no channel logo or watermark in any corner, no captions, no subtitles, no arrows or UI. No readable brand names or logos on his shirt or on the vehicles. Not a render, not an illustration, no cinematic colour grading.
````

#### Image prompt — `starting_frames/v29_c01_g3.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `939fbf50-ac73-47ea-9c13-42f57a92f455`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_010453_939fbf50-ac73-47ea-9c13-42f57a92f455.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c01_g2.png` · Higgsfield media `67161458-5765-467e-b459-f4f763c6e5d5`
- @Image 2: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `2812fa88-3367-4746-a761-4e99c42b73d1`

````text
Reproduce the FIRST attached image EXACTLY - same doorbell-camera viewpoint, same lens, same overcast winter day, same red brick pillar filling the right edge, same white lap siding and low brick porch wall with pine garland on the left, same concrete walkway, same driveway with the white SUV, same street and houses opposite, same flat pale grey overcast sky, same courier in the red padded winter jacket, dark beanie and gloves carrying the same stack of five flat MATTE BLACK product boxes from the SECOND attached image. Change ONE thing only, described below. Everything else is pixel-for-pixel the same photograph.

THE ONE CHANGE - ADD THE FRONT DOOR, CLOSED, CLEARLY VISIBLE IN FRAME. On the LEFT side of the frame, in the near foreground where the porch meets the white siding, the house's FRONT ENTRANCE is now in shot and the doorway must be plainly readable to the viewer. It consists of two doors, one behind the other, both fully CLOSED:
1. In front, an outward-opening GLASS STORM DOOR - a single tall sheet of clear glass set in a slim WHITE aluminium frame, with a horizontal brushed-metal LEVER HANDLE at waist height on the near side and a slim kick panel at the bottom. The glass is clean and clear and you can see straight through it.
2. Behind the glass, the solid main entrance door - a dark painted panelled door with a brass handle and a dead bolt, and a small evergreen wreath with a red bow hung on it.
The doorway sits in a plain square white-painted door frame with a straight vertical jamb and a straight horizontal head - no arch, no curve. The bottom of the door meets a flat concrete doorstep.

The door occupies a tall vertical band down the LEFT portion of the frame, roughly the mirror of the brick pillar on the right, and it is close to the camera so it reads large and sharp. It must be unmistakably a real closed door that a person could walk up to and pull open. The courier stays exactly where he is in the first image - out on the walkway, still mid-stride, still a few steps away from the door, NOT touching it.

GEOMETRY AND REALISM: the door frame, the storm-door frame and the jamb are factory-made and rigid - every edge perfectly straight and either plumb or level, corners square, the glass a flat clean plane with a faint even reflection of the grey sky. The doorstep is a flat rectangle with a crisp straight front edge. A normal wide-angle lens with only very slight barrel distortion; straight edges stay straight.

BANNED: the door is NOT open and NOT ajar, nobody is standing in the doorway, no light or interior visible beyond a dark hallway through the glass, no fisheye warping, no bending or melted frames, no rubbery geometry, no curved or arched door head, no second courier, no change to the courier's pose or clothing, no change to the boxes, no change to the sky or the street, no transparent window or cutout on any product box, no text, no timestamp, no watermark, no logo, no captions, no UI.

IMAGE QUALITY: a genuinely high-resolution modern 2K colour doorbell-camera still, tack-sharp edge to edge, soft even diffuse overcast daylight, cool neutral white balance, bright and properly exposed. No motion blur, no depth-of-field blur, no grain, no haze, no night-vision look, no CCTV mush, no cinematic grade.
````

#### Video prompt — `clips/v29_c01_g3.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `275b433d-2f63-4b85-8818-20839db6440c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_010642_275b433d-2f63-4b85-8818-20839db6440c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c01_g3.png` · Higgsfield media `939fbf50-ac73-47ea-9c13-42f57a92f455`

````text
THE CAMERA NEVER MOVES. This is the single most important rule. The shot is a fixed doorbell camera screwed to the brick pillar beside the front door. It does not pan, tilt, zoom, dolly, orbit, shake, drift, rack focus or re-frame at any moment. The red brick pillar stays locked in exactly the same place along the right edge of the frame for all five seconds, the front door and its white frame stay locked along the left edge, the horizon and the parked white car and the houses across the street never shift by a single pixel. Everything that moves in this clip is the man and the door leaf. Treat the background as a still photograph.

Continue the attached start frame as one continuous unbroken five-second take. No cuts, no edits, no transitions, no speed ramps, no slow motion. Same courier, same clothes, same winter light, same street as the frame.

THE DOOR IS ALREADY THERE IN FRAME ONE. Do NOT invent a new door and do NOT make a door appear, fade in, pop in or slide into frame. The closed glass storm door and its white frame, and the dark panelled front door with the wreath behind it, are visible on the LEFT of the attached start frame from the very first frame of the clip and they stay physically in the same place the whole time. Only the storm-door leaf moves, and only by swinging on its hinges. It is a rigid flat rectangle of clear glass in a slim white aluminium frame with a horizontal lever handle - it pivots on one vertical edge like a real door, it does not bend, stretch, flap, ripple, grow, shrink, teleport or pass through anything, and it never disappears once it is open.

THE ACTION, as a timeline:
0.0-1.8s - The courier walks up the concrete front walkway toward the door, coming steadily TOWARD the camera and toward the closed door on the left so he grows larger in frame. He is hugging the stack of matte black boxes against his chest with BOTH forearms underneath and both hands clamped on the far side, the stack tipped back against his collarbone, the top box level with his chin so it half hides his lower face. He has to lean back slightly to counterweight it. Normal walking pace, real steps, his weight rolling heel to toe, his shoulders swaying a little with the load, his breath faintly visible in the cold. The door stays shut.
1.8-2.5s - He steps up onto the flat concrete doorstep, now CLOSE to the camera and BIG in the frame. He turns a quarter turn to face the closed glass door, shifting the whole stack across onto his LEFT forearm and hip so his right hand comes free. The stack sags and he clamps his left arm tighter. The door is still shut.
2.5-3.4s - His right hand closes on the lever handle of the glass storm door and he PULLS it open. The leaf swings outward toward him and toward the camera on its hinges, a smooth continuous arc taking most of a second, the white aluminium frame and the clear glass sweeping across the left of the frame and catching the flat grey daylight, revealing the dark panelled inner door with its wreath standing behind it. He shuffles half a step backwards to let the leaf past him and ends up off balance on the ball of one foot, the glass door now standing wide open beside him and held there.
3.4-4.2s - HE FALLS. His front foot skids out from under him on the doorstep. He drops fast and heavily, straight down and backwards, twisting as he goes. His right hand slips off the handle and his arm shoots up and out and grabs at nothing. The stack of boxes bursts out of his left arm and the boxes tumble and slide away across the step and the walkway, bouncing and skittering. He lands hard on his hip and shoulder on the concrete, low in the frame, legs splayed. The open glass door stays exactly where it is, wide open, still clearly in shot.
4.2-5.0s - He is down on the ground at the bottom of the frame, on his side, one knee up, breathing hard. He lifts his head and props himself on one elbow, looking at the scattered boxes. He does not get up. Small real movements only - his chest rising, one hand flexing. The open glass door is still there, motionless.

PHYSICS AND REALISM: a real man with real weight, filmed by a real camera. Gravity is fast and unforgiving - the fall takes well under a second, it is not floaty or graceful or slowed down. Clothing creases and flaps. The boxes are light, rigid cardboard and they bounce and slide, they do not float, melt, stretch, multiply or vanish. His body stays whole and correctly proportioned throughout - arms and legs bend only at real joints and only the way real joints bend. Feet stay on the ground until he slips.

BANNED: no camera movement of any kind, no zoom, no push in, no handheld shake, no door appearing out of nowhere, no door materialising, fading in, popping in or sliding into frame, no second door, no door closing itself or vanishing, no ghosting or transparency on the door frame, no second person appearing, no one inside the house, no one in the doorway, no boxes disappearing or duplicating, no rubbery or elastic limbs, no impossible bends, no morphing faces, no extra arms or hands, no sliding feet, no slow motion, no cinematic grade, no lens flare, no text, no timestamp, no watermark, no logos, no captions, no UI.

LOOK: a genuinely sharp modern 2K colour doorbell-camera recording, bright and correctly exposed in the flat overcast winter daylight, natural colour, crisp detail. Not a movie, not a render, not an illustration.

AUDIO: natural outdoor sound only - his footsteps on the concrete, cold wind, a distant car, the click of the latch and the creak and rattle of the aluminium storm door swinging open, the scuff and thud of the fall, the cardboard boxes clattering onto the step, one short involuntary grunt from him as he lands. No music, no score, no background song, no narration, no sound effects library stings.
````

### C02 — Box over the sofa

**In the cut:** `starting_frames/v29_c02_g1.png` → `clips/v29_c02_g1.mp4`

#### Image prompt — `starting_frames/v29_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `07ebb15c-1e14-4ef7-b576-b0f4210e0c5b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_201059_07ebb15c-1e14-4ef7-b576-b0f4210e0c5b.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_20_assets/starting_frames/v20_c02_g5.png` · Higgsfield media `05989e1b-228c-432a-be58-a51cfbfa19ad`
- @Image 2: `content/video_28_assets/starting_frames/v28_c02_g1.png` · Higgsfield media `b870ee3e-2453-4d24-8dab-4909ce45bd14`

````text
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. The box is a closed rigid printed gift box with NO transparent window and NO cut-out panel anywhere on it. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: a late-twenties woman with fair skin and COPPER-RED hair worn in a high ponytail, wearing a FOREST-GREEN ribbed knit jumper and CAMEL wide-leg trousers. The room has a warm oak HERRINGBONE floor, a CREAM BOUCLE sofa with rust and mustard cushions and an oatmeal chunky-knit throw, a SAGE-GREEN panelled wainscot wall behind, a woven RATTAN dome pendant lamp hanging above, and a FLOCKED WHITE fir Christmas tree with gold baubles and red berry sprigs at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the knit of her jumper and in the print on the box, clean even indoor light with no blown highlights and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur on the box or on her, NO grain, NO haze, NO soft focus anywhere. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v29_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on
**Job** - `8629900e-5df9-4de5-9133-e94e47fd8b47`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_215611_8629900e-5df9-4de5-9133-e94e47fd8b47.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v29_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c02_g1.png` · Higgsfield media `3ccf24b9-e5a6-4517-9945-5bf165b55d3e`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `6e23db01-1643-4ed2-aee6-1b7954056a31`
- image ref 2: `product_images/box_nowindow/box_interior_g5.png` · Higgsfield media `01d1be50-61f2-4ebc-90df-6b03a0f49c4b`

````text
TWO SCENES IN ONE CLIP, JOINED BY ONE HARD CUT AT EXACTLY 2.5s. No dissolve, no fade, no whip pan, no transition effect — a straight in-camera cut, exactly like a creator cutting two takes together.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE ABOUT THE PERSON IN THIS CLIP. Everything the woman does happens at the pace a real person actually moves. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next. There is DELIBERATELY very little for her to do. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still mid-reach as the clip ends than that any part of it looks fast-forwarded.

REFERENCE IMAGES. Reference image 1 is the first frame of scene 1 — start there, unchanged, and it owns the room, the woman, the camera angle and the geometry. Reference image 2 is the CLOSED PRODUCT BOX: the artwork on the box in this video must match it exactly. Reference image 3 is the OPEN BOX INTERIOR: what she reveals in scene 2 must match it exactly.

THE WOMAN. Late twenties, fair skin, COPPER-RED hair worn long down her back, forest-green ribbed knit jumper, camel wide-leg trousers. She is at the LEFT of frame, seen from behind and slightly over her left shoulder. Her face is never turned fully to camera.

THE ROOM. Warm oak herringbone floor, a cream bouclé sofa running diagonally away to the RIGHT in front of her with rust and mustard cushions, a dark green console with a warm table lamp behind, a woven rattan dome pendant at the top right, a flocked white fir with gold baubles and red berry sprigs at the right edge. Warm indoor evening light. This room does not change between the two scenes — it is the same room, the same lamp, the same tree, the same floor, filmed twice.

BOX SPEC — TRUE IN EVERY FRAME. A matte black rigid retail box, 55 cm wide x 42 cm tall x 10 cm deep. It is BIG — much wider than the span of two outstretched hands, and when she holds it up it covers her whole torso. The printed front face carries the white LED CURTAIN LIGHTS headline, the gold subline, the red BEST SELLER corner flag, one photo panel of a lit house at night and a bottom row of five small icons, exactly as reference image 2. There is NO transparent window anywhere on this box. The artwork never redraws, never rearranges, never changes colour and never gains or loses text between frames.

SCENE 1 — 0.0s to 2.5s. Reference image 1 is frame one, unchanged.
0.0-0.9s — she is holding the big black box out in front of her, both hands under it, turning it a few degrees so the printed front catches the lamp light. Her shoulders settle, her weight moves onto her back foot, a loose strand of copper hair swings against her shoulder.
0.9-1.8s — she lowers the box slowly to waist height, her elbows bending, and takes one unhurried step forward toward the sofa. The room parallaxes very slightly with the step. The box stays flat and level, printed face to camera.
1.8-2.5s — she carries the box round in front of the sofa, sets it flat on the cream seat cushion AND drops to her knees IN THE SAME CONTINUOUS MOTION. The bouclé dimples under the weight. She is STILL settling onto her knees when the cut lands.

HARD CUT AT 2.5s.

SCENE 2 — 2.5s to 5.0s. A closer angle on the same sofa in the same room, still from behind her right shoulder, the box now flat on the seat cushion filling the middle of the frame. The flocked fir is still at the right edge, the lamp still glows behind.

LID MECHANISM, GEOMETRICALLY. The box is a magnetic-closure flip-top. The hinge runs along the TOP LONG EDGE of the box — the far edge away from her, at the back. The lid pivots UP and BACK on that hinge, rotating away from her and toward the back of the sofa, keeping its printed front face turned toward the camera as it rises. The inside of the lid is matte black. The lid is NEVER lifted off, NEVER removed, NEVER carried aside, NEVER set down, NEVER folded flat instantly, NEVER slid out like a drawer.
2.5-3.1s — she hooks her fingertips under the near front edge of the lid; a small snap as the magnets release and the front edge lifts a centimetre, a thin black shadow line opening slowly across the whole 55 cm width.
3.1-4.3s — she pivots the big printed lid UP and BACK on its hinge in ONE slow continuous arc with real cardboard weight, her elbows rising and her shoulders lifting with the effort, until it stands roughly vertical. This arc takes well over a full second of screen time — it travels heavily and never flips or snaps open.
4.3-5.0s — the interior is revealed exactly as reference image 3: the neatly folded BLACK LED mesh curtain lying in its tray, the coiled BLACK lead and the small accessory items beside it, all against a matte black interior. She reaches in with both hands and touches the folded black mesh, fingers spreading it slightly, then lifts her chin, looks off toward the fir tree and breaks into a big open-mouthed grin, eyebrows up.

THE CURTAIN INSIDE THE BOX IS BLACK. The cord is BLACK, the lead is BLACK, the unlit bulbs are small and dark. It is never white, never clear, never silver, never copper-coloured wire.

MOVEMENT RULE FOR BOTH SCENES: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole clip — weight shifting, chest breathing, the loose copper strands swinging and settling, sleeves creasing, the bouclé cushion dimpling under the box — and her face keeps changing, eyes, eyebrows and mouth reading differently moment to moment. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses.

CAMERA: handheld iPhone, held by a friend, locked focal length. Small natural breathing drift only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT within either scene. The only change of framing in the whole clip is the single hard cut at 2.5s.

BANNED: no second person, no pets, no text overlay, no captions, no subtitles, no watermark, no logo bug, no on-screen graphics, no lit LED curtain anywhere in this clip, no slow motion, no speed ramp, no cinematic grade, no lens flare, no confetti, no sparkles, no magic glow, no box floating, no box changing size, no second box.

AUDIO: natural room sound only — no music, no score, no background song. Soft indoor room tone, the dull thud of a heavy box landing on a cushion, the small click of magnets releasing, cardboard flexing, fabric rustling, one quiet delighted breath. No dialogue, no voice-over.

LOOK: real iPhone video, handheld, tack-sharp, candid UGC, warm domestic evening light. Slight sensor noise, no cinematic grade, no slow motion. No text overlay, no watermark, no captions, no logo.
````

### C03 — Mounting on the attached garage — close, side-on

**In the cut:** `starting_frames/v29_c03_g2.png` → `clips/v29_c03_g4.mp4`

#### Image prompt — `starting_frames/v29_c03_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `46b340e4-6caf-44c9-aa30-cc219dfe59a6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_202729_46b340e4-6caf-44c9-aa30-cc219dfe59a6.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_24_assets/starting_frames/v24_c03_g3.png` · Higgsfield media `9894c57e-8d7f-4754-9b39-357f18277863`
- @Image 2: `content/video_29_assets/starting_frames/v29_c03_g1.png` · Higgsfield media `169ef4c8-94f6-48cc-8693-ebf981b6262f`

````text
COPY THE CAMERA OF THE FIRST ATTACHED IMAGE EXACTLY - its position, its angle, its height, its closeness and her pose. This is a CLOSE, SIDE-ON shot, not the wide frontal shot.

THE CAMERA IS CLOSE AND OFF TO ONE SIDE, exactly as in the first image: the camera stands near the wall and slightly behind her at roughly waist height, looking ALONG the wall, so the wall runs away from the camera DIAGONALLY - nearest at the bottom-left of the frame and receding to the right, the roof gutter line along the top sloping down towards the right as it goes away, strong oblique one-point perspective. She fills most of the frame height in the right half, her whole body in shot from her boots on the stool up to her raised hands. MUCH CLOSER than a full-house shot: only a short run of the wall is in frame, no full facade, no wide establishing view, no flat square-on frontal view.

HER POSE - copy it from the first image: she stands on a small BLACK two-step folding step stool, seen from BEHIND and slightly to the side, facing the wall, both arms raised in front of her, her hands up at the trim board along the top of the wall as she presses the LED curtain into place. Her weight is on one foot, her back slightly arched.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Long vertical strands of thin BLACK cord with small DARK unlit bulbs hang down the wall to the left of her, and because the camera is close the strands are big in the frame and clearly readable as separate cords. A BIG LOOSE TANGLE of BLACK cord is heaped on the snow at the foot of the stool, spilling out to the left - a real messy nest of wire, obviously dark against the white snow, exactly like the bundle in the first image. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE HOUSE AND THE WOMAN - TAKE THEM FROM THE SECOND ATTACHED IMAGE, NOT FROM THE FIRST. It must read as LITERALLY THE SAME HOUSE and the SAME WOMAN as the second image, now seen close up from the side. The wall she is working on is the WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR of that house - soft WHITE with horizontal panel seams and recessed rectangular panels running away in perspective, and the row of small square windows across the top of the door visible at the far end. Around it the same WARM SAND-BEIGE lap siding with crisp WHITE trim, the same BLACK COACH LANTERN on the wall, the same WHITE gutter and WHITE downpipe, the same plain CONCRETE driveway under patchy snow. At the RIGHT of the frame, further away, the corner where the garage wing meets the MAIN HOUSE BODY is visible - the two-storey wall, the covered porch on white posts and the DARK RED front door - so it still reads as ONE house with the garage built into it. Same late-twenties woman with fair skin and COPPER-RED hair in a high ponytail spilling out from under a cream beanie, BURGUNDY puffer jacket, dark blue jeans, tan boots.

DO NOT COPY FROM THE FIRST IMAGE: not the dark slate-blue board-and-batten siding, not the shingled neighbouring house, not the brick wall, not the hedge, not her mustard-yellow jacket, not her dark curly hair, not her black trousers and not her white boots. The first image is there ONLY for the camera, the distance, the angle and the pose.

Daytime, overcast winter light, snow on the ground.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the door panels, the quilting of her jacket and every strand of black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v29_c03_g4.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `26b83e9c-176a-4c55-bf37-5096428cb0af`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_233048_26b83e9c-176a-4c55-bf37-5096428cb0af.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v29_c03_g4.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c03_g2.png` · Higgsfield media `ccd6c38b-e037-4721-bc00-cbdd0da159f1`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same overcast winter day, same WHITE SECTIONAL DOUBLE GARAGE DOOR filling the frame with its horizontal panel seams, its recessed rectangular panels and its row of small square windows across the top, same WARM SAND-BEIGE lap siding with crisp WHITE trim, same white trim board along the top of the garage door, same BLACK COACH LANTERN either side of the door, same gable with the round white louvre vent above it, same main house body continuing to the RIGHT with its covered front porch on white posts, its DARK RED front door and its two warm upstairs windows, same white gutter and white downpipe down the LEFT, same clipped boxwood hedge, same bare white birch at the left edge, same concrete driveway with patchy snow, same black folding step stool, same late-twenties woman with COPPER-RED hair in a high ponytail under a cream beanie, seen from behind in the BURGUNDY puffer jacket, dark blue jeans and tan boots, standing on the stool with both arms raised pinning the gathered fistful of unlit net up under the trim board, same LED net already hung flat across the door to her left, same loose tangled coil of curtain heaped on the snow at the foot of the stool.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she reaches at the speed an arm really reaches, she shakes the net out at the speed a heavy tangled net really swings, she shifts her weight at the speed a body really balances on a step stool. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in four seconds — one slow shake, one slow reach, one slow sideways press. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still mid-reach as the clip ends than that any part of it looks fast-forwarded.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH. Portrait, exactly the framing and the angle of the reference image, flat and frontal to the garage door, looking slightly up at it. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT. The garage door, the trim board, the house body at the right and the stool stay exactly the same size in frame from the first frame to the last, and the camera never swings round to an oblique or corner-on view of the door.

ONE SINGLE CONTINUOUS SHOT — NO CUTS. The whole four seconds is one unbroken take from one camera position. There is never a cut, never a jump, never a second angle, never a new scene, never a match cut, never a dissolve and never a reset. Every frame is a continuous in-between of the frame before it.

MOVEMENT RULE: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole four seconds — weight shifting on the stool, shoulders rolling, ribs breathing, the ponytail stirring, the burgundy puffer creasing and rustling, the strands swaying on after every touch. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses, and no limb ever travels faster than a real arm travels.

ACTION TIMELINE (4 seconds, one continuous take, no cuts) — ONLY TWO THINGS HAPPEN, AND BOTH ARE SLOW:
0.0-2.0s — she lifts the gathered bundle in her right hand and shakes it out ONCE, slowly and heavily. The shake takes well over a full second of screen time: her arm swings out and down, the tangled net lets go in stages rather than all at once, and a long sheet of black strands falls open down the white garage door and swings for a moment before it settles. The loose coil on the snow drags and shifts with it.
2.0-4.0s — still up on the stool, she stretches both arms high and presses the header wire up under the lip of the white trim board above the door, her thumbs working slowly along it, then walks her hands a short way sideways to her RIGHT along the trim board, onto the bare stretch of door beyond the strands she has already hung, pressing and tucking as she goes, her torso twisting and her heels lifting and dropping on the tread. She is STILL tucking when the clip ends. The curtain sways gently against the door and is still settling on the last frame.
THAT IS THE WHOLE CLIP. She does NOT step down off the stool, does NOT step back, does NOT plant her hands on her hips and does NOT tilt her head back to look at her work. There is no time for any of that at real speed, and cramming it in is exactly what would force the footage to look sped up. She stays on the stool from the first frame to the last.

THE LED CURTAIN IS BLACK — CRITICAL. The wire is BLACK, not white and not clear. Every vertical strand hanging down the garage door is a thin BLACK cord and the unlit bulbs on it are small and DARK. Against the white door the strands read as obvious thin dark lines, clearly visible the whole four seconds. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire appears at any moment.

HARD RULES: the curtain is COMPLETELY OFF the entire time — not one bulb lights, no glow, no colour, no animation on the door. The house never gains windows, doors or new features, the coach lanterns never move, the porch and the house body at the right never change and the driveway never changes. The strands are separate vertical strands obeying gravity, sagging slightly, with an uneven wavy bottom hem — never a flat sheet, never a panel, never a screen. The loose coil rests in the snow with real contact shadows. Her face is never shown; she stays turned away from camera throughout. No other people enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor winter ambience, thin plastic strands rattling and clicking against the metal garage door, a step-stool creak, boots on a metal tread, boots compressing snow, one quiet effortful breath. No voice.

LOOK: real iPhone UGC. Flat overcast winter daylight, slightly cool white balance, mild sensor noise, natural skin, no cinematic grade, no lens flare, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
````

**Other takes of C03 on disk (3)**

#### Image prompt — `starting_frames/v29_c03_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `169ef4c8-94f6-48cc-8693-ebf981b6262f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_201304_169ef4c8-94f6-48cc-8693-ebf981b6262f.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_28_assets/starting_frames/v28_c03_g1.png` · Higgsfield media `d4281baa-e62d-413c-b416-f7b09157d9fd`
- @Image 2: `content/video_29_assets/starting_frames/v29_c02_g1.png` · Higgsfield media `07ebb15c-1e14-4ef7-b576-b0f4210e0c5b`

````text
Same shot as the FIRST attached image - copy its camera, its framing and its staging EXACTLY. Daytime, overcast winter light, snow on the ground. A woman stands on a black folding step stool, seen from BEHIND, facing the wall, both arms raised in front of her, her hands up at the trim board above the garage door as she fixes the LED curtain to it. The big bundle of unlit LED curtain strands is heaped on the snow at the foot of the stool. The wide sectional DOUBLE GARAGE DOOR with horizontal panel seams, recessed rectangular panels and a row of small square windows across the top fills most of the frame behind her, and the curtain hangs DOWN OVER THE GARAGE DOOR ITSELF.

THE ONE BIG CHANGE - THIS IS NOT A DETACHED GARAGE ANY MORE. It is an ATTACHED GARAGE THAT IS PART OF A HOUSE: a single two-storey family home whose garage wing projects forward on the LEFT, with the MAIN HOUSE BODY clearly continuing to the RIGHT and set slightly back in the same building - two storeys tall, with a covered front porch on white posts, a DARK RED front door, and two upstairs windows with white frames and warm light inside. Above the garage door there is a gable with a round white louvre vent, and the roofline of the garage runs continuously into the roofline of the house. It must read unmistakably as ONE house with its garage built into it, NOT a separate garage building standing on its own in a yard. Do not leave empty sky or open yard where the house body should be.

THE CAMERA ANGLE IS FLAT AND FRONTAL, exactly as in the first image: the garage door faces the camera almost square-on and fills the frame, its horizontal seams run dead level and its vertical edges run straight up and down. The garage is NOT turned away at an angle, NOT receding steeply into the distance, NO strong oblique perspective, NO wide-angle corner view. The house body is visible along the right side of the frame in the same flat perspective.

THE HOUSE ITSELF - take it from this text only and NOT from the first attached image: WARM SAND-BEIGE lap siding with crisp WHITE trim; the garage door is soft WHITE with recessed panels and its row of small square windows; a BLACK COACH LANTERN with a lantern-shaped glass housing mounted either side of the garage door; the gutter along the roof edge and the downpipe are WHITE and the downpipe runs down the LEFT side; a plain CONCRETE driveway showing through patchy snow; a clipped boxwood hedge along the foot of the porch at the right; a bare white BIRCH tree at the left edge. Do NOT copy the navy board-and-batten, the cream door, the brass barn lights, the gravel driveway, the firewood stack or the spruce from the first image.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand hanging down the garage door is a thin BLACK cord with small DARK unlit bulbs on it, and against the white door the strands read as obvious thin dark lines. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - take her from the SECOND attached image: the same late-twenties woman with fair skin and COPPER-RED hair, here worn in a high ponytail spilling out from under a cream beanie. Outdoors she wears a BURGUNDY puffer jacket, dark blue jeans and tan boots. Same face, same hair colour, same person as in the second image.

IMAGE QUALITY - CRITICAL: a real iPhone photo, tack-sharp edge to edge, crisp fine detail in the siding boards, the door panels and the black cord, clean even overcast daylight with no blown-out white on the snow or the door and no crushed shadows, correct white balance, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v29_c03_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `42c92b58-a21c-4b41-8b9e-2a8b9effa8cd`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_223822_42c92b58-a21c-4b41-8b9e-2a8b9effa8cd.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c03_g2.png` · Higgsfield media `ccd6c38b-e037-4721-bc00-cbdd0da159f1`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — the same daytime overcast winter light, the same woman on the same black two-step folding stool seen from behind with her arms raised to the trim board above the garage door, the same wide white sectional double garage door with its horizontal panel seams and its row of small square windows across the top, the same warm sand-beige lap siding and white trim, the same attached-garage wing with the house body and the covered porch carrying on to the right, the same black coach lanterns, the same boxwood hedge, the same patchy snow on the concrete driveway, the same thin BLACK curtain strands already hanging down the door to her left, and the same heaped tangle of BLACK cord lying on the snow at the foot of the stool. Do not redraw the scene, do not restage it, do not re-light it, do not invent a different house, do not change the time of day and do not move the camera to a new position.

THE CORD IS A REAL PHYSICAL OBJECT AND ITS THICKNESS NEVER CHANGES. THIS IS THE MOST IMPORTANT RULE IN THIS CLIP. Every strand of this light curtain is a real black rubber-insulated cord about as thick as a shoelace, with small dark unlit bulbs moulded along it at regular spacing. That thickness is EXACTLY the same in the last frame as in the first frame, at the top of the door as at the bottom, in her hand as on the snow. A strand NEVER thins out, NEVER tapers, NEVER fades to a hairline, NEVER becomes a faint pencil line, NEVER becomes a scratch, NEVER dissolves, NEVER becomes semi-transparent and NEVER turns into a thin drawn line. If a strand ever looks thinner or fainter than it does in the reference image, THE CLIP HAS FAILED.

NOTHING MORPHS. The bundle of cord does NOT transform. It does not melt into lines, it does not unroll itself into a neat sheet, it does not reorganise into a pattern, it does not straighten itself out, and cord never appears out of nowhere. Cord that is in her hand stays in her hand until she lets it go, and then it FALLS as a physical tangle under gravity. Cord that is heaped on the snow STAYS a heaped tangle on the snow for the whole clip — it may drag a little and shift a little as the bundle above it pulls on it, but it never unwinds, never straightens, never flattens out and never becomes a set of lines. It stays an obvious messy black pile against the white snow from the first frame to the last.

NO GRID, NO MESH, NO NET, NO WIREFRAME. There are NO horizontal wires anywhere on the door. The only thing crossing the door horizontally is the single header cord along the trim board at the very top. Everything else hangs straight down as SEPARATE VERTICAL CORDS with wide dark gaps between them. The door must NEVER read as a net, a mesh, a screen, a grid, a fishnet, a wireframe, a scratched surface or a faint texture laid over the door. At every moment a viewer must be able to count the individual hanging cords.

HOW MUCH CURTAIN IS ON THE DOOR. In the reference image a section of strands is already hanging at the left of the door. Over the clip she adds ONE more section, roughly a quarter of the door's width, immediately beside the section already there. That is all. The door is NOT covered edge to edge by the end. Large areas of bare white door remain uncovered in the final frame. No strands ever appear on the right-hand part of the door, on the house siding, on the porch or anywhere she has not physically reached.

REAL TIME — NORMAL 1x SPEED. Everything she does happens at the pace a real person actually moves. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next. There is DELIBERATELY very little for her to do. If the action does not fit comfortably in four seconds, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still mid-tuck as the clip ends than that any part of it looks fast-forwarded.

HER FEET DO NOT MOVE. She stays standing on the same tread of the same stool from the first frame to the last. She does NOT step down, does NOT step up, does NOT walk, does NOT climb, does NOT jump, does NOT balance along anything and does NOT shift from one tread to the other. Only her arms, shoulders, torso and head move. Her heels may lift and drop slightly on the tread as she stretches, and that is all.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH. A friend is filming handheld from the same spot. Small natural breathing drift and a tiny weight shift only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO PAN to a new part of the house. The garage door and the house stay exactly the same size in frame from the first frame to the last. No cuts.

ACTION TIMELINE (4 seconds, one continuous take, no cuts) — ONLY TWO THINGS HAPPEN, AND BOTH ARE SLOW:
0.0-2.0s — she lifts the gathered bundle in her right hand and shakes it out ONCE, slowly and heavily. The shake takes well over a full second of screen time: her arm swings out and down, and the tangle lets go IN STAGES, a few thick cords at a time, each one dropping as a heavy black line of the same thickness it had in the bundle, swinging like a skipping rope before it hangs still. You can see individual bulbs on each falling cord. It is NOT a sheet unfurling and NOT a curtain unrolling — it is a knot of heavy cord coming loose a few strands at a time. The heap on the snow drags and shifts a little as this happens but stays a heap.
2.0-4.0s — still up on the stool, she stretches both arms high and presses the header wire up under the trim board directly above the garage door, her thumbs working slowly along it, then walks her hands a short way sideways along the header, onto the bare stretch of door beyond the strands she has already hung, pressing and tucking as she goes, her torso twisting and her heels lifting and dropping on the tread. She is STILL tucking when the clip ends. The hanging cords sway gently against the door and are still settling on the last frame.

THAT IS THE WHOLE CLIP. She does NOT step down off the stool, does NOT step back, does NOT plant her hands on her hips and does NOT tilt her head back to look at her work. She stays on the stool from the first frame to the last.

MOVEMENT RULE: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole four seconds — weight shifting, shoulders rolling, the copper ponytail swinging and settling, the puffer jacket creasing and the nylon catching the light, breath fogging faintly in the cold — but every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters and never stutters between poses.

THE LED CURTAIN IS BLACK — CRITICAL AND TRUE IN EVERY FRAME: the wire is BLACK, not white and not clear and not grey. Against the white door every strand reads as an OBVIOUS SOLID DARK LINE with clearly visible dark bulbs on it — high contrast, easy to see, never faint, never washed out, never pale, never blending into the door. The heap on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire, no copper wire anywhere at any moment.

THE LIGHTS ARE COMPLETELY OFF for the entire clip. No glow, no flicker, no bulb ever lights, no warm halo, no colour, no twinkle. Nothing switches on.

THE CURTAIN IS SEPARATE HANGING STRANDS, never a solid sheet, never a mesh panel, never a screen. The strands hang as distinct vertical lines obeying gravity, with visible dark gaps between them and the white door plainly visible through those gaps, with a slight natural sag and an UNEVEN WAVY BOTTOM HEM — not a ruler-straight line. Their bottom ends hang loose and free and some of them trail down onto the driveway.

HARD RULES: her face is never shown and she never turns toward the camera. No second person, no pets, no cars driving past, no falling snow, no wind gusts, no text overlay, no captions, no subtitles, no watermark, no logo bug, no on-screen graphics, no slow motion, no speed ramp, no cinematic grade, no lens flare, no sparkles, no magic glow, no time of day change, no sudden sunset.

AUDIO: natural outdoor sound only — no music, no score, no background song. Cold still winter air, the light plastic rattle and clatter of a bundle of light strands shaking loose, cord slapping softly against a metal garage door, boots creaking on a metal stool tread, nylon jacket rustling, one quiet breath. No voice, no dialogue, no commentary.

LOOK: real iPhone daytime video, handheld, tack-sharp, candid UGC, flat overcast winter light. Crisp fine detail in the siding boards, the door panels and the black cord. Slight sensor noise, no cinematic grade, no slow motion. No text overlay, no watermark, no captions, no logo.
````

#### Video prompt — `clips/v29_c03_g3.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `915bd806-87c3-465f-b8c6-d2735845cf71`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_230048_915bd806-87c3-465f-b8c6-d2735845cf71.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c03_g2.png` · Higgsfield media `ccd6c38b-e037-4721-bc00-cbdd0da159f1`

````text
ONE SINGLE CONTINUOUS SHOT. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT AND IT OUTRANKS EVERYTHING BELOW. The whole four seconds is ONE unbroken take from ONE fixed camera position. There is NO CUT, NO SECOND SHOT, NO SECOND SCENE, NO ANGLE CHANGE, NO JUMP CUT, NO MATCH CUT, NO REFRAME, NO CROSSFADE, NO DISSOLVE, NO WIPE, NO TRANSITION OF ANY KIND at any point. The camera never repositions, never changes its distance from the house and never changes its lens. Nothing in the frame is ever allowed to change state instantly between two frames. If you are tempted to cut to a second view or to skip forward in time, DO NOT — hold the single shot and let less happen instead.

Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same overcast winter day, same two-storey family home with the ATTACHED GARAGE WING projecting forward on the LEFT and the main house body continuing to the RIGHT, same WARM SAND-BEIGE lap siding with crisp WHITE trim, same soft WHITE sectional double garage door with its horizontal panel seams and its row of small square windows across the top, same white gutter and white downpipe, same black coach lantern, same covered front porch on white posts with the DARK RED front door at the right, same clipped boxwood hedge at the right, same concrete driveway with patchy snow, same black folding step stool, same woman seen from behind with COPPER-RED hair in a high ponytail spilling out from under a cream beanie, wearing a BURGUNDY puffer jacket, dark blue jeans and tan boots, standing on the stool with both arms raised pressing the header of the curtain up against the trim board above the garage door, same LED curtain already hanging down the garage door to her LEFT, same loose tangled coil of black curtain heaped on the snow at the foot of the stool.

THE AMOUNT OF CURTAIN ON THE DOOR NEVER CHANGES. THIS IS THE SECOND MOST IMPORTANT RULE. In the reference image a stretch of curtain is ALREADY hung across the garage door and a loose tangled heap of cord is ALREADY lying on the snow at the foot of the stool. That is exactly how it looks in the FIRST frame and that is exactly how it looks in the LAST frame. She is pressing and tucking strands that are ALREADY HANGING. The door does NOT start bare and become covered. No new sheet of curtain appears. No extra section is added. No section disappears. The heap on the snow stays a heap of roughly the same size and never unrolls, never shrinks and never vanishes. She is NOT holding a big loose bundle in her raised hands — her hands are flat and empty against the trim board, working the header wire that is already fixed there. At no single frame is there suddenly more curtain on the door than there was in the frame before.

REAL TIME — NORMAL 1x SPEED. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she reaches at the speed an arm really reaches, she shifts her weight at the speed a body really balances on a step stool. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in four seconds — one slow press, one slow sideways walk of the hands. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up and never cut to get through it. It is far better that she is still mid-reach as the clip ends than that any part of it looks fast-forwarded or edited.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH. Portrait, exactly the framing and the angle of the reference image, looking slightly up at the garage door. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO PAN, NO TILT. The garage door, the porch, the boxwood hedge and the step stool stay exactly the same size and in exactly the same place in frame from the first frame to the last, and the camera never swings round to an oblique or corner-on view.

MOVEMENT RULE: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole four seconds — weight shifting on the stool, shoulders rolling, ribs breathing, the copper ponytail swinging and settling, the burgundy puffer creasing and rustling, the strands swaying on after every touch. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses, and no limb ever travels faster than a real arm travels.

ACTION TIMELINE (4 seconds, ONE continuous take, NO cuts) — ONLY TWO THINGS HAPPEN AND BOTH ARE SLOW:
0.0-2.0s — up on the stool she stretches both arms high and presses the header wire firmly up under the lip of the white trim board above the garage door, her thumbs working slowly along it, pressing and tucking, her heels lifting and dropping on the tread as she balances. The hanging strands below her hands sway gently against the white door and settle.
2.0-4.0s — still on the stool, she walks her hands a short way sideways to her RIGHT along the trim board, pressing and tucking as she goes, her torso twisting and her shoulders rolling with the reach. She is STILL tucking when the clip ends. The curtain sways gently against the door and is still settling on the last frame.
THAT IS THE WHOLE CLIP. She does NOT step down off the stool, does NOT step back, does NOT plant her hands on her hips, does NOT turn round and does NOT tilt her head back to look at her work. She stays on the stool from the first frame to the last. There is no time for anything else at real speed, and cramming more in is exactly what would force a cut.

THE CORD IS A REAL PHYSICAL OBJECT AND ITS THICKNESS NEVER CHANGES. Every vertical strand hanging down the garage door is a real thin BLACK cord about as thick as a shoelace, with small DARK unlit bulbs strung along it. It has exactly the same thickness in the last frame as in the first. The strands NEVER thin out, NEVER taper, NEVER fade to faint grey hairlines, NEVER become pencil lines, NEVER dissolve, NEVER go semi-transparent and NEVER turn into a scratchy drawn texture. Against the white garage door they read as obvious solid dark lines you could reach out and grab, the whole four seconds.

NO GRID, NO MESH, NO NET, NO WIREFRAME. The curtain is a set of SEPARATE hanging vertical cords with clear gaps between them, and the white garage door is plainly visible through those gaps. There are no horizontal wires at all except the single header cord along the trim board. A viewer must be able to count the individual hanging cords at every instant. It is never a flat sheet, never a panel, never a screen, never a net and never a wireframe.

THE LED CURTAIN IS BLACK — CRITICAL. The wire is BLACK, not white and not clear. The heaped coil on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire appears at any moment.

HARD RULES: the curtain is COMPLETELY OFF the entire time — not one bulb lights, no glow, no colour, no animation on the door. The house never gains or loses windows, doors or features, the garage door panel seams stay dead level, the coach lantern never moves and the boxwood hedge never changes. The strands obey gravity, sagging slightly, with an uneven wavy bottom hem. The loose coil rests in the snow with real contact shadows. Her face is never shown; she stays turned away from camera throughout. No other people enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor winter ambience, thin plastic strands rattling and clicking against the metal garage door, a step-stool creak, boots on a metal tread, one quiet effortful breath. No voice.

LOOK: real iPhone UGC. Flat overcast winter daylight, slightly cool white balance, mild sensor noise, natural skin, no cinematic grade, no lens flare, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last, as ONE unbroken shot.
````

### C04 — Phone POV, the same house at night — whole door

**In the cut:** `starting_frames/v29_c04_g5.png`, `references/v29_c04_r1.png` → `clips/v29_c04_g7.mp4`

#### Image prompt — `starting_frames/v29_c04_g5.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `da8d1a05-5120-4508-96dc-c55f9c491d16`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_205200_da8d1a05-5120-4508-96dc-c55f9c491d16.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g4.png` · Higgsfield media `47ab5ef5-d6af-455c-b06c-fba3cc3025de`
- @Image 2: `content/video_29_assets/starting_frames/v29_c04_g2.png` · Higgsfield media `74f96513-1d68-4eaa-9df1-a61c1942df84`

````text
Same shot as the FIRST attached image. Copy its camera, its framing, its distance, its angle, its lighting, its house, its garage door, its curtain and the position, size and grip of the phone in the foreground EXACTLY. ONE THING CHANGES: the layout of the app on the phone screen.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. Square-on frontal view of the double garage door at night, the camera close to the house so the garage bay dominates the frame, and the ENTIRE garage door inside the picture with a little breathing room around it: both vertical side edges of the door in frame with white trim and siding visible beyond them on each side, the complete top edge in frame including the whole row of small square windows running across it, and the bottom edge where the door meets the concrete driveway in frame too. Nothing about the door cut off by any edge. Do NOT step closer and do NOT step further back. NO whole house, NO full two-storey facade, NO roofline, NO establishing shot from the end of the driveway. The door faces the camera flat, its horizontal panel seams dead level and its vertical edges straight up and down - NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up. Ignore the framing of the SECOND attached image completely - it is cropped too tight and it is here ONLY for its phone screen.

Everything around the door stays exactly as in the first image: the lap siding and white trim either side of the door, the black coach lanterns glowing warm on the wall, the sliver of the covered porch and dark front door cropped at the right edge, the concrete driveway with patchy snow across the bottom, the night sky, the same warm lantern light and street-lamp spill. The LED curtain stays fully mounted, hanging in evenly spaced vertical see-through BLACK strands with small dark unlit bulbs across the full width of the door, lights OFF, the door panels plainly visible through the gaps between strands.

THE ONE CHANGE - THE APP SCREEN LAYOUT. The first image has far too many panels: a dense grid of many tiny icons crammed across the screen. That is WRONG. Use the layout of the SECOND attached image's screen instead, which has FEWER and MUCH BIGGER panels.

EXACTLY WHAT THE SCREEN MUST SHOW: a dark navy-blue app screen carrying a grid of just TWO COLUMNS of large tiles - two tiles across the width of the screen, about five tiles down, so roughly TEN tiles in total and no more. Each tile is BIG - nearly half the width of the screen - with softly rounded corners and only a narrow gutter between it and its neighbour. Each tile is a small PHOTOGRAPH of a real house decorated in Christmas lights: a snow-covered roofline picked out in icy white and blue lights, a lit nativity scene, a glowing snowman, a reindeer outline in lights, a porch draped in blue and white light curtains. The palette across the grid is mostly ICY BLUE and cool WHITE with a couple of warm amber and red-green tiles mixed in. ONE tile is selected and is ringed with a bright electric-blue outline. Near the BOTTOM of the screen, below the grid, sits a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE pointing right in the middle of it.

ABSOLUTELY NOT on the screen: no dense grid of tiny icons, no three, four, five or six columns, no rows of little symbols or pictograms, no snowflake or Christmas-tree glyphs, no app-icon look. Only TWO COLUMNS of big photographic tiles. And NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

RENDER THAT SCREEN TACK-SHARP: crisp clean tile edges, perfectly aligned columns and rows, each photograph inside its tile clearly readable, the selection ring a clean bright outline and the play button a solid even circle with a crisp white triangle. In perfect focus, high contrast, no mush, no smearing, no blur, no moire, no warped or melted tiles. The screen glows and throws its light up onto the fingers and the palm, and it is the brightest thing in the foreground.

THE PHONE ITSELF IS UNCHANGED - same handset, same hand, same grip, same angle, same size and position in the bottom-centre foreground as in the first image. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `references/v29_c04_r1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `e6ce481d-4efe-4398-81b6-56f0958caa61`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_234352_e6ce481d-4efe-4398-81b6-56f0958caa61.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g7.png` · Higgsfield media `e128771f-0b9b-4145-aa16-e6e71f5ca6f3`
- @Image 2: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `40058517-9846-48c1-88e3-d48519a63b52`

````text
THE FIRST ATTACHED IMAGE IS THE SCENE AND IT MUST NOT CHANGE. THE SECOND ATTACHED IMAGE IS A STYLE SWATCH ONLY.

THE HOUSE IS NOT ALLOWED TO CHANGE - THIS IS THE MOST IMPORTANT INSTRUCTION. It must read as LITERALLY THE SAME GARAGE, photographed from the same spot a moment later. Identical PALE CREAM LAP SIDING with its fine horizontal board lines - not brick, not stone, not board-and-batten, not stucco, not shingle, not green, not grey. Identical SOFT WHITE SECTIONAL DOUBLE GARAGE DOOR, the same pale off-white colour, the same wide recessed rectangular panels, the same horizontal seams in the same places, and across the top the same row of small square windows in the SAME FOUR GROUPS OF FOUR with the same spacing. Identical crisp WHITE TRIM boards framing the door and the same white surround. Identical TWO BLACK COACH LANTERNS, one on the wall either side of the door at the same height, glowing the same warm amber. Identical snowy concrete driveway with the same tyre tracks. Identical night sky and the same cool ambient light. Do NOT restyle the door, do NOT change its proportions, do NOT change its colour, do NOT re-texture the siding, do NOT move the lanterns, do NOT add windows or trim or brickwork that is not already there.

THE SECOND ATTACHED IMAGE IS FOR ONE THING ONLY: how a cartoon is drawn out of small round lit bulbs strung on a curtain. DO NOT TAKE ANYTHING ELSE FROM IT - not its brick wall, not its gable, not its snowman, not its truck, not its street, not its wet road, not its mostly-white palette, not its camera position. Style of the bulbs only.

THREE THINGS CHANGE FROM THE FIRST IMAGE:

1. THE HAND AND THE PHONE ARE GONE. There is nothing at all in the foreground. No hand, no arm, no sleeve, no phone, no screen, no glow from a screen. The bottom of the frame is simply the empty snowy driveway. The whole garage door is completely unobstructed from edge to edge.

2. THE CAMERA HAS TILTED UP A LITTLE - IT HAS NOT MOVED. This is a handheld iPhone shot and the person filming has tipped the phone up slightly so the lights fill the frame. The camera stays in exactly the same place at exactly the same distance: the garage door must be exactly the same SIZE in the picture as it is in the first image, spanning almost the full width with only a narrow strip of trim and siding beyond each side edge. Do NOT step back, do NOT step closer, do NOT zoom out, do NOT add more siding to the left or right. Only the vertical framing shifts: there is now just a THIN sliver of driveway along the bottom edge and a slightly deeper band of siding above the top of the door. Still square-on from the front - the panel seams run dead level and the door edges run straight up and down. The ENTIRE door stays inside the frame: both side edges, the complete top edge with the whole row of square windows end to end, and the bottom edge where the door meets the driveway.

3. THE LED CURTAIN IS SWITCHED ON AND SHOWING A BRIGHT CARTOON ANIMATION. The same dense curtain of closely spaced vertical strands hanging over the garage door, but now every bulb is lit and together they draw a picture.

THE PICTURE - THE RUNAWAY SLEIGH, drawn chunky and simple out of the bulbs, running RIGHT ACROSS THE WHOLE GARAGE DOOR from left to right: FOUR REINDEER stretched out flat in a full-tilt gallop fill the left and centre of the door, legs kicked straight out fore and aft, antlers back, tongues out, eyes as wide white circles, the lead reindeer looking back over his shoulder in alarm. Behind them at the RIGHT the SLEIGH is tipped up on one runner, skidding at a steep angle, a fan of snow spraying off the runner. SANTA has been thrown half out of the seat and clings on by ONE HAND, body streaming horizontally behind the sleigh, legs kicking in the air, mouth wide open in a big round O, his red hat already blown off and tumbling away. Curved speed lines and dotted trajectory arcs trail the whole team. PRESENTS bounce out of the back of the sleigh, seven or eight of them, each a DIFFERENT BRIGHT COLOUR - emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow, two burst open. Small gold stars scattered through the gaps. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

THE PICTURE FILLS THE ENTIRE GARAGE DOOR: the team spans the FULL WIDTH of the door from its left edge to its right edge, and the reindeer plus the sleigh plus the bouncing presents plus the stars fill the FULL HEIGHT of the door from just under the row of square windows down to the bottom edge. Every part of the door is covered by lit artwork - no large dark empty areas anywhere on the door, and nothing is confined to a small panel in the middle. Nothing lit appears above the door, on the trim, on the siding, on the lanterns or in the sky.

COLOUR IS THE POINT: this is a loud multicoloured light show, not a mostly-white one - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all clearly present and clearly separated.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. The strands are densely spaced but there are still clear DARK GAPS between them and the white garage door behind is plainly visible through those gaps, especially in the unlit areas - the recessed panel seams and the row of square windows must still read through the curtain. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the cream lap siding, the garage door panels and the snowy driveway clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v29_c04_g7.mp4` — IN THE CUT

No Higgsfield video job matches this file byte-for-byte (re-encoded copy, recovered from an export, or older than the history).

**Other takes of C04 on disk (11)**

#### Image prompt — `starting_frames/v29_c04_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `271193cf-e71e-4035-8a7d-9eb0dd0f53ec`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_201424_271193cf-e71e-4035-8a7d-9eb0dd0f53ec.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_28_assets/starting_frames/v28_c04_g1.png` · Higgsfield media `a734b552-ed83-4ab2-84c6-e9b3d4d1d833`
- @Image 2: `content/video_29_assets/starting_frames/v29_c03_g1.png` · Higgsfield media `169ef4c8-94f6-48cc-8693-ebf981b6262f`

````text
Same shot as the FIRST attached image - copy its staging, its camera distance and its content EXACTLY. Night. The camera is a long way back so the WHOLE building is in frame, complete and large, with the LED curtain hanging down the garage door and a hand holding a phone up big in the bottom-centre foreground.

THE PHONE - COPY IT EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same size in frame, same position at the bottom centre, same hand, same grip, same angle. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline. Pulling the camera back must NOT shrink this phone; it stays big in the foreground.

THE SCREEN SHOWS THE SAME APP as the first image: a dark navy-blue app screen filled with a neat grid of small square scene thumbnails, each one a tiny colourful Christmas light picture on a dark background, one of them ringed with a bright highlight, and a BIG ROUND BLUE PLAY BUTTON centred near the bottom of the screen. The screen glows and throws its light up onto the fingers and the palm. NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is just the grid of thumbnails and the round play button.

THE BUILDING - TAKE IT FROM THE SECOND ATTACHED IMAGE. It must read as LITERALLY THE SAME HOUSE, the same property and the same street as the second image, now at night and seen whole from much further back: the SAME two-storey family home with its ATTACHED GARAGE WING projecting forward on the LEFT and the MAIN HOUSE BODY continuing to the RIGHT and set slightly back in the same building, the same WARM SAND-BEIGE lap siding with WHITE trim, the same soft WHITE sectional double garage door with its panel seams and its row of small square windows across the top, the same gable with the round white louvre vent above the garage, the same covered front porch on white posts with the DARK RED front door, the same two upstairs windows with white frames glowing warm inside, the same BLACK COACH LANTERN either side of the garage door, the same WHITE gutter and WHITE downpipe on the LEFT, the same CONCRETE driveway with patchy snow, the same clipped boxwood hedge at the foot of the porch and the same bare white BIRCH at the left edge. Do NOT copy the house, the siding, the door colour, the lamps or the driveway from the first image.

THE CAMERA - A DIFFERENT, WIDER ANGLE THAN THE SECOND IMAGE BUT STILL FROM THE FRONT: pulled right back and standing square on to the front of the house from the end of the driveway, so the garage wing AND the whole house body, the porch and the roofline are all inside the frame with room around them. The facade faces the camera flat, the horizontal lines run dead level and the vertical edges run straight up and down. NOT turned away at an angle, NOT receding into the distance, NO strong oblique perspective, NO corner view, NOT a low worm's-eye tilt looking up.

THE LED CURTAIN IS ALREADY FULLY MOUNTED AND IT IS BLACK - CRITICAL: it hangs from the trim board above the garage door in evenly spaced vertical see-through strands, down across the full width of the door, with slight natural sag and an uneven bottom hem. The wire is BLACK, not white and not clear, every strand a thin BLACK cord with small DARK unlit bulbs on it, no glow. Against the white door the strands read as clear thin dark vertical lines. No white wire, no clear wire, no silver wire anywhere.

Lighting: the two black coach lanterns glowing warm either side of the garage door, the porch light on, the upstairs windows warm, a street lamp glow from the left, snow on the driveway catching the light.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved and the whole facade in focus, the siding boards and the door panels clearly readable, correct exposure with no blown-out highlights around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `starting_frames/v29_c04_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `74f96513-1d68-4eaa-9df1-a61c1942df84`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_202917_74f96513-1d68-4eaa-9df1-a61c1942df84.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g1.png` · Higgsfield media `271193cf-e71e-4035-8a7d-9eb0dd0f53ec`
- @Image 2: `content/video_29_assets/starting_frames/v29_c03_g2.png` · Higgsfield media `46b340e4-6caf-44c9-aa30-cc219dfe59a6`

````text
Same shot as the FIRST attached image - same night, same house, same phone held up in the bottom-centre foreground, same app on the screen. ONE THING CHANGES: THE CAMERA IS MUCH, MUCH CLOSER.

THE NEW FRAMING - THIS IS THE WHOLE POINT: step right up to the house, close enough that the SECOND attached image's distance is the reference. Even a little CLOSER than the second image. The WIDE WHITE SECTIONAL DOUBLE GARAGE DOOR with the LED curtain hanging down it FILLS THE FRAME - the curtain strands and the door panels run from the top of the frame to the bottom and from edge to edge. We are near enough to read every panel seam, every recessed panel and every individual bulb on the cord. NO full facade, NO whole house, NO roofline, NO establishing shot, NO wide view from the end of the driveway. Only the garage bay and a narrow sliver of what is immediately beside it is in frame.

STILL SHOT FROM THE FRONT, not from the side: the garage door faces the camera square-on and flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. Do not turn it away at an angle and do not use the oblique receding perspective of the second image - take only the CLOSENESS from the second image, not its side angle.

WHAT STAYS IN FRAME AROUND THE DOOR: just the edge of the WARM SAND-BEIGE lap siding and the WHITE trim down one side, ONE BLACK COACH LANTERN glowing warm beside the door, and at the far right edge a small slice of the covered porch with its white post and the DARK RED front door, cropped by the frame. The concrete driveway with patchy snow across the very bottom.

THE PHONE - COPY IT EXACTLY FROM THE FIRST ATTACHED IMAGE. Same handset, same hand, same grip, same angle, held up big in the bottom-centre foreground. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

THE SCREEN SHOWS THE SAME APP as the first image: a dark navy-blue app screen filled with a neat grid of small square scene thumbnails, each one a tiny colourful Christmas light picture on a dark background, one of them ringed with a bright highlight, and a BIG ROUND BLUE PLAY BUTTON centred near the bottom of the screen. The screen glows and throws its light up onto the fingers and the palm. NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is just the grid of thumbnails and the round play button.

THE LED CURTAIN IS FULLY MOUNTED AND IT IS BLACK - CRITICAL: it hangs from the trim board above the garage door in evenly spaced vertical see-through strands, down across the full width of the door, with slight natural sag and an uneven bottom hem. The wire is BLACK, not white and not clear, every strand a thin BLACK cord with small DARK unlit bulbs on it, no glow. Against the white door the strands read as clear thin dark vertical lines, and at this close range each strand is thick and obvious in the frame. No white wire, no clear wire, no silver wire anywhere.

THE HOUSE MUST BE THE SAME HOUSE as both attached images - same warm sand-beige lap siding, same white trim, same soft white sectional door with its recessed panels and its row of small square windows across the top, same black coach lantern, same white gutter, same concrete driveway.

Lighting: night, the coach lantern glowing warm beside the door, a street lamp glow spilling in from one side, snow on the driveway catching the light, the phone screen the brightest thing in the foreground.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the garage door behind it equally in focus, the panel seams and the black cord clearly readable, correct exposure with no blown-out highlight around the lantern and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `starting_frames/v29_c04_g3.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `7da86a25-4fc3-4f5a-b61c-17d596c8f6ac`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_203725_7da86a25-4fc3-4f5a-b61c-17d596c8f6ac.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g2.png` · Higgsfield media `74f96513-1d68-4eaa-9df1-a61c1942df84`
- @Image 2: `content/video_29_assets/starting_frames/v29_c04_g1.png` · Higgsfield media `271193cf-e71e-4035-8a7d-9eb0dd0f53ec`

````text
Same shot as the FIRST attached image - same night, same house, same square-on frontal angle, same phone held up big in the bottom-centre foreground. TWO THINGS CHANGE: the camera steps back a little, and the app on the screen is drawn much more clearly.

CHANGE 1 - THE ENTIRE GARAGE DOOR MUST BE VISIBLE. The first image is cropped too tight and cuts the door off. Step the camera BACK just far enough that the WHOLE double garage door fits inside the frame with a little breathing room around it: BOTH vertical side edges of the door are inside the frame with siding visible beyond them on each side, the COMPLETE top edge of the door is in frame including the entire row of small square windows running all the way across it, and the BOTTOM edge where the door meets the concrete driveway is in frame too. Nothing about the door is cut off by any edge of the picture. Step back ONLY this far - this is still a CLOSE shot of the garage bay, MUCH closer than a full-facade view: NO whole house, NO full two-storey facade, NO roofline, NO establishing shot from the end of the driveway. The garage door is still the dominant object and fills most of the frame.

STILL SHOT SQUARE-ON FROM THE FRONT: the garage door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low worm's-eye tilt.

WHAT IS AROUND THE DOOR: a strip of WARM SAND-BEIGE lap siding with crisp WHITE trim down each side of the door and a band of it above - the siding is a clear WARM SANDY BEIGE, NOT white, NOT cream, NOT grey, and it must read visibly warmer and darker than the soft white of the garage door so the two are obviously different colours. ONE BLACK COACH LANTERN glowing warm on the siding beside the door. At the far right edge a small slice of the covered porch with its white post and the DARK RED front door, cropped by the frame. The concrete driveway with patchy snow across the bottom.

CHANGE 2 - THE APP SCREEN, DRAWN MUCH MORE CLEARLY AND CLEANLY. Same app idea as both attached images but rendered sharp, bold and easy to read at a glance instead of a mushy grid of tiny tiles. The screen is a deep NAVY-BLUE app background. On it: a neat grid of exactly NINE large square scene tiles, three across and three down, generously spaced apart with clear dark gutters between them and soft rounded corners on every tile. Each tile is a small crisp picture of a differently coloured Christmas light pattern on a dark background - one warm white, one red-and-green, one icy blue, one multicolour, one purple-and-pink, and so on - each one a distinct saturated colour so the grid reads as a colourful, clearly organised palette of scenes. ONE tile is selected and is ringed with a bright, obvious 3-pixel electric-blue border and a soft glow. Below the grid, centred, a BIG ROUND SOLID BRIGHT-BLUE PLAY BUTTON, large and unmistakable, with a clean WHITE TRIANGLE pointing right in the middle of it, crisp edges, no blur. Above the grid a simple empty header bar. EVERY element on the screen is tack-sharp, high contrast and cleanly separated - no mush, no smearing, no tiny illegible clutter. ABSOLUTELY NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is only the header bar, the nine picture tiles and the round play button. The screen glows and throws its light up onto the fingers and the palm.

THE PHONE - COPY IT EXACTLY FROM THE SECOND ATTACHED IMAGE. Same handset, same hand, same grip, same angle, held up big in the bottom-centre foreground, roughly the same size in frame as in the first image. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK - CRITICAL, AND THE FIRST IMAGE GETS THIS WRONG. In the first image the strands came out pale and washed out against the white door. They must be BLACK. The curtain hangs from the trim board above the garage door in evenly spaced vertical see-through strands, right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the soft white garage door each strand must read as a CLEARLY DARK, high-contrast vertical line, obviously black, easy to trace from top to bottom. NO white wire, NO clear wire, NO silver wire, NO pale grey wire anywhere. There are clear gaps between the strands and the door panels are plainly visible through them - it is a hanging curtain of separate strands, never a solid panel or a mesh screen.

THE HOUSE MUST BE THE SAME HOUSE as both attached images - same warm sand-beige lap siding, same white trim, same soft white sectional door with its recessed panels and its row of small square windows across the top, same black coach lantern, same white gutter, same concrete driveway.

Lighting: night, the coach lantern glowing warm beside the door, a street lamp glow spilling in from one side, snow on the driveway catching the light, the phone screen the brightest thing in the foreground.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lantern and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `starting_frames/v29_c04_g4.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `47ab5ef5-d6af-455c-b06c-fba3cc3025de`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_204332_47ab5ef5-d6af-455c-b06c-fba3cc3025de.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g3.png` · Higgsfield media `7da86a25-4fc3-4f5a-b61c-17d596c8f6ac`
- @Image 2: `content/video_29_assets/starting_frames/v29_c04_g1.png` · Higgsfield media `271193cf-e71e-4035-8a7d-9eb0dd0f53ec`

````text
Same shot as the FIRST attached image. Copy its camera, its framing, its distance, its angle, its lighting, its house and the position and size of the phone in the foreground EXACTLY. ONE THING CHANGES: the app on the phone screen goes back to the design in the SECOND attached image, just drawn much sharper.

THE FRAMING IS ALREADY CORRECT IN THE FIRST IMAGE - DO NOT CHANGE IT. Square-on frontal view of the double garage door at night, the camera close to the house so the garage bay dominates the frame, and the ENTIRE garage door inside the picture with a little breathing room around it: both vertical side edges of the door in frame with white trim and siding visible beyond them on each side, the complete top edge in frame including the whole row of small square windows running across it, and the bottom edge where the door meets the concrete driveway in frame too. Nothing about the door cut off by any edge. Do NOT step closer and do NOT step further back. NO whole house, NO full two-storey facade, NO roofline, NO establishing shot from the end of the driveway. The door faces the camera flat, its horizontal panel seams dead level and its vertical edges straight up and down - NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up.

Everything around the door stays exactly as in the first image: the lap siding and white trim either side of the door, the black coach lanterns glowing warm on the wall, the sliver of the covered porch and dark front door cropped at the right edge, the concrete driveway with patchy snow across the bottom, the night sky, the same warm lantern light and street-lamp spill.

THE ONE CHANGE - THE APP SCREEN. Discard the nine big square tiles on the phone in the first image. Instead put back the app design from the SECOND attached image, exactly that layout: a dark NAVY-BLUE app screen filled with a DENSE grid of MANY SMALL square scene thumbnails packed close together in even rows and columns, each thumbnail a tiny picture of a differently coloured Christmas light pattern on a dark background, ONE of them ringed with a bright highlight border, and a BIG ROUND BLUE PLAY BUTTON centred near the bottom of the screen below the grid. Same number of thumbnails, same small size, same dense packing, same overall layout and proportions as the second image.

RENDER THAT SCREEN MUCH SHARPER AND CLEANER THAN THE SECOND IMAGE - this is the whole point of the change. Every thumbnail has crisp clean edges and neat even gutters between it and its neighbours, perfectly aligned rows and columns, and a clearly readable little light pattern inside it in a distinct saturated colour. The highlighted thumbnail's ring is a clean bright electric-blue outline, not a smear. The round play button is a solid, evenly circular bright blue disc with a clean WHITE TRIANGLE pointing right in the middle of it, crisp edges. The screen is in perfect focus, high contrast, no mush, no smearing, no blur, no moire, no warped or melted tiles. ABSOLUTELY NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen - the UI is only the grid of picture thumbnails and the round play button. The screen glows and throws its light up onto the fingers and the palm.

THE PHONE ITSELF IS UNCHANGED - same handset, same hand, same grip, same angle, same size and position in the bottom-centre foreground as in the first image. It is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the garage door in evenly spaced vertical see-through strands, right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale garage door each strand must read as a clearly dark, high-contrast vertical line, obviously black and easy to trace from top to bottom. NO white wire, NO clear wire, NO silver wire, NO pale grey wire anywhere. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `starting_frames/v29_c04_g6.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `a6bcff66-91f5-4629-be28-3ba99b78c3a7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_205622_a6bcff66-91f5-4629-be28-3ba99b78c3a7.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g5.png` · Higgsfield media `da8d1a05-5120-4508-96dc-c55f9c491d16`

````text
Same shot as the attached image - same night, same house, same square-on frontal angle, same garage door, same curtain, same lanterns, same phone, same hand, same app screen. ONE THING CHANGES: THE GARAGE DOOR IS BIGGER IN THE FRAME.

THE CHANGE - PUSH IN SO THE GARAGE DOOR IS MUCH BIGGER. In the attached image the door sits too small with too much empty space around it. Move the camera closer to the house so the door grows to fill the picture: the door must now span almost the FULL WIDTH of the frame, with only a NARROW STRIP of white trim and siding left visible beyond its left edge and beyond its right edge, and only a SHALLOW BAND of siding above its top edge. Cut down the empty driveway at the bottom so only a low strip of snowy concrete remains under the door. The garage door should be by far the dominant object in the picture, big and imposing, reading at the same large scale as the wall does in the daytime install shot.

BUT THE ENTIRE DOOR MUST STILL BE VISIBLE - THIS IS THE LIMIT ON HOW FAR TO PUSH IN. Both vertical side edges of the door stay inside the frame with that narrow strip of trim and siding beyond each one. The complete top edge stays inside the frame, including the WHOLE row of small square windows running all the way across it, every window visible end to end. The bottom edge where the door meets the concrete driveway stays inside the frame. Nothing about the door is cut off by any edge of the picture. Push in exactly as far as that allows and no further.

STILL SQUARE-ON FROM THE FRONT: the door faces the camera flat, its horizontal panel seams run dead level across the frame and its vertical edges run straight up and down. NO oblique angle, NO receding perspective, NO corner view, NO low tilt looking up, NO whole house, NO full facade, NO roofline.

EVERYTHING ELSE IS UNCHANGED from the attached image. The same warm-lit lap siding and white trim around the door, the same black coach lanterns glowing warm on the wall either side, the sliver of covered porch and dark front door cropped at the right edge, the snowy concrete driveway, the night sky, the same warm lantern light and street-lamp spill.

THE LED CURTAIN IS FULLY MOUNTED AND THE WIRE IS BLACK: it hangs from the trim board above the door in evenly spaced vertical see-through strands right across the full width of the door, with slight natural sag and an uneven bottom hem. Every strand is a thin BLACK cord carrying small DARK unlit bulbs - the lights are OFF, no glow. Against the pale door each strand reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. There are clear gaps between the strands and the door panels are plainly visible through them - a hanging curtain of separate strands, never a solid panel or a mesh screen. At this closer range the strands and the bulbs are bigger and even easier to read.

THE PHONE AND ITS SCREEN ARE UNCHANGED - COPY THEM EXACTLY FROM THE ATTACHED IMAGE. Same handset, same hand, same grip, same angle, same size and same position in the bottom-centre foreground. Pushing the camera in must NOT shrink the phone and must NOT enlarge it. The screen shows the SAME app: a dark navy-blue screen with a grid of just TWO COLUMNS of large tiles, two across and about five down, roughly ten tiles in total and no more, each tile nearly half the screen wide with softly rounded corners and a narrow gutter, each one a small photograph of a house decorated in Christmas lights - a lit roofline, a nativity, a snowman, a reindeer, a porch draped in light curtains - mostly icy blue and cool white with a couple of warm tiles, ONE tile ringed with a bright electric-blue outline, and a ROUND SOLID BRIGHT-BLUE PLAY BUTTON with a clean WHITE TRIANGLE below the grid. NOT a dense grid of tiny icons, NOT three or more columns, NO glyphs or pictograms, and NO READABLE TEXT, NO LETTERS, NO WORDS AND NO NUMBERS anywhere on the screen.

The phone is a real current iPhone: a tall thin rounded rectangle almost exactly twice as tall as it is wide, one even corner radius on all four corners, a polished flat brushed-metal side rail all the way round catching a hard specular highlight, two small volume buttons and a mute switch on the left edge and one longer side button on the right, a thin glossy black bezel of exactly equal width on all four sides, and a small black PILL-SHAPED CUTOUT floating near the top centre inside the display. ABSOLUTELY NOT: a wide notch, a thick chin or forehead, a bezel thicker at the bottom than at the top, a home button, a rounded pebble body, an unevenly rounded outline, a square-cornered slab, a curved waterfall screen, a warped or melted outline.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every black cord clearly readable, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Image prompt — `starting_frames/v29_c04_g7.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `e128771f-0b9b-4145-aa16-e6e71f5ca6f3`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_234233_e128771f-0b9b-4145-aa16-e6e71f5ca6f3.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_29_assets/starting_frames/v29_c04_g6.png` · Higgsfield media `a6bcff66-91f5-4629-be28-3ba99b78c3a7`

````text
COPY THE ATTACHED IMAGE EXACTLY. Same house, same soft white sectional double garage door, same pale cream lap siding, same white trim, same black coach lanterns glowing warm either side, same snowy concrete driveway, same night light, same camera, same framing, same distance, same square-on angle, same foreground hand holding the same iPhone in the bottom-centre with the SAME two-column app grid and the same round blue play button. Everything is already correct and must be reproduced unchanged.

ONE SINGLE THING CHANGES: THE LED CURTAIN HAS ROUGHLY TWICE AS MANY STRANDS. In the attached image the vertical strands hanging over the garage door are spaced widely apart. Here they are packed about TWICE AS CLOSE TOGETHER - roughly double the number of strands across the same width, so the curtain reads as a much DENSER set of vertical lines running down the whole face of the door.

THE STRANDS THEMSELVES ARE UNCHANGED: each one is still a thin BLACK cord carrying small DARK unlit bulbs, the lights are OFF with no glow, and against the pale door each cord reads as a clearly dark, high-contrast vertical line. NO white wire, NO clear wire, NO silver wire, NO pale grey wire. They still hang from the trim board above the door, still span the full width of the door edge to edge, still have a slight natural sag and a slightly uneven bottom hem.

STILL A CURTAIN, NEVER A PANEL - CRITICAL: even at double the density these are SEPARATE HANGING VERTICAL STRANDS with clear DARK GAPS between them, and the garage door behind is plainly visible through those gaps - the recessed panel seams and the row of small square windows across the top must still read clearly through the curtain. Do NOT close the gaps. Do NOT turn it into a solid LED panel, a flat screen, a mesh, a net, a grille or a fabric sheet. Do NOT add horizontal wires. The strands run straight up and down only.

THE FRAMING IS ALREADY CORRECT - DO NOT CHANGE IT. The garage door stays big and dominant, spanning almost the full width of the picture, with the ENTIRE door visible: both vertical side edges inside the frame, the complete top edge including the WHOLE row of small square windows end to end, and the bottom edge where the door meets the driveway. Nothing about the door is cut off. Do NOT step closer, do NOT step back, do NOT tilt. Still square-on from the front: the panel seams run dead level and the door edges run straight up and down.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, the phone and its screen crisply resolved AND the whole garage door behind it equally in focus, the panel seams, the row of square windows and every individual black cord clearly readable and clearly separated from its neighbours, correct exposure with no blown-out highlight around the lanterns and no crushed black, NO motion blur, NO depth-of-field blur, NO soft focus, NO grain, NO haze. Candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v29_c04_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `6158ba56-08cf-421c-ba5f-a162d544dedf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_000729_6158ba56-08cf-421c-ba5f-a162d544dedf.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c04_g7.png` · Higgsfield media `33e117dc-afe4-4506-a25e-8ab508c8d930`
- image ref 1: `content/video_29_assets/references/v29_c04_r1.png` · Higgsfield media `f7585bc1-6c31-4f8c-b103-87b8839f716e`

````text
TWO REFERENCE IMAGES ARE ATTACHED. READ THIS FIRST.

REFERENCE 1 (the start image) IS THE FIRST FRAME OF THE VIDEO, UNCHANGED. Night. A white sectional garage door fills the frame, with a row of small black-framed square windows across its top and white trim all around it. A black coach lantern glows warm on each side. A BLACK LED curtain hangs down the whole face of the door in separate vertical strands, completely switched off. Snow-streaked concrete driveway across the bottom. A right hand enters from the bottom of the frame holding an iPhone upright in the lower middle of the picture; the phone screen shows a dark navy app with a two-column grid of small blue Christmas-light scene thumbnails and a round blue play button near the bottom.

REFERENCE 2 IS THE LAW FOR WHAT THE LIGHTS LOOK LIKE WHEN THEY TURN ON. Copy it literally. It is the SAME garage door in the SAME framing, with the curtain lit: a big warm-white and golden SANTA IN A SLEIGH PULLED BY THREE REINDEER flying to the LEFT across the door, a red Santa hat, a scatter of wrapped presents in green, pink, purple, blue and orange, gold stars, and swooshing dotted motion trails behind the sleigh. The instant the lights come on in this video, the door must look like REFERENCE 2. Same artwork, same colours, same placement on the door, same brightness, same warmth. Do NOT invent a different picture. Do NOT draw a snowman, a snowball fight, a tree or any other scene. Santa, sleigh, three reindeer, presents, stars, trails. Nothing else.

WHY REFERENCE 2 MATTERS MOST: it shows light that is COMING OUT OF OUR HANGING STRING LIGHTS, not light coming off a video screen. Study how it is built and reproduce it exactly:
- The picture is made of MANY THIN VERTICAL WIRES hanging side by side, each wire carrying small round bulbs. The whole image is built out of VERTICAL DOTTED LINES OF LIGHT.
- The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square pixel matrix.
- THE CURTAIN IS SEE-THROUGH. Through the gaps between strands you clearly read the white garage door behind it: its panel seams, its white trim, and the row of small square windows across the top all stay plainly visible THROUGH the lit artwork the entire time.
- Every lit bulb is a tiny individually countable point source: a blown-out white core, a warm coloured halo bleeding around it, a small soft star flare. The artwork is low resolution and chunky, with stepped blocky edges, no smooth curves, no thin outlines, no gradients, no anti-aliasing.
- The unlit areas are NOT a solid black field. They are dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin black wires as faint vertical lines.
- The curtain hangs a few inches PROUD of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, and the glow bounces back off the door behind it as a soft halo. Warm light spills onto the snowy driveway in a speckled uneven pattern, not a flat even wash.

ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projected image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. If it starts to look like a screen, it is wrong.

CAMERA - HELD IPHONE, LOCKED FOCAL LENGTH. One continuous handheld take, no cuts, no edits, no transitions. Gentle natural hand micro-shake the whole clip. The ONLY camera move is a SMALL, SLOW DRIFT UPWARD in the second half, roughly the height of the phone, so the top of the garage door and the windows settle a little lower in frame. It is a tilt, nothing more. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO WHIP PAN. The garage door stays exactly the same size on screen from the first frame to the last.

REAL TIME - NORMAL 1x SPEED. No fast motion, no time-lapse, no snappy jerks. Everything is smooth and natural, the speed of a real person filming their own house.

ACTION TIMELINE (4 seconds, one take):
0.0-0.6s - THE THUMB SCROLLS THE APP. A clear, visible flick: the thumb swipes UP across the phone screen and the two-column grid of blue scene thumbnails SLIDES UP with it, one row of thumbnails travelling off the top while a new row of different thumbnails rises in from the bottom, then the list decelerates and settles with a small natural rubber-band bounce. This scroll must be obvious and readable - the thumbnails clearly move on the screen. The garage door is still completely dark during the scroll.
0.6-0.9s - the thumb lifts, slides down and lands on the round blue play button.
0.9s - THE THUMB PRESSES PLAY AND THE CURTAIN LIGHTS UP ON THAT SAME FRAME. The press and the light are ONE event, perfectly in sync, not a frame apart. No gap, no fade-in delay, no build-up.
0.9-1.4s - the lit artwork snaps in bulb by bulb over about a quarter of a second, a fast ripple of bulbs waking up across the strands, and settles into exactly the picture from REFERENCE 2. At the same time the hand begins to LOWER, sinking straight down out of the bottom of the frame at a natural relaxed speed, the phone tilting slightly as the wrist drops.
1.4-1.6s - the hand and phone are completely gone below the bottom edge. They NEVER come back. Nothing else enters the frame for the rest of the clip.
1.6-4.0s - the lit garage door alone, with the camera drifting slowly upward.

THE ANIMATION IN THE LIGHTS MUST BE WILDLY ALIVE. THIS IS THE MOST IMPORTANT PART OF THE CLIP. A STATIC OR BARELY-MOVING PICTURE IS A TOTAL FAILURE. From the moment the lights come on to the very last frame, the artwork is in constant, big, entertaining motion. It is a running animation loop, not a still image with a twinkle on it.

WHAT MOVES, CONTINUOUSLY AND LARGELY:
- The whole SANTA AND SLEIGH AND THREE REINDEER team FLIES ACROSS THE DOOR, travelling a long visible distance to the LEFT, clearly crossing a large part of the door's width during the clip. When the team reaches the left edge it flies off and immediately re-enters from the right edge and keeps going. It is never parked in one spot.
- The three reindeer GALLOP: legs cycling fast, bodies bobbing up and down in a rolling wave, each reindeer out of phase with the one in front so the team ripples. Their antlers tilt as they bob.
- The sleigh rocks and tips as it flies, rising and falling on its own gentle wave.
- Santa's arm with the reins pumps up and down and his sack bounces behind him.
- The dotted motion trails STREAM backwards from the sleigh, each dot igniting and dying in fast sequence so the trails visibly chase and whip behind the team the whole way across.
- The wrapped presents BOUNCE and TUMBLE: each one pulses bright then dim in a staggered chase, and a few of them drift and spin slowly as if falling from the sleigh.
- The gold stars BURST on and off in fast scattered pops, twinkling hard, some flaring big then shrinking.
- Waves of colour chase horizontally across the unlit strands behind the artwork, so the whole curtain is shimmering with running light.
- Individual bulbs across the entire curtain flicker and sparkle constantly.

DENSITY OF MOTION - HARD RULE: at every single instant at least FOUR different things are changing at once. Compare any two moments a quarter of a second apart: the sleigh must have visibly moved, the reindeer legs must be in a different position, different presents must be lit, and different stars must be flashing. If any half-second stretch of this clip could be mistaken for a still photograph, the shot is wrong. Never freeze, never hold, never pause, not even at the end.

ABSOLUTE RULE - THE ARTWORK NEVER CHANGES SIZE AND NEVER LEAVES THE CURTAIN. Everything moves WITHIN the curtain. The figures stay exactly the scale they are in REFERENCE 2 - they travel across the door, they never grow, never shrink, never zoom toward the camera. The lit area never spreads onto the trim, the wall, the lanterns or the driveway, and never fills the frame. A wide band of dark unlit strands stays around the edges of the door for the whole clip.

ABSOLUTELY NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the lights or anywhere in the frame.

EVERYTHING ELSE IS UNCHANGED: the white sectional garage door, its square windows and white trim, the two black coach lanterns still glowing their own warm yellow, the snow-streaked concrete driveway, the dark night sky. No people, no faces, no other hands.

AUDIO: natural outdoor night ambience only - a faint breeze, a soft distant hum, the tiny sound of a thumb on glass. NO MUSIC, NO SCORE, NO VOICE, NO JINGLE BELLS, NO SOUND EFFECTS.

LOOK: real iPhone night video, handheld, candid UGC, natural sensor noise and bloom around the bright bulbs, no colour grading, no CGI polish, no cinematic filter. It must look like a normal person standing in their driveway filming their own Christmas lights turning on.
````

#### Video prompt — `clips/v29_c04_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `ccf649e1-02e4-4589-bf26-48d6e1e94371`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_223917_ccf649e1-02e4-4589-bf26-48d6e1e94371.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c04_g6.png` · Higgsfield media `d6ff8a3a-af39-4c6d-94ff-5b54b08e4f20`
- image ref 1: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `65c44162-9df0-40b4-8a50-f0fe41d6dd40`

````text
THE FIRST ATTACHED IMAGE IS THE LAW AND IT IS FRAME ONE. Same night, same wide WHITE SECTIONAL GARAGE DOOR filling the frame with its horizontal panel seams and its row of small black-framed square windows across the top, same white trim and same warm wall lantern glowing on each side, same snow-streaked concrete driveway along the bottom, same BLACK unlit curtain strands already hanging straight down over the ENTIRE width of the door, same right hand coming in from the bottom right holding an iPhone upright in the lower middle of frame, same app on its screen — a two-column grid of small blue animation thumbnails with a round blue play button at the bottom. Do not redraw the house, do not change the door, do not move the camera, do not change the lens or the framing.

THE SECOND ATTACHED IMAGE IS THE LOOK REFERENCE, AND ONLY THE LOOK. Copy from it ONLY how the lit picture is made: chunky cartoon shapes built out of separate round bulbs strung on separate hanging vertical black cords, with real dark gaps between the cords and the door visible through those gaps. Do NOT copy its house, its street, its camera angle, its car, its truck or its scene. Nothing from the second image appears in this clip except the WAY the lights look.

CAMERA — A HELD IPHONE, LOCKED FRAMING. Somebody is standing on the driveway filming this on a phone held in their other hand. Handheld micro-shake and a little breathing drift only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO PAN, NO TILT, NO ORBIT. The garage door stays exactly the same size and in exactly the same place in frame from the first frame to the last. No cuts.

THE TIMELINE — FOUR EXACT BEATS. Follow these times precisely.
0.0-0.8s — THE SCROLL. The curtain is still completely dark and unlit; the door is just black cords on white. The thumb slides slowly UP the phone screen and the grid of blue thumbnails SCROLLS with it, moving as one sheet: the top row slides up and off the top of the list, the rows below follow, and a new row of thumbnails rises into view from the bottom. It is a short, unhurried, ordinary scroll of about two rows, with a small elastic settle at the end. Nothing happens on the garage door during this time.
0.8-0.9s — THE PRESS. The thumb comes down onto the round blue PLAY BUTTON at the bottom of the screen and presses it. The button dips and flashes brighter under the thumb.
AT EXACTLY 0.9s — THE SNAP-ON. In the SAME SINGLE FRAME that the thumb lands on the play button, the ENTIRE GARAGE DOOR LIGHTS UP AT ONCE. Not a fade, not a ripple, not a wipe, not a warm-up, not a stagger — one instant hard SNAP from fully dark to fully lit, and the picture is ALREADY MOVING AT FULL SPEED in that very first lit frame. The two wall lanterns dim slightly by comparison and coloured light spills out across the snowy driveway.
0.9-1.3s — THE HAND LEAVES. Immediately after the press, the hand and the phone drop STRAIGHT DOWN and out through the bottom edge of frame in one smooth continuous movement, and they are COMPLETELY GONE by 1.3s. They do not drift sideways, do not linger, do not come back, and no part of a hand, finger, thumb, arm, sleeve, wrist or phone is visible anywhere in the frame for the rest of the clip.
1.3-4.0s — THE SHOW. The garage door is the only thing in frame, and the animation runs flat out without stopping for a single frame.

THE ANIMATION COVERS THE ENTIRE GARAGE DOOR. The lit picture is not a small rectangle in the middle. It uses the FULL WIDTH and the FULL HEIGHT of the curtain, from the trim board at the top all the way down to where the strands end above the driveway, and from the left edge of the door to the right edge of the door. The figures are drawn BIG — the snowman is nearly as tall as the door itself.

WHAT THE ANIMATION SHOWS. A giant chunky cartoon SNOWMAN built of three stacked balls stands on the right-hand half of the door, filling nearly the full height, with a black top hat, a bright orange carrot nose, coal eyes, a wide coal grin and a turquoise scarf. On the left-hand half a cartoon SANTA in a red suit with a white beard crouches and throws. Between them snowballs streak across the door on long curved red-and-orange dotted paths and burst into white splats. Bright stars and multicoloured snowflakes in pink, blue, yellow, green and orange are scattered over the whole door.

THE MOTION — LOUD AND CONTINUOUS FROM 0.9s TO 4.0s. Every half second the picture is a clearly different drawing, and every change FLOWS — limbs sweep through every position along their arc, nothing ever teleports, nothing ever blinks to an unrelated drawing, nothing ever freezes, pauses, resets or loops.
0.9-1.4s — the snowman's twiggy stick arm is already mid-throw; a snowball leaves his hand and travels left across the full width of the door.
1.4-1.9s — the snowball bursts on Santa's chest into a white splat; Santa is knocked backwards, both boots up, his hat flying off and tumbling.
1.9-2.4s — Santa scrambles up, packs a snowball between both hands so it visibly grows, and hurls it back across the door; his whole body follows through.
2.4-2.9s — it smacks the snowman in the face; his carrot nose SHOOTS OFF sideways and cartwheels across the door; his top hat spins off and drops back on; his coal eyes cross.
2.9-3.4s — the snowman shakes his whole body violently, snow flying off him, then scoops up a huge new snowball that visibly grows between his stick arms and winds it up over his head.
3.4-4.0s — he lets it go; it crosses the whole door and BURSTS on Santa, who is flung backwards with his boots kicking. The snowman throws both stick arms up, bounces on his base, his scarf flying. Everything is STILL moving in the very last frame — the boots still kicking, the scarf still whipping, the arms still pumping.
FLASHING IS NOT MOVEMENT. Colour chases and twinkles do not count. What the viewer sees is BODIES AND SNOWBALLS TRAVELLING LONG DISTANCES across the door.

IT MUST NOT LOOK LIKE AN LED PANEL OR A SCREEN. This is the single biggest thing to get right about the look. The curtain is NOT a video wall, NOT a TV, NOT a monitor, NOT a projection, NOT a flat glowing sheet and NOT a square pixel matrix. It is a hanging curtain of SEPARATE VERTICAL BLACK CORDS with small round bulbs strung along them. There are clear DARK GAPS between neighbouring cords and the white garage door, its panel seams and its black window frames stay plainly visible THROUGH those gaps the whole time, especially in the dark unlit areas of the picture. The horizontal gap between neighbouring cords is visibly wider than the vertical gap between bulbs on the same cord, so the grid reads as tall and rectangular, never square. The whole picture is built out of VERTICAL DOTTED LINES OF LIGHT. The unlit parts of the door are NOT a filled black field — they are simply the white door with dark unlit bulbs and dark cords over it. There is NO coloured backdrop, NO glowing background panel and NO solid field of colour behind the figures at any moment. Individual bulbs are visible as separate points of light, never merging into a smooth surface.

THE LIGHTS NEVER BREAK OUT OF THE CURTAIN. Everything lit stays on the hanging strands over the garage door. There is a clear margin of dark unlit bulbs around the whole picture — nothing lit ever touches or crosses the top trim board, the white side trim, the edges of the door or the bottom ends of the strands. No figure, no snowball, no splat and no star ever appears on the white trim, on the wall lanterns, on the siding, on the sky or on the driveway. Nothing lit ever floats in front of the door or detaches from the strands. The figures are a FLAT picture lying on the plane of the door — they are not solid, not 3D, not real, they never come forward out of the door, they never step onto the driveway and nothing ever comes out through the door toward the camera. Coloured light may spill onto the driveway as reflected glow, but no drawn shape ever does.

ABSOLUTELY NO TEXT anywhere in the lights or the frame — no letters, no words, no numbers, no captions, no subtitles, no watermark, no logo.

AUDIO: natural outdoor sound only — no music, no score, no background song. Cold still night air, one soft tap of a thumb on glass, the faint electrical hum and tick of a big light display switching on, a quiet breath. No voice, no dialogue, no commentary.

LOOK: real iPhone night video, handheld, tack-sharp, candid UGC. Slight sensor noise in the shadows, the lit bulbs blooming a little against the dark, no cinematic grade, no slow motion, no speed ramp.
````

#### Video prompt — `clips/v29_c04_g3.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `793cc572-ed52-4b31-b191-aae0790010bb`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_230146_793cc572-ed52-4b31-b191-aae0790010bb.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c04_g6.png` · Higgsfield media `d6ff8a3a-af39-4c6d-94ff-5b54b08e4f20`
- image ref 1: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `65c44162-9df0-40b4-8a50-f0fe41d6dd40`

````text
Animate the FIRST attached image (the start frame) exactly as it is. The first frame of the video IS that image, unchanged — night, the wide white sectional garage door filling the frame with its horizontal panel seams and its row of small black-framed square windows across the top, a warm wall lantern on each side, snow-streaked concrete driveway along the bottom, the UNLIT LED curtain hanging in black vertical strands across the whole door, and a right hand entering from the bottom right holding an iPhone upright in the lower middle, the app on screen showing a grid of small blue animation thumbnails with a round blue play button near the bottom.

THE SECOND ATTACHED IMAGE IS A LOOK REFERENCE ONLY — COPY HOW ITS LIGHTS ARE MADE, NOTHING ELSE. From the second image take ONLY these things: how DENSE the bulbs are, how the lit picture FILLS the whole curtain rectangle edge to edge, and the fact that the picture is built from thousands of small individual points of light strung on separate hanging vertical cords. Do NOT take its house, its gable, its stone, its street, its parked truck, its lamp post, its wet road, its camera angle or its framing. The house, the garage door, the driveway, the lanterns and the camera in this video come from the FIRST image and from nowhere else.

THE ANIMATION COVERS THE ENTIRE GARAGE DOOR. THIS IS THE MOST IMPORTANT RULE ABOUT THE PICTURE. When the lights come on, the lit picture fills the WHOLE curtain rectangle — the full width of the garage door from the left edge of the curtain to the right edge, and the full height from the trim board at the top down to the bottom hem just above the driveway. There is no large bare dark area left inside the curtain. The figure is drawn BIG: the snowman stands nearly the full height of the door, his hat almost at the top row of bulbs and his base almost at the bottom hem, and the scene spreads all the way out to both sides. It is NOT a small picture floating in the middle of a dark door. It is NOT confined to the centre. It is NOT a little logo or a small badge. Exactly as in the second image, the whole rectangle is alive with light.

THE LINES ARE DENSE. The curtain strands hang CLOSE TOGETHER and each cord carries MANY small bulbs packed tightly along it, so the picture resolves smoothly and reads clearly from a distance, just like the second image. Many more strands and many more bulbs than a sparse fairy-light string. The lit area is a fine, dense, high-resolution field of individual points of light.

AND YET IT MUST NEVER LOOK LIKE AN LED PANEL, A TV OR A PROJECTION. Even though it is dense, it is still made of SEPARATE HANGING VERTICAL CORDS. There are thin dark vertical gaps between the cords and the white garage door with its horizontal panel seams and its row of square windows stays visible through those gaps behind the picture, especially in the darker parts of the artwork. The horizontal gap between neighbouring cords is wider than the vertical gap between bulbs on the same cord, so the dot grid reads as TALL rather than square. The whole sheet sways very slightly as one hanging cloth, and the bottom hem is uneven and wavy, not a ruler-straight edge. It is never a solid glowing slab, never a flat screen, never a video wall, never a projected image, never a printed banner.

EXACT TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.8s — THE THUMB SCROLLS. The thumb slides up the grid of animation thumbnails and the grid scrolls by about two rows, fresh thumbnails coming in from the bottom, the list overshooting slightly and settling back with a small elastic bounce. Just that one short scroll — no repeated flicks, no rows racing past. The garage door stays completely DARK for this entire beat, not one bulb lit.
0.8-0.9s — the thumb slides down onto the ROUND BLUE PLAY BUTTON near the bottom of the screen and comes to rest on it.
0.9s — THE THUMB PRESSES PLAY. On that exact single frame the button visibly dips and flashes, AND the ENTIRE garage door SNAPS ON at full brightness in that very same frame, already mid-animation and already moving at full speed. NO fade, NO dissolve, NO ramp, NO brightness curve, NO bulbs lighting one by one, NO sweep, NO wipe, NO ripple, NO warm-up, NO gap and NO lag between the press and the light. One frame dark, the next frame the whole door fully lit.
0.9-1.3s — the hand and the phone drop straight down and out of the bottom of the frame, fast and smoothly, and are COMPLETELY GONE by 1.3s. No finger, no thumb, no phone corner, no sleeve and no glow from the screen remains anywhere in frame after 1.3s, and the hand NEVER comes back for the rest of the clip. From 1.3s onward the foreground is empty driveway and the frame belongs entirely to the lit garage door.
1.3-4.0s — nearly three full seconds of nothing but the lit door, animating hard.

WHAT THE LIGHTS SHOW — A SNOWBALL FIGHT, DRAWN CHUNKY AND SIMPLE OUT OF THE BULBS, FILLING THE WHOLE DOOR: a big three-ball SNOWMAN on the right standing nearly the full height of the door, with a black top hat, coal eyes, a coal grin, a bright orange carrot nose, two brown stick arms and a turquoise scarf streaming out sideways; and a smaller red-and-white SANTA on the left, ducking and throwing. Snowballs streak between them on curved dotted paths across the middle of the door, and small gold stars are scattered right across the rest of the lit area so almost none of it is empty.

MOTION — RELENTLESS FROM THE MOMENT IT SNAPS ON. Something changes every three tenths of a second, and at every instant at least TWO things are changing at once: a whole-body pose AND a lighting effect somewhere else in the picture. No held pose, no still frame, no pause.
0.9s — it lands mid-action: Santa already has one arm cocked right back behind his head, the snowman already leaning away, one snowball already halfway across the door.
1.4s — Santa whips his whole body forward and hurls the snowball; it streaks left to right across the middle of the door on a curved dotted trail while the gold stars all shift one row.
1.9s — the snowball reaches the snowman's chest and bursts into a small white star-shaped splat no bigger than his head; the snowman's whole stack squashes down with the hit, his top hat popping up off his head and dropping back on, and his turquoise scarf flares to double brightness.
2.4s — the snowman winds up: he swings both stick arms right back to one side, his middle snowball rotating with the twist, and a chase of colour runs down the three snowballs from hat to base.
2.9s — he flings a big snowball back the other way, right to left; it streaks across the door on a curved trail while Santa drops into a crouch behind a low bank of snow, both arms over his head, and every star twinkles out and back in a rolling wave.
3.4s — the snowball bursts into a small splat just above Santa; his red hat flies up off his head, spins and drops back on, his boots kicking, while the snowman shimmies his whole stack left-right-left.
3.9s — both figures land square facing us, the snowman's arms thrown wide, Santa's arms up laughing, and the whole picture — snowman, Santa, snowballs and every star — flashes to maximum brightness twice in quick succession for the final beat.
Every pose change is rendered by bulbs switching on and off row by row across the dense grid — chunky and instantaneous, never smooth morphing, never a crossfade.

THE LIGHTS NEVER BREAK OUT OF THE CURTAIN. Everything lit stays strictly inside the rectangle of the hanging curtain. No snowball, no splat, no star, no stick arm, no scarf and no glow ever crosses the top, bottom, left or right edge of the curtain. Nothing lit ever appears on the white trim, on the wall lanterns, on the siding, on the roof, in the sky or on the driveway except as ordinary soft coloured reflection on the snow and concrete directly below the door. No object ever appears to fly out of the picture toward the camera, no element ever gains depth or comes forward off the door, and there is never a shockwave, an expanding ring, a lens flare, a light leak or a burst of particles outside the rectangle. The picture is FLAT ON THE DOOR at all times.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, handheld micro-shake only, a few pixels of organic drift. The camera stays dead-on square to the garage door the whole four seconds. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO PAN, NO TILT. The garage door stays exactly the same size and in exactly the same place in frame from the first frame to the last, and the phone stays big and close to the camera for as long as it is in shot — it never shrinks and never recedes toward the door.

HARD RULES: the house never gains or loses windows, doors or features; the panel seams of the garage door stay dead level; the wall lanterns keep burning warm and steady and never change. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video, and no readable text on the phone screen — the app is just the grid of thumbnails and the round play button.

AUDIO: natural outdoor sound only — no music, no score, no background song. Cold still winter night ambience, one soft tap as the button is pressed, a faint electrical hum and a light plastic rattle from the curtain, distant neighbourhood quiet. No voice.

LOOK: real iPhone night UGC. Clean crisp points of light with no smeared bloom, correct exposure with no blown-out white and no crushed black, natural night white balance, mild sensor noise, no cinematic grade, no lens flare, no slow motion, no speed ramp. Normal 1x speed from first frame to last.
````

#### Video prompt — `clips/v29_c04_g4.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `1d4ccba9-6ec4-4568-98f8-87a45fc6b745`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_232043_1d4ccba9-6ec4-4568-98f8-87a45fc6b745.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c04_g6.png` · Higgsfield media `d6ff8a3a-af39-4c6d-94ff-5b54b08e4f20`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same two-storey family home seen dead-on and flat from the end of the driveway, same WARM SAND-BEIGE lap siding with WHITE trim, same WHITE SECTIONAL DOUBLE GARAGE DOOR filling the middle of the frame with its horizontal panel seams and its row of small square windows across the top, same gable with the round white louvre vent above it, same covered front porch with the dark red front door, same BLACK COACH LANTERN glowing warm either side of the garage door, same warm upstairs windows, same white gutter and white downpipe at the left, same bare white birch at the left edge, same CONCRETE DRIVEWAY with patchy snow across the bottom, with the UNLIT LED curtain hanging in thin BLACK vertical strands across the full width of the garage door, same hand coming up from the bottom holding a phone up in the lower part of frame, same app screen showing a dark navy grid of small colourful scene tiles with a BIG ROUND BLUE PLAY BUTTON at the bottom of the screen.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, handheld micro-shake only. The camera stays DEAD-ON SQUARE to the house the whole four seconds — it never swings round to an oblique angle, never turns to a corner view, never tilts up. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY. The house, the garage door and the phone stay exactly the same size in frame throughout. One continuous take, no cuts.

THE SINGLE MOST IMPORTANT THING IN THIS CLIP IS THE SYNC. The thumb presses the big round PLAY button, and ON THAT VERY SAME FRAME the garage door lights up. Not a frame early, not a frame late, no gap, no delay, no anticipation, no lag. The press and the light are ONE event. And the instant the button is pressed the hand immediately drops away out of the bottom of frame — it does not linger, does not hold the phone up to admire the lights, does not stay in shot for even half a second after the press.

THE PHONE PART IS SHORT. THE LIT PART IS MOST OF THE CLIP. The phone is finished and gone by 1.3s. From 1.3s to the very last frame — nearly THREE FULL SECONDS — there is nothing in the foreground and the curtain is lit and animating hard. The animation must NOT be squeezed into the last second and must NOT be a slow, sparse, gentle thing.

HOW THE PICTURE IN THE LIGHTS IS DRAWN — READ THIS BEFORE ANYTHING ELSE. It is FLAT CARTOON LIGHT ART built out of individual glowing bulbs, like a chunky neon shop sign or a big pixel sprite. Thick simple outlines, flat blocks of colour, big silly cartoon faces. It is NOT a photograph. It is NOT a realistic person or animal. It is NOT 3D, NOT rendered, NOT shaded, NOT textured, NOT lifelike, and NOT a video projected onto the door. If it could be mistaken for a photo of something real, it is wrong. Think cheap funny Christmas light display, not fine art.

ACTION TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.8s — A SHORT SCROLL, NOT A LONG ONE. The thumb comes in from the bottom and gives the grid of scene tiles ONE small flick: the tiles slide up by roughly ONE ROW only, a single fresh row of new scene thumbnails comes into view from the bottom, the list overshoots slightly and settles back with a small bounce. That is the entire scroll. NO long scroll, NO repeated flicks, NO second flick, NO rows racing past, NO scrolling through the whole list. One tile in the grid keeps its bright highlight ring the whole time — the scene is already chosen. The curtain on the garage door stays completely dark.
0.8-1.0s — the thumb slides straight down to the BIG ROUND BLUE PLAY BUTTON at the bottom of the app screen and comes to rest on it.
1.0s — THE THUMB PRESSES PLAY. On that exact frame the button visibly depresses and flashes, AND the entire curtain on the garage door SNAPS ON at full brightness in the very same single frame. NO fade, NO dissolve, NO ramp, NO brightness curve, NO bulbs lighting one by one, NO sweep across the door, NO pause between the press and the light. One frame dark, the next frame fully lit at maximum brightness and already animating.

THE ARTWORK THAT APPEARS — SANTA IS AMBUSHED IN A SNOWBALL FIGHT. On the RIGHT of the lit area a big three-ball SNOWMAN drawn in bulbs, with a black top hat, a bright orange carrot nose, coal eyes and a red scarf, twisted right back with a GIANT snowball held high over his head on both twiggy stick arms, grinning with a wide mouth of coal teeth. On the LEFT SANTA is crouched low behind a white snowbank, only his red hat, his white eyebrows and two round white eyes showing over the top, a small snowball clutched in one raised hand and a stack of coloured presents piled beside him as a barricade. Between them small snowballs fly across the middle on curved dotted paths and burst into little white splats. A few small gold stars and snowflakes scattered around. Colours: bright red, white, black, orange, emerald green, hot pink and gold. SANTA AND THE SNOWMAN EXIST ONLY INSIDE THE LIGHTS — they are never characters standing on the driveway, never figures in front of the house, and the driveway and the air in front of the house stay completely empty for the whole four seconds.

1.0-1.3s — the hand drops straight down and out of the bottom of frame fast and NEVER returns. The phone, the hand, the fingers and the sleeve are completely gone from frame by 1.3s and no part of them reappears at any point.
1.3-4.0s — THE REST OF THE CLIP IS THE LIT GARAGE DOOR ALONE, and it is relentless. See the movement block below.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. From the moment the curtain snaps on, SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least NINE separate changes between 1.3s and the last frame — and at every single instant AT LEAST TWO things are changing at once: a whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no pause, no settle, no gentle drifting. Every beat is a clearly DIFFERENT WHOLE-BODY pose — arms, body and head all in a new position — the figures fully redrawing between beats like an animated light-bulb sign. If two consecutive beats look similar, it is wrong. The fight runs forward continuously and NEVER resets to the opening pose and never loops.
1.3s — it lands out of the snap-on already mid-move: the snowman's torso whipping forward out of the wind-up, both stick arms sweeping down and across in one long curved arc, the giant snowball just leaving his hands, while Santa's two round eyes go huge and every gold star flashes on.
1.6s — the giant snowball crosses more than half the width of the picture on a curved dotted path, growing a trailing tail of small white dots. The snowman's arms follow through past his body and swing back, his top hat jumping off his head. Santa ducks lower so only his red hat and eyebrows show, and a bright chase of colour runs across the snowbank from left to right.
1.9s — the snowball SLAMS into the snowbank and BURSTS into a big white star-shaped splat. Santa is blasted backwards off his heels, both boots leaving the ground, arms flung up, mouth wide open, and the whole stack of presents topples sideways while every gold star twinkles out and back in a rolling wave.
2.2s — Santa lands on his back with his legs kicking in the air, the top three presents tumble loose in emerald green, hot pink and orange and bounce along the bottom, the splat collapses into falling dots, and the snowman's top hat drops back onto his head crooked.
2.5s — Santa scrambles back up behind the snowbank in a scurry of arms and legs and hoists the biggest present over his head as a shield, the snowman bends right down and scoops armfuls of snow with both stick arms, and the whole picture flashes brighter row by row from the bottom upward.
2.8s — Santa FLINGS his little snowball on a high curved dotted arc right across the picture, the snowman's new snowball is now huge and he twists right back into a fresh wind-up leaning so far his base lifts on one side, and his red scarf whips out sideways flashing red and white.
3.1s — Santa's snowball smacks the snowman square in the face and bursts into a white splat, his carrot nose SHOOTS OFF sideways and cartwheels away across the picture, his coal eyes cross, and a chase of colour runs UP from his base to the top of his hat.
3.4s — the snowman shakes his whole head violently side to side with snow flying off him in all directions and then hurls the second giant snowball the full width toward Santa, Santa drops behind the tipped-up present with only his eyes over the top, and the gold stars strobe.
3.7s — the snowball smashes into the present shield and EXPLODES into the biggest splat yet, Santa and the present are both flung backwards, the present spinning end over end, his boots kicking and his beard streaming out behind him, while two more presents burst loose and tumble across the bottom flashing colour.
3.9s — Santa lands upside down in the snowbank with only his red trousers and two kicking boots sticking out, the snowman throws both stick arms up in victory as his carrot nose flies back in and jams itself into his face, and the whole picture — the snowman, Santa's kicking boots, the presents and every gold star — flashes to maximum brightness twice in quick succession for the final beat. He is STILL celebrating and Santa's boots are STILL kicking on the final frame.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade, never a realistic animation curve. Coloured light spills and shifts across the snowy driveway below with every change.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. When the curtain snaps on, the lit picture sits inside the curtain rectangle with a wide band of dark unlit door above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from 1.0s to the last frame. The snowman is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the frame he first appears. The picture NEVER scales up, never grows, never inflates, never creeps outward and never drifts across the door. The dark unlit band around the picture is the same width in every single frame — at least six unlit bulb rows on all four sides — and every figure, every snowball, every present, every splat and every star stays inside it for the entire clip. If a pose would raise or widen the artwork past that margin, THE POSE IS DRAWN SMALLER AND LOWER. Nothing lit ever spreads onto the white door trim outside the curtain, onto the siding, onto the gable, the porch, the lanterns, the windows, the driveway or the sky. THE LIT RECTANGLE IS A FLAT PANEL OF LIGHT ON A FLAT GARAGE DOOR — it never becomes a stage, never becomes a doorway, never becomes a hole, and nothing ever comes out of it toward the camera.

THE REST OF THE HOUSE DOES NOT CHANGE. The coach lanterns keep their steady warm glow, the upstairs windows stay warm, the snow stays where it is. Nothing else on the building lights up, flickers or changes colour.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights or anywhere in the frame.

THE CURTAIN — CRITICAL: it stays a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the white garage door behind is plainly visible through those gaps — its panel seams and its row of square windows read straight through the curtain — especially in the unlit band around the picture. The horizontal gap between neighbouring strands is visibly wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square pixel matrix. The bulbs are small round points of light strung along thin BLACK cords, individually countable, each one a blown-out white core with a coloured halo bleeding around it. The unlit area is NOT a solid coloured field — it is dark cord and dark bulbs with the door showing through.

Real iPhone night video, handheld, tack-sharp, candid UGC. No text overlay, no watermark, no captions, no logo.
````

#### Video prompt — `clips/v29_c04_g5.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `8186c907-3916-4d51-8c10-c1e65c9e68c0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260916_002520_8186c907-3916-4d51-8c10-c1e65c9e68c0.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c04_g7.png` · Higgsfield media `33e117dc-afe4-4506-a25e-8ab508c8d930`
- image ref 1: `content/video_29_assets/references/v29_c04_r1.png` · Higgsfield media `f7585bc1-6c31-4f8c-b103-87b8839f716e`

````text
THE FIRST FRAME OF THIS VIDEO IS THE START IMAGE, PIXEL FOR PIXEL, UNCHANGED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. Frame one already contains A RIGHT HAND ENTERING FROM THE BOTTOM OF THE FRAME HOLDING AN iPHONE UPRIGHT IN THE LOWER MIDDLE OF THE PICTURE. The hand and the phone are present from the very first frame. Do NOT start on an empty garage door. Do NOT have the hand enter later. Do NOT re-stage, re-frame, re-light or redraw the start image in any way. The video simply begins on that exact photograph and moves forward from it.

WHAT IS IN THE START IMAGE: night; a white sectional garage door filling the frame, with a row of small black-framed square windows across its top and white trim all around it; a black coach lantern glowing warm on each side; a BLACK LED curtain hanging down the whole face of the door in separate vertical strands, completely switched off; snow-streaked concrete driveway across the bottom; and the right hand from the bottom edge holding the iPhone, its screen showing a dark navy app with a two-column grid of small blue Christmas-light scene thumbnails and a round blue play button near the bottom.

THE SECOND ATTACHED IMAGE IS NOT A FRAME OF THIS VIDEO. It is only a style guide for what the lights look like once they switch on. Never cut to it, never start on it, never copy its framing. Use it ONLY for the artwork and the quality of the light.

THAT STYLE GUIDE SHOWS: the same garage door with the curtain lit, carrying a big warm-white and golden SANTA IN A SLEIGH PULLED BY THREE REINDEER flying to the LEFT across the door, a red Santa hat, a scatter of wrapped presents in green, pink, purple, blue and orange, gold stars, and swooshing dotted motion trails behind the sleigh. When the lights come on in this video, that is exactly the picture that appears - same artwork, same colours, same placement on the door, same brightness, same warmth. Do NOT invent a different picture. Do NOT draw a snowman, a snowball fight, a tree or any other scene. Santa, sleigh, three reindeer, presents, stars, trails. Nothing else.

WHY THAT STYLE GUIDE MATTERS: it shows light COMING OUT OF OUR HANGING STRING LIGHTS, not light coming off a video screen. Reproduce it exactly:
- The picture is made of MANY THIN VERTICAL WIRES hanging side by side, each wire carrying small round bulbs. The whole image is built out of VERTICAL DOTTED LINES OF LIGHT.
- The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square pixel matrix.
- THE CURTAIN IS SEE-THROUGH. Through the gaps between strands you clearly read the white garage door behind it: its panel seams, its white trim, and the row of small square windows across the top all stay plainly visible THROUGH the lit artwork the entire time.
- Every lit bulb is a tiny individually countable point source: a blown-out white core, a warm coloured halo bleeding around it, a small soft star flare. The artwork is low resolution and chunky, with stepped blocky edges, no smooth curves, no thin outlines, no gradients, no anti-aliasing.
- The unlit areas are NOT a solid black field. They are dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin black wires as faint vertical lines.
- The curtain hangs a few inches PROUD of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, and the glow bounces back off the door behind it as a soft halo. Warm light spills onto the snowy driveway in a speckled uneven pattern, not a flat even wash.

ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projected image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. If it starts to look like a screen, it is wrong.

CAMERA - HELD IPHONE, LOCKED FOCAL LENGTH. One continuous handheld take, no cuts, no edits, no transitions. Gentle natural hand micro-shake the whole clip. The ONLY camera move is a SMALL, SLOW DRIFT UPWARD in the second half, roughly the height of the phone, so the top of the garage door and the windows settle a little lower in frame. It is a tilt, nothing more. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO WHIP PAN. The garage door stays exactly the same size on screen from the first frame to the last.

REAL TIME - NORMAL 1x SPEED. No fast motion, no time-lapse, no snappy jerks. Everything is smooth and natural, the speed of a real person filming their own house.

ACTION TIMELINE (4 seconds, one take):
0.0s - the exact start image. Hand and phone already in frame, garage door dark.
0.0-0.6s - THE THUMB SCROLLS THE APP. A clear, visible flick: the thumb swipes UP across the phone screen and the two-column grid of blue scene thumbnails SLIDES UP with it, one row of thumbnails travelling off the top while a new row of different thumbnails rises in from the bottom, then the list decelerates and settles with a small natural rubber-band bounce. This scroll must be obvious and readable - the thumbnails clearly move on the screen. The garage door is still completely dark during the scroll.
0.6-0.9s - the thumb lifts, slides down and lands on the round blue play button.
0.9s - THE THUMB PRESSES PLAY AND THE CURTAIN LIGHTS UP ON THAT SAME FRAME. The press and the light are ONE event, perfectly in sync, not a frame apart. No gap, no fade-in delay, no build-up.
0.9-1.4s - the lit artwork snaps in bulb by bulb over about a quarter of a second, a fast ripple of bulbs waking up across the strands, and settles into exactly the picture from the style guide. At the same time the hand begins to LOWER, sinking straight down out of the bottom of the frame at a natural relaxed speed, the phone tilting slightly as the wrist drops.
1.4-1.6s - the hand and phone are completely gone below the bottom edge. They NEVER come back. Nothing else enters the frame for the rest of the clip.
1.6-4.0s - the lit garage door alone, with the camera drifting slowly upward.

THE ANIMATION IN THE LIGHTS MUST BE WILDLY ALIVE. A STATIC OR BARELY-MOVING PICTURE IS A TOTAL FAILURE. From the moment the lights come on to the very last frame, the artwork is in constant, big, entertaining motion. It is a running animation loop, not a still image with a twinkle on it.

WHAT MOVES, CONTINUOUSLY AND LARGELY:
- The whole SANTA AND SLEIGH AND THREE REINDEER team FLIES ACROSS THE DOOR, travelling a long visible distance to the LEFT, clearly crossing a large part of the door's width during the clip. When the team reaches the left edge it flies off and immediately re-enters from the right edge and keeps going. It is never parked in one spot.
- The three reindeer GALLOP: legs cycling fast, bodies bobbing up and down in a rolling wave, each reindeer out of phase with the one in front so the team ripples. Their antlers tilt as they bob.
- The sleigh rocks and tips as it flies, rising and falling on its own gentle wave.
- Santa's arm with the reins pumps up and down and his sack bounces behind him.
- The dotted motion trails STREAM backwards from the sleigh, each dot igniting and dying in fast sequence so the trails visibly chase and whip behind the team the whole way across.
- The wrapped presents BOUNCE and TUMBLE: each one pulses bright then dim in a staggered chase, and a few of them drift and spin slowly as if falling from the sleigh.
- The gold stars BURST on and off in fast scattered pops, twinkling hard, some flaring big then shrinking.
- Waves of colour chase horizontally across the unlit strands behind the artwork, so the whole curtain is shimmering with running light.
- Individual bulbs across the entire curtain flicker and sparkle constantly.

DENSITY OF MOTION - HARD RULE: at every single instant at least FOUR different things are changing at once. Compare any two moments a quarter of a second apart: the sleigh must have visibly moved, the reindeer legs must be in a different position, different presents must be lit, and different stars must be flashing. If any half-second stretch of this clip could be mistaken for a still photograph, the shot is wrong. Never freeze, never hold, never pause, not even at the end.

ABSOLUTE RULE - THE ARTWORK NEVER CHANGES SIZE AND NEVER LEAVES THE CURTAIN. Everything moves WITHIN the curtain. The figures stay exactly the scale they are in the style guide - they travel across the door, they never grow, never shrink, never zoom toward the camera. The lit area never spreads onto the trim, the wall, the lanterns or the driveway, and never fills the frame. A wide band of dark unlit strands stays around the edges of the door for the whole clip.

ABSOLUTELY NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS anywhere in the lights or anywhere in the frame.

EVERYTHING ELSE IS UNCHANGED FROM THE START IMAGE: the white sectional garage door, its square windows and white trim, the two black coach lanterns still glowing their own warm yellow, the snow-streaked concrete driveway, the dark night sky. No people, no faces, no other hands.

AUDIO: natural outdoor night ambience only - a faint breeze, a soft distant hum, the tiny sound of a thumb on glass. NO MUSIC, NO SCORE, NO VOICE, NO JINGLE BELLS, NO SOUND EFFECTS.

LOOK: real iPhone night video, handheld, candid UGC, natural sensor noise and bloom around the bright bulbs, no colour grading, no CGI polish, no cinematic filter. It must look like a normal person standing in their driveway filming their own Christmas lights turning on.
````

### C05 — Lit facade — the ambush

**In the cut:** `starting_frames/v29_c05_g1.png` → `clips/v29_c05_g2.mp4`

#### Image prompt — `starting_frames/v29_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `0f0bd301-46da-449b-a256-fc8baa127215`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_201212_0f0bd301-46da-449b-a256-fc8baa127215.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_28_assets/starting_frames/v28_c05_g1.png` · Higgsfield media `a33527ab-d0c8-4c72-8795-00dcffb907ec`

````text
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a BUTTERMILK-YELLOW clapboard two-storey with crisp white trim, white window frames and a charcoal-grey roof, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: SANTA IS AMBUSHED IN A SNOWBALL FIGHT. On the RIGHT of the lit area a big three-ball SNOWMAN with a black top hat, a bright orange carrot nose, coal eyes and a red scarf is winding up, twisted right back, holding a GIANT snowball high over his head with both twiggy stick arms, one stick arm cocked, grinning with a wide mouth of coal teeth. On the LEFT, SANTA is crouched down low behind a white snowbank, only his red hat, his white eyebrows and two round white eyes showing over the top of it, a little snowball clutched in one raised hand and a stack of presents piled beside him like a barricade. Between them, two small snowballs are already flying across the middle of the picture on curved dotted paths, one bursting into a little white splat. A few small gold stars and snowflakes scattered around. The whole scene is one piece of light art on the wall.

3. Different foreground: a low picket fence capped with snow along the bottom left and a shovelled path with a snowbank either side leading to the house.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole picture sits within the curtain rectangle with a clear band of dark unlit wall above it, below it and at both sides. The snowman's hat and the raised snowball do not touch the top edge, the snowbank and the presents do not touch the bottom edge, and neither figure touches the side edges. Nothing lit appears on the roof, the trim, the sky or the window frames.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the buttermilk-yellow clapboard wall behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the clapboard texture and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v29_c05_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `da0eb4c5-ee6e-4286-abff-12dcf876f058`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_232135_da0eb4c5-ee6e-4286-abff-12dcf876f058.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v29_c05_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c05_g1.png` · Higgsfield media `8a1d156c-bacc-4c8c-b57a-70b1a813d79d`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same BUTTERMILK-YELLOW CLAPBOARD two-storey house with crisp white trim, white window frames and a charcoal-grey roof, same low snow-capped PICKET FENCE along the bottom left, same shovelled path with a snowbank either side leading to the house, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing SANTA AMBUSHED IN A SNOWBALL FIGHT — on the RIGHT a big three-ball SNOWMAN with a black top hat, a bright orange carrot nose, coal eyes and a red scarf, twisted right back with a GIANT snowball held high over his head on both twiggy stick arms, grinning with a wide mouth of coal teeth; on the LEFT SANTA crouched low behind a white snowbank with only his red hat, his white eyebrows and two round white eyes showing over the top, a small snowball in one raised hand and a stack of coloured presents piled beside him as a barricade; snowballs flying between them on curved dotted paths and bursting into white splats; small gold stars and snowflakes scattered around.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the picket fence, the snowbanks and the shrubs at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect. No cuts.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the front facade wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.
AS THE CAMERA WALKS CLOSER the individual bulbs simply get bigger and more countable and the gaps between the strands open up wider — the clapboard boards of the yellow wall read more and more clearly through them. The picture does NOT gain detail, does NOT gain resolution and does NOT become smoother as it gets closer. It must look MORE like a curtain of separate strands at 4.0s than it does at 0.0s, never less.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit picture sits inside the curtain rectangle with a wide band of dark unlit wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The snowman is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. The picture NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark wall between the highest lit point — the top of the snowman's hat and the raised giant snowball — and the top edge of the curtain, and the same clear margin at the bottom and at both sides. No hat, no stick arm, no snowball, no present, no splat and no star ever touches or crosses the edge of the curtain, and nothing lit ever appears on the white trim, the window frames, the charcoal roof, the sky or the neighbouring houses. If a pose would raise the arms or widen the body past that margin, THE POSE IS DRAWN SMALLER AND LOWER — the artwork is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: twisting, crouching, leaning, ducking, throwing low and flat, flashing and chasing — never stretching upward. THE LIT RECTANGLE IS A FLAT SHEET OF LIGHT ON A FLAT WALL — it never becomes a stage, never becomes a doorway, never becomes a hole. No snowball, no figure and no splat ever leaves the plane of the curtain or comes out of the wall toward the camera. Every snowball travels SIDEWAYS ACROSS the picture, never toward the lens.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. The animation is already ON, already mid-move and already running at full speed in the very first frame — there is NO still opening frame, NO pause, NO switch-on — and it is STILL running hard in the last frame. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST TWO things are changing at once: a whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no settle, no gentle drifting. Every pose is a clearly different WHOLE-BODY pose, the figures fully redrawing between beats like an animated light-bulb sign. The fight runs forward continuously and NEVER resets to the opening pose and never loops:
0.0s — it lands out of the first frame already mid-move: the snowman's torso whipping forward out of the wind-up, both stick arms sweeping down and across in one long curved arc, the giant snowball just leaving his hands, while Santa's two round eyes go huge and the gold stars fire to double brightness.
0.3s — the giant snowball crosses the middle of the picture on a curved dotted path growing a trailing tail of small white dots, the snowman's arms follow through past his body and swing back, and every snowflake shifts down a row.
0.6s — the snowball BURSTS on the snowbank into a big white star-shaped splat, Santa is blasted backwards off his heels with both boots off the ground and arms flung up, and a bright chase of colour runs across the whole picture from left to right.
0.9s — Santa lands on his back with his legs kicking in the air, the stack of presents topples sideways with the top three tumbling loose in emerald green, hot pink and orange, the splat collapses into falling dots, and the snowman's top hat jumps off and drops back on crooked.
1.2s — Santa scrambles back up behind the snowbank in a scurry of arms and legs, the loose presents bounce once off the snowbank, squash flat on impact and spring back into shape, and every snowflake twinkles out and back in a rolling wave from left to right.
1.5s — Santa snatches the biggest present and hoists it over his head as a shield, the snowman bends right down and scoops armfuls of snow with both stick arms, and the picture flashes brighter row by row from the bottom upward.
1.8s — the snowman's new snowball visibly grows between his stick arms, Santa peeks over the top of the present shield with one huge white eye, and the red scarf whips out sideways flashing red and white.
2.1s — Santa FLINGS his little snowball on a high curved dotted arc right across the picture, the snowman twists right back into a fresh wind-up leaning so far his base lifts on one side, and the gold stars strobe.
2.4s — Santa's snowball smacks the snowman square in the face and bursts into a white splat, his carrot nose SHOOTS OFF sideways and cartwheels away across the picture, his coal eyes cross, and the snowflakes flash on and off in alternating pairs.
2.7s — the snowman shakes his whole head violently side to side with snow flying off him in all directions, the scarf flies up over his head, and a chase of colour runs UP from his base to the top of his hat.
3.0s — he hurls the second giant snowball and it travels the full width of the picture toward Santa, Santa drops down behind the tipped-up present with only his eyes over the top, and the outline of the whole picture flashes brighter one bulb row at a time.
3.3s — the snowball smashes into the present shield and EXPLODES into the biggest splat yet, Santa and the present are both flung backwards, the present spinning end over end, his boots kicking and his beard streaming out behind him, and two more presents burst loose and tumble along the bottom.
3.6s — Santa lands upside down in the snowbank with only his red trousers and two kicking boots sticking out, the snowman throws both stick arms up in victory, and his carrot nose flies back in and jams itself into his face.
3.9s — he grins with a huge wide mouth of coal teeth, a ring of gold stars pops outward around his hat, and the whole picture — the snowman, Santa's kicking boots, the presents and every snowflake — flashes to maximum brightness twice in quick succession for the final beat. He is STILL celebrating and Santa's boots are STILL kicking on the final frame.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. Coloured light spills and shifts across the snow below with every change.

HARD RULES: no people, no cars, no pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C05 on disk (1)**

#### Video prompt — `clips/v29_c05_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `74457c68-16a3-4163-9eeb-2b6fed6c1679`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_220559_74457c68-16a3-4163-9eeb-2b6fed6c1679.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c05_g1.png` · Higgsfield media `8a1d156c-bacc-4c8c-b57a-70b1a813d79d`

````text
THE REFERENCE IMAGE IS THE LAW — READ THIS BEFORE ANYTHING ELSE. Frame one of this video IS the reference image, PIXEL FOR PIXEL. Do not redraw the scene, do not restage it, do not re-light it, do not invent a different building, do not change the colour of the building, do not change the lens, the angle, the framing or the time of night. Same night, same BUTTERMILK-YELLOW CLAPBOARD TWO-STOREY house with crisp white trim, white window frames and a charcoal-grey roof, same warm upstairs and downstairs windows, same little covered porch at the right with its glowing lantern and its small lit tree beside the steps, same dark conifer at the right edge, same low snow-capped picket fence running along the bottom left, same shovelled path with a snowbank either side leading up to the house, same neighbouring house glowing small at the far left, and the same big lit LED curtain across the front wall. All of it is still there in the last frame, in the same place, the same colour and the same size as in the first frame.

THE LIT ARTWORK — SANTA IS AMBUSHED IN A SNOWBALL FIGHT. On the RIGHT of the lit area a big three-ball SNOWMAN with a black top hat, a bright orange carrot nose, coal eyes and a red scarf is twisted right back, holding a GIANT snowball high over his head on both twiggy stick arms, grinning with a wide mouth of coal teeth. On the LEFT SANTA is crouched down low behind a white snowbank, only his red hat, his white eyebrows and two round white eyes showing over the top of it, a little snowball clutched in one raised hand and a stack of coloured presents piled beside him like a barricade. Between them snowballs fly across the middle of the picture on curved dotted paths, one bursting into a little white splat. Small gold stars and white snowflakes are scattered around.

SANTA AND THE SNOWMAN EXIST ONLY INSIDE THE LIGHTS. They are NOT characters in this scene. They are NOT real, NOT solid, NOT three-dimensional and NOT present in the world of the shot. They are A FLAT PICTURE MADE OF LIGHT BULBS hanging against the clapboard wall, confined to the lit rectangle and to nowhere else. THERE IS NEVER A SANTA STANDING ON THE GROUND. THERE IS NEVER A SNOWMAN ON THE PATH, THE LAWN, THE SNOWBANKS, THE PORCH, THE ROOF OR ANYWHERE IN FRONT OF THE HOUSE. No figure ever steps out of the wall, walks onto the ground, stands in the snow, casts a shadow on the snow or blocks any part of the building. No snowball and no present ever leaves the wall or lands in the snow. The path, the snowbanks and the air in front of the building stay COMPLETELY EMPTY of characters and objects for the whole four seconds.

HOW THE PICTURE IN THE LIGHTS IS DRAWN — It is FLAT CARTOON LIGHT ART built out of individual glowing bulbs, like a chunky neon shop sign or a big pixel sprite. Thick simple outlines, flat blocks of colour, big silly cartoon faces. It is NOT a photograph. It is NOT a realistic person or animal. It is NOT 3D, NOT rendered, NOT shaded, NOT textured, NOT lifelike, and NOT a video projected onto the wall. Think cheap funny Christmas light display, not fine art.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the picket fence, the snowbanks and the path edges sweep past and out of the bottom of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of the frame shows only the path ahead.

CONTINUOUS MOTION — THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. The figures move the way a hand-drawn cartoon moves: EVERY FRAME IS AN IN-BETWEEN OF THE FRAME BEFORE IT. Arms, bodies, snowballs and presents TRAVEL THROUGH every position along a smooth arc. Nothing is ever teleported from one position to another. The picture NEVER cuts, NEVER snaps to an unrelated drawing, NEVER jumps, NEVER resets to the opening pose, NEVER freezes, NEVER pauses, NEVER settles and NEVER restarts as a loop. It is ONE unbroken piece of comic business — an ambush that escalates — running from the very first frame to the very last, and it is still running in the last frame. Each thing that happens is caused by the thing that just happened.
THE TEST: play any half second of this clip and the motion inside it must FLOW — a body carries through, a stick arm sweeps, a snowball crosses ground. If you can see the picture blink from one drawing to a different unrelated drawing, THE CLIP HAS FAILED.
AND IT IS BIG. At every moment at least one shape is TRAVELLING A LONG WAY across the lit rectangle — at least a third of its width or height — not wobbling on the spot.
FLASHING IS NOT MOVEMENT. Colour chases and strobes are allowed but they are secondary, and no more than one is running at a time. No all-over twinkle, no constant colour cycling, no strobing every element at once, no fizzing multicoloured noise. What the viewer sees is BODIES AND SNOWBALLS TRAVELLING, not lights blinking.
IT IS ALREADY RUNNING IN FRAME ONE: the snowman already coiled at the top of his wind-up and starting to uncoil, snowballs already mid-flight, at full speed. No still opening frame, no switch-on, no ease-in, no warm-up.

THE THREE-FRAME TEST: freeze the clip at 1.3s, at 2.6s and at 4.0s. Those must be THREE COMPLETELY DIFFERENT DRAWINGS — different poses, different limb positions, different objects in the air, different splats. If a viewer could mistake any two of those frames for the same picture, THE CLIP HAS FAILED.

THE AMBUSH, PHASE BY PHASE — ONE CONTINUOUS STORY:
0.0-0.6s — the snowman's whole body UNCOILS. His torso whips forward out of the twisted wind-up, both stick arms sweeping down and across in one long curved arc, and the GIANT snowball LEAVES his hands and starts travelling left across the picture on a curving path, growing a trailing tail of small white dots. His top hat jumps off his head and hangs spinning in the air above him. His coal-tooth grin stretches wider and wider.
0.6-1.2s — the giant snowball crosses more than half the width of the lit rectangle. Santa's two round eyes swell from small circles into huge wide circles as he watches it come; his red hat lifts a few bulbs clear of his head. The snowball SLAMS into the snowbank in front of him and BURSTS into a big white star-shaped splat that expands outward over several frames. Santa is blasted backwards off his heels, both boots leaving the ground, arms flung up, mouth wide open, and the whole stack of presents beside him topples sideways, the top three tumbling loose in emerald green, hot pink and orange.
1.2-1.8s — the splat collapses into falling dots. Santa lands flat on his back behind the snowbank with his legs kicking in the air. The three loose presents each bounce once off the snowbank, SQUASH FLAT on impact, spring back into shape and roll a long way sideways along the bottom of the picture, each one tumbling end over end as it goes. The snowman's top hat drops back onto his head crooked and he shakes with laughter, his whole body wobbling from base to hat.
1.8-2.4s — Santa scrambles back up behind the snowbank in one continuous scurry of arms and legs, snatches up the biggest present and hoists it over his head like a shield with both hands. At the same time the snowman bends right down, scoops up armfuls of snow with both stick arms and packs a new snowball that visibly GROWS between his hands, bigger and bigger.
2.4-3.0s — Santa FLINGS his little snowball. It sails right across the picture on a high curved arc of dotted light, and it SMACKS the snowman square in the face and bursts into a white splat. His orange carrot nose SHOOTS OFF sideways and cartwheels away across the picture. His coal eyes cross. His red scarf flies straight up over his head and hangs there.
3.0-3.6s — the snowman shakes his whole head violently side to side, snow flying off him in all directions, then hurls the second giant snowball in one long unbroken swing. It travels the full width of the picture toward Santa, who ducks right down behind the tipped-up present with only his eyes over the top. The snowball SMASHES into the present shield and EXPLODES into the biggest splat yet.
3.6-4.0s — Santa and the present are both flung backwards, the present spinning end over end, Santa's boots kicking in the air and his beard streaming out behind him, until he lands upside down in the snowbank with only his red trousers and two kicking boots sticking out. The snowman throws both stick arms up in victory, his carrot nose flies back in and jams itself into his face and his mouth stretches into a huge grin. He is STILL celebrating, the loose presents are STILL rolling and Santa's boots are STILL kicking in the very last frame. Everything is still moving when the clip ends.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER BREAKS OUT OF THE CURTAIN. In the reference image the lit picture sits inside the curtain rectangle with a wide band of dark unlit clapboard wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The snowman, Santa, the presents and the snowballs are the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. The artwork NEVER scales up, never grows, never inflates, never creeps outward and never drifts across the wall. Nothing lit ever appears outside the curtain rectangle — not on the buttermilk-yellow clapboard, the white trim, the window frames, the porch, the roof, the sky, the picket fence, the path or the snow.

THE SAFE BOX. Imagine an inner rectangle drawn inside the lit curtain, leaving a wide dark border of at least six unlit bulb rows on all four sides. That inner rectangle is THE SAFE BOX. EVERY lit thing in this clip — the snowman, his hat, his scarf, his carrot nose, Santa, his hat, his boots, the presents, every snowball, every splat, every star and every snowflake — lives entirely inside the SAFE BOX for all four seconds, in every single frame, in every single pose. Nothing ever touches the edge of the SAFE BOX, let alone crosses it. No limb pokes out, no snowball flies out, no present rolls out, no splat sprays out. The SAFE BOX does not move and does not stretch. It is fixed to the wall and it scales with the wall as the camera walks in — exactly as the curtain does, exactly as the clapboard does. BECAUSE THE FIGURES CANNOT LEAVE THE BOX, ALL THE ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS — toppling, crouching, leaning, twisting, squashing, rolling, flashing and chasing — never reaching outward and never stretching upward. THE SNOWMAN'S RAISED SNOWBALL AND HIS TOP HAT ARE ALREADY AT THEIR HIGHEST POINT IN THE VERY FIRST FRAME AND NEVER GO HIGHER THAN THAT. A pose that would break the box IS DRAWN SMALLER AND LOWER instead.

THE LIT RECTANGLE IS A FLAT PANEL OF LIGHT ON A FLAT WALL. It is parallel to the clapboard behind it and it moves with the wall exactly as the wall moves as the camera walks in — same perspective, same skew, same foreshortening. It never detaches from the wall, never floats forward, never becomes a stage, never becomes a doorway, never becomes a hole, and nothing ever comes out through it.

THE CURTAIN — CRITICAL: it stays a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the buttermilk-yellow clapboard behind is plainly visible through those gaps, especially in the unlit band around the picture. The horizontal gap between neighbouring strands is visibly wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square pixel matrix. The bulbs are small round points of light strung along thin BLACK cords. The unlit area is NOT a solid coloured field — it is simply dark wall with dull unlit bulbs and faint dark cords, and there is NO filled background, NO coloured backdrop and NO saturated panel of colour behind the figures at any time. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail and does not gain size.

THE REST OF THE HOUSE DOES NOT CHANGE. The porch lantern keeps its steady warm glow, the windows stay warm, the little tree by the steps keeps its own lights, the snow stays where it is. Nothing else on the building lights up, flickers or changes colour.

Every pose change is rendered by bulbs switching on and off across the grid — chunky and stepped, like an animated light-bulb sign — but the movement it describes is continuous and flowing, never a jump between unrelated drawings. Coloured light spills and shifts across the snowbanks and the shovelled path as the picture moves.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights or anywhere in the frame. No captions, no subtitles, no watermark.

AUDIO: natural outdoor sound only — no music, no score, no background song. Cold night air, boots compressing snow at a walking rhythm, the faint electrical hum and tick of a big light display, one quiet amused breath. No voice, no dialogue.

LOOK: real iPhone night video, handheld, tack-sharp, candid UGC. Slight sensor noise in the shadows, no cinematic grade, no slow motion, no speed ramp. No text overlay, no watermark, no captions, no logo.
````

### C06 — Garage door + crowd — the snowball war

**In the cut:** `starting_frames/v29_c06_g1.png` → `clips/v29_c06_g3.mp4`

#### Image prompt — `starting_frames/v29_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `63a2e39f-ba00-457e-b1d2-0302fbe6c6e2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_201212_63a2e39f-ba00-457e-b1d2-0302fbe6c6e2.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_28_assets/starting_frames/v28_c06_g2.png` · Higgsfield media `77e2f041-136e-4c3e-ba53-fd386899e071`

````text
Same shot as the attached image - same camera, same distance, same house-with-attached-double-garage-door composition, same crowd of onlookers in silhouette along the bottom, same snow, same night. Keep the camera and the staging EXACTLY.

CHANGE TWO THINGS ONLY:

A) THE HOUSE COLOURS: the house is now DEEP SLATE-BLUE board-and-batten siding with white trim, and the wide double garage door is NATURAL OAK WOOD with dark iron strap hinges, instead of terracotta stucco with a white door.

B) THE PICTURE IN THE LIGHTS - throw it away completely and replace it with a much funnier, much wilder and MUCH MORE COLOURFUL cartoon scene, drawn chunky and simple out of the bulbs and filling the lit area fully.

THE NEW SCENE - AN ALL-OUT SNOWBALL WAR, SANTA AND THE ELVES AGAINST THE SNOWMEN:

Across the RIGHT of the lit area, THREE SNOWMEN in a ragged line are firing: the first winding up a giant snowball over his head, the second flinging one sidearm with his twiggy stick arm blurred into a curved motion arc, the third loading a huge home-made CATAPULT built out of candy canes, its bucket loaded with a stack of snowballs. All three have black top hats, bright orange carrot noses and scarves in different colours - red, turquoise and hot pink.

On the LEFT, SANTA is diving flat out through the air horizontally, both arms forward, mouth wide open, eyes as two white circles, his red hat blown off above him and his white beard streaming sideways, one boot flying off. Behind him TWO GREEN ELVES crouch behind a barricade of stacked presents, one popping up to throw, the other holding a saucepan lid over his head as a shield.

SNOWBALLS AND PRESENTS FILL THE AIR - eight or nine snowballs streaking across the middle on curved dotted paths, three of them bursting into white star-shaped splats, and five or six presents knocked loose and tumbling, each a DIFFERENT BRIGHT COLOUR: emerald green, hot pink, electric blue, orange, purple, yellow, turquoise, lime - each with a contrasting ribbon and bow. Two presents have burst open with little coloured shapes spilling out.

Curved multicoloured speed lines streak behind the thrown snowballs, and bright stars in many colours are scattered right across the lit area so almost none of it is empty.

COLOUR IS THE POINT: this is a loud multicoloured light show - red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated. It must NOT be mostly one or two colours.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit door above it, below it and at both sides. Nothing lit appears on the siding, the roof, the sky, the hedge or the snow.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the oak garage door behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the wood grain of the garage door and the snow detail clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v29_c06_g3.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `252cdf10-1f75-48d3-b5a7-91a9b813c242`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_230256_252cdf10-1f75-48d3-b5a7-91a9b813c242.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v29_c06_g3.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c06_g1.png` · Higgsfield media `0170b8a8-2dcf-462e-8ba4-34ae60f2148b`

````text
THE ANIMATION IS RELENTLESS FROM FRAME ONE. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. THE BIGGEST MISTAKE WOULD BE A QUIET, STATIC OR SLOWLY TWINKLING PICTURE. At 0.0s the light picture is ALREADY mid-cycle, already loud, already moving — snowballs are already halfway across the door, Santa is already mid-throw, a snowman is already mid-wind-up, presents are already tumbling. The picture does NOT switch on, does NOT hold still, does NOT ease in and NEVER settles. SOMETHING BIG CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST FOUR separate things are changing at once: a whole-body pose, an object travelling a long distance across the picture, a second object travelling the other way, and a lighting effect somewhere else. There is no held frame, no pause, no settle, no gentle drifting, no picture that merely sparkles in place. Every pose is a clearly DIFFERENT WHOLE-BODY pose — the figure fully redrawn between beats like an animated light-bulb sign — never a small wobble and never a shimmer.

Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same DEEP SLATE-BLUE board-and-batten house with white trim, same gable with the round white louvre vent above, same wide NATURAL OAK WOOD double garage door, same snowy driveway throwing coloured light back, same dark evergreen at the left edge and same lit lamp post at the right edge, same crowd of neighbours seen FROM BEHIND in winter coats and bobble hats along the bottom, same lit LED curtain across the garage door showing the all-out SNOWBALL WAR: Santa diving flat out through the air on the LEFT, two green elves crouched behind a barricade of stacked coloured presents at the bottom left, THREE SNOWMEN in a ragged line on the RIGHT with black top hats, orange carrot noses and red, turquoise and hot-pink scarves, one winding up a giant snowball overhead, one flinging sidearm, one loading a candy-cane catapult, with snowballs, tumbling coloured presents, curved speed lines, snowflakes and multicoloured stars filling the rest of the lit area.

FOUR LAYERS OF MOVEMENT RUN AT THE SAME TIME FOR ALL FOUR SECONDS, and all four are big, obvious movements that read clearly from the bottom of the driveway:
LAYER ONE — THE FIGURES REDRAW COMPLETELY. Santa's whole body flips between distinct poses: arms forward and legs trailing, then tucked into a ball, then sprawled and tumbling, then scrambling upright behind the barricade, then flat out diving again. Each snowman swings between full wind-up, full release and full recoil, their stacks squashing and stretching, their stick arms sweeping through wide arcs, their top hats popping up off their heads and dropping back on, their scarves whipping from one side to the other. The elves pop up over the barricade, throw, and duck back down.
LAYER TWO — SNOWBALLS TRAVEL ALL THE WAY ACROSS. At every instant at least three snowballs are in flight, crossing long distances between the left and the right of the picture on curved dotted trails, drawn by whole bulbs switching so they visibly fly rather than glide. A new snowball is launched roughly every third of a second, from alternating sides, so the middle of the picture is never empty.
LAYER THREE — PRESENTS TUMBLE AND THE CATAPULT FIRES. Brightly coloured wrapped presents — emerald, hot pink, electric blue, orange, purple, yellow, turquoise, lime — are knocked loose and tumble end over end through the picture, somersaulting as they go. The candy-cane catapult visibly cocks back, snaps forward and launches its whole stack of snowballs in a fan across the picture, then cocks back again.
LAYER FOUR — THE WHOLE FIELD PULSES. The scattered multicoloured stars and snowflakes never stop: they twinkle out and back in rolling waves from side to side, the curved speed lines chase along behind every thrown snowball, and colour chases run down the snowmen from hat to base and back up again.

BEAT BY BEAT:
0.0s — opens mid-war: Santa already flat out mid-dive with his hat blown off above him, the first snowman already at the top of his overhead wind-up, two snowballs already crossing the middle, one present already tumbling, an elf already popping up over the barricade.
0.3s — the first snowman hurls his giant snowball down and across; his whole stack pitches forward and his hat jumps off and lands back on; the stars all shift one row.
0.6s — Santa tucks into a rolling ball and somersaults across; the second snowman swings his stick arm through a full sidearm arc; a colour chase runs down all three snowmen.
0.9s — a snowball bursts on the barricade into a small white splat; both elves duck down out of sight behind the presents; two presents are knocked loose and tumble.
1.2s — the catapult cocks all the way back, its bucket dipping low; Santa scrambles up onto his knees; the snowflakes twinkle out and back in a wave from left to right.
1.5s — THE CATAPULT FIRES: its arm snaps forward and throws a fan of four snowballs across the whole picture at once; the third snowman recoils hard; the speed lines flare bright behind every one of them.
1.8s — an elf pops up and lobs a present back; Santa dives flat again the other way; the second snowman leans hard to one side, his scarf trailing.
2.1s — two of the fanned snowballs burst into small separate splats on the left; the elves' barricade of presents rocks and one present topples off the top and tumbles down.
2.4s — all three snowmen shimmy their stacks left-right-left at the same time, each snowball rotating against the one below it; their carrot noses strobe; three fresh snowballs launch from the right.
2.7s — Santa hurls a snowball back with his whole body twisting into it; it streaks the full width of the picture; a colour chase runs UP the snowmen from base to hat.
3.0s — three separate small splats land across the snowmen — three small splats, NOT one big one, NOT a combined explosion, NOT a flash, NOT a shockwave; all three snowmen squash down and spring back; presents tumble past them.
3.3s — the catapult cocks and fires a second fan; the elves both pop up and throw together; Santa rolls sideways out of the way; every star flashes in alternating pairs.
3.6s — the middle snowman takes a hit square in the chest, his whole stack pitching backward and his top hat spinning off and dropping back on; two presents somersault past him; Santa scrambles back behind the barricade.
3.9s — everything is still flying: snowballs still crossing, presents still tumbling, all three snowmen still mid-swing, and the whole picture flashes to maximum brightness twice in quick succession for the final beat.
THE PICTURE IS JUST AS FULL AT 4.0s AS AT 0.0s. It never empties out, never thins, never loses figures and never winds down. Every element in the reference image is still present and still moving in the last frame.

RULE — NOTHING LIT EVER LEAVES THE CURTAIN, NOT FOR A SINGLE FRAME. THIS OUTRANKS EVERY MOVEMENT INSTRUCTION ABOVE. The lit picture sits inside the curtain rectangle with a clear band of at least six unlit bulb rows of dark oak door above it, below it and at both sides, and that SAFE BOX is locked for the whole four seconds. No snowball, no splat, no present, no elf, no stick arm, no scarf, no hat, no star and no speed line ever touches or crosses the edge of the curtain. If a pose or a throw would carry something past that margin, IT IS DRAWN SMALLER AND FURTHER IN — the artwork is never enlarged and the rectangle is never enlarged to fit it. Nothing lit ever appears on the slate-blue siding, the white trim, the gable, the louvre vent, the roof, the sky, the evergreen, the lamp post or the driveway, except as ordinary soft coloured reflection on the snow directly below the door. There is never a glow bloom, a halo, a lens flare, a light leak, a smoke puff, a particle spray or an expanding ring outside the rectangle.

RULE — NO BIG WHITE FLASH AND NO GIANT BURST. No splat, flash, explosion or shockwave is ever bigger than one sixth of the lit rectangle. The picture never goes white, never washes out and never drops to a single colour. Splats are small, chunky and local, and there are several small ones rather than one big one.

RULE — THE PICTURE IS FLAT ON THE DOOR AND NOTHING EVER COMES OUT OF IT. Every lit element stays pressed flat against the plane of the garage door. Nothing gains depth, nothing grows toward the camera, nothing appears to fly out of the picture into the driveway, nothing casts a three-dimensional shadow and nothing becomes a real object in the scene. THERE ARE NEVER ANY WRAPPED PRESENTS SITTING ON THE SNOW, ON THE DRIVEWAY, AT THE FOOT OF THE DOOR OR IN FRONT OF THE HOUSE — the presents exist ONLY as light inside the curtain, at every moment, and ESPECIALLY NOT IN THE LAST SECOND. No physical prop of any kind appears anywhere in the scene.

THE ARTWORK NEVER CHANGES SIZE. Every figure is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first. The artwork never scales up, never inflates, never creeps upward and never fills more of the curtain than it does at the start. Because it cannot grow, ALL the energy goes sideways, downwards and into the bulbs.

THE CURTAIN — CRITICAL: it stays a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, never a solid LED video panel, never a flat screen, never a continuous mesh and never a projection. There are clear dark vertical gaps between the strands and the oak garage door is plainly visible through those gaps, especially in the unlit band around the picture. The bulbs are small round points of light strung along thin cords and you can count them. The whole sheet sways very slightly as one hanging cloth and the bottom hem is uneven.

THE CROWD IS CASUAL, RELAXED AND ALREADY MOVING IN THE VERY FIRST FRAME. They are neighbours hanging about on a driveway on a cold night, chatting, laughing, sipping drinks, glancing at the lights and back at each other. Nobody stands frozen waiting, there is no build-up and no synchronised cheer. All are seen FROM BEHIND — no face is ever turned toward camera. At 0.0s every person is already mid-movement: someone already mid-laugh, someone already turning, someone already raising a cup, a child already bouncing. Through the clip: a child bounces and points at the lights, two adults talk with their heads turned to each other, a woman rocks back laughing with her shoulders shaking, a man films on his phone and shifts his weight, a teenager hunches and blows a long fog of breath, two people knock shoulders, someone crouches to talk to a kid, scattered loose claps and easy laughter at different moments, never in unison. Coats crease, bobble hats bob, breath fogs, boots compress snow. NOBODY IS EVER STILL.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, filmed from behind the group at the bottom of the driveway. Handheld micro-shake only, a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO PAN, NO TILT. The house and the garage door stay exactly the same size and in exactly the same place in frame from the first frame to the last. One continuous take, no cuts.

HARD RULES: the house never gains or loses windows, doors or features; the lamp post keeps burning steady; the gable and the louvre vent never move. ABSOLUTELY NO TEXT — no letters, no words, no numbers, no speech bubbles, no signs, no captions, no subtitles and no watermark anywhere in the video or anywhere in the lights.

AUDIO: natural outdoor sound only — no music, no score, no background song. Cold winter night ambience, a faint electrical hum from the display, easy scattered laughter and low chatter from the group, a few loose claps, boots compressing snow. No clear speech.

LOOK: real iPhone night UGC. Clean crisp points of light with no smeared bloom, saturated separated colours, correct exposure with no blown-out white and no crushed black, mild sensor noise, no cinematic grade, no lens flare, no slow motion, no speed ramp. Normal 1x speed from first frame to last.
````

**Other takes of C06 on disk (2)**

#### Video prompt — `clips/v29_c06_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `97d8f124-73a7-46cc-9d41-47fa97803d6e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_220739_97d8f124-73a7-46cc-9d41-47fa97803d6e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c06_g1.png` · Higgsfield media `0170b8a8-2dcf-462e-8ba4-34ae60f2148b`

````text
Wholesome neighbourhood Christmas scene, warm and jolly.

THE REFERENCE IMAGE IS THE LAW — READ THIS BEFORE ANYTHING ELSE. Frame one of this video IS the reference image, PIXEL FOR PIXEL. Do not redraw the scene, do not restage it, do not re-light it, do not invent a different building, do not change the colour of the building, do not change the lens, the angle, the framing or the time of night. Same night, same DARK SLATE-BLUE BOARD-AND-BATTEN house with white trim and the round louvre vent in the gable, same WIDE NATURAL OAK WOOD DOUBLE GARAGE DOOR, same wall lantern glowing at the right, same dark conifer at the left edge, same snow-covered driveway throwing coloured light back, same neighbouring roof at the right, same CROWD OF NEIGHBOURS SEEN FROM BEHIND standing on the snow in winter coats and bobble hats along the bottom of frame, one of them holding up a phone. All of it is still there in the last frame, in the same place, the same colour and the same size as in the first frame.

THE LIT ARTWORK — AN ALL-OUT SNOWBALL WAR. Across the RIGHT of the lit area stand THREE SNOWMEN in a ragged line, each three balls tall, with black top hats, bright orange carrot noses, coal eyes and scarves in turquoise, blue and hot pink: the one at the back winding a giant snowball up over his head, the one in the middle front planted square on, the one at the right with his twiggy stick arms thrown wide. On the LEFT SANTA is in his big RED SLEIGH, tipped up and skidding, arms up, and a small GREEN ELF is down beside it. Along the bottom LEFT there is a big pile of chunky wrapped PRESENTS in hot pink, orange, emerald green, electric blue and yellow, each with a contrasting ribbon cross. Across the middle, snowballs streak on long curved RED AND ORANGE dotted paths, white star-shaped splats burst, and multicoloured snowflakes and bright stars in pink, blue, yellow, green and orange are scattered right across the lit area.

SANTA, THE ELF AND THE SNOWMEN EXIST ONLY INSIDE THE LIGHTS. They are NOT characters in this scene. They are NOT real, NOT solid, NOT three-dimensional and NOT present in the world of the shot. They are A FLAT PICTURE MADE OF LIGHT BULBS hanging against the garage door, confined to the lit rectangle shown in the reference image and to nowhere else. THERE IS NEVER A SANTA STANDING ON THE GROUND. THERE IS NEVER A SNOWMAN ON THE DRIVEWAY, THE SNOW, THE ROOF, AMONG THE CROWD OR ANYWHERE IN FRONT OF THE HOUSE. No figure ever steps out of the door, walks onto the ground, stands in the snow, casts a shadow on the snow or blocks any part of the building. No present and no snowball ever leaves the door, falls onto the driveway or lands in the snow. The ground and the air in front of the building stay COMPLETELY EMPTY of characters and objects for the whole four seconds — the only things on the ground are the things already on the ground in the reference image.

THE ARTWORK MUST STAY READABLE AT A DISTANCE — DO NOT LET IT TURN INTO A COLOURED BLUR. This is a wide shot, so the lit rectangle is small in frame. Every element inside it is therefore drawn BIG, CHUNKY and WELL SEPARATED: thick heavy outlines several bulbs wide, large flat blocks of a SINGLE colour inside each shape, and a clear band of DARK UNLIT BULBS between every figure and the next so the silhouettes never touch or merge. Each snowman is one solid readable snowman shape. The sleigh is one solid readable shape. Santa is one solid readable shape. The elf is one solid readable shape. EACH PRESENT IS ONE SOLID CHUNKY BOX OF A SINGLE FLAT COLOUR with a contrasting ribbon cross on it — big enough to read clearly from the bottom of the driveway. NO fine detail, NO thin lines, NO speckled multicoloured noise, NO confetti of tiny dots, NO gradients, NO glow bloom filling the gaps between shapes. If the lit rectangle ever reads as a mottled multicoloured blob instead of a clear cartoon picture a stranger could describe out loud, IT IS WRONG. Fewer, bigger, cleaner shapes beat more detail every single time.

HOW THE PICTURE IN THE LIGHTS IS DRAWN. It is FLAT CARTOON LIGHT ART built out of individual glowing bulbs, like a chunky neon shop sign or a big pixel sprite. Thick simple outlines, flat blocks of colour, big silly cartoon faces. It is NOT a photograph. It is NOT a realistic person or animal. It is NOT 3D, NOT rendered, NOT shaded, NOT textured, NOT lifelike, and NOT a video projected onto the door. Think cheap funny Christmas light display, not fine art.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, filmed from behind the group at the bottom of the driveway. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO PAN. The house and the garage door stay exactly the same size in frame from the first frame to the last. No cuts.

CONTINUOUS MOTION — THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. Everything in the lit picture moves the way a hand-drawn cartoon moves: EVERY FRAME IS AN IN-BETWEEN OF THE FRAME BEFORE IT. Bodies, stick arms, the sleigh, Santa, the elf, the snowballs and above all THE PRESENTS TRAVEL THROUGH every position along a smooth arc. Nothing is ever teleported from one position to another. The picture NEVER cuts, NEVER snaps to an unrelated drawing, NEVER jumps, NEVER resets to the opening arrangement, NEVER freezes, NEVER pauses, NEVER settles and NEVER restarts as a loop. It is ONE unbroken piece of comic business — a snowball war that escalates — running from the very first frame to the very last, and it is still running in the last frame. Each thing that happens is caused by the thing that just happened.
THE TEST: play any half second of this clip and the motion inside it must FLOW — a body carries through, a stick arm sweeps along its arc, a snowball crosses a visible distance, a present falls along a curve. If you can see the picture blink from one drawing to a different unrelated drawing, THE CLIP HAS FAILED.
AND IT IS BIG. At every moment at least one shape is TRAVELLING A LONG WAY across the lit rectangle — at least a third of its width or height — not wobbling on the spot.
FLASHING IS NOT MOVEMENT. Colour chases and strobes are allowed but they are secondary, and no more than one is running at a time. No all-over twinkle, no constant colour cycling, no strobing every element at once, no fizzing multicoloured noise. What the viewer sees is BODIES, SNOWBALLS AND BOXES TRAVELLING, not lights blinking.
IT IS ALREADY RUNNING IN FRAME ONE: snowballs already mid-flight, a stick arm already mid-swing, a present already mid-fall, at full speed. No still opening frame, no switch-on, no ease-in, no warm-up.

THE THREE-FRAME TEST: freeze the clip at 1.3s, at 2.6s and at 4.0s. Those must be THREE COMPLETELY DIFFERENT DRAWINGS — different poses, different limb positions, different snowballs in the air, different splats, a differently shaped pile of presents. If a viewer could mistake any two of those frames for the same picture, THE CLIP HAS FAILED.

THE PRESENTS ARE THE HEADLINE — THEY ARE NEVER STILL, NOT ONE OF THEM, NOT FOR ONE FRAME. This is the single thing to get right after the continuous motion rule.
- IN THE AIR: presents are knocked loose by the snowballs and fly in LONG SMOOTH CURVED ARCS across the picture, each one tumbling end over end as it goes so you can see it rotating. AT MOST TWO ARE IN THE AIR AT ANY ONE INSTANT — a new one roughly every second, each one big enough to follow with your eye the whole way. This is NOT a shower, NOT a rain of small objects, NOT confetti. Each flying present travels at least a third of the width of the lit rectangle, and it travels THROUGH every position on the way.
- ON LANDING: a present does not simply stop. It HITS, SQUASHES FLAT for an instant, BOUNCES back up in a smaller arc, comes down again, and ROLLS or SLIDES sideways along the bottom before it comes to rest — the whole bounce-and-roll drawn as one continuous travelling movement.
- IN THE PILE: THE PILE AT THE BOTTOM LEFT IS ALIVE THE WHOLE FOUR SECONDS. It is NEVER a static heap. At every single moment at least two presents already in the pile are moving: one rocking back and forth, one sliding sideways, one tipping over onto its side, one being knocked along by the present that just landed on it, one squirting out sideways from under the pile like a pip. When a snowball splat lands near it the whole pile JOLTS and several presents jump, scatter and resettle. The pile spreads SIDEWAYS along the bottom band as it grows, never upward, and it never rises past the lower third of the lit rectangle.
If at any moment a viewer could freeze the clip and find the pile of presents looking exactly as it did a second earlier, THE CLIP HAS FAILED.

FOUR LAYERS RUN AT THE SAME TIME FOR THE WHOLE FOUR SECONDS, all of them big, continuous, large-amplitude movement:
LAYER ONE — THE THREE SNOWMEN FIRE NON-STOP. They are not frozen decals: their twiggy stick arms sweep through full overhead and sidearm throwing arcs, their bodies twist and lean and squash short and stretch long, their top hats jump off and drop back on, their scarves whip out sideways, they duck, they bounce on their bases, they lean right over and scoop up new snow. Between one moment and the next the outline of the line of snowmen is unmistakably a different shape — never a small wobble.
LAYER TWO — SANTA AND THE SLEIGH GET HAMMERED. The red sleigh rocks, slews, tips up onto one runner and slams back down. Santa is knocked backwards out of it, hauls himself back in, ducks behind the side of it, pops up to throw, is blasted flat again — and he SWEEPS through every position in between, never cutting.
LAYER THREE — THE PRESENTS, exactly as described in the block above. This is the layer a viewer's eye lands on.
LAYER FOUR — THE ELF WORKS. The green elf keeps packing and hurling snowballs — two-handed, one-handed, rolling one along the ground — being knocked off his feet and scrambling back up, his whole body carrying through each throw. THE STARS AND SNOWFLAKES DO NOT CHASE, DO NOT RIPPLE AND DO NOT TWINKLE CONTINUOUSLY — they hold steady and only change on the few specific beats below that say so.

THE WAR, PHASE BY PHASE — ONE CONTINUOUS STORY:
0.0-0.5s — already mid-battle at full speed: the back snowman's whole body uncoils and his giant snowball LEAVES his stick arms, travelling left across the picture on a long curved red-and-orange dotted path. The middle snowman ducks under an incoming snowball that streaks past over his hat. Santa's sleigh is already slewing over onto one runner, and a hot-pink present is already mid-fall out of it, rotating as it goes.
0.5-1.0s — the giant snowball SLAMS into the side of the sleigh and BURSTS into a big white star-shaped splat that expands outward over several frames. Santa is blasted backwards out of the sleigh with both boots in the air and his beard streaming sideways. The sleigh slams back down and bounces; the whole pile of presents in the bottom-left corner JOLTS and three of them jump, scatter and resettle. The falling pink present lands, squashes, bounces and rolls sideways into the corner.
1.0-1.5s — the right-hand snowman flings one sidearm, his stick arm sweeping through a full blurred arc, and the snowball streaks the whole width of the picture. The elf scrambles up, packs a snowball between both hands so it visibly grows, and hurls it back. Santa hauls himself up over the side of the sleigh by both arms, his hat down over his eyes. A single chase of colour runs slowly up the picture from the bottom.
1.5-2.0s — the elf's snowball SMACKS the middle snowman square in the face and bursts into a white splat. His orange carrot nose SHOOTS OFF sideways and cartwheels away across the picture. His coal eyes cross and his top hat spins off his head. The right-hand snowman doubles over laughing, his whole body folding and springing back. An emerald green present bursts loose and starts its long arc down.
2.0-2.5s — all three snowmen scoop up snow together, leaning right over and packing, three new snowballs visibly GROWING between their stick arms at once. Santa seizes his moment, stands right up in the sleigh and flings two snowballs one after the other, following through with his whole body. The green present lands on the pile, bounces twice and slides; two more presents squirt sideways out from under it.
2.5-3.0s — Santa's two snowballs cross the picture and burst — one on the back snowman's chest, one on the right snowman's hat, both bursting into white splats. The back snowman rocks backwards on his base and nearly topples; the right snowman's hat flies up and tumbles end over end. The middle snowman shakes his whole head violently side to side, snow flying off him in all directions, and his carrot nose flies back in and jams itself into his face. Every gold star swaps colour gold to white.
3.0-3.5s — ALL THREE SNOWMEN FIRE AT ONCE. Three snowballs leave together on three different curved paths and converge on the sleigh. Santa dives flat behind it with both arms forward, the elf throws a present up over his head as a shield. The three snowballs hit in quick succession and EXPLODE into the biggest splats yet, one after another. The sleigh is flung up onto both runners and crashes down.
3.5-4.0s — Santa and the elf are both blasted backwards out of shot behind the sleigh with boots kicking, and four or five presents burst out of the pile and scatter sideways in a long spreading fan along the bottom — rolling, spinning, tipping and skidding in every direction, each one tumbling end over end. The three snowmen throw all six stick arms up in victory together, their scarves flying, bouncing on their bases, mouths stretching into huge grins. Presents are STILL rolling and rocking, the snowmen are STILL bouncing and Santa's boots are STILL kicking in the very last frame. Everything is still moving when the clip ends.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER BREAKS OUT OF THE CURTAIN. In the reference image the lit picture sits inside the curtain rectangle with a wide band of dark unlit garage door above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The snowmen, the sleigh, Santa, the elf and the presents are the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. The artwork NEVER scales up, never grows, never inflates, never creeps outward and never drifts across the door. There is ALWAYS a clear band of at least six unlit bulb rows of dark garage door between the highest lit point of the artwork — the tops of the snowmen's hats — and the top edge of the curtain, and the same clear margin at the bottom and at both sides. No hat, no stick arm, no runner, no boot, no present, no snowball, no splat and no star ever touches or crosses the edge of the curtain. Presents bounce and roll only INSIDE the rectangle and never fall out of the bottom of the curtain. Nothing lit ever appears outside the curtain rectangle — not on the slate-blue board-and-batten, the white trim, the gable, the round louvre vent, the roof, the sky, the conifer, the wall lantern, the driveway or the crowd.

THE SAFE BOX. Imagine an inner rectangle drawn inside the lit curtain, leaving a wide dark border of at least six unlit bulb rows on all four sides. That inner rectangle is THE SAFE BOX, and every part of every figure, every snowball, every present, every splat and every star stays inside it for the entire clip. The SAFE BOX does not move and does not stretch. If a pose would raise or widen the artwork past that margin, THE POSE IS DRAWN SMALLER AND LOWER. BECAUSE THE FIGURES CANNOT LEAVE THE BOX, ALL THE ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS.

THE LIT RECTANGLE IS A FLAT PANEL OF LIGHT ON A FLAT DOOR. It is parallel to the oak garage door behind it and it moves with the door exactly as the door moves. It never detaches from the door, never floats forward, never becomes a stage, never becomes a doorway, never becomes a hole, and nothing ever comes out through it.

THE CROWD IS CASUAL, RELAXED AND ALREADY HAPPY — AND ALREADY MOVING IN THE VERY FIRST FRAME. This is not an audience waiting for something to happen. Nobody is standing frozen staring at the garage in anticipation, nobody holds still and then reacts, there is no build-up and no big synchronised cheer. They are neighbours hanging about on a driveway on a cold night, chatting to each other, laughing at each other, glancing over at the lights and then back at their friends. Their attention drifts on and off the garage the whole time. They are ALL seen FROM BEHIND — no face is ever turned toward camera.
AT 0.0s, IN THE VERY FIRST FRAME, EVERY PERSON IS ALREADY MID-MOVEMENT. There is NO still opening frame, NO frozen first beat, NO pause before the motion starts.
CONTINUOUS OVERLAPPING MOTION, NEVER IN UNISON — at any instant several different people are doing several different things, and their little actions start and stop at different times so the group always looks alive:
0.0-0.5s — the person holding the raised phone shifts their weight to the other foot mid-shot; two adults beside them are mid-conversation, heads turned to each other, one shrugging.
0.5-1.0s — the woman in the long fur-collared coat laughs and rocks back on her heels, shoulders shaking; a child beside her bounces on the spot and swings an arm up toward the garage mid-bounce.
1.0-1.5s — two people in the front lean into each other and one points lazily at the lights without turning round; someone at the right shoves both hands deeper into their pockets, hunches, and blows out a long fog of breath.
1.5-2.0s — a woman at the left leans sideways into the person beside her and says something; they both laugh; another person scratches under their bobble hat and looks away from the garage entirely.
2.0-2.5s — two people knock shoulders and one claps once, casually; a child in a bobble hat twists round to tug a sleeve, then swings back; a couple sway slightly, arms linked.
2.5-3.0s — scattered easy laughter ripples through the group, a few loose claps at different moments, not together; one adult crouches down to say something to a kid; another points out at the lights.
3.0-3.5s — the person at the left lowers their phone, wipes their eyes laughing and says something sideways; a kid scrambles up onto their tiptoes; two heads tip together.
3.5-4.0s — a few people applaud loosely, hats bobbing, breath fogging, someone waves an arm overhead at a neighbour, someone else is already turning to talk to the person behind them.
Coats crease, hats bob, breath fogs, snow compresses under boots, shoulders shake with laughter. NOBODY IS EVER STILL and nobody is waiting.

COLOUR IS THE POINT: this stays a loud multicoloured light show the whole four seconds — red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated at every moment. It must NEVER drop back to one or two colours.

Every change is rendered by bulbs switching on and off across the grid — chunky and stepped, like an animated light-bulb sign — but the movement it describes is continuous and flowing, never a jump between unrelated drawings. Coloured light spills and shifts across the driveway and over the backs of the crowd as the picture moves.

THE CURTAIN — CRITICAL: it stays a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the oak garage door behind is plainly visible through those gaps, especially in the unlit band around the picture. The horizontal gap between neighbouring strands is visibly wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square pixel matrix. The bulbs are small round points of light strung along thin BLACK cords. The unlit area is NOT a solid coloured field — it is simply dark garage door with dull unlit bulbs and faint dark cords, and there is NO filled background, NO coloured backdrop and NO saturated panel of colour behind the figures at any time. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights or anywhere in the frame. No captions, no subtitles, no watermark.

AUDIO: natural outdoor sound only — no music, no score, no background song. Cold night air, a loose crowd chatting and laughing at different moments, scattered uneven clapping, boots in snow, the faint electrical hum and tick of a big light display, breath fogging. No commentary, no voice-over.

LOOK: real iPhone night video, handheld, tack-sharp, candid UGC. Slight sensor noise in the shadows, no cinematic grade, no slow motion, no speed ramp. No text overlay, no watermark, no captions, no logo.
````

#### Video prompt — `clips/v29_c06_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on
**Job** - `99bbe96d-c3ec-441f-82dc-8ada8cba7525`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_224225_99bbe96d-c3ec-441f-82dc-8ada8cba7525.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c06_g1.png` · Higgsfield media `0170b8a8-2dcf-462e-8ba4-34ae60f2148b`

````text
Wholesome neighbourhood Christmas scene, warm and jolly.

THE REFERENCE IMAGE IS THE LAW. Frame one of this video IS the reference image, PIXEL FOR PIXEL. Do not redraw the scene, do not restage it, do not re-light it, do not invent a different building, do not change the colour of the building, do not change the lens, the angle, the framing or the time of night. Same night, same dark board-and-batten house with white trim and the round louvre vent in the gable, same WIDE NATURAL OAK WOOD DOUBLE GARAGE DOOR, same wall lantern glowing at the right, same dark conifer at the left edge, same snow-covered driveway, same neighbouring roof at the right, same CROWD OF NEIGHBOURS SEEN FROM BEHIND standing on the snow in winter coats and bobble hats along the bottom of frame, one of them holding up a phone. All of it is still there in the last frame, in the same place, the same colour and the same size as in the first frame.

RULE ONE — NOTHING LIT EVER LEAVES THE CURTAIN, NOT FOR A SINGLE FRAME. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT AND IT OUTRANKS EVERYTHING ELSE BELOW. In the reference image the lit picture sits inside a rectangle on the garage door, with a band of dark unlit door above it, below it and at both sides. That rectangle is a HARD WALL. Every figure, every snowball, every present, every splat, every star and every snowflake stays strictly inside it for all four seconds. Draw an inner SAFE BOX leaving a margin of at least six unlit bulb rows on all four sides, and keep every drawn shape inside the SAFE BOX. If a pose or a burst would reach past that margin, DRAW IT SMALLER. Nothing lit ever appears on the board-and-batten siding, the white trim, the gable, the round louvre vent, the roof, the sky, the conifer, the wall lantern, the neighbouring house, the driveway, the snow or the crowd. There is NO glow bloom spreading past the rectangle, NO halo, NO flare, NO light leak, NO smoke, NO particles and NO expanding ring of any kind outside it. Coloured light may reflect softly off the snow and off the backs of the crowd, but no DRAWN SHAPE is ever outside the rectangle.

RULE TWO — NO BIG WHITE FLASH AND NO GIANT BURST. No splat, star, flash, shockwave, starburst or explosion is EVER bigger than one sixth of the lit rectangle. Nothing white ever fills the picture, washes it out, whites out the frame or covers the figures. The whole picture NEVER goes white, NEVER goes to a single colour and NEVER strobes to full brightness. A splat is a small chunky white star shape beside the thing it hits, and the figures around it stay fully visible and fully readable the entire time it is on screen. If at any moment a big white shape dominates the lit rectangle, THE CLIP HAS FAILED.

RULE THREE — THE PICTURE IS FLAT ON THE DOOR AND NOTHING EVER COMES OUT OF IT. The lit rectangle is a FLAT PANEL OF LIGHT lying on the plane of the oak garage door, parallel to it, moving exactly with it. Nothing ever floats forward off the door, nothing ever detaches, nothing gains depth, nothing rushes toward the camera, nothing casts a shadow onto the snow, and the rectangle NEVER becomes a stage, a doorway, a window, a portal or a hole. Santa, the elf, the snowmen, the snowballs and the presents are DRAWINGS MADE OF BULBS, not objects. THERE IS NEVER A SANTA STANDING ON THE GROUND, NEVER A SNOWMAN ON THE DRIVEWAY OR AMONG THE CROWD, AND — THIS IS THE ONE THAT WENT WRONG LAST TIME — THERE ARE NEVER ANY WRAPPED PRESENTS SITTING ON THE SNOW, ON THE DRIVEWAY, AT THE FOOT OF THE DOOR OR IN FRONT OF THE HOUSE, AT ANY MOMENT AND ESPECIALLY NOT IN THE LAST SECOND. Every present in this clip is a picture drawn in bulbs on the garage door and stays there. The ground and the air in front of the building stay COMPLETELY EMPTY of characters and objects for the whole four seconds — the only things on the ground are the things already on the ground in the reference image.

THE LIT ARTWORK — AN ALL-OUT SNOWBALL WAR. Across the RIGHT of the lit area stand THREE SNOWMEN in a ragged line, each three balls tall, with black top hats, bright orange carrot noses, coal eyes and scarves in turquoise, blue and hot pink: the one at the back winding a giant snowball up over his head, the one in the middle front planted square on, the one at the right with his twiggy stick arms thrown wide. On the LEFT SANTA is in his big RED SLEIGH, tipped up and skidding, arms up, and a small GREEN ELF is down beside it. Along the bottom LEFT there is a big pile of chunky wrapped PRESENTS in hot pink, orange, emerald green, electric blue and yellow, each with a contrasting ribbon cross. Across the middle, snowballs streak on long curved RED AND ORANGE dotted paths, small white star-shaped splats burst, and multicoloured snowflakes and bright stars in pink, blue, yellow, green and orange are scattered right across the lit area.

THE ARTWORK MUST STAY READABLE AT A DISTANCE. This is a wide shot, so the lit rectangle is small in frame. Every element inside it is therefore drawn BIG, CHUNKY and WELL SEPARATED: thick heavy outlines several bulbs wide, large flat blocks of a SINGLE colour inside each shape, and a clear band of DARK UNLIT BULBS between every figure and the next so the silhouettes never touch or merge. Each snowman is one solid readable snowman shape. The sleigh is one solid readable shape. Santa is one solid readable shape. The elf is one solid readable shape. EACH PRESENT IS ONE SOLID CHUNKY BOX OF A SINGLE FLAT COLOUR with a contrasting ribbon cross on it. NO fine detail, NO thin lines, NO speckled multicoloured noise, NO confetti of tiny dots, NO gradients, NO glow bloom filling the gaps between shapes. If the lit rectangle ever reads as a mottled multicoloured blob instead of a clear cartoon picture a stranger could describe out loud, IT IS WRONG. Fewer, bigger, cleaner shapes beat more detail every single time.

THE PICTURE IS JUST AS FULL AT 4.0s AS AT 0.0s. It never empties out, never thins, never clears, never goes quiet and never ends on a near-blank door. All three snowmen, the sleigh, Santa, the elf and a big pile of presents are ALL still drawn, all still in the rectangle and all still moving in the very last frame.

HOW THE PICTURE IN THE LIGHTS IS DRAWN. FLAT CARTOON LIGHT ART built out of individual glowing bulbs, like a chunky neon shop sign or a big pixel sprite. Thick simple outlines, flat blocks of colour, big silly cartoon faces. NOT a photograph, NOT realistic, NOT 3D, NOT rendered, NOT shaded, NOT textured, NOT lifelike, NOT a video projected onto the door. Think cheap funny Christmas light display, not fine art.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, filmed from behind the group at the bottom of the driveway. Handheld micro-shake only. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT, NO PAN. The house and the garage door stay exactly the same size in frame from the first frame to the last. No cuts.

CONTINUOUS MOTION, AND MORE OF IT THAN YOU THINK. Everything in the lit picture moves the way a hand-drawn cartoon moves: EVERY FRAME IS AN IN-BETWEEN OF THE FRAME BEFORE IT. Bodies, stick arms, the sleigh, Santa, the elf, the snowballs and the presents TRAVEL THROUGH every position along a smooth arc. Nothing is ever teleported. The picture NEVER cuts, NEVER snaps to an unrelated drawing, NEVER jumps, NEVER resets, NEVER freezes, NEVER pauses, NEVER settles and NEVER restarts as a loop. It is ONE unbroken escalating snowball war running from the very first frame to the very last, and it is still running in the last frame.
AT EVERY SINGLE INSTANT OF THE FOUR SECONDS, AT LEAST FOUR SEPARATE SHAPES ARE TRAVELLING LONG DISTANCES AT THE SAME TIME — each covering at least a third of the width or height of the lit rectangle. There is never a moment when only one thing is moving and never a moment when the picture is calm.
FLASHING IS NOT MOVEMENT. Colour chases and strobes are secondary and no more than one runs at a time. No all-over twinkle, no constant colour cycling, no strobing every element at once, no fizzing multicoloured noise. What the viewer sees is BODIES, SNOWBALLS AND BOXES TRAVELLING, not lights blinking.
IT IS ALREADY RUNNING IN FRAME ONE: snowballs already mid-flight, a stick arm already mid-swing, a present already mid-fall, at full speed. No still opening frame, no switch-on, no ease-in, no warm-up.

THE THREE-FRAME TEST: freeze at 1.3s, 2.6s and 4.0s. Those must be THREE COMPLETELY DIFFERENT DRAWINGS — different poses, different limb positions, different snowballs in the air, different splats, a differently shaped pile of presents. If a viewer could mistake any two for the same picture, THE CLIP HAS FAILED.

THE PRESENTS ARE THE HEADLINE — THEY ARE NEVER STILL, NOT ONE OF THEM, NOT FOR ONE FRAME, AND THEY NEVER LEAVE THE RECTANGLE.
- IN THE AIR: presents are knocked loose by snowballs and fly in LONG SMOOTH CURVED ARCS across the picture, tumbling end over end so you can see them rotating. AT MOST TWO ARE IN THE AIR AT ANY ONE INSTANT — a new one roughly every second, each big enough to follow with your eye the whole way. NOT a shower, NOT a rain of small objects, NOT confetti. Each flying present travels at least a third of the width of the lit rectangle, THROUGH every position on the way, and its whole arc stays inside the SAFE BOX.
- ON LANDING: a present does not simply stop. It HITS, SQUASHES FLAT for an instant, BOUNCES back up in a smaller arc, comes down again, and ROLLS or SLIDES sideways along the bottom of the rectangle before it comes to rest — one continuous travelling movement. It NEVER falls out of the bottom of the rectangle and NEVER lands on the door below the lights, on the driveway or in the snow.
- IN THE PILE: THE PILE AT THE BOTTOM LEFT IS ALIVE THE WHOLE FOUR SECONDS and NEVER a static heap. At every moment at least three presents already in the pile are moving: one rocking, one sliding sideways, one tipping onto its side, one knocked along by the present that just landed, one squirting out sideways from under the pile. When a splat lands near it the whole pile JOLTS and several presents jump, scatter and resettle. The pile spreads SIDEWAYS along the bottom band of the rectangle as it grows, never upward and never outward past the SAFE BOX.

FOUR LAYERS RUN AT THE SAME TIME FOR THE WHOLE FOUR SECONDS, all of them big, continuous, large-amplitude movement:
LAYER ONE — THE THREE SNOWMEN FIRE NON-STOP. Their twiggy stick arms sweep through full overhead and sidearm throwing arcs, their bodies twist, lean, squash short and stretch long, their top hats jump off and drop back on, their scarves whip out sideways, they duck, they bounce on their bases, they lean right over and scoop up new snow. Between one moment and the next the outline of the line of snowmen is unmistakably a different shape — never a small wobble.
LAYER TWO — SANTA AND THE SLEIGH GET HAMMERED. The red sleigh rocks, slews, tips up onto one runner and slams back down. Santa is knocked backwards out of it, hauls himself back in, ducks behind the side, pops up to throw, is blasted flat again — SWEEPING through every position in between, never cutting.
LAYER THREE — THE PRESENTS, exactly as described above. This is the layer the eye lands on.
LAYER FOUR — THE ELF WORKS. The green elf keeps packing and hurling snowballs — two-handed, one-handed, rolling one along the ground — being knocked off his feet and scrambling back up, his whole body carrying through each throw. THE STARS AND SNOWFLAKES DO NOT CHASE, DO NOT RIPPLE AND DO NOT TWINKLE CONTINUOUSLY — they hold steady and only change on the specific beats below that say so.

THE WAR, PHASE BY PHASE — ONE CONTINUOUS STORY, EVERY HALF SECOND A NEW DRAWING:
0.0-0.5s — already mid-battle at full speed: the back snowman's whole body uncoils and his giant snowball LEAVES his stick arms, travelling left on a long curved red-and-orange dotted path. The middle snowman ducks under an incoming snowball streaking past over his hat. Santa's sleigh is already slewing onto one runner. A hot-pink present is already mid-fall out of it, rotating. The elf is already mid-throw.
0.5-1.0s — the giant snowball SLAMS into the side of the sleigh and bursts into a SMALL chunky white star splat beside it. Santa is blasted backwards out of the sleigh with both boots in the air and his beard streaming sideways. The sleigh slams down and bounces; the pile of presents JOLTS and three of them jump, scatter and resettle sideways. The pink present lands, squashes, bounces and rolls into the corner. The right snowman is already winding up.
1.0-1.5s — the right-hand snowman flings one sidearm, his stick arm sweeping a full arc, and the snowball streaks the whole width of the picture. The elf scrambles up, packs a snowball between both hands so it visibly grows, and hurls it back. Santa hauls himself up over the side of the sleigh by both arms, hat down over his eyes. An electric-blue present bursts loose and starts its arc. One slow colour chase runs up the picture from the bottom.
1.5-2.0s — the elf's snowball SMACKS the middle snowman square in the face with a small white splat. His orange carrot nose SHOOTS OFF sideways and cartwheels across the picture. His coal eyes cross and his top hat spins off his head and drops back on. The right-hand snowman doubles over laughing, his whole body folding and springing back. The blue present lands, bounces twice and slides; two more squirt sideways out from under the pile. An emerald green present bursts loose and starts its long arc down.
2.0-2.5s — all three snowmen scoop up snow together, leaning right over and packing, three new snowballs visibly GROWING between their stick arms at once. Santa stands right up in the sleigh and flings two snowballs one after the other, following through with his whole body. The green present lands on the pile, bounces twice and slides sideways. The elf rolls a snowball along the bottom of the rectangle.
2.5-3.0s — Santa's two snowballs cross the picture and burst — one small splat on the back snowman's chest, one on the right snowman's hat. The back snowman rocks backwards on his base and nearly topples; the right snowman's hat flies up and tumbles end over end back onto his head. The middle snowman shakes his whole head violently side to side, snow flying off him, and his carrot nose flies back in and jams into his face. Every gold star swaps colour gold to white once, cleanly, all together.
3.0-3.5s — ALL THREE SNOWMEN FIRE AT ONCE. Three snowballs leave together on three different curved paths and converge on the sleigh. Santa dives flat behind it with both arms forward; the elf throws a present up over his head as a shield and it spins there. The three snowballs hit in quick succession, each bursting into its OWN SMALL white splat one after another — three separate small splats, NOT one big one, NOT a combined explosion, NOT a flash, NOT a shockwave, and the figures stay clearly visible through all of it. The sleigh is flung up onto both runners and crashes down.
3.5-4.0s — Santa is blasted backwards behind the sleigh with his boots kicking in the air, the elf tumbles over sideways and scrambles straight back up, and five presents burst out of the pile and scatter SIDEWAYS along the bottom band of the rectangle — rolling, spinning, tipping and skidding, each tumbling end over end, all of them still inside the SAFE BOX. The three snowmen throw all six stick arms up in victory together, scarves flying, bouncing on their bases, mouths stretching into huge grins. In the very last frame the presents are STILL rolling and rocking, the snowmen are STILL bouncing, Santa's boots are STILL kicking, the elf is STILL moving and the picture is STILL completely full.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE AND NEVER DRIFTS. The snowmen, the sleigh, Santa, the elf and the presents are the same number of bulbs tall and wide in the final frame as in the first frame. The artwork NEVER scales up, never grows, never inflates, never creeps outward and never drifts across the door. The lit rectangle keeps exactly the position and exactly the size it has in the reference image.

THE CROWD IS CASUAL, RELAXED AND ALREADY HAPPY — AND ALREADY MOVING IN THE VERY FIRST FRAME. Not an audience waiting for something. Nobody stands frozen staring at the garage, nobody holds still and then reacts, there is no build-up and no big synchronised cheer. They are neighbours hanging about on a driveway on a cold night, chatting, laughing at each other, glancing over at the lights and back at their friends. They are ALL seen FROM BEHIND — no face is ever turned toward camera. At 0.0s every person is ALREADY MID-MOVEMENT; there is NO still opening frame.
0.0-0.5s — the person holding the raised phone shifts weight to the other foot mid-shot; two adults beside them are mid-conversation, one shrugging.
0.5-1.0s — the woman in the long fur-collared coat laughs and rocks back on her heels, shoulders shaking; a child beside her bounces on the spot and swings an arm up mid-bounce.
1.0-1.5s — two people lean into each other and one points lazily at the lights without turning round; someone at the right hunches, hands deep in pockets, and blows a long fog of breath.
1.5-2.0s — a woman at the left leans sideways into the person beside her and says something; they both laugh; another scratches under their bobble hat and looks away from the garage entirely.
2.0-2.5s — two people knock shoulders and one claps once, casually; a child twists round to tug a sleeve then swings back; a couple sway, arms linked.
2.5-3.0s — scattered easy laughter ripples through the group, a few loose claps at different moments, never together; one adult crouches to say something to a kid; another points out at the lights.
3.0-3.5s — the person at the left lowers their phone, wipes their eyes laughing and says something sideways; a kid scrambles up onto tiptoes; two heads tip together.
3.5-4.0s — a few people applaud loosely, hats bobbing, breath fogging, someone waves an arm overhead at a neighbour, someone else is already turning to talk to the person behind them.
Coats crease, hats bob, breath fogs, snow compresses under boots, shoulders shake with laughter. NOBODY IS EVER STILL and nobody is waiting.

COLOUR IS THE POINT: a loud multicoloured light show the whole four seconds — red, green, blue, pink, orange, purple, yellow, turquoise and warm white all present and clearly separated at every moment. It must NEVER drop back to one or two colours and NEVER go white.

Every change is rendered by bulbs switching on and off across the grid — chunky and stepped, like an animated light-bulb sign — but the movement it describes is continuous and flowing, never a jump between unrelated drawings.

THE CURTAIN — CRITICAL: it stays a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the oak garage door behind is plainly visible through those gaps, especially in the unlit band around the picture. The horizontal gap between neighbouring strands is visibly wider than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular, never a square pixel matrix. The bulbs are small round points of light strung along thin BLACK cords. The unlit area is NOT a solid coloured field — it is simply dark garage door with dull unlit bulbs and faint dark cords, with NO filled background, NO coloured backdrop and NO saturated panel of colour behind the figures at any time. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs, no writing of any kind anywhere in the lights or the frame. No captions, no subtitles, no watermark.

AUDIO: natural outdoor sound only — no music, no score, no background song. Cold night air, a loose crowd chatting and laughing at different moments, scattered uneven clapping, boots in snow, the faint electrical hum and tick of a big light display, breath fogging. No commentary, no voice-over.

LOOK: real iPhone night video, handheld, tack-sharp, candid UGC. Slight sensor noise in the shadows, no cinematic grade, no slow motion, no speed ramp.
````

### C07 — Car-window POV — the snowman wins

**In the cut:** `starting_frames/v29_c07_g1.png` → `clips/v29_c07_g1.mp4`

#### Image prompt — `starting_frames/v29_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `40058517-9846-48c1-88e3-d48519a63b52`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_201212_40058517-9846-48c1-88e3-d48519a63b52.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_28_assets/starting_frames/v28_c07_g1.png` · Higgsfield media `058a0783-9754-481c-a79a-04c0deb1154c`

````text
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a WARM CREAM STONE gable with dark bronze trim and dark bronze window frames, instead of the house in the reference.

2. A COMPLETELY DIFFERENT PICTURE IN THE LIGHTS - a funny cartoon scene, drawn chunky and simple out of the bulbs: THE SNOWMAN HAS WON. A GIANT THREE-BALL SNOWMAN fills the full height of the lit area, standing square to us, both twiggy stick arms thrown up in the air in victory, a black top hat tipped back on his head, a bright orange carrot nose, coal eyes and a wide grin of coal teeth, a turquoise scarf flapping out to one side. SANTA IS STUCK HEAD-FIRST IN THE SNOWMAN'S BELLY - only his red trousers, his black belt and his two legs stick straight out of the middle snowball, boots kicking apart in the air, one boot flying off and a red-and-white striped sock showing underneath. Santa's red hat lies fallen in the snow at the snowman's base. Two chunky curved motion arcs sweep out from Santa's kicking legs and a small puff of snow bursts out around his waist. Small gold stars scattered around the pair. Fully clothed cartoon figures, a silly slapstick pose and nothing more.

3. A different parked car at the kerb - a mustard-yellow pickup truck instead of the car in the reference - and a snow-covered hedge at the right edge.

THE ARTWORK STAYS INSIDE THE CURTAIN: the whole scene sits within the curtain rectangle with a clear band of dark unlit gable above it, below it and at both sides. The snowman's hat and raised stick arms do not touch the top edge, his base does not touch the bottom edge, and nothing touches the side edges. Nothing lit appears on the roof, the trim, the window frames or the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights.

THE CURTAIN - CRITICAL: it is a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the cream stone gable behind is plainly visible through those gaps, especially in the unlit areas around the picture. The bulbs are small round points of light strung along thin cords - you can count them. Dense enough that the picture reads cleanly, but it must still obviously be a hanging curtain of strands, never a screen.

IMAGE QUALITY - CRITICAL: a real iPhone night photo, tack-sharp edge to edge, clean crisp bulbs with no smeared bloom, the stone texture and the wet road reflections clearly resolved, correct exposure with no blown-out white and no crushed black, NO motion blur, NO soft focus, NO grain, NO haze. Candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v29_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `1e71f6f1-19ef-40f2-a65b-ea60ad5de046`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260915_221438_1e71f6f1-19ef-40f2-a65b-ea60ad5de046.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v29_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_29_assets/starting_frames/v29_c07_g1.png` · Higgsfield media `65c44162-9df0-40b4-8a50-f0fe41d6dd40`

````text
THE REFERENCE IMAGE IS THE LAW. The attached start frame is the first frame of this clip and it defines EVERYTHING: the night street shot from inside a moving car through the open side window, the wet reflective road, the warm cream stone gable with dark bronze trim, the big lit LED curtain filling that gable edge to edge, the mustard-yellow pickup truck at the kerb, the snow-covered hedge at the right edge, the street lamp far left, the neighbouring houses glowing down the street. Do not redesign the house. Do not change the colour of anything. Do not re-draw the artwork in the lights into a different picture. Every single thing visible in frame one stays exactly what it is for all four seconds. The ONLY thing that changes is that the figures drawn in the lights are ALIVE and MOVING, and the car keeps driving forward.

THE LIT ARTWORK. Inside the curtain, drawn entirely in glowing coloured bulbs, is a GIANT THREE-BALL SNOWMAN filling the full height of the lit area, standing square to us, both twiggy stick arms thrown up in victory, black top hat tipped back on his head, bright orange carrot nose, coal eyes, a wide grin of coal teeth, a turquoise scarf flapping out to one side. SANTA IS STUCK HEAD-FIRST IN THE SNOWMAN'S BELLY — only his red trousers, his black belt and his two legs stick straight out of the middle snowball, boots kicking apart in the air, one boot already flying off with a red-and-white striped sock showing underneath. Santa's red hat lies fallen in the snow at the snowman's base. Two chunky curved motion arcs sweep out from Santa's kicking legs and a puff of snow bursts out around his waist. Small gold stars are scattered around the pair.

EXIST ONLY INSIDE THE LIGHTS. The snowman and Santa are a PICTURE MADE OF LIGHT BULBS hanging on the front of the house. They are not real objects, they are not in the street, they never step out of the curtain, they never cast light onto the road, nothing about them ever overlaps the roof line, the windows, the hedge or the pickup truck. Everything they do happens inside the rectangle of the lit curtain and nowhere else.

HOW THE PICTURE IN THE LIGHTS IS DRAWN. Chunky simplified cartoon shapes built from rows of individual glowing bulbs, like an animated pixel sign. When a limb moves, the bulbs that made the old position go dark and the bulbs of the new position light up. The line weight stays thick and the shapes stay simple and readable from across the street at all times.

CAMERA — THIS IS DRIVING, NOT ZOOMING. The car is DRIVING FORWARD along the street toward the house, filmed out of the open side window. A strict one-way size ladder: at 0.0s the lit gable is exactly the size it is in the reference frame; at 1.0s it is clearly bigger; at 2.0s bigger still; at 3.0s bigger still; at 4.0s it is the biggest it has been. HARD NEGATIVE ON DIRECTION: the house NEVER gets smaller for even a single frame, the car NEVER reverses, never backs up, never slows to a stop, and the scene is NEVER played in reverse. The mustard-yellow pickup truck is the proof of forward travel — it starts small down the street, grows steadily as we approach it, slides toward the near edge of frame and passes out of shot before the clip ends. The hedge at the right edge sweeps past faster than the house. The operator pans slowly to the side to keep the lit gable in frame as we pass. Gentle suspension rock and a slight rolling-shutter wobble, handheld, real, imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. The camera itself IS the phone, so we see ONLY what a passenger sees. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object in the foreground or along the bottom edge at any moment. The only foreground element allowed is the car's own dark window frame at the very edge of frame, exactly as it appears in the reference image.

CONTINUOUS MOTION. The figures in the lights are ALREADY MOVING IN FRAME ONE — there is no still opening moment, no ease-in, no settling. From the very first frame the legs are kicking and the arms are pumping. Motion never stops, never pauses, never rests for a single frame across the whole four seconds.

FLASHING IS NOT MOVEMENT. Bulbs turning on and off in place is NOT motion. Motion means BODIES TRAVELLING — a leg swinging through a wide arc, a boot tumbling across the frame, a hat jumping up and dropping back down, a scarf whipping from one side to the other. Every movement must cover a real distance of at least one third of the height of the lit rectangle. Do not substitute twinkling, sparkling, colour cycling or chasing lights for movement.

THE THREE-FRAME TEST. Take any three frames one second apart. Santa's legs must be in three completely different positions, the loose boot must be in three completely different places, the snowman's stick arms must be at three completely different angles, and the top hat must be at three different heights. If any two of those three frames look alike, the animation has failed.

BEATS — every half second, all of these happening AT THE SAME TIME.
0.0-0.5s: Santa's two legs scissor wide apart then snap together, kicking hard. The loose boot is tumbling end over end up and to the left, already in the air in frame one. The snowman's stick arms punch straight up. The top hat hops up off his head about a hand's width and starts to come back down. The turquoise scarf whips out to the right. The snow puff around Santa's waist bursts wide.
0.5-1.0s: The legs scissor the opposite way — left leg high, right leg low — bending hard at the knee. The boot reaches the top of its arc and starts to fall. The stick arms swing out wide to the sides. The top hat lands back on his head and tips further back. The scarf reverses and whips out to the left. The snow puff shrinks back in. The two curved motion arcs beside the legs redraw at a new angle.
1.0-1.5s: Both legs kick straight up together and the black belt jumps. The striped sock flexes. The boot tumbles down past the snowman's belly. The stick arms punch up again, higher. The top hat jumps again. The scarf snaps out to the right, straight and rigid. A fresh snow puff bursts.
1.5-2.0s: The legs flail in a wide circle, one drawing a full loop. The boot lands and bounces once in the snow at the base beside Santa's fallen red hat. The stick arms shake fast side to side in celebration. The top hat spins a half turn on his head. The scarf coils and uncoils. The coal grin widens — a bulb added at each end.
2.0-2.5s: The legs scissor wide again, faster. Santa's trousers shake as if he is struggling. The stick arms sweep down and across his belly then back up. The top hat lifts and tilts to the opposite side. The scarf whips left again. The gold stars around the pair pop bigger one after another in a wave from left to right — not a continuous twinkle, one clean wave.
2.5-3.0s: One leg kicks so high the boot line nearly touches the snowman's coal grin, the other leg braces low. The loose boot tumbles back up into the air off the bounce. The stick arms punch up together. The top hat hops. The scarf snaps out to the right. The snow puff bursts wide again.
3.0-3.5s: Both legs pedal in fast alternating circles like a bicycle. The stick arms shake overhead. The coal eyes squash into happy curved arcs. The top hat tips right back off the crown of his head. The scarf whips left. The motion arcs beside the legs redraw thicker.
3.5-4.0s: The legs scissor one last time, wide and hard. The boot is still tumbling in the air, in a different position from every earlier beat. The stick arms are thrown up in full victory. The top hat lands square. The scarf streams out to the right. The final frame is clearly different from the first frame — nothing has returned to its starting position.

DO NOT LOOP AND DO NOT RESET. The picture in the lights must never jump back to the arrangement it had in frame one. The animation runs continuously forward through the four seconds and ends somewhere new.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE RELATIVE TO THE HOUSE. The lit rectangle grows on screen only because the car is getting closer. Inside that rectangle the snowman always occupies exactly the same proportion of the curtain that he does in the reference frame. He never grows, never shrinks, never walks toward the camera, never scales up.

THE SAFE BOX. Draw an invisible rectangle exactly matching the lit area of the curtain in the reference frame. Every part of the snowman, of Santa, of the boot, of the hat, of the scarf, of the motion arcs, of the snow puff and of the gold stars stays inside that rectangle for all four seconds. Nothing crosses the roof line. Nothing crosses the edge of the curtain. Nothing spills onto the brickwork, the windows, the road, the hedge or the truck.

NOT A FLAT PANEL OF LIGHT. The curtain is NOT a video screen, NOT an LED wall, NOT a projection. It is a hanging curtain of separate vertical strands of bulbs. You can see the dark gable and its window outlines faintly through the gaps between strands. The strands sway very slightly in the cold air the whole time, and the picture drawn on them sways with them.

THE CURTAIN — CRITICAL. Visible individual bulbs on visible individual vertical strands, with real gaps between them. The strands hang from the top edge of the gable straight down. The wire is BLACK. Any unlit bulb is dark, never white, never clear, never silver.

ABSOLUTELY NO TEXT. No letters, no words, no numbers, no logos, no captions, no watermark anywhere in the frame or inside the lights.

AUDIO. Natural in-car sound only — tyres rolling on wet tarmac, a quiet engine, cold air coming through the open window, one short amused breath from the passenger. No voice, no dialogue, no music, no score, no background song, no sound effects.

LOOK. Real phone footage shot at night from a moving car, slightly noisy in the shadows, the lit curtain blooming a little against the dark, warm reflections smearing on the wet road, cold night air, photographic and unpolished.
````
