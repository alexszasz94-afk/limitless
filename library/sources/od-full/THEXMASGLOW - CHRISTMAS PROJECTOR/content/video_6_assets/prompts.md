# Video 6 - prompts

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_6.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

**THEXMASGLOW - CHRISTMAS PROJECTOR**
Working title: Christmas Projector

*Historical initial stage:* B-roll starting frames, plus the hook. Seven B-roll frames, one generation each. C01 was added on 2026-09-20 as three frames, g1 picked, g4 is g1 edited, and g4 was animated the same day as `clips/v6_c01_g1.mp4`.

## Planned cut

```
C01 -> C02 -> C03 -> C04 -> C05 -> C06 -> C07
 ^ hook  ^--------- B-roll round: C02 to C07 ---------^
```

C01 was not generated in the B-roll round - Daniel asked for B-roll only. It was added on 2026-09-20 as three options, see the C01 section below.

## Brief as given

> Here is what I want you to do now. Generate me the images for the next 3 videos, only for the broll (just without the hook). The same style as you did for video 2 and 3. Different tables, backgrounds, houses, kids and animations. Try to make the animation even more insane. Don't ask me how.
>
> All the images must be extremly high quality, perfect light, iphone shots, nothing blurish. Use gpt image 2.5 Sunburst, 2k, mid quality settings, 9x16.

## Look pack chosen - dark traditional, inky green / mahogany / brass

One coherent house carried across all seven frames, different from v2, v3, v4 and v5:

| element | v6 |
|---|---|
| sleeve | deep plum wool |
| table (C02) | deep mahogany, a rich dark red-brown timber with fine ribbon-stripe figure, French-polished to a deep glassy sheen, moulded edge |
| living room (C02) | walls fully panelled in deep black-green joinery, white marble fireplace with a polished brass fender, antique gold and cream ornaments, a brass picture light over a dark gilt-framed painting |
| counter (C03, C04) | honed cream limestone, soft warm off-white with gentle caramel veining and fine darker fossil flecks, chunky bullnose, completely matte |
| kitchen (C03, C04) | inky green inset cabinets with beaded face frames, unlacquered brass cup pulls, cream tumbled-marble backsplash, cream enamel range (left in C03, right in C04) |
| door (C05 F1) | four-panel deep oxblood red in eggshell, antique brass knob and matching antique brass escutcheon, plain painted cream frame |
| great room (C05 F2) | deep forest green walls with cream panelling to waist height, dark stained tongue-and-groove vault with cream-painted rafters and a dark stained ridge beam, full-height black marble fireplace with a brass fender and a carved cream mantel, oxblood chesterfield with antique gold cushions, faded antique Persian rug over dark stained oak |
| knitwear | deep plum and oatmeal cable-knit with a cream snowflake yoke, soft grey knitted trousers, thick red socks |
| bedroom (C06) | boy ~6, short straight black hair; warm oatmeal painted tongue-and-groove slopes with dark stained rafters, deep green knee-wall panelling, antique brass bed with a red tartan quilt, Persian runner, low dark green bookshelf |
| great room (C07) | American lodge, two-storey reclaimed red brick chimney breast with a chunky dark stained timber mantel, black wrought iron mezzanine rail, dark stained king-post trusses under a high vaulted oatmeal boarded ceiling; girl ~8 long black hair in a low ponytail, boy ~5 short black hair |
| **projection signature** | **rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown** |

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

## C01 - Ladder fail, taping Santa up

*Section:* Hook
*Status:* G1 PICKED BY DANIEL - g4 is g1 with the USA flag and the pyjamas. Animated 2026-09-20 as `clips/v6_c01_g1.mp4`, FOR REVIEW.

Added 2026-09-20, after the B-roll round. Daniel: *"I want you to make me a similar image with the one made for video 5 for the hook. Change the women and the background. Same framing and angle. Generate me 3 options"*, and, asked where they should live and how far apart the rooms should be: **video 6 C01**, **three different rooms**.

### The frame

Three options, one generation each, no re-rolls.

| take | file | job | room | woman |
|---|---|---|---|---|
| g1 | `starting_frames/v6_c01_g1.png` | `836690da-363a-486e-8ca1-fdf21acd0523` | traditional double-height living room, open curved staircase, cream panelling, white marble fireplace | early 30s, long auburn hair in a low ponytail, cream cable-knit, black leggings, grey wool socks |
| g2 | `starting_frames/v6_c01_g2.png` | `79e4f6de-39e4-4715-8260-61db9f192ef7` | white modern farmhouse, wall of black-framed windows, white open stair with black spindles | mid-30s, dark brown hair in a low bun, oatmeal sweatshirt, light-wash jeans, white socks |
| g3 | `starting_frames/v6_c01_g3.png` | `b400614f-d335-4252-8433-a21fe541acdf` | American lodge, two-storey red brick chimney breast, dark king-post trusses, oatmeal boarded vault | late 20s, long black hair in a low ponytail, plum and oatmeal snowflake knit, grey knitted trousers, red socks |
| g4 | `starting_frames/v6_c01_g4.png` | `9cd2cb32-1f96-4484-ad2f-cc726aca8088` | g1's room, plus a United States flag on the wall between the staircase and the tree | g1's woman, in red and white striped Christmas pyjamas with a navy star yoke |

**Settings** - `gpt_image_2 · aspect_ratio 9:16 · resolution 2k · quality high · count 1 · use_unlim false`, output 1520 x 2688. Workspace Oneofone1. Taken off `video_5_assets/prompts.md` § C01, which records the settings that produced `v5_c01_g1.png`. **This is deliberately not the v6 B-roll model** (`gpt_image_2_5` sunburst, quality medium) - the hook frame is a reuse of the v5 hook, and rule 3 says the settings come off the source section.

**Reference attached** - `v5_c01_g1.png` itself, as job `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74`, role `image`, on all three. It is the frame that owns the geometry: camera position, ladder height, her pose, where Santa sits in the picture. The thing Daniel asked to keep *is* the thing the reference carries, so it is attached rather than described from memory - and the geometry is restated in the prompt text as well, per `feedback_reference_attachment`.

**Lineage** - reused from `video_5_assets` § C01, whose image prompt lives in `video_4_assets/prompts.md` § C01 `#### g12, g13` (the g7 base plus the `COLOUR` block, the rewritten `LIGHTING AND QUALITY` and the top-sixth `FRAMING`). Pasted verbatim. Changed, and only these:

1. **`THE ROOM` rewritten per option** - three new houses. This is the "change the background" half of the brief.
2. **The woman's paragraph rewritten per option** - hair, age, knitwear, trousers, socks. The rest of that sentence, from *"standing near the top of a tall wooden A-frame ladder"* to *"she is high off the floor"*, is byte-identical.
3. **`THE ROOM: copy the attached reference room exactly` and `TWO THINGS CHANGE FROM THE REFERENCE` were replaced by a `FRAMING AND ANGLE` block.** In v4 the attached reference was the *room* and the job of that paragraph was to strip the projection out of it. Here the attached reference is the *framing*, so the block names what must be copied - camera position, distance, angle, ladder position, floor visible below her, Santa's place in the frame - and ends *"Only the room and the woman change."* The no-projected-light sentence is kept as its own paragraph, unchanged apart from the surfaces it names: the projector is off in the hook and that clause is what keeps it off.
4. **Ceiling noun in `THE KEY ELEMENT`** - "WHITE CEILING" on g1 and g2, "HIGH VAULTED OATMEAL BOARDED CEILING ... between the dark timber trusses" on g3, because that room has a boarded vault. Same change v4 g8 made for its truss room.
5. **`COLOUR` surface nouns** - the block names the surfaces that must read neutral, so those nouns follow the room. The structure, the NOT-orange list and the closing sentence are byte-identical.

`LIGHTING AND QUALITY` and `FRAMING` are byte-identical across all three and to v4 g12. Nothing describing camera, pacing or framing was reworded.

**g3 carries the v6 look pack** - plum and oatmeal snowflake knit, red socks, red brick chimney breast, dark king-post trusses, oatmeal boarded vault - so it is the option that matches C02 to C07. g1 and g2 deliberately do not, the same way `v5_c01_g1.png` does not match the v5 look pack; that is a pick, not a defect.

#### g1 - FOR REVIEW

job `836690da-363a-486e-8ca1-fdf21acd0523` · result `hf_20260920_131256_836690da-363a-486e-8ca1-fdf21acd0523.png` · 1520 x 2688

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas living room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height traditional living room with an open curved staircase - cream panelled walls, the wide staircase at the left with a thick green garland wound around its dark timber banister and stockings hung along it, a white marble fireplace with a lit fire and a gold mirror above it, a tall Christmas tree with warm white lights and red and gold baubles at the right, a deep blue velvet sofa, a patterned red and blue rug on dark oak boards.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is early 30s with long auburn hair in a loose low ponytail, a cream cable-knit sweater, black leggings and thick grey wool socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and the panelling read as clean white and cream paint, her sweater reads as true cream, the banister and the floor read as natural wood, the rug keeps its own colours. The Christmas tree lights, the fire and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
```

**Result:** the framing holds - same low three-quarters-from-behind, ladder centre frame, Santa taped flat above her, clean band across the top sixth. Cream panelled stair wall with the garland and stockings runs up the left, tree and blue velvet sofa at the right, fire lit. Neutral balance, no orange cast, no background blur. **Flagged, not re-rolled:** the ceiling is a plain shallow dome and the room reads a little wider and more formal than the v5 frame, so she sits slightly smaller in the picture than in `v5_c01_g1.png`.

#### g2 - FOR REVIEW

job `79e4f6de-39e4-4715-8260-61db9f192ef7` · result `hf_20260920_131256_79e4f6de-39e4-4715-8260-61db9f192ef7.png` · 1520 x 2688

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas living room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height white modern farmhouse living room - white shiplap walls, a wall of tall black-framed windows at the right with a dark winter garden behind them, a white open staircase with slim black spindles at the left and a garlanded landing above it, a white plaster fireplace, a slim flocked Christmas tree with warm white lights and pale blue and silver ornaments, a light linen sectional sofa, pale wide-plank oak floor and a cream jute rug.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s with dark brown hair in a low bun, an oversized oatmeal sweatshirt, light-wash jeans and white ribbed socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and the shiplap read as clean white paint, her sweatshirt reads as true oatmeal, the window frames read as true black, the oak floor reads as natural wood. The Christmas tree lights, the fireplace and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweatshirt, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
```

**Result:** the closest of the three to `v5_c01_g1.png` in scale and stance - she fills the same amount of frame, the ladder is the same height, Santa sits in the same place. **The cleanest top band of the three**, a genuinely empty sixth of plain white ceiling. Black-framed window wall at the right, mezzanine with a black rail and garland at the left, fire lit below. Neutral throughout. **Flagged:** the room is the whitest and coolest of the three, so it reads a touch more showroom than the other two.

#### g3 - FOR REVIEW

job `b400614f-d335-4252-8433-a21fe541acdf` · result `hf_20260920_131256_b400614f-d335-4252-8433-a21fe541acdf.png` · 1520 x 2688

```text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas great room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height American lodge great room - a two-storey reclaimed red brick chimney breast with a chunky dark stained timber mantel and a lit fire, a black wrought iron mezzanine rail above at the left with stockings hung from it, dark stained king-post trusses under a high vaulted oatmeal boarded ceiling, a tall Christmas tree with warm white lights and antique gold baubles at the right, an oxblood leather sofa, a faded antique Persian rug on dark stained oak boards.

There is no projected light anywhere - the boarded ceiling, the trusses, the brick and the walls are plain painted boards, plain dark wood and plain brick, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fire and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE HIGH VAULTED OATMEAL BOARDED CEILING high above her, between the dark timber trusses, lying on its back against the boards and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is late 20s with long black hair in a low ponytail, a deep plum and oatmeal cable-knit sweater with a cream snowflake yoke, soft grey knitted trousers and thick red socks, standing near the top of a tall wooden A-frame ladder that reaches up into the vaulted space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The boarded ceiling reads as clean warm oatmeal paint, the trusses read as natural dark wood, the chimney breast reads as natural red brick, her sweater reads as true deep plum and oatmeal, the rug keeps its own colours. The Christmas tree lights, the fire and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
```

**Result:** the warmest and most lived-in of the three, and the only one carrying the v6 look pack - brick chimney breast and lit fire at the left, stockings on the iron mezzanine rail, dark king-post trusses, oxblood leather sofa, Persian rug. Santa is taped between the trusses. Clean band across the top sixth. **Flagged:** a truss crosses just under the band on the right, closer to the top edge than in g1 or g2, and the brick and the fire make this the warmest frame of the set - still neutrally balanced, but it is the one to watch if the grade matters.

#### g4 - g1 with the flag and the pyjamas, FOR REVIEW

Daniel picked g1: *"I like G1 - one thing we need to modify: I want a usa flag in the background and she should wear christmas usa pijamas"*.

Two named changes and nothing else, so this is an **edit of g1, not a re-roll of the g1 prompt** - per `feedback_fix_one_region_by_editing_the_frame`, a fresh roll of the long prompt would regenerate the whole picture and lose the room he just approved. `v6_c01_g1.png` is attached as job `836690da-363a-486e-8ca1-fdf21acd0523`, role `image`, and the prompt is short and names only what changes, per `feedback_short_prompt_when_reference_attached` - no camera, no geometry, no room description.

job `9cd2cb32-1f96-4484-ad2f-cc726aca8088` · result `hf_20260920_132402_9cd2cb32-1f96-4484-ad2f-cc726aca8088.png` · 1520 x 2688 · settings unchanged: `gpt_image_2 · 9:16 · 2k · quality high · count 1 · use_unlim false`

```text
Keep the attached image exactly as it is - the same room, the same camera position, distance and angle, the same woman in the same pose near the top of the same ladder with both arms up, the same inflatable Santa taped flat to the ceiling with the same silver duct tape, the same curved staircase, garland, stockings, marble fireplace, gold mirror, Christmas tree, blue velvet sofa and rug, the same lighting, and the same clean empty band of ceiling across the top sixth of the frame. Change only these two things:

1. HER CLOTHES: instead of the cream sweater and black leggings she is wearing matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit. Same body, same hair, same pose, same thick grey wool socks, same roll of duct tape in her left hand.

2. A UNITED STATES FLAG: a real fabric United States flag hangs flat against the plain cream wall in the background behind her, clearly readable stars and stripes, hanging straight and still. It does not cover the Christmas tree, the fireplace or the staircase, and it does not reach up into the empty band of ceiling at the top of the frame.

Everything else in the picture stays exactly as it is. Same neutral white balance with no orange cast, same iPhone snapshot look, tack sharp and in focus everywhere, absolutely nothing blurry, no background blur.
```

**Result:** the room came back unchanged - same camera, same ladder, same pose, same taped Santa, same staircase with the garland and stockings, same fireplace, tree, sofa and rug, same clean top sixth. The flag hangs flat on the cream wall between the staircase and the tree, stars and stripes readable, clear of the tree, the fireplace and the caption band. The pyjamas read as pyjamas - red and white striped top and bottoms with a navy star yoke across the shoulders - and the grey wool socks survived.

**Flagged, not re-rolled:** the striped bottoms now run all the way down her legs where g1 had plain black leggings, so her silhouette is busier against the pale wall; worth a look at whether that reads well once she falls and the legs are the last thing in frame.

### Video prompts

Generated 2026-09-20 on `v6_c01_g4.png`. One generation, no re-rolls.

| take | file | job | start frame | result |
|---|---|---|---|---|
| g1 | `clips/v6_c01_g1.mp4` | `3be81f83-f33e-4612-8a19-7d3a2c532c38` | `v6_c01_g4.png` | 4.05s, 1080 x 1920, 97 frames, audio present. FOR REVIEW - camera pulls back, see below |

**Settings** - `seedance_2_5 · mode omni_reference · aspect_ratio 9:16 · duration 4 · resolution 1080p · generate_audio true · count 1 · use_unlim false · declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612`. Workspace Oneofone1. Taken verbatim off `video_5_assets/prompts.md` § C01 `**Settings**`.

**Reference attached** - `v6_c01_g4.png` as job `9cd2cb32-1f96-4484-ad2f-cc726aca8088`, passed twice inside `medias`: once role `start_image`, once role `image`. The backend coerced the second to `image_references`, which is the recorded seedance 2.5 behaviour and not an error.

**Lineage** - Reused from v5 C01 g2 - changed: nothing. The prompt is byte-identical to `video_5_assets/prompts.md` § C01 `#### g2.mp4 - TAKE 2`. Daniel's brief for this clip (*"Held iphone shot, no cuts, no zooms. For the first second she tries to set up the inflatable christmas decoration on the ceiling then is is falling o0n the ground. Natural and hyperrealistic. Use seedance 2.5 - 4s, 1080p"*) is the same beat, the same camera and the same settings as that take, and the v5 g2 prompt names neither the room nor her clothes - the two things that physically differ between `v5_c01_g1.png` and `v6_c01_g4.png` - so there was no noun to change. v5 g2 is also the take that specifically fixed Daniel's *"It must be a held iphone shot"* note on v5 g1, by naming the hand sway and micro-jitter and banning the locked-off tripod look.

#### g1.mp4 - FOR REVIEW

job `3be81f83-f33e-4612-8a19-7d3a2c532c38` · result `hf_20260920_133110_3be81f83-f33e-4612-8a19-7d3a2c532c38.mp4` · 4.05s · 1080 x 1920 · 97 video frames · 128 audio frames

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

**Result - what was checked, frame by frame**

- **No cut.** `ffmpeg select='gt(scene,0.08)'` returns zero frames across all 97. There is no scene change, no jump, no second angle anywhere in the clip. Her body never resets or teleports.
- **Start frame held.** Frames 0 to 36 (0 to 1.5s) are the taping - both arms up, pressing and smoothing. The fall begins between frame 45 and frame 60.
- **Landing inside the frame.** She comes down onto the rug and is fully visible, lying on her back, for the last ~1.5s. She settles and stays down.
- **Santa stays taped.** Present on the ceiling in every frame, including the last.
- **Audio present.** 128 audio frames.

