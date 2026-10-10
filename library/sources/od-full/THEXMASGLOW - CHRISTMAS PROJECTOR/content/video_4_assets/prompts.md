# Video 4 - prompts

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_4.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

**THEXMASGLOW - CHRISTMAS PROJECTOR**
Working title: Christmas Projector

*Historical initial stage:* B-roll C02-C07 generated as starting frames only, one generation each. C01 (the hook) is generated and picked - frame `v4_c01_g6.png`, clip `v4_c01_g5.mp4`. C02-C07 still have no clips.

## Planned cut

```
C01 -> C02 -> C03 -> C04 -> C05 -> C06 -> C07
        ^--------- this round: C02 to C07 ---------^
```

C01 was not generated in the B-roll round - Daniel asked for B-roll only. It was generated in a later round and is archived below; see `## C01`.

## Brief as given

> Here is what I want you to do now. Generate me the images for the next 3 videos, only for the broll (just without the hook). The same style as you did for video 2 and 3. Different tables, backgrounds, houses, kids and animations. Try to make the animation even more insane. Don't ask me how.
>
> All the images must be extremly high quality, perfect light, iphone shots, nothing blurish. Use gpt image 2.5 Sunburst, 2k, mid quality settings, 9x16.

## Look pack chosen - Craftsman, sage green / oak / burgundy

One coherent house carried across all seven frames, different from v2 and v3:

| element | v4 |
|---|---|
| sleeve | charcoal-grey cable-knit wool |
| table (C02) | dark-stained quarter-sawn oak trestle, medullary ray flecks, matte hand-rubbed oil |
| living room (C02) | dark green glazed-tile fireplace, heavy oak mantel, leaded-glass oak bookcase, burgundy + antique brass baubles, brass floor lamp with amber mica shade |
| counter (C03, C04) | honed charcoal soapstone |
| kitchen (C03, C04) | sage-green shaker, unlacquered brass cup pulls, cream zellige, black cast-iron range (left in C03, right in C04) |
| door (C05 F1) | four-panel deep matte forest green, oil-rubbed bronze knob and escutcheon, stained oak frame |
| great room (C05 F2) | sage walls over quarter-sawn oak wainscoting, warm cream tongue-and-groove vault with dark stained oak rafters, clinker brick fireplace, burgundy roll-arm sofa |
| knitwear | charcoal-grey and cream fair-isle snowflake band, oatmeal trousers, mustard socks |
| bedroom (C06) | girl ~7, long auburn hair; butter-cream tongue-and-groove slopes, white rafters, sage-green bed, burgundy quilt |
| great room (C07) | barn great room, two-storey dark clinker brick chimney breast, whitewashed reclaimed timber, blackened steel rail, dark stained king-post trusses; girl ~8 long wavy auburn, boy ~5 short auburn |
| **projection signature** | **a long procession of glowing gold carol singers and lantern carriers winding along the village lane** |

## The escalation clause

Daniel asked for the animation to be "even more insane". One clause was appended **identically** to every projection paragraph in v4, v5 and v6, placed after the falling-light clause and before "It stays ONE continuous night-sky picture":

```text
; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth.
```

## Settings

`gpt_image_2_5 · variant sunburst · quality medium · resolution 2k · aspect_ratio 9:16 · count 1 · use_unlim false` - output 1520 x 2688. Workspace Oneofone1.

## Lineage

Every frame in this round is a v3 prompt reused per CLAUDE.md rule 3 - pasted verbatim, with only the nouns that physically differ changed. Nothing describing motion, camera, pacing or framing was reworded.

---

## C01 - The hook: taping Santa to the ceiling, then falling off the ladder

*Section:* Hook
*Status:* PICKED - frame `v4_c01_g6.png`, clip `v4_c01_g5.mp4`
*What it is:* a mom up a step ladder inside a decorated living room, taping a big inflatable Santa flat to the ceiling. A second and a half in she loses her footing and comes off the ladder. A "fail in the beginning" hook, modelled on the two LED-curtain videos that performed.

- frames: `v4_c01_g1.png` `v4_c01_g2.png` `v4_c01_g3.png` `v4_c01_g4.png` `v4_c01_g5.png` `v4_c01_g6.png` (**g6 PICKED**), plus the tall-room set `v4_c01_g7.png` `v4_c01_g8.png` (**both approved**) and `v4_c01_g9.png` `v4_c01_g10.png` `v4_c01_g11.png` (awaiting review)
- clips: `v4_c01_g1.mp4` `v4_c01_g2.mp4` `v4_c01_g3.mp4` `v4_c01_g4.mp4` `v4_c01_g5.mp4` (**g5 PICKED**)
- references: `v4_c01_r1.png` `v4_c01_r2.png` (the two tall-room photos Daniel attached; used only for g7 and g8)

*Not reused from anything.* This is the first hook on the projector and it was written fresh. Nothing on this drive animates a fall.

### Brief as given

> a mom / dad in the house trying to install a decoration and falls of the ladder. Like a fail in the beginning
>
> Now I want you to make me 2 variation of this but for a taller room, like in the images attached. No animations on the walls, christmas decorated room / Just the starting frame

Standing requirements carried into every prompt below: a slim clean band at the top of the frame for the CapCut caption; "all the images must be extremly high quality, perfect light, iphone shots, nothing blurish"; held-iPhone look with no zooms and no cuts; clips generated dry because the music is added in CapCut.

---

### Image prompts

**Settings** - `gpt_image_2 · quality medium · resolution 2k · aspect_ratio 9:16 · count 1 · use_unlim false` - output 1520 x 2688. Workspace Oneofone1. Takes g1-g6 are pure text-to-image, **no references attached**. Takes g7-g8 each attach one room photo.

Note for the archive: `show_generation_by_ids` reports `params.model` as `videotape-alpha` on these records. The `gpt_image_2` string lives on the item's top-level `model` field. Do not copy `videotape-alpha` into a future call.

#### g1 - REJECTED

job `8380e5f3-ae2a-4b04-bcf2-278e8a3746f7`

```text
Candid vertical iPhone photo shot from low down on the living room floor looking steeply up, so the whole step ladder and the ceiling fill the frame. A mom in her mid-30s with dark hair in a messy bun, wearing a red Christmas sweater and leggings, is balanced on the second step from the top of an aluminium step ladder, reaching up with one arm to hold a big inflatable Santa Claus decoration against the white ceiling while her other hand tries to tear a strip of duct tape off a roll with her teeth. The inflatable Santa is oversized and drooping, one arm of it flopping down into her face. Two used strips of tape hang loose from the ceiling. Her body is twisted and off-balance, one knee braced against the ladder. Cosy living room below: lit Christmas tree, sofa, wrapping paper and an open decorations box on the rug. Warm indoor evening light, handheld amateur snapshot realism, slight grain, sharp and very high quality, realistic textures. Keep a slim clean band of plain ceiling at the very top of the frame for a caption.
```

**Why it failed:** the Santa is *drooping off* the ceiling, held in her hands, not taped to it. The whole hook depends on Santa already being fixed up there before she falls - if she is holding him, the fall reads as her dropping a balloon, not as a decoration going wrong.

#### g2 - REJECTED

job `85e175db-91fb-4762-9fa5-1c21095a019f`

```text
Candid vertical iPhone photo taken from inside a cosy American family living room, evening. A mom in her mid-30s, light grey sweater, jeans and fluffy socks, stands near the top of a wooden step ladder, stretching up on tiptoes with both arms over her head, pressing a large inflatable Santa Claus Christmas decoration flat against the white ceiling while trying to stick it there with a roll of clear packing tape held in one hand. The inflatable Santa is big and floppy and sagging down over her head and shoulders, clearly not staying up. Strips of tape are already stuck to the ceiling around it, one strip dangling loose. The ladder is slightly wobbling, one of her feet lifted off the step. Decorated Christmas tree with warm lights in the background, sofa, coffee table with a mug, garland on the mantel. Warm cosy interior lighting from a lamp and the tree, natural handheld amateur snapshot look, slight grain, nothing blurry, very high quality, sharp detail, realistic skin texture. Leave a slim clean uncluttered band of ceiling across the very top of the frame for a caption.
```

**Why it failed:** same defect. "sagging down over her head and shoulders, clearly not staying up" is me describing the failure I wanted *later in the video*, and the image model rendered it as the state of the still. The line that caused it is mine.

#### g3 - REJECTED

job `917aa37f-619b-4c89-8236-1c041bc42ea2`

```text
Candid vertical iPhone photo of a cosy open-plan American living room in the evening, camera at normal standing height across the room, wide enough to see the whole scene. A mom in her mid-30s, blonde ponytail, cream cable-knit sweater and jeans, stands on the top platform of a wooden step ladder in the middle of the room with both hands above her head, pressing a huge inflatable Santa Claus decoration up against the white ceiling and taping it with brown packing tape. The inflatable Santa is enormous and clearly too heavy, sagging off the ceiling, one side already peeling away with a long strip of tape hanging down. A roll of tape sits on top of the ladder, scissors on the floor. She is leaning to one side, the ladder tilted slightly on the rug. Behind her: a decorated Christmas tree with warm lights, a garlanded fireplace, sofa with cushions, a cardboard decorations box open on the floor. Warm cosy lamp and tree lighting, handheld amateur snapshot look, slight grain, nothing blurry, very high quality and sharp, realistic skin and fabric detail. Reserve a slim clean uncluttered band across the very top of the frame for a caption.
```

**Why it failed:** third variant of the same bug - "sagging off the ceiling, one side already peeling away". All three of batch 1 died on the same line because I wrote the same idea three ways instead of removing it.

#### g4 - REJECTED

job `d2f8b3ce-bdde-48f8-a9d3-5dff1b7485ff`

```text
Extremely high quality candid vertical iPhone photo, shot from across a cosy American family living room at chest height with a slight upward tilt, evening.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is ALREADY STUCK TO THE WHITE CEILING, lying flat on its back against the ceiling, facing down into the room, held up by five or six criss-crossed strips of silver duct tape running over its arms, legs and belly onto the plaster. It is firmly taped up there, not falling, not draped over anyone. One long strip of tape has peeled and curls down loose.

A mom in her mid-30s, blonde hair in a ponytail, cream cable-knit sweater, jeans and fluffy socks, stands on a wooden step ladder directly under it, reaching up with both arms to smooth another strip of tape onto Santa's boot, standing on tiptoe, a roll of duct tape hooked on her wrist.

Behind and below: a decorated Christmas tree with warm lights, a sofa with cushions, an open cardboard decorations box on the rug, scissors on the floor.

LIGHTING AND QUALITY: perfect warm cosy interior lighting from a floor lamp and the tree, clean and even on her face and on the ceiling, every surface sharp and in focus, crisp detail in the tape, the vinyl sheen of the inflatable and the knit of her sweater. Natural handheld iPhone snapshot look, realistic skin texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: place the taped Santa in the upper middle of the frame and keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
```

**Why it failed:** the Santa is finally taped to the ceiling - the `THE KEY ELEMENT` block fixed that - but "from across a cosy American family living room at chest height" put the camera too far back. She reads as a small figure in a wide room, which kills a hook. Daniel: across the room, chest height.

#### g5 - REJECTED

job `8b9aee3a-9e83-47b9-9175-0eaacc3e69dd`

```text
Extremely high quality candid vertical iPhone photo, camera low near the living room floor looking steeply up at the ceiling, evening, cosy American home.

THE KEY ELEMENT: a big inflatable Santa Claus decoration is TAPED TO THE WHITE CEILING above, lying flat against it and facing down at the camera, pinned there by many criss-crossed strips of brown packing tape stretched over its arms, hat and belly onto the plaster. Clearly stuck up there. Two loose ends of tape dangle down. A few older torn tape strips are still stuck to the ceiling nearby.

A mom in her mid-30s with dark hair in a messy bun, red Christmas sweater and leggings, stands near the top of an aluminium step ladder on the right of the frame, seen from below, both arms stretched overhead pressing another strip of tape across Santa's arm, her face tilted up and concentrating.

Below her: a lit Christmas tree, sofa, wrapping paper and an open decorations box on the rug.

LIGHTING AND QUALITY: perfect warm even interior lighting, the ceiling well lit and clean, no harsh shadows, everything tack sharp and in focus, crisp detail in the tape strips, the glossy inflatable vinyl and her sweater. Natural handheld iPhone snapshot realism, realistic skin texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of Santa and of tape, for a caption.
```

**Why it failed:** over-corrected the other way. "camera low near the living room floor looking steeply up" is a floor-level worm's-eye view - the ceiling dominates, she is a silhouette, and there is nowhere for the fall to land in frame.

#### g6 - PICKED

job `34ab4b0f-7a4e-4383-9120-8602e2eeed2e` · result `hf_20260919_204803_34ab4b0f-7a4e-4383-9120-8602e2eeed2e.png`

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a step ladder in a cosy American living room, evening. We see her from behind at three-quarters, her raised arms and the ceiling in front of her.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING in front of her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing on the second step from the top of a wooden step ladder, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand.

Around them: a decorated Christmas tree with warm lights to the side, garland on a mantel, a mug on the coffee table, an open decorations box on the rug.

LIGHTING AND QUALITY: perfect warm cosy interior light from a lamp and the tree, clean and even across the ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
```

**Why it won:** "slightly behind and below ... we see her from behind at three-quarters" is the camera position that made it work. Close enough that she fills the frame, low enough that the ceiling and the taped Santa are both visible over her shoulder, and *behind* her so there is empty floor in the lower third for her to land in. Every clip below animates off this frame.

---

### The tall-room variations - g7 and g8

Daniel asked for two variations of the picked frame in a taller room, with two photos attached, and said "No animations on the walls" - meaning the projector is OFF in the hook and the projected light that saturates both reference photos must not carry over.

Per CLAUDE.md rule 3 the g6 prompt was pasted and only the nouns that physically differ were changed: the room, and the step ladder becoming a tall A-frame ladder because a step ladder cannot reach a double-height ceiling. `THE KEY ELEMENT`, `LIGHTING AND QUALITY` and `FRAMING` are byte-identical to g6 apart from the ceiling being "high above her".

A `TWO THINGS CHANGE FROM THE REFERENCE` paragraph was added to kill the projection. This is the same reversed technique the C05-C07 real-house round used - there the reference houses were undecorated and shot in daylight, so each prompt carried an explicit two-things-change paragraph. Here the references are *over*-decorated with projected light and the paragraph removes it.

**References attached**

| slot | file | why |
|---|---|---|
| g7 @Image 1 | `references/v4_c01_r1.png` | the two-storey open living room - open staircase, garlanded balcony hung with stockings, kitchen through the opening at left, tall window at right, patterned terracotta rug, big lit tree |
| g8 @Image 1 | `references/v4_c01_r2.png` | the barn-style vaulted great room - dark exposed timber trusses, arched front door, balcony, kitchen island with rattan pendants, cream sectional |

media ids `f0ade236-59f7-4299-b680-818d3b2934a1` (r1), `4e57238e-ef76-46f4-a112-e081eda53907` (r2)

#### g7 - APPROVED

job `23797b37-302e-4827-a64d-6bfa5acff602` · `gpt_image_2 · 9:16 · 2k · medium` · ref `f0ade236-59f7-4299-b680-818d3b2934a1` role `image`

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the double-height Christmas living room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the two-storey open living room with the open staircase and the garlanded balcony railing hung with stockings, the kitchen through the opening at the left, the tall window at the right, the patterned terracotta rug, the big lit Christmas tree. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the walls and the balcony are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

LIGHTING AND QUALITY: perfect warm cosy interior light from the lamps and the tree, clean and even across the high ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
```

#### g8 - APPROVED

job `4579c34e-70dd-411a-951e-29607cba6a56` · `gpt_image_2 · 9:16 · 2k · medium` · ref `4e57238e-ef76-46f4-a112-e081eda53907` role `image`

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the vaulted Christmas great room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the barn-style vaulted great room with the dark exposed timber trusses across the ceiling, the arched front door, the balcony above, the kitchen island with rattan pendant lights, the cream sectional sofa, the lit Christmas tree and the garlands. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the timber trusses and the walls are plain plaster and plain dark wood, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the pendant lights and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE VAULTED CEILING high above her, between the timber beams, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the vaulted space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

