# Video 10 - prompts archive

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_10.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

*Product:* THEXMASGLOW - CHRISTMAS PROJECTOR  
*Round:* 2026-09-20  
*Scope:* B-roll C02 to C07 generated first; the **C01 hook was added later on 2026-09-20** in the v7/v8/v9/v10 hook round, then revised the same day - see the C01 section below.

## Planned cut

| card | section | shot |
|---|---|---|
| C02 | B-roll 1 - the unbox | hands on the closed carton |
| C03 | B-roll 1 - the unbox | the dome lifted onto the counter |
| C04 | B-roll 1 - the unbox | the cable going in |
| C05 | B-roll 2 - the reveal | F1 the closed door, F2 the room behind it |
| C06 | B-roll 2 - the reveal | the child in bed under the running ceiling |
| C07 | B-roll 2 - the reveal | the two children in the middle of the great room |

## Brief as given

> They camed out good. Now I want you to make me the broll images for the next 2
> videos. The same way you did for the last ones.
>
> Just change the doors, houses, animations, tables, kids. Make shure the ceiling of
> the rooms it's looking real in terms of shape and it makes sense.
>
> I want the animation on the walls and ceiling to be even more impressive and wow.
> I attached you some reference images make shure they are are looking perfect on
> the walls and ceiling
>
> All the images must be extremly high quality, perfect light, iphone shots, nothing
> blurish. Use gpt image 2.5 Sunburst, 2k, mid quality settings, 9x16.

## Look pack chosen

Nantucket coastal cottage. Limed oak, walnut butcher-block, oxblood red, sage green and cream. Distinct from v2-v9 in every slot Daniel named.

| slot | v10 |
|---|---|
| sleeve | deep burgundy wool |
| C02 table | limed white oak, pale blond timber with the open grain filled chalky white, dead matte, simple square edge |
| C02 background | chalk-white painted shiplap walls, chalk-white painted brick fireplace with a pale oak mantel, cream knitted stockings, antique gold and pearl-white ornaments on the tree |
| C03/C04 counter | end-grain walnut butcher-block, chalk-white zellige tile backsplash |
| C03/C04 kitchen | coastal cottage kitchen - LEFT in C03, RIGHT in C04 |
| C05 F1 door | classic American four-panel door in deep oxblood red eggshell, two tall panels below and two short above |
| knitwear | sage-green and cream nordic with a row of cream fir trees across the yoke, charcoal knitted lounge trousers, thick mustard socks |
| C06 child | boy, about 7, short sandy-blond hair |
| C07 children | girl about 8 with short dark curly hair, boy about 5 with straight black hair |
| C05 F2 + C07 room | tall great room under a single-slope shed ceiling of narrow white T&G raking to a high eaves, three slim black steel tie rods, tall black glazed gable, forest-green slab kitchen on the left |
| C06 room | bedroom with a flat tray ceiling - one rectangle recessed into flat cream plaster with an angled reveal, downlights in the flat border, two double-hung windows with cream pinch-pleat curtains |

## The projection - rebuilt from Daniel's four reference screenshots

This is the largest change in the round and the one most worth his eye. Daniel attached four screenshots of real projector output and said the animation on the walls and ceiling must be "even more impressive and wow" and must look like them. The projection paragraph was therefore **not** carried over from v8. It was rewritten from what is actually in those four pictures, in this order:

1. a snow-laden pine forest running along the bottom of the wall
2. an ornate gilded fairy-tale Christmas city of spires and onion domes on the left, every window lit gold
3. a lit steam train of eight gold-windowed carriages crossing on the right
4. wide aurora ribbons in emerald green, rose magenta, warm gold and soft teal
5. one colossal spiral whirlpool of seven concentric rings drawing in to a white-gold core
6. Santa's sleigh and eight reindeer sweeping out of the spiral's mouth on a trail of gold
7. a pale blue cratered moon with a tiny second sleigh crossing its face
8. floating wrapped gifts at five or six depths
9. a dense star field with shooting stars, large six-point snowflakes, glowing cloud wisps
10. a heavy fall of tiny light points over the whole surface

### Two standing bans were deliberately lifted

Both of these ran through v1-v8 and both are **gone in v9 and v10**, on purpose, because Daniel's own references break them:

| ban that was lifted | why |
|---|---|
| `NO cold colours - no cyan, no teal, no electric blue, no violet, no grey` | his references are emphatically multicoloured - emerald, magenta, teal and a pale blue moon are the loudest things in all four pictures |
| `must NOT look like ... a spiral vortex` | the spiral whirlpool is the centrepiece of two of the four references |

The anti-sci-fi guard rail was **kept**, reworded so it still fires: the spiral must read as *an AURORA WHIRLPOOL made of Christmas light with a sleigh flying out of its mouth, not a space nebula*.

If Daniel wants the old warm-gold-only look back, that is one line to restore - say so and it goes back.

### The ceiling was made structurally honest

He asked that "the ceiling of the rooms it's looking real in terms of shape and it makes sense". Every B-roll 2 prompt now carries a dedicated `HOW THE LIGHT SITS ON THE CEILING` block (or `... ON THE SURFACES` for C07) that ties the projection to the actual built geometry of that room: which timbers it crosses, where it has to break and step, where it distorts across an angled reveal or a curved vault, and what it reads as from the floor. The projection can no longer float free of the ceiling it is supposedly landing on.

## Settings

`gpt_image_2_5 - variant sunburst - quality medium - resolution 2k - aspect_ratio 9:16 - count 1 - use_unlim false` - output 1520 x 2688. Workspace Oneofone1.

## Lineage

All seven frames are reused from **v8**. v8 is the most recent complete B-roll set and the one Daniel signed off with "they camed out good", so it is the correct base.

Per CLAUDE.md rule 3 every source paragraph was pasted byte-identically and only the nouns that physically differ were changed. The builder asserted a single match on every substitution, so untouched text is verified identical, not assumed identical. The paragraph diff below is the proof:

```
c02      identical: [0,5,6,7]              changed: [1,2,3,4]
c03      identical: [0,1,2,3,5,6,9,10]     changed: [4,7,8]
c04      identical: [0,1,2,6,7]            changed: [3,4,5]
c05_f1   identical: [0,3,4,6,7,8]          changed: [1,2,5]
c05_f2   identical: [1,7,8,9]              changed: [0,2,3,4,5,6]
c06      identical: [1,7,8,9]              changed: [0,2,3,4,5,6]
c07      identical: [1,7,8,9]              changed: [0,2,3,4,5,6]
```

Every camera paragraph, every pose paragraph, the projector-not-visible paragraph, the quality paragraph and the no-text paragraph are byte-identical to v8.

---

## C01 - Under the tree in the stair hall

*Section:* Hook
*Status:* REVISED - g3/g4 GENERATED FOR REVIEW
*Defect note:* this C01 section was written on 2026-09-20 but never landed in this file - it was authored as a fresh `prompts.md` while this archive already existed at 67 KB with C02-C07, so the write did not merge. Recovered and inserted here.
*What it is:* the "Christmas Decor In 1965" stair-hall screenshot copied exactly, with the boy on the stairs replaced by a mother and two children standing on the hall floor.

- frames: `v10_c01_g1.png`, `v10_c01_g2.png` (right hall, wrong placement), `v10_c01_g3.png`, `v10_c01_g4.png` (mother on the stairs)
- clips: none yet

*Copied from* the reference Daniel attached (his "3rd image attached") - changed: (a) the staircase is emptied, the boy leaning over the railing and the man at the lower left are both gone; (b) a mother and two children in American-flag Christmas pyjamas stand on the hall floor; (c) a modest United States flag added to the left wall. The hall, the camera position, the perspective, the staircase, the newel post, the nutcracker, the doorway, the ceiling fan, the floor and the tree with its full dressing are all held to the reference.

*Read as:* "a christmas flag in the background (not too big)" was read as the **United States flag**, poster-sized, matching the explicit "usa flag" in the video 8 brief and the flag in v6 C01 g4. Flagged to Daniel.

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `references/v10_c01_r1.png` | owns everything - the hall, the camera position, the perspective, the staircase and the tree |

media id `c39519a8-920d-46b9-ba05-dbffde968da0`

**Prompt - option A** (`v10_c01_g1.png`) - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `a34b4b1f-6668-4be9-91e2-b4b8eff7eca9`

The trio stands at the bottom left in front of the tree, faces visible, heads tipped back. Mother mid 30s with long light brown hair, girl about 8, boy about 5.

```text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: there is NO ONE on the staircase. Nobody is leaning over the railing, nobody is standing on the treads, the whole staircase is empty. The man standing at the lower left of the reference is gone too. In their place, standing together on the hall FLOOR at the bottom left of the frame in front of the tree, small in the frame because they are far below the top of the tree: a mother in her mid 30s with long light brown hair, and two children - a girl about 8 with long wavy brown hair and a boy about 5 with short sandy hair. All three stand on the floor looking up at the top of the tall tree, heads tipped back, the mother with one hand resting on the boy's shoulder. They are clearly on the ground floor, not on the stairs. Their heads reach only a little way up the tree, so the tree still towers over them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks on the wood floor.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind and above the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, the same gold star tilted at the very top, the same wrapped presents piled at its base.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
```

**Prompt - option B** (`v10_c01_g2.png`) - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `dd2ab4c7-a128-4b7a-8708-2074098b7e08`

The trio is seen **from behind**, directly in front of the tree at the bottom of the frame. Mother late 20s with a low ponytail, boy about 9, girl about 4.

```text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: there is NO ONE on the staircase. Nobody is leaning over the railing, nobody is standing on the treads, the whole staircase is empty. The man standing at the lower left of the reference is gone too. In their place, standing together on the hall FLOOR at the bottom of the frame directly in front of the tree with their backs to the camera, small in the frame because they are far below the top of the tree: a mother in her late 20s with dark brown hair in a low ponytail, and two children - a boy about 9 with short dark hair and a girl about 4 with short blonde hair. All three are seen from behind, standing on the floor with their heads tipped back looking up at the top of the tall tree, the mother holding the little girl's hand. They are clearly on the ground floor, not on the stairs. Their heads reach only a little way up the tree, so the tree still towers over them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks on the wood floor.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, the same gold star tilted at the very top, the same wrapped presents piled at its base.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
```

*Difference between the two:* A puts faces in the shot, which reads warmer and gives a reaction to cut to. B is backs-to-camera, which keeps the tree the undisputed subject and matches the "looking up at the impossible tree" read of the original screenshot more closely. B also avoids any face-consistency problem if this trio has to recur in the B-roll.

### Revision round - 2026-09-20

Daniel on g1/g2: *"both of the images are really good, but you didn't get one thing right, the mom
should be on the stairs over the railing, look again at that reference image I gave you, try to set
up a christmas decoration at the top of the christmas tree. 2 more generations"*.

The original brief - *"the boy on the stairs will be replaced with a mom and 2 kids down the
stairs"* - was read as *all three on the floor with the staircase emptied*. It meant the opposite:
the mother **takes the boy's exact place on the stairs**, leaning out over the black wrought-iron
railing, and the two children are the ones down on the floor. Re-read `references/v10_c01_r1.png`
and that is unambiguous - the boy is up on the upper run, chest over the rail, reaching toward the
tree.

`p10g1` and `p10g2` were pasted byte-identically and only the people paragraph plus three supporting
lines were touched:

1. `THE PEOPLE - REMOVE AND REPLACE` - the mother now occupies the boy's position, height, distance
   and size in frame, one hand on the rail, the other arm stretched across the gap to the treetop
   holding the topper. The two children stand on the hall floor below, small because they are far
   below the top of the tree, heads tipped back. The man at the lower left is still gone.
2. `with thick cream wool socks on the wood floor.` became `with thick cream wool socks.` - she is
   not on the floor any more.
3. The tree paragraph: the reference tree already wears a gold star, which contradicts a mother in
   the act of placing one. The treetop is now stated as **BARE**, with the gold star topper in her
   outstretched hand, held clear of the highest tip and not yet fixed to it.
4. The caption band exclusion list gained `of the mother's outstretched arm,` so the new pose cannot
   invade the top eighth.

Everything else - the copy-the-reference-exactly opening, the clothes, the flag, `FRAMING`,
`COLOUR`, `LIGHTING AND QUALITY` - is g1/g2 text unchanged.

*Reused from v10 C01 g1 and g2 - changed: the mother moves from the hall floor to the boy's position
on the stairs over the railing and is now placing the topper, the treetop is stated bare with the
star in her hand, and her arm is added to the caption-band exclusion list. g3 continues g1 (faces to
camera), g4 continues g2 (children from behind).*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `references/v10_c01_r1.png` | owns everything - the hall, the camera position, the perspective, the staircase and the tree, and now also the mother's exact position on the stairs |

media id `c39519a8-920d-46b9-ba05-dbffde968da0`

**Prompt - g3** (`v10_c01_g3.png`) - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `2556cc64-088b-4890-86bb-e0040fe24a54`

Continues g1: mother mid 30s with long light brown hair tied back; the girl about 8 and boy about 5
stand at the bottom left facing into the frame, faces visible, the girl's hand on the boy's shoulder.

```text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: the boy who is up on the staircase in the reference is replaced by a MOTHER in exactly his position, at exactly his height on the stairs, at exactly his distance from the camera and exactly his size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother in her mid 30s with long light brown hair tied back. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom left of the frame in front of the tree, small in the frame because they are far below the top of the tree, two children - a girl about 8 with long wavy brown hair and a boy about 5 with short sandy hair - stand on the floor looking up at their mother and at the top of the tall tree, heads tipped back, the girl with one hand resting on the boy's shoulder. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind and above the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
```

**Prompt - g4** (`v10_c01_g4.png`) - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `29aecf91-e6ec-44b2-aac0-c176bc6a9faf`

Continues g2: mother late 20s with a low ponytail; the boy about 9 and girl about 4 seen from behind
directly in front of the tree, the boy holding her hand, both heads tipped back.

```text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: the boy who is up on the staircase in the reference is replaced by a MOTHER in exactly his position, at exactly his height on the stairs, at exactly his distance from the camera and exactly his size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother in her late 20s with dark brown hair in a low ponytail. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom of the frame directly in front of the tree with their backs to the camera, small in the frame because they are far below the top of the tree, two children - a boy about 9 with short dark hair and a girl about 4 with short blonde hair - are seen from behind, standing on the floor with their heads tipped back looking up at their mother and at the top of the tall tree, the boy holding the little girl's hand. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
```

*Difference between g3 and g4:* g3 gives faces and a reaction to cut to. g4 keeps the children as
silhouettes looking up, which holds the tree and the reaching mother as the whole subject and matches
the original screenshot's read more closely.

### Revision round 2 - 2026-09-20

Daniel on g3/g4: *"g4 it's good, but the kids should be more on the right, not right in front of
the kids because when we will animate the image the women will fall over the tree - one more
generation"*.

The second "kids" is the tree. The children were sitting directly under the tree, in the exact
patch of floor the mother lands on when she goes over the railing, which would read as her falling
onto them. One generation, one change.

`p10g4` was pasted byte-identically and exactly one clause was touched - the children's position:

```
at the bottom of the frame directly in front of the tree with their backs to the camera
->
at the bottom of the frame over to the RIGHT side of the frame, well clear of the tree and NOT in
front of it - the floor directly in front of the tree's base is left completely empty - with their
backs to the camera
```

Nothing else moved. Same camera, same 1965 stair-hall staging, same mother over the rail, same
topper, same flag, same caption band, same colour and lighting blocks. The empty floor at the base
of the tree is now written into the prompt as a positive requirement, because that is the landing
zone the animation needs.

*Reused from v10 C01 g4 - changed: the two children move to the right of the frame, clear of the
tree, leaving the floor at its base empty for the fall.*

**References attached**

```
1  v10_c01_r1.png   the 1965 stair-hall reference - media c39519a8-920d-46b9-ba05-dbffde968da0
```

**Prompt - g5** (`v10_c01_g5.png`) - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `15d71118-2cbd-4f84-9212-72a89f89bd5d`

```text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: the boy who is up on the staircase in the reference is replaced by a MOTHER in exactly his position, at exactly his height on the stairs, at exactly his distance from the camera and exactly his size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother in her late 20s with dark brown hair in a low ponytail. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom of the frame over to the RIGHT side of the frame, well clear of the tree and NOT in front of it - the floor directly in front of the tree's base is left completely empty - with their backs to the camera, small in the frame because they are far below the top of the tree, two children - a boy about 9 with short dark hair and a girl about 4 with short blonde hair - are seen from behind, standing on the floor with their heads tipped back looking up at their mother and at the top of the tall tree, the boy holding the little girl's hand. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
```

### Revision round 3 - 2026-09-20

Daniel on g5: *"only for video 10 needs one more regeneration. Use the exact same prompt, It just
camed out a little weird on one stair but in rest it's perfect"*.

A straight re-roll, not an edit. The prompt is `p10g5` **byte for byte** - same text, same single
reference, same settings. Nothing was reworded to "fix" the stair: he approved the composition and
asked for another take of it, and rewriting geometry he has already signed off is exactly the drift
this file exists to prevent.

*Reused from v10 C01 g5 - changed: nothing. Re-roll of the identical prompt for a cleaner staircase.*

**References attached**

```
1  v10_c01_r1.png   the 1965 stair-hall reference - media c39519a8-920d-46b9-ba05-dbffde968da0
```

**Prompt - g6** (`v10_c01_g6.png`) - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `3084e67e-22fa-4cf6-9a21-bdd9957c0e1e`

Byte-identical to g5.

```text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: the boy who is up on the staircase in the reference is replaced by a MOTHER in exactly his position, at exactly his height on the stairs, at exactly his distance from the camera and exactly his size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother in her late 20s with dark brown hair in a low ponytail. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom of the frame over to the RIGHT side of the frame, well clear of the tree and NOT in front of it - the floor directly in front of the tree's base is left completely empty - with their backs to the camera, small in the frame because they are far below the top of the tree, two children - a boy about 9 with short dark hair and a girl about 4 with short blonde hair - are seen from behind, standing on the floor with their heads tipped back looking up at their mother and at the top of the tall tree, the boy holding the little girl's hand. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
```

### Revision round 4 - 2026-09-20

Daniel: *"Remake it, I changed my mind, I don't want the kids in that side on the stairs, put them
into the left side"*.

The children were on the right, which is the staircase side - the newel post and the bottom of the
flight are in that corner, so they were crowding the stairs. They move to the left instead, the
open side of the hall.

`p10g5` was pasted byte-identically and exactly one clause was touched:

```
over to the RIGHT side of the frame, well clear of the tree and NOT in front of it
->
over to the LEFT side of the frame, on the opposite side of the picture from the staircase and the
newel post, well clear of the tree and NOT in front of it
```

The empty floor at the base of the tree is still written in as a positive requirement, so the
mother's landing zone survives the move. Nothing else changed - same camera, same 1965 staging,
same mother over the rail, same topper, same flag, same caption band, same colour and lighting.

*Reused from v10 C01 g5 - changed: the two children move from the right of the frame to the left,
off the staircase side.*

**References attached**

```
1  v10_c01_r1.png   the 1965 stair-hall reference - media c39519a8-920d-46b9-ba05-dbffde968da0
```

**Prompt - g7** (`v10_c01_g7.png`) - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `ff02562a-4709-4fc1-bade-56457b3e7817`

```text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: the boy who is up on the staircase in the reference is replaced by a MOTHER in exactly his position, at exactly his height on the stairs, at exactly his distance from the camera and exactly his size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother in her late 20s with dark brown hair in a low ponytail. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom of the frame over to the LEFT side of the frame, on the opposite side of the picture from the staircase and the newel post, well clear of the tree and NOT in front of it - the floor directly in front of the tree's base is left completely empty - with their backs to the camera, small in the frame because they are far below the top of the tree, two children - a boy about 9 with short dark hair and a girl about 4 with short blonde hair - are seen from behind, standing on the floor with their heads tipped back looking up at their mother and at the top of the tall tree, the boy holding the little girl's hand. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
```

---

### Video prompt - `clips/v10_c01_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 1080p - 9:16 - 5s - count 1 - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c01_g7.png` - Higgsfield media `d64272c4-b6bc-4114-8742-743cf9958aff`
**Extra references** - the motion reference clip as `video_references` - Higgsfield media `5bc86b80-fbd2-43a2-90dd-53ef8aa2df00`. See the provenance block below.
**Job** - `f5d28b26-a436-49fa-97d5-f80444c846fe`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_171641_f5d28b26-a436-49fa-97d5-f80444c846fe.mp4

**Lineage** - New prompt, not a reuse. Written to Daniel's brief of 2026-09-20 plus the attached motion reference: held iPhone shot, no zooms no cuts, first second she tries to set the star on top of the tree, then she falls to the ground, the kids move aside so the tree doesn't fall on them, 5s, "exactly like this attached video".

MOTION REFERENCE PROVENANCE. Daniel attached `scene-1.mp4` (1080x1920, hevc + aac, 2.933s, 30fps, md5 `44492538bc41c1c5701e8f314f15c1a0`). This is NOT the same file as the pre-existing `video_2_assets/references/v2_c01_r2.mp4` (formerly `scene-1.mp4`) (md5 `b1a1ac6ded7c5563a4c838c1f5c28960`) - they share a filename only.

A seedance video reference imports its audio track and this one has an aac bed, so a silenced h264 copy was built and uploaded instead:

```
ffmpeg -v error -y -i scene-1.mp4 -an -c:v libx264 -preset slow -crf 18 \
  -pix_fmt yuv420p -movflags +faststart v10_motion_ref_silent.mp4
```
1080x1920, 30fps, 2.934s, no audio stream, 2,507,533 B, md5 `a6aa2d127a552ba4ed5adc9bbde42be0`.
Uploaded as Higgsfield media `5bc86b80-fbd2-43a2-90dd-53ef8aa2df00`.

The silenced copy is NOT stored on this drive: `NAMING.md` allows only `.png` in `references/`, so an `.mp4` reference has no legal filename. Re-creating this shot needs the Higgsfield media id above, or the ffmpeg line above re-run on Daniel's original attachment.

BEAT MAP read off the reference frame by frame (n/10 s): 0.0-0.9s she leans over the stair railing working at the top of the tree; 0.9-1.4s her weight goes onto the tree and it starts to tip; 1.4-1.8s the tree topples diagonally and the star snaps off; 1.8-2.2s she comes down with it and lands, ornaments bursting free and rolling toward camera; 2.2-2.9s she lies across the fallen tree, ornaments still rolling, camera holds. The output timeline is this map stretched to 5s.