**Two flags, not fixed - Daniel decides**

1. **The camera pulls back.** The clip does not cut, but it widens steadily from start to finish: frame 0 is a tight framing on her and the ladder, frame 96 shows most of the room - the fireplace, the sofa, the coffee table and a wide floor. Landmark matching against the static architecture fails to converge at unity scale, which is consistent with a real change of framing rather than hand sway. Daniel's brief said **no zooms**, and the prompt bans zoom, push-in and reframing in two separate places, so prose is not holding it here. v5 g2 did not do this on its own start frame.
2. **The ladder disappears.** It is present and falling at frame 60, and gone by frame 96 - it is not lying on the rug at the end. The prompt line *"The ladder goes over with her and clatters onto the rug"* is not being honoured through to the last frame.

Both are prompt-side, not frame-side, so per `feedback_fix_the_prompt_not_the_frame` the fix is a surgical edit re-rolled on the same `v6_c01_g4.png`, not a new still. Not attempted - one generation, then review.

---

## C02 - Hands on the box

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW
*What it is:* two hands resting on the closed carton on the polished mahogany table, the beat before it opens.

- frames: `v6_c02_g1.png` (current)
- clips: `v6_c02_g1.mp4` (current)

*Reused from* v3 C02 - changed: (a) the sleeve, dark green wool -> deep plum wool; (b) `SECOND - THE TABLE`, creamy white painted farmhouse -> deep mahogany, French-polished; (c) `THIRD - THE BACKGROUND`, classic American Christmas living room -> dark traditional American drawing room with the black-green panelling, the white marble fireplace with its brass fender and the brass picture light; (d) the table dressing baubles, gold and red -> antique gold and cream. The carton description, the hands clause, the quality tail and the wordmark spelling clause are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c02_g1.png` | owns the geometry - camera position, top-down-ish angle, distance, the table plane, the hands' position and grip, the box's position, scale and angle |
| @Image 2 | `../../product_images/box_festive_green_g2.png` | owns the carton artwork |

media ids `1cdfcc53-e771-4bba-9eab-b1788346098b`, `2597b25d-60d1-4060-9602-32b0ee26c2f7`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `d4bf54ca-487c-4f02-92b5-b0778a68c74b`

```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep plum wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a deep mahogany dining table top: a rich dark red-brown timber with fine ribbon-stripe figure running through it, French-polished to a deep glassy sheen that holds soft warm reflections, with a moulded edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused dark traditional American Christmas drawing room: walls fully panelled in deep black-green painted joinery, a white marble fireplace with a polished brass fender and cream knitted stockings hanging from the mantel, a decorated Christmas tree with warm white fairy lights and antique gold and cream ornaments standing off to one side, a brass picture light glowing over a dark gilt-framed painting, all well out of focus so the box stays the clear subject.

Dress the mahogany table more festively: a sprig of fir and a few red berries, two or three small antique gold and cream baubles, a short cream candle, a soft warm string light trailing across the polished mahogany, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.
```

*Flag, not fixed:* watch the red band - in earlier rounds the wordmark has printed twice.

### Video prompt - `clips/v6_c02_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c02_g1.png` - Higgsfield media `6b40ce6f-718f-44b5-86ec-5b44a1bb44b0` (media_input)
**Extra references** - `video reference` `1d2e8a8d-1e49-422a-8b04-d1a1230096a4` (video_input)
**Job** - `7be8c6ed-38e3-4f07-b126-12e2a930dda9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_223516_7be8c6ed-38e3-4f07-b126-12e2a930dda9.mp4

**Note on the start image** - the media attached to this job is `6b40ce6f-718f-44b5-86ec-5b44a1bb44b0`, a re-uploaded copy (`media_input`), not the original image job `d4bf54ca-487c-4f02-92b5-b0778a68c74b` that the C02 frame was generated under. The prompt's own text says the two-handed lift "is the thing the last take got wrong", so an earlier C02 take exists outside the 2026-09-19 21:44-24:00 window that was scanned; it is not recorded here.

```
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a French-polished deep mahogany dining table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a deep plum wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a French-polished deep mahogany dining table fills the frame. A lit cream pillar candle sits at the left, fir sprigs with red berries and small antique gold and cream baubles beside it, a white marble fireplace with a polished brass fender, hanging cream knitted stockings and deep black-green panelled walls, and a decorated Christmas tree with warm white lights and antique gold and cream ornaments softly out of focus behind. The candle, the fir, the berries, the baubles, the defocused fireplace and the defocused tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the French-polished deep mahogany dining table, lid flaps folded back, with the candle, the fir, the berries, the defocused fireplace and the defocused tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
```

---

## C03 - The product lifted

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW
*What it is:* two hands hold the projector up in the air just above the cream limestone counter.

- frames: `v6_c03_g1.png` (current)
- clips: `v6_c03_g1.mp4` (current)

*Reused from* v3 C03 - changed: (a) `THE HANDS`, the sleeve only -> deep plum wool; (b) `THE COUNTER`, the material -> honed cream limestone; (c) `THE KITCHEN` -> dark traditional American Christmas kitchen. The camera block, the `THE COUNTERTOP MUST BE IN FRAME` block, `THE POSE`, `SCALE AND PLACEMENT`, `THE PRODUCT` and the quality tail are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c03_g1.png` | owns the geometry and the look - camera position and height, the lens, the distance, the pose and grip, the product's size, position and tilt, where each forearm enters, the counter wedge in the lower right |

media id `7ccdd557-bfee-45b0-a067-0652320f537b`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `e3d2f546-11bb-4ccc-ba70-288d93b2c8eb`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a deep plum wool sweater sleeve pushed back; right forearm enters from the right in the same deep plum sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed cream limestone counter: a soft warm off-white stone with gentle caramel veining drifting through it and fine darker fossil flecks scattered across the surface, a chunky bullnosed edge, a completely matte surface with no shine at all. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A dark traditional American Christmas kitchen, softly defocused: inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream tumbled-marble backsplash with soft uneven edges, a cream enamel range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

*Flag, not fixed:* the dome has come out squat in earlier rounds - check the proportions against the product shots.

### Video prompt - `clips/v6_c03_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c03_g1.png` - Higgsfield media `e3d2f546-11bb-4ccc-ba70-288d93b2c8eb` (image_job)
**Extra references** - none
**Job** - `0f3cf04e-54db-494c-bec6-10d00f0ab15c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215208_0f3cf04e-54db-494c-bec6-10d00f0ab15c.mp4

```
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a honed cream limestone kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in deep plum wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a honed cream limestone countertop fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream enamel range built into the tall cabinet run on the left, a cream tumbled-marble backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the limestone counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The limestone is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
```

---

## C04 - Plugging it in

*Section:* B-roll 1 - the unbox
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW
*What it is:* the projector stands on the counter, her right hand pushing a USB-C connector toward the port on the stand.

- frames: `v6_c04_g1.png` (current)
- clips: `v6_c04_g1.mp4` (current)

*Reused from* v3 C04 - changed: (a) `THE HANDS`, the sleeve only -> deep plum wool; (b) `THE COUNTER`, the material -> honed cream limestone; (c) `THE KITCHEN` -> dark traditional American Christmas kitchen with the range on the right. The `CAMERA` block with its four DO NOTs, `THE PRODUCT`, the connector-and-port sentences and the quality tail are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c04_g1.png` | owns the geometry and the look - the low close camera just above counter level, the shallow downward tilt, the product's size and placement, both hands' positions and actions, the cable running off to the right |

media id `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `339a1286-5b1c-4461-89d7-41c52a4722c8`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep plum wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed cream limestone counter: a soft warm off-white stone with gentle caramel veining drifting through it and fine darker fossil flecks scattered across the surface, a chunky bullnosed edge, a completely matte surface with no shine at all. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A dark traditional American Christmas kitchen, softly defocused across the top third of the frame: inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream tumbled-marble backsplash with soft uneven edges, a cream enamel range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
```

*Flag, not fixed:* same squat-dome risk as C03.

### Video prompt - `clips/v6_c04_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c04_g1.png` - Higgsfield media `339a1286-5b1c-4461-89d7-41c52a4722c8` (image_job)
**Extra references** - none
**Job** - `74b8404c-8310-458a-acd0-040368826711`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215209_74b8404c-8310-458a-acd0-040368826711.mp4

```
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand pushes a white cable into the projector's base and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a deep plum wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same deep plum sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a honed cream limestone countertop fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream enamel range built into the tall cabinet run on the right, a cream tumbled-marble backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the limestone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
```

---

## C05 - The door opens on the room

*Section:* B-roll 2 - the payoff
*Status:* BOTH FRAMES GENERATED · FRAME 2 RE-ROLLED ON A REAL-HOUSE REFERENCE - TAKE 2 FOR REVIEW
*What it is:* one clip, two frames. Her hand on the closed oxblood door, then a real double-height room already buried in the projection.

- frames: `v6_c05_g1.png` (frame 1), `v6_c05_r2.png` (frame 2, current, in `references/`) · `v6_c05_r1.png` (frame 2, take 1, superseded)
- clips: `v6_c05_g1.mp4` .. `v6_c05_g5.mp4` (five takes, g5 picked)

### FRAME 1 - hand on the closed door

*Reused from* v3 C05 frame 1 - changed: the door only. Navy five-panel with brass knob and cream frame -> four-panel deep oxblood red in eggshell with an antique brass knob and a matching antique brass escutcheon in a plain painted cream frame, and the two exposure sentences follow the new colour ("the oxblood paint reads clearly as a deep red rather than black", "the brass knob catches a warm highlight"). The `KEEP IDENTICAL` list, `CHANGE 2` (the no-light-at-the-edge block), `THE WREATH`, `SHARPNESS` and the quality tail are byte-identical to v3.

**Why `CHANGE 2` is worded the way it is.** Daniel rejected the v3 C05 frame for a glittering sparkler at the door edge: *"when the person it's oppening the door the animation must already be on the walls and ceiling, not to appear at that time."* The frame-1 door must be dead sealed so the reveal lands entirely in the cut to frame 2. That block is not to be softened.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c05_g2.png` | owns the geometry and the look - hallway, camera position and height, the knob position, the forearm entering from the lower right, the warm low-key evening light |

media id `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `e393a7c9-e564-4e4d-a55c-bf19b637848e`

```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American four-panel door painted a deep oxblood red in a soft eggshell finish: crisp raised mouldings around four flat recessed panels, clean painted surfaces with the faintest brush texture, an antique brass knob and a matching antique brass escutcheon plate, set in a plain painted cream frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the oxblood paint reads clearly as a deep red rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### FRAME 2 - the room behind the door