LIGHTING AND QUALITY: perfect warm cosy interior light from the pendants and the tree, clean and even across the high ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
```

#### g9, g10, g11 - three more, FOR REVIEW

Daniel: *"The ones you generated to for the taller livingroom are good / Now I want you to make me 3 more variations and don't forget that I need a little space at the top"*.

g7 and g8 are approved, so these are **three more rolls of the two approved prompts**, not three new rooms. The only text that changed is the `FRAMING` line, because the top band is the one thing he named. Everything else - `THE ROOM`, `TWO THINGS CHANGE FROM THE REFERENCE`, `THE KEY ELEMENT`, the wardrobe, the ladder, the camera position and `LIGHTING AND QUALITY` - is byte-identical to g7 / g8.

| take | job | base prompt | reference |
|---|---|---|---|
| g9 | `48614108-fe4b-45a5-88a3-4ca7c37d7ee6` | g7 | `v4_c01_r1.png` - media `f0ade236-59f7-4299-b680-818d3b2934a1`, role `image` |
| g10 | `7ad5dcc5-c5a7-4b4e-8ca6-bbbaa98fb2c5` | g8 | `v4_c01_r2.png` - media `4e57238e-ef76-46f4-a112-e081eda53907`, role `image` |
| g11 | `0930d451-db6f-4174-99df-4cbc3322475d` | g7 | `v4_c01_r1.png` - media `f0ade236-59f7-4299-b680-818d3b2934a1`, role `image` |

Two rolls off r1 and one off r2 because the r1 room - open staircase, garlanded balcony, tall window - has more vertical structure behind a tall ladder, so it is the room worth two attempts. Settings unchanged: `gpt_image_2 - quality medium - resolution 2k - aspect_ratio 9:16 - count 1 - use_unlim false`, output 1520 x 2688.

**The FRAMING line, the only change.** g7 / g8 read:

```text
FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
```

g9 / g10 / g11 read:

```text
FRAMING: leave a slim clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
```

Two things were added and both are deliberate. The band is given a **measurement** - "roughly the top eighth of the frame" - because "slim" is not a quantity and the model had been reading it as whatever was left over. And the **enumerated exclusion list** names the objects that had actually been intruding into the band (Santa himself, the loose tape ends, the timber trusses in the barn room, the balcony garland) rather than saying "objects" in the abstract. The closing sentence is the standing rule from `feedback_hook_frame_headroom` written into the prompt: headroom is never bought by pulling the camera back, because that shrinks the subject and kills the hook.

**Result, for review:**

- **g9** - r1 room. Clean band across the top, Santa taped flat with the tape crossing his legs and arms, ladder tall and clearly off the floor, balcony and stockings behind her. Projection is gone.
- **g10** - r2 room. The cleanest top band of the three. Santa is taped between the timber trusses and the tape reads as real duct tape. Projection is gone.
- **g11** - r1 room, a second roll. The strongest read of Santa, biggest in frame - and **the tightest top band of the three**; his arm and the tape come close to the top edge. Flagged, not re-rolled.

---

#### g12, g13 - neutral colour, iPhone look, FOR REVIEW

Daniel: *"A little more and not that orangesh colors, more iphone shots / Extremly high quality, perfect lightning, nothing blurish, 2 more options"*.

Three notes in one message: **more top space**, **kill the orange cast**, and **make it read as a phone snapshot, not a graded photo**. g12 is another roll of the g7 base (r1 room), g13 of the g8 base (r2 room). Three prompt blocks changed and one setting. Everything else - `THE ROOM`, `TWO THINGS CHANGE FROM THE REFERENCE`, `THE KEY ELEMENT`, the wardrobe, the ladder, the camera position - is byte-identical to g7 / g8.

| take | job | base prompt | reference |
|---|---|---|---|
| g12 | `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74` | g7 | `v4_c01_r1.png` - media `f0ade236-59f7-4299-b680-818d3b2934a1`, role `image` |
| g13 | `47abd381-4c53-4768-b2b4-cb5c6a747792` | g8 | `v4_c01_r2.png` - media `4e57238e-ef76-46f4-a112-e081eda53907`, role `image` |

**Settings** - `gpt_image_2 - aspect_ratio 9:16 - resolution 2k - count 1 - use_unlim false`, output 1520 x 2688. **`quality` moved `medium` -> `high`.** That is a settings change, not a prompt change, and it is the response to "extremly high quality" and "nothing blurish" - no amount of prose about sharpness substitutes for the sampler doing more work.

**Change 1 - a new `COLOUR` block, inserted before `LIGHTING AND QUALITY`.** The orange cast was never addressed by the prompt at all. g7 / g8 said "warm Christmas lighting" and the model correctly laid a warm grade over the *whole picture*. The fix is not to remove the warmth - the tree and the lamps must still be warm - it is to separate the warm *sources* from the overall *white balance*. So the block names the neutral target, then lists what is NOT wanted as colours rather than as a vague "less warm":

```text
COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and walls read as clean white and off-white plaster, her sweater reads as true light grey, the wood reads as natural wood, the rug keeps its own colours. The Christmas tree lights and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.
```

g13's copy swaps only the nouns that physically differ in the barn room: *"The vaulted ceiling reads as clean white and off-white plaster ... the timber trusses read as natural dark wood, the sectional reads as true cream ... the Christmas tree lights and the pendants are warm points of light ..."*.

**Change 2 - `LIGHTING AND QUALITY` rewritten.** "More iphone shots" is a camera-identity instruction, and the old line was written in photography words that pull the opposite way. The rewrite names the device, names the pipeline (wide dynamic range, lifted shadows), and then bans every term that produces softness or a grade:

```text
LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.
```

"No background blur" is in that ban list on purpose. Shallow depth of field is the single strongest tell that a picture is not a phone snapshot, and it had been softening the balcony and the tree in earlier takes.

**Change 3 - `FRAMING`, top eighth -> top sixth.** "A little more" against the g9 / g10 / g11 band, which was already measured. Only the fraction moved; the enumerated exclusion list and the do-not-pull-back sentence are unchanged from g9:

```text
FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
```

**Result, for review:**

- **g12** - r1 room. The orange cast is gone; walls and ceiling read as clean off-white plaster and the sweater reads true grey, with the tree and the balcony garland still warm as points of light. Top band is clear across the full width, though Santa's taped bulk sits just under it - this is the tighter of the two. Santa is taped flat and large with the tape crossing arms, legs and belly, ladder tall and clearly off the floor, stockings and staircase behind her.
- **g13** - r2 room. **The cleanest top band of the pair** - a genuinely empty sixth of plain white ceiling above the trusses. Neutral balance throughout, arched stained-glass door and pendants warm without tinting the room. Santa is taped along a truss and reads slightly smaller in frame than g12.

Both are noticeably sharper than the medium-quality takes, and neither has background blur. Generated once each, not re-rolled.

---

### Video prompts

**Settings** - `seedance_2_5 · mode omni_reference · aspect_ratio 9:16 · generate_audio true · count 1 · use_unlim false · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612`. Duration and resolution vary by take, recorded per take below. The start frame is a ROLE inside `medias`, never a top-level param: every take attaches job `34ab4b0f-7a4e-4383-9120-8602e2eeed2e` twice, once with role `start_image` and once with role `image`.

**Un-turned knobs, recorded because they bit.** Every take below came back with `speedramp: "auto"` and `genre: "auto"` in its params, because neither was ever set. Prose saying "No speed ramp" does not override a parameter that defaults to auto. See the lesson at the end of this section.

#### g1.mp4 - REJECTED

job `36471ab7-0f8c-4a07-bd42-6197dbccc780` · `4s · 720p`

```text
ONE CONTINUOUS HANDHELD TAKE, NO CUTS. Hyper-realistic, natural, like a real phone video a family member shot by accident. The scene, the room, the woman, her clothes, the ladder and the inflatable Santa taped to the ceiling are exactly as in the start frame and never change.

CAMERA: a real person standing a few steps behind her holds the phone at chest height. The camera stays in one place with small natural handheld sway. Between 1.6s and 2.6s it tilts gently DOWN to follow her to the floor, then holds. No zoom, no push-in, no orbit, no slow motion, no speed ramp. The ladder and the rug stay in frame the whole time.

BEATS:
0.0-1.0s - She is up on the step ladder with both arms above her head, pressing a strip of tape onto the inflatable Santa's shoulder. She smooths it with her palm twice, rising slightly onto the balls of her feet on the step, shoulders working, head tilted up.
1.0-1.6s - The strip of tape peels away from the ceiling under her hand. Her weight shifts, her hips swing out to one side and the ladder tips over with her. Her free hand grabs at the air.
1.6-2.6s - She comes down, sliding and scrambling against the tipping ladder, body low and close to it the whole way, and the ladder goes over sideways onto the rug beside her. She does not leap, spin or fly.
2.6-4.0s - She ends up sitting slumped on the rug on her backside next to the fallen ladder, legs sprawled, one hand flat on the floor, chest heaving. The roll of tape rolls a short distance across the rug and stops. She stays down, looks up at the ceiling and lets her head drop back. She does not get up.

HARD RULES: The inflatable Santa stays taped flat to the ceiling for the entire clip and never falls, never detaches, never lands on her. Everything stays low and inside the room. NO object is thrown, launched, flung or flies through the air. No Christmas tree falls, no furniture moves, nothing leaves the frame. She does not bounce, does not roll over, does not somersault. No other people, no pets, no doors opening. No cuts, no jump cuts, no scene change, no second angle. No captions, no text, no on-screen graphics, no logos, no watermark.

AUDIO: natural room sound only - no music, no score, no background song. The rip of tape, a short startled gasp from her, the clatter of the aluminium ladder hitting the floor, then quiet room tone and her breathing. No dialogue.
```

**Why it failed:** did not hold the start frame - the opening frame was re-imagined rather than inherited. The cause was mine: the CAMERA block contains "Between 1.6s and 2.6s it tilts gently DOWN to follow her to the floor". Any camera-move instruction licenses seedance to re-frame, and once it re-frames it re-designs.

#### g2.mp4 - REJECTED

job `63137ca3-5de5-4702-b0ee-5ccbf2818d7a` · `4s · 720p`

```text
THE FIRST FRAME OF THIS VIDEO IS THE ATTACHED START IMAGE, PIXEL FOR PIXEL. This is the most important rule in the clip. Frame 0 is identical to @Image 1 - same camera position, same height, same angle, same distance, same room, same white ceiling, same inflatable Santa taped flat to the ceiling, same step ladder, same woman seen from behind and below in her light grey sweater and jeans, same Christmas tree and furniture in the same places. Nothing is re-imagined, re-framed, re-lit or re-designed at any point.

CAMERA: ONE LOCKED HANDHELD SHOT, filmed by a person standing in the room a few steps behind her, phone held at chest height. The camera stays in exactly the same spot for all 4 seconds with only tiny natural hand sway and micro-jitter. THE CAMERA DOES NOT MOVE: no zoom, no push-in, no pull-back, no dolly, no pan, no tilt up, no tilt down, no crane, no orbit, no rack focus, no slow motion, no speed ramp. The frame does not reframe to follow her - she falls out of the lower part of the frame naturally, the way a real phone video would catch it. NO CUTS, no jump cuts, no second angle, no scene change. No phone, hand, fingers, thumb, arm or any object ever appears in the foreground.

BEATS:
0.0-1.0s - She stays exactly as in the start image, arms above her head, and presses the strip of tape onto the inflatable Santa's shoulder, smoothing it with her palm twice, rising slightly onto the balls of her feet on the step.
1.0-1.6s - The tape peels off the ceiling under her hand. Her weight shifts, her hips swing to one side and the ladder starts tipping over with her. Her free hand grabs at the air.
1.6-2.6s - She goes down with the ladder, body staying low and close against it, sliding and scrambling, and the ladder falls sideways onto the rug. She does not leap, spin, somersault or fly.
2.6-4.0s - She is down on the rug beside the fallen ladder, sitting slumped on her backside with her legs sprawled, one hand flat on the floor, breathing hard, head tipped back looking up at the ceiling. The roll of tape rolls a short way across the rug and stops. She stays down and does not get up.

HARD RULES: The inflatable Santa stays taped flat to the ceiling for the entire clip - it never falls, never detaches, never lands on her. Everything stays low and inside the room. NO object is thrown, launched, flung or flies through the air. The Christmas tree does not fall, no furniture moves, no decorations come down. No other people, no pets, no doors opening. No captions, no text, no on-screen graphics, no logos, no watermark.

AUDIO: natural room sound only - no music, no score, no background song. The rip of tape, one short startled gasp, the clatter of the ladder hitting the floor, then quiet room tone and her breathing. No dialogue.
```

**What changed from g1 and why:** removed the downward tilt entirely and hoisted a `THE FIRST FRAME OF THIS VIDEO IS THE ATTACHED START IMAGE, PIXEL FOR PIXEL` paragraph to the top. That fixed the start frame.

**Why it failed:** Daniel - "very unnatural". The fall itself. The beat list choreographs the fall pose by pose ("hips swing to one side", "sliding and scrambling", "sitting slumped on her backside with her legs sprawled") and seedance animated each described pose in turn, which reads as a performance, not as gravity.

#### g3.mp4 - REJECTED

job `48e780b3-acd8-4004-81c2-9a0db3eef87d` · `4s · 720p`

```text
Real home video. One continuous handheld phone shot, no cuts, camera never moves from where it is in the attached image.

For the first second she is just taping the inflatable Santa to the ceiling - both hands up, pressing and smoothing, nothing dramatic.

Then she loses her footing and falls off the ladder to the floor.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery. The ladder goes over with her and clatters onto the rug. She lands hard, stays down, stunned, and is still on the floor when the clip ends.

The inflatable Santa stays taped to the ceiling the whole time.

No slow motion. No speed ramp. No zoom, no push-in, no pan, no tilt. No cuts, no second angle. No captions or text.

Audio: room tone only, no music - the tape, a short gasp, the ladder hitting the floor, then her breathing.
```

**What changed from g2 and why:** two failed patches, so the prompt was rewritten from scratch per the standing rule - the pose-by-pose choreography was deleted and the fall was described by real-world feel instead ("gravity takes her ... fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder"). Down from ~2600 characters to ~1000.

**Why it failed:** Daniel - "still looks very fake". Closer, but four seconds is not enough room for tape-then-fall-then-stillness; the fall was still being rushed and stylised to fit.

#### g4.mp4 - REJECTED

job `ee938061-a27d-40fa-8714-e370c41c510a` · `5s · 1080p`

Prompt as in g5 below - identical text.

**What changed from g3 and why:** duration 4s -> 5s and resolution 720p -> 1080p. The prompt gained only the beat timings that the extra second bought: "For the first second and a half", and "She stays down on the floor for the last second and a half". This is the standing rule that a missing or rushed beat is a duration problem, not a wording problem.

**Why it failed:** nothing was wrong with it mechanically. Daniel asked for a 5s generation not realising this take already was 5s, so it was resubmitted unchanged as g5. Recorded here as a rejected take because it was not the one picked.

#### g5.mp4 - PICKED

job `6b97b59c-435a-4a21-bf63-78f85c46ec96` · `5s · 1080p` · result `hf_20260919_213150_6b97b59c-435a-4a21-bf63-78f85c46ec96.mp4`

```text
Real home video. One continuous handheld phone shot, no cuts, camera never moves from where it is in the attached image.

For the first second and a half she is just taping the inflatable Santa to the ceiling - both hands up, pressing and smoothing, nothing dramatic.

Then she loses her footing and falls off the ladder to the floor.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second - fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug.

She lands hard and then the room is still. She stays down on the floor for the last second and a half, not moving much, just stunned and breathing, and she is still there when the clip ends.

The inflatable Santa stays taped to the ceiling the whole time.

No slow motion. No speed ramp. No zoom, no push-in, no pan, no tilt. No cuts, no second angle. No captions or text.