A caption is burned into the reference picture, which is why the prompt opens with a HIGHEST PRIORITY block banning every visual import from `@Video 1` and repeats `No subtitles`. The children moving LEFT (Daniel's correction on `g7`) is written into the 1.0-1.6s beat.

```
HIGHEST PRIORITY, READ THIS FIRST: @Video 1 is a motion reference only. Copy its timing, its physics and the way the tree goes over — nothing else. Do NOT copy anything visual from it: not its room, not its people, not its clothes, not its colours, and above all not the text caption burned into its picture. No subtitles, no captions, no on-screen words anywhere in the output. Every person, surface and object in the output comes from the start frame.

Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the hallway floor holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the staircase behind the dark wooden railing, leaning out over it with one arm stretched up to the gold star on top of the tall decorated Christmas tree beside the stairs. Two small children in matching American-flag pajamas stand on the floor at the lower left of the frame with their backs to the camera, watching her. Wrapped presents at the foot of the tree.

ACTION TIMELINE:
0.0–1.0s — Both hands now on the gold star, she works it down onto the top of the tree, stretching further and further out over the railing, more and more of her weight going onto the tree itself.
1.0–1.6s — The tree tips. It leans away from the stairs toward the open floor and keeps going, and she loses her balance and comes over the railing with it, still holding on. At the same instant the two children take three quick steps further to the left, well out of the way, and stop there — the tree never comes near them.
1.6–2.4s — The whole tree swings down diagonally across the frame and crashes flat onto the wooden floor, branches flattening, the gold star snapping off the top and skittering away on its own.
2.4–3.2s — She lands on the floor face-down across the fallen tree, and the impact bursts a wave of ornaments off the branches — dozens of red, gold, pink and white baubles bouncing out low across the wooden floor and rolling toward the camera, spreading right across the bottom of the frame.
3.2–5.0s — The last ornaments wobble to a stop on the floor. She lies still across the fallen tree for a beat, then lifts her head, blows the hair out of her face and starts laughing. The two children stay where they moved to on the left, staring at the mess. End frame: the tree flat on the floor, ornaments scattered everywhere, her looking up laughing.

AUDIO: her real voice, lip-synced, matching her appearance — a short yelp as she goes over, then breathless laughing at the end; the dry rush of the tree branches going over; the heavy thud of the tree hitting the wooden floor; dozens of glass and plastic ornaments clattering, bouncing and rolling on hard wood; one small surprised squeal from a child. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip, and the two children keep exactly the same clothes and size. The hallway stays pixel-faithful to the start frame — same staircase, same dark wooden railing and newel post, same American flag on the wall, same wooden floor, same daylight. The children are never touched by the tree and are never underneath it. Real weight and gravity — the tree topples on its own mass and stops on the floor, she drops straight down, nobody is thrown or launched. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
```

*Submission note: the first batch attempt for this index came back `submission_failed` with "Preset "IN THE DARK" was recommended instead of submitting a job". Resubmitted byte-identically with `declined_preset_id = 24bae836-2c4a-48e0-89b6-49fcc0b21612`.*

### Video prompt - `clips/v10_c01_g2.mp4` (take 2)

Daniel on take 1: *"Camed out very bad, the ai kinda combined these 2 clips. This time don't add any reference video."*

**Lineage** - Reused from v10 C01 take 1 - changed: the video reference is gone. The whole opening `HIGHEST PRIORITY, READ THIS FIRST: @Video 1 is a motion reference only...` paragraph is deleted and NO `video_references` media was attached - the silenced DialBop-style motion reference `5bc86b80-fbd2-43a2-90dd-53ef8aa2df00` is banned from this shot. Because that deleted paragraph also carried the no-captions ban, one clause was appended to HARD RULES to keep it. The five-beat timeline, the held-iPhone framing lock, the children stepping LEFT, the containment rules and the real-time locks are byte-identical to take 1.

```text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the hallway floor holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the staircase behind the dark wooden railing, leaning out over it with one arm stretched up to the gold star on top of the tall decorated Christmas tree beside the stairs. Two small children in matching American-flag pajamas stand on the floor at the lower left of the frame with their backs to the camera, watching her. Wrapped presents at the foot of the tree.

ACTION TIMELINE:
0.0–1.0s — Both hands now on the gold star, she works it down onto the top of the tree, stretching further and further out over the railing, more and more of her weight going onto the tree itself.
1.0–1.6s — The tree tips. It leans away from the stairs toward the open floor and keeps going, and she loses her balance and comes over the railing with it, still holding on. At the same instant the two children take three quick steps further to the left, well out of the way, and stop there — the tree never comes near them.
1.6–2.4s — The whole tree swings down diagonally across the frame and crashes flat onto the wooden floor, branches flattening, the gold star snapping off the top and skittering away on its own.
2.4–3.2s — She lands on the floor face-down across the fallen tree, and the impact bursts a wave of ornaments off the branches — dozens of red, gold, pink and white baubles bouncing out low across the wooden floor and rolling toward the camera, spreading right across the bottom of the frame.
3.2–5.0s — The last ornaments wobble to a stop on the floor. She lies still across the fallen tree for a beat, then lifts her head, blows the hair out of her face and starts laughing. The two children stay where they moved to on the left, staring at the mess. End frame: the tree flat on the floor, ornaments scattered everywhere, her looking up laughing.

AUDIO: her real voice, lip-synced, matching her appearance — a short yelp as she goes over, then breathless laughing at the end; the dry rush of the tree branches going over; the heavy thud of the tree hitting the wooden floor; dozens of glass and plastic ornaments clattering, bouncing and rolling on hard wood; one small surprised squeal from a child. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip, and the two children keep exactly the same clothes and size. The hallway stays pixel-faithful to the start frame — same staircase, same dark wooden railing and newel post, same American flag on the wall, same wooden floor, same daylight. The children are never touched by the tree and are never underneath it. Real weight and gravity — the tree topples on its own mass and stops on the floor, she drops straight down, nobody is thrown or launched. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark. No subtitles, no captions and no on-screen words of any kind anywhere in the picture.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
```

**Start image** - `starting_frames/v10_c01_g7.png` - media `d64272c4-b6bc-4114-8742-743cf9958aff`. This is the ONLY media attached - no video reference, by instruction.

**Settings** - seedance_2_5 - mode omni_reference - 1080p - 9:16 - 5s - count 1 - credits (use_unlim false) - workspace Oneofone1. Submitted with `declined_preset_id = 24bae836-2c4a-48e0-89b6-49fcc0b21612` after the backend recommended the preset "IN THE DARK" instead of submitting; the payload was otherwise identical. Job `0c62f8eb-758e-45ff-8996-8a20d0a4cae3`. Output 5.05s, md5 `582e42c6fcec6c22443445ae074e0df3`.

---

## C02 - Hands on the box

*Section:* B-roll 1 - the unbox  
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW  
*What it is:* two hands resting on the closed carton on the limed white-oak table, the beat before it opens.

- frames: `v10_c02_g1.png` (current)
- clips: `v10_c02_g1.mp4` (current)

*Reused from v8 C02 - changed: (a) the sleeve, now deep burgundy wool; (b) `SECOND - THE TABLE`, now limed white oak with the grain filled chalky white, dead matte, square edge; (c) `THIRD - THE BACKGROUND`, now the Nantucket coastal cottage parlour; (d) the dressing paragraph retuned to that table and palette.*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c02_g1.png` | owns the geometry - camera position, top-down-ish angle, distance, the table plane, the hands' position and grip, the box's position, scale and angle |
| @Image 2 | `../../product_images/box_festive_green_g2.png` | owns the carton artwork |

media ids `1cdfcc53-e771-4bba-9eab-b1788346098b`, `2597b25d-60d1-4060-9602-32b0ee26c2f7`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `55dddc27-3f22-450c-a287-58df40d369c3`

```text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep burgundy wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a limed white-oak table top: a pale blond timber whose open grain is filled with a chalky white lime wax so the pores read as fine white lines drifting across the surface, finished dead matte with no sheen at all, with a simple square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused Nantucket coastal cottage Christmas parlour: walls of chalk-white painted shiplap boards, a chalk-white painted brick fireplace with a simple pale oak mantel and cream knitted stockings hanging from it, a decorated Christmas tree with warm white fairy lights and antique gold and pearl-white ornaments standing off to one side, a narrow shelf high on the wall carrying a row of pale green sea-glass jars, all well out of focus so the box stays the clear subject.

Dress the limed oak table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte limed oak, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.

```

*Flag, not fixed:* check the THEXMASGLOW wordmark on this take - v4 to v8 all printed it twice, once on the green top face and once on the red band. Not re-rolled; that is Daniel's call, not a self-initiated re-roll.

---


### Video prompt - `clips/v10_c02_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c02_g1.png` - Higgsfield media `63c5d03c-c834-49b7-90a0-07931c541e52`
**Extra references** - `@Video 1` - the v6 C02 unboxing-mechanics clip, Higgsfield media `1d2e8a8d-1e49-422a-8b04-d1a1230096a4` (mechanics only, silent - see the AUDIO RULE at the top of the prompt). Stored by the backend under role `video`.
**Job** - `fa2b2ff0-ef25-46e7-be38-b5dff31c2247`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_fa2b2ff0-ef25-46e7-be38-b5dff31c2247.mp4

**Lineage** - Reused from v8 C02 - changed: the sleeve (soft dove-blue wool -> deep burgundy wool), the table (warm honey cherry dining -> limed white-oak, pale blond timber with chalky white lime-waxed pores, dead matte, square edge, in all three mentions including the 3.6-4.0s hold beat) and `[5] LOCATION` rewritten to the v10 room - chalk-white painted shiplap and a chalk-white painted brick fireplace with a pale oak mantel and cream knitted stockings in place of beadboard over a dove-blue dado and red brick, and white berries with antique gold and pearl-white baubles in place of red berries and red/antique-silver ones. The AUDIO RULE, the four priority rules, every beat with its time range, the camera block and the whole ban list are v8's words unchanged.

```
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a limed white-oak table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a deep burgundy wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a limed white-oak table fills the frame: pale blond timber whose open grain is filled with a chalky white lime wax so the pores read as fine white lines drifting across the surface, finished dead matte with no sheen at all, and a simple square edge. A lit cream pillar candle sits at the left, fir sprigs with white berries and small antique gold and pearl-white baubles beside it, and behind it, softly out of focus, chalk-white painted shiplap boards, a chalk-white painted brick fireplace with a simple pale oak mantel and cream knitted stockings hanging from it, a narrow shelf high on the wall carrying a row of pale green sea-glass jars, and a decorated Christmas tree with warm white fairy lights and antique gold and pearl-white ornaments. The candle, the fir, the berries, the baubles, the defocused fireplace and the defocused tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the limed white-oak table, lid flaps folded back, with the candle, the fir, the berries, the defocused fireplace and the defocused tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
```

## C03 - The dome lifted out

*Section:* B-roll 1 - the unbox  
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW  
*What it is:* one hand lifting the dome clear of the open carton onto the counter.

- frames: `v10_c03_g1.png` (current)
- clips: `v10_c03_g1.mp4` (current)

*Reused from v8 C03 - changed: (a) the sleeve, now deep burgundy, in both places it is named; (b) `THE COUNTER`, now end-grain walnut butcher-block; (c) `THE KITCHEN`, now the coastal cottage kitchen with a chalk-white zellige backsplash, LEFT.*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c03_g1.png` | owns the geometry - camera height, the counter plane, the dome's position and scale, the hand's approach |

media ids `7ccdd557-bfee-45b0-a067-0652320f537b`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `89ed549a-35bb-4e66-8865-c5a112bc239a`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a deep burgundy wool sweater sleeve pushed back; right forearm enters from the right in the same deep burgundy sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a thick end-grain walnut butcher-block counter: a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge, and a low satin oil finish. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A Nantucket coastal cottage Christmas kitchen, softly defocused: chalk-white shaker cabinets with polished nickel bin pulls, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a cream enamel range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

```

---


### Video prompt - `clips/v10_c03_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c03_g1.png` - Higgsfield media `3caebb7b-da16-4703-a637-fab90311dcd7`
**Extra references** - none
**Job** - `97937cae-55f3-488f-8307-5294b09bb075`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_97937cae-55f3-488f-8307-5294b09bb075.mp4

**Lineage** - Reused from v8 C03 - changed: the sleeve (soft dove-blue wool -> deep burgundy wool), the counter (honed toasted-oat sandstone -> thick end-grain walnut butcher block, in every mention - including `[11] PHYSICS` "The sandstone is hard:" -> "The butcher block is hard:" and "the stone" -> "the timber" inside the 1.2-3.0s and 3.0-3.4s beats and the audio line) and the kitchen (dove-blue inset cabinets with antique pewter cup pulls and cream crackle-glazed tile -> chalk-white shaker cabinets with polished nickel bin pulls and a chalk-white zellige backsplash). Every beat with its time range, the static camera block and the ban list are v8's words unchanged.

```
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a thick end-grain walnut butcher-block kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in deep burgundy wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a thick end-grain walnut butcher-block countertop - a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish - fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with chalk-white shaker cabinets with polished nickel bin pulls, a cream enamel range built into the tall cabinet run on the left, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the butcher-block counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the timber. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the timber in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the timber.
3.0-3.4s - the four feet of the stand touch the timber; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The butcher block is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the timber, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
```

## C04 - The cable going in

*Section:* B-roll 1 - the unbox  
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW  
*What it is:* the barrel plug meeting the socket on the back of the dome.

- frames: `v10_c04_g1.png` (current)
- clips: `v10_c04_g1.mp4`, `v10_c04_g2.mp4` (current)

*Reused from v8 C04 - changed: (a) the sleeve, now deep burgundy wool; (b) `THE COUNTER`, now end-grain walnut butcher-block; (c) `THE KITCHEN`, now the coastal cottage kitchen, RIGHT across the top third.*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c04_g1.png` | owns the geometry - camera height, the counter plane, the dome's position and scale, the cable and the hand |

media ids `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `1d69a04c-84ad-4a97-8d55-d5ce334848c1`

```text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep burgundy wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a thick end-grain walnut butcher-block counter: a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge, and a low satin oil finish. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A Nantucket coastal cottage Christmas kitchen, softly defocused across the top third of the frame: chalk-white shaker cabinets with polished nickel bin pulls, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a cream enamel range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.

```

---


### Video prompt - `clips/v10_c04_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c04_g1.png` - Higgsfield media `7963ee51-0e88-44d3-b10a-a3458a6ae8ac`
**Extra references** - none
**Job** - `3509e6c7-63ff-470b-b008-973b1d514135`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_3509e6c7-63ff-470b-b008-973b1d514135.mp4

**Lineage** - Reused from v8 C04 - changed: the sleeve in both hand definitions (soft dove-blue -> deep burgundy wool), the same sandstone -> end-grain walnut butcher-block counter and the same chalk-white kitchen swap as C03, and the two RED-glow lines ("spills onto the stone" -> "spills onto the timber", "the sandstone immediately around it" -> "the timber immediately around it"). FREEZE MEANS FREEZE, the RED-only lock, the black mesh disc starfield beat, the COUNT LOCK and the ban list are v8's words unchanged.

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
THE LEFT HAND - a woman's hand in a deep burgundy wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same deep burgundy sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a thick end-grain walnut butcher-block countertop - a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish - fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with chalk-white shaker cabinets with polished nickel bin pulls, a cream enamel range built into the tall cabinet run on the right, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the timber around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the timber immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
```

### Video prompt - `clips/v10_c04_g2.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c04_g1.png` - Higgsfield media `7963ee51-0e88-44d3-b10a-a3458a6ae8ac` - unchanged, a fix is a prompt edit not a new frame
**Extra references** - none. No video reference.
**Job** - `2cc97b1c-181d-495c-a8db-6d6e43fd014c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_204700_2cc97b1c-181d-495c-a8db-6d6e43fd014c.mp4

**Lineage** - Reused from `v10_c04_g1` - changed: the port. Daniel: *"it's not plugging the cable into the projector hole. This is probably an error from the ai model but to be sure check your prompt too."* The prompt was wrong. g1's TIMELINE said the connector goes into `the port on the side of the white stand base`. Opening `starting_frames/v10_c04_g1.png` at 3x on the port region shows the socket is not on the stand at all: it is a small dark oval USB-C socket set into the white plastic at the very bottom rim of the DOME body, just above where the dome meets the stand, slightly right of centre - and the plug's dark metal tongue already points LEFT straight at it with about a two-centimetre gap. The prompt was aiming the hand at a part that has no hole in it. Fixed by adding THE PORT and THE CONNECTOR to OBJECTS with that exact geometry, and rewriting the seating beat so the plug travels left along its own axis, the tongue enters and disappears inside the dome, and the plastic shoulder comes to rest flush against the white rim - with the hover / hesitate / drift / retreat / tap-the-outside / slide-along-the-rim failures banned by name. **Verified:** frames extracted at t=0.0/0.5/1.0/1.4/2.5/4.0 - the plug approaches, enters at 1.0s, is flush by 1.4s, and at 4.0s sits seated in the dome rim with the hand withdrawn and the cable trailing right. The seating now works.

```
TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands, product and lighting exactly. The ONLY things that change are the cable seating into the port and the projector lighting up RED.

[1] SUMMARY
Locked-off close shot: a hand PLUGS a white USB-C connector INTO the small dark socket in the bottom rim of the projector's white dome, and the projector switches on with RED light. 4 seconds, one take, camera completely static.

[2] GLOBAL STYLE
Real phone footage on a stable surface, warm modern kitchen light, extremely sharp and clean, correctly exposed. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, both hands, the cable and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand, standing left of centre on the counter. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE LEFT HAND - a woman's hand in a deep burgundy wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same deep burgundy sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a thick end-grain walnut butcher-block countertop - a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish - fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with chalk-white shaker cabinets with polished nickel bin pulls, a cream enamel range built into the tall cabinet run on the right, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the timber and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the timber around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the timber immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
```

## C05 - The door, then the room

*Section:* B-roll 2 - the reveal  
*Status:* BOTH FRAMES GENERATED - TAKE 1 FOR REVIEW  
*What it is:* two frames. F1 is the closed door with the wreath. F2 is the same doorway open with the room running behind it. F2 files in `references/` under NAMING.md section 4, not in `starting_frames/`.

- frames: `v10_c05_g1.png` (F1, current) - `references/v10_c05_r1.png`, `references/v10_c05_r2.png` (F2, current - the room frame attached to the video job)
- clips: `v10_c05_g1.mp4`, `v10_c05_g2.mp4` (current)

### FRAME 1 - the closed door

*Reused from v8 C05 F1 - changed: (a) the sleeve wording, now burgundy; (b) `CHANGE 1 - THE DOOR`, now a classic American four-panel door in deep oxblood red eggshell; (c) the colour-read check line retuned from dove blue to oxblood red.*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c05_g2.png` | owns the geometry - the closed door filling the frame, the wreath's position and scale, the camera distance and the hallway light |

media ids `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `c301edff-f38f-42fc-bdde-d914d68ab37d`

```text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and deep burgundy sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American four-panel door painted a deep oxblood red in a soft eggshell finish: crisp raised mouldings around four flat recessed panels, two tall ones below and two short ones above, clean painted surfaces with the faintest brush texture, an antique brass knob and a matching antique brass escutcheon plate, set in a plain painted cream frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the oxblood paint reads clearly as a deep warm red rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

```

### FRAME 2 - the room behind it

*Reused from v8 C05 F2 - changed: (a) the architecture clause and `CHANGE 1 - THE ROOM`, now the tall great room under a single-slope shed ceiling with three black steel tie rods; (b) the `TWO THINGS CHANGE FROM @Image 2` paragraph rebuilt for that room; (c) the knitwear, now sage-green and cream with cream fir trees; (d) `CHANGE 2 - THE PROJECTION` replaced wholesale with the new reference-driven block plus its `HOW THE LIGHT SITS ON THE CEILING` tail; (e) the floor clause retuned to the shed-ceiling room.*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/references/v1_c05_r1.png` | owns the geometry - the open doorway, the camera standing in the hall looking through, the door leaf swung inward on the left, the room beyond |
| @Image 2 | `../../references/house_great_room_shed.png` | owns the architecture - a newly generated architecture reference, not a photograph. See "The houses" below |

media ids `f3a8c329-4152-4a22-9469-d89578812e09`, `4dec9045-2ac2-4a2c-8412-6dc4ae08cfc0`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `c305720b-3c50-4de2-8006-13ff0da79bbf`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its raking ceiling, its boarding, its tie rods, its walls, its glazed gable and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm sage-green and cream nordic knitted Christmas jumpers with a row of cream fir trees across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall great room under a SINGLE-SLOPE SHED CEILING - one continuous flat plane of narrow white-painted tongue-and-groove boards that starts low over the left-hand side of the room and rakes up in one unbroken climb to a very high eaves line on the right, the board seams all running straight up the slope; the room is held together across that span by three slim black steel tie rods, each a straight round rod running horizontally from wall to wall well below the boards and bolted into a small black anchor plate at each end; small flush recessed downlights are set in a line up the rake; there is NO timber rafter, no ridge, no collar beam, no king post and no vault anywhere in this room - the ceiling is one single straight raking plane; cream plaster walls; under the high side of the rake on the right, an almost full-height glazed gable wall of slim black steel frames divided into many small rectangular panes, rising with the slope; on the back wall a wide cream plaster fireplace with a long low horizontal firebox and a tall potted olive tree standing beside it; along the left an open kitchen with deep forest-green slab cabinetry, aged brass hardware, a pale stone island and woven rattan counter stools. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground and a round dark walnut coffee table on a large oat flat-weave rug. Copy the proportions, the single raking plane, the direction of the board seams, the three black tie rods and their anchor plates, and the tall black glazed gable from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall glazed gable shows a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing against the cream plaster back wall beside the fireplace with warm white lights and sage-green and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and sage-green velvet ribbon laid along the plaster above the firebox, cream knitted stockings hanging beneath it, and a large evergreen wreath with a sage-green velvet bow hung on the glazed gable wall. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every cream plaster wall, the whole raking boarded ceiling from its low edge all the way up to the high eaves, and the three black steel tie rods strung beneath it, with no visible edge, no rectangle and no screen. LOW ALONG THE WALLS, a deep snow-laden pine forest running the whole width of the room along the very bottom of the projection, rank behind rank of little glowing firs in emerald green and warm gold with snow heaped on every branch, and rising straight out of that forest on the left a whole ornate fairy-tale Christmas city built of lit gold - tier upon tier of slender spires, ribbed onion domes, arched galleries and pinnacled towers stacked up the wall, every arched window lit warm gold, fine gold filigree running along every cornice and balustrade, thick snow lying on every ledge and roof and dome, the whole city glowing as though it were carved out of light; and winding out of the pines on the right a long lit steam train, a dark locomotive leading eight carriages whose windows all glow warm gold, a bright plume of steam and sparks trailing back over the carriage roofs and a glowing gold rail curving away behind it through the trees; ABOVE THE FOREST AND THE CITY, wide soft aurora ribbons in emerald green, rose magenta, warm gold and soft teal sweeping up the walls in long slow curves and carrying over onto the single raking shed plane, five or six broad overlapping bands layered over each other so there is very little bare boarded slope left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe, where they lie flat along the rake and run straight up it with the climb of the plane instead of hanging as vertical curtains, and are stretched longer and thinner the further up the slope they travel; ACROSS THE RAKING CEILING OVERHEAD, one colossal spiral whirlpool of light filling most of the slope - seven concentric glowing rings of emerald green, warm gold and rose magenta winding in on each other in a slow tightening spiral and drawing down to one brilliant white-gold core at the very centre, every ring built of countless tiny points of light so the whole thing reads as a whirlpool of stars rather than a painted disc; Santa's sleigh drawn by a team of eight flying reindeer sweeping straight out of the mouth of that spiral, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners into the spiral, the whole team lying flat on the rake so it is keystoned and stretched by the climb of the plane, growing larger and brighter as it rises toward the tall glazed gable; a big pale blue full moon glowing high on the cream plaster chimney breast on the back wall, cool silver-blue and softly cratered and the one cool-coloured thing in the whole picture, with the tiny black silhouette of a second sleigh and its reindeer team crossing right over the face of it; floating wrapped Christmas gifts drifting through the whole scene at five or six different depths and sizes, each a solid glowing box in gold, emerald or rose with a bright ribbon cross and a big soft bow on top, the nearest big enough to read the weave of the ribbon, all of them turning slowly end over end as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the raking boards and both walls; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE: emerald green, warm gold, cream white, rose magenta and soft teal, richly saturated against the white boards and the cream plaster, with the single pale blue moon as the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue. The great spiral is an AURORA WHIRLPOOL made of Christmas light with a sleigh flying out of its mouth, not a space nebula: it must NOT look like outer space, a galaxy, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit gold Christmas city, a steam train, flying reindeer and falling gifts in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real painted boarding, not paint and not a sticker. The light is TRANSLUCENT - the white-painted boards of the slope and the fine seam between every board, the three slim black steel tie rods and their black anchor plates, and the line of flush recessed downlights running up the rake, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each black tie rod breaks the light with its own hard shadow line where it hangs below the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the single raking plane, stretching longer and thinner the further up the slope it travels. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real single-slope boarded shed ceiling climbing in one unbroken rake to the glazed gable, with the black tie rods crossing beneath it, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the round walnut coffee table, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no city, no train, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

```

---


### Video prompt - `clips/v10_c05_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 8s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c05_g1.png` - Higgsfield media `8a67ec09-6f62-4ee1-81d7-bf9a9523ac84`
**Extra references** - `@Image 1` - `references/v10_c05_r2.png`, the room the projection is read from, Higgsfield media `db543b24-0c41-4ca2-b1ee-237f92dc5743`. Stored by the backend under role `image`. No video reference - banned on C05/C06/C07.
**Job** - `c05a1b4a-4cae-401f-b415-055bdc0c723a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_c05a1b4a-4cae-401f-b415-055bdc0c723a.mp4

**Lineage** - Reused from v8 C05 g3 (the rewritten take, not g1) - changed: the vaulted plaster ceiling -> a flat coffered drywall ceiling of white beams with a sunken panel in every square (plaster -> drywall throughout, "THE VAULT IS FULL" -> "THE CEILING IS FULL"); the door (six-panel dove-blue -> four-panel oxblood-red); THE BALLOONS and THE SNOW GLOBES -> THE FERRIS WHEEL AND THE CAROUSEL and THE RIPPLE RINGS (seven concentric rings spreading outward from the great star); the aurora now RADIATES OUTWARD FROM THE GREAT STAR in crimson, ruby, gold and emerald; the sleigh now arcs in toward that star; the moon and north star -> the church clock face as the only fixed element; the sofa (pale grey sectional -> big oatmeal linen sectional) and the boy now starts with his back to camera rather than facing it; and "no bare un-animated patch of cream plaster" -> "no bare un-animated coffer panel and no bare white beam", with the matching ban-list entries. The HIGHEST PRIORITY opener, the one-continuous-move camera walk, every beat with its time range and the HARD RULES are v8 g3's words unchanged.

```
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the flat coffered ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the drywall. @Image 1 is ONE PAUSED FRAME of that movie. At 0.0s it un-pauses and keeps running to the last frame. Smoke pours from every chimney, the aurora radiates, the sleigh flies, the Ferris wheel and the carousel turn, the ripple rings spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed four-panel oxblood-red door with a wreath, a hand on the brass knob. @Image 1 is the great room behind that door and the authority on its layout, coffered ceiling, furniture, the two children, their clothes, the colours, and the exact set and style of every projected shape.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Every chimney in the snowy storybook village pours smoke like a real wood fire on a cold still evening: it boils out of the pot, leans right, climbs and widens and thins away, and the next plume is already forming behind it. Not one chimney in the village is without its plume.

THE AURORA. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the drywall; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE FERRIS WHEEL AND THE CAROUSEL. The enormous lit Ferris wheel TURNS steadily about its lit hub, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel TURNS the other way under its striped canopy, its horses rising and falling on their twisted brass poles as they come round, the lights along every scallop of the canopy chasing round the rim. Both keep turning from the first frame to the last.

THE RIPPLE RINGS. The seven concentric rings SPREAD OUTWARD from the great star across the ceiling like rings on water, each one travelling away from the core, widening and thinning and fading as it reaches the walls, while a fresh ring is already forming at the centre behind it, so the spread never stops.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the tiny skating silhouettes circling on the frozen pond, shooting stars streaking and fading, the floating baubles and candy canes turning slowly as they drift, the big gold bells swinging gently on their crimson bow with the clappers glowing inside them, the lit shopfront windows and the church clock flickering warm, and wisps of crimson and gold cloud drifting between the aurora bands. Only the glowing clock face of the church holds position; it simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, steps up into every sunken coffer and back down onto the beams between them, and breaks where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, its spreading ripple rings, the radiating aurora, the flying sleigh, pouring snow and twinkling stars run into every single coffer panel and over every beam, right into all four corners. No bare un-animated coffer panel and no bare white beam anywhere in the closing framing.

BEATS
0.0-0.8s - The hand turns the knob and pushes the door away from camera. The room behind it is already running; the widening gap only uncovers more of a movie that was already playing. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.8s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white coffered ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the aurora ripples, the sleigh flies on across the ceiling, the Ferris wheel and the carousel keep turning, the ripple rings keep spreading and the snow keeps falling.
Inside that single move: THE BOY, the child standing on the right at 0.0s with his back to camera, takes three or four quick real steps and LAUNCHES HIMSELF UP ONTO the big oatmeal linen sectional sofa that wraps the room right behind him, landing on his knees with both arms flying up, laughing, then keeps bouncing there until the last frame. THE GIRL stays where she is, seen from behind, turning her head to follow him. Projected shapes slide down the walls behind them and pass across their backs.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.8s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the oxblood-red door, the brass knob, the bare forearm and its thin gold bangle. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole coffered ceiling is covered in moving picture at the end. The boy ends the clip bouncing on the sofa. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an aurora that sits still; a parked sleigh; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated coffer panel in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; children posed or standing still; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.
```

### Video prompt - `clips/v10_c05_g2.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s (returned to the v6/v7 5s standard - the 8s came from the v8 C05 g3 motion fix and should not have propagated) - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c05_g1.png` - Higgsfield media `8a67ec09-6f62-4ee1-81d7-bf9a9523ac84` - unchanged, a fix is a prompt edit not a new frame
**Extra references** - `@Image 1` - `references/v10_c05_r2.png`, the room the projection is read from, Higgsfield media `db543b24-0c41-4ca2-b1ee-237f92dc5743`. Coerced by the backend to `image_references`. No video reference - banned on C05/C06/C07.
**Job** - `def9fb7a-c704-46f7-887a-3dba143e0dfc`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_204700_def9fb7a-c704-46f7-887a-3dba143e0dfc.mp4

**Lineage** - Reused from `v10_c05_g1` - changed: the duration and the children's entrance, the same two defects as v9 C05 and fixed with the same edits. **(1) Duration.** g1 ran 8s; back to 5s. The 8s came from my own v8 C05 g3 motion fix and propagated into v9 and v10 through CLAUDE.md Rule 3's *reuse the settings*. My error. **(2) The kids.** `THE GIRL stays where she is, seen from behind, turning her head to follow him.` is deleted and replaced with her own run across the rug toward the fireplace, head back, one arm up pointing at the great radiating star overhead, still moving on the last frame; beat 0.0-0.6s states BOTH CHILDREN ARE ALREADY IN MOTION; the POSITIVE LOCK and the BANNED list get the same explicit no-freeze set. Nouns held to this room - the oatmeal sectional, the lit tree, the great radiating star. The boy's sofa launch, the hero motion blocks, the camera, the start frame and the reference are byte-identical to g1.

```
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the flat coffered ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the drywall. @Image 1 is ONE PAUSED FRAME of that movie. At 0.0s it un-pauses and keeps running to the last frame. Smoke pours from every chimney, the aurora radiates, the sleigh flies, the Ferris wheel and the carousel turn, the ripple rings spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed four-panel oxblood-red door with a wreath, a hand on the brass knob. @Image 1 is the great room behind that door and the authority on its layout, coffered ceiling, furniture, the two children, their clothes, the colours, and the exact set and style of every projected shape.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Every chimney in the snowy storybook village pours smoke like a real wood fire on a cold still evening: it boils out of the pot, leans right, climbs and widens and thins away, and the next plume is already forming behind it. Not one chimney in the village is without its plume.

THE AURORA. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the drywall; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE FERRIS WHEEL AND THE CAROUSEL. The enormous lit Ferris wheel TURNS steadily about its lit hub, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel TURNS the other way under its striped canopy, its horses rising and falling on their twisted brass poles as they come round, the lights along every scallop of the canopy chasing round the rim. Both keep turning from the first frame to the last.

THE RIPPLE RINGS. The seven concentric rings SPREAD OUTWARD from the great star across the ceiling like rings on water, each one travelling away from the core, widening and thinning and fading as it reaches the walls, while a fresh ring is already forming at the centre behind it, so the spread never stops.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the tiny skating silhouettes circling on the frozen pond, shooting stars streaking and fading, the floating baubles and candy canes turning slowly as they drift, the big gold bells swinging gently on their crimson bow with the clappers glowing inside them, the lit shopfront windows and the church clock flickering warm, and wisps of crimson and gold cloud drifting between the aurora bands. Only the glowing clock face of the church holds position; it simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, steps up into every sunken coffer and back down onto the beams between them, and breaks where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, its spreading ripple rings, the radiating aurora, the flying sleigh, pouring snow and twinkling stars run into every single coffer panel and over every beam, right into all four corners. No bare un-animated coffer panel and no bare white beam anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white coffered ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the aurora ripples, the sleigh flies on across the ceiling, the Ferris wheel and the carousel keep turning, the ripple rings keep spreading and the snow keeps falling.
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. The door opens on two kids in the middle of doing something, not on two kids standing waiting to be filmed, and neither of them is ever still. THE BOY, the child on the right with his back to camera, is already mid-stride as the gap widens; he takes three or four quick real steps and LAUNCHES HIMSELF UP ONTO the big oatmeal linen sectional sofa that wraps the room right behind him, landing on his knees with both arms flying up, laughing, and keeps bouncing there until the last frame. THE GIRL, the child on the left with the long wavy hair, is already running as the door opens; she runs on across the room toward the lit Christmas tree without breaking step, tips her head right back to look straight up at the great radiating star on the coffered ceiling and throws one arm up pointing at it, mouth open, delighted - and she is still moving and still pointing on the last frame. Both runs are ordinary excited-kid running at real speed with real weight: feet landing, knees bending, arms swinging, hair and jumpers moving with them. Projected shapes slide down the walls behind them and pass across their backs.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the oxblood-red door, the brass knob, the bare forearm and its thin gold bangle. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole coffered ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: the boy ends the clip bouncing on the sofa, the girl ends it still running and still pointing up at the ceiling. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an aurora that sits still; a parked sleigh; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated coffer panel in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.
```

## C06 - The child in bed

*Section:* B-roll 2 - the reveal  
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW  
*What it is:* the child in bed looking up at the projection running across the bedroom ceiling.

- frames: `v10_c06_g1.png`, `v10_c06_g2.png` (current - the frame this clip was animated from)
- clips: `v10_c06_g1.mp4` (current)

*Reused from v8 C06 - changed: (a) `CHANGE 1 - THE CHILD`, now a boy about seven with short sandy-blond hair; (b) `CHANGE 2 - THE ROOM`, now the bedroom under a flat tray ceiling with an angled reveal and downlights in the flat border; (c) the `TWO THINGS CHANGE FROM @Image 2` paragraph rebuilt for that tray; (d) `CHANGE 3 - THE PROJECTION` replaced with the new block plus the tray-ceiling tail; (e) the floor clause.*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c06_g1.png` | owns the geometry - camera height at the foot of the bed, the child's position in frame, how much ceiling is visible |
| @Image 2 | `../../references/house_bedroom_tray.png` | owns the architecture - a newly generated architecture reference, not a photograph |

media ids `0a845da6-2607-46cc-a595-4fee4b17d6a9`, `0c193093-94b1-498d-9dfe-4d3f7a8aee03`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `d9d7d019-1e11-4be0-a1fd-bee6b12f8ff9`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its tray ceiling, its walls, its windows, its door and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about seven with short sandy-blond hair, fully dressed for winter in a warm sage-green and cream nordic knitted Christmas jumper with a row of cream fir trees across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom with a FLAT TRAY CEILING - one big clean rectangle is recessed up into the middle of an otherwise flat cream plaster ceiling, its edges crisp and straight and parallel to the walls, with a plain shallow angled reveal stepping up from the flat border into the recessed panel, and small flush recessed downlights set in the flat border on either side; the whole ceiling is smooth plaster and perfectly flat apart from that one rectangular step - there is no vault, no slope, no ridge, no rafter, no beam and no boarding anywhere in this room; warm greige plaster walls with plain white skirting; the far wall carrying two tall white-framed double-hung windows spaced apart, each hung with long cream pinch-pleat curtains on a slim black rod, and a tall white-painted panelled door at the right-hand end; an upholstered bed with a wide cream headboard standing against that wall between the windows, two small pale oak nightstands with small cream table lamps, and a long cream upholstered bench on slim pale oak legs at the foot of the bed; a warm oak plank floor under a very large oat flat-weave rug. Copy the proportions, the flat ceiling, the single rectangular tray recess, its crisp edges and its angled reveal, and the two windows and the door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: both windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and both table lamps are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a sage-green wool quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking hangs on the wall above the headboard, a warm fairy-light garland is strung around the left-hand window, a small lit Christmas tree with sage-green and antique gold ornaments stands on the floor beside the bed, and a small evergreen wreath with a sage-green velvet bow hangs on the panelled door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, the flat cream plaster border of the ceiling, up the angled reveal and right across the recessed tray panel set into the middle of it, wrapping around the corner where wall meets ceiling without a break, with no visible edge, no rectangle and no screen. LOW ALONG THE WALLS, a deep snow-laden pine forest running the whole width of the room along the very bottom of the projection, rank behind rank of little glowing firs in emerald green and warm gold with snow heaped on every branch, and rising straight out of that forest on the left a whole ornate fairy-tale Christmas city built of lit gold - tier upon tier of slender spires, ribbed onion domes, arched galleries and pinnacled towers stacked up the wall, every arched window lit warm gold, fine gold filigree running along every cornice and balustrade, thick snow lying on every ledge and roof and dome, the whole city glowing as though it were carved out of light; and winding out of the pines on the right a long lit steam train, a dark locomotive leading eight carriages whose windows all glow warm gold, a bright plume of steam and sparks trailing back over the carriage roofs and a glowing gold rail curving away behind it through the trees; ABOVE THE FOREST AND THE CITY, wide soft aurora ribbons in emerald green, rose magenta, warm gold and soft teal sweeping up the walls in long slow curves and carrying over onto the flat tray ceiling, five or six broad overlapping bands layered over each other so there is very little bare cream plaster left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe, where they lie flat on the ceiling and run with the long direction of the room instead of hanging as vertical curtains, and visibly break at the crisp square edge of the tray, stepping up onto the recessed panel and back down onto the flat border; ACROSS THE TRAY CEILING OVERHEAD, one colossal spiral whirlpool of light filling most of the recessed tray panel - seven concentric glowing rings of emerald green, warm gold and rose magenta winding in on each other in a slow tightening spiral and drawing down to one brilliant white-gold core at the very centre, every ring built of countless tiny points of light so the whole thing reads as a whirlpool of stars rather than a painted disc; Santa's sleigh drawn by a team of eight flying reindeer sweeping straight out of the mouth of that spiral, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners into the spiral, the whole team lying flat on the tray panel so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big pale blue full moon glowing high on the greige plaster wall above the bed, cool silver-blue and softly cratered and the one cool-coloured thing in the whole picture, with the tiny black silhouette of a second sleigh and its reindeer team crossing right over the face of it; floating wrapped Christmas gifts drifting through the whole scene at five or six different depths and sizes, each a solid glowing box in gold, emerald or rose with a bright ribbon cross and a big soft bow on top, the nearest big enough to read the weave of the ribbon, all of them turning slowly end over end as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the tray panel, the flat border and both walls; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE: emerald green, warm gold, cream white, rose magenta and soft teal, richly saturated against the cream plaster of the tray, with the single pale blue moon as the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue. The great spiral is an AURORA WHIRLPOOL made of Christmas light with a sleigh flying out of its mouth, not a space nebula: it must NOT look like outer space, a galaxy, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit gold Christmas city, a steam train, flying reindeer and falling gifts in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, the crisp edge of the tray and the plain angled reveal stepping up into it, and the flush recessed downlights set in the flat border, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the square edge of the tray breaks the light with its own hard shadow line where the ceiling steps up. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the flat plane of the border and stepping up onto the recessed tray panel. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling with one clean rectangular tray recessed into the middle of it, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The warm oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no city, no train, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with the boy's face clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.

```

---


### Video prompt - `clips/v10_c06_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 5s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c06_g2.png` - Higgsfield media `a8dbc496-95dd-4c47-85ec-863af73b643c`
**Extra references** - none
**Job** - `7f57a886-f8e5-4706-81e4-edd5725c064e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_7f57a886-f8e5-4706-81e4-edd5725c064e.mp4

**Lineage** - Reused from v8 C06 - changed: the room (attic with a flat plaster centre panel and two knuckle lines -> a bedroom with a flat cream tray ceiling, its four angled reveals and crown moulding, and a four-panel picture-frame moulding accent wall behind the bed); the boy (about six with short dark brown hair -> about seven with short sandy-blond hair) and his jumper (dove-blue and cream with cream stags -> cream and oatmeal with deep-green firs and rust-red reindeer); the projected picture is now a storybook village with lit shopfronts, market stalls and a church clock, every single chimney smoking; THE BALLOONS -> THE FERRIS WHEEL AND THE CAROUSEL, plus new THE RIPPLE RINGS and THE SKATERS AND THE FLOATING THINGS paragraphs; the aurora radiates outward from the great star; the moon and north star -> the church clock as the only fixed element; and "near the knuckle line" -> "near the crown moulding of the tray". The high-start TILT DOWN camera move with its slight pull back, every beat with its time range and the ban-list structure are v8's words unchanged.

```
Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected snow-village picture is PLAYING across the panelled accent wall behind the bed and the whole flat tray ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the flat cream plaster ceiling and its single rectangular tray recess with its four angled reveals and its crown moulding, the flush recessed downlights in the flat border, the four-panel picture-frame moulding accent wall behind the bed, the bed with its deep crimson wool quilt and cream linen pillows, the wide cream upholstered headboard, the long cream upholstered bench at the foot of the bed, the small lit Christmas tree, the large oat flat-weave rug, the two windows with their curtains and garland, the stocking, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child, about seven years old with short sandy-blond hair, in a warm cream and oatmeal nordic knitted Christmas jumper with a row of deep-green fir trees and rust-red reindeer across the yoke, charcoal knitted lounge trousers and thick mustard knitted socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the panelled wall and the whole flat tray ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a whole snowy storybook Christmas village running low along the walls with steep-gabled houses and lit shopfronts, a church with a lit steeple and a glowing clock face, market stalls under red-and-white striped awnings and lamp-posts hung with wreaths, a curl of smoke above every single chimney, a frozen silver-blue pond set into the village with tiny skating silhouettes circling on it, an enormous lit FERRIS WHEEL rising out of the village on the left in crimson and gold bulbs and a great golden CAROUSEL under a striped canopy on the right, wide aurora ribbons in deep crimson and ruby red with warm gold and emerald green threaded between them radiating outward from the star overhead, one colossal eight-pointed STAR OF BETHLEHEM filling the whole tray ceiling with four long rays reaching into its corners, seven concentric ripple rings spreading outward from it, Santa's sleigh drawn by eight flying reindeer arcing in toward the star with a long tapering trail, a huge pair of ornate gold bells tied with a crimson bow high on one wall, floating glowing baubles and candy canes drifting at five or six different depths, a dense field of stars of many sizes, long-tailed shooting stars, and a heavy fall of large soft glowing six-point snowflakes and tiny points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE AURORA - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE FERRIS WHEEL AND THE CAROUSEL - both TURN, steadily and without ever stopping. The enormous lit Ferris wheel turns about its lit hub roughly a quarter of a full turn every second, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel turns the other way under its striped canopy at about the same rate, its horses rising and falling on their twisted brass poles as they come round, and the lights along every scallop of the canopy edge chasing round the rim.
- THE RIPPLE RINGS - the seven concentric rings SPREAD OUTWARD from the great star across the tray ceiling like rings on water, each one travelling away from the core toward the walls, widening and thinning and fading as it goes, while a fresh ring is already forming at the centre behind it, so the spread never stops.
- THE SKATERS AND THE FLOATING THINGS - the tiny silhouettes keep circling on the frozen pond, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers glowing inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the crown moulding of the tray, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE CHURCH CLOCK - the glowing clock face on the church steeple is the ONLY element that holds its position. It stays exactly where it is in the village for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the panelled wall and the flat tray ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the aurora rippling, the ripple rings spreading and the sleigh flying across the tray as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
```

## C07 - The two children in the room

*Section:* B-roll 2 - the reveal  
*Status:* FRAME GENERATED - TAKE 1 FOR REVIEW  
*What it is:* the two children standing in the middle of the great room with the projection running over every surface.

- frames: `v10_c07_g1.png`, `v10_c07_g2.png` (current - the frame this clip was animated from)
- clips: `v10_c07_g1.mp4` (current)

*Reused from v8 C07 - changed: (a) the architecture clause and `CHANGE 2 - THE ROOM`, now the same shed-ceiling great room C05 F2 opens onto; (b) `CHANGE 1 - THE CHILDREN`, now a girl about eight with short dark curly hair and a boy about five with straight black hair, in sage green and cream; (c) the `TWO THINGS CHANGE FROM @Image 2` paragraph; (d) `CHANGE 3 - THE PROJECTION` replaced with the new block plus its `HOW THE LIGHT SITS ON THE SURFACES` tail; (e) the floor clause.*

**References attached**

| slot | file | why |
|---|---|---|
| @Image 1 | `../video_1_assets/starting_frames/v1_c07_g1.png` | owns the geometry - camera height, the children's position and scale in frame, how much of the room and ceiling is in shot |
| @Image 2 | `../../references/house_great_room_shed.png` | owns the architecture - the same room C05 F2 opens onto. Within one ad C05 F2 and C07 are always the same house |

media ids `c9a6740d-383b-4829-a7b9-f7a3c079c03f`, `4dec9045-2ac2-4a2c-8412-6dc4ae08cfc0`

**Prompt** - `gpt_image_2_5 - sunburst - 9:16 - 2k - medium` - job `0beea661-fa15-432f-bf8c-1052a0f512cc`

```text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its raking ceiling, its boarding, its tie rods, its walls, its glazed gable and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with short dark curly hair, the boy is about five with straight black hair. Both are fully dressed for winter in warm sage-green and cream nordic knitted Christmas jumpers with a row of cream fir trees across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: a tall great room under a SINGLE-SLOPE SHED CEILING - one continuous flat plane of narrow white-painted tongue-and-groove boards that starts low over the left-hand side of the room and rakes up in one unbroken climb to a very high eaves line on the right, the board seams all running straight up the slope; the room is held together across that span by three slim black steel tie rods, each a straight round rod running horizontally from wall to wall well below the boards and bolted into a small black anchor plate at each end; small flush recessed downlights are set in a line up the rake; there is NO timber rafter, no ridge, no collar beam, no king post and no vault anywhere in this room - the ceiling is one single straight raking plane; cream plaster walls; under the high side of the rake on the right, an almost full-height glazed gable wall of slim black steel frames divided into many small rectangular panes, rising with the slope; on the back wall a wide cream plaster fireplace with a long low horizontal firebox and a tall potted olive tree standing beside it; along the left an open kitchen with deep forest-green slab cabinetry, aged brass hardware, a pale stone island and woven rattan counter stools. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground and a round dark walnut coffee table on a large oat flat-weave rug. Copy the proportions, the single raking plane, the direction of the board seams, the three black tie rods and their anchor plates, and the tall black glazed gable from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall glazed gable shows a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the cream plaster back wall beside the fireplace with warm white lights and sage-green and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and sage-green velvet ribbon laid along the plaster above the firebox, cream knitted stockings hanging beneath it, and a large evergreen wreath with a sage-green velvet bow hung on the glazed gable wall. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire cream plaster back wall, the plaster walls either side of it, the whole raking boarded ceiling from its low edge up to the high eaves and the three black steel tie rods strung beneath it, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. LOW ALONG THE WALLS, a deep snow-laden pine forest running the whole width of the room along the very bottom of the projection, rank behind rank of little glowing firs in emerald green and warm gold with snow heaped on every branch, and rising straight out of that forest on the left a whole ornate fairy-tale Christmas city built of lit gold - tier upon tier of slender spires, ribbed onion domes, arched galleries and pinnacled towers stacked up the wall, every arched window lit warm gold, fine gold filigree running along every cornice and balustrade, thick snow lying on every ledge and roof and dome, the whole city glowing as though it were carved out of light; and winding out of the pines on the right a long lit steam train, a dark locomotive leading eight carriages whose windows all glow warm gold, a bright plume of steam and sparks trailing back over the carriage roofs and a glowing gold rail curving away behind it through the trees; ABOVE THE FOREST AND THE CITY, wide soft aurora ribbons in emerald green, rose magenta, warm gold and soft teal sweeping up the walls in long slow curves and carrying over onto the single raking shed plane, five or six broad overlapping bands layered over each other so there is very little bare boarded slope left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe, where they lie flat along the rake and run straight up it with the climb of the plane instead of hanging as vertical curtains, and are stretched longer and thinner the further up the slope they travel; ACROSS THE RAKING CEILING OVERHEAD, one colossal spiral whirlpool of light filling most of the slope - seven concentric glowing rings of emerald green, warm gold and rose magenta winding in on each other in a slow tightening spiral and drawing down to one brilliant white-gold core at the very centre, every ring built of countless tiny points of light so the whole thing reads as a whirlpool of stars rather than a painted disc; Santa's sleigh drawn by a team of eight flying reindeer sweeping straight out of the mouth of that spiral, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners into the spiral, the whole team lying flat on the rake so it is keystoned and stretched by the climb of the plane, growing larger and brighter as it rises toward the tall glazed gable; a big pale blue full moon glowing high on the cream plaster chimney breast on the back wall, cool silver-blue and softly cratered and the one cool-coloured thing in the whole picture, with the tiny black silhouette of a second sleigh and its reindeer team crossing right over the face of it; floating wrapped Christmas gifts drifting through the whole scene at five or six different depths and sizes, each a solid glowing box in gold, emerald or rose with a bright ribbon cross and a big soft bow on top, the nearest big enough to read the weave of the ribbon, all of them turning slowly end over end as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the raking boards and both walls; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE: emerald green, warm gold, cream white, rose magenta and soft teal, richly saturated against the white boards and the cream plaster, with the single pale blue moon as the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue. The great spiral is an AURORA WHIRLPOOL made of Christmas light with a sleigh flying out of its mouth, not a space nebula: it must NOT look like outer space, a galaxy, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit gold Christmas city, a steam train, flying reindeer and falling gifts in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real painted boarding, not paint and not a sticker. The light is TRANSLUCENT - the white-painted boards of the slope and the fine seam between every board, the three slim black steel tie rods and their black anchor plates, and the line of flush recessed downlights running up the rake, all stay clearly visible THROUGH the coloured light, and each black tie rod breaks the light with its own hard shadow line where it hangs below the boards. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full it must still read as projected light on a real single-slope boarded ceiling with black steel tie rods crossing beneath it, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the round walnut coffee table and the tree carry NO projected shapes at all - no snowflakes, no stars, no city, no train, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.

```

---


### Video prompt - `clips/v10_c07_g1.mp4`

**Settings** - seedance_2_5 - mode omni_reference - 720p - 9:16 - 4s - count 1 - generate_audio true - multi_shots false - declined_preset_id `24bae836-2c4a-48e0-89b6-49fcc0b21612` - credits (use_unlim false) - workspace Oneofone1
**Start image** - `starting_frames/v10_c07_g2.png` - Higgsfield media `52c89c73-8abb-4e85-a638-258f60ee7ab4`
**Extra references** - none
**Job** - `53a182b3-65e4-4a1c-9f82-f02e3c82232f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194655_53a182b3-65e4-4a1c-9f82-f02e3c82232f.mp4

**Lineage** - Reused from v8 C07 - changed: the ceiling (cathedral vault of cream plaster with dark walnut rafters -> a flat deep coffered ceiling of chunky white beams crossing in a grid with a recessed panel in every square) and the walls (white raised-panel wainscot with a moulded chair rail, whitewashed painted brick chimney breast); the smaller child now has straight black hair and looks up at the ceiling in wonder, and the girl is caught mid-air above the cushions with the cushion compressed under her; the jumpers (-> cream and oatmeal with deep-green firs and rust-red reindeer); the floor list (warm oak boards / greige rug / grey sectional / round coffee table -> pale oak boards / oat flat-weave rug / oatmeal linen sectional / long ottoman); the same storybook village, radiating aurora, Ferris wheel, carousel, ripple-ring and church-clock substitutions as C05; and one new ban on an un-animated coffer panel or white beam. The camera tilt-up, every beat with its time range and the ban-list structure are v8's words unchanged.

```
Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected snow-village picture is PLAYING across the back wall and the whole flat coffered ceiling and its chunky white beams, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the flat deep coffered ceiling of chunky white beams crossing in a grid with a deep recessed panel in every square, the white raised-panel wainscot and its moulded chair rail running round the lower walls, the whitewashed painted brick chimney breast rising the full height on the back wall with its plain white mantel shelf, the second-floor gallery landing on the right behind its dark walnut handrail on slim black wrought-iron balusters, the three tall arched-top windows on the left with snow outside, the lit Christmas tree with its deep crimson and antique gold ornaments and its presents, the large oatmeal linen sectional sofa wrapping the foreground, the long upholstered ottoman, the oat flat-weave rug, the pale oak plank floor, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with straight black hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with short dark curly hair, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in warm cream and oatmeal nordic knitted Christmas jumpers with a row of deep-green fir trees and rust-red reindeer across the yoke, charcoal knitted lounge trousers and thick mustard knitted socks, so their knitted jumpers read clearly. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole flat coffered ceiling. Everything glowing on the drywall, the brick and the white beams is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a whole snowy storybook Christmas village running low along the walls with steep-gabled houses and lit shopfronts, a church with a lit steeple and a glowing clock face, market stalls under red-and-white striped awnings and lamp-posts hung with wreaths, a curl of smoke above every single chimney, a frozen silver-blue pond set into the village with tiny skating silhouettes circling on it, an enormous lit FERRIS WHEEL rising out of the village on the left in crimson and gold bulbs and a great golden CAROUSEL under a striped canopy on the right, wide aurora ribbons in deep crimson and ruby red with warm gold and emerald green threaded between them radiating outward from the star overhead, one colossal eight-pointed STAR OF BETHLEHEM filling the entire coffered ceiling with four long rays reaching into its four corners, seven concentric ripple rings spreading outward from it across the ceiling, Santa's sleigh drawn by eight flying reindeer arcing in toward the star with a long tapering trail, a huge pair of ornate gold bells tied with a crimson velvet bow high on one wall, floating glowing baubles and red-and-white striped candy canes drifting at five or six different depths, a dense field of stars of many sizes, long-tailed shooting stars, and a heavy fall of large soft glowing six-point snowflakes and tiny points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the drywall, the brick and the white beams and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE AURORA - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the drywall; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE FERRIS WHEEL AND THE CAROUSEL - both TURN, steadily and without ever stopping. The enormous lit Ferris wheel turns about its lit hub roughly a quarter of a full turn every second, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel turns the other way under its striped canopy at about the same rate, its horses rising and falling on their twisted brass poles as they come round, and the lights along every scallop of the canopy edge chasing round the rim.
- THE RIPPLE RINGS - the seven concentric rings SPREAD OUTWARD from the great star across the coffered ceiling like rings on water, each one travelling away from the core toward the walls, widening and thinning and fading as it goes, while a fresh ring is already forming at the centre behind it, so the spread never stops.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the ceiling beams, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny silhouettes keep circling on the frozen pond and the big gold bells swing gently on their crimson bow with the clappers glowing inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE CHURCH CLOCK - the glowing clock face on the church steeple is the ONLY element that holds its position. It stays exactly where it is in the village for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the drywall, the brick or the white beams. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the oat flat-weave rug, the oatmeal linen sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the flat coffered ceiling fills the upper half of the frame, the aurora rippling along it, the ripple rings still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated coffer panel or an un-animated white beam in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.
```

## Round summary

| card | frame | job | md5 | result |
|---|---|---|---|---|
| C02 | `v10_c02_g1.png` | `55dddc27` | `d38b77b3701b8eedf6e043df06b64d90` | ok |
| C03 | `v10_c03_g1.png` | `89ed549a` | `e58e9890d5aa80815463d1df9093dfb8` | ok |
| C04 | `v10_c04_g1.png` | `1d69a04c` | `498934417d178852b9e60052d36a5d43` | ok |
| C05 F1 | `v10_c05_g1.png` | `c301edff` | `3ba9c28f9de8875b8352b5125ad6fb2e` | ok |
| C05 F2 | `references/v10_c05_r1.png` | `c305720b` | `b0ad50e74cead1123c2871c8a18e6fa6` | ok |
| C06 | `v10_c06_g1.png` | `d9d7d019` | `e71c65b7d47411ce065e9be24cf55296` | ok |
| C07 | `v10_c07_g1.png` | `0beea661` | `5786e65c2c64da048ce631f24883f18b` | ok |

Seven frames, seven jobs, zero failures, zero refusals, zero re-rolls. All 1520 x 2688 PNG. One generation per shot, then stop - Daniel reviews before anything is re-rolled.

## The houses - four newly generated architecture references

**State this plainly: these are not photographs.**

Four real house photographs exist in `../../references/`. All four had already been used twice across v4-v8. Daniel asked for different houses, so reusing them was not an option, and no new real photographs are obtainable here.

Four new architecture references were generated instead - plain, undecorated, daylight, deliberately simple, each built around one clearly legible ceiling structure so that the "make the ceiling make sense" instruction has something honest to attach to. All four were inspected at full size before being accepted as references.

| file | ceiling | used by | media id | md5 |
|---|---|---|---|---|
| `house_great_room_coffered.png` | flat coffered grid, 3 bays across x 5 deep, deep white crown cornice | v9 C05 F2 + C07 | `8e9d9dea-3bcd-4f16-bd98-0730b1661bb0` | `5d9a5645d6f43dd2108fad8eb9209352` |
| `house_bedroom_barrel.png` | shallow barrel vault of white T&G boards off a flat plaster border | v9 C06 | `6c140c66-38ed-4648-8249-3c9de037deae` | `c424911e7fb05609181a5fd50f51305e` |
| `house_great_room_shed.png` | single-slope shed ceiling, narrow white T&G, three black steel tie rods | v10 C05 F2 + C07 | `4dec9045-2ac2-4a2c-8412-6dc4ae08cfc0` | `2500dbc66ef5eb229cac044ecd607c01` |
| `house_bedroom_tray.png` | flat tray ceiling, one rectangle recessed into cream plaster, angled reveal | v10 C06 | `0c193093-94b1-498d-9dfe-4d3f7a8aee03` | `9979f8a7c714dcd2a8ddd60720ed0b84` |

This departs from the rule recorded after v4 - *B-roll 2 geometry always comes off a photograph of a real house*. A real photograph is still the better input. If Daniel can drop four more real interior photographs into `references/`, the next round goes back to photographs and this note goes away.

## Result URLs

CDN base `https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/`

```
v10_c02_g1.png               ->  hf_20260920_141454_55dddc27-3f22-450c-a287-58df40d369c3.png
v10_c03_g1.png               ->  hf_20260920_141453_89ed549a-35bb-4e66-8865-c5a112bc239a.png
v10_c04_g1.png               ->  hf_20260920_141454_1d69a04c-84ad-4a97-8d55-d5ce334848c1.png
v10_c05_g1.png               ->  hf_20260920_141454_c301edff-f38f-42fc-bdde-d914d68ab37d.png
references/v10_c05_r1.png    ->  hf_20260920_141641_c305720b-3c50-4de2-8006-13ff0da79bbf.png
v10_c06_g1.png               ->  hf_20260920_141641_d9d7d019-1e11-4be0-a1fd-bee6b12f8ff9.png
v10_c07_g1.png               ->  hf_20260920_141642_0beea661-fa15-432f-bf8c-1052a0f512cc.png
```

Every file was downloaded from the CDN, copied onto the drive and md5-verified against the download. 14 of 14 matched across both videos.

## Next

1. Daniel reviews the seven frames on the board.
2. Nothing is animated until he picks. Video prompts go in this file under a `### Video prompt` subsection per card, with the reuse lineage recorded.
3. Two decisions are his and are not being made for him: whether the lifted colour ban stays lifted, and whether generated architecture references are acceptable or he would rather supply four more real interior photographs.

## Take 2 round - 2026-09-20 - the three B-roll 2 frames, rebuilt on the approved v9 take 4

**Daniel's note, verbatim:** "Ok do the same for video 10 / Different animation,
houses, kids / In the end add them to the board for both videos"

"The same" is v9 take 4, which he approved: total coverage of every wall and
ceiling surface, razor sharpness with no bloom or haze, ninety-percent-opaque
light, a near-black sky between the elements, a red-led palette and a real
American room. Scope is the same three shots he named for video 9 - C05 FRAME 2
(the reference image, not the starting frame), C06 and C07. The three
"differents" are his: a different projection animation, different houses and
different children from video 9.

### How these prompts were derived

Take 2 is video 10's take 1 with nine blocks LIFTED BYTE-IDENTICALLY out of the
approved v9 take-4 text, plus a wholly new projection scene and two new rooms.
Each lift is asserted to appear exactly once in the v9 source and exactly once
in each finished prompt, so the approved language is *proven* carried over
rather than paraphrased - rewording is the bug Rule 3 exists to stop.

The nine ported blocks: `NO SURFACE IN THE ROOM IS LEFT BARE` (coverage),
`AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK` (near-black sky),
`There is NO falloff anywhere` (no dim edges), the backlit stained-glass
window simile, `It is NOT pale, NOT pastel` (the anti-wash ban),
`ONE SINGLE PROJECTOR sitting low in the near corner` (keystone origin),
`The thousands of points of light are DISCRETE PINPOINTS` (razor sharpness and
the bloom/haze/bokeh bans), `THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT
OPAQUE` and `THE PALETTE IS LED BY RED`.

Paragraph diff against take 1:

```
c05f2   identical: [1, 7, 9]  changed: [0, 2, 3, 4, 5, 6, 8]  chars 11827 -> 18954
c06     identical: [1, 7, 9]  changed: [0, 2, 3, 4, 5, 6, 8]  chars 11472 -> 18268
c07     identical: [1, 7, 9]  changed: [0, 2, 3, 4, 5, 6, 8]  chars 12113 -> 19404
```

Paragraphs 1, 7 and 9 are byte-identical in all three: video 10 keeps its own
camera, framing and poses, its projector-not-visible clause and its no-text
clause exactly as they were.

### The three "differents"

**Different animation.** Every v9 signature was dropped - no pine forest, no
gold onion-domed city, no steam train, no spiral whirlpool, no pale blue moon,
no floating wrapped gifts. The new scene is a snowy storybook CHRISTMAS VILLAGE
low along the walls (steep-gabled houses and shopfronts with warm-gold lit
windows, a church with a lit steeple and a glowing clock face, market stalls
under red-and-white striped awnings, cast-iron lamp-posts hung with wreaths,
smoke from every chimney) with a frozen silver-blue pond and tiny skating
silhouettes as the one cool note; an enormous lit FERRIS WHEEL in crimson and
gold bulbs rising on the left and a gold CAROUSEL under a striped canopy on the
right; overhead a colossal eight-pointed STAR OF BETHLEHEM filling the ceiling,
white-gold core bleeding through gold to ruby tips, with four long rays into
the corners; CONCENTRIC RIPPLE RINGS radiating out from it; Santa's sleigh and
eight reindeer arcing IN toward the star (v9's flew out of the spiral); a huge
pair of ornate gold BELLS with a crimson velvet bow high on one wall; aurora
bands that radiate outward from the star instead of sweeping past in long
curves; and floating glowing BAUBLES and CANDY CANES. The dense star field,
shooting stars, six-point snowflakes and the heavy fall of light points are
kept.

**Different houses.** Two new American architecture references were generated
and inspected at full size before use. They replace `house_great_room_shed.png`
and `house_bedroom_tray.png` used in take 1, and they are structurally
different from v9's cathedral vault and gable-and-batten bedroom.

| file | ceiling | used by | media id / job | md5 |
|---|---|---|---|---|
| `house_great_room_us_coffered.png` | flat deep coffered grid, chunky white crossing beams, one can light per coffer | v10 C05 F2 + C07 | `08f4bcf5-a441-49c5-81c6-ef6a0953c4df` | `48cae106d14969ace9ff3177cc239d8f` |
| `house_bedroom_us_tray.png` | flat tray ceiling, four angled reveals, raised flat panel, crown at the tray edge | v10 C06 | `24b58778-42a3-4a92-a214-553b51e4a904` | `f831dae25e291e66042a8744bfc1de78` |

The great room also carries a raised-panel wainscot with a chair rail, a
whitewashed painted brick chimney breast, three tall arched-top windows and a
second-floor gallery on slim black wrought-iron balusters. The bedroom carries
a four-panel picture-frame moulding accent wall and two double-hung windows.
Both ceilings were chosen because their edges - coffer recesses, beam faces,
tray reveals - give the projection real geometry to break and step over, which
is what the wrap clause needs to bite on.

**Different kids.** Video 10's children stay as cast in take 1 (C06 a boy about
seven with short sandy-blond hair; C07 a girl about eight with short dark curly
hair and a boy about five with straight black hair) - already distinct from
video 9's blonde-ponytail girl and curly light-brown-haired boy. The knitwear
changed: sage-green and cream with cream fir trees became warm cream and
oatmeal nordic jumpers with a row of deep-green firs and rust-red reindeer
across the yoke, with charcoal knitted lounge trousers and thick mustard socks.
Reason: sage green reads muddy under a crimson-led projection. The room
decoration moved from sage-green velvet to crimson velvet for the same reason.

### Two hand patches after the build

1. **`vault` -> `ceiling`.** The lifted `There is NO falloff anywhere` block
   ends "right up into the top corners of the vault", which is correct for v9's
   cathedral vault and wrong for video 10's flat coffered ceiling and flat tray
   ceiling. Replaced with "right up into the corners of the ceiling" in all
   three, single-match asserted. The one remaining `vault` in each prompt is the
   legitimate negation "there is NO vault" in the room description.
2. **`drywall` -> `plaster` in C06 only.** The bedroom is plaster, not drywall,
   but two lifted phrases carried drywall in: "NOT pale drywall" in the
   near-black-sky block and "the tooth of the drywall" in the quality line.
   Both replaced, then verified with a word-boundary regex - zero `drywall` in
   the C06 prompt, eight each in C05 F2 and C07 where the great room really is
   drywall.

**Settings** - gpt_image_2_5, variant sunburst, 2k, quality medium, 9:16,
use_unlim false, workspace Oneofone1. Identical to v9 take 4.

**Lineage** - Reused from v10 take 1 (C05 F2 / C06 / C07) and from v9 take 4 -
changed: the nine approved coverage / opacity / sharpness / palette blocks were
ported byte-identically out of v9 take 4, the projection scene was replaced
wholesale with the village / Ferris wheel / carousel / Star of Bethlehem
animation, both rooms were rebuilt on the two new coffered and tray references,
and the knitwear and Christmas trim moved from sage green to cream-and-crimson.

**References attached**

- C05 F2: @Image 1 `f3a8c329-4152-4a22-9469-d89578812e09`
  (`../video_1_assets/references/v1_c05_r1.png` - owns camera, framing, poses,
  light), @Image 2 `08f4bcf5-a441-49c5-81c6-ef6a0953c4df`
  (`../../references/house_great_room_us_coffered.png` - owns architecture)
- C06: @Image 1 `0a845da6-2607-46cc-a595-4fee4b17d6a9`, @Image 2
  `24b58778-42a3-4a92-a214-553b51e4a904`
  (`../../references/house_bedroom_us_tray.png`)
- C07: @Image 1 `c9a6740d-383b-4829-a7b9-f7a3c079c03f`
  (`../video_1_assets/starting_frames/v1_c07_g1.png`), @Image 2
  `08f4bcf5-a441-49c5-81c6-ef6a0953c4df` - the same great room as C05 F2 on
  purpose; within one ad C05 F2 and C07 are always the same house

**Results**

| shot | file | job | md5 |
|---|---|---|---|
| C05 F2 | `references/v10_c05_r2.png` | `1f88d0ff-b4ae-4d75-a61b-9e36719f41a5` | `16bb99994b8f00f257a53db224b0e31e` |
| C06 | `starting_frames/v10_c06_g2.png` | `37832ca3-a7dd-48b5-ba4e-187e5f082652` | `28bedab0923e7ba11ddb4e2c4e099ed0` |
| C07 | `starting_frames/v10_c07_g2.png` | `9c101565-8f83-4591-9907-7aa314411d73` | `184c18e0f3323b1b7dd74a07e060beef` |

All three 1520 x 2688 PNG, one generation per shot, zero re-rolls, zero
refusals. Each was downloaded from the CDN, copied onto the drive and
md5-verified against the download - 3 of 3 matched.

CDN base `https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/`

```
references/v10_c05_r2.png    ->  hf_20260920_170414_1f88d0ff-b4ae-4d75-a61b-9e36719f41a5.png
v10_c06_g2.png               ->  hf_20260920_170414_37832ca3-a7dd-48b5-ba4e-187e5f082652.png
v10_c07_g2.png               ->  hf_20260920_170716_9c101565-8f83-4591-9907-7aa314411d73.png
```


### C05 F2 - Image prompt (take 2)

```
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its flat coffered ceiling, its beams, its wainscot, its brick chimney breast, its gallery railing, its arched windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm cream and oatmeal nordic knitted Christmas jumpers with a row of deep-green fir trees and rust-red reindeer across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height great room under a FLAT DEEP COFFERED CEILING - one single flat horizontal plane, gridded by chunky white-painted beams crossing each other at right angles into a regular grid of about three bays across by four deep, every square between them a deep recessed coffer panel stepped up above the face of the beams with a crisp moulded edge, and one small flush recessed downlight set in the middle of each coffer; there is NO vault, no slope, no ridge, no rafter and no truss anywhere in this room - the ceiling is one single flat coffered plane; white painted drywall walls carrying a white raised-panel wainscot with a moulded chair rail running around the lower third; on the back wall a tall floor-to-ceiling chimney breast of whitewashed painted brick, every brick and every mortar line legible, with a plain white mantel shelf and a simple firebox under it; on the left a bank of three tall arched-top windows reaching almost the full height of the room, white-framed with slim glazing bars; on the right, above head height, a second-floor gallery landing open to the room behind a dark walnut handrail carried on slim black wrought-iron balusters, with the plain white soffit of the gallery floor beneath it. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground, a long upholstered ottoman and a large oat flat-weave rug. Copy the proportions, the flat coffered grid and the depth of its recesses, the raised-panel wainscot and its chair rail, the whitewashed brick chimney breast, the three arched windows and the gallery railing on its black balusters from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the three tall arched windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight in every coffer and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing against the whitewashed brick chimney breast with warm white lights and deep crimson and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and crimson velvet ribbon laid along the white mantel shelf, cream knitted stockings hanging beneath it, and a large evergreen wreath with a crimson velvet bow hung on the gallery railing. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every white painted drywall wall and the white raised-panel wainscot below them, across the whitewashed brick chimney breast, across the gallery railing and the soffit beneath it, and across the whole flat coffered ceiling - over every recessed coffer panel and over every face of every white beam crossing between them, with no visible edge, no rectangle and no screen. NO SURFACE IN THE ROOM IS LEFT BARE. Every square inch of wall and ceiling the camera can see is inside the projection, and that explicitly includes THE TALL WHITEWASHED BRICK CHIMNEY BREAST ABOVE THE FIREPLACE: the picture crosses it from the mantel shelf all the way up to the ceiling exactly as densely as it crosses everything else, so that brick carries lit village, Ferris wheel, aurora bands, stars and drifting baubles across it and is NEVER a bare white or grey column running up the middle of the frame. The same is true of EVERY SINGLE COFFER PANEL of the ceiling grid and every face of every beam between them, the lower halves of all the walls, the white raised-panel wainscot and its chair rail, the wall above and behind the gallery railing, the white soffit under the gallery floor, the strips of wall between and beside the three arched windows, and the wall on the right - every one of them carries the picture at full density right down to where it meets the floor. If any wall or ceiling surface anywhere in the frame reads as plain paint, plain drywall or plain brick, the image is wrong. LOW ALONG THE WALLS, a whole snowy storybook Christmas village running the full width of the room along the very bottom of the projection - rows of steep-gabled houses and little shopfronts crowded side by side with thick snow heaped on every roof and every small paned window lit warm gold, a tall church rising behind them with a lit steeple and a glowing clock face, a row of market stalls under red-and-white striped awnings with tiny lit wares on them, cast-iron lamp-posts hung with evergreen wreaths lining the little street, and a curl of smoke rising from every single chimney; set into the middle of that village a frozen pond of pale silver-blue ice with a handful of tiny skating silhouettes circling on it, the one cool-coloured thing in the whole picture; rising straight up out of the village on the left an enormous lit FERRIS WHEEL, its great rim and every one of its spokes picked out in crimson and warm gold bulbs, a dozen little gondolas hanging around it and a lit hub at its centre, tall enough to climb most of the height of that wall; and on the right a great golden CAROUSEL under a red-and-white striped canopy, its horses caught mid-rise on twisted brass poles, every scallop of the canopy edge strung with lights and a lit finial on top; ABOVE THE VILLAGE, wide soft aurora ribbons in deep Christmas crimson and glowing ruby red, with warm gold, emerald green and rose magenta threaded between them and only a thin thread of teal, RADIATING OUTWARD FROM THE GREAT STAR OVERHEAD rather than sweeping past in long curves - five or six broad overlapping bands fanning down the walls from that one point, layered over each other so there is very little bare surface left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe; ACROSS THE CEILING OVERHEAD, one colossal EIGHT-POINTED STAR OF BETHLEHEM filling the entire ceiling - four long tapering rays reaching right out into the four corners of the ceiling and four shorter rays between them, a brilliant white-gold core at its centre bleeding outward through warm gold into deep ruby red at the very tips of the rays, the whole star built of countless tiny points of light so it reads as a star of massed light rather than a painted shape, and a fine scatter of sparks trailing off the edge of every ray; CONCENTRIC RIPPLE RINGS spreading outward from that star across the whole ceiling like rings on water, seven of them in crimson and warm gold, each one thinner and fainter than the last as it travels out toward the walls; Santa's sleigh drawn by a team of eight flying reindeer ARCING IN TOWARD the star on a long sweeping curve, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners across the ceiling; a huge pair of ornate gold CHRISTMAS BELLS hanging high on one wall, tied together with a big crimson velvet bow, every scroll of their casting picked out in light and a bright clapper glowing inside each; floating glowing BAUBLES and CANDY CANES drifting through the whole scene at five or six different depths and sizes, the baubles ribbed and faceted in crimson, gold and emerald with a bright cap and a tiny hanging loop, the candy canes striped red and white, the nearest big enough to read the stripe, all of them turning slowly as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the ceiling and every wall; faint wisps of glowing crimson and gold cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS LED BY RED. Deep Christmas crimson and glowing ruby red are the dominant colours of the entire picture, warm gold is second, then emerald green, cream white and rose magenta; soft teal survives only as a thin accent inside one or two of the aurora bands. The aurora ribbons are mostly crimson and ruby with gold and emerald threaded between them, the rays of the great star run from a gold core out to deep red tips, the ripple rings are crimson and gold, the village windows and the church clock burn red-gold, the Ferris wheel and the carousel are strung with crimson and gold bulbs, and most of the floating baubles are crimson and gold. Everything is richly saturated, and the small frozen pond is the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue.  AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn. The great star is a STORYBOOK STAR OF BETHLEHEM made of Christmas light with a sleigh flying in toward it, not a space nebula: it must NOT look like outer space, a galaxy, a supernova, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit snowy village, a Ferris wheel, a carousel, flying reindeer and floating baubles in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely. The white painted drywall, the white coffer beams, the white wainscot panels and the whitewashed brick do NOT read as white anywhere inside the projection field - the light has swallowed their colour. The only things that survive through it are the surface's TEXTURE and its SHADOWS: the slight tooth of the drywall, the moulded edges of the coffers and the wainscot, the faces and mortar lines of the brick, the square corners of the beams. That is the ten percent; the colour of the surface is not part of it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white. Contrast is extreme: the cores of the great star, the Ferris wheel, the carousel and the lit village windows are near-white hot, the mid-tones are deep saturated crimson and emerald, and the empty sky between them is almost black - never pale paint.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.  The flat coffered ceiling is one single plane, so nothing folds at a ridge - instead the grid breaks it everywhere. Every coffer is a sunken box, so the picture STEPS UP into each recessed panel and back down onto the beams between them, and the rays of the great star, the ripple rings and every aurora band visibly kink up and down at every beam they cross, running across the ceiling in a stepped grid rather than as one smooth sheet. The face of each chunky crossing beam that points back toward the projector catches its own bright slice of the picture, offset and stepped from the coffer panel behind it, while the far side and the underside of every beam sit in hard unlit shadow, so the ceiling reads as a lit grid of sunken boxes ribbed by dark beams and never as one flat painted mural. Where the light reaches the top of a wall it breaks again at that corner and runs down the vertical plane at a different angle. The raised-panel wainscot breaks it further, every raised panel and the moulded chair rail catching its own bright band and throwing its own shadow so the picture steps across the lower wall. The whitewashed brick chimney breast breaks it again, every brick catching the light on its own face and every mortar line throwing its own fine shadow. The gallery railing breaks it a fourth time, each slim black baluster catching a bright edge and casting a bar of shadow onto the wall behind it, and the white soffit under the gallery floor takes the picture at its own flat angle. The surface texture stays legible inside the light - the tooth of the drywall, the square edges of the beams and the wainscot panels, the brick faces and their mortar joints - so it still reads as projected light on a real room and never as paint, wallpaper, a sticker or a printed panel. AND EVERY PIECE OF STANDING-PROUD TIMBER AND TRIM THROWS A REAL SHADOW: each chunky coffer beam, each raised wainscot panel, the chair rail and each black baluster casts a hard-edged shadow of itself across the surface behind it, so a dark unlit band runs alongside every beam and every moulding where the picture is blocked. Those cast shadows are the clearest proof that this is light crossing a real room and not a mural, and they must be plainly visible. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room. Three or four thin volumetric shafts of coloured light hang visibly in the air of the room so the beam itself is seen in the space, but they are narrow and crisply defined and they do NOT fog, veil or soften any part of the picture. EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP. Each gable and lit window of the village, each spoke and gondola of the Ferris wheel, each horse and every scallop of the carousel canopy, each antler and harness bell on each reindeer, each arm of each snowflake, each stripe on each candy cane and each ray of the great star has a hard, crisp, precisely drawn edge. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Ferris wheel, no carousel, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the brick and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### C06 - Image prompt (take 2)

```
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its tray ceiling and its four reveals, its panelled accent wall, its walls, its windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about seven with short sandy-blond hair, fully dressed for winter in a warm cream and oatmeal nordic knitted Christmas jumper with a row of deep-green fir trees and rust-red reindeer across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom with a FLAT TRAY CEILING - one big clean rectangle recessed up into the middle of an otherwise flat cream plaster ceiling, with a plain angled reveal stepping up on all FOUR sides from the flat border into a raised flat panel, a crisp crown moulding running around the outer edge of the tray where it meets the border, and small flush recessed downlights set in the flat border; the whole ceiling is smooth plaster and perfectly flat apart from that one rectangular step - there is no vault, no slope, no ridge, no rafter, no beam and no boarding anywhere in this room; soft cream painted walls with plain white skirting; the far wall behind the bed is a full PICTURE-FRAME MOULDING ACCENT WALL - four tall raised rectangular panels side by side, each outlined in a crisp applied moulding that stands proud of the wall, running from skirting to crown; on the right-hand wall two tall white-framed double-hung windows spaced apart, each hung with long cream pinch-pleat curtains on a slim black rod; an upholstered bed with a wide cream headboard standing against the panelled accent wall, two small pale oak nightstands with small cream table lamps, and a long cream upholstered bench on slim pale oak legs at the foot of the bed; a pale oak plank floor under a very large oat flat-weave rug. Copy the proportions, the flat ceiling, the single rectangular tray recess with its four angled reveals and its crown moulding, the four-panel picture-frame moulding accent wall and the two windows on the right from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: both windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and both table lamps are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a deep crimson wool quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking hangs on the panelled wall above the headboard, a warm fairy-light garland is strung around the nearer window, and a small lit Christmas tree with crimson and antique gold ornaments stands on the floor beside the bed. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole picture-frame moulding accent wall behind the bed, the right-hand wall and its windows, the flat cream plaster border of the ceiling, up all four angled reveals and right across the raised tray panel set into the middle of it, wrapping around the corner where wall meets ceiling without a break, with no visible edge, no rectangle and no screen. NO SURFACE IN THE ROOM IS LEFT BARE. Every square inch of wall and ceiling the camera can see is inside the projection, and that explicitly includes THE WHOLE PICTURE-FRAME MOULDING ACCENT WALL BEHIND THE BED: the picture crosses all four raised panels and every moulding between them from the skirting all the way up to the crown exactly as densely as it crosses everything else, so that wall carries lit village, Ferris wheel, aurora bands, stars and drifting baubles across it and is NEVER a bare cream panelled wall behind the child. The same is true of the ENTIRE FLAT BORDER of the ceiling, ALL FOUR ANGLED REVEALS of the tray, the whole raised tray panel in the middle, the crown moulding around its edge, the right-hand wall and the strips of wall between and beside its two windows, and the wall on the left - every one of them carries the picture at full density right down to where it meets the floor. If any wall or ceiling surface anywhere in the frame reads as plain paint or plain plaster, the image is wrong. LOW ALONG THE WALLS, a whole snowy storybook Christmas village running the full width of the room along the very bottom of the projection - rows of steep-gabled houses and little shopfronts crowded side by side with thick snow heaped on every roof and every small paned window lit warm gold, a tall church rising behind them with a lit steeple and a glowing clock face, a row of market stalls under red-and-white striped awnings with tiny lit wares on them, cast-iron lamp-posts hung with evergreen wreaths lining the little street, and a curl of smoke rising from every single chimney; set into the middle of that village a frozen pond of pale silver-blue ice with a handful of tiny skating silhouettes circling on it, the one cool-coloured thing in the whole picture; rising straight up out of the village on the left an enormous lit FERRIS WHEEL, its great rim and every one of its spokes picked out in crimson and warm gold bulbs, a dozen little gondolas hanging around it and a lit hub at its centre, tall enough to climb most of the height of that wall; and on the right a great golden CAROUSEL under a red-and-white striped canopy, its horses caught mid-rise on twisted brass poles, every scallop of the canopy edge strung with lights and a lit finial on top; ABOVE THE VILLAGE, wide soft aurora ribbons in deep Christmas crimson and glowing ruby red, with warm gold, emerald green and rose magenta threaded between them and only a thin thread of teal, RADIATING OUTWARD FROM THE GREAT STAR OVERHEAD rather than sweeping past in long curves - five or six broad overlapping bands fanning down the walls from that one point, layered over each other so there is very little bare surface left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe; ACROSS THE CEILING OVERHEAD, one colossal EIGHT-POINTED STAR OF BETHLEHEM filling the entire ceiling - four long tapering rays reaching right out into the four corners of the ceiling and four shorter rays between them, a brilliant white-gold core at its centre bleeding outward through warm gold into deep ruby red at the very tips of the rays, the whole star built of countless tiny points of light so it reads as a star of massed light rather than a painted shape, and a fine scatter of sparks trailing off the edge of every ray; CONCENTRIC RIPPLE RINGS spreading outward from that star across the whole ceiling like rings on water, seven of them in crimson and warm gold, each one thinner and fainter than the last as it travels out toward the walls; Santa's sleigh drawn by a team of eight flying reindeer ARCING IN TOWARD the star on a long sweeping curve, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners across the ceiling; a huge pair of ornate gold CHRISTMAS BELLS hanging high on one wall, tied together with a big crimson velvet bow, every scroll of their casting picked out in light and a bright clapper glowing inside each; floating glowing BAUBLES and CANDY CANES drifting through the whole scene at five or six different depths and sizes, the baubles ribbed and faceted in crimson, gold and emerald with a bright cap and a tiny hanging loop, the candy canes striped red and white, the nearest big enough to read the stripe, all of them turning slowly as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the ceiling and every wall; faint wisps of glowing crimson and gold cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS LED BY RED. Deep Christmas crimson and glowing ruby red are the dominant colours of the entire picture, warm gold is second, then emerald green, cream white and rose magenta; soft teal survives only as a thin accent inside one or two of the aurora bands. The aurora ribbons are mostly crimson and ruby with gold and emerald threaded between them, the rays of the great star run from a gold core out to deep red tips, the ripple rings are crimson and gold, the village windows and the church clock burn red-gold, the Ferris wheel and the carousel are strung with crimson and gold bulbs, and most of the floating baubles are crimson and gold. Everything is richly saturated, and the small frozen pond is the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue.  AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale plaster and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn. The great star is a STORYBOOK STAR OF BETHLEHEM made of Christmas light with a sleigh flying in toward it, not a space nebula: it must NOT look like outer space, a galaxy, a supernova, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit snowy village, a Ferris wheel, a carousel, flying reindeer and floating baubles in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely. The cream painted plaster, the white crown moulding and the raised panel mouldings of the accent wall do NOT read as pale anywhere inside the projection field - the light has swallowed their colour. The only things that survive through it are the surface's TEXTURE and its SHADOWS: the fine tooth of the plaster, the crisp moulded edge of the tray, the square corners of every applied moulding. That is the ten percent; the colour of the surface is not part of it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white. Contrast is extreme: the cores of the great star, the Ferris wheel, the carousel and the lit village windows are near-white hot, the mid-tones are deep saturated crimson and emerald, and the empty sky between them is almost black - never pale paint.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.  The ceiling is one flat plane with a single tray cut up into it, so nothing folds at a ridge - instead the tray breaks it. The picture runs across the flat border, STEPS UP each of the four angled reveals, each reveal taking it at its own angle and stretching it differently, and carries on across the raised panel in the middle, so the rays of the great star, the ripple rings and every aurora band visibly kink at the crown moulding and again at the top of each reveal. The crown moulding around the tray edge catches its own bright band on the face pointing back toward the projector and throws a hard shadow on the other side, and the reveal on the far side of the tray sits in unlit shadow where it turns away from the beam. Where the light reaches the top of a wall it breaks again at that corner and runs down the vertical plane at a different angle. The picture-frame moulding of the accent wall breaks it further, every applied moulding catching a bright edge on the side facing the projector and casting its own shadow on the other, so the picture steps in and out of each of the four panels. The window casings and the skirting break it again, each catching its own bright edge. The surface texture stays legible inside the light - the fine tooth of the plaster, the square edges of the crown moulding and of every applied panel moulding - so it still reads as projected light on a real room and never as paint, wallpaper, a sticker or a printed panel. AND EVERY PIECE OF STANDING-PROUD TRIM THROWS A REAL SHADOW: the crown moulding at the tray edge, each applied picture-frame moulding on the accent wall, each window casing and the skirting all cast a hard-edged shadow of themselves across the surface behind them, so a dark unlit band runs alongside every moulding where the picture is blocked. Those cast shadows are the clearest proof that this is light crossing a real room and not a mural, and they must be plainly visible. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room. Three or four thin volumetric shafts of coloured light hang visibly in the air of the room so the beam itself is seen in the space, but they are narrow and crisply defined and they do NOT fog, veil or soften any part of the picture. EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP. Each gable and lit window of the village, each spoke and gondola of the Ferris wheel, each horse and every scallop of the carousel canopy, each antler and harness bell on each reindeer, each arm of each snowflake, each stripe on each candy cane and each ray of the great star has a hard, crisp, precisely drawn edge. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Ferris wheel, no carousel, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the plaster, the crisp moulded edges of the panelling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

### C07 - Image prompt (take 2)

```
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its flat coffered ceiling, its beams, its wainscot, its brick chimney breast, its gallery railing, its arched windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with short dark curly hair, the boy is about five with straight black hair. Both are fully dressed for winter in warm cream and oatmeal nordic knitted Christmas jumpers with a row of deep-green fir trees and rust-red reindeer across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height great room under a FLAT DEEP COFFERED CEILING - one single flat horizontal plane, gridded by chunky white-painted beams crossing each other at right angles into a regular grid of about three bays across by four deep, every square between them a deep recessed coffer panel stepped up above the face of the beams with a crisp moulded edge, and one small flush recessed downlight set in the middle of each coffer; there is NO vault, no slope, no ridge, no rafter and no truss anywhere in this room - the ceiling is one single flat coffered plane; white painted drywall walls carrying a white raised-panel wainscot with a moulded chair rail running around the lower third; on the back wall a tall floor-to-ceiling chimney breast of whitewashed painted brick, every brick and every mortar line legible, with a plain white mantel shelf and a simple firebox under it; on the left a bank of three tall arched-top windows reaching almost the full height of the room, white-framed with slim glazing bars; on the right, above head height, a second-floor gallery landing open to the room behind a dark walnut handrail carried on slim black wrought-iron balusters, with the plain white soffit of the gallery floor beneath it. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground, a long upholstered ottoman and a large oat flat-weave rug. Copy the proportions, the flat coffered grid and the depth of its recesses, the raised-panel wainscot and its chair rail, the whitewashed brick chimney breast, the three arched windows and the gallery railing on its black balusters from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the three tall arched windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight in every coffer and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the whitewashed brick chimney breast with warm white lights and deep crimson and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and crimson velvet ribbon laid along the white mantel shelf, cream knitted stockings hanging beneath it, and a large evergreen wreath with a crimson velvet bow hung on the gallery railing. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every white painted drywall wall and the white raised-panel wainscot below them, across the whitewashed brick chimney breast, across the gallery railing and the soffit beneath it, and across the whole flat coffered ceiling - over every recessed coffer panel and over every face of every white beam crossing between them, with no visible edge, no rectangle and no screen. NO SURFACE IN THE ROOM IS LEFT BARE. Every square inch of wall and ceiling the camera can see is inside the projection, and that explicitly includes THE TALL WHITEWASHED BRICK CHIMNEY BREAST ABOVE THE FIREPLACE: the picture crosses it from the mantel shelf all the way up to the ceiling exactly as densely as it crosses everything else, so that brick carries lit village, Ferris wheel, aurora bands, stars and drifting baubles across it and is NEVER a bare white or grey column running up the middle of the frame. The same is true of EVERY SINGLE COFFER PANEL of the ceiling grid and every face of every beam between them, the lower halves of all the walls, the white raised-panel wainscot and its chair rail, the wall above and behind the gallery railing, the white soffit under the gallery floor, the strips of wall between and beside the three arched windows, and the wall on the right - every one of them carries the picture at full density right down to where it meets the floor. If any wall or ceiling surface anywhere in the frame reads as plain paint, plain drywall or plain brick, the image is wrong. LOW ALONG THE WALLS, a whole snowy storybook Christmas village running the full width of the room along the very bottom of the projection - rows of steep-gabled houses and little shopfronts crowded side by side with thick snow heaped on every roof and every small paned window lit warm gold, a tall church rising behind them with a lit steeple and a glowing clock face, a row of market stalls under red-and-white striped awnings with tiny lit wares on them, cast-iron lamp-posts hung with evergreen wreaths lining the little street, and a curl of smoke rising from every single chimney; set into the middle of that village a frozen pond of pale silver-blue ice with a handful of tiny skating silhouettes circling on it, the one cool-coloured thing in the whole picture; rising straight up out of the village on the left an enormous lit FERRIS WHEEL, its great rim and every one of its spokes picked out in crimson and warm gold bulbs, a dozen little gondolas hanging around it and a lit hub at its centre, tall enough to climb most of the height of that wall; and on the right a great golden CAROUSEL under a red-and-white striped canopy, its horses caught mid-rise on twisted brass poles, every scallop of the canopy edge strung with lights and a lit finial on top; ABOVE THE VILLAGE, wide soft aurora ribbons in deep Christmas crimson and glowing ruby red, with warm gold, emerald green and rose magenta threaded between them and only a thin thread of teal, RADIATING OUTWARD FROM THE GREAT STAR OVERHEAD rather than sweeping past in long curves - five or six broad overlapping bands fanning down the walls from that one point, layered over each other so there is very little bare surface left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe; ACROSS THE CEILING OVERHEAD, one colossal EIGHT-POINTED STAR OF BETHLEHEM filling the entire ceiling - four long tapering rays reaching right out into the four corners of the ceiling and four shorter rays between them, a brilliant white-gold core at its centre bleeding outward through warm gold into deep ruby red at the very tips of the rays, the whole star built of countless tiny points of light so it reads as a star of massed light rather than a painted shape, and a fine scatter of sparks trailing off the edge of every ray; CONCENTRIC RIPPLE RINGS spreading outward from that star across the whole ceiling like rings on water, seven of them in crimson and warm gold, each one thinner and fainter than the last as it travels out toward the walls; Santa's sleigh drawn by a team of eight flying reindeer ARCING IN TOWARD the star on a long sweeping curve, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners across the ceiling; a huge pair of ornate gold CHRISTMAS BELLS hanging high on one wall, tied together with a big crimson velvet bow, every scroll of their casting picked out in light and a bright clapper glowing inside each; floating glowing BAUBLES and CANDY CANES drifting through the whole scene at five or six different depths and sizes, the baubles ribbed and faceted in crimson, gold and emerald with a bright cap and a tiny hanging loop, the candy canes striped red and white, the nearest big enough to read the stripe, all of them turning slowly as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the ceiling and every wall; faint wisps of glowing crimson and gold cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS LED BY RED. Deep Christmas crimson and glowing ruby red are the dominant colours of the entire picture, warm gold is second, then emerald green, cream white and rose magenta; soft teal survives only as a thin accent inside one or two of the aurora bands. The aurora ribbons are mostly crimson and ruby with gold and emerald threaded between them, the rays of the great star run from a gold core out to deep red tips, the ripple rings are crimson and gold, the village windows and the church clock burn red-gold, the Ferris wheel and the carousel are strung with crimson and gold bulbs, and most of the floating baubles are crimson and gold. Everything is richly saturated, and the small frozen pond is the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue.  AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn. The great star is a STORYBOOK STAR OF BETHLEHEM made of Christmas light with a sleigh flying in toward it, not a space nebula: it must NOT look like outer space, a galaxy, a supernova, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit snowy village, a Ferris wheel, a carousel, flying reindeer and floating baubles in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely. The white painted drywall, the white coffer beams, the white wainscot panels and the whitewashed brick do NOT read as white anywhere inside the projection field - the light has swallowed their colour. The only things that survive through it are the surface's TEXTURE and its SHADOWS: the slight tooth of the drywall, the moulded edges of the coffers and the wainscot, the faces and mortar lines of the brick, the square corners of the beams. That is the ten percent; the colour of the surface is not part of it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white. Contrast is extreme: the cores of the great star, the Ferris wheel, the carousel and the lit village windows are near-white hot, the mid-tones are deep saturated crimson and emerald, and the empty sky between them is almost black - never pale paint.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.  The flat coffered ceiling is one single plane, so nothing folds at a ridge - instead the grid breaks it everywhere. Every coffer is a sunken box, so the picture STEPS UP into each recessed panel and back down onto the beams between them, and the rays of the great star, the ripple rings and every aurora band visibly kink up and down at every beam they cross, running across the ceiling in a stepped grid rather than as one smooth sheet. The face of each chunky crossing beam that points back toward the projector catches its own bright slice of the picture, offset and stepped from the coffer panel behind it, while the far side and the underside of every beam sit in hard unlit shadow, so the ceiling reads as a lit grid of sunken boxes ribbed by dark beams and never as one flat painted mural. Where the light reaches the top of a wall it breaks again at that corner and runs down the vertical plane at a different angle. The raised-panel wainscot breaks it further, every raised panel and the moulded chair rail catching its own bright band and throwing its own shadow so the picture steps across the lower wall. The whitewashed brick chimney breast breaks it again, every brick catching the light on its own face and every mortar line throwing its own fine shadow. The gallery railing breaks it a fourth time, each slim black baluster catching a bright edge and casting a bar of shadow onto the wall behind it, and the white soffit under the gallery floor takes the picture at its own flat angle. The surface texture stays legible inside the light - the tooth of the drywall, the square edges of the beams and the wainscot panels, the brick faces and their mortar joints - so it still reads as projected light on a real room and never as paint, wallpaper, a sticker or a printed panel. AND EVERY PIECE OF STANDING-PROUD TIMBER AND TRIM THROWS A REAL SHADOW: each chunky coffer beam, each raised wainscot panel, the chair rail and each black baluster casts a hard-edged shadow of itself across the surface behind it, so a dark unlit band runs alongside every beam and every moulding where the picture is blocked. Those cast shadows are the clearest proof that this is light crossing a real room and not a mural, and they must be plainly visible. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room. Three or four thin volumetric shafts of coloured light hang visibly in the air of the room so the beam itself is seen in the space, but they are narrow and crisply defined and they do NOT fog, veil or soften any part of the picture. EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP. Each gable and lit window of the village, each spoke and gondola of the Ferris wheel, each horse and every scallop of the carousel canopy, each antler and harness bell on each reindeer, each arm of each snowflake, each stripe on each candy cane and each ray of the great star has a hard, crisp, precisely drawn edge. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Ferris wheel, no carousel, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the brick and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
```

---

## Upscale round - 2026-09-21 - all seven clips to 2K

Every picked clip in this video was upscaled with **ByteDance Upscale**, driven in
the browser at `https://higgsfield.ai/upscale` because **Model version: Pro is
UI-only** - the MCP `upscale_video` tool rejects `model_version` outright
(`additionalProperties: false`), so Pro cannot be reached from the API.

Settings, identical on all seven except the preset:

```
ByteDance Upscale
Model version: Pro
Resolution:    2K
FPS:           30 fps
Preset:        AIGC   for C01
               Common for C02-C07
```

The upscale carries its source clip's exact filename and lives in
`clips/upscaled/` - the folder is the suffix, per `_tool/NAMING.md`.

| shot | source clip | preset | upscale | upscale job | source | result |
|---|---|---|---|---|---|---|
| C01 | `clips/v10_c01_g2.mp4` | **AIGC** | `clips/upscaled/v10_c01_g2.mp4` | `0130f45a` | 1080x1920 · 24 fps · 5.05 s · 6.9 MB | 1440x2560 · 30 fps · 5.06 s · 10.4 MB |
| C02 | `clips/v10_c02_g1.mp4` | Common | `clips/upscaled/v10_c02_g1.mp4` | `fd30e876` | 720x1280 · 24 fps · 4.05 s · 1.7 MB | 1440x2560 · 30 fps · 4.07 s · 8.5 MB |
| C03 | `clips/v10_c03_g1.mp4` | Common | `clips/upscaled/v10_c03_g1.mp4` | `00a287ff` | 720x1280 · 24 fps · 4.05 s · 1.2 MB | 1440x2560 · 30 fps · 4.07 s · 7.2 MB |
| C04 | `clips/v10_c04_g2.mp4` | Common | `clips/upscaled/v10_c04_g2.mp4` | `3ed7903f` | 720x1280 · 24 fps · 4.05 s · 1.0 MB | 1440x2560 · 30 fps · 4.07 s · 4.9 MB |
| C05 | `clips/v10_c05_g2.mp4` | Common | `clips/upscaled/v10_c05_g2.mp4` | `0c96b304` | 720x1280 · 24 fps · 5.05 s · 2.9 MB | 1440x2560 · 30 fps · 5.06 s · 9.3 MB |
| C06 | `clips/v10_c06_g1.mp4` | Common | `clips/upscaled/v10_c06_g1.mp4` | `10fd6770` | 720x1280 · 24 fps · 5.05 s · 4.3 MB | 1440x2560 · 30 fps · 5.06 s · 10.1 MB |
| C07 | `clips/v10_c07_g1.mp4` | Common | `clips/upscaled/v10_c07_g1.mp4` | `70e5a7b8` | 720x1280 · 24 fps · 4.05 s · 3.8 MB | 1440x2560 · 30 fps · 4.07 s · 8.6 MB |

In every case the **last** take of the shot was the one upscaled - C01 on `g2`,
C04 on `g2`, C05 on `g2`, the rest on `g1`. Cost was 1.62 credits per job,
billed to the **Oneofone1** workspace.

### Result URLs

```
C01  https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_220815_6aef69eb-2c79-434d-9b19-0f57376afc41.mp4
C02  https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_221136_7e896400-4746-4e54-988f-c34e5028ba7c.mp4
C03  https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_221225_bf578994-6189-4be5-be6b-d9cf4d736355.mp4
C04  https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_221304_9f464efa-3855-468b-b6f0-699abe8edbab.mp4
C05  https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_221342_50175d03-bb40-4678-b845-c5e252040253.mp4
C06  https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_221422_a6b7a1ef-724f-4ef7-b15c-3660993e1a5c.mp4
C07  https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_221503_bcbc59c5-2baa-468b-b3a3-780804a396f1.mp4
```

### What was learned

**The preset is sticky across navigations.** After C01 went through on AIGC, a
freshly loaded `/upscale` still read AIGC for the next clip. A preset left
unchecked silently applies the wrong model to the whole rest of a batch, so
every submit in this round went through a guard that read the panel back and
refused to click Upscale unless it said exactly `Pro + 2K + 30fps` and the
intended preset.

**A submit can silently no-op.** The only reliable proof a job was created is
`location.href` flipping from `?media=video--<id>` to `?media=video-job--<id>`.
All fourteen submits in this round were verified that way.

**Done-ness is a hostname, not a video element.** While a job renders, the page
still shows a `<video>` - pointing at the *source* on `d2ol7oe51mr4n9`. It flips
to `d8j0ntlcm91z4` when the upscale lands.

**Every download was byte-checked** against the remote `Content-Length`. C03
came down truncated at 1,703,936 of 7,545,142 bytes and was re-fetched - a
silent short read that a casual eyeball would have missed.


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v10_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v10_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v10_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v10_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v10_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v10_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v10_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c01_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v10_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v10_c01_r1.png` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `references/v10_c05_r1.png` | Embedded PNG `hf-job-id`: `c305720b-3c50-4de2-8006-13ff0da79bbf`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `references/v10_c05_r2.png` | Embedded PNG `hf-job-id`: `1f88d0ff-b4ae-4d75-a61b-9e36719f41a5`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c01_g7.png` | Embedded PNG `hf-job-id`: `ff02562a-4709-4fc1-bade-56457b3e7817`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c02_g1.png` | Embedded PNG `hf-job-id`: `55dddc27-3f22-450c-a287-58df40d369c3`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c03_g1.png` | Embedded PNG `hf-job-id`: `89ed549a-35bb-4e66-8865-c5a112bc239a`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c04_g1.png` | Embedded PNG `hf-job-id`: `1d69a04c-84ad-4a97-8d55-d5ce334848c1`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c05_g1.png` | Embedded PNG `hf-job-id`: `c301edff-f38f-42fc-bdde-d914d68ab37d`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c06_g1.png` | Embedded PNG `hf-job-id`: `d9d7d019-1e11-4be0-a1fd-bee6b12f8ff9`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c06_g2.png` | Embedded PNG `hf-job-id`: `37832ca3-a7dd-48b5-ba4e-187e5f082652`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c07_g1.png` | Embedded PNG `hf-job-id`: `0beea661-fa15-432f-bf8c-1052a0f512cc`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v10_c07_g2.png` | Embedded PNG `hf-job-id`: `9c101565-8f83-4591-9907-7aa314411d73`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |


---

## Verified record — Higgsfield (checked 2026-09-23)

Every file below was matched to the Higgsfield job that produced it: each clip is byte-identical (md5) to its Higgsfield result, each generated image matches its result by exact byte size, and every start frame was checked against the clip job's attached start image. Prompts are the exact text Higgsfield stored for the job — when anything above in this file disagrees, **this section wins**. Reuse protocol (CLAUDE.md rule 3) pastes from here.

**Board corrections made on 2026-09-23**

- C01: the board did not show the exact clip prompt of `v10_c01_g2.mp4`; it now does (text above).
- C01: the board did not show the exact image prompt of `v10_c01_g7.png`; it now does.
- C02: the board did not show the exact clip prompt of `v10_c02_g1.mp4`; it now does (text above).
- C03: the board did not show the exact clip prompt of `v10_c03_g1.mp4`; it now does (text above).
- C04: the board did not show the exact clip prompt of `v10_c04_g2.mp4`; it now does (text above).
- C05: the board did not show the exact clip prompt of `v10_c05_g2.mp4`; it now does (text above).
- C06: the board did not show the exact clip prompt of `v10_c06_g1.mp4`; it now does (text above).
- C07: the board did not show the exact clip prompt of `v10_c07_g1.mp4`; it now does (text above).

### C01 — Stair hall — reaching for the topper

**In the cut:** `starting_frames/v10_c01_g7.png` → `clips/v10_c01_g2.mp4`

#### Image prompt — `starting_frames/v10_c01_g7.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `ff02562a-4709-4fc1-bade-56457b3e7817`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_160252_ff02562a-4709-4fc1-bade-56457b3e7817.png
**References, in submission order**
- @Image 1: `content/video_10_assets/references/v10_c01_r1.png` · Higgsfield media `c39519a8-920d-46b9-ba05-dbffde968da0`

````text
Copy the attached reference photo EXACTLY as a photograph: the same two-storey American entrance hall, the same camera position standing on the hall floor a few steps back and tilted up, the same eye level, the same distance, the same vertical 9:16 framing, the same very tall slim Christmas tree standing in the middle of the frame and rising the full height of the picture past the staircase, the same dark-stained wood staircase with slim black wrought-iron balusters climbing from the lower right of the frame up to the upper left behind the tree, the same second run of railing higher up, the same heavy dark newel post in the lower right corner, the same cream painted walls and white crown moulding, the same pale ceiling across the top, the same open doorway and ceiling fan visible at the left, the same tall painted wooden nutcracker standing at the far left, the same dark polished wood floor. Same composition, same perspective, same scale of the tree, same everything. Change only the people and add the one item below.

THE PEOPLE - REMOVE AND REPLACE: the boy who is up on the staircase in the reference is replaced by a MOTHER in exactly his position, at exactly his height on the stairs, at exactly his distance from the camera and exactly his size in the frame - she is up on the upper run of the staircase behind the slim black wrought-iron railing, leaning far out over that railing toward the Christmas tree, one hand gripping the rail, her other arm stretched out across the gap toward the top of the tree, holding a Christmas tree topper and reaching to set it on the highest tip. She is a mother in her late 20s with dark brown hair in a low ponytail. She is on the STAIRS, over the railing - not on the floor. The man standing at the lower left of the reference is gone. Below her, standing together on the hall FLOOR at the bottom of the frame over to the LEFT side of the frame, on the opposite side of the picture from the staircase and the newel post, well clear of the tree and NOT in front of it - the floor directly in front of the tree's base is left completely empty - with their backs to the camera, small in the frame because they are far below the top of the tree, two children - a boy about 9 with short dark hair and a girl about 4 with short blonde hair - are seen from behind, standing on the floor with their heads tipped back looking up at their mother and at the top of the tall tree, the boy holding the little girl's hand. The tree still towers over all of them and still fills the height of the frame exactly as it does in the reference.

THEIR CLOTHES: all three wear matching American-flag Christmas pyjamas - pyjama tops with bold red and white horizontal stripes and a navy blue yoke across the shoulders covered in small white stars, and matching red and white striped pyjama bottoms, soft brushed cotton, slightly loose the way real pyjamas fit - with thick cream wool socks.

ADD ONE THING: a real fabric United States flag hangs flat against the cream wall in the background at the left, behind the family, clearly readable stars and stripes, hanging straight and still. Keep it modest - about the size of a large poster, noticeably smaller than the tree - so it does not dominate the wall, does not cover the doorway or the staircase, and does not reach up into the empty band of ceiling at the top of the frame.

The tree stays exactly as it is in the reference: the same very tall slim green artificial tree, the same dense old-fashioned dressing of mismatched multicoloured glass baubles, candy canes, snowmen, tinsel garland and warm white string lights, and the same wrapped presents piled at its base. THE VERY TOP OF THE TREE IS BARE - there is no star and no topper sitting on it, because the mother is in the act of reaching out from the stairs to place one there; the gold star topper is in her outstretched hand, held just clear of the highest tip and not yet fixed to it.

FRAMING: leave a clean band of plain empty ceiling across the very top of the image - roughly the top eighth of the frame - free of the tree top, of the star, of the mother's outstretched arm, of the railing and of any other object, so a caption can sit there. Do not pull the camera back or shrink the tree to make that room.

COLOUR: neutral white balance, the way an iPhone auto-corrects a warm room. The picture is NOT orange, NOT amber, NOT sepia and there is no warm colour cast laid over the whole frame. The walls read as clean cream paint, the staircase and floor as natural dark wood, the flag keeps true red, white and navy.

LIGHTING AND QUALITY: bright, clean and evenly lit daytime interior, plenty of light on the walls and on the family, no dark corners, no heavy shadows. Shot on an iPhone and straight out of the camera roll - an ordinary everyday snapshot, not a magazine photo and not a rendered image. Extremely high quality, tack sharp and in focus everywhere, crisp detail in the ornaments, the tinsel and the knit of the pyjamas, realistic skin and fabric texture. Absolutely nothing blurry: no motion blur, no soft focus, no background blur, no bokeh, no grain, no film look, no cinematic grade, no vignette. Normal wide-angle lens, vertical lines vertical and parallel, no fisheye distortion.

No captions, no watermarks, no lettering, no user-interface elements and no social-media overlays anywhere in the image.
````

#### Video prompt — `clips/v10_c01_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `0c62f8eb-758e-45ff-8996-8a20d0a4cae3`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_174043_0c62f8eb-758e-45ff-8996-8a20d0a4cae3.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v10_c01_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c01_g7.png` · Higgsfield media `d64272c4-b6bc-4114-8742-743cf9958aff`

````text
Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the hallway floor holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the staircase behind the dark wooden railing, leaning out over it with one arm stretched up to the gold star on top of the tall decorated Christmas tree beside the stairs. Two small children in matching American-flag pajamas stand on the floor at the lower left of the frame with their backs to the camera, watching her. Wrapped presents at the foot of the tree.

ACTION TIMELINE:
0.0–1.0s — Both hands now on the gold star, she works it down onto the top of the tree, stretching further and further out over the railing, more and more of her weight going onto the tree itself.
1.0–1.6s — The tree tips. It leans away from the stairs toward the open floor and keeps going, and she loses her balance and comes over the railing with it, still holding on. At the same instant the two children take three quick steps further to the left, well out of the way, and stop there — the tree never comes near them.
1.6–2.4s — The whole tree swings down diagonally across the frame and crashes flat onto the wooden floor, branches flattening, the gold star snapping off the top and skittering away on its own.
2.4–3.2s — She lands on the floor face-down across the fallen tree, and the impact bursts a wave of ornaments off the branches — dozens of red, gold, pink and white baubles bouncing out low across the wooden floor and rolling toward the camera, spreading right across the bottom of the frame.
3.2–5.0s — The last ornaments wobble to a stop on the floor. She lies still across the fallen tree for a beat, then lifts her head, blows the hair out of her face and starts laughing. The two children stay where they moved to on the left, staring at the mess. End frame: the tree flat on the floor, ornaments scattered everywhere, her looking up laughing.

AUDIO: her real voice, lip-synced, matching her appearance — a short yelp as she goes over, then breathless laughing at the end; the dry rush of the tree branches going over; the heavy thud of the tree hitting the wooden floor; dozens of glass and plastic ornaments clattering, bouncing and rolling on hard wood; one small surprised squeal from a child. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip, and the two children keep exactly the same clothes and size. The hallway stays pixel-faithful to the start frame — same staircase, same dark wooden railing and newel post, same American flag on the wall, same wooden floor, same daylight. The children are never touched by the tree and are never underneath it. Real weight and gravity — the tree topples on its own mass and stops on the floor, she drops straight down, nobody is thrown or launched. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark. No subtitles, no captions and no on-screen words of any kind anywhere in the picture.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
````

**Other takes of C01 on disk (2)**

#### Image prompt — `references/v10_c01_r1.png`

Not a Higgsfield generation on record (no matching job in the workspace history) — a supplied reference.

#### Video prompt — `clips/v10_c01_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `f5d28b26-a436-49fa-97d5-f80444c846fe`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_171641_f5d28b26-a436-49fa-97d5-f80444c846fe.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c01_g7.png` · Higgsfield media `d64272c4-b6bc-4114-8742-743cf9958aff`
- video ref 1: uploaded image, not on the drive · Higgsfield media `5bc86b80-fbd2-43a2-90dd-53ef8aa2df00`

````text
HIGHEST PRIORITY, READ THIS FIRST: @Video 1 is a motion reference only. Copy its timing, its physics and the way the tree goes over — nothing else. Do NOT copy anything visual from it: not its room, not its people, not its clothes, not its colours, and above all not the text caption burned into its picture. No subtitles, no captions, no on-screen words anywhere in the output. Every person, surface and object in the output comes from the start frame.

Single continuous handheld iPhone shot, 5 seconds, vertical 9:16, filmed by someone standing on the hallway floor holding the phone up — real held-phone look with natural handheld sway, no cuts, no zoom, no lens push-in, framing locked exactly as in the start frame for the whole clip.

Start frame: a woman in American-flag pajamas stands on the staircase behind the dark wooden railing, leaning out over it with one arm stretched up to the gold star on top of the tall decorated Christmas tree beside the stairs. Two small children in matching American-flag pajamas stand on the floor at the lower left of the frame with their backs to the camera, watching her. Wrapped presents at the foot of the tree.

ACTION TIMELINE:
0.0–1.0s — Both hands now on the gold star, she works it down onto the top of the tree, stretching further and further out over the railing, more and more of her weight going onto the tree itself.
1.0–1.6s — The tree tips. It leans away from the stairs toward the open floor and keeps going, and she loses her balance and comes over the railing with it, still holding on. At the same instant the two children take three quick steps further to the left, well out of the way, and stop there — the tree never comes near them.
1.6–2.4s — The whole tree swings down diagonally across the frame and crashes flat onto the wooden floor, branches flattening, the gold star snapping off the top and skittering away on its own.
2.4–3.2s — She lands on the floor face-down across the fallen tree, and the impact bursts a wave of ornaments off the branches — dozens of red, gold, pink and white baubles bouncing out low across the wooden floor and rolling toward the camera, spreading right across the bottom of the frame.
3.2–5.0s — The last ornaments wobble to a stop on the floor. She lies still across the fallen tree for a beat, then lifts her head, blows the hair out of her face and starts laughing. The two children stay where they moved to on the left, staring at the mess. End frame: the tree flat on the floor, ornaments scattered everywhere, her looking up laughing.

AUDIO: her real voice, lip-synced, matching her appearance — a short yelp as she goes over, then breathless laughing at the end; the dry rush of the tree branches going over; the heavy thud of the tree hitting the wooden floor; dozens of glass and plastic ornaments clattering, bouncing and rolling on hard wood; one small surprised squeal from a child. (no BGM). No subtitles.

REALISM — HARD RULES: she keeps exactly the same face, hair and American-flag pajamas as the start frame the whole clip, and the two children keep exactly the same clothes and size. The hallway stays pixel-faithful to the start frame — same staircase, same dark wooden railing and newel post, same American flag on the wall, same wooden floor, same daylight. The children are never touched by the tree and are never underneath it. Real weight and gravity — the tree topples on its own mass and stops on the floor, she drops straight down, nobody is thrown or launched. Real phone-camera look, slight sensor noise, mild motion blur on the fall, no cinematic bokeh, no slow motion, no text overlays, no watermark.

POSITIVE LOCKS: everything plays at real-time speed. One continuous take from 0.0s to 5.0s. The camera never moves from where it is in the start frame.
````

### C02 — Hands on the box

**In the cut:** `starting_frames/v10_c02_g1.png` → `clips/v10_c02_g1.mp4`

#### Image prompt — `starting_frames/v10_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `55dddc27-3f22-450c-a287-58df40d369c3`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141454_55dddc27-3f22-450c-a287-58df40d369c3.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c02_g1.png` · Higgsfield media `1cdfcc53-e771-4bba-9eab-b1788346098b`
- @Image 2: `product_images/box_festive_green_g2.png` · Higgsfield media `2597b25d-60d1-4060-9602-32b0ee26c2f7`

````text
Copy the FIRST attached reference photo EXACTLY: same camera position, same top-down-ish angle, same distance, same vertical 9:16 framing, same table surface at the same height and same angle, same two hands resting on the box in the same position and same grip, same arms entering frame the same way. Keep OUR product box exactly as it appears in the FIRST reference and in the SECOND attached reference: a tall upright rectangular tuck-top carton, square footprint, roughly 15 x 15 x 24 cm, forest green body, dark red band across the top with a gold THEXMASGLOW wordmark, cream serif headline CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed render of a smooth white dome-topped cylindrical projector on a separate white four-legged splayed stand base, slim red remote printed beside it, gold village skyline along the bottom, no transparent window. Keep the box at the same position, scale and angle it occupies in the FIRST reference. Change only three things.

FIRST - THE HANDS. A woman's hands, about 32, slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep burgundy wool sweater pushed back at both wrists. Same position on the box, same grip, same arms entering the frame the same way, same scale.

SECOND - THE TABLE. The surface under the box is no longer bare timber. It is now a limed white-oak table top: a pale blond timber whose open grain is filled with a chalky white lime wax so the pores read as fine white lines drifting across the surface, finished dead matte with no sheen at all, with a simple square edge. Same height, same angle, same amount of the surface visible as in the FIRST reference.

THIRD - THE BACKGROUND. Behind and above the table, a softly defocused Nantucket coastal cottage Christmas parlour: walls of chalk-white painted shiplap boards, a chalk-white painted brick fireplace with a simple pale oak mantel and cream knitted stockings hanging from it, a decorated Christmas tree with warm white fairy lights and antique gold and pearl-white ornaments standing off to one side, a narrow shelf high on the wall carrying a row of pale green sea-glass jars, all well out of focus so the box stays the clear subject.

Dress the limed oak table more festively: a sprig of fir and a few white berries, two or three small antique gold and pearl-white baubles, a short cream candle, a soft warm string light trailing across the matte limed oak, all at the edges of frame so the box stays the clear subject.

Shot on an iPhone 16 Pro, photorealistic, extremely high quality, tack-sharp focus on the box and the hands, crisp legible detail in the printing on the carton, perfect natural realistic lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

The wordmark printed on the red band must read exactly THEXMASGLOW - eleven letters, T-H-E-X-M-A-S-G-L-O-W, correctly spelled, sharp and legible, with no invented or misspelled brand name anywhere on the carton.

No captions, no watermarks, no added lettering anywhere in the image other than the printing on our own carton.
````

#### Video prompt — `clips/v10_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `fa2b2ff0-ef25-46e7-be38-b5dff31c2247`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_fa2b2ff0-ef25-46e7-be38-b5dff31c2247.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v10_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c02_g1.png` · Higgsfield media `63c5d03c-c834-49b7-90a0-07931c541e52`
- video ref 1: `references/scene_no_audio-2.mp4` — upload · 2.14 s · Higgsfield media `1d2e8a8d-1e49-422a-8b04-d1a1230096a4`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. The attached reference video is SILENT and has no audio track at all - take nothing from it but movement. If any music appears anywhere in the 4 seconds the clip is wrong.

BOTH HANDS RULE - SECOND MOST IMPORTANT: this is a TWO-HANDED lift and it is the thing the last take got wrong. From the moment the hands take hold of the projector inside the box until it has left the top of the frame, BOTH hands are on it at once - one hand on the left side of the dome, the other hand on the right side of the dome, thumbs on the near side, fingers curled around the far side. The left hand never lets go, never opens, never drops back to the table, never rests on the box rim or on a lid flap, and never leaves the product for a single frame. Both hands rise together, both hands carry it out of the top of frame together. This is never a one-handed lift.

EXIT RULE - THIRD MOST IMPORTANT: the projector does NOT stay in frame at the end. The hands lift it out of the box and KEEP GOING, carrying it straight up and completely out of the top of the frame. At 4.0s the projector is GONE from the picture and only the open carton is left on the table. The hands never stop, never hold the product up for inspection, never settle, never pause.

SPEED RULE - FOURTH MOST IMPORTANT: the hands work at a brisk, confident, real-time pace. This is a normal person opening a box at normal speed, not a careful slow-motion demonstration. The lift is QUICK and decisive. Do not slow anything down.

TASK: image-to-video. The start image is frame 0.0s. Hold its table, box artwork, props and lighting exactly.

[1] SUMMARY
First-person POV: two hands open a tall dark-green Christmas carton on a limed white-oak table, lift the white projector briskly straight up out of it and carry it out of the top of frame. Locked POV looking down. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm domestic Christmas light, crisp and sharp, correctly exposed. Very slight handheld drift. Real-time speed throughout. No cinematic grade, no grain, no slow motion, no speed ramp.

[3] ASSET ROLES
The start image controls the table, the carton artwork, the hands, the candle, the props and the light. @Video 1 controls ONLY the mechanics of the unboxing: fingers slide under the front lid flap, flaps fold up and back, hands grip the unit inside, the unit lifts straight up. Do not copy the table, the box design, the room, the hands or the product from @Video 1. Do NOT copy the pacing from @Video 1 - use the faster timeline below. Do NOT copy its ending - in this clip the product leaves the frame.

[4] OBJECTS
THE BOX - a dark-green tuck-top carton standing upright, front panel facing camera, a dark red band across the top with a gold THEXMASGLOW wordmark, the cream serif words CHRISTMAS LIGHT PROJECTOR, a gold star-and-tree burst over a printed white dome-topped projector on a white four-legged splayed stand, a gold village skyline along the bottom, no transparent window. About 15 x 15 x 24 cm. Plain interior, no insert, no foam tray.
THE PROJECTOR - inside THE BOX: a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two hands, a woman's, with the cuff of a deep burgundy wool sweater pushed back at each wrist and no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - a limed white-oak table fills the frame: pale blond timber whose open grain is filled with a chalky white lime wax so the pores read as fine white lines drifting across the surface, finished dead matte with no sheen at all, and a simple square edge. A lit cream pillar candle sits at the left, fir sprigs with white berries and small antique gold and pearl-white baubles beside it, and behind it, softly out of focus, chalk-white painted shiplap boards, a chalk-white painted brick fireplace with a simple pale oak mantel and cream knitted stockings hanging from it, a narrow shelf high on the wall carrying a row of pale green sea-glass jars, and a decorated Christmas tree with warm white fairy lights and antique gold and pearl-white ornaments. The candle, the fir, the berries, the baubles, the defocused fireplace and the defocused tree must still be in the final frame.

[6] FIRST FRAME - exactly the start image: THE BOX closed and upright, both HANDS gripping its sides.

[7] TIMELINE - brisk real-time pacing, every beat lands on time
0.0-0.7s - camera locked. The fingers of both HANDS slide under the front top flap of THE BOX and lift it sharply; the tuck tongue pops out of the front panel.
0.7-1.4s - the lid flaps fold upward and backward away from camera on the rear fold in one quick motion, staying attached to THE BOX; the dark interior comes into view.
1.4-2.1s - both HANDS drop straight down into THE BOX and grip THE PROJECTOR by its sides, thumbs on the near side. The BLACK perforated mesh disc on its top face is clearly visible.
2.1-3.0s - THE HANDS lift THE PROJECTOR QUICKLY and decisively straight up and out of THE BOX in one brisk continuous vertical pull, clearing the rim in well under a second. The BLACK top face is clearly visible as it rises.
3.0-3.6s - the HANDS DO NOT STOP. They keep rising in the same continuous motion; THE PROJECTOR travels up towards the top edge of frame, first the stand then the dome crossing the edge and leaving the picture.
3.6-4.0s - THE PROJECTOR and both HANDS are completely OUT OF FRAME. The frame holds on the open empty carton on the limed white-oak table, lid flaps folded back, with the candle, the fir, the berries, the defocused fireplace and the defocused tree still in shot. Nothing else moves.

[9] CAMERA AND OPTICS - one static POV looking down at the table at roughly 50 degrees, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. The camera NEVER follows the product upward - it stays exactly where it is and lets the product exit the frame. No push-in, no orbit, no zoom, no tilt, no cut.

[10] LIGHTING - warm indoor candle and fairy-light mix, unchanged for the whole clip.

[11] PHYSICS - cardboard behaves like cardboard: the flaps crease on their folds and stay attached to THE BOX. THE BOX stays flat on the table and does not slide, tip or lift. The box rim rocks very slightly as the product is pulled out quickly, and settles once the hands have gone.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly two things and nothing else: cardboard flaps creasing and fingers moving on the carton. Total silence apart from those. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the lid is never lifted off, never removed, never carried aside, never set down. THE BOX never leaves the table. Exactly two hands, and both of them are on the product for the whole lift and the whole exit. The top face of THE PROJECTOR is BLACK. The lift out of the box is fast. THE PROJECTOR exits the top of frame and the last frame shows only the open box on the table.
BANNED: any music, any song, any score, any soundtrack; a one-handed lift; either hand letting go of the product, opening, dropping back to the table, resting on the box rim or on a lid flap, or leaving the product at any moment while it rises or exits; only one hand visible on the product; the product still held in frame at 4.0s; the hands stopping, hovering, settling or presenting the product; the camera tilting or panning up to follow the product; slow motion; a slow or hesitant lift; an all-white product top, a lens on the front, a swivel camera head, a third hand, the candle, the fir or the berries disappearing, the box vanishing, a second box, a cut, subtitles, on-screen text.
````

### C03 — The projector lifted

**In the cut:** `starting_frames/v10_c03_g1.png` → `clips/v10_c03_g1.mp4`

#### Image prompt — `starting_frames/v10_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `89ed549a-35bb-4e66-8865-c5a112bc239a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141453_89ed549a-35bb-4e66-8865-c5a112bc239a.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c03_g3.png` · Higgsfield media `7ccdd557-bfee-45b0-a067-0652320f537b`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

KEEP IDENTICAL TO @Image 1: the camera position, the camera height, the lens, the distance, the vertical 9:16 crop, the exact pose of both hands, the exact grip on the product, the product's size and position and tilt in frame, where each forearm enters the frame, and the countertop.

THE COUNTERTOP MUST BE IN FRAME. Exactly as in @Image 1, the countertop occupies the LOWER RIGHT of the frame as a clean wedge running diagonally, passing behind and below the right forearm, clearly visible right up to the bottom edge of the picture. DO NOT remove the countertop. DO NOT replace the lower part of the frame with floor. NO floor is visible anywhere in this shot.

THE POSE - two hands hold the projector UP IN THE AIR just above the countertop, lifted clear of it, nothing touching the unit but the fingers, with a visible gap of air between the base of the stand and the counter below. Same pose and same grip as @Image 1.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch. Left forearm enters from the lower left in a deep burgundy wool sweater sleeve pushed back; right forearm enters from the right in the same deep burgundy sleeve, smooth bare forearm. Same positions, same grip, same entry points, same scale as @Image 1.

SCALE AND PLACEMENT - the product fills about one quarter of the frame height and sits just right of the centre line, a little above the middle of the frame, exactly the same size and place as in @Image 1. Do not shrink it. Do not pull the camera back.

THE PRODUCT - a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible and angled slightly toward the lens. Do not render an all-white top.

THE COUNTER - this is the second change. It is no longer marble. It is now a thick end-grain walnut butcher-block counter: a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge, and a low satin oil finish. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A Nantucket coastal cottage Christmas kitchen, softly defocused: chalk-white shaker cabinets with polished nickel bin pulls, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a cream enamel range set into the tall cabinet run on the left, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look, shallow depth of field on the background only.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v10_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `97937cae-55f3-488f-8307-5294b09bb075`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_97937cae-55f3-488f-8307-5294b09bb075.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v10_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c03_g1.png` · Higgsfield media `3caebb7b-da16-4703-a637-fab90311dcd7`

````text
AUDIO RULE - HIGHEST PRIORITY, READ THIS FIRST: this clip has NO MUSIC OF ANY KIND. No background song, no soundtrack, no score, no melody, no instruments, no singing, no humming, no jingle, no Christmas song, no festive music bed, no ambient musical pad, no strings, no piano, no bells used as music. The audio track contains ONLY real natural sound recorded in that room. If any music appears anywhere in the 4 seconds the clip is wrong.

NATURALNESS RULE - SECOND MOST IMPORTANT: these are REAL HUMAN HANDS, not a robot arm and not a CGI animation. Human hands are never perfectly steady and never move on a perfectly straight mechanical line. Throughout the whole descent the hands carry a small living tremor, the wrists flex slightly, the fingers re-seat their grip once, and the object drifts a few millimetres off true as a real person would let it. The descent slows naturally as it nears the counter the way a person eases something down, instead of arriving at constant speed. Nothing about this movement may look mechanical, robotic, motorised, gliding, floating, animated or rigged.

TASK: image-to-video. The start image is frame 0.0s. Hold its kitchen, counter, hands and lighting exactly.

[1] SUMMARY
First-person POV: two real hands hold the white projector high above a thick end-grain walnut butcher-block kitchen counter, then lower it and set it down naturally. Locked POV. 4 seconds, one take.

[2] GLOBAL STYLE
Real handheld phone POV, warm modern kitchen light, extremely sharp and clean, correctly exposed. Very slight handheld drift. Documentary realism. No cinematic grade, no grain, no slow motion.

[3] ASSET ROLES
The start image controls the kitchen, the counter, the hands and the product. It is the only authority on the scene.

[4] OBJECTS
THE PROJECTOR - a matte-white dome-shaped body on a separate white four-legged splayed stand. Set into the top of the dome is a flat circular BLACK perforated mesh disc. The top face is BLACK and stays black for every frame. No front lens, no camera head, no swivel.
THE HANDS - exactly two real human hands holding THE PROJECTOR, entering from the bottom of frame, a woman's, in deep burgundy wool sweater sleeves pushed back at both wrists, no jewellery of any kind - no rings, no bangle, no watch.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a thick end-grain walnut butcher-block countertop - a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish - fills the lower half of frame and stays there for the whole clip; behind it a warm Christmas kitchen with chalk-white shaker cabinets with polished nickel bin pulls, a cream enamel range built into the tall cabinet run on the left, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE HANDS holding THE PROJECTOR in the air above the butcher-block counter.

[7] TIMELINE
0.0-0.8s - camera locked. THE HANDS raise THE PROJECTOR upward away from the counter until the bottom of the stand is roughly 35 cm above the counter, with a natural small overshoot and correction at the top of the lift. THE PROJECTOR now sits high in the upper half of frame with a large clear gap of air between the stand feet and the timber. THE PROJECTOR STARTS HIGH - this gap is what the rest of the clip travels through.
0.8-1.2s - the hands pause for a beat and the fingers re-seat their grip on the sides of the dome, the way a person adjusts their hold before setting something down.
1.2-3.0s - THE HANDS lower THE PROJECTOR down through that gap toward the timber in one continuous human descent, carrying a small natural tremor, easing slower and slower as the feet approach the timber.
3.0-3.4s - the four feet of the stand touch the timber; the hands relax their pressure and the object settles flat with a tiny real-world adjustment.
3.4-4.0s - THE HANDS open, release THE PROJECTOR and withdraw downward out of frame, leaving THE PROJECTOR standing alone on the counter.

[9] CAMERA AND OPTICS - one static POV looking down at the counter, vertical 9:16, normal wide-angle phone lens, very slight handheld drift only. No push-in, no orbit, no zoom, no tilt, no cut. Normal wide-angle only - no fisheye, no barrel distortion, no curved cabinet lines.

[10] LIGHTING - warm white under-cabinet light plus the soft warm glow of the small Christmas tree in the far corner, unchanged for the whole clip.

[11] PHYSICS - THE PROJECTOR is a solid rigid object with real weight and the hands are visibly carrying that weight. It stays essentially upright but is allowed the tiny tilts a real hand-held object has. The butcher block is hard: contact is a small firm settle. The fingertips whiten very slightly where they press the dome.

[12] AUDIO - DRY DOCUMENTARY AUDIO ONLY. The track contains exactly one thing and nothing else: a soft contact tap when the stand meets the timber, in a quiet kitchen. Total silence apart from that. NO MUSIC, NO SONG, NO SCORE, NO SOUNDTRACK, NO INSTRUMENTS, NO VOICE.

[13] POSITIVE LOCKS - the movement reads as a real person's hands at every moment. The countertop and the kitchen behind it are visible in every single frame. The top face of THE PROJECTOR is BLACK. Exactly two hands. The descent travels the full 35 cm gap.
BANNED: any music, any song, any score, any soundtrack; robotic, mechanical, motorised, gliding, floating or animated movement; perfectly constant speed; the object appearing to hover unsupported; the countertop disappearing, the kitchen being replaced by a plain or dark background, an all-white product top, a lens on the front, a swivel camera head, a third hand, the product tipping over or spinning, the camera moving, a cut, subtitles, on-screen text.
````

### C04 — The cable going in

**In the cut:** `starting_frames/v10_c04_g1.png` → `clips/v10_c04_g2.mp4`

#### Image prompt — `starting_frames/v10_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `1d69a04c-84ad-4a97-8d55-d5ce334848c1`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141454_1d69a04c-84ad-4a97-8d55-d5ce334848c1.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c04_g3.png` · Higgsfield media `0327ed0d-ff56-40c1-a9a9-389a7ceb9916`

````text
COPY @Image 1 EXACTLY. The ONLY things that change are the hands, the countertop material and the kitchen behind them. Everything else is a literal copy.

CAMERA - follow this precisely. The phone is held CLOSE, only just above the level of the countertop, and tilted down gently - a shallow downward angle, not a top-down one. The product is LARGE in frame: its white dome is about one third of the frame width and sits slightly LEFT of the centre line, a little above the middle of the frame. The counter surface fills the lower two thirds as a near foreground plane. DO NOT shoot from high above. DO NOT use a steep downward angle. DO NOT show a wide empty expanse of countertop. DO NOT make the product small in the frame. The front edge of the counter is not visible. NO floor is visible anywhere in this shot.

THE PRODUCT - standing upright ON the countertop: a compact matte-white rounded dome-shaped body on a small white four-legged splayed stand. The TOP FACE of the dome is a flat BLACK circular perforated mesh lens panel, clearly visible from this angle. Do not render an all-white top.

THE HANDS - this is the first change. They are now a woman's hands, about 32: slender fingers, narrow wrists, smooth bare skin, short clean natural nails with no polish, no jewellery of any kind - no rings, no bangle, no watch - the cuffs of a deep burgundy wool sweater pushed back at both wrists. Same positions, same actions and same scale as @Image 1: her LEFT hand enters from the left edge of the frame, fingers curled around the left side of the white dome, steadying it; her RIGHT hand enters from the lower right, thumb and index finger pinching the end of a slim white USB-C connector and pushing it toward the small port on the white stand at the base of the unit, the connector only a couple of centimetres from the port, arm mid-reach, clearly about to plug it in. The white cable trails away to the right across the counter and off the frame. Both the connector and the port must be unobstructed and clearly readable.

THE COUNTER - this is the second change. It is no longer marble. It is now a thick end-grain walnut butcher-block counter: a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge, and a low satin oil finish. Same shape, same position and the same amount of it in frame as in @Image 1.

THE KITCHEN - this is the third change. A Nantucket coastal cottage Christmas kitchen, softly defocused across the top third of the frame: chalk-white shaker cabinets with polished nickel bin pulls, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a cream enamel range set into the tall cabinet run on the right, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries running high along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. Evening interior light, warm white, clean and even.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp on the hands, the cable and the product, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no logos, no lettering anywhere in the image.
````

#### Video prompt — `clips/v10_c04_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `2cc97b1c-181d-495c-a8db-6d6e43fd014c`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_204700_2cc97b1c-181d-495c-a8db-6d6e43fd014c.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v10_c04_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c04_g1.png` · Higgsfield media `7963ee51-0e88-44d3-b10a-a3458a6ae8ac`

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
THE LEFT HAND - a woman's hand in a deep burgundy wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same deep burgundy sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
THE PORT - a small dark oval USB-C socket set into the white plastic at the very bottom rim of the dome body, just above where the dome meets the white stand, a little right of the dome's centre line. It is clearly visible in the start image and it is the only opening on the product. It is NOT on the stand, NOT on the back, NOT on the top. It stays open and visible until the connector fills it, and it never disappears, closes over or moves.
THE CONNECTOR - a white plastic USB-C plug on a white cable, held between the right thumb and forefinger. Its dark flat metal tongue points LEFT, straight at THE PORT, with a gap of roughly two centimetres between the tip and the socket at 0.0s. The plug and THE PORT are already lined up on the same horizontal axis - all that is missing is the push.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a thick end-grain walnut butcher-block countertop - a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish - fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with chalk-white shaker cabinets with polished nickel bin pulls, a cream enamel range built into the tall cabinet run on the right, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.2s - camera completely locked. THE RIGHT HAND drives THE CONNECTOR straight to the LEFT along its own axis and PLUGS IT IN. The two-centimetre gap closes, the dark metal tongue enters THE PORT and disappears completely inside the dome, and the white plastic shoulder of the plug comes to rest flush against the white rim with no gap left between plug and dome. THIS IS THE SINGLE MOST IMPORTANT EVENT IN THE CLIP: the plug must visibly travel, enter the hole, and stay in it. The hand pushes once, firmly and in one go - it does not hover, hesitate, drift, retreat, tap the outside of the dome, slide along the rim, or hold the plug in mid-air. The white cable trails away to the right across the timber and stays slack. THE LEFT HAND stays still on the dome.
1.2-2.0s - THE CONNECTOR is now fully seated and stays seated for the rest of the clip; it never comes back out. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the timber around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND lets go of the seated plug - which stays in THE PORT - and relaxes onto the counter beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.2s onward. The red light is a local glow on the product and the timber immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - THE CONNECTOR ends the clip FULLY INSERTED into THE PORT, its metal tongue hidden inside the dome and its white shoulder flush against the white rim; anyone watching can see the plug go into the hole. The light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: a plug that stops short of the socket; a plug that never moves; a plug pressed against the outside of the dome or the stand instead of entering the socket; a plug pushed into the stand, the base tray, the back or the top instead of the rim socket; a plug that goes in and then comes back out; a plug left hovering in mid-air at the end; a hand that only holds or fiddles with the cable; THE PORT closing over, healing, vanishing or moving to another part of the product; a second socket appearing; blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

**Other takes of C04 on disk (1)**

#### Video prompt — `clips/v10_c04_g1.mp4`

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `3509e6c7-63ff-470b-b008-973b1d514135`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_3509e6c7-63ff-470b-b008-973b1d514135.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c04_g1.png` · Higgsfield media `7963ee51-0e88-44d3-b10a-a3458a6ae8ac`

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
THE LEFT HAND - a woman's hand in a deep burgundy wool sweater sleeve pushed back, no jewellery of any kind - no rings, no bangle, no watch - resting on the left side of the dome. It does not move.
THE RIGHT HAND - a woman's hand in the same deep burgundy sleeve, no jewellery, entering from the right edge of frame, holding a white cable connector near the base of the stand.
COUNT LOCK: exactly two hands for the whole clip.

[5] LOCATION - hold every one of these, they exist in the start image and must survive to the last frame: a thick end-grain walnut butcher-block countertop - a mosaic of small square end-grain blocks in warm chocolate brown, each block showing its own ring pattern and the joints reading as a fine chequered grid across the whole surface, a softly eased square edge and a low satin oil finish - fills the lower two thirds of frame and stays there for the whole clip; behind it a warm Christmas kitchen with chalk-white shaker cabinets with polished nickel bin pulls, a cream enamel range built into the tall cabinet run on the right, a chalk-white zellige tile backsplash whose handmade glaze is uneven and catches the light in irregular patches, a warm white LED strip glowing under the upper cabinets, a thick pine garland with small warm fairy lights and white berries along the top of the cabinetry, and a small decorated Christmas tree with warm white lights glowing softly in the far corner. The kitchen stays soft and out of focus. Do not remove the countertop. Do not replace the kitchen with a plain wall, a studio backdrop or a dark room.

[6] FIRST FRAME - exactly the start image: THE PROJECTOR unlit on the counter, THE LEFT HAND on the dome, THE RIGHT HAND holding the white cable connector beside the base.

[7] TIMELINE
0.0-1.0s - camera completely locked. THE RIGHT HAND pushes the white cable connector horizontally into the port on the side of the white stand base. THE LEFT HAND stays still on the dome.
1.0-2.0s - the connector seats fully. A thin RED light ring ignites in the seam between the white dome and the white stand base and glows steadily.
2.0-3.0s - the BLACK perforated mesh disc on top of the dome fills with a dense field of small RED points of light, like a red starfield, brightening from the centre outward across the black disc. A soft RED glow spills onto the timber around the base of the stand.
3.0-4.0s - the RED light settles and holds at full brightness; the small red points shimmer very slightly. THE RIGHT HAND relaxes and rests beside the base. Nothing else moves.

[9] CAMERA AND OPTICS - one absolutely locked-off shot, vertical 9:16, normal wide-angle phone lens, close on the product over the counter. FREEZE MEANS FREEZE: no drift, no wobble, no micro-motion, no push-in, no handheld shake, no reframe, no zoom, no cut. Normal wide-angle only - no fisheye, no barrel distortion.

[10] LIGHTING - warm white under-cabinet kitchen light for the whole clip; the only lighting change is the RED light emitted by THE PROJECTOR itself from 1.0s onward. The red light is a local glow on the product and the timber immediately around it - it does not repaint the whole kitchen.

[11] PHYSICS - THE PROJECTOR is a rigid object bolted to the spot; it does not shift, rock, rotate or lift when the cable is pushed in. The cable is flexible and bends slightly as it seats.

[12] AUDIO - natural room sound only: a small plastic click as the connector seats. No music, no speech, no score.

[13] POSITIVE LOCKS - the light is RED and only RED. The top face of THE PROJECTOR is BLACK and the red starfield appears ON that black disc. The countertop and the kitchen behind it are visible in every single frame. Exactly two hands. The camera never moves.
BANNED: blue light, white light, green light, amber light, multicoloured or rainbow light; a beam projected onto the ceiling or the walls; the product moving, lifting or rotating; the camera moving in any way; an all-white top face; the countertop or the kitchen disappearing; a third hand; a cut; subtitles; on-screen text; music.
````

### C05 — The door opens on the room

**In the cut:** `starting_frames/v10_c05_g1.png`, `references/v10_c05_r2.png` → `clips/v10_c05_g2.mp4`

#### Image prompt — `starting_frames/v10_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `c301edff-f38f-42fc-bdde-d914d68ab37d`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141454_c301edff-f38f-42fc-bdde-d914d68ab37d.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c05_g2.png` · Higgsfield media `c9e1f960-9e19-4b9b-ad88-8f5298db1880`

````text
Recreate @Image 1 with two changes.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo, the same dim hallway, the same antique brass round doorknob in the same place, the same small pine wreath with the red velvet bow hung on the door, the same oak floorboards, the same woman's forearm entering from the lower right with the thin gold bangle and deep burgundy sleeve, her hand closed around the knob, the same camera position and camera height, the same warm low-key evening light.

CHANGE 1 - THE DOOR. It is no longer a white panelled door. It is now a classic American four-panel door painted a deep oxblood red in a soft eggshell finish: crisp raised mouldings around four flat recessed panels, two tall ones below and two short ones above, clean painted surfaces with the faintest brush texture, an antique brass knob and a matching antique brass escutcheon plate, set in a plain painted cream frame. Same size, same position in frame, same flat-on angle as @Image 1.

CHANGE 2 - the door is FULLY CLOSED and flush in its frame. There is NO gap at the edge of the door and absolutely NO light spilling out - no rainbow strip, no coloured glow, no bright line, no glare anywhere along the door edge, the jamb, the threshold or the floor. The seam between door and frame is a plain dark shadow line only. Nothing behind the door is visible or lit.

THE WREATH - it hangs on the FACE of the door, centred on the upper half of the door and comfortably inside the frame with clear painted door visible all the way around it. It must NOT be cut off by the right edge of the picture and must NOT drift onto the door frame or the wall. The whole circle of the wreath and the whole red velvet bow are visible.

EXPOSURE - brighter and warmer than @Image 1, which came out too dark. The hallway is dim but comfortably readable: the oxblood paint reads clearly as a deep warm red rather than black, the brass knob catches a warm highlight, the oak floorboards and the forearm are clearly lit, and the shadows stay deep but still hold detail. Do not crush the blacks and do not let any part of the frame go to a flat dark mass.

SHARPNESS - this frame must be tack sharp edge to edge: every moulding edge and panel corner in the door, the machined edge and the patina of the brass knob, the individual needles of the pine wreath and the woven nap of the red velvet bow, the skin texture and fine hairs on the forearm, the grain of the floorboards. Extremely high quality, perfect lighting, perfectly exposed, hyper realistic. BANNED: blur, soft focus, haze, mushy low-detail surfaces, waxy skin, a dreamy or filtered look, motion blur, noise, upscaling artefacts.

Natural handheld UGC look, shot on an iPhone 16 Pro, photorealistic, zero motion blur, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Image prompt — `references/v10_c05_r2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `1f88d0ff-b4ae-4d75-a61b-9e36719f41a5`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_170414_1f88d0ff-b4ae-4d75-a61b-9e36719f41a5.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `f3a8c329-4152-4a22-9469-d89578812e09`
- @Image 2: `references/house_great_room_us_coffered.png` · Higgsfield media `08f4bcf5-a441-49c5-81c6-ef6a0953c4df`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its flat coffered ceiling, its beams, its wainscot, its brick chimney breast, its gallery railing, its arched windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm cream and oatmeal nordic knitted Christmas jumpers with a row of deep-green fir trees and rust-red reindeer across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height great room under a FLAT DEEP COFFERED CEILING - one single flat horizontal plane, gridded by chunky white-painted beams crossing each other at right angles into a regular grid of about three bays across by four deep, every square between them a deep recessed coffer panel stepped up above the face of the beams with a crisp moulded edge, and one small flush recessed downlight set in the middle of each coffer; there is NO vault, no slope, no ridge, no rafter and no truss anywhere in this room - the ceiling is one single flat coffered plane; white painted drywall walls carrying a white raised-panel wainscot with a moulded chair rail running around the lower third; on the back wall a tall floor-to-ceiling chimney breast of whitewashed painted brick, every brick and every mortar line legible, with a plain white mantel shelf and a simple firebox under it; on the left a bank of three tall arched-top windows reaching almost the full height of the room, white-framed with slim glazing bars; on the right, above head height, a second-floor gallery landing open to the room behind a dark walnut handrail carried on slim black wrought-iron balusters, with the plain white soffit of the gallery floor beneath it. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground, a long upholstered ottoman and a large oat flat-weave rug. Copy the proportions, the flat coffered grid and the depth of its recesses, the raised-panel wainscot and its chair rail, the whitewashed brick chimney breast, the three arched windows and the gallery railing on its black balusters from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the three tall arched windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight in every coffer and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing against the whitewashed brick chimney breast with warm white lights and deep crimson and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and crimson velvet ribbon laid along the white mantel shelf, cream knitted stockings hanging beneath it, and a large evergreen wreath with a crimson velvet bow hung on the gallery railing. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every white painted drywall wall and the white raised-panel wainscot below them, across the whitewashed brick chimney breast, across the gallery railing and the soffit beneath it, and across the whole flat coffered ceiling - over every recessed coffer panel and over every face of every white beam crossing between them, with no visible edge, no rectangle and no screen. NO SURFACE IN THE ROOM IS LEFT BARE. Every square inch of wall and ceiling the camera can see is inside the projection, and that explicitly includes THE TALL WHITEWASHED BRICK CHIMNEY BREAST ABOVE THE FIREPLACE: the picture crosses it from the mantel shelf all the way up to the ceiling exactly as densely as it crosses everything else, so that brick carries lit village, Ferris wheel, aurora bands, stars and drifting baubles across it and is NEVER a bare white or grey column running up the middle of the frame. The same is true of EVERY SINGLE COFFER PANEL of the ceiling grid and every face of every beam between them, the lower halves of all the walls, the white raised-panel wainscot and its chair rail, the wall above and behind the gallery railing, the white soffit under the gallery floor, the strips of wall between and beside the three arched windows, and the wall on the right - every one of them carries the picture at full density right down to where it meets the floor. If any wall or ceiling surface anywhere in the frame reads as plain paint, plain drywall or plain brick, the image is wrong. LOW ALONG THE WALLS, a whole snowy storybook Christmas village running the full width of the room along the very bottom of the projection - rows of steep-gabled houses and little shopfronts crowded side by side with thick snow heaped on every roof and every small paned window lit warm gold, a tall church rising behind them with a lit steeple and a glowing clock face, a row of market stalls under red-and-white striped awnings with tiny lit wares on them, cast-iron lamp-posts hung with evergreen wreaths lining the little street, and a curl of smoke rising from every single chimney; set into the middle of that village a frozen pond of pale silver-blue ice with a handful of tiny skating silhouettes circling on it, the one cool-coloured thing in the whole picture; rising straight up out of the village on the left an enormous lit FERRIS WHEEL, its great rim and every one of its spokes picked out in crimson and warm gold bulbs, a dozen little gondolas hanging around it and a lit hub at its centre, tall enough to climb most of the height of that wall; and on the right a great golden CAROUSEL under a red-and-white striped canopy, its horses caught mid-rise on twisted brass poles, every scallop of the canopy edge strung with lights and a lit finial on top; ABOVE THE VILLAGE, wide soft aurora ribbons in deep Christmas crimson and glowing ruby red, with warm gold, emerald green and rose magenta threaded between them and only a thin thread of teal, RADIATING OUTWARD FROM THE GREAT STAR OVERHEAD rather than sweeping past in long curves - five or six broad overlapping bands fanning down the walls from that one point, layered over each other so there is very little bare surface left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe; ACROSS THE CEILING OVERHEAD, one colossal EIGHT-POINTED STAR OF BETHLEHEM filling the entire ceiling - four long tapering rays reaching right out into the four corners of the ceiling and four shorter rays between them, a brilliant white-gold core at its centre bleeding outward through warm gold into deep ruby red at the very tips of the rays, the whole star built of countless tiny points of light so it reads as a star of massed light rather than a painted shape, and a fine scatter of sparks trailing off the edge of every ray; CONCENTRIC RIPPLE RINGS spreading outward from that star across the whole ceiling like rings on water, seven of them in crimson and warm gold, each one thinner and fainter than the last as it travels out toward the walls; Santa's sleigh drawn by a team of eight flying reindeer ARCING IN TOWARD the star on a long sweeping curve, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners across the ceiling; a huge pair of ornate gold CHRISTMAS BELLS hanging high on one wall, tied together with a big crimson velvet bow, every scroll of their casting picked out in light and a bright clapper glowing inside each; floating glowing BAUBLES and CANDY CANES drifting through the whole scene at five or six different depths and sizes, the baubles ribbed and faceted in crimson, gold and emerald with a bright cap and a tiny hanging loop, the candy canes striped red and white, the nearest big enough to read the stripe, all of them turning slowly as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the ceiling and every wall; faint wisps of glowing crimson and gold cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS LED BY RED. Deep Christmas crimson and glowing ruby red are the dominant colours of the entire picture, warm gold is second, then emerald green, cream white and rose magenta; soft teal survives only as a thin accent inside one or two of the aurora bands. The aurora ribbons are mostly crimson and ruby with gold and emerald threaded between them, the rays of the great star run from a gold core out to deep red tips, the ripple rings are crimson and gold, the village windows and the church clock burn red-gold, the Ferris wheel and the carousel are strung with crimson and gold bulbs, and most of the floating baubles are crimson and gold. Everything is richly saturated, and the small frozen pond is the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue.  AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn. The great star is a STORYBOOK STAR OF BETHLEHEM made of Christmas light with a sleigh flying in toward it, not a space nebula: it must NOT look like outer space, a galaxy, a supernova, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit snowy village, a Ferris wheel, a carousel, flying reindeer and floating baubles in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely. The white painted drywall, the white coffer beams, the white wainscot panels and the whitewashed brick do NOT read as white anywhere inside the projection field - the light has swallowed their colour. The only things that survive through it are the surface's TEXTURE and its SHADOWS: the slight tooth of the drywall, the moulded edges of the coffers and the wainscot, the faces and mortar lines of the brick, the square corners of the beams. That is the ten percent; the colour of the surface is not part of it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white. Contrast is extreme: the cores of the great star, the Ferris wheel, the carousel and the lit village windows are near-white hot, the mid-tones are deep saturated crimson and emerald, and the empty sky between them is almost black - never pale paint.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.  The flat coffered ceiling is one single plane, so nothing folds at a ridge - instead the grid breaks it everywhere. Every coffer is a sunken box, so the picture STEPS UP into each recessed panel and back down onto the beams between them, and the rays of the great star, the ripple rings and every aurora band visibly kink up and down at every beam they cross, running across the ceiling in a stepped grid rather than as one smooth sheet. The face of each chunky crossing beam that points back toward the projector catches its own bright slice of the picture, offset and stepped from the coffer panel behind it, while the far side and the underside of every beam sit in hard unlit shadow, so the ceiling reads as a lit grid of sunken boxes ribbed by dark beams and never as one flat painted mural. Where the light reaches the top of a wall it breaks again at that corner and runs down the vertical plane at a different angle. The raised-panel wainscot breaks it further, every raised panel and the moulded chair rail catching its own bright band and throwing its own shadow so the picture steps across the lower wall. The whitewashed brick chimney breast breaks it again, every brick catching the light on its own face and every mortar line throwing its own fine shadow. The gallery railing breaks it a fourth time, each slim black baluster catching a bright edge and casting a bar of shadow onto the wall behind it, and the white soffit under the gallery floor takes the picture at its own flat angle. The surface texture stays legible inside the light - the tooth of the drywall, the square edges of the beams and the wainscot panels, the brick faces and their mortar joints - so it still reads as projected light on a real room and never as paint, wallpaper, a sticker or a printed panel. AND EVERY PIECE OF STANDING-PROUD TIMBER AND TRIM THROWS A REAL SHADOW: each chunky coffer beam, each raised wainscot panel, the chair rail and each black baluster casts a hard-edged shadow of itself across the surface behind it, so a dark unlit band runs alongside every beam and every moulding where the picture is blocked. Those cast shadows are the clearest proof that this is light crossing a real room and not a mural, and they must be plainly visible. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room. Three or four thin volumetric shafts of coloured light hang visibly in the air of the room so the beam itself is seen in the space, but they are narrow and crisply defined and they do NOT fog, veil or soften any part of the picture. EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP. Each gable and lit window of the village, each spoke and gondola of the Ferris wheel, each horse and every scallop of the carousel canopy, each antler and harness bell on each reindeer, each arm of each snowflake, each stripe on each candy cane and each ray of the great star has a hard, crisp, precisely drawn edge. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the long upholstered ottoman, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no village, no Ferris wheel, no carousel, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the brick and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v10_c05_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `def9fb7a-c704-46f7-887a-3dba143e0dfc`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_204700_def9fb7a-c704-46f7-887a-3dba143e0dfc.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v10_c05_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c05_g1.png` · Higgsfield media `8a67ec09-6f62-4ee1-81d7-bf9a9523ac84`
- image ref 1: `content/video_10_assets/references/v10_c05_r2.png` · Higgsfield media `db543b24-0c41-4ca2-b1ee-237f92dc5743`

````text
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the flat coffered ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the drywall. @Image 1 is ONE PAUSED FRAME of that movie. At 0.0s it un-pauses and keeps running to the last frame. Smoke pours from every chimney, the aurora radiates, the sleigh flies, the Ferris wheel and the carousel turn, the ripple rings spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed four-panel oxblood-red door with a wreath, a hand on the brass knob. @Image 1 is the great room behind that door and the authority on its layout, coffered ceiling, furniture, the two children, their clothes, the colours, and the exact set and style of every projected shape.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Every chimney in the snowy storybook village pours smoke like a real wood fire on a cold still evening: it boils out of the pot, leans right, climbs and widens and thins away, and the next plume is already forming behind it. Not one chimney in the village is without its plume.

THE AURORA. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the drywall; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE FERRIS WHEEL AND THE CAROUSEL. The enormous lit Ferris wheel TURNS steadily about its lit hub, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel TURNS the other way under its striped canopy, its horses rising and falling on their twisted brass poles as they come round, the lights along every scallop of the canopy chasing round the rim. Both keep turning from the first frame to the last.

THE RIPPLE RINGS. The seven concentric rings SPREAD OUTWARD from the great star across the ceiling like rings on water, each one travelling away from the core, widening and thinning and fading as it reaches the walls, while a fresh ring is already forming at the centre behind it, so the spread never stops.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the tiny skating silhouettes circling on the frozen pond, shooting stars streaking and fading, the floating baubles and candy canes turning slowly as they drift, the big gold bells swinging gently on their crimson bow with the clappers glowing inside them, the lit shopfront windows and the church clock flickering warm, and wisps of crimson and gold cloud drifting between the aurora bands. Only the glowing clock face of the church holds position; it simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, steps up into every sunken coffer and back down onto the beams between them, and breaks where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, its spreading ripple rings, the radiating aurora, the flying sleigh, pouring snow and twinkling stars run into every single coffer panel and over every beam, right into all four corners. No bare un-animated coffer panel and no bare white beam anywhere in the closing framing.

BEATS
0.0-0.6s - The hand turns the knob and pushes the door away from camera in one quick decisive shove. The room behind it is already running AND BOTH CHILDREN ARE ALREADY IN MOTION - the widening gap only uncovers more of a movie that was already playing and two kids who were already running before the door opened. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.6s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white coffered ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the aurora ripples, the sleigh flies on across the ceiling, the Ferris wheel and the carousel keep turning, the ripple rings keep spreading and the snow keeps falling.
Inside that single move, BOTH CHILDREN ARE ALREADY RUNNING THE FIRST FRAME THEY ARE VISIBLE. The door opens on two kids in the middle of doing something, not on two kids standing waiting to be filmed, and neither of them is ever still. THE BOY, the child on the right with his back to camera, is already mid-stride as the gap widens; he takes three or four quick real steps and LAUNCHES HIMSELF UP ONTO the big oatmeal linen sectional sofa that wraps the room right behind him, landing on his knees with both arms flying up, laughing, and keeps bouncing there until the last frame. THE GIRL, the child on the left with the long wavy hair, is already running as the door opens; she runs on across the room toward the lit Christmas tree without breaking step, tips her head right back to look straight up at the great radiating star on the coffered ceiling and throws one arm up pointing at it, mouth open, delighted - and she is still moving and still pointing on the last frame. Both runs are ordinary excited-kid running at real speed with real weight: feet landing, knees bending, arms swinging, hair and jumpers moving with them. Projected shapes slide down the walls behind them and pass across their backs.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.6s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the oxblood-red door, the brass knob, the bare forearm and its thin gold bangle. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole coffered ceiling is covered in moving picture at the end. BOTH CHILDREN ARE MOVING IN EVERY FRAME THEY APPEAR IN, from the first frame the door uncovers them to the last frame of the clip: the boy ends the clip bouncing on the sofa, the girl ends it still running and still pointing up at the ceiling. Their movement is natural, unchoreographed, real-speed kid movement. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an aurora that sits still; a parked sleigh; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated coffer panel in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; either child standing still, waiting, hesitating, posed or rooted to one spot at any point; a child who only turns her head while her feet stay planted; a child who begins the clip motionless and starts moving later; a child who stops moving before the last frame; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.
````

**Other takes of C05 on disk (2)**

#### Image prompt — `references/v10_c05_r1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `c305720b-3c50-4de2-8006-13ff0da79bbf`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141641_c305720b-3c50-4de2-8006-13ff0da79bbf.png
**References, in submission order**
- @Image 1: `content/video_1_assets/references/v1_c05_r2.png` · Higgsfield media `f3a8c329-4152-4a22-9469-d89578812e09`
- @Image 2: uploaded image, not on the drive · Higgsfield media `4dec9045-2ac2-4a2c-8412-6dc4ae08cfc0`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a much bigger projection. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its raking ceiling, its boarding, its tie rods, its walls, its glazed gable and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing of a whole tall room seen from a doorway, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two children - a boy standing TURNED AROUND FACING THE CAMERA, front-on, his face fully visible and lit by the coloured light, looking towards the lens with a delighted open-mouthed smile, arms slightly out in wonder, and a girl beside him seen from behind, still looking up at the projected wall.

Both children are fully dressed for winter in warm sage-green and cream nordic knitted Christmas jumpers with a row of cream fir trees across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 1 - THE ROOM. The room is the real house photographed in @Image 2, seen from the doorway. Build its architecture exactly as it is built there, as a real room a real builder made: a tall great room under a SINGLE-SLOPE SHED CEILING - one continuous flat plane of narrow white-painted tongue-and-groove boards that starts low over the left-hand side of the room and rakes up in one unbroken climb to a very high eaves line on the right, the board seams all running straight up the slope; the room is held together across that span by three slim black steel tie rods, each a straight round rod running horizontally from wall to wall well below the boards and bolted into a small black anchor plate at each end; small flush recessed downlights are set in a line up the rake; there is NO timber rafter, no ridge, no collar beam, no king post and no vault anywhere in this room - the ceiling is one single straight raking plane; cream plaster walls; under the high side of the rake on the right, an almost full-height glazed gable wall of slim black steel frames divided into many small rectangular panes, rising with the slope; on the back wall a wide cream plaster fireplace with a long low horizontal firebox and a tall potted olive tree standing beside it; along the left an open kitchen with deep forest-green slab cabinetry, aged brass hardware, a pale stone island and woven rattan counter stools. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground and a round dark walnut coffee table on a large oat flat-weave rug. Copy the proportions, the single raking plane, the direction of the board seams, the three black tie rods and their anchor plates, and the tall black glazed gable from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall glazed gable shows a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a tall real Christmas tree standing against the cream plaster back wall beside the fireplace with warm white lights and sage-green and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and sage-green velvet ribbon laid along the plaster above the firebox, cream knitted stockings hanging beneath it, and a large evergreen wreath with a sage-green velvet bow hung on the glazed gable wall. Nothing else about the room changes.

CHANGE 2 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every cream plaster wall, the whole raking boarded ceiling from its low edge all the way up to the high eaves, and the three black steel tie rods strung beneath it, with no visible edge, no rectangle and no screen. LOW ALONG THE WALLS, a deep snow-laden pine forest running the whole width of the room along the very bottom of the projection, rank behind rank of little glowing firs in emerald green and warm gold with snow heaped on every branch, and rising straight out of that forest on the left a whole ornate fairy-tale Christmas city built of lit gold - tier upon tier of slender spires, ribbed onion domes, arched galleries and pinnacled towers stacked up the wall, every arched window lit warm gold, fine gold filigree running along every cornice and balustrade, thick snow lying on every ledge and roof and dome, the whole city glowing as though it were carved out of light; and winding out of the pines on the right a long lit steam train, a dark locomotive leading eight carriages whose windows all glow warm gold, a bright plume of steam and sparks trailing back over the carriage roofs and a glowing gold rail curving away behind it through the trees; ABOVE THE FOREST AND THE CITY, wide soft aurora ribbons in emerald green, rose magenta, warm gold and soft teal sweeping up the walls in long slow curves and carrying over onto the single raking shed plane, five or six broad overlapping bands layered over each other so there is very little bare boarded slope left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe, where they lie flat along the rake and run straight up it with the climb of the plane instead of hanging as vertical curtains, and are stretched longer and thinner the further up the slope they travel; ACROSS THE RAKING CEILING OVERHEAD, one colossal spiral whirlpool of light filling most of the slope - seven concentric glowing rings of emerald green, warm gold and rose magenta winding in on each other in a slow tightening spiral and drawing down to one brilliant white-gold core at the very centre, every ring built of countless tiny points of light so the whole thing reads as a whirlpool of stars rather than a painted disc; Santa's sleigh drawn by a team of eight flying reindeer sweeping straight out of the mouth of that spiral, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners into the spiral, the whole team lying flat on the rake so it is keystoned and stretched by the climb of the plane, growing larger and brighter as it rises toward the tall glazed gable; a big pale blue full moon glowing high on the cream plaster chimney breast on the back wall, cool silver-blue and softly cratered and the one cool-coloured thing in the whole picture, with the tiny black silhouette of a second sleigh and its reindeer team crossing right over the face of it; floating wrapped Christmas gifts drifting through the whole scene at five or six different depths and sizes, each a solid glowing box in gold, emerald or rose with a bright ribbon cross and a big soft bow on top, the nearest big enough to read the weave of the ribbon, all of them turning slowly end over end as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the raking boards and both walls; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE: emerald green, warm gold, cream white, rose magenta and soft teal, richly saturated against the white boards and the cream plaster, with the single pale blue moon as the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue. The great spiral is an AURORA WHIRLPOOL made of Christmas light with a sleigh flying out of its mouth, not a space nebula: it must NOT look like outer space, a galaxy, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit gold Christmas city, a steam train, flying reindeer and falling gifts in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster and real painted boarding, not paint and not a sticker. The light is TRANSLUCENT - the white-painted boards of the slope and the fine seam between every board, the three slim black steel tie rods and their black anchor plates, and the line of flush recessed downlights running up the rake, all stay clearly visible THROUGH the coloured light across the whole ceiling, and each black tie rod breaks the light with its own hard shadow line where it hangs below the boards. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the single raking plane, stretching longer and thinner the further up the slope it travels. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real single-slope boarded shed ceiling climbing in one unbroken rake to the glazed gable, with the black tie rods crossing beneath it, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 3 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the round walnut coffee table, the tree and the gifts carry NO projected shapes at all - no snowflakes, no stars, no city, no train, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children's faces and their knitted jumpers catch that spill so both faces read clearly.

CHANGE 4 - the projector unit must NOT be visible. No projector, no side table, no stool, no glowing device anywhere in frame. The corner it would occupy is plain floor and the edge of the rug.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with both children's faces clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v10_c05_g1.mp4`

**Settings** - seedance_2_5 · 720p · 8 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `c05a1b4a-4cae-401f-b415-055bdc0c723a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_c05a1b4a-4cae-401f-b415-055bdc0c723a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c05_g1.png` · Higgsfield media `8a67ec09-6f62-4ee1-81d7-bf9a9523ac84`
- image ref 1: `content/video_10_assets/references/v10_c05_r2.png` · Higgsfield media `db543b24-0c41-4ca2-b1ee-237f92dc5743`

````text
HIGHEST PRIORITY, READ THIS FIRST: the pictures on the walls and the flat coffered ceiling are A MOVIE THAT IS PLAYING, not a pattern painted on the drywall. @Image 1 is ONE PAUSED FRAME of that movie. At 0.0s it un-pauses and keeps running to the last frame. Smoke pours from every chimney, the aurora radiates, the sleigh flies, the Ferris wheel and the carousel turn, the ripple rings spread, the snow falls - continuously, in every single frame. If the shapes on the walls and ceiling hold still, the clip has failed.

Wholesome family Christmas scene, children at home at Christmas.

TASK: image-to-video, one continuous handheld phone POV take, vertical 9:16. Frame 0.0s is the start image: a closed four-panel oxblood-red door with a wreath, a hand on the brass knob. @Image 1 is the great room behind that door and the authority on its layout, coffered ceiling, furniture, the two children, their clothes, the colours, and the exact set and style of every projected shape.

THE SIX MOVING THINGS - all six running from the first frame to the last.

SMOKE. Every chimney in the snowy storybook village pours smoke like a real wood fire on a cold still evening: it boils out of the pot, leans right, climbs and widens and thins away, and the next plume is already forming behind it. Not one chimney in the village is without its plume.

THE AURORA. The crimson, ruby, gold and emerald ribbons RADIATE OUTWARD FROM THE GREAT STAR and ripple as they go, like long silk curtains hung in a draught - a slow swell travels down the length of each band away from the star, brightening it as it passes and combing its lower fringe into new folds. The fan stays where it is on the drywall; the swell inside it travels.

THE SLEIGH. Santa's sleigh and its eight reindeer are FLYING ACROSS THE CEILING the way a plane crosses the sky, arcing in toward the great star on a long sweeping curve. Legs gallop, heads nod, the sleigh rocks, the long trail of light streams off the runners, the team rises and dips. They start near one side of the ceiling and finish far across it, closer to the star than they began. Never parked.

THE FERRIS WHEEL AND THE CAROUSEL. The enormous lit Ferris wheel TURNS steadily about its lit hub, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel TURNS the other way under its striped canopy, its horses rising and falling on their twisted brass poles as they come round, the lights along every scallop of the canopy chasing round the rim. Both keep turning from the first frame to the last.

THE RIPPLE RINGS. The seven concentric rings SPREAD OUTWARD from the great star across the ceiling like rings on water, each one travelling away from the core, widening and thinning and fading as it reaches the walls, while a fresh ring is already forming at the centre behind it, so the spread never stops.

THE SNOW. The big soft six-point flakes and the tiny points of light fall the way heavy snow falls past a window at night - down and slightly sideways, each turning on its own centre. One fades out at the floor line as a fresh one fades in high near the ceiling, so the density never thins.

Everything else travels too: the tiny skating silhouettes circling on the frozen pond, shooting stars streaking and fading, the floating baubles and candy canes turning slowly as they drift, the big gold bells swinging gently on their crimson bow with the clappers glowing inside them, the lit shopfront windows and the church clock flickering warm, and wisps of crimson and gold cloud drifting between the aurora bands. Only the glowing clock face of the church holds position; it simply breathes brighter and dimmer.

ONE PROJECTOR, ONE PICTURE: whatever the wall is doing, the ceiling is doing at the same instant and the same speed. The picture's outer boundary is anchored - it never rotates, spins or slides across the room as one sheet; only the things inside it travel. It is flat light lying on the surfaces: it skews with their angle, steps up into every sunken coffer and back down onto the beams between them, and breaks where wall meets ceiling. Nothing ever leaves a surface, and nothing is projected on the floor, rug, sofa, table, tree or gifts.

THE CEILING IS FULL. The ceiling carries as much moving picture as the walls do, everywhere it appears in frame and above all in the closing seconds: the great star, its spreading ripple rings, the radiating aurora, the flying sleigh, pouring snow and twinkling stars run into every single coffer panel and over every beam, right into all four corners. No bare un-animated coffer panel and no bare white beam anywhere in the closing framing.

BEATS
0.0-0.8s - The hand turns the knob and pushes the door away from camera. The room behind it is already running; the widening gap only uncovers more of a movie that was already playing. Nothing ignites or spreads as the door opens, and the door edge and frame stay plain painted wood - no glowing strip, no coloured fringe, no bright seam in the gap.
0.8s to the end - ONE SINGLE UNBROKEN CAMERA MOVE, exactly like a person walking into a room with their chin lifting the whole way. The camera walks steadily forward while its aim rises smoothly at a constant rate, so the frame climbs from the floor to the white coffered ceiling and its great star in one continuous sweep. Walk and rise happen together at the same steady pace for the whole span; the camera never pauses, never holds and never re-starts, and there is no second move. All through it the smoke pours from every chimney, the aurora ripples, the sleigh flies on across the ceiling, the Ferris wheel and the carousel keep turning, the ripple rings keep spreading and the snow keeps falling.
Inside that single move: THE BOY, the child standing on the right at 0.0s with his back to camera, takes three or four quick real steps and LAUNCHES HIMSELF UP ONTO the big oatmeal linen sectional sofa that wraps the room right behind him, landing on his knees with both arms flying up, laughing, then keeps bouncing there until the last frame. THE GIRL stays where she is, seen from behind, turning her head to follow him. Projected shapes slide down the walls behind them and pass across their backs.

CAMERA - eye height, normal wide-angle phone lens, natural handheld bounce. One move for the whole clip. No stop, no second move, no cut, no zoom, no orbit, no fisheye, no curved walls. The camera is the person's eyes; no phone, screen or device in frame after 0.8s.

EXACTLY TWO CHILDREN, no adults, no third child, no pets. Hold the sharpness and exposure of the start image - the panel edges of the oxblood-red door, the brass knob, the bare forearm and its thin gold bangle. Crisp phone footage, in focus first frame to last.

AUDIO - dry documentary sound only: the handle, the door swinging, running feet, a body landing on cushions, children laughing, quiet room tone. (no BGM). No subtitles.

POSITIVE LOCKS - real-time motion at normal speed. One continuous take. One single smooth camera move. The projected picture is visibly in motion in every single frame, at the start, in the middle and in the last second. The whole coffered ceiling is covered in moving picture at the end. The boy ends the clip bouncing on the sofa. Sharp focus to the final frame.

BANNED - a still or frozen picture; a projection that appears to move only because the camera moves; light that moves for a moment then stops; chimneys without smoke; an aurora that sits still; a parked sleigh; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that twinkle but never travel; a still ceiling above a moving wall; an empty or un-animated area of ceiling or an un-animated coffer panel in any frame; the whole picture rotating or sliding as one sheet; a pattern that looks printed, painted or like wallpaper; a glow or bright seam along the door edge or gap; light that grows or fills the room as the door opens; particles falling through the open air of the room; volumetric snow; snow in front of the children, the sofa, the stair or the real tree; a camera that moves, stops and then moves again; two separate camera moves; the boy still standing on the floor at the end; children posed or standing still; the projector unit visible; slow motion; blur; any music; a cut; an adult; subtitles; on-screen text.
````

### C06 — The bed bounce

**In the cut:** `starting_frames/v10_c06_g2.png` → `clips/v10_c06_g1.mp4`

#### Image prompt — `starting_frames/v10_c06_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `37832ca3-a7dd-48b5-ba4e-187e5f082652`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_170414_37832ca3-a7dd-48b5-ba4e-187e5f082652.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `0a845da6-2607-46cc-a595-4fee4b17d6a9`
- @Image 2: `references/house_bedroom_us_tray.png` · Higgsfield media `24b58778-42a3-4a92-a214-553b51e4a904`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its tray ceiling and its four reveals, its panelled accent wall, its walls, its windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about seven with short sandy-blond hair, fully dressed for winter in a warm cream and oatmeal nordic knitted Christmas jumper with a row of deep-green fir trees and rust-red reindeer across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom with a FLAT TRAY CEILING - one big clean rectangle recessed up into the middle of an otherwise flat cream plaster ceiling, with a plain angled reveal stepping up on all FOUR sides from the flat border into a raised flat panel, a crisp crown moulding running around the outer edge of the tray where it meets the border, and small flush recessed downlights set in the flat border; the whole ceiling is smooth plaster and perfectly flat apart from that one rectangular step - there is no vault, no slope, no ridge, no rafter, no beam and no boarding anywhere in this room; soft cream painted walls with plain white skirting; the far wall behind the bed is a full PICTURE-FRAME MOULDING ACCENT WALL - four tall raised rectangular panels side by side, each outlined in a crisp applied moulding that stands proud of the wall, running from skirting to crown; on the right-hand wall two tall white-framed double-hung windows spaced apart, each hung with long cream pinch-pleat curtains on a slim black rod; an upholstered bed with a wide cream headboard standing against the panelled accent wall, two small pale oak nightstands with small cream table lamps, and a long cream upholstered bench on slim pale oak legs at the foot of the bed; a pale oak plank floor under a very large oat flat-weave rug. Copy the proportions, the flat ceiling, the single rectangular tray recess with its four angled reveals and its crown moulding, the four-panel picture-frame moulding accent wall and the two windows on the right from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: both windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and both table lamps are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a deep crimson wool quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking hangs on the panelled wall above the headboard, a warm fairy-light garland is strung around the nearer window, and a small lit Christmas tree with crimson and antique gold ornaments stands on the floor beside the bed. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole picture-frame moulding accent wall behind the bed, the right-hand wall and its windows, the flat cream plaster border of the ceiling, up all four angled reveals and right across the raised tray panel set into the middle of it, wrapping around the corner where wall meets ceiling without a break, with no visible edge, no rectangle and no screen. NO SURFACE IN THE ROOM IS LEFT BARE. Every square inch of wall and ceiling the camera can see is inside the projection, and that explicitly includes THE WHOLE PICTURE-FRAME MOULDING ACCENT WALL BEHIND THE BED: the picture crosses all four raised panels and every moulding between them from the skirting all the way up to the crown exactly as densely as it crosses everything else, so that wall carries lit village, Ferris wheel, aurora bands, stars and drifting baubles across it and is NEVER a bare cream panelled wall behind the child. The same is true of the ENTIRE FLAT BORDER of the ceiling, ALL FOUR ANGLED REVEALS of the tray, the whole raised tray panel in the middle, the crown moulding around its edge, the right-hand wall and the strips of wall between and beside its two windows, and the wall on the left - every one of them carries the picture at full density right down to where it meets the floor. If any wall or ceiling surface anywhere in the frame reads as plain paint or plain plaster, the image is wrong. LOW ALONG THE WALLS, a whole snowy storybook Christmas village running the full width of the room along the very bottom of the projection - rows of steep-gabled houses and little shopfronts crowded side by side with thick snow heaped on every roof and every small paned window lit warm gold, a tall church rising behind them with a lit steeple and a glowing clock face, a row of market stalls under red-and-white striped awnings with tiny lit wares on them, cast-iron lamp-posts hung with evergreen wreaths lining the little street, and a curl of smoke rising from every single chimney; set into the middle of that village a frozen pond of pale silver-blue ice with a handful of tiny skating silhouettes circling on it, the one cool-coloured thing in the whole picture; rising straight up out of the village on the left an enormous lit FERRIS WHEEL, its great rim and every one of its spokes picked out in crimson and warm gold bulbs, a dozen little gondolas hanging around it and a lit hub at its centre, tall enough to climb most of the height of that wall; and on the right a great golden CAROUSEL under a red-and-white striped canopy, its horses caught mid-rise on twisted brass poles, every scallop of the canopy edge strung with lights and a lit finial on top; ABOVE THE VILLAGE, wide soft aurora ribbons in deep Christmas crimson and glowing ruby red, with warm gold, emerald green and rose magenta threaded between them and only a thin thread of teal, RADIATING OUTWARD FROM THE GREAT STAR OVERHEAD rather than sweeping past in long curves - five or six broad overlapping bands fanning down the walls from that one point, layered over each other so there is very little bare surface left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe; ACROSS THE CEILING OVERHEAD, one colossal EIGHT-POINTED STAR OF BETHLEHEM filling the entire ceiling - four long tapering rays reaching right out into the four corners of the ceiling and four shorter rays between them, a brilliant white-gold core at its centre bleeding outward through warm gold into deep ruby red at the very tips of the rays, the whole star built of countless tiny points of light so it reads as a star of massed light rather than a painted shape, and a fine scatter of sparks trailing off the edge of every ray; CONCENTRIC RIPPLE RINGS spreading outward from that star across the whole ceiling like rings on water, seven of them in crimson and warm gold, each one thinner and fainter than the last as it travels out toward the walls; Santa's sleigh drawn by a team of eight flying reindeer ARCING IN TOWARD the star on a long sweeping curve, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners across the ceiling; a huge pair of ornate gold CHRISTMAS BELLS hanging high on one wall, tied together with a big crimson velvet bow, every scroll of their casting picked out in light and a bright clapper glowing inside each; floating glowing BAUBLES and CANDY CANES drifting through the whole scene at five or six different depths and sizes, the baubles ribbed and faceted in crimson, gold and emerald with a bright cap and a tiny hanging loop, the candy canes striped red and white, the nearest big enough to read the stripe, all of them turning slowly as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the ceiling and every wall; faint wisps of glowing crimson and gold cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS LED BY RED. Deep Christmas crimson and glowing ruby red are the dominant colours of the entire picture, warm gold is second, then emerald green, cream white and rose magenta; soft teal survives only as a thin accent inside one or two of the aurora bands. The aurora ribbons are mostly crimson and ruby with gold and emerald threaded between them, the rays of the great star run from a gold core out to deep red tips, the ripple rings are crimson and gold, the village windows and the church clock burn red-gold, the Ferris wheel and the carousel are strung with crimson and gold bulbs, and most of the floating baubles are crimson and gold. Everything is richly saturated, and the small frozen pond is the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue.  AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale plaster and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn. The great star is a STORYBOOK STAR OF BETHLEHEM made of Christmas light with a sleigh flying in toward it, not a space nebula: it must NOT look like outer space, a galaxy, a supernova, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit snowy village, a Ferris wheel, a carousel, flying reindeer and floating baubles in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely. The cream painted plaster, the white crown moulding and the raised panel mouldings of the accent wall do NOT read as pale anywhere inside the projection field - the light has swallowed their colour. The only things that survive through it are the surface's TEXTURE and its SHADOWS: the fine tooth of the plaster, the crisp moulded edge of the tray, the square corners of every applied moulding. That is the ten percent; the colour of the surface is not part of it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white. Contrast is extreme: the cores of the great star, the Ferris wheel, the carousel and the lit village windows are near-white hot, the mid-tones are deep saturated crimson and emerald, and the empty sky between them is almost black - never pale paint.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.  The ceiling is one flat plane with a single tray cut up into it, so nothing folds at a ridge - instead the tray breaks it. The picture runs across the flat border, STEPS UP each of the four angled reveals, each reveal taking it at its own angle and stretching it differently, and carries on across the raised panel in the middle, so the rays of the great star, the ripple rings and every aurora band visibly kink at the crown moulding and again at the top of each reveal. The crown moulding around the tray edge catches its own bright band on the face pointing back toward the projector and throws a hard shadow on the other side, and the reveal on the far side of the tray sits in unlit shadow where it turns away from the beam. Where the light reaches the top of a wall it breaks again at that corner and runs down the vertical plane at a different angle. The picture-frame moulding of the accent wall breaks it further, every applied moulding catching a bright edge on the side facing the projector and casting its own shadow on the other, so the picture steps in and out of each of the four panels. The window casings and the skirting break it again, each catching its own bright edge. The surface texture stays legible inside the light - the fine tooth of the plaster, the square edges of the crown moulding and of every applied panel moulding - so it still reads as projected light on a real room and never as paint, wallpaper, a sticker or a printed panel. AND EVERY PIECE OF STANDING-PROUD TRIM THROWS A REAL SHADOW: the crown moulding at the tray edge, each applied picture-frame moulding on the accent wall, each window casing and the skirting all cast a hard-edged shadow of themselves across the surface behind them, so a dark unlit band runs alongside every moulding where the picture is blocked. Those cast shadows are the clearest proof that this is light crossing a real room and not a mural, and they must be plainly visible. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room. Three or four thin volumetric shafts of coloured light hang visibly in the air of the room so the beam itself is seen in the space, but they are narrow and crisply defined and they do NOT fog, veil or soften any part of the picture. EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP. Each gable and lit window of the village, each spoke and gondola of the Ferris wheel, each horse and every scallop of the carousel canopy, each antler and harness bell on each reindeer, each arm of each snowflake, each stripe on each candy cane and each ray of the great star has a hard, crisp, precisely drawn edge. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Ferris wheel, no carousel, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the plaster, the crisp moulded edges of the panelling and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v10_c06_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `7f57a886-f8e5-4706-81e4-edd5725c064e`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194653_7f57a886-f8e5-4706-81e4-edd5725c064e.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v10_c06_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c06_g2.png` · Higgsfield media `a8dbc496-95dd-4c47-85ec-863af73b643c`

````text
Wholesome family Christmas scene, a child at home with his family at Christmas.

SUMMARY: a boy bounces on his bed in a Christmas bedroom at night while a projected snow-village picture is PLAYING across the panelled accent wall behind the bed and the whole flat tray ceiling above it, thrown there by a projector standing on the floor. 5 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the bedroom, the flat cream plaster ceiling and its single rectangular tray recess with its four angled reveals and its crown moulding, the flush recessed downlights in the flat border, the four-panel picture-frame moulding accent wall behind the bed, the bed with its deep crimson wool quilt and cream linen pillows, the wide cream upholstered headboard, the long cream upholstered bench at the foot of the bed, the small lit Christmas tree, the large oat flat-weave rug, the two windows with their curtains and garland, the stocking, THE BOY and the colour.

SUBJECTS:
THE BOY - exactly one child, about seven years old with short sandy-blond hair, in a warm cream and oatmeal nordic knitted Christmas jumper with a row of deep-green fir trees and rust-red reindeer across the yoke, charcoal knitted lounge trousers and thick mustard knitted socks, standing on the bed with his arms thrown wide. No second child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running on the bedroom floor, out of shot. One lens throws one wide cone of light across the panelled wall and the whole flat tray ceiling. Everything glowing on the plaster is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a whole snowy storybook Christmas village running low along the walls with steep-gabled houses and lit shopfronts, a church with a lit steeple and a glowing clock face, market stalls under red-and-white striped awnings and lamp-posts hung with wreaths, a curl of smoke above every single chimney, a frozen silver-blue pond set into the village with tiny skating silhouettes circling on it, an enormous lit FERRIS WHEEL rising out of the village on the left in crimson and gold bulbs and a great golden CAROUSEL under a striped canopy on the right, wide aurora ribbons in deep crimson and ruby red with warm gold and emerald green threaded between them radiating outward from the star overhead, one colossal eight-pointed STAR OF BETHLEHEM filling the whole tray ceiling with four long rays reaching into its corners, seven concentric ripple rings spreading outward from it, Santa's sleigh drawn by eight flying reindeer arcing in toward the star with a long tapering trail, a huge pair of ornate gold bells tied with a crimson bow high on one wall, floating glowing baubles and candy canes drifting at five or six different depths, a dense field of stars of many sizes, long-tailed shooting stars, and a heavy fall of large soft glowing six-point snowflakes and tiny points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the plaster and holds perfectly still, while everything inside the picture is in constant motion for all five seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the bedroom, the bed, THE BOY and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE AURORA - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the plaster; the wave inside it travels. Every ribbon on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 5.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes.
- THE FERRIS WHEEL AND THE CAROUSEL - both TURN, steadily and without ever stopping. The enormous lit Ferris wheel turns about its lit hub roughly a quarter of a full turn every second, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel turns the other way under its striped canopy at about the same rate, its horses rising and falling on their twisted brass poles as they come round, and the lights along every scallop of the canopy edge chasing round the rim.
- THE RIPPLE RINGS - the seven concentric rings SPREAD OUTWARD from the great star across the tray ceiling like rings on water, each one travelling away from the core toward the walls, widening and thinning and fading as it goes, while a fresh ring is already forming at the centre behind it, so the spread never stops.
- THE SKATERS AND THE FLOATING THINGS - the tiny silhouettes keep circling on the frozen pond, and the floating baubles and candy canes drift through the scene at their own depths, each one turning slowly as it goes, while the big gold bells swing gently on their crimson bow with the clappers glowing inside them.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the skirting board fades out there while a fresh one fades in high near the crown moulding of the tray, so the density holds even. Track this one so the fall is unmistakable: a large cream six-point flake that begins just above the headboard, falls steadily and drifts slightly right, passes the middle of the wall at 2.5s and fades out low near the skirting at 5.0s.
- THE SHOOTING STARS - the long-tailed shooting stars streak across, their tails thinning out behind them, and fade; fresh ones set off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE CHURCH CLOCK - the glowing clock face on the church steeple is the ONLY element that holds its position. It stays exactly where it is in the village for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the plaster.

TIMELINE - THE CAMERA MAKES EXACTLY TWO MOVES AND NO MORE, and they are the opposite of the other clips in this set: this one starts high and comes DOWN.
0.0-2.2s the camera is aimed HIGH at the start, weighted to the top of the panelled wall and the flat tray ceiling so the projected picture fills most of the frame and THE BOY is small and low near the bottom edge. From 0.0s the camera TILTS DOWN in one slow steady continuous move, the aurora rippling, the ripple rings spreading and the sleigh flying across the tray as it goes, until the bed and THE BOY fill the lower half. THE BOY bends his knees and pushes off the mattress; both feet leave the quilt, arms swinging up over his head, mouth open laughing. The mattress compresses and springs back.
2.2-5.0s the tilt ends and the camera PULLS BACK a little in one slow steady move, the frame opening slightly wider so a little more of the bedroom comes in at the edges - a small gentle zoom out, nothing sudden. THE BOY lands on both feet and drives straight into a second, higher jump, knees tucking, then a third; he never stops moving and the body motion carries straight across the seam between the two camera moves.

AUDIO: room tone, mattress springs compressing on each landing, bedding rustling, a boy laughing. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed - a real boy jumping at real speed and landing with real weight. Exactly one child. One continuous take with no cut. The camera makes exactly two moves: a slow tilt DOWN, then a small gentle pull back. The picture's outer boundary holds still while every element inside it moves. Wall and ceiling always move together. The picture stays sharp to the last frame.

DO NOT INCLUDE: a camera that tilts UP; a camera that pushes in; more than two camera moves; a hard or fast zoom; a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that only twinkle without travelling; a still ceiling above a moving wall; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; the projector unit in shot; a second child; an adult; blur; a cut; on-screen text; subtitles.
````

**Other takes of C06 on disk (1)**

#### Image prompt — `starting_frames/v10_c06_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `d9d7d019-1e11-4be0-a1fd-bee6b12f8ff9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141641_d9d7d019-1e11-4be0-a1fd-bee6b12f8ff9.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c06_g1.png` · Higgsfield media `0a845da6-2607-46cc-a595-4fee4b17d6a9`
- @Image 2: uploaded image, not on the drive · Higgsfield media `0c193093-94b1-498d-9dfe-4d3f7a8aee03`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with a different child and a much bigger projection. Wholesome family Christmas scene, a child at home with his family at Christmas. @Image 1 owns the camera, the framing, the pose and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its tray ceiling, its walls, its windows, its door and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same framing that shows the wall behind the bed and the ceiling above it both in shot, and the same magical low-key evening light in which the only light in the room is the projection itself.

CHANGE 1 - THE CHILD. A different child from @Image 1: a boy of about seven with short sandy-blond hair, fully dressed for winter in a warm sage-green and cream nordic knitted Christmas jumper with a row of cream fir trees across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. He is standing up on top of the bed, knees bent and both arms raised out to his sides, caught mid-bounce, head tipped back looking up at the projected ceiling, laughing. Clearly standing on top of the bed, not sitting on its edge.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2. Build its architecture exactly as it is built there, as a real room a real builder made: a bedroom with a FLAT TRAY CEILING - one big clean rectangle is recessed up into the middle of an otherwise flat cream plaster ceiling, its edges crisp and straight and parallel to the walls, with a plain shallow angled reveal stepping up from the flat border into the recessed panel, and small flush recessed downlights set in the flat border on either side; the whole ceiling is smooth plaster and perfectly flat apart from that one rectangular step - there is no vault, no slope, no ridge, no rafter, no beam and no boarding anywhere in this room; warm greige plaster walls with plain white skirting; the far wall carrying two tall white-framed double-hung windows spaced apart, each hung with long cream pinch-pleat curtains on a slim black rod, and a tall white-painted panelled door at the right-hand end; an upholstered bed with a wide cream headboard standing against that wall between the windows, two small pale oak nightstands with small cream table lamps, and a long cream upholstered bench on slim pale oak legs at the foot of the bed; a warm oak plank floor under a very large oat flat-weave rug. Copy the proportions, the flat ceiling, the single rectangular tray recess, its crisp edges and its angled reveal, and the two windows and the door from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: both windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and both table lamps are switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: the bed is made up with a sage-green wool quilt, a cream cable-knit throw and cream linen pillows, a cream knitted stocking hangs on the wall above the headboard, a warm fairy-light garland is strung around the left-hand window, a small lit Christmas tree with sage-green and antique gold ornaments stands on the floor beside the bed, and a small evergreen wreath with a sage-green velvet bow hangs on the panelled door. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the whole wall behind the bed, the flat cream plaster border of the ceiling, up the angled reveal and right across the recessed tray panel set into the middle of it, wrapping around the corner where wall meets ceiling without a break, with no visible edge, no rectangle and no screen. LOW ALONG THE WALLS, a deep snow-laden pine forest running the whole width of the room along the very bottom of the projection, rank behind rank of little glowing firs in emerald green and warm gold with snow heaped on every branch, and rising straight out of that forest on the left a whole ornate fairy-tale Christmas city built of lit gold - tier upon tier of slender spires, ribbed onion domes, arched galleries and pinnacled towers stacked up the wall, every arched window lit warm gold, fine gold filigree running along every cornice and balustrade, thick snow lying on every ledge and roof and dome, the whole city glowing as though it were carved out of light; and winding out of the pines on the right a long lit steam train, a dark locomotive leading eight carriages whose windows all glow warm gold, a bright plume of steam and sparks trailing back over the carriage roofs and a glowing gold rail curving away behind it through the trees; ABOVE THE FOREST AND THE CITY, wide soft aurora ribbons in emerald green, rose magenta, warm gold and soft teal sweeping up the walls in long slow curves and carrying over onto the flat tray ceiling, five or six broad overlapping bands layered over each other so there is very little bare cream plaster left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe, where they lie flat on the ceiling and run with the long direction of the room instead of hanging as vertical curtains, and visibly break at the crisp square edge of the tray, stepping up onto the recessed panel and back down onto the flat border; ACROSS THE TRAY CEILING OVERHEAD, one colossal spiral whirlpool of light filling most of the recessed tray panel - seven concentric glowing rings of emerald green, warm gold and rose magenta winding in on each other in a slow tightening spiral and drawing down to one brilliant white-gold core at the very centre, every ring built of countless tiny points of light so the whole thing reads as a whirlpool of stars rather than a painted disc; Santa's sleigh drawn by a team of eight flying reindeer sweeping straight out of the mouth of that spiral, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners into the spiral, the whole team lying flat on the tray panel so it is keystoned and stretched by the ceiling's angle and foreshortens as it recedes across the room; a big pale blue full moon glowing high on the greige plaster wall above the bed, cool silver-blue and softly cratered and the one cool-coloured thing in the whole picture, with the tiny black silhouette of a second sleigh and its reindeer team crossing right over the face of it; floating wrapped Christmas gifts drifting through the whole scene at five or six different depths and sizes, each a solid glowing box in gold, emerald or rose with a bright ribbon cross and a big soft bow on top, the nearest big enough to read the weave of the ribbon, all of them turning slowly end over end as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the tray panel, the flat border and both walls; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE: emerald green, warm gold, cream white, rose magenta and soft teal, richly saturated against the cream plaster of the tray, with the single pale blue moon as the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue. The great spiral is an AURORA WHIRLPOOL made of Christmas light with a sleigh flying out of its mouth, not a space nebula: it must NOT look like outer space, a galaxy, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit gold Christmas city, a steam train, flying reindeer and falling gifts in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE CEILING, and this has to be exactly right: it is projected light landing on real plaster, not paint and not a sticker. The light is TRANSLUCENT - the cream plaster and its fine surface texture, the crisp edge of the tray and the plain angled reveal stepping up into it, and the flush recessed downlights set in the flat border, all stay clearly visible THROUGH the coloured light across the whole ceiling, and the square edge of the tray breaks the light with its own hard shadow line where the ceiling steps up. Every shape up there is soft-edged and feathered with no hard opaque border, and is distorted by the surface it lands on - keystoned, stretched and skewed by the flat plane of the border and stepping up onto the recessed tray panel. The light also falls off with distance: it is brightest and most saturated where the beam first strikes and gets steadily fainter, softer and paler across the rest of the ceiling, so the far end is much dimmer than the near end and the corners fade to bare plaster. Even packed full, the ceiling must still read unmistakably as a real flat plaster ceiling with one clean rectangular tray recessed into the middle of it, never as a flat backdrop or a printed panel. Two or three faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The warm oak floorboards, the large flat-weave rug, the bed and its covers, the bench at its foot and the little Christmas tree carry NO projected shapes at all - no snowflakes, no stars, no city, no train, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. The boy's face and his knitted jumper catch that spill so his face reads clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no stool, no side table, no glowing device anywhere in frame. The corner it would occupy is plain wall and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed with the boy's face clearly readable, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

### C07 — The whole Christmas room

**In the cut:** `starting_frames/v10_c07_g2.png` → `clips/v10_c07_g1.mp4`

#### Image prompt — `starting_frames/v10_c07_g2.png` — IN THE CUT

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `9c101565-8f83-4591-9907-7aa314411d73`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_170716_9c101565-8f83-4591-9907-7aa314411d73.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `c9a6740d-383b-4829-a7b9-f7a3c079c03f`
- @Image 2: `references/house_great_room_us_coffered.png` · Higgsfield media `08f4bcf5-a441-49c5-81c6-ef6a0953c4df`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its flat coffered ceiling, its beams, its wainscot, its brick chimney breast, its gallery railing, its arched windows and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with short dark curly hair, the boy is about five with straight black hair. Both are fully dressed for winter in warm cream and oatmeal nordic knitted Christmas jumpers with a row of deep-green fir trees and rust-red reindeer across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: a tall double-height great room under a FLAT DEEP COFFERED CEILING - one single flat horizontal plane, gridded by chunky white-painted beams crossing each other at right angles into a regular grid of about three bays across by four deep, every square between them a deep recessed coffer panel stepped up above the face of the beams with a crisp moulded edge, and one small flush recessed downlight set in the middle of each coffer; there is NO vault, no slope, no ridge, no rafter and no truss anywhere in this room - the ceiling is one single flat coffered plane; white painted drywall walls carrying a white raised-panel wainscot with a moulded chair rail running around the lower third; on the back wall a tall floor-to-ceiling chimney breast of whitewashed painted brick, every brick and every mortar line legible, with a plain white mantel shelf and a simple firebox under it; on the left a bank of three tall arched-top windows reaching almost the full height of the room, white-framed with slim glazing bars; on the right, above head height, a second-floor gallery landing open to the room behind a dark walnut handrail carried on slim black wrought-iron balusters, with the plain white soffit of the gallery floor beneath it. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground, a long upholstered ottoman and a large oat flat-weave rug. Copy the proportions, the flat coffered grid and the depth of its recesses, the raised-panel wainscot and its chair rail, the whitewashed brick chimney breast, the three arched windows and the gallery railing on its black balusters from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the three tall arched windows show a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight in every coffer and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the whitewashed brick chimney breast with warm white lights and deep crimson and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and crimson velvet ribbon laid along the white mantel shelf, cream knitted stockings hanging beneath it, and a large evergreen wreath with a crimson velvet bow hung on the gallery railing. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across every white painted drywall wall and the white raised-panel wainscot below them, across the whitewashed brick chimney breast, across the gallery railing and the soffit beneath it, and across the whole flat coffered ceiling - over every recessed coffer panel and over every face of every white beam crossing between them, with no visible edge, no rectangle and no screen. NO SURFACE IN THE ROOM IS LEFT BARE. Every square inch of wall and ceiling the camera can see is inside the projection, and that explicitly includes THE TALL WHITEWASHED BRICK CHIMNEY BREAST ABOVE THE FIREPLACE: the picture crosses it from the mantel shelf all the way up to the ceiling exactly as densely as it crosses everything else, so that brick carries lit village, Ferris wheel, aurora bands, stars and drifting baubles across it and is NEVER a bare white or grey column running up the middle of the frame. The same is true of EVERY SINGLE COFFER PANEL of the ceiling grid and every face of every beam between them, the lower halves of all the walls, the white raised-panel wainscot and its chair rail, the wall above and behind the gallery railing, the white soffit under the gallery floor, the strips of wall between and beside the three arched windows, and the wall on the right - every one of them carries the picture at full density right down to where it meets the floor. If any wall or ceiling surface anywhere in the frame reads as plain paint, plain drywall or plain brick, the image is wrong. LOW ALONG THE WALLS, a whole snowy storybook Christmas village running the full width of the room along the very bottom of the projection - rows of steep-gabled houses and little shopfronts crowded side by side with thick snow heaped on every roof and every small paned window lit warm gold, a tall church rising behind them with a lit steeple and a glowing clock face, a row of market stalls under red-and-white striped awnings with tiny lit wares on them, cast-iron lamp-posts hung with evergreen wreaths lining the little street, and a curl of smoke rising from every single chimney; set into the middle of that village a frozen pond of pale silver-blue ice with a handful of tiny skating silhouettes circling on it, the one cool-coloured thing in the whole picture; rising straight up out of the village on the left an enormous lit FERRIS WHEEL, its great rim and every one of its spokes picked out in crimson and warm gold bulbs, a dozen little gondolas hanging around it and a lit hub at its centre, tall enough to climb most of the height of that wall; and on the right a great golden CAROUSEL under a red-and-white striped canopy, its horses caught mid-rise on twisted brass poles, every scallop of the canopy edge strung with lights and a lit finial on top; ABOVE THE VILLAGE, wide soft aurora ribbons in deep Christmas crimson and glowing ruby red, with warm gold, emerald green and rose magenta threaded between them and only a thin thread of teal, RADIATING OUTWARD FROM THE GREAT STAR OVERHEAD rather than sweeping past in long curves - five or six broad overlapping bands fanning down the walls from that one point, layered over each other so there is very little bare surface left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe; ACROSS THE CEILING OVERHEAD, one colossal EIGHT-POINTED STAR OF BETHLEHEM filling the entire ceiling - four long tapering rays reaching right out into the four corners of the ceiling and four shorter rays between them, a brilliant white-gold core at its centre bleeding outward through warm gold into deep ruby red at the very tips of the rays, the whole star built of countless tiny points of light so it reads as a star of massed light rather than a painted shape, and a fine scatter of sparks trailing off the edge of every ray; CONCENTRIC RIPPLE RINGS spreading outward from that star across the whole ceiling like rings on water, seven of them in crimson and warm gold, each one thinner and fainter than the last as it travels out toward the walls; Santa's sleigh drawn by a team of eight flying reindeer ARCING IN TOWARD the star on a long sweeping curve, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners across the ceiling; a huge pair of ornate gold CHRISTMAS BELLS hanging high on one wall, tied together with a big crimson velvet bow, every scroll of their casting picked out in light and a bright clapper glowing inside each; floating glowing BAUBLES and CANDY CANES drifting through the whole scene at five or six different depths and sizes, the baubles ribbed and faceted in crimson, gold and emerald with a bright cap and a tiny hanging loop, the candy canes striped red and white, the nearest big enough to read the stripe, all of them turning slowly as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the ceiling and every wall; faint wisps of glowing crimson and gold cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE IS LED BY RED. Deep Christmas crimson and glowing ruby red are the dominant colours of the entire picture, warm gold is second, then emerald green, cream white and rose magenta; soft teal survives only as a thin accent inside one or two of the aurora bands. The aurora ribbons are mostly crimson and ruby with gold and emerald threaded between them, the rays of the great star run from a gold core out to deep red tips, the ripple rings are crimson and gold, the village windows and the church clock burn red-gold, the Ferris wheel and the carousel are strung with crimson and gold bulbs, and most of the floating baubles are crimson and gold. Everything is richly saturated, and the small frozen pond is the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue.  AND THE NIGHT SKY BETWEEN THE ELEMENTS IS DEEP AND DARK: everywhere the picture is not occupied by a lit element it is a rich near-black midnight sky of blackened indigo and very dark crimson, NOT white paint, NOT pale drywall and NOT a grey haze. It is that darkness between the elements that makes the bright ones burn. The great star is a STORYBOOK STAR OF BETHLEHEM made of Christmas light with a sleigh flying in toward it, not a space nebula: it must NOT look like outer space, a galaxy, a supernova, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit snowy village, a Ferris wheel, a carousel, flying reindeer and floating baubles in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right. THE PROJECTION IS DENSE AND ROUGHLY NINETY PERCENT OPAQUE, and it is the brightest and most saturated thing in the frame. It lies on the room like an enormous backlit stained-glass window: deep, dense, fully saturated colour at full strength, crimson and ruby and warm gold and emerald at their richest, and it OVERPOWERS the colour of the surface underneath completely. The white painted drywall, the white coffer beams, the white wainscot panels and the whitewashed brick do NOT read as white anywhere inside the projection field - the light has swallowed their colour. The only things that survive through it are the surface's TEXTURE and its SHADOWS: the slight tooth of the drywall, the moulded edges of the coffers and the wainscot, the faces and mortar lines of the brick, the square corners of the beams. That is the ten percent; the colour of the surface is not part of it. It is NOT pale, NOT pastel, NOT milky, NOT hazy, NOT semi-transparent, NOT a faint tint and NOT a washed-out overlay; there is no grey veil over any of it, and no part of the projection is so faint that the bare surface shows through as white. Contrast is extreme: the cores of the great star, the Ferris wheel, the carousel and the lit village windows are near-white hot, the mid-tones are deep saturated crimson and emerald, and the empty sky between them is almost black - never pale paint.  AND IT WRAPS THE ARCHITECTURE. ONE SINGLE PROJECTOR sitting low in the near corner of the room throws all of this from that one point, so the entire picture keystones away from that origin and every surface takes it at its own angle. This is real projected light crossing a real three-dimensional room, so it obeys every surface it lands on.  The flat coffered ceiling is one single plane, so nothing folds at a ridge - instead the grid breaks it everywhere. Every coffer is a sunken box, so the picture STEPS UP into each recessed panel and back down onto the beams between them, and the rays of the great star, the ripple rings and every aurora band visibly kink up and down at every beam they cross, running across the ceiling in a stepped grid rather than as one smooth sheet. The face of each chunky crossing beam that points back toward the projector catches its own bright slice of the picture, offset and stepped from the coffer panel behind it, while the far side and the underside of every beam sit in hard unlit shadow, so the ceiling reads as a lit grid of sunken boxes ribbed by dark beams and never as one flat painted mural. Where the light reaches the top of a wall it breaks again at that corner and runs down the vertical plane at a different angle. The raised-panel wainscot breaks it further, every raised panel and the moulded chair rail catching its own bright band and throwing its own shadow so the picture steps across the lower wall. The whitewashed brick chimney breast breaks it again, every brick catching the light on its own face and every mortar line throwing its own fine shadow. The gallery railing breaks it a fourth time, each slim black baluster catching a bright edge and casting a bar of shadow onto the wall behind it, and the white soffit under the gallery floor takes the picture at its own flat angle. The surface texture stays legible inside the light - the tooth of the drywall, the square edges of the beams and the wainscot panels, the brick faces and their mortar joints - so it still reads as projected light on a real room and never as paint, wallpaper, a sticker or a printed panel. AND EVERY PIECE OF STANDING-PROUD TIMBER AND TRIM THROWS A REAL SHADOW: each chunky coffer beam, each raised wainscot panel, the chair rail and each black baluster casts a hard-edged shadow of itself across the surface behind it, so a dark unlit band runs alongside every beam and every moulding where the picture is blocked. Those cast shadows are the clearest proof that this is light crossing a real room and not a mural, and they must be plainly visible. There is NO falloff anywhere. The picture stays strong, dense and fully coloured right into all four corners of the frame and right up into the corners of the ceiling, with no dim zone, no dark gap, no faded edge and no bare patch at any boundary of the room. Three or four thin volumetric shafts of coloured light hang visibly in the air of the room so the beam itself is seen in the space, but they are narrow and crisply defined and they do NOT fog, veil or soften any part of the picture. EVERY ELEMENT OF THE PROJECTION IS RAZOR SHARP. Each gable and lit window of the village, each spoke and gondola of the Ferris wheel, each horse and every scallop of the carousel canopy, each antler and harness bell on each reindeer, each arm of each snowflake, each stripe on each candy cane and each ray of the great star has a hard, crisp, precisely drawn edge. The thousands of points of light are DISCRETE PINPOINTS - tiny, tight, individually separated dots - and not soft round blobs, not fuzzy balls and not smeared streaks. There is NO bloom, NO glow halo, NO lens flare, NO atmospheric haze, NO soft-focus glaze and NO gaussian softness anywhere over the picture, and the brightest cores stay tight and do not bleed into what surrounds them. The whole frame is in focus from the nearest person to the farthest corner of the ceiling: nothing is out of focus, nothing is soft, and there is no depth-of-field blur and no bokeh anywhere in the image.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the long upholstered ottoman and the tree carry NO projected shapes at all - no snowflakes, no stars, no village, no Ferris wheel, no carousel, no star, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, RAZOR SHARP EDGE TO EDGE AND CORNER TO CORNER at full 2K resolution with fine micro-detail legible everywhere - the knit stitches of the jumpers, the grain of the floorboards, the tooth of the drywall, the faces and mortar joints of the brick and every individual pinpoint of the projection all crisply resolved - perfect lighting, perfectly exposed, hyper realistic, zero motion blur, zero depth-of-field blur, zero bokeh, zero bloom, zero glow haze, zero soft focus, nothing blurry, nothing smeared and nothing soft or gauzy anywhere in the frame, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````

#### Video prompt — `clips/v10_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 4 s · 9:16 · audio on · count 1 · genre auto · speedramp auto · multi_shots false · bitrate standard
**Job** - `53a182b3-65e4-4a1c-9f82-f02e3c82232f`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_194655_53a182b3-65e4-4a1c-9f82-f02e3c82232f.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v10_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_10_assets/starting_frames/v10_c07_g2.png` · Higgsfield media `52c89c73-8abb-4e85-a638-258f60ee7ab4`

````text
Wholesome family Christmas scene, children at home with their family at Christmas.

SUMMARY: two children play in a double-height Christmas great room while a projected snow-village picture is PLAYING across the back wall and the whole flat coffered ceiling and its chunky white beams, thrown there by a projector standing in the room. 4 seconds, one continuous handheld phone take, vertical.

GLOBAL STYLE: crisp real iPhone footage at night, handheld, real-time speed. Sharp and in focus from the first frame to the last, at least as sharp as the start image. No blur, no haze, no soft focus, no washed-out exposure, no colour shift.

ASSET ROLES: @Image 1 is frame 0.0s and controls the great room, the flat deep coffered ceiling of chunky white beams crossing in a grid with a deep recessed panel in every square, the white raised-panel wainscot and its moulded chair rail running round the lower walls, the whitewashed painted brick chimney breast rising the full height on the back wall with its plain white mantel shelf, the second-floor gallery landing on the right behind its dark walnut handrail on slim black wrought-iron balusters, the three tall arched-top windows on the left with snow outside, the lit Christmas tree with its deep crimson and antique gold ornaments and its presents, the large oatmeal linen sectional sofa wrapping the foreground, the long upholstered ottoman, the oat flat-weave rug, the pale oak plank floor, the children and the colour.

SUBJECTS:
THE SMALLER CHILD - a boy of about five with straight black hair, on the rug in front of the sofa, back to camera and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder, turning slowly on the spot.
THE OTHER CHILD - a girl of about eight with short dark curly hair, jumping on the sofa cushions, caught mid-air above them with her knees bent and her arms flung up, the cushion compressed under where she pushed off, bouncing on the spot.
Both in warm cream and oatmeal nordic knitted Christmas jumpers with a row of deep-green fir trees and rust-red reindeer across the yoke, charcoal knitted lounge trousers and thick mustard knitted socks, so their knitted jumpers read clearly. Both stay small in frame, in scale with the huge room. Exactly two children. No third child, no adult, no pet.
THE PROJECTOR - a single Christmas projector switched on and running in the room, out of shot. One lens throws one wide cone of light across the back wall and the whole flat coffered ceiling. Everything glowing on the drywall, the brick and the white beams is that one cone landing.
THE PICTURE - the animated scene that cone is playing: a whole snowy storybook Christmas village running low along the walls with steep-gabled houses and lit shopfronts, a church with a lit steeple and a glowing clock face, market stalls under red-and-white striped awnings and lamp-posts hung with wreaths, a curl of smoke above every single chimney, a frozen silver-blue pond set into the village with tiny skating silhouettes circling on it, an enormous lit FERRIS WHEEL rising out of the village on the left in crimson and gold bulbs and a great golden CAROUSEL under a striped canopy on the right, wide aurora ribbons in deep crimson and ruby red with warm gold and emerald green threaded between them radiating outward from the star overhead, one colossal eight-pointed STAR OF BETHLEHEM filling the entire coffered ceiling with four long rays reaching into its four corners, seven concentric ripple rings spreading outward from it across the ceiling, Santa's sleigh drawn by eight flying reindeer arcing in toward the star with a long tapering trail, a huge pair of ornate gold bells tied with a crimson velvet bow high on one wall, floating glowing baubles and red-and-white striped candy canes drifting at five or six different depths, a dense field of stars of many sizes, long-tailed shooting stars, and a heavy fall of large soft glowing six-point snowflakes and tiny points of light.

HOW THE PICTURE BEHAVES - THIS IS THE ENTIRE POINT OF THE CLIP. In every previous attempt the picture sat dead still like printed wallpaper and the clip was worthless. THE PICTURE IS A FILM PLAYING ON A CINEMA SCREEN: the screen is the drywall, the brick and the white beams and holds perfectly still, while everything inside the picture is in constant motion for all four seconds. The start image is one paused frame of that film; at 0.0s it un-pauses. Matching @Image 1 applies to the great room, the furniture, the children and the colours, not to where any element of the picture sits.
THE PICTURE AS A WHOLE IS ANCHORED. It does not rotate, spin, swing, sweep sideways or slide across the room as one sheet. Its outer boundary stays where it is. The motion lives INSIDE it, element by element:
- THE CHIMNEY SMOKE - every single chimney in the village is smoking, not one of them without its plume. Each thin curl climbs upward out of its chimney pot, leaning slightly to the right, rising about one roof height every second, widening and thinning as it climbs and fading out before it reaches the aurora, while a fresh curl forms at the pot behind it. The plumes are never a fixed painted shape.
- THE RISING SPARKS - a slow steady rise of glowing gold sparks lifts off the village chimneys and climbs the full height of the wall to join the star field, drifting slightly sideways as it goes, new sparks leaving the chimneys continuously so the column never empties.
- THE AURORA - each crimson, ruby, gold and emerald ribbon radiates outward from the great star and ripples ALONG ITS OWN LENGTH, a slow travelling wave running down the band away from the star, about a third of the ribbon's length every second, the ribbon swelling brighter and thinner as the wave passes and its lower fringe combing and re-forming. Each ribbon's overall fan stays where it is on the drywall; the wave inside it travels. Every ribbon on the wall and on the ceiling is doing this at the same time.
- THE SLEIGH AND THE REINDEER - they are FLYING. The team travels steadily across the ceiling on a long sweeping curve away from where it sits in the start image, arcing in toward the great star, covering about a fifth of the ceiling's width every second, so by 4.0s it has crossed most of the way. The reindeer's legs gallop, their heads nod, the sleigh rocks gently behind them, the long tapering trail streams out behind, and the whole team rises and dips a little as it goes. The team is never parked.
- THE FERRIS WHEEL AND THE CAROUSEL - both TURN, steadily and without ever stopping. The enormous lit Ferris wheel turns about its lit hub roughly a quarter of a full turn every second, every spoke sweeping round and every little gondola swinging level underneath its pivot as it rides over the top and down. The golden carousel turns the other way under its striped canopy at about the same rate, its horses rising and falling on their twisted brass poles as they come round, and the lights along every scallop of the canopy edge chasing round the rim.
- THE RIPPLE RINGS - the seven concentric rings SPREAD OUTWARD from the great star across the coffered ceiling like rings on water, each one travelling away from the core toward the walls, widening and thinning and fading as it goes, while a fresh ring is already forming at the centre behind it, so the spread never stops.
- THE SNOWFLAKES AND THE POINTS OF LIGHT - each one drifts downward and slightly sideways about a quarter of the wall's height every second, the way snow falls past a window at night. Each turns slowly on its own centre as it drifts and breathes brighter and dimmer on its own timing. One that reaches the floor line fades out there while a fresh one fades in high near the ceiling beams, so the density holds even.
- THE SMALL TRAVELLERS - the red-and-white striped candy canes and the glowing baubles turn slowly end over end as they drift; the tiny silhouettes keep circling on the frozen pond and the big gold bells swing gently on their crimson bow with the clappers glowing inside them; the long-tailed shooting stars streak across, their tails thinning out behind them, and fade, with fresh ones setting off elsewhere.
- THE STAR FIELD - the small gold stars hold their places and twinkle, each brightening and dimming on its own timing, never all together.
- THE CHURCH CLOCK - the glowing clock face on the church steeple is the ONLY element that holds its position. It stays exactly where it is in the village for the whole clip and only brightens and dims very slightly. Nothing else in the picture is allowed to hold still.
Because the back wall and the whole ceiling are lit by the SAME projector, they are one picture and behave identically at the same instant. Whatever the flakes, the aurora and the stars on the wall are doing, the flakes, the aurora and the stars on the ceiling are doing at the same moment and at the same speed. There is never a still ceiling above a moving wall. Nothing is painted, printed or stencilled on the drywall, the brick or the white beams. NOTHING IS PROJECTED ON THE FLOOR: the pale oak floorboards, the oat flat-weave rug, the oatmeal linen sectional sofa, the long ottoman, the tree and the gifts carry no projected shapes at all.

TIMELINE:
0.0-1.0s the person filming takes one clear step forward; the frame moves in and settles. THE OTHER CHILD bounces on the sofa cushions with both arms up, laughing. THE SMALLER CHILD turns on the rug with his face tipped up.
1.0-2.0s the camera holds in the closer position. THE OTHER CHILD pushes up harder and drops back down onto the cushion, her knees bending and springing back. THE SMALLER CHILD keeps turning and tips his head further back.
2.0-4.0s the camera tilts up in one slow smooth move past the top of the tree until the flat coffered ceiling fills the upper half of the frame, the aurora rippling along it, the ripple rings still spreading outward across it from the great star and the sleigh team still flying in toward that star. Both children stay low in the frame and keep moving.

AUDIO: room tone, two children laughing and squealing, feet thumping on the sofa cushions, feet on a rug. (no BGM). No subtitles.

POSITIVE LOCKS: real-time motion at normal speed throughout - real children moving at real speed with real weight. Exactly two children, and their knitted jumpers read clearly. One continuous take with no cut. The camera makes one move per beat and no more. The picture's outer boundary holds still while every element inside it moves. Walls and ceiling always move together. THE OTHER CHILD stays on the sofa. The picture stays sharp to the last frame.

DO NOT INCLUDE: a frozen or still pattern; chimneys that are not smoking; an aurora that sits still; a sleigh and reindeer parked in one place; a Ferris wheel or a carousel that does not turn; ripple rings that do not spread outward; flakes that only twinkle without travelling; a still ceiling above moving walls; an un-animated coffer panel or an un-animated white beam in any frame; the whole picture rotating, spinning, sweeping or sliding as one sheet; slow motion; floating or weightless movement; any music; children standing still; a third child; an adult; the projector unit in shot; jellyfish, fish, coral or bubbles; blur; a cut; on-screen text; subtitles.
````

**Other takes of C07 on disk (1)**

#### Image prompt — `starting_frames/v10_c07_g1.png`

**Settings** - gpt_image_2_5 · sunburst · 9:16 · 2k · medium · 1520×2688
**Job** - `0beea661-fa15-432f-bf8c-1052a0f512cc`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260920_141642_0beea661-fa15-432f-bf8c-1052a0f512cc.png
**References, in submission order**
- @Image 1: `content/video_1_assets/starting_frames/v1_c07_g2.png` · Higgsfield media `c9a6740d-383b-4829-a7b9-f7a3c079c03f`
- @Image 2: uploaded image, not on the drive · Higgsfield media `4dec9045-2ac2-4a2c-8412-6dc4ae08cfc0`

````text
Recreate @Image 1's camera, light quality and style in a completely different room, with different children and a much bigger projection. Wholesome family Christmas scene, children at home with their family at Christmas. @Image 1 owns the camera, the framing, the poses and the light. @Image 2 is a photograph of a REAL HOUSE and owns the architecture of the room and nothing else - its raking ceiling, its boarding, its tie rods, its walls, its glazed gable and its proportions are to be copied as built; ignore its daylight, its lamps, its time of day and the fact that it is not decorated.

KEEP IDENTICAL: the same vertical 9:16 iPhone photo look, the same camera position and camera height, the same wide framing that shows a whole enormous double-height room with its full ceiling in shot, the same magical low-key evening light in which the only light in the room is the projection itself, and the same two poses - a girl JUMPING ON THE SOFA, caught mid-air above the cushions, knees bent, arms flung up, hair lifted, the cushion compressed under where she pushed off; and a boy standing on the rug in front of the sofa, seen from behind and slightly to the side, head tipped back looking up at the projected ceiling with his arms out in wonder. Both are small in frame, in scale with the huge room - keeping them small preserves the sense of how big the space is.

CHANGE 1 - THE CHILDREN. Different children: the girl is about eight with short dark curly hair, the boy is about five with straight black hair. Both are fully dressed for winter in warm sage-green and cream nordic knitted Christmas jumpers with a row of cream fir trees across the yoke, matching charcoal knitted lounge trousers and thick mustard knitted socks. Wholesome family Christmas scene, children at home with their family at Christmas.

CHANGE 2 - THE ROOM. The room is the real house photographed in @Image 2 - the same house seen earlier in this ad, now from the middle of the great room. Build its architecture exactly as it is built there, as a real room a real builder made: a tall great room under a SINGLE-SLOPE SHED CEILING - one continuous flat plane of narrow white-painted tongue-and-groove boards that starts low over the left-hand side of the room and rakes up in one unbroken climb to a very high eaves line on the right, the board seams all running straight up the slope; the room is held together across that span by three slim black steel tie rods, each a straight round rod running horizontally from wall to wall well below the boards and bolted into a small black anchor plate at each end; small flush recessed downlights are set in a line up the rake; there is NO timber rafter, no ridge, no collar beam, no king post and no vault anywhere in this room - the ceiling is one single straight raking plane; cream plaster walls; under the high side of the rake on the right, an almost full-height glazed gable wall of slim black steel frames divided into many small rectangular panes, rising with the slope; on the back wall a wide cream plaster fireplace with a long low horizontal firebox and a tall potted olive tree standing beside it; along the left an open kitchen with deep forest-green slab cabinetry, aged brass hardware, a pale stone island and woven rattan counter stools. Pale oak plank floor, a very large oatmeal linen sectional sofa wrapping the foreground and a round dark walnut coffee table on a large oat flat-weave rug. Copy the proportions, the single raking plane, the direction of the board seams, the three black tie rods and their anchor plates, and the tall black glazed gable from @Image 2 exactly - this is a photograph of a room that exists, and the finished picture must still read as that room.

TWO THINGS CHANGE FROM @Image 2. First, it is night: the tall glazed gable shows a dark blue snow-covered night outside, there is no daylight anywhere in the room, every recessed downlight and every fixture in the house is switched off and dark, and the projection is the only light. Second, the room is decorated for Christmas: a very tall real Christmas tree standing against the cream plaster back wall beside the fireplace with warm white lights and sage-green and antique gold ornaments and wrapped gifts beneath it, a thick evergreen garland with pine cones and sage-green velvet ribbon laid along the plaster above the firebox, cream knitted stockings hanging beneath it, and a large evergreen wreath with a sage-green velvet bow hung on the glazed gable wall. Nothing else about the room changes.

CHANGE 3 - THE PROJECTION, and this is the part that matters most. It is ONE enormous cinematic Christmas night scene - a single continuous picture, NOT scattered floating icons - and it is far bigger, denser and more beautiful than in @Image 1. It reads as one unbroken field across the entire cream plaster back wall, the plaster walls either side of it, the whole raking boarded ceiling from its low edge up to the high eaves and the three black steel tie rods strung beneath it, with no dark unlit wedge and no hard diagonal seam anywhere in the frame, with no visible edge, no rectangle and no screen. LOW ALONG THE WALLS, a deep snow-laden pine forest running the whole width of the room along the very bottom of the projection, rank behind rank of little glowing firs in emerald green and warm gold with snow heaped on every branch, and rising straight out of that forest on the left a whole ornate fairy-tale Christmas city built of lit gold - tier upon tier of slender spires, ribbed onion domes, arched galleries and pinnacled towers stacked up the wall, every arched window lit warm gold, fine gold filigree running along every cornice and balustrade, thick snow lying on every ledge and roof and dome, the whole city glowing as though it were carved out of light; and winding out of the pines on the right a long lit steam train, a dark locomotive leading eight carriages whose windows all glow warm gold, a bright plume of steam and sparks trailing back over the carriage roofs and a glowing gold rail curving away behind it through the trees; ABOVE THE FOREST AND THE CITY, wide soft aurora ribbons in emerald green, rose magenta, warm gold and soft teal sweeping up the walls in long slow curves and carrying over onto the single raking shed plane, five or six broad overlapping bands layered over each other so there is very little bare boarded slope left between them, each band shot through with a fine glittering grain so it reads as a river of stars rather than a painted stripe, where they lie flat along the rake and run straight up it with the climb of the plane instead of hanging as vertical curtains, and are stretched longer and thinner the further up the slope they travel; ACROSS THE RAKING CEILING OVERHEAD, one colossal spiral whirlpool of light filling most of the slope - seven concentric glowing rings of emerald green, warm gold and rose magenta winding in on each other in a slow tightening spiral and drawing down to one brilliant white-gold core at the very centre, every ring built of countless tiny points of light so the whole thing reads as a whirlpool of stars rather than a painted disc; Santa's sleigh drawn by a team of eight flying reindeer sweeping straight out of the mouth of that spiral, seen side-on in glowing warm gold and large enough to read every antler, the harness and bells on each reindeer, the curved runners and Santa himself sitting up in the sleigh with his sack behind him, a long bright tapering trail of golden light streaming back behind the runners into the spiral, the whole team lying flat on the rake so it is keystoned and stretched by the climb of the plane, growing larger and brighter as it rises toward the tall glazed gable; a big pale blue full moon glowing high on the cream plaster chimney breast on the back wall, cool silver-blue and softly cratered and the one cool-coloured thing in the whole picture, with the tiny black silhouette of a second sleigh and its reindeer team crossing right over the face of it; floating wrapped Christmas gifts drifting through the whole scene at five or six different depths and sizes, each a solid glowing box in gold, emerald or rose with a bright ribbon cross and a big soft bow on top, the nearest big enough to read the weave of the ribbon, all of them turning slowly end over end as they drift; a dense field of stars at many different sizes, hundreds of them, from tiny pinpricks to a few large bright ones with soft radiating rays, with four or five long-tailed shooting stars crossing at different angles with bright tapering trails; large soft glowing six-point snowflakes in cream and pale gold at several different sizes, the nearest big enough to read every arm, drifting across the raking boards and both walls; faint wisps of glowing cloud between the aurora bands; and over all of it a heavy fall of hundreds of tiny bright points of light drifting down the walls like real snow caught in a beam. It stays ONE continuous night-sky picture, richly packed and busy, not scattered separate icons. THE PALETTE: emerald green, warm gold, cream white, rose magenta and soft teal, richly saturated against the white boards and the cream plaster, with the single pale blue moon as the only cool note anywhere in it. NO grey, no muddy brown, no violet and no harsh electric blue. The great spiral is an AURORA WHIRLPOOL made of Christmas light with a sleigh flying out of its mouth, not a space nebula: it must NOT look like outer space, a galaxy, a wormhole, a tunnel or anything science-fiction, alien or dystopian - it is a storybook Christmas night sky with a lit gold Christmas city, a steam train, flying reindeer and falling gifts in it. Every element is a separate glowing shape sitting on the surface - nothing is painted, printed, stencilled or wallpapered, and nothing is a flat repeating texture. HOW THE LIGHT SITS ON THE SURFACES, and this has to be exactly right: it is projected light landing on real plaster and real painted boarding, not paint and not a sticker. The light is TRANSLUCENT - the white-painted boards of the slope and the fine seam between every board, the three slim black steel tie rods and their black anchor plates, and the line of flush recessed downlights running up the rake, all stay clearly visible THROUGH the coloured light, and each black tie rod breaks the light with its own hard shadow line where it hangs below the boards. Every shape is soft-edged and feathered with no hard opaque border, and is keystoned, stretched and skewed by the surface it lands on. The light falls off with distance: brightest where the beam first strikes, then steadily fainter, softer and paler, with the far corners fading to bare plaster. Even packed full it must still read as projected light on a real single-slope boarded ceiling with black steel tie rods crossing beneath it, never as paint, a sticker or a printed panel. Three or four faint volumetric shafts of coloured light hang visibly in the air of the room, so the beam itself is seen in the space.

CHANGE 4 - NOTHING IS PROJECTED ON THE FLOOR. The projected imagery lives on the WALLS and the CEILING only. The pale oak floorboards, the oat flat-weave rug, the oatmeal sectional sofa, the round walnut coffee table and the tree carry NO projected shapes at all - no snowflakes, no stars, no city, no train, no sleigh, no falling light on them - they are lit only by the soft warm colour spill coming off the walls and sit in gentle shadow. Both children catch that spill so their knitted jumpers read clearly.

CHANGE 5 - the projector unit must NOT be visible. No projector, no round side table, no glowing device anywhere in frame. The corner it would occupy is plain rug and floor.

Vertical 9:16 photo, shot on an iPhone 16 Pro, natural handheld UGC look, extremely high quality, tack sharp edge to edge, perfect lighting, perfectly exposed, hyper realistic, zero motion blur, nothing blurry or soft, no CGI look. Normal wide-angle lens, straight vertical lines, no fisheye distortion.

No text, no captions, no watermarks, no lettering anywhere in the image.
````