*Reused from* v3 C05 frame 2 - changed: `CHANGE 1 - THE ROOM` (the whole room swapped to the dark traditional look pack), the knitwear inside the `KEEP IDENTICAL` paragraph, the surfaces named inside the physics block (dark stained boards with cream-painted rafters and the black marble fireplace in place of v3's surfaces), the projection signature, the escalation clause, and the floor materials listed in `CHANGE 3`. The two children's poses, `CHANGE 2`'s layer order, the whole physics block, `CHANGE 4` and the quality tail are byte-identical to v3.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/references/v1_c05_r1.png` | owns the geometry and the look - the wide framing of a whole tall room seen from a doorway, camera position and height, the magical low-key light in which the projection is the only light, the two children's poses |

media id `f3a8c329-4152-4a22-9469-d89578812e09`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `53080c12-ace7-44bf-90b7-1cca5268e592`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. A dark traditional American family room: deep forest green painted walls with cream painted panelling to waist height and cream trim, a high vaulted ceiling clad in dark stained tongue-and-groove boards with exposed cream-painted rafters rising to a dark stained ridge beam, a full-height black marble fireplace on the right with a low fire burning behind a polished brass fender and a carved cream mantel with cream knitted stockings hanging from it, a deep oxblood red chesterfield sofa with antique gold cushions and a cream cable-knit throw, a faded antique Persian rug over dark stained oak floorboards, a tall real Christmas tree in the left corner with warm white lights and antique gold and cream ornaments, wrapped gifts under it, and a tall cream-trimmed sash window behind the tree showing a dark blue snow-covered night outside.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every painted wall, the whole vaulted boarded ceiling and its cream rafters and ridge beam, and the black marble of the fireplace, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the wall beside the fireplace; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the deep green paint and the dark boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the dark stained boards, their seams and their subtle grain, and every cream-painted rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The dark oak floorboards, the Persian rug, the oxblood sofa, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

*Note:* this frame carried the face-readability wording and the `perfectly exposed with both children's faces clearly readable` tail and passed on the first submission - as did C06 in this same video. Only C07 needed edits. See the refusal log.

### FRAME 2 - TAKE 2, the real-house architecture

*Reused from* v6 C05 frame 2 take 1 - changed: (a) the whole `CHANGE 1 - THE ROOM` paragraph, replaced by the architecture of `house_great_room_trusses.png` read off the photograph, plus a second paragraph naming the only two departures from it - night, and Christmas dressing; (b) a role sentence appended to the opening paragraph that splits authority between the two references; (c) the surface names inside `CHANGE 2` and its physics block, which had to follow the new room or the prompt contradicts itself - this ceiling is a plastered cathedral vault crossed by pairs of dark walnut rafters with collar beams, not a boarded vault with cream rafters and a ridge beam, so `run with the direction of the boards` -> `run with the direction of the rafters`, the moon -> `high on the plaster wall above the gallery landing`, the palette surfaces -> `the pale plaster and the dark walnut rafters`, the physics block's materials -> plaster and timber, the closing ceiling assertion -> `a real plastered cathedral vault with dark walnut rafter pairs and their collar beams crossing it`, and the no-floor list -> the warm oak boards, the greige rug, the grey sectional and the round coffee table.

The projection's layer list is unchanged - the village, the carol singers and lantern carriers, the aurora, the sleigh and reindeer, the moon, the north star, the star field, the snowflakes, the bunting, the candy canes, the musical notes and the ice crystals are all byte-identical, as are the `KEEP IDENTICAL` list, the two poses, the knitwear paragraph, the palette statement and its cold-colour ban, the not-outer-space ban, the no-projector clause and the quality and no-text tails. Only surfaces were renamed. Nine replacements, each applied with a single-match assert, so the untouched text is verified identical rather than asserted.

*Why:* the model was inventing the architecture, and the ceilings came out wrong. A photograph of a real room now owns the geometry.

*Which house, and why this one.* `house_great_room_trusses.png` was already spent on v4 C07 - but that is a **wide** shot from the middle of the room and this is a **doorway** shot, so the same architecture reads as a different picture. It is also the same house used for C07 below, deliberately: video 6's door-opening shot and its big-room shot are then one home, which is what *"things make sense"* asks for.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/references/v1_c05_r1.png` | camera, framing, the two poses and the light - unchanged from take 1 |
| @Image 2 | `../../references/house_great_room_trusses.png` | **the architecture, and nothing else** - the plastered cathedral vault, the dark walnut rafter pairs and their collar beams, the gallery landing, the stair, the tall windows, the proportions |

media ids `f3a8c329-4152-4a22-9469-d89578812e09` · `1d79cde5-c6a5-4259-b414-2b0d4bd8434b`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `b6fb9884-52a1-4556-bb00-59aa6deb8f7d`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: an enormous double-height great room whose ceiling is a cathedral vault of smooth cream plaster in two long slopes meeting at a ridge that runs away from the camera, crossed by two pairs of dark walnut-stained timber rafters, each pair rising as an inverted V to meet at the ridge with a matching collar beam below it, and small recessed downlights set flush into the plaster between them; a first-floor gallery landing crossing the right-hand half of the room at mid height, its railing made of clear glass panels held in slim black metal posts under a dark timber top rail; an open-tread pale oak staircase descending from that landing towards the camera with the same glass-and-black-post railing and black wall sconces on the wall beside it; a tall arched window with dark muntins set high on the right above the stair; a pale plaster back wall at the centre carrying a black arched double glazed door of many small panes; and along the left an open kitchen with pale oak slab cabinetry, a full-height integrated cabinet run, a cream island with a stone waterfall front, four woven rattan counter stools and two big woven rattan dome pendants hanging on long black cords. Wide warm oak plank floor, a large pale grey sectional sofa wrapping the right foreground, a round dark-stained wood coffee table and a large greige rug. Copy the proportions, the rafter pairs, the ridge, the glass railing, the stair and the arched door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the arched window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every downlight, pendant and sconce in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing against the pale plaster back wall beside the arched door with warm white lights and antique gold and cream ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and antique gold ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a large evergreen wreath with a cream bow on the arched door. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every plaster wall, the whole high vaulted plaster ceiling, the dark walnut rafters and their collar beams, and the underside and railing of the gallery landing, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the plaster wall above the gallery landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the dark walnut rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, and every dark walnut rafter, every collar beam and the ridge line of the vault, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the collar beams break the light with their own hard shadow lines where they stand proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real plastered cathedral vault with dark walnut rafter pairs and their collar beams crossing it, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The warm oak floorboards, the greige rug, the grey sectional sofa, the round coffee table, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt - `clips/v6_c05_g1.mp4` (take 1)

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c05_g1.png` - Higgsfield media `e393a7c9-e564-4e4d-a55c-bf19b637848e` (image_job)
**Extra references** - `image reference` `b6fb9884-52a1-4556-bb00-59aa6deb8f7d` (image_job); `video reference` `c5b72684-3884-4e7d-8b77-7bad9f4af4cf` (video_input)
**Job** - `008b3706-79f9-4944-89d3-ea62886d03da`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215719_008b3706-79f9-4944-89d3-ea62886d03da.mp4

```
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

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the oxblood red door, the brass of the round knob and its escutcheon, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed oxblood red four-panel door in its cream frame, the brass round knob on its brass escutcheon, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow hanging on the door.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree against the pale plaster back wall at the centre, the pale grey sectional sofa wrapping the right foreground, the gallery landing with its glass-panelled garlanded railing on the right, the high vaulted plaster ceiling on its dark walnut rafters, the two children and their deep plum and oatmeal cable-knit knitwear, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - deep plum and oatmeal cable-knit Christmas jumper with soft grey knitted lounge trousers, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching deep plum and oatmeal cable-knit knitwear, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - an enormous American great room with a high vaulted cream plaster ceiling on dark walnut rafters and their collar beams: tall decorated Christmas tree against the pale plaster back wall at the centre, pale grey sectional sofa wrapping the right foreground, gallery landing with a glass-panelled garlanded railing crossing the right at mid height, tall arched window high on the right, warm oak plank floor with a large greige rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, the hallway lit only by its own warm dim light, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door swings away from the camera and the room behind it comes into view. The projection is ALREADY running at full strength on the far wall and across the whole ceiling before the door moves - the widening doorway simply uncovers more of a display that was already there, the way drawing a curtain back uncovers a view. Nothing lights up, ignites, spreads, ripples or switches on as the door opens, and nothing glows along the edge of the door, along the door frame or in the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light is sweeping across the far wall and the tree and raining down over the floor ahead and over the camera's own path, at exactly the same speed and the same brightness it already had before the door opened.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the field of light keeps sliding and pouring down every wall and across both children, shapes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The light is sweeping and pouring across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the moving projection as the only bright light source. Because the shapes are sweeping and pouring, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Knitwear and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the projection is already running at full strength on the walls and across the whole ceiling in the very first frame in which any part of the room is visible, and its brightness never changes from that moment on; the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a glittering sparkler, a strip of fairy lights, a glowing seam, a bright vertical line, a shaft or any other light effect along the edge of the door, along the door frame or in the door gap; light that grows, spreads, ignites, switches on or fills the room as the door opens; a projection that is dim or absent when the door starts to move and gets stronger afterwards; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
```

### Video prompt - `clips/v6_c05_g2.mp4` (take 2)

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c05_g1.png` - Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4` (media_input)
**Extra references** - `image reference` `c4fc3193-2325-46da-a3a7-0f0cc422be64` (media_input); `video reference` `c5b72684-3884-4e7d-8b77-7bad9f4af4cf` (video_input)
**Job** - `07783067-8c19-4bf0-b4e1-26ffc370823b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_223429_07783067-8c19-4bf0-b4e1-26ffc370823b.mp4

**Note on the start images** - takes 2-5 attach re-uploaded copies (`media_input` `d58a1298-e600-423c-bb27-186c3ceac1a4` for the door and `c4fc3193-2325-46da-a3a7-0f0cc422be64` for the room) rather than the original image jobs, so these four were matched to the shot on prompt content, not on media UUID.

```
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

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the oxblood red door, the brass of the round knob and its escutcheon, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed oxblood red four-panel door in its cream frame, the brass round knob on its brass escutcheon, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow hanging on the door.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree against the pale plaster back wall at the centre, the pale grey sectional sofa wrapping the right foreground, the gallery landing with its glass-panelled garlanded railing on the right, the high vaulted plaster ceiling on its dark walnut rafters, the two children and their deep plum and oatmeal cable-knit knitwear, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - deep plum and oatmeal cable-knit Christmas jumper with soft grey knitted lounge trousers, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching deep plum and oatmeal cable-knit knitwear, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - an enormous American great room with a high vaulted cream plaster ceiling on dark walnut rafters and their collar beams: tall decorated Christmas tree against the pale plaster back wall at the centre, pale grey sectional sofa wrapping the right foreground, gallery landing with a glass-panelled garlanded railing crossing the right at mid height, tall arched window high on the right, warm oak plank floor with a large greige rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, the hallway lit only by its own warm dim light, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door swings away from the camera and the room behind it comes into view. The projection is ALREADY running at full strength on the far wall and across the whole ceiling before the door moves - the widening doorway simply uncovers more of a display that was already there, the way drawing a curtain back uncovers a view. Nothing lights up, ignites, spreads, ripples or switches on as the door opens, and nothing glows along the edge of the door, along the door frame or in the gap.
1.0-2.0s - the door swings inward and wide; the camera steps forward through the doorway. Light is sweeping across the far wall and the tree and raining down over the floor ahead and over the camera's own path, at exactly the same speed and the same brightness it already had before the door opened.
2.0-3.0s - the camera is fully inside the room. THE BOY is already running across the middle of the room, arms out, mouth wide open laughing, and leaps onto the sofa cushion. THE GIRL spins on the rug behind him to the left, hair flying, laughing and shouting. Behind and around them the field of light keeps sliding and pouring down every wall and across both children, shapes visibly travelling from the top of frame towards the bottom.
3.0-4.0s - the camera keeps moving forward and TILTS UP, bringing the ceiling into the top of frame. The light is sweeping and pouring across the entire ceiling too, streaming towards the far end of the room. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

[8] CAMERA AND OPTICS - one continuous handheld POV walk, vertical 9:16, normal wide-angle phone lens, eye height. Two movements only: the forward walk from 1.0s and the upward tilt from 3.0s. No cut, no zoom, no orbit. Normal wide-angle only - no fisheye, no barrel distortion, no curved walls. The camera IS the person's eyes: no phone, screen, hand, fingers, thumb or device in the lower part of frame after 1.0s.

[9] LIGHTING - the hallway is warm and dim; the room is dim with the moving projection as the only bright light source. Because the shapes are sweeping and pouring, the bright and dark areas on the walls, the furniture and the children change continuously. Do not flood the room with one flat colour.

[10] PHYSICS - the door swings on its hinges, never lifted off or removed. The sofa cushion compresses when THE BOY lands. Knitwear and hair swing and lift with their motion.

[11] AUDIO - DRY DOCUMENTARY AUDIO ONLY. Exactly three things and nothing else: the door handle and the door swinging, children laughing and squealing, and quiet room tone. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS.

[12] POSITIVE LOCKS - the projection is already running at full strength on the walls and across the whole ceiling in the very first frame in which any part of the room is visible, and its brightness never changes from that moment on; the light is visibly sweeping and pouring in every single frame, on the walls and on the ceiling; a viewer can follow individual shapes travelling across and down. Both children are in full motion from the moment they appear. The projection shows CHRISTMAS imagery only. Every element inside the picture is visibly travelling in every single frame - the chimneys smoke, the aurora ripples, the sleigh and reindeer fly across the ceiling, the flakes pour down, the stars twinkle - while the picture's outer boundary holds still. The walls and the ceiling always move together. The picture is sharp.
BANNED: a projected pattern that stays in the same place; a static or frozen projected pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that only twinkle without travelling; a still ceiling above a moving wall; a quiet or empty ceiling when the camera tilts up; the whole picture rotating, spinning, sweeping or sliding across the room as one sheet; shapes that only brighten, twinkle, pulse or fade without travelling; a projection that appears to move only because the camera moves; a glittering sparkler, a strip of fairy lights, a glowing seam, a bright vertical line, a shaft or any other light effect along the edge of the door, along the door frame or in the door gap; light that grows, spreads, ignites, switches on or fills the room as the door opens; a projection that is dim or absent when the door starts to move and gets stronger afterwards; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; any music, any song, any score, any soundtrack; blur or soft focus; children standing still, posed or frozen; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible anywhere in frame; a third child; an adult; a cut; subtitles; on-screen text.
```

### Video prompt - `clips/v6_c05_g3.mp4` (take 3)

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c05_g1.png` - Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4` (media_input)
**Extra references** - `image reference` `c4fc3193-2325-46da-a3a7-0f0cc422be64` (media_input); `video reference` `c5b72684-3884-4e7d-8b77-7bad9f4af4cf` (video_input)
**Job** - `eb523fc7-abd5-4559-b0ec-8170814708aa`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_225058_eb523fc7-abd5-4559-b0ec-8170814708aa.mp4

```
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s.

THE ONLY THING THIS CLIP IS FOR
The Christmas picture thrown onto the walls and the ceiling is a MOVING PICTURE. Six previous attempts failed for one reason and one reason only: the picture sat still on the plaster like printed wallpaper and drifted across the screen only because the camera was walking. That is the failure. Do not repeat it.

THE TEST THIS CLIP MUST PASS
Freeze any two frames half a second apart and line the wall up. Every shape must be somewhere different ON THE PLASTER:
- Follow one snowflake. In one second it falls a quarter of the wall's height and lands somewhere else entirely.
- Follow the sleigh and reindeer. They gallop clean across the ceiling during the clip and finish nowhere near where they started.
- Follow one chimney. A plume of smoke leaves the pot, climbs a roof-height, spreads and fades, and a fresh one starts behind it.
- Follow one aurora ribbon. A bright swell runs along its length end to end, the way a wave runs down a shaken rope.
If the shapes sit in the same spots on the wall, the clip is worthless no matter how good everything else looks.

WHAT HOLDS STILL: the room. The plaster, the rafters, the door, the floor, the furniture, the tree, the framing, the colours. The picture's outer edge stays put too - it never rotates, spins, swings or slides across the room as one sheet. Only the things INSIDE the picture travel. The moon is the single exception: it holds its place and only breathes brighter and dimmer.

@Video 1 is real footage of this projector running. Copy ONE thing from it: how restlessly its light moves. Take nothing else - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. It is completely silent; import no sound from it.
@Image 1 controls only what the room LOOKS like once the door is open - the layout, the tree, the sofa, the gallery landing, the vaulted ceiling, the two children, and the colour and style of the Christmas shapes. It is a photograph. Copy its look, never its stillness.

BEATS

0.0-1.0s - The right hand grips the brass knob, turns it, and pushes the door away from camera. The room behind it is ALREADY full of moving light before the door shifts - flakes pouring down the far wall, an aurora rippling, the sleigh already crossing the ceiling. The widening doorway simply uncovers more of a display that was already running, the way pulling a curtain back uncovers a view. Nothing ignites, spreads, switches on or grows as the door opens. Nothing glows along the door edge, the frame or the gap.

1.0-2.0s - The door swings wide and the camera walks through it. The flakes keep falling at exactly the rate they already had, over the far wall, over the floor ahead, over the camera's own path.

2.0-3.5s - Inside the room. THE BOY is already running across the middle, arms out, mouth open laughing, and he leaps onto the sofa cushion. THE GIRL spins on the rug behind him and to his left, hair flying. Shapes travel down the walls behind them and slide across their backs and faces as they move.

3.5-5.0s - The camera keeps walking forward and TILTS UP until the vaulted ceiling fills the top of frame. The ceiling is the BUSIEST surface in the whole clip, never the calmest: the aurora ripples along the rafters end to end, the sleigh and reindeer gallop across it, snow pours down it, the stars twinkle. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the forward walk from 1.0s, the tilt up from 3.5s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera IS the person's eyes - no phone, screen, hand or device in frame after 1.0s.

THE CHILDREN - exactly two, no adults, no third child, no pets. Deep plum and oatmeal cable-knit knitwear. They are in full motion the instant they appear and never stand still, never pose, never freeze - a clearly different whole-body pose every half second.

SHARPNESS - hold the exact sharpness, exposure and fine detail of the start image: the floor's wood grain, the panel edges and sheen of the oxblood red door, the brass knob, the skin texture of the bare forearm, the leaves of the wreath. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle and the door swinging, children laughing and squealing, quiet room tone. NO music, no song, no score, no soundtrack, no instruments, no bells used as music.

BANNED - a projected shape that stays in the same place on the plaster; a projection that appears to move only because the camera moves; shapes that only twinkle, pulse, brighten or fade without travelling; a parked sleigh; chimneys not smoking; a still aurora; a still or empty ceiling when the camera tilts up; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam, bright line or sparkler along the door edge, frame or gap; light that grows, ignites or fills the room as the door opens; any music; blur or soft focus; children standing still or posed; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
```

### Video prompt - `clips/v6_c05_g4.mp4` (take 4)

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c05_g1.png` - Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4` (media_input)
**Extra references** - `image reference` `c4fc3193-2325-46da-a3a7-0f0cc422be64` (media_input)
**Job** - `4aaaa8fa-d202-48c9-90f6-67a4ff2c5066`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_230812_4aaaa8fa-d202-48c9-90f6-67a4ff2c5066.mp4

```
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s: a closed oxblood red door with a wreath, a hand on the brass knob.

THE PICTURE ON THE WALLS IS A CLOSED SET
The start image does not show the room, so read the room ONLY from @Image 1. Everything thrown onto the walls and ceiling is already drawn in @Image 1. You are not designing a projection - you are making the one in @Image 1 move. Invent nothing. If a thing is not in the list below, it does not exist in this clip.

THE COMPLETE LIST OF WHAT IS PROJECTED, AND WHAT EACH ONE DOES

Moving layer - these travel across the plaster:
- Six-point snowflakes, white and pale gold. They fall steadily and continuously down the ceiling and down both walls, top to bottom, new ones entering above as others slide out below. They never hang still.
- Candy canes, red and white striped. They drift down with the snow, tumbling slowly end over end as they go.
- Shooting stars, gold with a tail. They streak across, the tail thinning out behind them, and fade; fresh ones set off elsewhere.
- The aurora ribbons, green and pink and magenta, laid along and between the dark rafters. A bright swell runs the length of each ribbon end to end, the way a wave runs down a shaken rope, and the ribbons themselves creep sideways.
- The fine gold star specks filling the gaps. The whole field creeps slowly and the specks twinkle in and out.
- The gold line of musical notes on their staff, along the right-hand rafter. The notes travel along the staff like sheet music sliding past.
- The reindeer team and sleigh, gold, to the left of the moon. They gallop steadily across and finish a long way from where they set off.

Holding layer - these keep their exact positions and only twinkle:
- The moon, bright and full, centre right. It holds and only breathes brighter and dimmer.
- The church with the tall steeple, right of the moon. Holds; its windows twinkle.
- The snowy village houses low on the left wall. Hold; their lit windows twinkle.
- The big gold Christmas tree and the slimmer cone tree behind it on the left wall. Hold; their lights twinkle.
- The street lamps among the houses. Hold; they flicker faintly.

ADD NOTHING. No smoke and no chimney plumes of any kind. No extra buildings, no extra trees, no extra figures, no angels, no bells, no letters, no numbers, no new shapes. Nothing appears that is not on the list.

WHAT ELSE HOLDS: the real room. The plaster, the rafters, the staircase and its gallery landing, the door, the wooden floor, the rug, the sofa, the real Christmas tree and its lights, the framing, the colours. The projected picture's outer edge stays put - it never rotates, spins, swings or slides across the room as one sheet. Only the things inside it travel.

@Image 1 is the authority on the room and on every projected shape: its layout, its staircase, its furniture, its two children, and the exact set, style and colour of the projected shapes. It is a photograph - copy its look, never its stillness.

BEATS
0.0-0.8s - The hand turns the brass knob and pushes the door away from camera. Behind it the room is ALREADY running: snow already falling, the aurora already swelling, the reindeer already crossing. The widening gap simply uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on, spreads or grows as the door opens, and nothing glows along the door edge, frame or gap.
0.8-2.0s - The door swings wide and the camera walks through. The snow keeps falling at the same steady rate it already had - down the far wall, across the floor ahead, across the camera's own path.
2.0-3.3s - Inside. The two children are both already in motion and stay in motion. Projected shapes slide down the walls behind them and pass across their backs and faces.
3.3-5.0s - The camera keeps walking and TILTS UP until the rafters fill the top of frame. The ceiling is the busiest surface in the clip: snow pouring down it, the swell running along every aurora ribbon, the notes sliding along the staff, the reindeer crossing it, the specks twinkling.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the walk from 0.8s, the tilt up from 3.3s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes - no phone, screen, hand or device in frame after 0.8s.

THE CHILDREN - exactly two, both visible from 2.0s on, no adults, no third child, no pets. Deep plum and oatmeal cable-knit knitwear, as in @Image 1. They never stand still and never pose.

SHARPNESS - hold the sharpness, exposure and fine detail of the start image: the wood grain of the floor, the panel edges and sheen of the red door, the brass knob, the skin of the bare forearm, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, children laughing, quiet room tone. NO music, no song, no score, no instruments, no bells used as music.

BANNED - any projected shape that is not on the list above; smoke; a shape that stays in the same place on the plaster when the list says it travels; a projection that appears to move only because the camera moves; shapes that only twinkle when the list says they travel; a parked sleigh; a still aurora; a still or empty ceiling when the camera tilts up; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; any music; blur or soft focus; children standing still or posed; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
```

### Video prompt - `clips/v6_c05_g5.mp4` (take 5 - PICKED, the take that was upscaled)

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c05_g1.png` - Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4` (media_input)
**Extra references** - `image reference` `c4fc3193-2325-46da-a3a7-0f0cc422be64` (media_input)
**Job** - `dcb1778f-3a97-4fc7-a2e8-172f977af6b6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_231602_dcb1778f-3a97-4fc7-a2e8-172f977af6b6.mp4

```
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s: a closed oxblood red door with a wreath, a hand on the brass knob.

THE PICTURE ON THE WALLS IS A CLOSED SET
The start image does not show the room, so read the room ONLY from @Image 1. Everything thrown onto the walls and ceiling is already drawn in @Image 1. You are not designing a projection - you are making the one in @Image 1 move. Invent nothing. If a thing is not in the list below, it does not exist in this clip.

THE COMPLETE LIST OF WHAT IS PROJECTED, AND WHAT EACH ONE DOES

Moving layer - these travel across the plaster:
- Six-point snowflakes, white and pale gold. They fall steadily and continuously, top to bottom, new ones entering above as others slide out below. They never hang still. They are FLAT LIGHT LYING ON THE PLASTER and they never leave it: a flake slides down the face of the ceiling or the face of a wall and stays welded to that surface for its whole journey. It is a stain of light on a solid surface, not a falling object. There is no snow in the air of the room, none between the camera and the walls, none in front of the children, the sofa, the staircase or the tree, and none landing on the floor or on anyone.
- Candy canes, red and white striped. They drift down with the snow, tumbling slowly end over end as they go.
- Shooting stars, gold with a tail. They streak across, the tail thinning out behind them, and fade; fresh ones set off elsewhere.
- The aurora ribbons, green and pink and magenta, laid along and between the dark rafters. A bright swell runs the length of each ribbon end to end, the way a wave runs down a shaken rope, and the ribbons themselves creep sideways.
- The fine gold star specks filling the gaps. The whole field creeps slowly and the specks twinkle in and out.
- The gold line of musical notes on their staff, along the right-hand rafter. The notes travel along the staff like sheet music sliding past.
- The reindeer team and sleigh, gold, to the left of the moon. They gallop steadily across and finish a long way from where they set off.

Holding layer - these keep their exact positions and only twinkle:
- The moon, bright and full, centre right. It holds and only breathes brighter and dimmer.
- The church with the tall steeple, right of the moon. Holds; its windows twinkle.
- The snowy village houses low on the left wall. Hold; their lit windows twinkle.
- The big gold Christmas tree and the slimmer cone tree behind it on the left wall. Hold; their lights twinkle.
- The street lamps among the houses. Hold; they flicker faintly.

ADD NOTHING. No smoke and no chimney plumes of any kind. No extra buildings, no extra trees, no extra figures, no angels, no bells, no letters, no numbers, no new shapes. Nothing appears that is not on the list.

EVERY PROJECTED SHAPE IS PAINT, NOT AN OBJECT. All of it is flat light lying on whatever surface it lands on. It skews and stretches with the slope of that surface, it bends over the rafters, it breaks where a wall meets the ceiling. Nothing ever floats free of a surface into the air of the room.

WHAT ELSE HOLDS: the real room. The plaster, the rafters, the staircase and its gallery landing, the door, the wooden floor, the rug, the sofa, the real Christmas tree and its lights, the framing, the colours. The projected picture's outer edge stays put - it never rotates, spins, swings or slides across the room as one sheet. Only the things inside it travel.

@Image 1 is the authority on the room and on every projected shape: its layout, its staircase, its furniture, its two children, and the exact set, style and colour of the projected shapes. It is a photograph - copy its look, never its stillness.

BEATS
0.0-0.8s - The hand turns the brass knob and pushes the door away from camera. Behind it the room is ALREADY running: snow already falling, the aurora already swelling, the reindeer already crossing. The widening gap simply uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on, spreads or grows as the door opens, and nothing glows along the door edge, frame or gap.
0.8-2.0s - The door swings wide and the camera walks through. The snow keeps falling at the same steady rate it already had, down the face of the far wall. It stays on that wall - it does not cross the open air of the room and it does not drift toward the camera.
2.0-3.3s - Inside. The two children are both already in motion and stay in motion. Projected shapes slide down the walls behind them and pass across their backs and faces.
3.3-5.0s - The camera keeps walking and TILTS UP until the rafters fill the top of frame. The ceiling is the busiest surface in the clip: snow pouring down it, the swell running along every aurora ribbon, the notes sliding along the staff, the reindeer crossing it, the specks twinkling.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the walk from 0.8s, the tilt up from 3.3s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes - no phone, screen, hand or device in frame after 0.8s.

THE CHILDREN - exactly two, both visible from 2.0s on, no adults, no third child, no pets. Deep plum and oatmeal cable-knit knitwear, as in @Image 1. They never stand still and never pose.

SHARPNESS - hold the sharpness, exposure and fine detail of the start image: the wood grain of the floor, the panel edges and sheen of the red door, the brass knob, the skin of the bare forearm, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, children laughing, quiet room tone. NO music, no song, no score, no instruments, no bells used as music.

BANNED - snow, snowflakes or any particles falling through the open air of the room; volumetric or three-dimensional snow; anything drifting between the camera and the walls; snow passing in front of the children, the sofa, the staircase, the rug or the real tree; snow settling on the floor, the furniture or anyone's hair or shoulders; any projected shape that appears to leave the surface it is painted on; any projected shape that is not on the list above; smoke; a shape that stays in the same place on the plaster when the list says it travels; a projection that appears to move only because the camera moves; shapes that only twinkle when the list says they travel; a parked sleigh; a still aurora; a still or empty ceiling when the camera tilts up; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; any music; blur or soft focus; children standing still or posed; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
```

---

## C06 - The bed bounce

*Section:* B-roll 2 - the payoff
*Status:* RE-ROLLED ON A REAL-HOUSE REFERENCE - TAKE 2 FOR REVIEW (take 1 passed on the first submission, unedited)
*What it is:* a boy of about six standing on top of the bed mid-bounce under a projected attic sky.

- frames: `v6_c06_g2.png` (current) · `v6_c06_g1.png` (take 1, superseded)
- clips: `v6_c06_g1.mp4` (current)

*Reused from* v3 C06 - changed: (a) the child, a boy of about eight with short dark curly hair -> a boy of about six with short straight black hair; (b) the knitwear; (c) the room, grey-blue boards and a white bed -> warm oatmeal painted tongue-and-groove slopes with dark stained rafters, deep green knee-wall panelling, an antique brass bed with a red tartan quilt and a low dark green bookshelf; (d) the surfaces named inside the physics block; (e) the projection signature and the escalation clause. The bounce-pose sentence, the camera block, the whole `CHANGE 3` projection layer order, the physics block and `CHANGE 5` are byte-identical.

**No moderation edits.** This is the only C06 of the three videos that cleared on the first submission. It still carries the unedited `The boy's face and his knitted jumper catch that spill so his face reads clearly.` in `CHANGE 4` and the unedited `perfectly exposed with the boy's face clearly readable` tail - the exact two clauses that had to be rewritten in v4 and v5. See the refusal log.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c06_g1.png` | owns the geometry and the look - camera position and height, the framing that carries both the wall behind the bed and the ceiling above it, the low-key light where the projection is the only light |

media id `0a845da6-2607-46cc-a595-4fee4b17d6a9`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `abdf9332-5e41-4966-9b60-cbf747f02be3`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with short straight black hair, fully dressed for winter in a warm deep plum and oatmeal cable-knit Christmas jumper with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. A classic American child's bedroom tucked under the roof: a low sloped ceiling on both sides clad in warm oatmeal painted tongue-and-groove boards with dark stained exposed rafters running up to a dark stained ridge beam, deep green painted panelling on the knee wall below, a small cream-trimmed dormer window with a dark snowy night outside and a warm fairy-light garland around it, a low antique brass bed set against the knee wall made up with a red tartan quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking pinned to the rafter above the headboard, a small lit Christmas tree standing on the floor beside the bed, a faded antique Persian runner on dark stained oak floorboards, and a low dark green bookshelf of picture books tucked under the slope.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both painted sloped ceiling planes and the dark rafters, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the dormer window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the painted boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the painted boards, their seams and their subtle grain, and every dark stained rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The dark oak floorboards, the Persian runner, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with the boy's face clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### TAKE 2 - the real-house architecture

*Reused from* v6 C06 take 1 - changed: (a) the whole `CHANGE 2 - THE ROOM` paragraph, replaced by the architecture of `house_bedroom_attic.png` read off the photograph, plus a second paragraph naming the only two departures from it - night, and Christmas dressing; (b) a role sentence appended to the opening paragraph that splits authority between the two references; (c) the surface names inside `CHANGE 3` and its physics block, which had to follow the new room or the prompt contradicts itself.

**This is the one shot in the round where new prose had to be written.** Every earlier C06 prompt on this drive describes a ceiling of two boarded slopes meeting at a ridge with dark stained rafters. The attic house has none of that: one broad FLAT panel of warm cream plaster down the middle of the room, breaking at a clean knuckle line on the left and again on the right into a short shallow plaster slope running down to a low knee wall on each side, and **no exposed timber anywhere** - no rafters, no ridge beam, no collar, no king post, no tongue-and-groove boarding. There was no approved wording to copy, so the geometry paragraph and that explicit ban were authored fresh. Everything that could be copied still was: `lie flat ALONG the slope ... run with the direction of the boards ... kink and change direction at the ridge` -> `lie flat ALONG the ceiling ... run with the long direction of the room ... kink and change direction at the two knuckle lines`, the sleigh `lying on the sloping plane` -> `lying flat on the centre panel`, the snowflakes `drifting across both slopes` -> `across the flat centre panel and both side slopes`, the moon -> `high on the plaster wall above the sliding barn door`, the palette surfaces -> `the warm cream plaster`, the physics block's material -> plaster, the closing assertion -> `a real flat plaster panel breaking at a knuckle line into a shallow plaster slope on each side`, and the no-floor list -> the pale oak boards, the flat-weave rug and the bench at the foot of the bed.

The projection's layer list is unchanged, as are the bounce pose, the camera block, `CHANGE 1`'s child and knitwear, the palette statement and its cold-colour ban, the not-outer-space ban, the no-projector clause and the quality and no-text tails. Ten replacements, each applied with a single-match assert, so the untouched text is verified identical rather than asserted.

*Why:* the model was inventing the architecture, and the ceilings came out wrong. A photograph of a real room now owns the geometry. Take 1 was not refused and was not a bad picture - it was superseded only because its ceiling was invented.

*Which house, and why this one.* `house_bedroom_attic.png` is the one photograph that had never been used - it was cropped and filed during the v4 round and held in reserve as the calmer C06 alternative. This is that reserve being spent.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c06_g1.png` | camera, framing, the bounce pose and the light - unchanged from take 1 |
| @Image 2 | `../../references/house_bedroom_attic.png` | **the architecture, and nothing else** - the flat cream plaster centre panel, its two knuckle lines, the shallow side slopes down to the knee walls, the sliding barn door on its black track, the proportions |

media ids `0a845da6-2607-46cc-a595-4fee4b17d6a9` · `14d330fa-4734-4f6f-98c6-368bb4cd0312`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `a442c4f0-8275-4b57-9e74-d4be36837f36`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its walls, its door, its windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with short straight black hair, fully dressed for winter in a warm deep plum and oatmeal cable-knit Christmas jumper with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom tucked under a clipped attic roof, the ceiling one broad FLAT panel of warm cream plaster down the middle of the room which breaks at a clean knuckle line on the left and again on the right into a short shallow plaster slope running down to a low knee wall on each side, with four small flush recessed downlights set in a loose square into the flat centre panel; the plaster is smooth and unbroken - there is NO exposed timber anywhere in this room, no rafters, no ridge beam, no collar, no king post and no tongue-and-groove boarding on the ceiling or on the walls; warm greige plaster walls with plain white skirting; the back wall carrying a reclaimed oak sliding barn door of X-braced planks hung on a black steel track with black spoked rollers, flanked on its left by a tall white-framed double-hung window with a pale linen curtain and on its right by a tall white-framed glazed door with a matching curtain, and a large green potted plant standing at the far right; a framed landscape print in a thin gold frame on the wall above the bed; a low pale oak platform bed with a wide upholstered taupe headboard, two pale oak nightstands with cream drum-shade lamps, and a pale oak bench with a woven rush seat at the foot of the bed; a pale white-oak plank floor under a very large oat flat-weave rug. Copy the proportions, the flat centre panel, the two knuckle lines, the shallow side slopes, the knee walls, the barn door and its black track, and the window and the glazed door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and both table lamps are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a red tartan quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking hangs on the wall above the headboard, a warm fairy-light garland is strung around the window, a small lit Christmas tree with antique gold and cream ornaments stands on the floor beside the bed, and a small evergreen wreath with a cream bow hangs on the barn door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, the flat cream plaster centre panel of the ceiling and both shallow plaster side slopes running down to the knee walls, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling and run with the long direction of the room instead of hanging as vertical curtains, and visibly kink and change direction at the two knuckle lines where the flat centre panel breaks into the shallow side slopes; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the centre panel so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the plaster wall above the sliding barn door; one big brilliant north star high on the flat centre panel of the ceiling with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across the flat centre panel and both side slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the warm cream plaster. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster, not paint and not a sticker. The light is TRANSLUCENT - the warm cream plaster and its fine surface texture, the two knuckle lines where the flat centre panel breaks into the shallow side slopes, and the four flush recessed downlights set into that centre panel, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each knuckle line breaks the light with its own soft crease where the plaster changes angle. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the flat centre panel and bending again where it runs down each shallow side slope. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster panel breaking at a knuckle line into a shallow plaster slope on each side, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with the boy's face clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

*Flag, not fixed:* the ceiling came out as one broad continuous plaster curve rather than a crisp flat panel breaking at two knuckle lines. Timber-free and believable as real plaster, which was the defect being fixed, but not literally the photographed geometry.

### Video prompt - `clips/v6_c06_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c06_g2.png` - Higgsfield media `a442c4f0-8275-4b57-9e74-d4be36837f36` (image_job)
**Extra references** - none
**Job** - `707f2010-0be0-4630-bce6-ab7fccafbf9f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215719_707f2010-0be0-4630-bce6-ab7fccafbf9f.mp4

```
SUMMARY: a boy bounces on his bed in an attic Christmas bedroom at night while a projected snow-village picture is PLAYING across the left wall and the whole plaster ceiling, thrown there by a projector standing on the floor. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the attic bedroom, the flat plaster centre panel and its two knuckle lines, the bed with its red tartan quilt and cream cable-knit throw, the wide upholstered taupe headboard, the sliding barn door, the small lit Christmas tree, the large oat flat-weave rug, the window with its garland, the stocking, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child in a deep plum and oatmeal cable-knit Christmas jumper and soft grey knitted lounge trousers, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall and the whole plaster ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene that cone is playing: snow-covered gabled cottages with lit windows and fir trees low on the LEFT wall, plumes above their chimneys, ribbons of aurora arching across the flat centre panel and both shallow side slopes of the ceiling, a sleigh drawn by reindeer keystoned across the ceiling at the upper left, a big pale moon over on the right, a dense field of gold stars of many sizes, and a heavy fall of small glowing six-point snowflakes and points of light in red, green, blue, gold and white.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every cottage chimney on the left wall is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from the upper left corner where it sits in the start image, toward the far side of the ceiling, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, and the whole team rises and dips a little as it goes.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts, breathes brighter and dimmer on its own timing, and cycles slowly through red, green, blue and gold. One that reaches the skirting board fades out there while a fresh one fades in high near the knuckle line, so the density holds even. Track this one so the fall is unmistakable: a large white six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.0s and fades out low near the skirting at 4.0s.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON - the moon is the ONE element that holds its position. It stays exactly where it is on the right for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE:
0.0-1.5s the camera holds still. THE BOY bends his knees and pushes off the mattress; both feet leave the duvet, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
1.5-2.5s the camera still holds. He lands on both feet and drives straight into a second, higher jump, knees tucking.
2.5-4.0s the camera tilts up in one slow smooth move until the plaster ceiling fills the upper half of the frame, the aurora rippling along the flat centre panel and both shallow side slopes and the sleigh still flying across it. THE BOY stays low in frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes one move only, a tilt up at the end. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; blur; a cut; on-screen text; subtitles.
```

---

## C07 - The double-height room

*Section:* B-roll 2 - the payoff
*Status:* RE-ROLLED ON A REAL-HOUSE REFERENCE - TAKE 2 FOR REVIEW
*What it is:* a real double-height great room - the same house as C05 frame 2 - the girl mid-air over the sofa, the boy on the rug looking up, the whole two-storey volume inside the projection.

- frames: `v6_c07_g2.png` (current) · `v6_c07_g1.png` (take 1, superseded)
- clips: `v6_c07_g1.mp4` (current)

*Reused from* v3 C07 - changed: (a) the children, hair colour and age only; (b) the knitwear; (c) `CHANGE 2 - THE ROOM` swapped to the American lodge with the two-storey reclaimed red brick chimney breast, the black wrought iron mezzanine rail and the dark stained king-post trusses; (d) the surfaces named inside the physics block; (e) the projection signature and the escalation clause. The `KEEP IDENTICAL` pose paragraph - the mid-air jump, the compressed cushion, the boy from behind, both children small in frame to preserve the scale of the space - is byte-identical, as are `CHANGE 3`'s layer order, the physics block, `CHANGE 5` and the quality tail with its no-fisheye clause.

**The two moderation edits** - see the refusal log:

1. the opening line gained `with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas.`
2. `CHANGE 4` final sentence: `Both children catch that spill so their jumpers and the girl's mid-air pose read clearly.` -> `Both children catch that spill so their knitted jumpers read clearly.`

The same two edits cleared C07 in v4 and v5. Nothing describing motion, camera, pacing or framing was touched.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c07_g1.png` | owns the geometry and the look - the wide framing that carries the whole double-height volume and its full ceiling, camera position and height, the two poses, both children small in frame |

media id `c9a6740d-383b-4829-a7b9-f7a3c079c03f` - **the original reference.** The reference swap tested during the refusal round was abandoned; this frame was won on the original.

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `b21a64ba-a6bf-49ab-b1b1-d8af07925429`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long black hair tied in a low ponytail, the boy is about five with short black hair. Both are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. An American lodge double-height great room: one enormous two-storey chimney breast of reclaimed red brick running the full height of the space with a chunky dark stained timber mantel and cream knitted stockings, deep forest green painted walls either side of it with cream trim, a mezzanine landing with a black wrought iron rail crossing high across the room with an open dark stained staircase rising to it on the right, exposed dark stained king-post roof trusses under a high vaulted oatmeal boarded ceiling, tall cream-trimmed sash windows on the left showing a dark blue snowy night, dark stained oak floorboards with a large faded antique Persian rug, a long deep oxblood red sectional sofa with antique gold cushions, a leather ottoman, and a very tall real Christmas tree standing against the brick with warm white lights, antique gold and cream ornaments and wrapped gifts beneath it.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey red brick chimney breast, the painted walls, the whole high vaulted boarded ceiling, the exposed king-post trusses and the underside and railing of the mezzanine landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the brick above the mezzanine landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the red brick and the oatmeal boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real brick and real boards, not paint and not a sticker. The light is TRANSLUCENT - every individual reclaimed brick and its mortar joints, and the boards, seams and dark trusses of the ceiling, all stay clearly visible THROUGH the coloured light, and the trusses and the mantel break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare brick and bare board. Even packed full it must still read as projected light on a real textured surface, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The dark oak floorboards, the Persian rug, the oxblood sectional sofa, the ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

*Flag, not fixed:* check that the girl reads as genuinely mid-air over the cushions rather than standing on them - this pose has come out flat-footed in earlier rounds.

### TAKE 2 - the real-house architecture

*Reused from* v6 C07 take 1 - changed: (a) the whole `CHANGE 2 - THE ROOM` paragraph, replaced by the architecture of `house_great_room_trusses.png` read off the photograph, plus a second paragraph naming the only two departures from it - night, and Christmas dressing; (b) a role sentence appended to the opening paragraph that splits authority between the two references, and which also states that this is **the same house seen earlier in this ad**; (c) the surface names inside `CHANGE 3` and its physics block, which had to follow the new room or the prompt contradicts itself - the back wall is pale plaster and the vault is crossed by dark walnut rafters, not reclaimed red brick under oatmeal boards, so `run with the direction of the boards` -> `run with the direction of the rafters`, the moon -> `high on the plaster wall above the gallery landing`, the palette surfaces -> `the pale plaster and the dark walnut rafters`, the physics block's materials -> plaster and timber, the falloff `fading to bare brick and bare board` -> `fading to bare plaster`, the closing assertion -> `a real plastered vault with real timber rafters crossing it` (v4 C07's approved phrasing, copied not reworded), and the no-floor list -> the warm oak boards, the greige rug, the grey sectional and the round coffee table.

The projection's layer list is unchanged - every layer, the palette statement and its cold-colour ban, the not-outer-space ban, the `KEEP IDENTICAL` pose paragraph, `CHANGE 1`'s children and knitwear, the no-projector clause and the quality and no-text tails with the no-fisheye clause are byte-identical. Only surfaces were renamed. Nine replacements, each applied with a single-match assert, so the untouched text is verified identical rather than asserted.

*Why:* the model was inventing the architecture, and the ceilings came out wrong. A photograph of a real room now owns the geometry.

*Which house, and why this one.* Deliberately the same house as C05 frame 2 above. Video 6 opens a door onto a room and then cuts to the middle of that room - if the two shots were different houses the ad would contradict itself. The cost is that v4 C07 and v6 C07 now share a house; with two great-room photographs and three great-room slots that collision could not be avoided, so it was placed two ads apart, with different children, different knitwear and different Christmas dressing.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c07_g1.png` | camera, framing, the two poses and the light - unchanged from take 1 |
| @Image 2 | `../../references/house_great_room_trusses.png` | **the architecture, and nothing else** - the plastered cathedral vault, the dark walnut rafter pairs and their collar beams, the gallery landing, the stair, the tall windows, the proportions |

media ids `c9a6740d-383b-4829-a7b9-f7a3c079c03f` · `1d79cde5-c6a5-4259-b414-2b0d4bd8434b`

**Prompt** - `gpt_image_2_5 · sunburst · 9:16 · 2k · medium` · job `1d555499-7849-4f47-8643-8c00f25bd280`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long black hair tied in a low ponytail, the boy is about five with short black hair. Both are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: an enormous double-height great room whose ceiling is a cathedral vault of smooth cream plaster in two long slopes meeting at a ridge that runs away from the camera, crossed by two pairs of dark walnut-stained timber rafters, each pair rising as an inverted V to meet at the ridge with a matching collar beam below it, and small recessed downlights set flush into the plaster between them; a first-floor gallery landing crossing the right-hand half of the room at mid height, its railing made of clear glass panels held in slim black metal posts under a dark timber top rail; an open-tread pale oak staircase descending from that landing towards the camera with the same glass-and-black-post railing and black wall sconces on the wall beside it; a tall arched window with dark muntins set high on the right above the stair; a pale plaster back wall at the centre carrying a black arched double glazed door of many small panes; and along the left an open kitchen with pale oak slab cabinetry, a full-height integrated cabinet run, a cream island with a stone waterfall front, four woven rattan counter stools and two big woven rattan dome pendants hanging on long black cords. Wide warm oak plank floor, a large pale grey sectional sofa wrapping the right foreground, a round dark-stained wood coffee table and a large greige rug. Copy the proportions, the rafter pairs, the ridge, the glass railing, the stair and the arched door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the arched window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every downlight, pendant and sconce in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the pale plaster back wall beside the arched door with warm white lights and antique gold and cream ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and antique gold ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a large evergreen wreath with a cream bow on the arched door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey pale plaster back wall, the plaster walls either side of it, the whole high vaulted plaster ceiling, the dark walnut rafters and their collar beams and the underside and railing of the gallery landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the plaster wall above the gallery landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the dark walnut rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every dark walnut rafter, every collar beam and the ridge line of the vault, all stay clearly visible THROUGH the coloured light, and the rafters and the collar beams break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full it must still read as projected light on a real plastered vault with real timber rafters crossing it, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The warm oak floorboards, the greige rug, the grey sectional sofa, the round coffee table and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### Video prompt - `clips/v6_c07_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - multi_shot_mode custom - speedramp auto - bitrate_mode standard - workspace Oneofone1
**Start image** - `starting_frames/v6_c07_g2.png` - Higgsfield media `1d555499-7849-4f47-8643-8c00f25bd280` (image_job)
**Extra references** - none
**Job** - `11f7e62d-f275-486b-bb47-0bf465dec8e1`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215719_11f7e62d-f275-486b-bb47-0bf465dec8e1.mp4

```
SUMMARY: two children play in a double-height Christmas great room while a projected snow-village picture is PLAYING across the back wall and the whole vaulted plaster ceiling and its dark timber rafters, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the dark walnut rafters and their collar beams, the open-tread pale oak staircase and its garlanded glass railing on the right, the tall arched window high on the right with snow outside, the pale plaster back wall with its black arched glazed door and wreath, the lit Christmas tree with its presents, the pale grey sectional sofa, the round dark wood coffee table, the greige rug, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - on the rug at the front left, back to camera, facing the wall, turning on the spot with his arms out.
THE OTHER CHILD - standing up on the sofa cushions in front of the garlanded staircase on the right, back to camera, with both arms raised toward the wall, bouncing on the spot.
Both in deep plum and oatmeal cable-knit Christmas jumpers and soft grey knitted lounge trousers. Exactly two children. No third child, no adult, no pet.
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
```

---

## Round summary

| shot | file | job | status |
|---|---|---|---|
| C02 | `starting_frames/v6_c02_g1.png` | `d4bf54ca` | take 1, for review - watch for the doubled wordmark |
| C03 | `starting_frames/v6_c03_g1.png` | `e3d2f546` | take 1, for review - watch for the squat dome |
| C04 | `starting_frames/v6_c04_g1.png` | `339a1286` | take 1, for review - watch for the squat dome |
| C05 F1 | `starting_frames/v6_c05_g1.png` | `e393a7c9` | take 1, for review |
| C05 F2 | `references/v6_c05_r1.png` | `53080c12` | take 1, superseded - invented architecture |
| C06 | `starting_frames/v6_c06_g1.png` | `abdf9332` | take 1, superseded - invented architecture. Passed first pass, unedited |
| C07 | `starting_frames/v6_c07_g1.png` | `b21a64ba` | take 1, superseded - invented architecture. Cleared on submission 3 |

**Take 2 - the real-house reference round, B-roll 2 only**

| shot | file | job | status |
|---|---|---|---|
| C05 F2 | `references/v6_c05_r2.png` | `b6fb9884` | take 2, **current**, for review |
| C06 | `starting_frames/v6_c06_g2.png` | `a442c4f0` | take 2, **current**, for review |
| C07 | `starting_frames/v6_c07_g2.png` | `1d555499` | take 2, **current**, for review |

No shot has more than one generation per take. A moderation refusal returns no file, so the resubmissions below are not re-rolls.

## The real-house reference round - B-roll 2

*2026-09-19.* The v4 treatment landed, so Daniel extended it: *"it turned out good, now you need to remake / V5 - C7 / V6 - C5, C6, C7."* On the reference shortage he added: *"Use houses in that style, make shure that the ceiling it's looking good and things make sense."*

All three B-roll 2 shots in this video were re-rolled. C05 frame 1 is a closed door with no ceiling in shot, so it is out of scope and untouched, exactly as in v4. C02, C03 and C04 stay at take 1.

**Which house went where.**

| shot | photograph | why |
|---|---|---|
| C05 F2 | `house_great_room_trusses.png` | v4 spent it on a wide shot; this is a doorway shot, so the picture differs |
| C06 | `house_bedroom_attic.png` | the one photograph never used before - filed in reserve during the v4 round |
| C07 | `house_great_room_trusses.png` | **the same house as C05 F2, on purpose** - the door opens onto this room, so the cut has to land in it |

Two great-room photographs cannot cover three great-room slots across v4, v5 and v6, so one collision was forced. It sits between v4 C07 and v6 C07 - two ads apart, different children, different knitwear, different dressing.

**The attic house needed new geometry language.** Its ceiling is a broad flat plaster panel that breaks at a knuckle line into a shallow slope down to a knee wall on each side, with **no exposed timber anywhere**. Every earlier C06 prompt on this drive assumed boarded slopes meeting at a ridge with dark rafters, and there was no approved wording to copy, so the geometry paragraph and an explicit no-timber ban were written fresh for C06 - the only place in this round where new prose was authored rather than copied.

**One divergence to flag.** The room palettes now leave the v6 look pack (inky green / mahogany / brass) behind, because these houses are plaster, oak and cream. Architecture off the photograph beat the look pack, because architecture is the defect Daniel named. The antique-gold-and-cream Christmas dressing still carries the v6 colour story.

## Refusal log - C07 only

C07 was refused `nsfw` on the first pass. **C06 in this video was not** - it went through on the first submission with no edits at all. The investigation ran across v4, v5 and v6 together, in four rounds:

| round | what changed | result |
|---|---|---|
| 1 | nothing - identical prompt, identical reference | refused again |
| 2 | reference swapped to the approved v3 frames, prompt untouched | refused again |
| 3 | original references restored, surgical additive text edits | v6 C07 passed (`b21a64ba`) |
| 4 | v4 C06 only - a third edit | not needed for v6 |

**What this establishes.** The verdict is deterministic on the exact prompt string - identical resubmissions were refused every time. It is **not** driven by the reference image - every reference swap was refused. The trigger is text-side, and specifically the clauses that emphasise a child's face and body rather than motion, camera, pacing or framing.

**v6 C06 is the cleanest counter-example on this drive.** It kept both of the clauses that had to be rewritten in v4 and v5 - `The boy's face and his knitted jumper catch that spill so his face reads clearly.` and the `perfectly exposed with the boy's face clearly readable` tail - and passed on the first attempt. C05 frame 2 in this video did the same. So the trigger is a **combination** of the prompt's contents, not a single banned phrase. Rewriting those clauses is a reliable fix when a refusal happens; their presence does not predict a refusal.

This **contradicts** the v2 C06 precedent, which recorded a reference swap as the only thing that had ever cleared a repeated refusal. That precedent did not hold here.

## Result URLs

CDN base `https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/`

```
v6_c02_g1.png   hf_20260919_182327_d4bf54ca-487c-4f02-92b5-b0778a68c74b.png
v6_c03_g1.png   hf_20260919_182327_e3d2f546-11bb-4ccc-ba70-288d93b2c8eb.png
v6_c04_g1.png   hf_20260919_182327_339a1286-5b1c-4461-89d7-41c52a4722c8.png
v6_c05_g1.png   hf_20260919_182327_e393a7c9-e564-4e4d-a55c-bf19b637848e.png
v6_c05_r1.png   hf_20260919_182327_53080c12-ace7-44bf-90b7-1cca5268e592.png
v6_c06_g1.png   hf_20260919_182327_abdf9332-5e41-4966-9b60-cbf747f02be3.png
v6_c07_g1.png   hf_20260919_184014_b21a64ba-a6bf-49ab-b1b1-d8af07925429.png
v6_c05_r2.png   hf_20260919_210246_b6fb9884-52a1-4556-bb00-59aa6deb8f7d.png
v6_c06_g2.png   hf_20260919_210246_a442c4f0-8275-4b57-9e74-d4be36837f36.png
v6_c07_g2.png   hf_20260919_210246_1d555499-7849-4f47-8643-8c00f25bd280.png
```

## Upscales - 2026-09-20

All seven picked takes upscaled through the Higgsfield web UI at
`https://higgsfield.ai/upscale` (Model version **Pro** is UI-only - the
`upscale_video` MCP tool rejects `model_version`, so every Pro run has to be
driven in the browser).

**Settings** - ByteDance Upscale - Model version Pro - Resolution 2K -
FPS 30fps - Preset AIGC on C01, Common on C02-C07 (Daniel's spec, verbatim).

Outputs keep the source filename exactly and live in `clips/upscaled/`;
the folder is the suffix. All seven land at 1440x2560, 30fps, duration
unchanged from the source.

```
clip            preset   job id                                 result
v6_c01_g1.mp4   AIGC     696f31f8-5e33-4e96-9f94-77aafa36320e   hf_20260920_134851_718c734d-51d4-4f81-aeef-6b54db3ac042.mp4
v6_c02_g1.mp4   Common   dbfb9b17-dda1-4978-9c3e-5a5a75e6d3e2   hf_20260920_135010_a2c19cb6-8a33-4602-baaa-f404e02903d0.mp4
v6_c03_g1.mp4   Common   761e5c40-d977-41b5-8d4a-1d07826cd729   hf_20260920_135052_ebc71384-a73c-4c49-a342-e433b9c3cf2a.mp4
v6_c04_g1.mp4   Common   043413f6-718c-4e55-9f6d-d7818ed9fe4e   hf_20260920_135332_257e8642-5571-4110-8d34-271db40ab6bc.mp4
v6_c05_g5.mp4   Common   48d2ad26-dfc1-4dac-a99a-dbff6015147f   hf_20260920_135414_7185c7b5-670f-4e1e-a709-6c9e20a40cd7.mp4
v6_c06_g1.mp4   Common   e5820b43-634e-4e33-abfd-13244b06725b   hf_20260920_135455_08a906f8-31a3-4ddc-81f6-21486f2280ef.mp4
v6_c07_g1.mp4   Common   ddf5cd0e-6d76-44ea-8ce7-8aa2ae0d9a78   hf_20260920_135538_1b8c7d13-922d-4c54-b655-109b0805a48b.mp4
```

Result CDN base is `https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/`.
C05 is the only shot with more than one take, so its last take is g5; every
other shot's last take is g1.

*Defect, FIXED 2026-09-20:* the source clips `v6_c02_g1.mp4` through
`v6_c07_g1.mp4` had no entry in this file. All ten video jobs (C02, C03, C04,
the five C05 takes, C06, C07) were recovered from Higgsfield and archived as
`### Video prompt` subsections under their shot headings above, each with its
settings, media roles, job id and result URL. Every v6 clip can now be
re-created from this prompts.md alone. Two caveats are recorded in place: the
C02 job carries a re-uploaded start image rather than the original image job,
and an earlier C02 take exists outside the scanned window and is not recorded.

## Next

Daniel reviews the board. B-roll 2 now shows take 2 on all three shots - C05 F2, C06 and C07 - rebuilt on real-house architecture references; C02, C03, C04 and C05 F1 are unchanged at take 1. No clips are submitted until he picks. C01 (the hook) has not been generated for this video.

*Flag, not fixed:* in `v6_c06_g2.png` the ceiling came out as one broad continuous plaster curve rather than the crisp flat centre panel breaking at two knuckle lines that the photograph shows. It is timber-free and reads as real plaster, which was the defect being fixed, but it is not literally the photographed geometry. Daniel's call whether it matters.


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v6_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v6_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v6_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v6_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v6_c05_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v6_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v6_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c05_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c05_g4.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c05_g5.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v6_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v6_c05_r1.png` | Embedded PNG `hf-job-id`: `53080c12-ace7-44bf-90b7-1cca5268e592`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v6_c05_r2.png` | Embedded PNG `hf-job-id`: `b6fb9884-52a1-4556-bb00-59aa6deb8f7d`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c01_g1.png` | Embedded PNG `hf-job-id`: `836690da-363a-486e-8ca1-fdf21acd0523`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c01_g2.png` | Embedded PNG `hf-job-id`: `79e4f6de-39e4-4715-8260-61db9f192ef7`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c01_g3.png` | Embedded PNG `hf-job-id`: `b400614f-d335-4252-8433-a21fe541acdf`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c01_g4.png` | Embedded PNG `hf-job-id`: `9cd2cb32-1f96-4484-ad2f-cc726aca8088`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c02_g1.png` | Embedded PNG `hf-job-id`: `d4bf54ca-487c-4f02-92b5-b0778a68c74b`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c03_g1.png` | Embedded PNG `hf-job-id`: `e3d2f546-11bb-4ccc-ba70-288d93b2c8eb`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c04_g1.png` | Embedded PNG `hf-job-id`: `339a1286-5b1c-4461-89d7-41c52a4722c8`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c05_g1.png` | Embedded PNG `hf-job-id`: `e393a7c9-e564-4e4d-a55c-bf19b637848e`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c06_g1.png` | Embedded PNG `hf-job-id`: `abdf9332-5e41-4966-9b60-cbf747f02be3`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c06_g2.png` | Embedded PNG `hf-job-id`: `a442c4f0-8275-4b57-9e74-d4be36837f36`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c07_g1.png` | Embedded PNG `hf-job-id`: `b21a64ba-a6bf-49ab-b1b1-d8af07925429`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v6_c07_g2.png` | Embedded PNG `hf-job-id`: `1d555499-7849-4f47-8643-8c00f25bd280`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C01: the board did not show the exact clip prompt of `v6_c01_g1.mp4`; it now does (text above).
- C01: the board did not show the exact image prompt of `v6_c01_g4.png`; it now does.
- C02: the board did not show the exact clip prompt of `v6_c02_g1.mp4`; it now does (text above).
- C03: the board did not show the exact clip prompt of `v6_c03_g1.mp4`; it now does (text above).
- C04: the board did not show the exact clip prompt of `v6_c04_g1.mp4`; it now does (text above).
- C05: the board did not show the exact clip prompt of `v6_c05_g5.mp4`; it now does (text above).
- C06: the board did not show the exact clip prompt of `v6_c06_g1.mp4`; it now does (text above).
- C07: the board did not show the exact clip prompt of `v6_c07_g1.mp4`; it now does (text above).

### C01 — Ladder fail — taping Santa up

**In the cut:** `starting_frames/v6_c01_g4.png` → `clips/v6_c01_g1.mp4`

#### Image prompt — `starting_frames/v6_c01_g4.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · high · 1520×2688
**Job** - `9cd2cb32-1f96-4484-ad2f-cc726aca8088`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_132402_9cd2cb32-1f96-4484-ad2f-cc726aca8088.png
**References, in submission order**
- @Image 1: `content/video_6_assets/starting_frames/v6_c01_g1.png` · Higgsfield media `836690da-363a-486e-8ca1-fdf21acd0523`

````text
Keep the attached image exactly as it is - the same room, the same camera position, distance and angle, the same woman in the same pose near the top of the same ladder with both arms up, the same inflatable Santa taped flat to the ceiling with the same silver duct tape, the same curved staircase, garland, stockings, marble fireplace, gold mirror, Christmas tree, blue velvet sofa and rug, the same lighting, and the same clean empty band of ceiling across the top sixth of the frame. Change only these two things:

1. HER CLOTHES: instead of the cream sweater and black leggings she is wearing matching Christmas American-flag pyjamas - a pyjama top with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit. Same body, same hair, same pose, same thick grey wool socks, same roll of duct tape in her left hand.

2. A UNITED STATES FLAG: a real fabric United States flag hangs flat against the plain cream wall in the background behind her, clearly readable stars and stripes, hanging straight and still. It does not cover the Christmas tree, the fireplace or the staircase, and it does not reach up into the empty band of ceiling at the top of the frame.

Everything else in the picture stays exactly as it is. Same neutral white balance with no orange cast, same iPhone snapshot look, tack sharp and in focus everywhere, absolutely nothing blurry, no background blur.
````

#### Video prompt — `clips/v6_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `3be81f83-f33e-4612-8a19-7d3a2c532c38`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_133110_3be81f83-f33e-4612-8a19-7d3a2c532c38.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v6_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c01_g4.png` · Higgsfield media `9cd2cb32-1f96-4484-ad2f-cc726aca8088`
- image ref 1: `content/video_6_assets/starting_frames/v6_c01_g4.png` · Higgsfield media `9cd2cb32-1f96-4484-ad2f-cc726aca8088`

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

#### Image prompt — `starting_frames/v6_c01_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · high · 1520×2688
**Job** - `836690da-363a-486e-8ca1-fdf21acd0523`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_131256_836690da-363a-486e-8ca1-fdf21acd0523.png
**References, in submission order**
- @Image 1: `content/video_4_assets/starting_frames/v4_c01_g12.png` · Higgsfield media `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas living room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height traditional living room with an open curved staircase - cream panelled walls, the wide staircase at the left with a thick green garland wound around its dark timber banister and stockings hung along it, a white marble fireplace with a lit fire and a gold mirror above it, a tall Christmas tree with warm white lights and red and gold baubles at the right, a deep blue velvet sofa, a patterned red and blue rug on dark oak boards.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is early 30s with long auburn hair in a loose low ponytail, a cream cable-knit sweater, black leggings and thick grey wool socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and the panelling read as clean white and cream paint, her sweater reads as true cream, the banister and the floor read as natural wood, the rug keeps its own colours. The Christmas tree lights, the fire and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

#### Image prompt — `starting_frames/v6_c01_g2.png`

**Settings** - gpt_image_2 · 9:16 · 2k · high · 1520×2688
**Job** - `79e4f6de-39e4-4715-8260-61db9f192ef7`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_131256_79e4f6de-39e4-4715-8260-61db9f192ef7.png
**References, in submission order**
- @Image 1: `content/video_4_assets/starting_frames/v4_c01_g12.png` · Higgsfield media `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas living room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height white modern farmhouse living room - white shiplap walls, a wall of tall black-framed windows at the right with a dark winter garden behind them, a white open staircase with slim black spindles at the left and a garlanded landing above it, a white plaster fireplace, a slim flocked Christmas tree with warm white lights and pale blue and silver ornaments, a light linen sectional sofa, pale wide-plank oak floor and a cream jute rug.

There is no projected light anywhere - the ceiling, the walls and the staircase are plain painted plaster and plain timber, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fireplace and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE WHITE CEILING high above her, lying on its back against the plaster and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is mid-30s with dark brown hair in a low bun, an oversized oatmeal sweatshirt, light-wash jeans and white ribbed socks, standing near the top of a tall wooden A-frame ladder that reaches up into the double-height space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The ceiling and the shiplap read as clean white paint, her sweatshirt reads as true oatmeal, the window frames read as true black, the oak floor reads as natural wood. The Christmas tree lights, the fireplace and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweatshirt, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

#### Image prompt — `starting_frames/v6_c01_g3.png`

**Settings** - gpt_image_2 · 9:16 · 2k · high · 1520×2688
**Job** - `b400614f-d335-4252-8433-a21fe541acdf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_131256_b400614f-d335-4252-8433-a21fe541acdf.png
**References, in submission order**
- @Image 1: `content/video_4_assets/starting_frames/v4_c01_g12.png` · Higgsfield media `195e86f7-31ca-48d1-a1eb-4c0e64e0cf74`

````text
Extremely high quality candid vertical iPhone photo taken from slightly behind and below a woman on a tall A-frame ladder in a double-height Christmas great room, evening. We see her from behind at three-quarters, her raised arms and the high ceiling in front of her.

FRAMING AND ANGLE: copy the attached image exactly - the same camera position, the same distance, the same low three-quarters-from-behind angle, the tall A-frame ladder standing in the middle of the frame with the woman near the top of it, the same amount of floor visible below her, the inflatable Santa taped flat to the ceiling above her at the same place in the frame. Only the room and the woman change.

THE ROOM: a double-height American lodge great room - a two-storey reclaimed red brick chimney breast with a chunky dark stained timber mantel and a lit fire, a black wrought iron mezzanine rail above at the left with stockings hung from it, dark stained king-post trusses under a high vaulted oatmeal boarded ceiling, a tall Christmas tree with warm white lights and antique gold baubles at the right, an oxblood leather sofa, a faded antique Persian rug on dark stained oak boards.

There is no projected light anywhere - the boarded ceiling, the trusses, the brick and the walls are plain painted boards, plain dark wood and plain brick, completely clean, no projected patterns, no snowflakes, no stars, no coloured light spilling on any surface. The room is lit only by the Christmas tree, the fire and ordinary warm lamps.

THE KEY ELEMENT: a large inflatable Santa Claus decoration is TAPED FLAT TO THE HIGH VAULTED OATMEAL BOARDED CEILING high above her, between the dark timber trusses, lying on its back against the boards and facing down into the room, held by a mess of criss-crossed silver duct tape strips over its legs, arms and hat. It is clearly fixed to the ceiling. One corner has started to peel, with a long strip of tape hanging down beside her head.

The mom is late 20s with long black hair in a low ponytail, a deep plum and oatmeal cable-knit sweater with a cream snowflake yoke, soft grey knitted trousers and thick red socks, standing near the top of a tall wooden A-frame ladder that reaches up into the vaulted space, both hands above her head pressing a fresh piece of tape onto Santa's shoulder, a roll of duct tape in her left hand. The ladder is clearly very tall and she is high off the floor.

COLOUR - READ THIS CAREFULLY: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia, NOT golden-hour, and there is no warm colour cast laid over the whole frame. The boarded ceiling reads as clean warm oatmeal paint, the trusses read as natural dark wood, the chimney breast reads as natural red brick, her sweater reads as true deep plum and oatmeal, the rug keeps its own colours. The Christmas tree lights, the fire and the lamps are warm points of light sitting inside a neutrally balanced room - they do not tint the rest of the picture.

LIGHTING AND QUALITY: bright, clean and evenly lit - plenty of light on the high ceiling and on her back, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll: an ordinary everyday snapshot, not a magazine photo and not a rendered image. Modern phone-camera look - wide dynamic range, lifted shadows, clean highlights, accurate colour. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the duct tape, the inflatable vinyl sheen and the knit of her sweater, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no grain, no film look, no cinematic grade, no vignette, no bloom.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top sixth of the frame - completely empty and free of Santa, of tape, of beams, of garland and of any other object, so a caption can sit there. Do not pull the camera back or shrink the woman to make that room - she stays exactly the size described above.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v6_c02_g1.png` → `clips/v6_c02_g1.mp4`

#### Image prompt — `starting_frames/v6_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `d4bf54ca-487c-4f02-92b5-b0778a68c74b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_182327_d4bf54ca-487c-4f02-92b5-b0778a68c74b.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `1cdfcc53-e771-4bba-9eab-b1788346098b`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep plum wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a deep mahogany dining table top: a rich dark red-brown timber with fine ribbon-stripe figure running through it, French-polished to a deep glassy sheen that holds soft warm reflections, with a moulded edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused dark traditional American Christmas drawing room: walls fully panelled in deep black-green painted joinery, a white marble fireplace with a polished brass fender and cream knitted stockings hanging from the mantel, a decorated Christmas tree with warm white fairy lights and antique gold and cream ornaments standing off to one side, a brass picture light glowing over a dark gilt-framed painting, all well out of focus so the box stays the clear subject.

Dress the mahogany table more festively: a sprig of fir and a few red berries, two or three small antique gold and cream baubles, a short cream candle, a soft warm string light trailing across the polished mahogany, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.
````

#### Video prompt — `clips/v6_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `7be8c6ed-38e3-4f07-b126-12e2a930dda9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_223516_7be8c6ed-38e3-4f07-b126-12e2a930dda9.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v6_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c02_g1.png` · Higgsfield media `6b40ce6f-718f-44b5-86ec-5b44a1bb44b0`
- video ref 1: `references/scene_no_audio-2.mp4` — upload · 2.14 s · Higgsfield media `1d2e8a8d-1e49-422a-8b04-d1a1230096a4`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a French-polished deep mahogany dining table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a deep plum wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a French-polished deep mahogany dining table fills the frame. A lit cream pillar candle sits at the left, fir sprigs with red berries and small antique gold and cream baubles beside it, a white marble fireplace with a polished brass fender, hanging cream knitted stockings and deep black-green panelled walls, and a decorated Christmas tree with warm white lights and antique gold and cream ornaments softly out of focus behind. The candle, the fir, the berries, the baubles, the defocused fireplace and the defocused tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the French-polished deep mahogany dining table, lid flaps folded back, with the candle, the fir, the berries, the defocused fireplace and the defocused tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v6_c03_g1.png` → `clips/v6_c03_g1.mp4`

#### Image prompt — `starting_frames/v6_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `e3d2f546-11bb-4ccc-ba70-288d93b2c8eb`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_182327_e3d2f546-11bb-4ccc-ba70-288d93b2c8eb.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `7ccdd557-bfee-45b0-a067-0652320f537b`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a deep plum wool sweater sleeve pushed back; right forearm enters from the right in the same deep plum sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed cream limestone counter: a soft warm off-white stone with gentle caramel veining drifting through it and fine darker fossil flecks scattered across the surface, a chunky bullnosed edge, a completely matte surface with no shine at all. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A dark traditional American Christmas kitchen, softly defocused: inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream tumbled-marble backsplash with soft uneven edges, a cream enamel range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v6_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `0f3cf04e-54db-494c-bec6-10d00f0ab15c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215208_0f3cf04e-54db-494c-bec6-10d00f0ab15c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v6_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c03_g1.png` · Higgsfield media `e3d2f546-11bb-4ccc-ba70-288d93b2c8eb`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a honed cream limestone kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in deep plum wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a honed cream limestone countertop fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream enamel range built into the tall cabinet run on the left, a cream tumbled-marble backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the limestone counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the stone. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the stone in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the stone.
3.0-3.4s - the four feet of the stand touch the stone; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The limestone is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the stone, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v6_c04_g1.png` → `clips/v6_c04_g1.mp4`

#### Image prompt — `starting_frames/v6_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `339a1286-5b1c-4461-89d7-41c52a4722c8`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_182327_339a1286-5b1c-4461-89d7-41c52a4722c8.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep plum wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a honed cream limestone counter: a soft warm off-white stone with gentle caramel veining drifting through it and fine darker fossil flecks scattered across the surface, a chunky bullnosed edge, a completely matte surface with no shine at all. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A dark traditional American Christmas kitchen, softly defocused across the top third of the frame: inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream tumbled-marble backsplash with soft uneven edges, a cream enamel range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v6_c04_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `74b8404c-8310-458a-acd0-040368826711`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215209_74b8404c-8310-458a-acd0-040368826711.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v6_c04_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c04_g1.png` · Higgsfield media `339a1286-5b1c-4461-89d7-41c52a4722c8`

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
THE LEFT HAND - a woman's hand in a deep plum wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same deep plum sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a honed cream limestone countertop fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with inky green inset cabinets with beaded face frames and unlacquered brass cup pulls, a cream enamel range built into the tall cabinet run on the right, a cream tumbled-marble backsplash, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and red berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the stone around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the limestone immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v6_c05_g1.png`, `references/v6_c05_r2.png` → `clips/v6_c05_g5.mp4`

#### Image prompt — `starting_frames/v6_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `e393a7c9-e564-4e4d-a55c-bf19b637848e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_182327_e393a7c9-e564-4e4d-a55c-bf19b637848e.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and cream sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American four-panel door painted a deep oxblood red in a soft eggshell finish: crisp raised mouldings around four flat recessed panels, clean painted surfaces with the faintest brush texture, an antique brass knob and a matching antique brass escutcheon plate, set in a plain painted cream frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the oxblood paint reads clearly as a deep red rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Image prompt — `references/v6_c05_r2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `b6fb9884-52a1-4556-bb00-59aa6deb8f7d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_210246_b6fb9884-52a1-4556-bb00-59aa6deb8f7d.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `f3a8c329-4152-4a22-9469-d89578812e09`
- @Image 2: `references/house_great_room_trusses.png` · Higgsfield media `1d79cde5-c6a5-4259-b414-2b0d4bd8434b`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: an enormous double-height great room whose ceiling is a cathedral vault of smooth cream plaster in two long slopes meeting at a ridge that runs away from the camera, crossed by two pairs of dark walnut-stained timber rafters, each pair rising as an inverted V to meet at the ridge with a matching collar beam below it, and small recessed downlights set flush into the plaster between them; a first-floor gallery landing crossing the right-hand half of the room at mid height, its railing made of clear glass panels held in slim black metal posts under a dark timber top rail; an open-tread pale oak staircase descending from that landing towards the camera with the same glass-and-black-post railing and black wall sconces on the wall beside it; a tall arched window with dark muntins set high on the right above the stair; a pale plaster back wall at the centre carrying a black arched double glazed door of many small panes; and along the left an open kitchen with pale oak slab cabinetry, a full-height integrated cabinet run, a cream island with a stone waterfall front, four woven rattan counter stools and two big woven rattan dome pendants hanging on long black cords. Wide warm oak plank floor, a large pale grey sectional sofa wrapping the right foreground, a round dark-stained wood coffee table and a large greige rug. Copy the proportions, the rafter pairs, the ridge, the glass railing, the stair and the arched door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the arched window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every downlight, pendant and sconce in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing against the pale plaster back wall beside the arched door with warm white lights and antique gold and cream ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and antique gold ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a large evergreen wreath with a cream bow on the arched door. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every plaster wall, the whole high vaulted plaster ceiling, the dark walnut rafters and their collar beams, and the underside and railing of the gallery landing, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the plaster wall above the gallery landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the dark walnut rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, and every dark walnut rafter, every collar beam and the ridge line of the vault, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the collar beams break the light with their own hard shadow lines where they stand proud of the plaster. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real plastered cathedral vault with dark walnut rafter pairs and their collar beams crossing it, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The warm oak floorboards, the greige rug, the grey sectional sofa, the round coffee table, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v6_c05_g5.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `dcb1778f-3a97-4fc7-a2e8-172f977af6b6`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_231602_dcb1778f-3a97-4fc7-a2e8-172f977af6b6.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v6_c05_g5.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c05_g1.png` · Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4`
- image ref 1: `content/video_6_assets/references/v6_c05_r2.png` · Higgsfield media `c4fc3193-2325-46da-a3a7-0f0cc422be64`

````text
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s: a closed oxblood red door with a wreath, a hand on the brass knob.

THE PICTURE ON THE WALLS IS A CLOSED SET
The start image does not show the room, so read the room ONLY from @Image 1. Everything thrown onto the walls and ceiling is already drawn in @Image 1. You are not designing a projection - you are making the one in @Image 1 move. Invent nothing. If a thing is not in the list below, it does not exist in this clip.

THE COMPLETE LIST OF WHAT IS PROJECTED, AND WHAT EACH ONE DOES

Moving layer - these travel across the plaster:
- Six-point snowflakes, white and pale gold. They fall steadily and continuously, top to bottom, new ones entering above as others slide out below. They never hang still. They are FLAT LIGHT LYING ON THE PLASTER and they never leave it: a flake slides down the face of the ceiling or the face of a wall and stays welded to that surface for its whole journey. It is a stain of light on a solid surface, not a falling object. There is no snow in the air of the room, none between the camera and the walls, none in front of the children, the sofa, the staircase or the tree, and none landing on the floor or on anyone.
- Candy canes, red and white striped. They drift down with the snow, tumbling slowly end over end as they go.
- Shooting stars, gold with a tail. They streak across, the tail thinning out behind them, and fade; fresh ones set off elsewhere.
- The aurora ribbons, green and pink and magenta, laid along and between the dark rafters. A bright swell runs the length of each ribbon end to end, the way a wave runs down a shaken rope, and the ribbons themselves creep sideways.
- The fine gold star specks filling the gaps. The whole field creeps slowly and the specks twinkle in and out.
- The gold line of musical notes on their staff, along the right-hand rafter. The notes travel along the staff like sheet music sliding past.
- The reindeer team and sleigh, gold, to the left of the moon. They gallop steadily across and finish a long way from where they set off.

Holding layer - these keep their exact positions and only twinkle:
- The moon, bright and full, centre right. It holds and only breathes brighter and dimmer.
- The church with the tall steeple, right of the moon. Holds; its windows twinkle.
- The snowy village houses low on the left wall. Hold; their lit windows twinkle.
- The big gold Christmas tree and the slimmer cone tree behind it on the left wall. Hold; their lights twinkle.
- The street lamps among the houses. Hold; they flicker faintly.

ADD NOTHING. No smoke and no chimney plumes of any kind. No extra buildings, no extra trees, no extra figures, no angels, no bells, no letters, no numbers, no new shapes. Nothing appears that is not on the list.

EVERY PROJECTED SHAPE IS PAINT, NOT AN OBJECT. All of it is flat light lying on whatever surface it lands on. It skews and stretches with the slope of that surface, it bends over the rafters, it breaks where a wall meets the ceiling. Nothing ever floats free of a surface into the air of the room.

WHAT ELSE HOLDS: the real room. The plaster, the rafters, the staircase and its gallery landing, the door, the wooden floor, the rug, the sofa, the real Christmas tree and its lights, the framing, the colours. The projected picture's outer edge stays put - it never rotates, spins, swings or slides across the room as one sheet. Only the things inside it travel.

@Image 1 is the authority on the room and on every projected shape: its layout, its staircase, its furniture, its two children, and the exact set, style and colour of the projected shapes. It is a photograph - copy its look, never its stillness.

BEATS
0.0-0.8s - The hand turns the brass knob and pushes the door away from camera. Behind it the room is ALREADY running: snow already falling, the aurora already swelling, the reindeer already crossing. The widening gap simply uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on, spreads or grows as the door opens, and nothing glows along the door edge, frame or gap.
0.8-2.0s - The door swings wide and the camera walks through. The snow keeps falling at the same steady rate it already had, down the face of the far wall. It stays on that wall - it does not cross the open air of the room and it does not drift toward the camera.
2.0-3.3s - Inside. The two children are both already in motion and stay in motion. Projected shapes slide down the walls behind them and pass across their backs and faces.
3.3-5.0s - The camera keeps walking and TILTS UP until the rafters fill the top of frame. The ceiling is the busiest surface in the clip: snow pouring down it, the swell running along every aurora ribbon, the notes sliding along the staff, the reindeer crossing it, the specks twinkling.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the walk from 0.8s, the tilt up from 3.3s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes - no phone, screen, hand or device in frame after 0.8s.

THE CHILDREN - exactly two, both visible from 2.0s on, no adults, no third child, no pets. Deep plum and oatmeal cable-knit knitwear, as in @Image 1. They never stand still and never pose.

SHARPNESS - hold the sharpness, exposure and fine detail of the start image: the wood grain of the floor, the panel edges and sheen of the red door, the brass knob, the skin of the bare forearm, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, children laughing, quiet room tone. NO music, no song, no score, no instruments, no bells used as music.

BANNED - snow, snowflakes or any particles falling through the open air of the room; volumetric or three-dimensional snow; anything drifting between the camera and the walls; snow passing in front of the children, the sofa, the staircase, the rug or the real tree; snow settling on the floor, the furniture or anyone's hair or shoulders; any projected shape that appears to leave the surface it is painted on; any projected shape that is not on the list above; smoke; a shape that stays in the same place on the plaster when the list says it travels; a projection that appears to move only because the camera moves; shapes that only twinkle when the list says they travel; a parked sleigh; a still aurora; a still or empty ceiling when the camera tilts up; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; any music; blur or soft focus; children standing still or posed; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
````

**Other takes of C05 on disk (5)**

#### Image prompt — `references/v6_c05_r1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `53080c12-ace7-44bf-90b7-1cca5268e592`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_182327_53080c12-ace7-44bf-90b7-1cca5268e592.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `f3a8c329-4152-4a22-9469-d89578812e09`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. A dark traditional American family room: deep forest green painted walls with cream painted panelling to waist height and cream trim, a high vaulted ceiling clad in dark stained tongue-and-groove boards with exposed cream-painted rafters rising to a dark stained ridge beam, a full-height black marble fireplace on the right with a low fire burning behind a polished brass fender and a carved cream mantel with cream knitted stockings hanging from it, a deep oxblood red chesterfield sofa with antique gold cushions and a cream cable-knit throw, a faded antique Persian rug over dark stained oak floorboards, a tall real Christmas tree in the left corner with warm white lights and antique gold and cream ornaments, wrapped gifts under it, and a tall cream-trimmed sash window behind the tree showing a dark blue snow-covered night outside.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every painted wall, the whole vaulted boarded ceiling and its cream rafters and ridge beam, and the black marble of the fireplace, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the wall beside the fireplace; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the deep green paint and the dark boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the dark stained boards, their seams and their subtle grain, and every cream-painted rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The dark oak floorboards, the Persian rug, the oxblood sofa, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v6_c05_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `008b3706-79f9-4944-89d3-ea62886d03da`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215719_008b3706-79f9-4944-89d3-ea62886d03da.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: uploaded image, not on the drive · Higgsfield media `e393a7c9-e564-4e4d-a55c-bf19b637848e`
- image ref 1: uploaded image, not on the drive · Higgsfield media `b6fb9884-52a1-4556-bb00-59aa6deb8f7d`
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

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the oxblood red door, the brass of the round knob and its escutcheon, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed oxblood red four-panel door in its cream frame, the brass round knob on its brass escutcheon, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow hanging on the door.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree against the pale plaster back wall at the centre, the pale grey sectional sofa wrapping the right foreground, the gallery landing with its glass-panelled garlanded railing on the right, the high vaulted plaster ceiling on its dark walnut rafters, the two children and their deep plum and oatmeal cable-knit knitwear, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - deep plum and oatmeal cable-knit Christmas jumper with soft grey knitted lounge trousers, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching deep plum and oatmeal cable-knit knitwear, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - an enormous American great room with a high vaulted cream plaster ceiling on dark walnut rafters and their collar beams: tall decorated Christmas tree against the pale plaster back wall at the centre, pale grey sectional sofa wrapping the right foreground, gallery landing with a glass-panelled garlanded railing crossing the right at mid height, tall arched window high on the right, warm oak plank floor with a large greige rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, the hallway lit only by its own warm dim light, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door swings away from the camera and the room behind it comes into view. The projection is ALREADY running at full strength on the far wall and across the whole ceiling before the door moves - the widening doorway simply uncovers more of a display that was already there, the way drawing a curtain back uncovers a view. Nothing lights up, ignites, spreads, ripples or switches on as the door opens, and nothing glows along the edge of the door, along the door frame or in the gap.
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

#### Video prompt — `clips/v6_c05_g2.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `07783067-8c19-4bf0-b4e1-26ffc370823b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_223429_07783067-8c19-4bf0-b4e1-26ffc370823b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c05_g1.png` · Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4`
- image ref 1: `content/video_6_assets/references/v6_c05_r2.png` · Higgsfield media `c4fc3193-2325-46da-a3a7-0f0cc422be64`
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

IMAGE QUALITY RULE - SECOND MOST IMPORTANT. The finished clip must look at least as sharp and as clean as the start image. Do not soften it, do not smear it, do not repaint it, do not re-imagine it. Hold the exact sharpness, exposure, contrast and fine detail of the start image: the wood grain of the floor, the panel edges and painted sheen of the oxblood red door, the brass of the round knob and its escutcheon, the skin texture and fine hairs of the bare forearm, the individual leaves of the green wreath and its red bow. Crisp modern phone footage, in focus from the first frame to the last. BANNED: blur, soft focus, haze, motion smear on objects that are not moving, mushy low-detail surfaces, plastic or waxy skin, a repainted or re-imagined door or hallway, colour shift, washed-out or muddy exposure, upscaling artefacts, a dreamy or filtered look.

AUDIO RULE - THIRD MOST IMPORTANT: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

CHILDREN MOTION RULE: the children are ALREADY in full motion at the very first frame they appear. Never standing still, never posed, never frozen. They run, spin, jump and laugh continuously, with a clearly different whole-body pose every half second - arms, legs, heads and faces all changing. Eyes wide, mouths open laughing and shouting. Real children filmed on a phone, not a photograph coming to life.

TASK: image-to-video. The start image is frame 0.0s. Hold its door, hallway, forearm, geometry and materials exactly - but NOT its stillness and NOT the position of its light pattern.

[1] SUMMARY
First-person POV: a hand opens a door and walks into a Christmas living room where light is sweeping and pouring down every wall and the ceiling, two children running and laughing inside; the camera pushes in and tilts up. 4 seconds, one continuous take.

[2] GLOBAL STYLE
Real handheld phone POV walking forward. Warm dim hallway opening into a room lit only by the moving projection. Sharp, clean, correctly exposed, natural handheld bounce. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls frame 0.0s: the closed oxblood red four-panel door in its cream frame, the brass round knob on its brass escutcheon, the bare right forearm, the warm dim hallway, the wood floor and the green wreath with the red bow hanging on the door.
@Image 1 controls ONLY what is inside the room once the door is open: the room layout, the tall decorated Christmas tree against the pale plaster back wall at the centre, the pale grey sectional sofa wrapping the right foreground, the gallery landing with its glass-panelled garlanded railing on the right, the high vaulted plaster ceiling on its dark walnut rafters, the two children and their deep plum and oatmeal cable-knit knitwear, and the COLOUR and STYLE of the Christmas shapes.
@Video 1 controls ONLY how the projected light MOVES. Nothing else.
Both images are photographs - copy their look, NEVER their stillness.

[4] CHARACTERS
THE BOY - deep plum and oatmeal cable-knit Christmas jumper with soft grey knitted lounge trousers, centre of the room, running and jumping, mouth wide open laughing.
THE GIRL - matching deep plum and oatmeal cable-knit knitwear, behind him and to his left, spinning and running, laughing.
COUNT LOCK: exactly two children. No adults, no third child, no pets.

[5] LOCATION - an enormous American great room with a high vaulted cream plaster ceiling on dark walnut rafters and their collar beams: tall decorated Christmas tree against the pale plaster back wall at the centre, pale grey sectional sofa wrapping the right foreground, gallery landing with a glass-panelled garlanded railing crossing the right at mid height, tall arched window high on the right, warm oak plank floor with a large greige rug, presents under the tree. Sweeping, pouring light covers every wall AND the whole ceiling. Its coverage is dense but uneven and constantly changing, because it is moving - that is correct and expected.

[6] FIRST FRAME - exactly the start image: the door CLOSED, the hallway lit only by its own warm dim light, the bare right forearm reaching to the brass knob.

[7] TIMELINE - the light is sweeping and pouring in every single beat
0.0-1.0s - the camera is the person's own eyes. THE RIGHT HAND grips the brass knob, turns it and pushes; the door swings away from the camera and the room behind it comes into view. The projection is ALREADY running at full strength on the far wall and across the whole ceiling before the door moves - the widening doorway simply uncovers more of a display that was already there, the way drawing a curtain back uncovers a view. Nothing lights up, ignites, spreads, ripples or switches on as the door opens, and nothing glows along the edge of the door, along the door frame or in the gap.
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

#### Video prompt — `clips/v6_c05_g3.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `eb523fc7-abd5-4559-b0ec-8170814708aa`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_225058_eb523fc7-abd5-4559-b0ec-8170814708aa.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c05_g1.png` · Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4`
- image ref 1: `content/video_6_assets/references/v6_c05_r2.png` · Higgsfield media `c4fc3193-2325-46da-a3a7-0f0cc422be64`
- video ref 1: `references/scene_no_audio-5.mp4` — silenced upload padded to 4.50 s · Higgsfield media `c5b72684-3884-4e7d-8b77-7bad9f4af4cf`

````text
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s.

THE ONLY THING THIS CLIP IS FOR
The Christmas picture thrown onto the walls and the ceiling is a MOVING PICTURE. Six previous attempts failed for one reason and one reason only: the picture sat still on the plaster like printed wallpaper and drifted across the screen only because the camera was walking. That is the failure. Do not repeat it.

THE TEST THIS CLIP MUST PASS
Freeze any two frames half a second apart and line the wall up. Every shape must be somewhere different ON THE PLASTER:
- Follow one snowflake. In one second it falls a quarter of the wall's height and lands somewhere else entirely.
- Follow the sleigh and reindeer. They gallop clean across the ceiling during the clip and finish nowhere near where they started.
- Follow one chimney. A plume of smoke leaves the pot, climbs a roof-height, spreads and fades, and a fresh one starts behind it.
- Follow one aurora ribbon. A bright swell runs along its length end to end, the way a wave runs down a shaken rope.
If the shapes sit in the same spots on the wall, the clip is worthless no matter how good everything else looks.

WHAT HOLDS STILL: the room. The plaster, the rafters, the door, the floor, the furniture, the tree, the framing, the colours. The picture's outer edge stays put too - it never rotates, spins, swings or slides across the room as one sheet. Only the things INSIDE the picture travel. The moon is the single exception: it holds its place and only breathes brighter and dimmer.

@Video 1 is real footage of this projector running. Copy ONE thing from it: how restlessly its light moves. Take nothing else - not its room, not its furniture, not its people, not its framing, not its colours, not its camera move, not its lighting. It is completely silent; import no sound from it.
@Image 1 controls only what the room LOOKS like once the door is open - the layout, the tree, the sofa, the gallery landing, the vaulted ceiling, the two children, and the colour and style of the Christmas shapes. It is a photograph. Copy its look, never its stillness.

BEATS

0.0-1.0s - The right hand grips the brass knob, turns it, and pushes the door away from camera. The room behind it is ALREADY full of moving light before the door shifts - flakes pouring down the far wall, an aurora rippling, the sleigh already crossing the ceiling. The widening doorway simply uncovers more of a display that was already running, the way pulling a curtain back uncovers a view. Nothing ignites, spreads, switches on or grows as the door opens. Nothing glows along the door edge, the frame or the gap.

1.0-2.0s - The door swings wide and the camera walks through it. The flakes keep falling at exactly the rate they already had, over the far wall, over the floor ahead, over the camera's own path.

2.0-3.5s - Inside the room. THE BOY is already running across the middle, arms out, mouth open laughing, and he leaps onto the sofa cushion. THE GIRL spins on the rug behind him and to his left, hair flying. Shapes travel down the walls behind them and slide across their backs and faces as they move.

3.5-5.0s - The camera keeps walking forward and TILTS UP until the vaulted ceiling fills the top of frame. The ceiling is the BUSIEST surface in the whole clip, never the calmest: the aurora ripples along the rafters end to end, the sleigh and reindeer gallop across it, snow pours down it, the stars twinkle. THE BOY jumps again with both arms straight up; THE GIRL is still turning below.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the forward walk from 1.0s, the tilt up from 3.5s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera IS the person's eyes - no phone, screen, hand or device in frame after 1.0s.

THE CHILDREN - exactly two, no adults, no third child, no pets. Deep plum and oatmeal cable-knit knitwear. They are in full motion the instant they appear and never stand still, never pose, never freeze - a clearly different whole-body pose every half second.

SHARPNESS - hold the exact sharpness, exposure and fine detail of the start image: the floor's wood grain, the panel edges and sheen of the oxblood red door, the brass knob, the skin texture of the bare forearm, the leaves of the wreath. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle and the door swinging, children laughing and squealing, quiet room tone. NO music, no song, no score, no soundtrack, no instruments, no bells used as music.

BANNED - a projected shape that stays in the same place on the plaster; a projection that appears to move only because the camera moves; shapes that only twinkle, pulse, brighten or fade without travelling; a parked sleigh; chimneys not smoking; a still aurora; a still or empty ceiling when the camera tilts up; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam, bright line or sparkler along the door edge, frame or gap; light that grows, ignites or fills the room as the door opens; any music; blur or soft focus; children standing still or posed; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
````

#### Video prompt — `clips/v6_c05_g4.mp4`

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `4aaaa8fa-d202-48c9-90f6-67a4ff2c5066`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_230812_4aaaa8fa-d202-48c9-90f6-67a4ff2c5066.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c05_g1.png` · Higgsfield media `d58a1298-e600-423c-bb27-186c3ceac1a4`
- image ref 1: `content/video_6_assets/references/v6_c05_r2.png` · Higgsfield media `c4fc3193-2325-46da-a3a7-0f0cc422be64`

````text
TASK: image-to-video. 5 seconds. One continuous handheld phone POV take, vertical 9:16. The start image is frame 0.0s: a closed oxblood red door with a wreath, a hand on the brass knob.

THE PICTURE ON THE WALLS IS A CLOSED SET
The start image does not show the room, so read the room ONLY from @Image 1. Everything thrown onto the walls and ceiling is already drawn in @Image 1. You are not designing a projection - you are making the one in @Image 1 move. Invent nothing. If a thing is not in the list below, it does not exist in this clip.

THE COMPLETE LIST OF WHAT IS PROJECTED, AND WHAT EACH ONE DOES

Moving layer - these travel across the plaster:
- Six-point snowflakes, white and pale gold. They fall steadily and continuously down the ceiling and down both walls, top to bottom, new ones entering above as others slide out below. They never hang still.
- Candy canes, red and white striped. They drift down with the snow, tumbling slowly end over end as they go.
- Shooting stars, gold with a tail. They streak across, the tail thinning out behind them, and fade; fresh ones set off elsewhere.
- The aurora ribbons, green and pink and magenta, laid along and between the dark rafters. A bright swell runs the length of each ribbon end to end, the way a wave runs down a shaken rope, and the ribbons themselves creep sideways.
- The fine gold star specks filling the gaps. The whole field creeps slowly and the specks twinkle in and out.
- The gold line of musical notes on their staff, along the right-hand rafter. The notes travel along the staff like sheet music sliding past.
- The reindeer team and sleigh, gold, to the left of the moon. They gallop steadily across and finish a long way from where they set off.

Holding layer - these keep their exact positions and only twinkle:
- The moon, bright and full, centre right. It holds and only breathes brighter and dimmer.
- The church with the tall steeple, right of the moon. Holds; its windows twinkle.
- The snowy village houses low on the left wall. Hold; their lit windows twinkle.
- The big gold Christmas tree and the slimmer cone tree behind it on the left wall. Hold; their lights twinkle.
- The street lamps among the houses. Hold; they flicker faintly.

ADD NOTHING. No smoke and no chimney plumes of any kind. No extra buildings, no extra trees, no extra figures, no angels, no bells, no letters, no numbers, no new shapes. Nothing appears that is not on the list.

WHAT ELSE HOLDS: the real room. The plaster, the rafters, the staircase and its gallery landing, the door, the wooden floor, the rug, the sofa, the real Christmas tree and its lights, the framing, the colours. The projected picture's outer edge stays put - it never rotates, spins, swings or slides across the room as one sheet. Only the things inside it travel.

@Image 1 is the authority on the room and on every projected shape: its layout, its staircase, its furniture, its two children, and the exact set, style and colour of the projected shapes. It is a photograph - copy its look, never its stillness.

BEATS
0.0-0.8s - The hand turns the brass knob and pushes the door away from camera. Behind it the room is ALREADY running: snow already falling, the aurora already swelling, the reindeer already crossing. The widening gap simply uncovers more of something that was already going, like pulling a curtain off a window. Nothing ignites, switches on, spreads or grows as the door opens, and nothing glows along the door edge, frame or gap.
0.8-2.0s - The door swings wide and the camera walks through. The snow keeps falling at the same steady rate it already had - down the far wall, across the floor ahead, across the camera's own path.
2.0-3.3s - Inside. The two children are both already in motion and stay in motion. Projected shapes slide down the walls behind them and pass across their backs and faces.
3.3-5.0s - The camera keeps walking and TILTS UP until the rafters fill the top of frame. The ceiling is the busiest surface in the clip: snow pouring down it, the swell running along every aurora ribbon, the notes sliding along the staff, the reindeer crossing it, the specks twinkling.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. Exactly two moves: the walk from 0.8s, the tilt up from 3.3s. No cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes - no phone, screen, hand or device in frame after 0.8s.

THE CHILDREN - exactly two, both visible from 2.0s on, no adults, no third child, no pets. Deep plum and oatmeal cable-knit knitwear, as in @Image 1. They never stand still and never pose.

SHARPNESS - hold the sharpness, exposure and fine detail of the start image: the wood grain of the floor, the panel edges and sheen of the red door, the brass knob, the skin of the bare forearm, the wreath needles. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, children laughing, quiet room tone. NO music, no song, no score, no instruments, no bells used as music.

BANNED - any projected shape that is not on the list above; smoke; a shape that stays in the same place on the plaster when the list says it travels; a projection that appears to move only because the camera moves; shapes that only twinkle when the list says they travel; a parked sleigh; a still aurora; a still or empty ceiling when the camera tilts up; the whole picture rotating, spinning or sliding as one sheet; a pattern that looks printed, painted, stencilled or like wallpaper; light that moves for a moment then stops; a glow, seam or bright line along the door edge, frame or gap; light that grows or fills the room as the door opens; any music; blur or soft focus; children standing still or posed; jellyfish, fish, coral, bubbles or any underwater imagery; a room lit entirely blue; the projector unit visible; a third child; an adult; a cut; subtitles; on-screen text.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v6_c06_g2.png` → `clips/v6_c06_g1.mp4`

#### Image prompt — `starting_frames/v6_c06_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `a442c4f0-8275-4b57-9e74-d4be36837f36`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_210246_a442c4f0-8275-4b57-9e74-d4be36837f36.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `0a845da6-2607-46cc-a595-4fee4b17d6a9`
- @Image 2: `references/house_bedroom_attic.png` · Higgsfield media `14d330fa-4734-4f6f-98c6-368bb4cd0312`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its walls, its door, its windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with short straight black hair, fully dressed for winter in a warm deep plum and oatmeal cable-knit Christmas jumper with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom tucked under a clipped attic roof, the ceiling one broad FLAT panel of warm cream plaster down the middle of the room which breaks at a clean knuckle line on the left and again on the right into a short shallow plaster slope running down to a low knee wall on each side, with four small flush recessed downlights set in a loose square into the flat centre panel; the plaster is smooth and unbroken - there is NO exposed timber anywhere in this room, no rafters, no ridge beam, no collar, no king post and no tongue-and-groove boarding on the ceiling or on the walls; warm greige plaster walls with plain white skirting; the back wall carrying a reclaimed oak sliding barn door of X-braced planks hung on a black steel track with black spoked rollers, flanked on its left by a tall white-framed double-hung window with a pale linen curtain and on its right by a tall white-framed glazed door with a matching curtain, and a large green potted plant standing at the far right; a framed landscape print in a thin gold frame on the wall above the bed; a low pale oak platform bed with a wide upholstered taupe headboard, two pale oak nightstands with cream drum-shade lamps, and a pale oak bench with a woven rush seat at the foot of the bed; a pale white-oak plank floor under a very large oat flat-weave rug. Copy the proportions, the flat centre panel, the two knuckle lines, the shallow side slopes, the knee walls, the barn door and its black track, and the window and the glazed door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and both table lamps are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a red tartan quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking hangs on the wall above the headboard, a warm fairy-light garland is strung around the window, a small lit Christmas tree with antique gold and cream ornaments stands on the floor beside the bed, and a small evergreen wreath with a cream bow hangs on the barn door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, the flat cream plaster centre panel of the ceiling and both shallow plaster side slopes running down to the knee walls, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the ceiling and run with the long direction of the room instead of hanging as vertical curtains, and visibly kink and change direction at the two knuckle lines where the flat centre panel breaks into the shallow side slopes; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying flat on the centre panel so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big soft ivory full moon glowing high on the plaster wall above the sliding barn door; one big brilliant north star high on the flat centre panel of the ceiling with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across the flat centre panel and both side slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the warm cream plaster. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster, not paint and not a sticker. The light is TRANSLUCENT - the warm cream plaster and its fine surface texture, the two knuckle lines where the flat centre panel breaks into the shallow side slopes, and the four flush recessed downlights set into that centre panel, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each knuckle line breaks the light with its own soft crease where the plaster changes angle. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the flat centre panel and bending again where it runs down each shallow side slope. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster panel breaking at a knuckle line into a shallow plaster slope on each side, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with the boy's face clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v6_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `707f2010-0be0-4630-bce6-ab7fccafbf9f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215719_707f2010-0be0-4630-bce6-ab7fccafbf9f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v6_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c06_g2.png` · Higgsfield media `a442c4f0-8275-4b57-9e74-d4be36837f36`

````text
SUMMARY: a boy bounces on his bed in an attic Christmas bedroom at night while a projected snow-village picture is PLAYING across the left wall and the whole plaster ceiling, thrown there by a projector standing on the floor. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the attic bedroom, the flat plaster centre panel and its two knuckle lines, the bed with its red tartan quilt and cream cable-knit throw, the wide upholstered taupe headboard, the sliding barn door, the small lit Christmas tree, the large oat flat-weave rug, the window with its garland, the stocking, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child in a deep plum and oatmeal cable-knit Christmas jumper and soft grey knitted lounge trousers, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the wall and the whole plaster ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene that cone is playing: snow-covered gabled cottages with lit windows and fir trees low on the LEFT wall, plumes above their chimneys, ribbons of aurora arching across the flat centre panel and both shallow side slopes of the ceiling, a sleigh drawn by reindeer keystoned across the ceiling at the upper left, a big pale moon over on the right, a dense field of gold stars of many sizes, and a heavy fall of small glowing six-point snowflakes and points of light in red, green, blue, gold and white.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every cottage chimney on the left wall is smoking. Each plume climbs upward out of its chimney pot, leaning slightly to the right, rising about one cottage-roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh plume forms at the pot behind it. The plumes are never a fixed painted shape.
- THE AURORA - each ribbon ripples ALONG ITS OWN LENGTH, a slow travelling wave running from one end of the ribbon to the other, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall arc stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling away from the upper left corner where it sits in the start image, toward the far side of the ceiling, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, and the whole team rises and dips a little as it goes.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts, breathes brighter and dimmer on its own timing, and cycles slowly through red, green, blue and gold. One that reaches the skirting board fades out there while a fresh one fades in high near the knuckle line, so the density holds even. Track this one so the fall is unmistakable: a large white six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.0s and fades out low near the skirting at 4.0s.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE MOON - the moon is the ONE element that holds its position. It stays exactly where it is on the right for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE:
0.0-1.5s the camera holds still. THE BOY bends his knees and pushes off the mattress; both feet leave the duvet, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
1.5-2.5s the camera still holds. He lands on both feet and drives straight into a second, higher jump, knees tucking.
2.5-4.0s the camera tilts up in one slow smooth move until the plaster ceiling fills the upper half of the frame, the aurora rippling along the flat centre panel and both shallow side slopes and the sleigh still flying across it. THE BOY stays low in frame, still bouncing.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes one move only, a tilt up at the end. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; blur; a cut; on-screen text; subtitles.
````

**Other takes of C06 on disk (1)**

#### Image prompt — `starting_frames/v6_c06_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `abdf9332-5e41-4966-9b60-cbf747f02be3`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_182327_abdf9332-5e41-4966-9b60-cbf747f02be3.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `0a845da6-2607-46cc-a595-4fee4b17d6a9`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about six with short straight black hair, fully dressed for winter in a warm deep plum and oatmeal cable-knit Christmas jumper with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. A classic American child's bedroom tucked under the roof: a low sloped ceiling on both sides clad in warm oatmeal painted tongue-and-groove boards with dark stained exposed rafters running up to a dark stained ridge beam, deep green painted panelling on the knee wall below, a small cream-trimmed dormer window with a dark snowy night outside and a warm fairy-light garland around it, a low antique brass bed set against the knee wall made up with a red tartan quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking pinned to the rafter above the headboard, a small lit Christmas tree standing on the floor beside the bed, a faded antique Persian runner on dark stained oak floorboards, and a low dark green bookshelf of picture books tucked under the slope.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, both painted sloped ceiling planes and the dark rafters, wrapping around the corner where wall meets slope without a break, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction where the two sloping halves of the ceiling meet at the ridge beam; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the slope above the dormer window; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm, drifting across both slopes; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the painted boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on a real boarded surface, not paint and not a sticker. The light is TRANSLUCENT - the painted boards, their seams and their subtle grain, and every dark stained rafter and the ridge beam, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the rafters and the ridge beam break the light with their own hard shadow lines where they stand proud of the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the two sloping planes and bending sharply at the ridge line. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare board. Even packed full, the ceiling must still read unmistakably as two sloping boarded planes meeting at a ridge beam, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The dark oak floorboards, the Persian runner, the bed and its covers and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with the boy's face clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v6_c07_g2.png` → `clips/v6_c07_g1.mp4`

#### Image prompt — `starting_frames/v6_c07_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `1d555499-7849-4f47-8643-8c00f25bd280`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_210246_1d555499-7849-4f47-8643-8c00f25bd280.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `c9a6740d-383b-4829-a7b9-f7a3c079c03f`
- @Image 2: `references/house_great_room_trusses.png` · Higgsfield media `1d79cde5-c6a5-4259-b414-2b0d4bd8434b`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its ceiling, its rafters, its walls, its stair, its railings and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long black hair tied in a low ponytail, the boy is about five with short black hair. Both are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: an enormous double-height great room whose ceiling is a cathedral vault of smooth cream plaster in two long slopes meeting at a ridge that runs away from the camera, crossed by two pairs of dark walnut-stained timber rafters, each pair rising as an inverted V to meet at the ridge with a matching collar beam below it, and small recessed downlights set flush into the plaster between them; a first-floor gallery landing crossing the right-hand half of the room at mid height, its railing made of clear glass panels held in slim black metal posts under a dark timber top rail; an open-tread pale oak staircase descending from that landing towards the camera with the same glass-and-black-post railing and black wall sconces on the wall beside it; a tall arched window with dark muntins set high on the right above the stair; a pale plaster back wall at the centre carrying a black arched double glazed door of many small panes; and along the left an open kitchen with pale oak slab cabinetry, a full-height integrated cabinet run, a cream island with a stone waterfall front, four woven rattan counter stools and two big woven rattan dome pendants hanging on long black cords. Wide warm oak plank floor, a large pale grey sectional sofa wrapping the right foreground, a round dark-stained wood coffee table and a large greige rug. Copy the proportions, the rafter pairs, the ridge, the glass railing, the stair and the arched door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the arched window and the glazed door show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every downlight, pendant and sconce in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the pale plaster back wall beside the arched door with warm white lights and antique gold and cream ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and antique gold ribbon wound along the gallery railing and down the stair rail, cream knitted stockings hanging from the gallery rail, and a large evergreen wreath with a cream bow on the arched door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey pale plaster back wall, the plaster walls either side of it, the whole high vaulted plaster ceiling, the dark walnut rafters and their collar beams and the underside and railing of the gallery landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the rafters instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the plaster wall above the gallery landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the pale plaster and the dark walnut rafters. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real timber, not paint and not a sticker. The light is TRANSLUCENT - the plaster and its fine surface texture, and every dark walnut rafter, every collar beam and the ridge line of the vault, all stay clearly visible THROUGH the coloured light, and the rafters and the collar beams break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full it must still read as projected light on a real plastered vault with real timber rafters crossing it, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The warm oak floorboards, the greige rug, the grey sectional sofa, the round coffee table and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v6_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `11f7e62d-f275-486b-bb47-0bf465dec8e1`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_215719_11f7e62d-f275-486b-bb47-0bf465dec8e1.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v6_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_6_assets/starting_frames/v6_c07_g2.png` · Higgsfield media `1d555499-7849-4f47-8643-8c00f25bd280`

````text
SUMMARY: two children play in a double-height Christmas great room while a projected snow-village picture is PLAYING across the back wall and the whole vaulted plaster ceiling and its dark timber rafters, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the dark walnut rafters and their collar beams, the open-tread pale oak staircase and its garlanded glass railing on the right, the tall arched window high on the right with snow outside, the pale plaster back wall with its black arched glazed door and wreath, the lit Christmas tree with its presents, the pale grey sectional sofa, the round dark wood coffee table, the greige rug, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - on the rug at the front left, back to camera, facing the wall, turning on the spot with his arms out.
THE OTHER CHILD - standing up on the sofa cushions in front of the garlanded staircase on the right, back to camera, with both arms raised toward the wall, bouncing on the spot.
Both in deep plum and oatmeal cable-knit Christmas jumpers and soft grey knitted lounge trousers. Exactly two children. No third child, no adult, no pet.
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

#### Image prompt — `starting_frames/v6_c07_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `b21a64ba-a6bf-49ab-b1b1-d8af07925429`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260919_184014_b21a64ba-a6bf-49ab-b1b1-d8af07925429.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `c9a6740d-383b-4829-a7b9-f7a3c079c03f`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with long black hair tied in a low ponytail, the boy is about five with short black hair. Both are fully dressed for winter in warm deep plum and oatmeal cable-knit Christmas jumpers with a cream snowflake yoke across the shoulders, matching soft grey knitted lounge trousers and thick red knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. An American lodge double-height great room: one enormous two-storey chimney breast of reclaimed red brick running the full height of the space with a chunky dark stained timber mantel and cream knitted stockings, deep forest green painted walls either side of it with cream trim, a mezzanine landing with a black wrought iron rail crossing high across the room with an open dark stained staircase rising to it on the right, exposed dark stained king-post roof trusses under a high vaulted oatmeal boarded ceiling, tall cream-trimmed sash windows on the left showing a dark blue snowy night, dark stained oak floorboards with a large faded antique Persian rug, a long deep oxblood red sectional sofa with antique gold cushions, a leather ottoman, and a very tall real Christmas tree standing against the brick with warm white lights, antique gold and cream ornaments and wrapped gifts beneath it.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire two-storey red brick chimney breast, the painted walls, the whole high vaulted boarded ceiling, the exposed king-post trusses and the underside and railing of the mezzanine landing, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. Built in layers, all of them present at once: LOW ALONG THE WALLS, a snow-covered village at night - rows of little gabled cottages with warm gold lit windows, a church steeple, thin curls of chimney smoke, snow-laden pine trees along the lanes, a tiny frozen pond, all glowing warm gold and cream, and rising out of the middle of the village one enormous glowing gold Christmas tree of light climbing the full height of the wall above the rooftops, its branches hung with big ornate baubles that turn slowly on their threads and a bright star at its crown; ABOVE THE VILLAGE, wide soft aurora ribbons in warm gold, emerald green and deep rose sweeping up the walls in long slow curves and carrying over onto the ceiling as five or six broad overlapping bands layered over each other so there is very little bare ceiling left between them, where they lie flat ALONG the slope and run with the direction of the boards instead of hanging as vertical curtains, and visibly kink and change direction at the ridge; ACROSS THE CEILING OVERHEAD, Santa's sleigh drawn by a team of eight flying reindeer, seen side-on in glowing warm gold, large enough to read the antlers, the harness and the curved front of the sleigh, with a long bright tapering trail of light streaming behind the runners, the whole team lying on the sloping plane so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes towards the ridge; a big soft ivory full moon glowing high on the brick above the mezzanine landing; one big brilliant north star high near the ridge with long rays spreading out of it; a dense field of warm gold five-point stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in warm gold and cream at several different sizes, the nearest big enough to read every arm; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam; and layered through all of it, long ribbons of glowing gold bunting and glowing red-and-cream striped candy canes turning slowly end over end as they drift, a wide sweeping arc of glowing gold musical notes and tiny bells curving across the upper wall, huge ornate six-point ice crystals the size of a dinner plate each faceted with fine internal lines turning slowly as they cross the ceiling, and a second deeper shoal of tiny stars far behind the first so the whole field has real depth. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS WARM: warm gold, cream white, deep Christmas red, emerald green and soft rose, richly saturated against the red brick and the oatmeal boards. NO cold colours - no cyan, no teal, no electric blue, no violet, no grey. It must NOT look like outer space, a nebula, a galaxy, a spiral vortex, a tunnel or anything science-fiction, alien or dystopian - it is a warm storybook Christmas night sky. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real brick and real boards, not paint and not a sticker. The light is TRANSLUCENT - every individual reclaimed brick and its mortar joints, and the boards, seams and dark trusses of the ceiling, all stay clearly visible THROUGH the coloured light, and the trusses and the mantel break the light with their own hard shadow lines where they stand proud. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare brick and bare board. Even packed full it must still read as projected light on a real textured surface, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The dark oak floorboards, the Persian rug, the oxblood sectional sofa, the ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````