Audio: room tone only, no music - the tape, a short gasp, the ladder hitting the floor, then her breathing.
```

**What changed from g4:** nothing. Byte-identical resubmission, a fresh roll at the same settings.

**Why it won:** Daniel - "this last one generated is good, we will use it for video 4".

---

### What was learned

**1. The fall needed a duration, not better words.** Three rewrites at 4s all read as fake. The same prompt at 5s, with the extra second spent on stillness after the landing, read as real. A beat that has to be rushed to fit will be stylised to fit. When a motion note keeps failing, count the actions against the seconds before touching the wording again.

**2. Describe the fall by feel, not by pose.** g2 choreographed it - hips, limbs, landing position - and seedance animated the choreography. g3 said "gravity takes her ... exactly like real footage of someone coming off a ladder" and got closer in one roll. Real-world feel beats a pose list for anything physical.

**3. A camera-move instruction voids the start frame.** g1's "tilts gently DOWN to follow her" was enough to make seedance re-imagine frame 0. There is no such thing as a small camera move in an omni_reference job.

**4. The picked clip still has a cut in it, and prose did not prevent it.** "No cuts" appears in the prompt and the cut happened anyway. Two causes, both mine:

  - The prompt gives seedance three clearly separated activity blocks - a second and a half of taping, the fall, a second and a half of stillness. Separated activity blocks are a seam, and seedance takes seams as permission to cut. The known fix is to carry the body motion across the seam and put the continuity rule FIRST as a hard rule, not last as a trailing negative. This prompt does neither: "No cuts, no second angle" sits in the penultimate line among the other negatives.
  - `speedramp` was never set, so it defaulted to `"auto"` on all five takes while the prose said "No speed ramp". A parameter I had and did not turn.

  Both of these must shape the next seedance prompt written on this drive. Daniel accepted the clip; he did not accept the method.

**5. The Santa has to be taped up in the still.** Three image takes died because I described the decoration failing - which is what happens in the *video* - inside the *still* prompt. A still prompt describes the moment before, not the moment after. This is the same rule as "anything that must move has to exist in the starting frame", read backwards.

---

## C02 - Hands on the box

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW
*What it is:* two hands resting on the closed carton on the dark oak trestle table, the beat before it opens.

- frames: `v4_c02_g1.png` (current)
- clips: none yet

*Reused from* v3 C02 - changed: (a) the sleeve, dark green wool -> charcoal-grey cable-knit; (b) `SECOND - THE TABLE`, creamy white painted farmhouse -> dark-stained quarter-sawn oak trestle; (c) `THIRD - THE BACKGROUND`, classic American Christmas living room -> American Craftsman Christmas living room with the green tile fireplace and leaded-glass bookcase; (d) the table dressing baubles, gold and red -> brass and burgundy. The carton description, the hands clause, the quality tail and the wordmark spelling clause are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c02_g1.png` | owns the geometry - camera position, top-down-ish angle, distance, the table plane, the hands' position and grip, the box's position, scale and angle |
| @Image 2 | `../../product_images/box_festive_green_g2.png` | owns the carton artwork |

media ids `1cdfcc53-e771-4bba-9eab-b1788346098b`, `2597b25d-60d1-4060-9602-32b0ee26c2f7`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `624bfa6f-b152-4cc4-9667-b7d3414b2755`

```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a charcoal-grey cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a dark-stained quarter-sawn oak trestle table top: broad boards with tight straight grain and the distinctive pale medullary ray flecks of quarter-sawn oak showing through the deep brown stain, a matte hand-rubbed oil finish with almost no sheen. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused American Craftsman Christmas living room: a fireplace faced in dark green glazed tile under a heavy oak mantel with knitted stockings hanging from it, a built-in oak bookcase with leaded-glass doors beside it, a decorated Christmas tree with warm white fairy lights and burgundy and antique brass baubles standing off to one side, a brass floor lamp with an amber mica shade glowing warm, all well out of focus so the box stays the clear subject.

Dress the oak table more festively: a sprig of fir and a few red berries, two or three small brass and burgundy baubles, a short cream candle, a soft warm string light trailing across the oak, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.
```

> **Flagged, not fixed:** v3 C02 came back with the wordmark printed twice - once in gold on the green above the red band and again on the red band itself. The clause that governs this was not touched, so the same defect may repeat here. Daniel never ruled on it.

---

## C03 - The product lifted

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW
*What it is:* two hands hold the projector up in the air just above the soapstone counter.

- frames: `v4_c03_g1.png` (current)
- clips: none yet

*Reused from* v3 C03 - changed: (a) the sleeve, dark green wool -> charcoal-grey cable-knit; (b) `THE COUNTER`, walnut butcher-block -> honed charcoal soapstone; (c) `THE KITCHEN`, classic American -> Craftsman, sage-green shaker with brass cup pulls, cream zellige, black cast-iron range. The `KEEP IDENTICAL` block, `THE COUNTERTOP MUST BE IN FRAME`, `THE POSE`, `SCALE AND PLACEMENT`, `THE PRODUCT` and the quality tail are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c03_g3.png` | owns the geometry and the look - camera, pose, grip, product scale and placement, the counter wedge |

media id `7ccdd557-bfee-45b0-a067-0652320f537b`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `e877bf29-bdb8-4d79-9e16-4da1f2f724fb`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a charcoal-grey cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same charcoal-grey sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed charcoal soapstone counter: deep grey-black stone with a soft matte surface and faint pale veining drifting through it, a softly eased square edge, a low satin lustre that catches the warm light without shining. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. An American Craftsman Christmas kitchen, softly defocused: sage-green shaker cabinets with unlacquered brass cup pulls, a cream zellige tile backsplash with its slightly uneven handmade glaze, a black cast-iron range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

> **Flagged, not fixed:** v3 C03 and C04 both came back with a squatter dome than the packshot. `THE PRODUCT` was not touched, so the same proportion may repeat.

---

## C04 - Plugging it in

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW
*What it is:* low close camera, the unit large and left of centre on the soapstone counter, her right hand pushing the USB-C connector toward the port.

- frames: `v4_c04_g1.png` (current)
- clips: none yet

*Reused from* v3 C04 - changed: the same three nouns as C03 - the sleeve, the counter and the kitchen (range on the right in this shot, as in v3). The whole `CAMERA` block, `THE PRODUCT`, the hand-action sentences and the quality tail are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c04_g3.png` | owns the geometry and the look - the low close camera, the product large and left of centre, the counter filling the lower two thirds |

media id `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `7aa2297c-f157-474c-b631-a43a0fe73c00`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a charcoal-grey cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed charcoal soapstone counter: deep grey-black stone with a soft matte surface and faint pale veining drifting through it, a softly eased square edge, a low satin lustre that catches the warm light without shining. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. An American Craftsman Christmas kitchen, softly defocused across the top third of the frame: sage-green shaker cabinets with unlacquered brass cup pulls, a cream zellige tile backsplash with its slightly uneven handmade glaze, a black cast-iron range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

---

## C05 - The door opens on the room

*Section:* B-roll 2 - the payoff
*Status:* BOTH FRAMES GENERATED · FRAME 2 RE-ROLLED ON A REAL-HOUSE REFERENCE - TAKE 2 FOR REVIEW
*What it is:* one clip, two frames. Her hand on the closed forest-green door, then the great room already buried in the projection.

- frames: `v4_c05_g1.png` (frame 1), `v4_c05_r2.png` (frame 2, current, in `references/`) · `v4_c05_r1.png` (frame 2, take 1, superseded)
- clips: none yet

### FRAME 1 - hand on the closed door

*Reused from* v3 C05 frame 1 - changed: the door only. Navy five-panel with brass knob and cream frame -> deep matte forest green four-panel with an oil-rubbed bronze knob and escutcheon in a stained oak frame, and the two exposure sentences follow the new colour ("the forest green paint reads clearly as green rather than black", "the bronze knob catches a warm highlight"). The `KEEP IDENTICAL` list, the fully-closed / no-light-spill clause, `THE WREATH`, the `SHARPNESS` block and its BANNED list are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c05_g2.png` | owns the geometry and the look - hallway, camera position and height, the knob position, the forearm entering from the lower right, the warm low-key evening light |

media id `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `a3d7df02-f6f1-486f-9b05-2ce08e16aa76`

```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American four-panel door painted a deep matte forest green: crisp raised mouldings around four flat recessed panels, clean painted surfaces with the faintest brush texture, an oil-rubbed bronze knob and a matching oil-rubbed bronze escutcheon plate, set in a plain stained oak frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest green paint reads clearly as green rather than black, the bronze knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the bronze knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### FRAME 2 - the room behind the door

*Reused from* v3 C05 frame 2 - changed: the room (American Craftsman great room), the knitwear (charcoal-grey and cream fair-isle snowflake band, oatmeal trousers, mustard socks), the surfaces named inside the physics block (shiplap -> tongue-and-groove, fieldstone -> clinker brick), the moon's anchor ("high on the wall beside the fireplace"), and the projection signature - **a long procession of glowing gold carol singers and lantern carriers winding along the village lane** - plus the shared escalation clause. The pose sentences, the aurora / sleigh / star / snowflake layers, the palette ban list, the whole `HOW THE LIGHT SITS ON THE CEILING` block, the floor clause and the projector-not-visible clause are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/references/v1_c05_r2.png` | framing only - the wide view of a whole tall room from the doorway, camera position and height, the boy front-on and the girl from behind, the low-key light where the projection is the only light |

media id `f3a8c329-4152-4a22-9469-d89578812e09`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `367765ca-c873-4750-a2b6-4cebe5167a20`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. An American Craftsman great room in a traditional house: soft sage green painted walls above quarter-sawn oak wainscoting to waist height with a broad oak plate rail, a high vaulted ceiling clad in warm cream painted tongue-and-groove boards with exposed dark stained oak rafters rising to a dark stained oak ridge beam, a full-height clinker brick fireplace on the right with a low fire burning and a heavy oak mantel with knitted stockings hanging from it, a deep burgundy roll-arm sofa with olive green cushions and a cream cable-knit throw, a patterned wool rug over wide oak floorboards, a tall real Christmas tree in the left corner with warm white lights and burgundy and antique brass baubles, wrapped gifts under it, and a tall oak-trimmed window with leaded glass behind the tree showing a dark blue snow-covered night outside.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every painted wall, the whole vaulted boarded ceiling and its oak rafters and ridge beam, and the clinker brick of the fireplace, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the wall beside the fireplace; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the sage paint and the cream boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the tongue-and-groove boards, their seams and their subtle grain, and every dark stained oak rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the patterned rug, the burgundy sofa, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### FRAME 2 - TAKE 2, the real-house architecture

*Reused from* v4 C05 frame 2 take 1 - changed: (a) the whole `CHANGE 1 - THE ROOM` paragraph, replaced by the architecture of `house_great_room_beams.png` read off the photograph, plus a second paragraph naming the only two departures from it - night, and Christmas dressing; (b) a role sentence appended to the opening paragraph that splits authority between the two references; (c) the surfaces named inside the physics block, which had to follow the new room or the prompt contradicts itself - the ceiling is FLAT plaster crossed by four square oak beams, not two boarded slopes meeting at a ridge, so `kink and change direction ... at the ridge beam` -> `break and step where each heavy beam crosses them`, the moon's anchor -> `high on the wall above the gallery landing`, and the closing ceiling assertion -> `a real flat plaster ceiling crossed by four heavy oak beams with a skylight set between them`.

Nothing in the projection changed. The `KEEP IDENTICAL` list, the two poses, the knitwear, every projection layer, the palette statement and its cold-colour ban list, the not-outer-space ban, the translucency / keystone / falloff logic, the volumetric-shaft sentence, the no-floor-projection clause, the no-projector clause and the quality and no-text tails are byte-identical to take 1. Every replacement was applied with a single-match assert, so the untouched text is verified identical rather than asserted.

*Why:* the model was inventing the architecture, and the ceilings came out wrong. A photograph of a real room now owns the geometry.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/references/v1_c05_r2.png` | camera, framing, the two poses and the light - unchanged from take 1 |
| @Image 2 | `../../references/house_great_room_beams.png` | **the architecture, and nothing else** - the flat plaster ceiling, its four square oak beams, the skylight, the gallery landing and its black baluster rail, the stair, the tall black-framed windows, the proportions |

media ids `f3a8c329-4152-4a22-9469-d89578812e09` · `e402f616-c876-4e01-bb5a-60774babf36a`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `9260746b-a26d-4de6-b1e2-91bacfbddff4`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its beams, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height living space whose ceiling is flat smooth cream plaster crossed by four heavy square-sawn pale oak beams running left to right at even spacing, each one a real chunky timber with square corners and visible grain where it lands on the wall, and one large rectangular flush skylight set into the plaster between the first two beams; a first-floor gallery landing crossing the left and centre of the room at mid height, its railing made of slim black metal balusters under a black top rail with a plain cream fascia below it; a straight run of stairs on the right coming down towards the camera with pale oak treads and the same slim black baluster railing; tall black-framed windows filling the right-hand wall to full height; pale limewashed plaster walls; and underneath the gallery an open kitchen with a white marble waterfall island, open shelving with pottery and a full-height pale oak cabinet run. Terracotta saltillo tile floor laid in a square pattern, a large faded Persian rug in rust, cream and terracotta, a big cream linen sectional sofa, a chunky rustic reclaimed-wood low coffee table, and a large olive tree in a terracotta pot in the right foreground. Copy the proportions, the beam spacing, the skylight, the railings and the stair from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall windows show a dark blue snow-covered night outside, there is no daylight and no sunlight anywhere in the room, every lamp, pendant and downlight in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing in front of the tall windows with warm white lights and burgundy and antique brass baubles and wrapped gifts underneath, a thick evergreen garland with pine cones and burgundy ribbon wound along the gallery railing and down the stair rail, knitted stockings hanging from the gallery rail, and a bowl of burgundy and brass baubles on the coffee table. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every plaster wall, the whole flat plaster ceiling and its four heavy square oak beams, and the fascia and railing of the gallery landing, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling plane and run with the direction of the oak beams instead of hanging as vertical curtains, and visibly break and step where each heavy beam crosses them; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the ceiling plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the wall above the gallery landing; one big brilliant north star high beside the skylight with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across the whole ceiling; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the oak beams. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every heavy square oak beam with its grain and its square corners, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each beam breaks the light with its own hard shadow line where it stands proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the ceiling plane and stepping where it crosses each beam. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling crossed by four heavy oak beams with a skylight set between them, never as a backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The terracotta tile floor, the Persian rug, the cream sectional sofa, the olive tree, the Christmas tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

---

## C06 - The bed bounce

*Section:* B-roll 2 - the payoff
*Status:* RE-ROLLED ON A REAL-HOUSE REFERENCE - TAKE 2 FOR REVIEW
*What it is:* a girl of about seven standing on top of the bed mid-bounce under a projected vaulted sky.

- frames: `v4_c06_g2.png` (current) · `v4_c06_g1.png` (take 1, superseded)
- clips: none yet

*Reused from* v3 C06 - changed: (a) the child, a boy of about eight with short dark curly hair -> a girl of about seven with long auburn hair, and the pronouns that follow; (b) the knitwear; (c) the room, grey-blue boards and a white bed -> butter-cream tongue-and-groove with a sage-green bed and burgundy quilt; (d) the surfaces named inside the physics block; (e) the projection signature and the shared escalation clause. **Plus the three moderation edits below**, which are the only other differences from v3 and are recorded because they are the text that actually ran.

**The three moderation edits** - see the refusal log at the foot of this file:

1. `CHANGE 4` final sentence: `The girl's face and her knitted jumper catch that spill so her face reads clearly.` -> `Her knitted jumper catches that spill so the jumper and the mid-bounce pose read clearly.`
2. quality tail: `perfectly exposed with the girl's face clearly readable` -> `perfectly exposed`
3. v4 only, added after the fourth refusal - `CHANGE 1` gained a second copy of the wholesome clause, appended after `Clearly standing on top of the bed, not sitting on its edge.`: ` Wholesome family Christmas scene, a child at home with her family at Christmas.`

Nothing describing motion, camera, pacing or framing was touched. The bounce-pose sentence, the whole `CHANGE 3` projection paragraph and the physics block are byte-identical.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c06_g1.png` | owns the geometry and the look - camera position and height, the framing that carries both the wall behind the bed and the ceiling above it, the low-key light where the projection is the only light |

media id `0a845da6-2607-46cc-a595-4fee4b17d6a9` - **the original reference.** The reference swap tested during the refusal round was abandoned; this frame was won on the original.

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `4c885155-2672-4e5c-a853-b548d9eb1a03`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with her family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a girl of about seven with long auburn hair, fully dressed for winter in a warm charcoal-grey and cream fair-isle knitted Christmas jumper with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. She is standing up on top of the bed, knees bent and both arms raised out to her sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge. Wholesome family Christmas scene, a child at home with her family at Christmas.

CHANGE 2 - THE ROOM. A classic American child's bedroom tucked under the roof: a low sloped ceiling on both sides clad in soft butter-cream painted tongue-and-groove boards with white-painted exposed rafters running up to a ridge beam, white painted beadboard on the knee wall below, a small white-trimmed dormer window with a dark snowy night outside and a warm fairy-light garland around it, a low sage-green painted wooden bed set against the knee wall made up with a burgundy quilt, a cream cable-knit throw and ticking-stripe pillows, a knitted stocking pinned to the rafter above the headboard, a small lit Christmas tree standing on the floor beside the bed, a braided round rug on wide oak floorboards, and a low sage-green bookshelf of picture books tucked under the slope.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both painted sloped ceiling planes and the white rafters, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the dormer window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the painted boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the painted boards, their seams and their subtle grain, and every white-painted rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the braided round rug, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Her knitted jumper catches that spill so the jumper and the mid-bounce pose read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### TAKE 2 - the real-house architecture

*Reused from* v4 C06 take 1 - changed: (a) the whole `CHANGE 2 - THE ROOM` paragraph, replaced by the architecture of `house_bedroom_rafters.png` read off the photograph, plus a second paragraph naming the only two departures from it - night, and Christmas dressing; (b) a role sentence appended to the opening paragraph, placed **after** the wholesome clause so the moderation-critical text stays exactly where it was; (c) the surfaces named inside the physics block - painted tongue-and-groove and white rafters -> smooth cream plaster and heavy reclaimed oak rafters with a king-post truss, the moon's anchor -> `high on the slope above the gable window`.

This shot needed the fewest edits of the three: the photograph's ridge-and-rafter geometry already matches the geometry the physics block was written around, so the kink-at-the-ridge sentence, the two-sloping-planes assertion and the keystone logic survive word for word.

The child, her pose, the knitwear, every projection layer, the palette statement, the ban lists, the falloff logic, the floor clause, the projector clause and both quality tails are byte-identical to take 1, **including all three moderation edits recorded above**. Cleared moderation on the first submission this time.

*Why:* the model was inventing the attic, and the ceiling came out wrong. A photograph of a real room now owns the geometry.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c06_g1.png` | camera, framing, the pose and the light - unchanged from take 1 |
| @Image 2 | `../../references/house_bedroom_rafters.png` | **the architecture, and nothing else** - the two plaster slopes and their ridge, the reclaimed oak rafters, the king-post truss, the wrought-iron ring chandelier, the gable end wall and its triangular-headed window, the plank accent wall, the proportions |

media ids `0a845da6-2607-46cc-a595-4fee4b17d6a9` · `c1ea3b08-e710-4bda-9d33-4dd99b0e3012`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `25a6c79a-8576-43c0-89b6-4157c77c312d`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with her family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its truss, its walls, its window and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a girl of about seven with long auburn hair, fully dressed for winter in a warm charcoal-grey and cream fair-isle knitted Christmas jumper with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. She is standing up on top of the bed, knees bent and both arms raised out to her sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge. Wholesome family Christmas scene, a child at home with her family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom under a high vaulted roof, the ceiling two sloping planes of smooth cream plaster meeting at a ridge that runs away from the camera, crossed by heavy reclaimed oak rafters - a king-post truss near the front, its two rafters meeting at the ridge above a horizontal collar, and four or five more rafters marching down the right-hand slope onto a horizontal oak wall plate - with small recessed downlights set into the plaster between them, and a big black wrought-iron ring chandelier of two concentric rings carrying a row of plain candle bulbs hanging on a black rod from the ridge; a tall gable end wall on the left with a triangular-headed window above a pair of dark-framed glazed doors with side lights and long taupe linen curtains; a horizontal grey-brown plank accent wall behind the bed with three small framed prints in thin dark frames and a black wall sconce beside them; a low reclaimed-wood platform bed with a wide plank headboard, two nightstands with table lamps, wide pale oak plank floorboards and a large flat-weave oat rug. Copy the proportions, the rafter spacing, the king-post truss, the ridge, the ring chandelier and the gable window from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the gable window and the glazed doors show a dark blue snow-covered night outside, there is no daylight anywhere in the room, the ring chandelier and every downlight and table lamp are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a burgundy quilt, a cream cable-knit throw and ticking-stripe pillows, a knitted stocking hangs from the rafter above the headboard, a warm fairy-light garland is strung around the gable window, a small lit Christmas tree stands on the floor beside the bed, and a small evergreen wreath with a burgundy bow hangs on the plank wall. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both sloping plaster ceiling planes, the heavy oak rafters and the king-post truss, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the gable window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the cream plaster and the oak rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, and every heavy reclaimed oak rafter, the king-post truss and the ridge, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the truss break the light with their own hard shadow lines where they stand proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as two sloping plaster planes meeting at a ridge and crossed by heavy oak rafters, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the flat-weave rug, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Her knitted jumper catches that spill so the jumper and the mid-bounce pose read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

---

## C07 - The double-height room

*Section:* B-roll 2 - the payoff
*Status:* RE-ROLLED ON A REAL-HOUSE REFERENCE - TAKE 2 FOR REVIEW
*What it is:* a great room, the girl mid-air over the sofa, the boy on the rug looking up, the whole two-storey volume inside the projection.

- frames: `v4_c07_g2.png` (current) · `v4_c07_g1.png` (take 1, superseded)
- clips: none yet

*Reused from* v3 C07 - changed: (a) the children, dark braids and blond -> long wavy auburn and short auburn; (b) the knitwear; (c) the room, fieldstone and white shiplap -> dark clinker brick and whitewashed reclaimed timber, blackened steel rail, dark stained king-post trusses; (d) the surfaces named inside the physics block; (e) the projection signature and the shared escalation clause. **Plus the two moderation edits below.**

**The two moderation edits:**

1. the opening paragraph gained the wholesome clause: `...with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas.`
2. `CHANGE 4` final sentence: `Both children catch that spill so their jumpers and the girl's mid-air pose read clearly.` -> `Both children catch that spill so their knitted jumpers read clearly.`

The jump-pose sentence in `KEEP IDENTICAL` was left byte-identical.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c07_g2.png` | owns the geometry and the look - the wide framing of a whole double-height room with its full ceiling in shot, camera position and height, the two poses, the low-key light |

media id `c9a6740d-383b-4829-a7b9-f7a3c079c03f` - the original reference.

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `a42f98d9-6008-43a0-bbb1-ef7cde26e12e`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long wavy auburn hair, the boy is about five with short auburn hair. Both are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. An American barn-style double-height great room: one enormous two-storey chimney breast of dark clinker brick running the full height of the space with a chunky reclaimed timber mantel and knitted stockings, whitewashed reclaimed timber plank walls either side of it, a balcony landing with a blackened steel rail crossing high across the room with an open blackened-steel-and-oak staircase rising to it on the right, exposed dark stained king-post roof trusses under a high vaulted cream boarded ceiling, tall black-framed windows on the left showing a dark blue snowy night, wide oak floorboards with a large patterned wool rug, a long deep burgundy sectional sofa with olive green cushions, a leather ottoman, and a very tall real Christmas tree standing against the brick with warm white lights, burgundy and antique brass baubles and wrapped gifts beneath it.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey clinker brick chimney breast, the whitewashed timber walls, the whole high vaulted boarded ceiling, the exposed king-post trusses and the underside and railing of the balcony landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the brick above the balcony landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the dark brick and the whitewashed timber. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real brick and real boards, not paint and not a sticker. The light is TRANSLUCENT - every individual clinker brick and its mortar joints, and the planks, seams and dark trusses of the ceiling, all stay clearly visible THROUGH the coloured light, and the trusses and the mantel break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare brick and bare board. Even packed full it must still read as projected light on a real textured surface, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the patterned rug, the burgundy sectional sofa, the ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

> **Flagged, not fixed:** v3 C07 came back with the jump pose reading soft - the girl looked like she was standing rather than mid-air. That sentence lives in `KEEP IDENTICAL`, which rule 3 says stays byte-identical, so it was not touched and the same softness may repeat.

### TAKE 2 - the real-house architecture

*Reused from* v4 C07 take 1 - changed: (a) the whole `CHANGE 2 - THE ROOM` paragraph, replaced by the architecture of `house_great_room_trusses.png` read off the photograph, plus a second paragraph naming the only two departures from it - night, and Christmas dressing; (b) a role sentence appended to the opening paragraph, placed **after** the wholesome clause so the moderation-critical text stays exactly where it was; (c) the surfaces named inside the physics block - clinker brick chimney breast and whitewashed timber -> the two-storey plaster back wall and plaster side walls, king-post trusses -> the two pairs of dark walnut rafters and their collar beams, balcony -> gallery landing, `every individual clinker brick and its mortar joints` -> `the plaster and its fine surface texture, and every dark walnut rafter, every collar beam and the ridge line of the vault`, `fading to bare brick and bare board` -> `fading to bare plaster`.

The children, both poses, the knitwear, every projection layer, the palette statement, the ban lists, the falloff logic, the floor clause, the projector clause, the no-fisheye tail and the no-text tail are byte-identical to take 1, **including both moderation edits recorded above**. Cleared moderation on the first submission this time.

*Why:* the model was inventing the barn, and the vault came out wrong. A photograph of a real room now owns the geometry.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c07_g2.png` | camera, framing, both poses, the scale of the children against the room and the light - unchanged from take 1 |
| @Image 2 | `../../references/house_great_room_trusses.png` | **the architecture, and nothing else** - the plaster cathedral vault and its ridge, the two pairs of dark walnut rafters with their collar beams, the gallery landing and its glass-and-black-post rail, the open-tread stair, the arched window, the arched glazed door, the proportions |

media ids `c9a6740d-383b-4829-a7b9-f7a3c079c03f` · `1d79cde5-c6a5-4259-b414-2b0d4bd8434b`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `245f4be5-1799-4f2e-8fe4-7df48c13d29d`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long wavy auburn hair, the boy is about five with short auburn hair. Both are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: an enormous double-height great room whose ceiling is a cathedral vault of smooth cream plaster in two long slopes meeting at a ridge that runs away from the camera, crossed by two pairs of dark walnut-stained timber rafters, each pair rising as an inverted V to meet at the ridge with a matching collar beam below it, and small recessed downlights set flush into the plaster between them; a first-floor gallery landing crossing the right-hand half of the room at mid height, its railing made of clear glass panels held in slim black metal posts under a dark timber top rail; an open-tread pale oak staircase descending from that landing towards the camera with the same glass-and-black-post railing and black wall sconces on the wall beside it; a tall arched window with dark muntins set high on the right above the stair; a pale plaster back wall at the centre carrying a black arched double glazed door of many small panes; and along the left an open kitchen with pale oak slab cabinetry, a full-height integrated cabinet run, a cream island with a stone waterfall front, four woven rattan counter stools and two big woven rattan dome pendants hanging on long black cords. Wide warm oak plank floor, a large pale grey sectional sofa wrapping the right foreground, a round dark-stained wood coffee table and a large greige rug. Copy the proportions, the rafter pairs, the ridge, the glass railing, the stair and the arched door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the arched window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every downlight, pendant and sconce in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the pale plaster back wall beside the arched door with warm white lights and burgundy and antique brass baubles and wrapped gifts beneath it, a thick evergreen garland with pine cones and burgundy ribbon wound along the gallery railing and down the stair rail, knitted stockings hanging from the gallery rail, and a large evergreen wreath with a burgundy bow on the arched door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey pale plaster back wall, the plaster walls either side of it, the whole high vaulted plaster ceiling, the dark walnut rafters and their collar beams and the underside and railing of the gallery landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the plaster wall above the gallery landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the dark walnut rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every dark walnut rafter, every collar beam and the ridge line of the vault, all stay clearly visible THROUGH the coloured light, and the rafters and the collar beams break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full it must still read as projected light on a real plastered vault with real timber rafters crossing it, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the greige rug, the grey sectional sofa, the round coffee table and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

---

## Round summary

| shot | file | job | status |
|---|---|---|---|
| C02 | `starting_frames/v4_c02_g1.png` | `624bfa6f` | take 1, for review - watch for the doubled wordmark |
| C03 | `starting_frames/v4_c03_g1.png` | `e877bf29` | take 1, for review - watch for the squat dome |
| C04 | `starting_frames/v4_c04_g1.png` | `7aa2297c` | take 1, for review - watch for the squat dome |
| C05 F1 | `starting_frames/v4_c05_g1.png` | `a3d7df02` | take 1, for review |
| C05 F2 | `references/v4_c05_r1.png` | `367765ca` | take 1, superseded - invented architecture |
| C06 | `starting_frames/v4_c06_g1.png` | `4c885155` | take 1, superseded - invented architecture. Cleared on submission 4 |
| C07 | `starting_frames/v4_c07_g1.png` | `a42f98d9` | take 1, superseded - invented architecture. Cleared on submission 3 |

**Take 2 - the real-house reference round, B-roll 2 only**

| shot | file | job | status |
|---|---|---|---|
| C05 F2 | `references/v4_c05_r2.png` | `9260746b` | take 2, **current**, for review |
| C06 | `starting_frames/v4_c06_g2.png` | `25a6c79a` | take 2, **current**, for review |
| C07 | `starting_frames/v4_c07_g2.png` | `245f4be5` | take 2, **current**, for review |

No shot has more than one generation per take. A moderation refusal returns no file, so the resubmissions below are not re-rolls.

## The real-house reference round - B-roll 2

*2026-09-19.* Daniel: *"For Broll 2, I like the animations, they are very good, the ai model fails on making realistic rooms especially ceiling. Let's try to add some reference images with some real houses / they must be christmas decorated. / Try this only for video 4, and if everything is good, we will do the same for the next ones."*

The diagnosis is right and the `HOW THE LIGHT SITS ON THE CEILING` block was never going to fix it, because the model was inventing the architecture in the first place - there was nothing for the block to keep visible. So the lever is a second reference that owns the geometry, which is the standing two-references-per-regen doctrine: one reference for layout, one for look.

Four interior photographs were cropped and filed at `<PRODUCT>/references/` under `NAMING.md` §4, the sanctioned product-level exception to no-descriptive-names:

| file | ceiling | used for |
|---|---|---|
| `house_great_room_beams.png` | flat cream plaster crossed by four square oak beams, one flush skylight | C05 frame 2 |
| `house_bedroom_rafters.png` | two plaster slopes to a ridge, reclaimed oak rafters, king-post truss | C06 |
| `house_great_room_trusses.png` | plaster cathedral vault, two pairs of dark walnut rafters with collar beams | C07 |
| `house_bedroom_attic.png` | coved attic ceiling, barn door on a black track | **held in reserve** - the calmer C06 alternative, not used |

The reference houses are not decorated and are shot in daylight, so each prompt carries an explicit two-things-change paragraph: it is night with every fixture in the house switched off, and the room is dressed for Christmas. Everything else about the room is copied as built.

**One divergence to flag.** The room palettes now leave the v4 look pack (sage green / oak / burgundy) behind, because these houses are plaster, oak, cream and terracotta. Architecture off the photograph beat the look pack, because architecture is the defect Daniel named. The burgundy-and-antique-brass Christmas dressing still carries the v4 colour story through all three shots.

## Refusal log - C06 and C07

Both shots were refused `nsfw` on the first pass. The investigation ran in four rounds:

| round | what changed | result |
|---|---|---|
| 1 | nothing - identical prompt, identical reference | refused again, both |
| 2 | reference swapped to the approved v3 frames, prompt untouched | refused again, both - C06 `0d76ef5a-c373-47ca-a943-bd6939d983b8`, C07 `161b4025-6f1a-48cd-af08-0124163f0778` |
| 3 | original references restored, surgical additive text edits | C07 passed (`a42f98d9`); C06 still refused (`1acdc79f-e269-4847-bd75-d2b367f4e06b`) |
| 4 | C06 only - second copy of the wholesome clause added to `CHANGE 1` | passed (`4c885155`) |

**What this establishes.** The verdict is deterministic on the exact prompt string - five identical resubmissions were refused five times. It is **not** driven by the reference image - five reference swaps were refused five times. The trigger is text-side, and specifically the clauses that emphasise the child's face and body rather than motion, camera, pacing or framing. v6 C06, which is a boy, passed on the first pass with structurally identical text.

This **contradicts** the v2 C06 precedent, which recorded a reference swap as the only thing that had ever cleared a repeated refusal. That precedent did not hold here.

## Result URLs

CDN base `https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/`

```
v4_c02_g1.png   hf_20260919_181932_624bfa6f-b152-4cc4-9667-b7d3414b2755.png
v4_c03_g1.png   hf_20260919_181932_e877bf29-bdb8-4d79-9e16-4da1f2f724fb.png
v4_c04_g1.png   hf_20260919_181932_7aa2297c-f157-474c-b631-a43a0fe73c00.png
v4_c05_g1.png   hf_20260919_181932_a3d7df02-f6f1-486f-9b05-2ce08e16aa76.png
v4_c05_r1.png   hf_20260919_181933_367765ca-c873-4750-a2b6-4cebe5167a20.png
v4_c06_g1.png   hf_20260919_184129_4c885155-2672-4e5c-a853-b548d9eb1a03.png
v4_c07_g1.png   hf_20260919_184014_a42f98d9-6008-43a0-bbb1-ef7cde26e12e.png
v4_c05_r2.png   hf_20260919_195527_9260746b-a26d-4de6-b1e2-91bacfbddff4.png
v4_c06_g2.png   hf_20260919_195559_25a6c79a-8576-43c0-89b6-4157c77c312d.png
v4_c07_g2.png   hf_20260919_195633_245f4be5-1799-4f2e-8fe4-7df48c13d29d.png
```

## Next

Daniel reviews the board. B-roll 2 now shows take 2 on all three shots - C05 F2, C06 and C07 - rebuilt on real-house architecture references; C02, C03 and C04 are unchanged at take 1. No clips are submitted until he picks. C01 (the hook) has not been generated for this video.

If the real-house references land, the same treatment goes to the B-roll 2 shots of video 5 and video 6. Held for his word: `house_bedroom_attic.png` is filed and unused, and the room palettes now diverge from the v4 look pack.


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v4_c01_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v4_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v4_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v4_c04_g2.mp4` | Named derivative of `../v4_c04_g2.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v4_c05_g2.mp4` | Named derivative of `../v4_c05_g2.mp4` under the existing naming convention; upscale job/settings and exact source linkage remain unverified. |
| `clips/upscaled/v4_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v4_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c01_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c01_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c01_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c04_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v4_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c05_g2.mp4` | UNRESOLVED — no exact filename stem in the original archive; exact take prompt/settings/job association not established. Existing neighbouring prompts must not be substituted. |
| `clips/v4_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v4_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v4_c01_r1.png` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v4_c01_r2.png` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v4_c05_r1.png` | Embedded PNG `hf-job-id`: `367765ca-c873-4750-a2b6-4cebe5167a20`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v4_c05_r2.png` | Embedded PNG `hf-job-id`: `9260746b-a26d-4de6-b1e2-91bacfbddff4`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g1.png` | Embedded PNG `hf-job-id`: `8380e5f3-ae2a-4b04-bcf2-278e8a3746f7`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g10.png` | Embedded PNG `hf-job-id`: `7ad5dcc5-c5a7-4b4e-8ca6-bbbaa98fb2c5`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g11.png` | Embedded PNG `hf-job-id`: `0930d451-db6f-4174-99df-4cbc3322475d`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g12.png` | Embedded PNG `hf-job-id`: `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v4_c01_g13.png` | Embedded PNG `hf-job-id`: `47abd381-4c53-4768-b2b4-cb5c6a747792`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v4_c01_g2.png` | Embedded PNG `hf-job-id`: `85e175db-91fb-4762-9fa5-1c21095a019f`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g3.png` | Embedded PNG `hf-job-id`: `917aa37f-619b-4c89-8236-1c041bc42ea2`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g4.png` | Embedded PNG `hf-job-id`: `d2f8b3ce-bdde-48f8-a9d3-5dff1b7485ff`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g5.png` | Embedded PNG `hf-job-id`: `8b9aee3a-9e83-47b9-9175-0eaacc3e69dd`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g6.png` | Embedded PNG `hf-job-id`: `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g7.png` | Embedded PNG `hf-job-id`: `23797b37-302e-4827-a64d-6bfa5acff602`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g8.png` | Embedded PNG `hf-job-id`: `4579c34e-70dd-411a-951e-29607cba6a56`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c01_g9.png` | Embedded PNG `hf-job-id`: `48614108-fe4b-45a5-88a3-4ca7c37d7ee6`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c02_g1.png` | Embedded PNG `hf-job-id`: `624bfa6f-b152-4cc4-9667-b7d3414b2755`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c03_g1.png` | Embedded PNG `hf-job-id`: `e877bf29-bdb8-4d79-9e16-4da1f2f724fb`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c04_g1.png` | Embedded PNG `hf-job-id`: `7aa2297c-f157-474c-b631-a43a0fe73c00`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c05_g1.png` | Embedded PNG `hf-job-id`: `a3d7df02-f6f1-486f-9b05-2ce08e16aa76`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c06_g1.png` | Embedded PNG `hf-job-id`: `4c885155-2672-4e5c-a853-b548d9eb1a03`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c06_g2.png` | Embedded PNG `hf-job-id`: `25a6c79a-8576-43c0-89b6-4157c77c312d`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c07_g1.png` | Embedded PNG `hf-job-id`: `a42f98d9-6008-43a0-bbb1-ef7cde26e12e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v4_c07_g2.png` | Embedded PNG `hf-job-id`: `245f4be5-1799-4f2e-8fe4-7df48c13d29d`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |

### Unresolved take records

The following 4 files still need exact take provenance or verified derivative lineage. Their presence is documented; their prompts have **not** been invented. MP4 C2PA manifest and instance IDs are authenticity identifiers, not Higgsfield job IDs.

- `clips/upscaled/v4_c04_g2.mp4`
- `clips/upscaled/v4_c05_g2.mp4`
- `clips/v4_c04_g2.mp4`
- `clips/v4_c05_g2.mp4`

### Recovered take — `starting_frames/v4_c01_g12.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the double-height Christmas living room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the two-storey open living room with the open staircase and the garlanded balcony railing hung with stockings, the kitchen through the opening at the left, the tall window at the right, the patterned terracotta rug, the big lit Christmas tree. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the walls and the balcony are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and walls read as clean white and off-white plaster, her sweater reads as true light grey, the wood reads as natural wood, the rug keeps its own colours. The Christmas tree lights and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "f0ade236-59f7-4299-b680-818d3b2934a1",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/f0ade236-59f7-4299-b680-818d3b2934a1.png"
      }
    }
  ],
  "width": 1520,
  "height": 2688,
  "quality": "high",
  "resolution": "2k",
  "model": "videotape-alpha",
  "remove_bg": false,
  "reference_elements": []
}
```


### Recovered take — `starting_frames/v4_c01_g13.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `47abd381-4c53-4768-b2b4-cb5c6a747792`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the vaulted Christmas great room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the barn-style vaulted great room with the dark exposed timber trusses across the ceiling, the arched front door, the balcony above, the kitchen island with rattan pendant lights, the cream sectional sofa, the lit Christmas tree and the garlands. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the timber trusses and the walls are plain plaster and plain dark wood, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the pendant lights and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE VAULTED CEILING high above her, between the timber beams, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the vaulted space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The vaulted ceiling reads as clean white and off-white plaster, her sweater reads as true light grey, the timber trusses read as natural dark wood, the sectional reads as true cream. The Christmas tree lights and the pendants are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high vaulted ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "4e57238e-ef76-46f4-a112-e081eda53907",
        "type": "media_input",
        "url": "https://d2ol7oe51mr4n9.cloudfront.net/user_REMOVED/4e57238e-ef76-46f4-a112-e081eda53907.png"
      }
    }
  ],
  "width": 1520,
  "height": 2688,
  "quality": "high",
  "resolution": "2k",
  "model": "videotape-alpha",
  "remove_bg": false,
  "reference_elements": []
}
```


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C01: the board did not show the exact clip prompt of `v4_c01_g5.mp4`; it now does (text above).
- C02: the board did not show the exact clip prompt of `v4_c02_g1.mp4`; it now does (text above).
- C03: the board did not show the exact clip prompt of `v4_c03_g1.mp4`; it now does (text above).
- C04: the board did not show the exact clip prompt of `v4_c04_g2.mp4`; it now does (text above).
- C05: the board did not show the exact clip prompt of `v4_c05_g2.mp4`; it now does (text above).
- C06: the board did not show the exact clip prompt of `v4_c06_g1.mp4`; it now does (text above).
- C07: the board did not show the exact clip prompt of `v4_c07_g1.mp4`; it now does (text above).

### C01 — Ladder fail — taping Santa up

**In the cut:** `starting_frames/v4_c01_g6.png` → `clips/v4_c01_g5.mp4`

#### Image prompt — `starting_frames/v4_c01_g6.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_204803_34ab4b0f-7a4e-4383-9120-8602e2eeed2e.png
**References, in submission order**
- none (text-only generation)

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a step ladder in a cosy American living room, evening. We see her from behind at three-quarters, her raised arms and the ceiling in front of her.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING in front of her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing on the second step from the top of a wooden step ladder, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand.

Around them: a decorated Christmas tree with warm lights to the side, garland on a mantel, a mug on the coffee table, an open decorations box on the rug.

LIGHTING AND QUALITY: perfect warm cosy interior light from a lamp and the tree, clean and even across the ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
````

#### Video prompt — `clips/v4_c01_g5.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `6b97b59c-435a-4a21-bf63-78f85c46ec96`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_213150_6b97b59c-435a-4a21-bf63-78f85c46ec96.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c01_g5.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`
- image ref 1: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`

````text
Real home video. One continuous handheld phone shot, no cuts, camera never moves from where it is in the attached image.

For the first second and a half she is just taping the inflatable Santa to the ceiling — both hands up, pressing and smoothing, nothing dramatic.

Then she loses her footing and falls off the ladder to the floor.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second — fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug.

She lands hard and then the room is still. She stays down on the floor for the last second and a half, not moving much, just stunned and breathing, and she is still there when the clip ends.

The inflatable Santa stays taped to the ceiling the whole time.

No slow motion. No speed ramp. No zoom, no push-in, no pan, no tilt. No cuts, no second angle. No captions or text.

Audio: room tone only, no music — the tape, a short gasp, the ladder hitting the floor, then her breathing.
````

**Other takes of C01 on disk (18)**

#### Image prompt — `starting_frames/v4_c01_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `8380e5f3-ae2a-4b04-bcf2-278e8a3746f7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_204421_8380e5f3-ae2a-4b04-bcf2-278e8a3746f7.png
**References, in submission order**
- none (text-only generation)

````text
Candid vertical iPhone photo shot from low down on the living room floor looking steeply up, so the whole step ladder and the ceiling fill the frame. A mom in her mid-30s with dark hair in a messy bun, wearing a red Christmas sweater and leggings, is balanced on the second step from the top of an aluminium step ladder, reaching up with one arm to hold a big inflatable Santa Claus decoration against the white ceiling while her other hand tries to tear a strip of duct tape off a roll with her teeth. The inflatable Santa is oversized and drooping, one arm of it flopping down into her face. Two used strips of tape hang loose from the ceiling. Her body is twisted and off-balance, one knee braced against the ladder. Cosy living room below: lit Christmas tree, sofa, wrapping paper and an open decorations box on the rug. Warm indoor evening light, handheld amateur snapshot realism, slight grain, sharp and very high quality, realistic textures. Keep a slim clean band of plain ceiling at the very top of the frame for a caption.
````

#### Image prompt — `starting_frames/v4_c01_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `85e175db-91fb-4762-9fa5-1c21095a019f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_204421_85e175db-91fb-4762-9fa5-1c21095a019f.png
**References, in submission order**
- none (text-only generation)

````text
Candid vertical iPhone photo taken from inside a cosy American family living room, evening. A mom in her mid-30s, light grey sweater, jeans and fluffy socks, stands near the top of a wooden step ladder, stretching up on tiptoes with both arms over her head, pressing a large inflatable Santa Claus Christmas decoration flat against the white ceiling while trying to stick it there with a roll of clear packing tape held in one hand. The inflatable Santa is big and floppy and sagging down over her head and shoulders, clearly not staying up. Strips of tape are already stuck to the ceiling around it, one strip dangling loose. The ladder is slightly wobbling, one of her feet lifted off the step. Decorated Christmas tree with warm lights in the background, sofa, coffee table with a mug, garland on the mantel. Warm cosy interior lighting from a lamp and the tree, natural handheld amateur snapshot look, slight grain, nothing blurry, very high quality, sharp detail, realistic skin texture. Leave a slim clean uncluttered band of ceiling across the very top of the frame for a caption.
````

#### Image prompt — `starting_frames/v4_c01_g3.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `917aa37f-619b-4c89-8236-1c041bc42ea2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_204421_917aa37f-619b-4c89-8236-1c041bc42ea2.png
**References, in submission order**
- none (text-only generation)

````text
Candid vertical iPhone photo of a cosy open-plan American living room in the evening, camera at normal standing height across the room, wide enough to see the whole scene. A mom in her mid-30s, blonde ponytail, cream cable-knit sweater and jeans, stands on the top platform of a wooden step ladder in the middle of the room with both hands above her head, pressing a huge inflatable Santa Claus decoration up against the white ceiling and taping it with brown packing tape. The inflatable Santa is enormous and clearly too heavy, sagging off the ceiling, one side already peeling away with a long strip of tape hanging down. A roll of tape sits on top of the ladder, scissors on the floor. She is leaning to one side, the ladder tilted slightly on the rug. Behind her: a decorated Christmas tree with warm lights, a garlanded fireplace, sofa with cushions, a cardboard decorations box open on the floor. Warm cosy lamp and tree lighting, handheld amateur snapshot look, slight grain, nothing blurry, very high quality and sharp, realistic skin and fabric detail. Reserve a slim clean uncluttered band across the very top of the frame for a caption.
````

#### Image prompt — `starting_frames/v4_c01_g4.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `d2f8b3ce-bdde-48f8-a9d3-5dff1b7485ff`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_204803_d2f8b3ce-bdde-48f8-a9d3-5dff1b7485ff.png
**References, in submission order**
- none (text-only generation)

````text
Extremely high quality candid vertical iPhone photo, shot from across a cosy American family living room at chest height with a slight upward tilt, evening.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is ALREADY STUCK TO THE WHITE CEILING, lying flat on its back against the ceiling, facing down into the room, held up by five or six criss-crossed strips of silver duct tape running over its arms, legs and belly onto the plaster. It is firmly taped up there, not falling, not draped over anyone. One long strip of tape has peeled and curls down loose.

A mom in her mid-30s, blonde hair in a ponytail, cream cable-knit sweater, jeans and fluffy socks, stands on a wooden step ladder directly under it, reaching up with both arms to smooth another strip of tape onto Santa's boot, standing on tiptoe, a roll of duct tape hooked on her wrist.

Behind and below: a decorated Christmas tree with warm lights, a sofa with cushions, an open cardboard decorations box on the rug, scissors on the floor.

LIGHTING AND QUALITY: perfect warm cosy interior lighting from a floor lamp and the tree, clean and even on her face and on the ceiling, every surface sharp and in focus, crisp detail in the tape, the vinyl sheen of the inflatable and the knit of her sweater. Natural handheld iPhone snapshot look, realistic skin texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: place the taped Santa in the upper middle of the frame and keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
````

#### Image prompt — `starting_frames/v4_c01_g5.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `8b9aee3a-9e83-47b9-9175-0eaacc3e69dd`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_204803_8b9aee3a-9e83-47b9-9175-0eaacc3e69dd.png
**References, in submission order**
- none (text-only generation)

````text
Extremely high quality candid vertical iPhone photo, camera low near the living room floor looking steeply up at the ceiling, evening, cosy American home.

THE KEY ELEMENT: a big inflatable Santa Claus decoration is TAPED TO THE WHITE CEILING above, lying flat against it and facing down at the camera, pinned there by many criss-crossed strips of brown packing tape stretched over its arms, hat and belly onto the plaster. Clearly stuck up there. Two loose ends of tape dangle down. A few older torn tape strips are still stuck to the ceiling nearby.

A mom in her mid-30s with dark hair in a messy bun, red Christmas sweater and leggings, stands near the top of an aluminium step ladder on the right of the frame, seen from below, both arms stretched overhead pressing another strip of tape across Santa's arm, her face tilted up and concentrating.

Below her: a lit Christmas tree, sofa, wrapping paper and an open decorations box on the rug.

LIGHTING AND QUALITY: perfect warm even interior lighting, the ceiling well lit and clean, no harsh shadows, everything tack sharp and in focus, crisp detail in the tape strips, the glossy inflatable vinyl and her sweater. Natural handheld iPhone snapshot realism, realistic skin texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of Santa and of tape, for a caption.
````

#### Image prompt — `starting_frames/v4_c01_g7.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `23797b37-302e-4827-a64d-6bfa5acff602`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214938_23797b37-302e-4827-a64d-6bfa5acff602.png
**References, in submission order**
- @Image 1: `content/video_4_assets/references/v4_c01_r1.png` · Higgsfield media `f0ade236-59f7-4299-b680-818d3b2934a1`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the double-height Christmas living room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly — the two-storey open living room with the open staircase and the garlanded balcony railing hung with stockings, the kitchen through the opening at the left, the tall window at the right, the patterned terracotta rug, the big lit Christmas tree. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere — the ceiling, the walls and the balcony are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

LIGHTING AND QUALITY: perfect warm cosy interior light from the lamps and the tree, clean and even across the high ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
````

#### Image prompt — `starting_frames/v4_c01_g8.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `4579c34e-70dd-411a-951e-29607cba6a56`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214939_4579c34e-70dd-411a-951e-29607cba6a56.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `4e57238e-ef76-46f4-a112-e081eda53907`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the vaulted Christmas great room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly — the barn-style vaulted great room with the dark exposed timber trusses across the ceiling, the arched front door, the balcony above, the kitchen island with rattan pendant lights, the cream sectional sofa, the lit Christmas tree and the garlands. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere — the ceiling, the timber trusses and the walls are plain plaster and plain dark wood, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the pendant lights and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE VAULTED CEILING high above her, between the timber beams, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the vaulted space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

LIGHTING AND QUALITY: perfect warm cosy interior light from the pendants and the tree, clean and even across the high ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: keep a slim clean band of plain empty ceiling across the very top of the image, free of objects, for a caption.
````

#### Image prompt — `starting_frames/v4_c01_g9.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `48614108-fe4b-45a5-88a3-4ca7c37d7ee6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_221101_48614108-fe4b-45a5-88a3-4ca7c37d7ee6.png
**References, in submission order**
- @Image 1: `content/video_4_assets/references/v4_c01_r1.png` · Higgsfield media `f0ade236-59f7-4299-b680-818d3b2934a1`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the double-height Christmas living room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the two-storey open living room with the open staircase and the garlanded balcony railing hung with stockings, the kitchen through the opening at the left, the tall window at the right, the patterned terracotta rug, the big lit Christmas tree. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the walls and the balcony are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

LIGHTING AND QUALITY: perfect warm cosy interior light from the lamps and the tree, clean and even across the high ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: leave a slim clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

#### Image prompt — `starting_frames/v4_c01_g10.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `7ad5dcc5-c5a7-4b4e-8ca6-bbbaa98fb2c5`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_221102_7ad5dcc5-c5a7-4b4e-8ca6-bbbaa98fb2c5.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `4e57238e-ef76-46f4-a112-e081eda53907`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the vaulted Christmas great room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the barn-style vaulted great room with the dark exposed timber trusses across the ceiling, the arched front door, the balcony above, the kitchen island with rattan pendant lights, the cream sectional sofa, the lit Christmas tree and the garlands. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the timber trusses and the walls are plain plaster and plain dark wood, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the pendant lights and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE VAULTED CEILING high above her, between the timber beams, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the vaulted space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

LIGHTING AND QUALITY: perfect warm cosy interior light from the pendants and the tree, clean and even across the high ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: leave a slim clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

#### Image prompt — `starting_frames/v4_c01_g11.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `0930d451-db6f-4174-99df-4cbc3322475d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_221101_0930d451-db6f-4174-99df-4cbc3322475d.png
**References, in submission order**
- @Image 1: `content/video_4_assets/references/v4_c01_r1.png` · Higgsfield media `f0ade236-59f7-4299-b680-818d3b2934a1`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the double-height Christmas living room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the two-storey open living room with the open staircase and the garlanded balcony railing hung with stockings, the kitchen through the opening at the left, the tall window at the right, the patterned terracotta rug, the big lit Christmas tree. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the walls and the balcony are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

LIGHTING AND QUALITY: perfect warm cosy interior light from the lamps and the tree, clean and even across the high ceiling and her back, everything sharp and in focus, crisp detail in the tape, the inflatable vinyl sheen and her knitwear. Natural handheld iPhone snapshot look, realistic skin and fabric texture. Absolutely nothing blurry, no motion blur, no soft focus, no grain.

FRAMING: leave a slim clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

#### Image prompt — `starting_frames/v4_c01_g12.png`

**Settings** - gpt_image_2 · 9:16 · 2k · high · 1520×2688
**Job** - `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_222322_195e86f7-31ca-48d1-a1eb-4c0e64e0cf74.png
**Same Higgsfield job as** - `content/video_5_assets/starting_frames/v5_c01_g1.png`
**References, in submission order**
- @Image 1: `content/video_4_assets/references/v4_c01_r1.png` · Higgsfield media `f0ade236-59f7-4299-b680-818d3b2934a1`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the double-height Christmas living room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the two-storey open living room with the open staircase and the garlanded balcony railing hung with stockings, the kitchen through the opening at the left, the tall window at the right, the patterned terracotta rug, the big lit Christmas tree. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the walls and the balcony are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and walls read as clean white and off-white plaster, her sweater reads as true light grey, the wood reads as natural wood, the rug keeps its own colours. The Christmas tree lights and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

#### Image prompt — `starting_frames/v4_c01_g13.png`

**Settings** - gpt_image_2 · 9:16 · 2k · high · 1520×2688
**Job** - `47abd381-4c53-4768-b2b4-cb5c6a747792`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_222323_47abd381-4c53-4768-b2b4-cb5c6a747792.png
**References, in submission order**
- @Image 1: uploaded image, not on the drive · Higgsfield media `4e57238e-ef76-46f4-a112-e081eda53907`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in the vaulted Christmas great room from the attached reference image, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

THE ROOM: copy the attached reference room exactly - the barn-style vaulted great room with the dark exposed timber trusses across the ceiling, the arched front door, the balcony above, the kitchen island with rattan pendant lights, the cream sectional sofa, the lit Christmas tree and the garlands. Same architecture, same furniture, same decorations, same camera position in the room.

TWO THINGS CHANGE FROM THE REFERENCE: first, there is no projected light anywhere - the ceiling, the timber trusses and the walls are plain plaster and plain dark wood, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the pendant lights and ordinary warm lamps. Second, the woman and her ladder are in the room as described below.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE VAULTED CEILING high above her, between the timber beams, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s, light grey sweater, jeans, fluffy socks, standing near the top of a tall wooden A-frame ladder that reaches up into the vaulted space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The vaulted ceiling reads as clean white and off-white plaster, her sweater reads as true light grey, the timber trusses read as natural dark wood, the sectional reads as true cream. The Christmas tree lights and the pendants are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high vaulted ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

#### Image prompt — `references/v4_c01_r1.png`

Not a Higgsfield generation on record (no matching job in the workspace history) — a supplied reference.

#### Image prompt — `references/v4_c01_r2.png`

Not a Higgsfield generation on record (no matching job in the workspace history) — a supplied reference.

#### Video prompt — `clips/v4_c01_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `36471ab7-0f8c-4a07-bd42-6197dbccc780`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_205206_36471ab7-0f8c-4a07-bd42-6197dbccc780.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`
- image ref 1: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`

````text
ONE CONTINUOUS HANDHELD TAKE, NO CUTS. Hyper-realistic, natural, like a real phone video a family member shot by accident. The scene, the room, the woman, her clothes, the ladder and the inflatable Santa taped to the ceiling are exactly as in the start frame and never change.

CAMERA: a real person standing a few steps behind her holds the phone at chest height. The camera stays in one place with small natural handheld sway. Between 1.6s and 2.6s it tilts gently DOWN to follow her to the floor, then holds. No zoom, no push-in, no orbit, no slow motion, no speed ramp. The ladder and the rug stay in frame the whole time.

BEATS:
0.0-1.0s — She is up on the step ladder with both arms above her head, pressing a strip of tape onto the inflatable Santa's shoulder. She smooths it with her palm twice, rising slightly onto the balls of her feet on the step, shoulders working, head tilted up.
1.0-1.6s — The strip of tape peels away from the ceiling under her hand. Her weight shifts, her hips swing out to one side and the ladder tips over with her. Her free hand grabs at the air.
1.6-2.6s — She comes down, sliding and scrambling against the tipping ladder, body low and close to it the whole way, and the ladder goes over sideways onto the rug beside her. She does not leap, spin or fly.
2.6-4.0s — She ends up sitting slumped on the rug on her backside next to the fallen ladder, legs sprawled, one hand flat on the floor, chest heaving. The roll of tape rolls a short distance across the rug and stops. She stays down, looks up at the ceiling and lets her head drop back. She does not get up.

HARD RULES: The inflatable Santa stays taped flat to the ceiling for the entire clip and never falls, never detaches, never lands on her. Everything stays low and inside the room. NO object is thrown, launched, flung or flies through the air. No Christmas tree falls, no furniture moves, nothing leaves the frame. She does not bounce, does not roll over, does not somersault. No other people, no pets, no doors opening. No cuts, no jump cuts, no scene change, no second angle. No captions, no text, no on-screen graphics, no logos, no watermark.

AUDIO: natural room sound only — no music, no score, no background song. The rip of tape, a short startled gasp from her, the clatter of the aluminium ladder hitting the floor, then quiet room tone and her breathing. No dialogue.
````

#### Video prompt — `clips/v4_c01_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `63137ca3-5de5-4702-b0ee-5ccbf2818d7a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_205942_63137ca3-5de5-4702-b0ee-5ccbf2818d7a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`
- image ref 1: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`

````text
THE FIRST FRAME OF THIS VIDEO IS THE ATTACHED START IMAGE, PIXEL FOR PIXEL. This is the most important rule in the clip. Frame 0 is identical to @Image 1 — same camera position, same height, same angle, same distance, same room, same white ceiling, same inflatable Santa taped flat to the ceiling, same step ladder, same woman seen from behind and below in her light grey sweater and jeans, same Christmas tree and furniture in the same places. Nothing is re-imagined, re-framed, re-lit or re-designed at any point.

CAMERA: ONE LOCKED HANDHELD SHOT, filmed by a person standing in the room a few steps behind her, phone held at chest height. The camera stays in exactly the same spot for all 4 seconds with only tiny natural hand sway and micro-jitter. THE CAMERA DOES NOT MOVE: no zoom, no push-in, no pull-back, no dolly, no pan, no tilt up, no tilt down, no crane, no orbit, no rack focus, no slow motion, no speed ramp. The frame does not reframe to follow her — she falls out of the lower part of the frame naturally, the way a real phone video would catch it. NO CUTS, no jump cuts, no second angle, no scene change. No phone, hand, fingers, thumb, arm or any object ever appears in the foreground.

BEATS:
0.0-1.0s — She stays exactly as in the start image, arms above her head, and presses the strip of tape onto the inflatable Santa's shoulder, smoothing it with her palm twice, rising slightly onto the balls of her feet on the step.
1.0-1.6s — The tape peels off the ceiling under her hand. Her weight shifts, her hips swing to one side and the ladder starts tipping over with her. Her free hand grabs at the air.
1.6-2.6s — She goes down with the ladder, body staying low and close against it, sliding and scrambling, and the ladder falls sideways onto the rug. She does not leap, spin, somersault or fly.
2.6-4.0s — She is down on the rug beside the fallen ladder, sitting slumped on her backside with her legs sprawled, one hand flat on the floor, breathing hard, head tipped back looking up at the ceiling. The roll of tape rolls a short way across the rug and stops. She stays down and does not get up.

HARD RULES: The inflatable Santa stays taped flat to the ceiling for the entire clip — it never falls, never detaches, never lands on her. Everything stays low and inside the room. NO object is thrown, launched, flung or flies through the air. The Christmas tree does not fall, no furniture moves, no decorations come down. No other people, no pets, no doors opening. No captions, no text, no on-screen graphics, no logos, no watermark.

AUDIO: natural room sound only — no music, no score, no background song. The rip of tape, one short startled gasp, the clatter of the ladder hitting the floor, then quiet room tone and her breathing. No dialogue.
````

#### Video prompt — `clips/v4_c01_g3.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `48e780b3-acd8-4004-81c2-9a0db3eef87d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_211738_48e780b3-acd8-4004-81c2-9a0db3eef87d.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`
- image ref 1: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`

````text
Real home video. One continuous handheld phone shot, no cuts, camera never moves from where it is in the attached image.

For the first second she is just taping the inflatable Santa to the ceiling — both hands up, pressing and smoothing, nothing dramatic.

Then she loses her footing and falls off the ladder to the floor.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second — fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery. The ladder goes over with her and clatters onto the rug. She lands hard, stays down, stunned, and is still on the floor when the clip ends.

The inflatable Santa stays taped to the ceiling the whole time.

No slow motion. No speed ramp. No zoom, no push-in, no pan, no tilt. No cuts, no second angle. No captions or text.

Audio: room tone only, no music — the tape, a short gasp, the ladder hitting the floor, then her breathing.
````

#### Video prompt — `clips/v4_c01_g4.mp4`

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `ee938061-a27d-40fa-8714-e370c41c510a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_212515_ee938061-a27d-40fa-8714-e370c41c510a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`
- image ref 1: `content/video_4_assets/starting_frames/v4_c01_g6.png` · Higgsfield media `34ab4b0f-7a4e-4383-9120-8602e2eeed2e`

````text
Real home video. One continuous handheld phone shot, no cuts, camera never moves from where it is in the attached image.

For the first second and a half she is just taping the inflatable Santa to the ceiling — both hands up, pressing and smoothing, nothing dramatic.

Then she loses her footing and falls off the ladder to the floor.

The fall has real weight. An ordinary woman's balance goes, gravity takes her, and she is on the floor in well under a second — fast, heavy, a bit ugly, exactly like real footage of someone coming off a ladder. Her limbs are heavy and human, not floaty or rubbery, and she never hangs in the air. The ladder goes over with her and clatters onto the rug.

She lands hard and then the room is still. She stays down on the floor for the last second and a half, not moving much, just stunned and breathing, and she is still there when the clip ends.

The inflatable Santa stays taped to the ceiling the whole time.

No slow motion. No speed ramp. No zoom, no push-in, no pan, no tilt. No cuts, no second angle. No captions or text.

Audio: room tone only, no music — the tape, a short gasp, the ladder hitting the floor, then her breathing.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v4_c02_g1.png` → `clips/v4_c02_g1.mp4`

#### Image prompt — `starting_frames/v4_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `624bfa6f-b152-4cc4-9667-b7d3414b2755`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_181932_624bfa6f-b152-4cc4-9667-b7d3414b2755.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `1cdfcc53-e771-4bba-9eab-b1788346098b`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a charcoal-grey cable-knit wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a dark-stained quarter-sawn oak trestle table top: broad boards with tight straight grain and the distinctive pale medullary ray flecks of quarter-sawn oak showing through the deep brown stain, a matte hand-rubbed oil finish with almost no sheen. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused American Craftsman Christmas living room: a fireplace faced in dark green glazed tile under a heavy oak mantel with knitted stockings hanging from it, a built-in oak bookcase with leaded-glass doors beside it, a decorated Christmas tree with warm white fairy lights and burgundy and antique brass baubles standing off to one side, a brass floor lamp with an amber mica shade glowing warm, all well out of focus so the box stays the clear subject.

Dress the oak table more festively: a sprig of fir and a few red berries, two or three small brass and burgundy baubles, a short cream candle, a soft warm string light trailing across the oak, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.
````

#### Video prompt — `clips/v4_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `b45761d0-802e-4162-b285-cfc4e18d0c87`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214327_b45761d0-802e-4162-b285-cfc4e18d0c87.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c02_g1.png` · Higgsfield media `624bfa6f-b152-4cc4-9667-b7d3414b2755`
- video ref 1: `references/scene_no_audio-2.mp4` — upload · 2.14 s · Higgsfield media `1d2e8a8d-1e49-422a-8b04-d1a1230096a4`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a dark-stained quarter-sawn oak trestle table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a charcoal-grey cable-knit wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a dark-stained quarter-sawn oak trestle table fills the frame. A lit cream pillar candle sits at the left, fir sprigs with red berries and small brass and burgundy baubles beside it, a dark green glazed-tile fireplace with a heavy oak mantel, hanging knitted stockings and an oak bookcase with leaded-glass doors, and a decorated Christmas tree with warm white lights and burgundy and antique brass baubles softly out of focus behind. The candle, the fir, the berries, the baubles, the defocused fireplace and the defocused tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the dark-stained quarter-sawn oak trestle table, lid flaps folded back, with the candle, the fir, the berries, the defocused fireplace and the defocused tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v4_c03_g1.png` → `clips/v4_c03_g1.mp4`

#### Image prompt — `starting_frames/v4_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `e877bf29-bdb8-4d79-9e16-4da1f2f724fb`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_181932_e877bf29-bdb8-4d79-9e16-4da1f2f724fb.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `7ccdd557-bfee-45b0-a067-0652320f537b`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a charcoal-grey cable-knit wool sweater sleeve pushed back; right forearm enters from the right in the same charcoal-grey sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed charcoal soapstone counter: deep grey-black stone with a soft matte surface and faint pale veining drifting through it, a softly eased square edge, a low satin lustre that catches the warm light without shining. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. An American Craftsman Christmas kitchen, softly defocused: sage-green shaker cabinets with unlacquered brass cup pulls, a cream zellige tile backsplash with its slightly uneven handmade glaze, a black cast-iron range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v4_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `4600f082-31cd-4111-baf8-814fff5dd452`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214326_4600f082-31cd-4111-baf8-814fff5dd452.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c03_g1.png` · Higgsfield media `e877bf29-bdb8-4d79-9e16-4da1f2f724fb`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a honed charcoal soapstone kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in charcoal-grey cable-knit wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a honed charcoal soapstone countertop fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with sage-green shaker cabinets with unlacquered brass cup pulls, a black cast-iron range built into the tall cabinet run on the left, a cream zellige tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the soapstone counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The soapstone is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v4_c04_g1.png` → `clips/v4_c04_g2.mp4`

#### Image prompt — `starting_frames/v4_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `7aa2297c-f157-474c-b631-a43a0fe73c00`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_181932_7aa2297c-f157-474c-b631-a43a0fe73c00.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a charcoal-grey cable-knit wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed charcoal soapstone counter: deep grey-black stone with a soft matte surface and faint pale veining drifting through it, a softly eased square edge, a low satin lustre that catches the warm light without shining. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. An American Craftsman Christmas kitchen, softly defocused across the top third of the frame: sage-green shaker cabinets with unlacquered brass cup pulls, a cream zellige tile backsplash with its slightly uneven handmade glaze, a black cast-iron range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v4_c04_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `b5274d1d-6899-45ff-bcaf-e3cdaae82e50`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_223157_b5274d1d-6899-45ff-bcaf-e3cdaae82e50.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c04_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c04_g1.png` · Higgsfield media `70c8393e-5f54-4338-af63-462cd8dc8fb8`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a charcoal-grey cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same charcoal-grey cable-knit sleeve, no jewellery, entering from the right edge of frame, pinching the white cable connector between thumb and forefinger and holding it out horizontally toward the projector.
THE PORT - a small dark recessed rectangular socket set into the LOWER FRONT FACE of the white dome body, just above the point where the dome meets the white cradle and the flat white base plate, facing the camera and slightly to the right. It is already there in the start image as a small dark slot. It is the only opening on the body apart from the black mesh disc on top. It never moves, never changes shape and never closes.
THE CONNECTOR - a flat white plug on the end of a white cable. Its tip is a small flat oval, held level with THE PORT and pointing LEFT, straight down the axis of the socket. In the start image its tip sits a short gap away from the socket mouth - roughly the length of the plug itself. The cable behind it is one continuous unbroken piece running back under her fingers and off the right edge of frame; it is never cut, never doubled and never disappears.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a honed charcoal soapstone countertop fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with sage-green shaker cabinets with unlacquered brass cup pulls, a black cast-iron range built into the tall cabinet run on the right, a cream zellige tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND moves the white connector LEFT along the socket's own axis, in one straight unbroken push, and closes the whole gap: the flat oval tip meets the mouth of THE PORT and slides inside it. The plug travels its full length - about 1 cm - so the entire metal-free tip disappears into the dark slot and only the white plastic body of the plug is left outside. The plug stays perfectly level and square to the socket the whole way; it never tilts, never scrapes down the outside of the housing and never stops short. THE LEFT HAND stays still on the dome.
1.0-2.0s - the plug is fully home. Its white plastic shoulder is now pressed flat against the white face of the dome body around the socket, with NO gap, NO daylight and NO shadow line between the plug and the housing - plastic touching plastic. Her thumb and forefinger give one last short firm push of a couple of millimetres, the plug does not move any further, and the cable behind it bends slightly and hangs from the connector under its own weight. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the soapstone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; a connector that stops short of the socket; a gap left between the plug and the housing when it is seated; a plug that hovers in front of the body without entering it; a plug that slides down the outside of the housing instead of into the socket; a plug that passes through the housing or vanishes into solid white plastic; the socket closing, moving or healing over; a plug that is still outside the body after 1.0s; a cable that is cut, doubled, detached or floating; the plug being pulled back out; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

**Other takes of C04 on disk (1)**

#### Video prompt — `clips/v4_c04_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `1804769b-e6e1-4de1-a8ae-97a54dc615a2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214327_1804769b-e6e1-4de1-a8ae-97a54dc615a2.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: uploaded image, not on the drive · Higgsfield media `7aa2297c-f157-474c-b631-a43a0fe73c00`

````text
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a charcoal-grey cable-knit wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same charcoal-grey cable-knit sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a honed charcoal soapstone countertop fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with sage-green shaker cabinets with unlacquered brass cup pulls, a black cast-iron range built into the tall cabinet run on the right, a cream zellige tile backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the soapstone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v4_c05_g1.png`, `references/v4_c05_r2.png` → `clips/v4_c05_g2.mp4`

#### Image prompt — `starting_frames/v4_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a3d7df02-f6f1-486f-9b05-2ce08e16aa76`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_181932_a3d7df02-f6f1-486f-9b05-2ce08e16aa76.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American four-panel door painted a deep matte forest green: crisp raised mouldings around four flat recessed panels, clean painted surfaces with the faintest brush texture, an oil-rubbed bronze knob and a matching oil-rubbed bronze escutcheon plate, set in a plain stained oak frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the forest green paint reads clearly as green rather than black, the bronze knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the bronze knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Image prompt — `references/v4_c05_r2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `9260746b-a26d-4de6-b1e2-91bacfbddff4`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_195527_9260746b-a26d-4de6-b1e2-91bacfbddff4.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `f3a8c329-4152-4a22-9469-d89578812e09`
- @Image 2: `references/house_great_room_beams.png` · Higgsfield media `e402f616-c876-4e01-bb5a-60774babf36a`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its beams, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height living space whose ceiling is flat smooth cream plaster crossed by four heavy square-sawn pale oak beams running left to right at even spacing, each one a real chunky timber with square corners and visible grain where it lands on the wall, and one large rectangular flush skylight set into the plaster between the first two beams; a first-floor gallery landing crossing the left and centre of the room at mid height, its railing made of slim black metal balusters under a black top rail with a plain cream fascia below it; a straight run of stairs on the right coming down towards the camera with pale oak treads and the same slim black baluster railing; tall black-framed windows filling the right-hand wall to full height; pale limewashed plaster walls; and underneath the gallery an open kitchen with a white marble waterfall island, open shelving with pottery and a full-height pale oak cabinet run. Terracotta saltillo tile floor laid in a square pattern, a large faded Persian rug in rust, cream and terracotta, a big cream linen sectional sofa, a chunky rustic reclaimed-wood low coffee table, and a large olive tree in a terracotta pot in the right foreground. Copy the proportions, the beam spacing, the skylight, the railings and the stair from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall windows show a dark blue snow-covered night outside, there is no daylight and no sunlight anywhere in the room, every lamp, pendant and downlight in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing in front of the tall windows with warm white lights and burgundy and antique brass baubles and wrapped gifts underneath, a thick evergreen garland with pine cones and burgundy ribbon wound along the gallery railing and down the stair rail, knitted stockings hanging from the gallery rail, and a bowl of burgundy and brass baubles on the coffee table. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every plaster wall, the whole flat plaster ceiling and its four heavy square oak beams, and the fascia and railing of the gallery landing, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling plane and run with the direction of the oak beams instead of hanging as vertical curtains, and visibly break and step where each heavy beam crosses them; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the ceiling plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the wall above the gallery landing; one big brilliant north star high beside the skylight with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across the whole ceiling; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the oak beams. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every heavy square oak beam with its grain and its square corners, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each beam breaks the light with its own hard shadow line where it stands proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the ceiling plane and stepping where it crosses each beam. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling crossed by four heavy oak beams with a skylight set between them, never as a backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The terracotta tile floor, the Persian rug, the cream sectional sofa, the olive tree, the Christmas tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v4_c05_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `bb6a9aaf-18be-40f1-a3b9-24a450f6f623`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_223249_bb6a9aaf-18be-40f1-a3b9-24a450f6f623.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c05_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c05_g1.png` · Higgsfield media `3587bbac-bcf9-4f7e-bfd5-da95454643ff`
- image ref 1: `content/video_4_assets/references/v4_c05_r2.png` · Higgsfield media `5d9846e6-2297-464a-87cd-8927806f172e`
- video ref 1: `references/scene_no_audio-5.mp4` — silenced upload padded to 4.50 s · Higgsfield media `c5b72684-3884-4e7d-8b77-7bad9f4af4cf`

````text
RULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on the walls and on the ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the restlessness of every element inside the projected picture, not one of them ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every cottage chimney on the walls is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to one side, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the walls and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling, away from where it sits in the start image and toward the far side of the ceiling, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, and the whole team rises and dips a little as it goes. It is never parked.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts, breathes brighter and dimmer on its own timing, and cycles slowly through red, green, blue and gold. One that reaches the floor fades out there while a fresh one fades in high near the ceiling line, so the density holds even. This happens on every wall and across the whole ceiling at once.
- THE VILLAGE AND THE FOREST - the lit cottage windows and the church windows flicker gently and breathe brighter and dimmer on their own timing, and the fir trees sway very slightly as if in a light wind. The village never sits completely dead.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON - the moon is the ONE element that holds its position. It stays exactly where it is for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the walls and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the walls are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. THE CEILING IS THE BUSIEST PART OF THE PICTURE, NOT THE CALMEST: when the camera tilts up and the ceiling fills the frame, the aurora is rippling along its whole length, the sleigh and reindeer are flying across it, the snowflakes are pouring down it and the stars are twinkling, so the ceiling is never a quiet or empty surface. Nothing is painted, printed or stencilled on the plaster.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this picture. At 0.0s the film RESUMES and every element inside the picture starts moving and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, doors, furniture, people, colours and framing. It does NOT apply to anything inside the projected picture. Every element inside the picture must leave its starting position immediately.

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the forest green door, the bronze of the round knob and its escutcheon, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed forest green four-panel door in its stained oak frame, the bronze round knob on its bronze escutcheon, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow hanging on the door.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree in front of the tall black-framed windows on the right, the cream linen sectional sofa in the foreground, the gallery landing with its garlanded black baluster railing, the flat plaster ceiling on its four heavy oak beams, the two children and their charcoal-grey and cream fair-isle knitwear, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - charcoal-grey and cream fair-isle knitted Christmas jumper with oatmeal knitted lounge trousers, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching charcoal-grey and cream fair-isle knitwear, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a big American great room with a flat cream plaster ceiling crossed by four heavy pale oak beams and one flush skylight: tall decorated Christmas tree in front of the tall black-framed windows on the right, cream linen sectional sofa in the foreground, gallery landing with slim black metal balusters and a garlanded rail crossing the room at mid height, an open kitchen with a white marble island underneath it, terracotta tile floor with a large faded Persian rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, the hallway lit only by its own warm dim light, the bare right forearm reaching to the bronze knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the bronze knob, turns it and pushes; the door swings away from the camera and the room behind it comes into view. The projection is ALREADY running at full strength on the far wall and across the whole ceiling before the door moves - the widening doorway simply uncovers more of a display that was already there, the way drawing a curtain back uncovers a view. Nothing lights up, ignites, spreads, ripples or switches on as the door opens, and nothing glows along the edge of the door, along the door frame or in the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light is sweeping across the far wall and the tree and raining down over the floor ahead and over the camera's own path, at exactly the same speed and the same brightness it already had before the door opened.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the field of light keeps sliding and pouring down every wall and across both children, shapes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The light is sweeping and pouring across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the moving projection as the only bright light source. Because the shapes are sweeping and pouring, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Knitwear and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the projection is already running at full strength on the walls and across the whole ceiling in the very first frame in which any part of the room is visible, and its brightness never changes from that moment on; the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only. Every element inside the picture is visibly travelling in every single frame - the chimneys smoke, the aurora ripples, the sleigh and reindeer fly across the ceiling, the flakes pour down, the stars twinkle - while the picture's outer boundary holds still. The walls and the ceiling always move together. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that only twinkle without travelling; a still ceiling above a moving wall; a quiet or empty ceiling when the camera tilts up; the whole picture rotating, spinning, sweeping or sliding across the room as one sheet; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a glittering sparkler, a strip of fairy lights, a glowing seam, a bright vertical line, a shaft or any other light effect along the edge of the door, along the door frame or in the door gap; light that grows, spreads, ignites, switches on or fills the room as the door opens; a projection that is dim or absent when the door starts to move and gets stronger afterwards; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
````

**Other takes of C05 on disk (2)**

#### Image prompt — `references/v4_c05_r1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `367765ca-c873-4750-a2b6-4cebe5167a20`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_181933_367765ca-c873-4750-a2b6-4cebe5167a20.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `f3a8c329-4152-4a22-9469-d89578812e09`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. An American Craftsman great room in a traditional house: soft sage green painted walls above quarter-sawn oak wainscoting to waist height with a broad oak plate rail, a high vaulted ceiling clad in warm cream painted tongue-and-groove boards with exposed dark stained oak rafters rising to a dark stained oak ridge beam, a full-height clinker brick fireplace on the right with a low fire burning and a heavy oak mantel with knitted stockings hanging from it, a deep burgundy roll-arm sofa with olive green cushions and a cream cable-knit throw, a patterned wool rug over wide oak floorboards, a tall real Christmas tree in the left corner with warm white lights and burgundy and antique brass baubles, wrapped gifts under it, and a tall oak-trimmed window with leaded glass behind the tree showing a dark blue snow-covered night outside.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every painted wall, the whole vaulted boarded ceiling and its oak rafters and ridge beam, and the clinker brick of the fireplace, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the wall beside the fireplace; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the sage paint and the cream boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the tongue-and-groove boards, their seams and their subtle grain, and every dark stained oak rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the patterned rug, the burgundy sofa, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v4_c05_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `21d9baec-5ff6-415b-96b7-94e881c3edaa`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214449_21d9baec-5ff6-415b-96b7-94e881c3edaa.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: uploaded image, not on the drive · Higgsfield media `a3d7df02-f6f1-486f-9b05-2ce08e16aa76`
- image ref 1: uploaded image, not on the drive · Higgsfield media `9260746b-a26d-4de6-b1e2-91bacfbddff4`
- video ref 1: `references/scene_no_audio-5.mp4` — silenced upload padded to 4.50 s · Higgsfield media `c5b72684-3884-4e7d-8b77-7bad9f4af4cf`

````text
RULE ZERO - THE ONLY THING THAT DECIDES WHETHER THIS CLIP IS USABLE. READ THIS BEFORE ANYTHING ELSE.
The Christmas light pattern on the walls and on the ceiling MUST BE MOVING, hard and fast, in every single frame. This is the entire purpose of the clip. Every previous attempt failed for exactly one reason: the pattern sat still like wallpaper. If the pattern is still, the clip is worthless.

@Video 1 IS THE MOTION AUTHORITY. It is real footage of this exact projector running. Copy the MOVEMENT of the projected light from @Video 1: its speed, its direction, its restlessness, the way the whole field of glowing shapes slides and swarms across the plaster without ever pausing. Match that amount of movement or exceed it.
TAKE NOTHING ELSE FROM @Video 1 - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. @Video 1 is completely silent and has no audio track at all; import no sound whatsoever from it. It is a MOVEMENT REFERENCE ONLY.

WHAT THE LIGHT DOES, described so it cannot be mistaken for a texture:
- The whole field of glowing shapes SLIDES BODILY across the wall and across the ceiling, the way light from a spinning projector head sweeps a room. It never locks onto the plaster.
- On top of that sliding, individual shapes POUR DOWNWARD like heavy snowfall filmed through a window at night, and each one spins slowly as it goes and drags a faint soft trail.
- SPEED: a single shape crosses the full height of the wall in ABOUT ONE SECOND. That is fast. A viewer must see it moving within the first quarter second of the clip.
- THE TEST: take any two frames a third of a second apart and lay them on top of each other. NOT ONE glowing shape is in the same place. Not one. If any shape has stayed put, the clip is wrong.
- The moving light also pours down over the tree, the sofa, the floor and across both children's faces and knitwear as it passes over them, so the brightness on everything in the room is changing continuously. The projected picture is never a still mural or a painted scene held on the wall: the entire picture - every star, every shape, every band of colour - is travelling.
- THE START IMAGE IS A SINGLE PAUSED FRAME of this moving light. At 0.0s the video RESUMES and the light instantly goes back to sweeping and pouring and never stops - not for one frame, not at the beginning and not at the end.
- "Hold the start image" applies to the ROOM: its walls, doors, furniture, people, colours and framing. It does NOT apply to the light pattern. The light pattern must leave its starting position immediately.

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the forest green door, the bronze of the round knob and its escutcheon, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed forest green four-panel door in its stained oak frame, the bronze round knob on its bronze escutcheon, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow hanging on the door.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree in front of the tall black-framed windows on the right, the cream linen sectional sofa in the foreground, the gallery landing with its garlanded black baluster railing, the flat plaster ceiling on its four heavy oak beams, the two children and their charcoal-grey and cream fair-isle knitwear, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - charcoal-grey and cream fair-isle knitted Christmas jumper with oatmeal knitted lounge trousers, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching charcoal-grey and cream fair-isle knitwear, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - a big American great room with a flat cream plaster ceiling crossed by four heavy pale oak beams and one flush skylight: tall decorated Christmas tree in front of the tall black-framed windows on the right, cream linen sectional sofa in the foreground, gallery landing with slim black metal balusters and a garlanded rail crossing the room at mid height, an open kitchen with a white marble island underneath it, terracotta tile floor with a large faded Persian rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, the hallway lit only by its own warm dim light, the bare right forearm reaching to the bronze knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the bronze knob, turns it and pushes; the door swings away from the camera and the room behind it comes into view. The projection is ALREADY running at full strength on the far wall and across the whole ceiling before the door moves - the widening doorway simply uncovers more of a display that was already there, the way drawing a curtain back uncovers a view. Nothing lights up, ignites, spreads, ripples or switches on as the door opens, and nothing glows along the edge of the door, along the door frame or in the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light is sweeping across the far wall and the tree and raining down over the floor ahead and over the camera's own path, at exactly the same speed and the same brightness it already had before the door opened.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the field of light keeps sliding and pouring down every wall and across both children, shapes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The light is sweeping and pouring across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the moving projection as the only bright light source. Because the shapes are sweeping and pouring, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Knitwear and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the projection is already running at full strength on the walls and across the whole ceiling in the very first frame in which any part of the room is visible, and its brightness never changes from that moment on; the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a glittering sparkler, a strip of fairy lights, a glowing seam, a bright vertical line, a shaft or any other light effect along the edge of the door, along the door frame or in the door gap; light that grows, spreads, ignites, switches on or fills the room as the door opens; a projection that is dim or absent when the door starts to move and gets stronger afterwards; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v4_c06_g2.png` → `clips/v4_c06_g1.mp4`

#### Image prompt — `starting_frames/v4_c06_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `25a6c79a-8576-43c0-89b6-4157c77c312d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_195559_25a6c79a-8576-43c0-89b6-4157c77c312d.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `0a845da6-2607-46cc-a595-4fee4b17d6a9`
- @Image 2: `references/house_bedroom_rafters.png` · Higgsfield media `c1ea3b08-e710-4bda-9d33-4dd99b0e3012`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with her family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its truss, its walls, its window and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a girl of about seven with long auburn hair, fully dressed for winter in a warm charcoal-grey and cream fair-isle knitted Christmas jumper with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. She is standing up on top of the bed, knees bent and both arms raised out to her sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge. Wholesome family Christmas scene, a child at home with her family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom under a high vaulted roof, the ceiling two sloping planes of smooth cream plaster meeting at a ridge that runs away from the camera, crossed by heavy reclaimed oak rafters - a king-post truss near the front, its two rafters meeting at the ridge above a horizontal collar, and four or five more rafters marching down the right-hand slope onto a horizontal oak wall plate - with small recessed downlights set into the plaster between them, and a big black wrought-iron ring chandelier of two concentric rings carrying a row of plain candle bulbs hanging on a black rod from the ridge; a tall gable end wall on the left with a triangular-headed window above a pair of dark-framed glazed doors with side lights and long taupe linen curtains; a horizontal grey-brown plank accent wall behind the bed with three small framed prints in thin dark frames and a black wall sconce beside them; a low reclaimed-wood platform bed with a wide plank headboard, two nightstands with table lamps, wide pale oak plank floorboards and a large flat-weave oat rug. Copy the proportions, the rafter spacing, the king-post truss, the ridge, the ring chandelier and the gable window from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the gable window and the glazed doors show a dark blue snow-covered night outside, there is no daylight anywhere in the room, the ring chandelier and every downlight and table lamp are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a burgundy quilt, a cream cable-knit throw and ticking-stripe pillows, a knitted stocking hangs from the rafter above the headboard, a warm fairy-light garland is strung around the gable window, a small lit Christmas tree stands on the floor beside the bed, and a small evergreen wreath with a burgundy bow hangs on the plank wall. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both sloping plaster ceiling planes, the heavy oak rafters and the king-post truss, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the gable window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the cream plaster and the oak rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, and every heavy reclaimed oak rafter, the king-post truss and the ridge, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the truss break the light with their own hard shadow lines where they stand proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as two sloping plaster planes meeting at a ridge and crossed by heavy oak rafters, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the flat-weave rug, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Her knitted jumper catches that spill so the jumper and the mid-bounce pose read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v4_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `7a10dfc4-5f87-4d14-afc0-8810a304ed6c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214449_7a10dfc4-5f87-4d14-afc0-8810a304ed6c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c06_g2.png` · Higgsfield media `25a6c79a-8576-43c0-89b6-4157c77c312d`

````text
SUMMARY: a girl bounces on her bed in a vaulted Christmas bedroom at night while a projected snow-village picture is PLAYING across the left wall and the whole sloping plaster ceiling and its heavy oak rafters, thrown there by a projector standing on the floor. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the vaulted bedroom, the heavy oak rafters and the king-post truss, the bed with its burgundy quilt and cream cable-knit throw, the wide plank headboard, the grey-brown plank accent wall, the small lit Christmas tree, the oat flat-weave rug, the gable window with its garland, the stocking, THE GIRL and the colour.

SUBJECTS:
THE GIRL - exactly one child in a charcoal-grey and cream fair-isle knitted Christmas jumper and oatmeal knitted lounge trousers, standing on the bed with her arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall and both slopes of the ceiling. Everything glowing on the timber and the plaster is that one cone landing.
THE PICTURE - the animated scene that cone is playing: snow-covered gabled cottages with lit windows and fir trees low on the LEFT wall, plumes above their chimneys, ribbons of aurora arching across both slopes of the ceiling, a sleigh drawn by reindeer keystoned across the ceiling at the upper right, a big pale moon over on the left, a dense field of gold stars of many sizes, and a heavy fall of small glowing six-point snowflakes and points of light in red, green, blue, gold and white.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the timber and the plaster and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE GIRL and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every cottage chimney on the left wall is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on both ceiling slopes is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from the upper right corner where it sits in the start image, toward the far side of the ceiling, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, and the whole team rises and dips a little as it goes.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts, breathes brighter and dimmer on its own timing, and cycles slowly through red, green, blue and gold. One that reaches the skirting board fades out there while a fresh one fades in high near the ridge, so the density holds even. Track this one so the fall is unmistakable: a large white six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.0s and fades out low near the skirting at 4.0s.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON - the moon is the ONE element that holds its position. It stays exactly where it is on the left for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and both ceiling slopes are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the oak rafters.

TIMELINE:
0.0-1.5s the camera holds still. THE GIRL bends her knees and pushes off the mattress; both feet leave the duvet, arms swinging up over her head, mouth open laughing. The mattress compresses and springs back.
1.5-2.5s the camera still holds. She lands on both feet and drives straight into a second, higher jump, knees tucking.
2.5-4.0s the camera tilts up in one slow smooth move until the sloping ceiling fills the upper half of the frame, the aurora rippling along both slopes and the sleigh still flying across it. THE GIRL stays low in frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a girl laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real girl jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes one move only, a tilt up at the end. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; blur; a cut; on-screen text; subtitles.
````

**Other takes of C06 on disk (1)**

#### Image prompt — `starting_frames/v4_c06_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `4c885155-2672-4e5c-a853-b548d9eb1a03`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_184129_4c885155-2672-4e5c-a853-b548d9eb1a03.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `0a845da6-2607-46cc-a595-4fee4b17d6a9`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with her family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a girl of about seven with long auburn hair, fully dressed for winter in a warm charcoal-grey and cream fair-isle knitted Christmas jumper with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. She is standing up on top of the bed, knees bent and both arms raised out to her sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge. Wholesome family Christmas scene, a child at home with her family at Christmas.

CHANGE 2 - THE ROOM. A classic American child's bedroom tucked under the roof: a low sloped ceiling on both sides clad in soft butter-cream painted tongue-and-groove boards with white-painted exposed rafters running up to a ridge beam, white painted beadboard on the knee wall below, a small white-trimmed dormer window with a dark snowy night outside and a warm fairy-light garland around it, a low sage-green painted wooden bed set against the knee wall made up with a burgundy quilt, a cream cable-knit throw and ticking-stripe pillows, a knitted stocking pinned to the rafter above the headboard, a small lit Christmas tree standing on the floor beside the bed, a braided round rug on wide oak floorboards, and a low sage-green bookshelf of picture books tucked under the slope.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both painted sloped ceiling planes and the white rafters, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the dormer window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the painted boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the painted boards, their seams and their subtle grain, and every white-painted rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the braided round rug, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Her knitted jumper catches that spill so the jumper and the mid-bounce pose read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v4_c07_g2.png` → `clips/v4_c07_g1.mp4`

#### Image prompt — `starting_frames/v4_c07_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `245f4be5-1799-4f2e-8fe4-7df48c13d29d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_195633_245f4be5-1799-4f2e-8fe4-7df48c13d29d.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `c9a6740d-383b-4829-a7b9-f7a3c079c03f`
- @Image 2: `references/house_great_room_trusses.png` · Higgsfield media `1d79cde5-c6a5-4259-b414-2b0d4bd8434b`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long wavy auburn hair, the boy is about five with short auburn hair. Both are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: an enormous double-height great room whose ceiling is a cathedral vault of smooth cream plaster in two long slopes meeting at a ridge that runs away from the camera, crossed by two pairs of dark walnut-stained timber rafters, each pair rising as an inverted V to meet at the ridge with a matching collar beam below it, and small recessed downlights set flush into the plaster between them; a first-floor gallery landing crossing the right-hand half of the room at mid height, its railing made of clear glass panels held in slim black metal posts under a dark timber top rail; an open-tread pale oak staircase descending from that landing towards the camera with the same glass-and-black-post railing and black wall sconces on the wall beside it; a tall arched window with dark muntins set high on the right above the stair; a pale plaster back wall at the centre carrying a black arched double glazed door of many small panes; and along the left an open kitchen with pale oak slab cabinetry, a full-height integrated cabinet run, a cream island with a stone waterfall front, four woven rattan counter stools and two big woven rattan dome pendants hanging on long black cords. Wide warm oak plank floor, a large pale grey sectional sofa wrapping the right foreground, a round dark-stained wood coffee table and a large greige rug. Copy the proportions, the rafter pairs, the ridge, the glass railing, the stair and the arched door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the arched window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every downlight, pendant and sconce in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the pale plaster back wall beside the arched door with warm white lights and burgundy and antique brass baubles and wrapped gifts beneath it, a thick evergreen garland with pine cones and burgundy ribbon wound along the gallery railing and down the stair rail, knitted stockings hanging from the gallery rail, and a large evergreen wreath with a burgundy bow on the arched door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey pale plaster back wall, the plaster walls either side of it, the whole high vaulted plaster ceiling, the dark walnut rafters and their collar beams and the underside and railing of the gallery landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the plaster wall above the gallery landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the dark walnut rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every dark walnut rafter, every collar beam and the ridge line of the vault, all stay clearly visible THROUGH the coloured light, and the rafters and the collar beams break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full it must still read as projected light on a real plastered vault with real timber rafters crossing it, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the greige rug, the grey sectional sofa, the round coffee table and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v4_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `82010def-63f7-4580-b0ec-bfd24903df95`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_214448_82010def-63f7-4580-b0ec-bfd24903df95.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v4_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_4_assets/starting_frames/v4_c07_g2.png` · Higgsfield media `245f4be5-1799-4f2e-8fe4-7df48c13d29d`

````text
SUMMARY: two children play in a double-height Christmas great room while a projected snow-village picture is PLAYING across the back wall and the whole vaulted plaster ceiling and its dark timber rafters, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the dark walnut rafters and their collar beams, the open-tread pale oak staircase and its garlanded glass railing on the right, the tall arched window high on the right with snow outside, the pale plaster back wall with its black arched glazed door and wreath, the lit Christmas tree with its presents, the pale grey sectional sofa, the round dark wood coffee table, the greige rug, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - on the rug at the front left, back to camera, facing the wall, turning on the spot with his arms out.
THE OTHER CHILD - standing up on the sofa cushions in front of the garlanded staircase on the right, back to camera, with both arms raised toward the wall, bouncing on the spot.
Both in charcoal-grey and cream fair-isle knitted Christmas jumpers and oatmeal knitted lounge trousers. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole vaulted ceiling. Everything glowing on the plaster and the timber is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a snow village across the back wall with snow-covered gabled cottages with lit windows, a little footbridge and fir trees between them, plumes above their chimneys, ribbons of aurora arching over the back wall and across the ceiling, a sleigh drawn by reindeer keystoned on the ceiling at the upper left, a big pale moon over on the right, a dense field of gold stars of many sizes, and a heavy fall of small glowing snowflakes and points of light in red, green, blue, gold and white.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and the timber and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every cottage chimney in the village is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from where it sits in the start image, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, and the whole team rises and dips a little as it goes. The team is never parked.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts, breathes brighter and dimmer on its own timing, and cycles slowly through red, green, blue and gold. One that reaches the floor line fades out there while a fresh one fades in high near the rafters, so the density holds even.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON - the moon is the ONE element that holds its position. It stays exactly where it is on the right for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster or the timber.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the vaulted ceiling fills the upper half of the frame, the aurora rippling along it and the sleigh team still flying across it. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, bare feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that only twinkle without travelling; a still ceiling above moving walls; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.
````

**Other takes of C07 on disk (1)**

#### Image prompt — `starting_frames/v4_c07_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a42f98d9-6008-43a0-bbb1-ef7cde26e12e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_184014_a42f98d9-6008-43a0-bbb1-ef7cde26e12e.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `c9a6740d-383b-4829-a7b9-f7a3c079c03f`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long wavy auburn hair, the boy is about five with short auburn hair. Both are fully dressed for winter in warm charcoal-grey and cream fair-isle knitted Christmas jumpers with a band of snowflakes across the chest, matching oatmeal knitted lounge trousers and thick mustard yellow knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. An American barn-style double-height great room: one enormous two-storey chimney breast of dark clinker brick running the full height of the space with a chunky reclaimed timber mantel and knitted stockings, whitewashed reclaimed timber plank walls either side of it, a balcony landing with a blackened steel rail crossing high across the room with an open blackened-steel-and-oak staircase rising to it on the right, exposed dark stained king-post roof trusses under a high vaulted cream boarded ceiling, tall black-framed windows on the left showing a dark blue snowy night, wide oak floorboards with a large patterned wool rug, a long deep burgundy sectional sofa with olive green cushions, a leather ottoman, and a very tall real Christmas tree standing against the brick with warm white lights, burgundy and antique brass baubles and wrapped gifts beneath it.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey clinker brick chimney breast, the whitewashed timber walls, the whole high vaulted boarded ceiling, the exposed king-post trusses and the underside and railing of the balcony landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and winding along the village lane a long procession of glowing gold carol singers and lantern carriers, each figure small but clearly readable, their lanterns burning as bright points strung out along the whole curve of the lane; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the brick above the balcony landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the dark brick and the whitewashed timber. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real brick and real boards, not paint and not a sticker. The light is TRANSLUCENT - every individual clinker brick and its mortar joints, and the planks, seams and dark trusses of the ceiling, all stay clearly visible THROUGH the coloured light, and the trusses and the mantel break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare brick and bare board. Even packed full it must still read as projected light on a real textured surface, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The oak floorboards, the patterned rug, the burgundy sectional sofa, the ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````
