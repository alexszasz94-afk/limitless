# Video 25 — Reindeer, Tree, Elf

**Current status — verified 2026-09-21:** local finished export present at `../../videos_to_post/video_25.mp4`. Earlier stages and decisions below are retained as history; this check does not verify posting.

Hook plus the same six beats again, with a new woman, a cream stucco install wall and three new pictures in the bulbs. The hook frame is deliberately the still moment before the kick — the tree goes over in the clip, not in the frame.

| | |
|---|---|
| **Runtime** | 16.02s |
| **Stage** | Final cut |
| **Resolution** | 2160×3840 |
| **Shots** | 7 in final cut |
| **Frames** | gpt_image_2 · 2k · medium |
| **Takes** | 6 frames · 6 kept |
| **Regens** | none — one generation per shot |

**Final cut** — C01 → C02 → C03 → C04 → C05 → C06 → C07

**Continuity locks** — C02 → C03 same woman · C03 → C04 same wall & background

**Brief** — Exactly the same, just change some things — different women, houses, backgrounds, animation

## C01 — Kicking the taped-up tree

Night living room. An ugly artificial tree is wrapped in spiralling silver duct tape with deflated inflatables taped flat to the branches. The man stands in the left foreground, three-quarter rear, feet flat and fists clenched — the still beat before the kick.

**Status** CLIP · #1 
**Frame** `v25_c01_g1.png` 
**Clip** `v25_c01_g1.mp4` 
**Settings** gpt_image_2 · 2k · medium · 1520×2688 · 9:16 · seedance 2.5 · 720p · 5s

**References passed**

- @Image 1 · v25_c01_g1.png — The g1 frame, reproduced exactly — room, tree, tape spiral, taped-on inflatables, cords, floor clutter, sofa, lamp, curtains, night lighting and the man’s position and size in frame. One change only: more empty space at the top.

### Image prompt

```text
@Image 1 is a photograph. Reproduce it EXACTLY - the same living room, the same tall artificial tree wrapped in spiralling silver duct-tape bands, the same deflated inflatable Santa, snowman, reindeer and penguin taped flat to the branches in exactly the same positions, the same lopsided foil star on top, the same cords trailing to the orange extension leads, the same plastic storage tub, tape roll, scissors and air pump on the floor, the same beige sofa, the same framed photos, the same lamp, the same curtains, the same warm night lighting, and the same man in the grey marl sweatshirt and dark jeans standing in the left foreground with his back three-quarters to the camera, feet flat, fists clenched, looking up at the tree - in exactly the same position and at exactly the same size in the frame.

CHANGE ONE THING ONLY: ADD A LITTLE MORE EMPTY SPACE AT THE TOP OF THE FRAME. Tilt the camera down very slightly so there is a clean band of plain empty ceiling and bare wall above the star at the top of the picture - a little more headroom than in @Image 1, about one tenth of the frame height of clean empty space, so a text caption can sit there. JUST A LITTLE - do not zoom out, do not move the camera back, do not shrink the tree or the man, do not add anything into that space. The tree top and star must still be high in the frame, just with a small clean gap above them.

Everything else identical.

IMAGE QUALITY - CRITICAL: a real photo taken on a recent iPhone. Extremely high quality, hyper realistic, tack-sharp across the whole frame, clean natural warm indoor lighting. Absolutely no blur, no softness, no smearing, no heavy noise, no shallow-depth-of-field bokeh, no cinematic colour grade, no vignette, no haze, no bloom, no motion blur, no CGI polish. Real amateur phone photo, natural noise. No text overlay, no captions, no watermark, no logos.
```

### Video prompt

```text
The attached start frame is frame one. Animate it exactly as it is: the same ugly-decorated living room, the same Christmas tree with plush and inflatable decorations duct-taped to its branches and wide tape bands spiralling down it, the same man standing in front of the tree, the same lamps and lighting, the same clothes, the same everything.

CAMERA: locked handheld. The camera does not move to a new position at any point — no zoom in, no zoom out, no push, no pull, no pan, no tilt, no orbit, no rack focus. The only movement is a tiny natural handheld micro-shake, as if someone is standing still holding a phone. The framing at 5.0s is the same framing as at 0.0s. NOTHING of the camera operator is visible — no phone, no screen, no hand, no fingers, no arm, no sleeve, no device, no object in the foreground or along any edge at any moment.

TIMELINE (5 seconds):
0.0-0.8s — The man is rigid with rage. His fists clench tighter, his shoulders rise, his head tips back and he yells at the tree, his whole upper body shaking.
0.8-1.6s — He takes one hard step toward the tree, weight shifting onto his left foot, right arm swinging back, still shouting.
1.6-2.3s — THE KICK. He drives his right foot hard into the lower trunk of the tree — one single violent kick, boot connecting with the taped branches, the impact snapping his leg straight.
2.3-3.3s — The tree goes over. It tips away from him, the taped plush and inflatable decorations tearing loose and flying off, tape strips fluttering, baubles bouncing, the trunk swinging down through the frame.
3.3-5.0s — The tree crashes onto the floor with a heavy thud and a spray of needles and ornaments. The man stands over it, chest heaving, both arms flung out to the sides, still yelling down at the wreck.

AUDIO: natural room sound only — the thud of the kick, branches snapping, tape tearing, ornaments bouncing on the floor, the heavy crash of the tree. The man shouts furiously: "I'M DONE WITH THIS! DONE!" No music, no score, no background song, no narration.

Hyper-realistic amateur iPhone video, extremely high quality, real weight and physics on the tree and the flying decorations, natural indoor lighting, natural motion blur, no slow motion, no text, no watermark, no logo.
```

### Rejected takes

- **v25_c01_g1.png · take 1** — No clean strip at the top of the frame, so there was nowhere for the CapCut headline to sit without covering the tree. Everything else was right, so g2 was written as a single-change edit rather than a new prompt.

### What made it work

Generate the still beat, not the action — the action belongs to the video. The frame is deliberately the moment BEFORE the kick: feet flat, fists clenched, jaw set. Putting the kick in the start frame gives the clip nothing left to do.

Headroom is a one-change edit, not a re-prompt. g2 reproduces g1 in an exhaustive inventory and then says “CHANGE ONE THING ONLY”. Re-describing everything is what stops the room, the tree and the man drifting while the crop moves.

A reference can be attached for a single detail. g1 used Daniel’s “Christmas Decor in 1965” screenshot for one thing — the wide duct-tape bands spiralling down the tree with figures taped flat to the branches — with its room, staircase, ladder and woman explicitly excluded.

## C02 — Box over the sofa

Sage-green wall, charcoal linen sofa running diagonally away in front of her with the cushions empty, camera at her shoulder height over the left shoulder.

**Status** CLIP · #2 
**Frame** `v25_c02_g1.png` 
**Clip** `v25_c02_g1.mp4` 
**Settings** gpt_image_2 · 2k · medium · 1520×2688 · 9:16 · seedance 2.5 · 1080p · 5s

**References passed**

- @Image 1 · v20_c02_g1.png — the canonical C2 framing - camera, crop and the sofa in front of her running diagonally into depth. Composition only.
- @Image 2 · v24 C2 (job) — camera height only - shoulder height. Explicitly not the hair, clothing, sofa colour, wall or tree.

### Image prompt

```text
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: an early-thirties East Asian woman with fair warm-toned skin and straight black hair falling to her shoulder blades with a blunt fringe, wearing a cream cable-knit jumper and light-wash jeans. The room has a warm walnut floor, a charcoal-grey linen sofa with cream and rust cushions and a chunky cream knit throw, a sage-green painted wall, a brass arc floor lamp, and a real green Christmas tree with multicolour lights and gold baubles at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

Real iPhone photo, tack-sharp, candid UGC, no text overlay, no watermark.
```

### Video prompt

```text
TWO SCENES IN ONE CLIP, JOINED BY ONE HARD CUT AT EXACTLY 2.5s. No dissolve, no fade, no whip pan, no transition effect — a straight in-camera cut, exactly like a creator cutting two takes together.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she walks at a walking pace, she kneels at the speed a body really kneels, the lid swings open at the speed heavy cardboard really swings. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in five seconds — one slow lowering, one slow kneel, one slow lid. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still settling as the clip ends than that any part of it looks fast-forwarded.

REFERENCE IMAGES. Reference image 1 is the first frame of scene 1 — start there, unchanged, and it owns the room, the woman, the camera angle and the geometry. Reference image 2 is the CLOSED PRODUCT BOX: the artwork on the box in this video must match it exactly. Reference image 3 is the OPEN BOX INTERIOR: what she reveals in scene 2 must match it exactly.

THE WOMAN — she is exactly the woman in reference image 1 and never changes: an early-thirties East Asian woman with fair warm-toned skin and straight black hair falling to her shoulder blades with a blunt fringe, in a cream cable-knit jumper and light-wash jeans. Same hair, same fringe, same skin, same clothes, first frame to last.

BOX SPEC — TRUE IN EVERY FRAME. A matte black rigid retail box, 55 cm wide x 42 cm tall x 10 cm deep. It is BIG — much wider than the span of two outstretched hands; each of her hands covers less than a quarter of the box width, and laid on the sofa seat it spans most of one cushion. Front panel top to bottom: a large white condensed uppercase headline LED CURTAIN LIGHTS; a warm gold subline Create Your Own Magic; a red diagonal BEST SELLER ribbon flag in the top-right corner; one large photographic panel with a thin gold hairline border showing a night house facade with a glowing pixel LED Christmas tree on the garage door; a bottom row of five small gold line icons with white captions. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible through the front, NO glowing lights showing through the cardboard. The box is closed and sealed until the moment she opens it in scene 2.

SCENE 1 — 0.0 to 2.5s. CAMERA: HELD IPHONE, LOCKED FOCAL LENGTH, portrait, a friend filming from just behind her left shoulder at HER SHOULDER HEIGHT, tilted down only very slightly — exactly where reference image 1 was taken. NOT above her head, NOT a top-down shot. NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO DOLLY. Handheld micro-shake only. She is at the LEFT EDGE of frame, partly cut off by it; the charcoal-grey linen sofa is directly IN FRONT of her, running diagonally away into depth and filling the right and bottom-right of frame, its empty seat cushions facing up. The room behind her — the warm walnut floor, the sage-green painted wall, the brass arc floor lamp, the cream and rust cushions, the chunky cream knit throw and the real green Christmas tree with multicolour lights and gold baubles at the right — stays exactly as it is and never changes.
THE WHOLE POINT OF SCENE 1: she carries the box round in front of the sofa, sets it flat on the seat cushion AND drops to her knees IN THE SAME CONTINUOUS MOTION. These are not two separate steps — the box going down and her body going down are one move.
0.0-0.9s — one unhurried step forward and to her right, her shoulders turning, the heavy box swinging slowly out in front of her; her straight black hair swings across her back and settles, her cream sleeve creases with the weight.
0.9-1.8s — she steps in front of the sofa and leans forward from the hips, lowering the box steadily toward the empty charcoal-grey linen seat cushion, arms extending, knees already bending underneath her. This lowering is SLOW and heavy — the box is big and awkward and she is being careful with it.
1.8-2.5s — the box settles flat and printed-side-up on the cushion with a soft compression of the linen, her hands still on it, and in the same continuous motion her knees come down onto the warm walnut floor one after the other, her weight settling and her back rounding forward; she tucks a strand of hair behind one ear and plants both palms flat on the box lid, chest rising with one excited breath.

HARD CUT AT 2.5s.

SCENE 2 — 2.5 to 5.0s. Direct continuation, same room, same second, same woman, same cream cable-knit jumper, same box in exactly the same place on the same charcoal-grey cushion. The camera has moved about 30 degrees round to her side — a slightly more side-on three-quarter angle, a little lower, closer to the level of the sofa seat, so we now see the lid edge in profile and read the pivot clearly. Still HELD IPHONE, LOCKED FOCAL LENGTH, handheld micro-shake only, NO ZOOM.
LID MECHANISM, GEOMETRICALLY. The box is a magnetic-closure flip-top. The hinge runs along the TOP LONG EDGE of the box — the far edge away from her, at the back. The lid pivots UP and BACK on that hinge, rotating away from her and toward the back of the sofa, keeping its printed front face turned toward the camera as it rises. The inside of the lid is matte black. The lid is NEVER lifted off, NEVER removed, NEVER carried aside, NEVER set down, NEVER folded flat instantly, NEVER slid out like a drawer.
2.5-3.1s — she hooks her fingertips under the near front edge of the lid; a small snap as the magnets release and the front edge lifts a centimetre, a thin black shadow line opening slowly across the whole 55 cm width.
3.1-4.3s — she pivots the big printed lid UP and BACK on its hinge in ONE slow continuous arc with real cardboard weight, her elbows rising and her shoulders lifting with the effort, until it stands roughly vertical. This arc takes well over a full second of screen time — it travels heavily and never flips or snaps open.
4.3-5.0s — the interior is revealed exactly as reference image 3: the neatly folded BLACK LED mesh curtain lying in its tray, the coiled black lead and the small accessory items beside it, all against a matte black interior. She reaches in with both hands and touches the folded black mesh, fingers spreading it slightly, then lifts her chin, looks off toward the tree and breaks into a big open-mouthed grin, eyebrows up.

MOVEMENT RULE FOR BOTH SCENES: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole clip — weight shifting, chest breathing, hair and sleeves swinging and settling, the cushion compressing under the box — and her face keeps changing, eyes, eyebrows and mouth reading differently moment to moment. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses.

HARD RULES: exactly ONE cut, at 2.5s. The box never changes size, never changes artwork, never gains a window or a cutout. The curtain inside the box is BLACK cord with small dark bulbs — never white wire, never clear wire, never silver wire. Nobody else enters frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Quiet warm living-room ambience, the soft thump of a heavy box on a cushion, knees on the floor, the click of magnets releasing, stiff cardboard flexing, plastic mesh rustling, one small delighted exhale.

LOOK: real iPhone UGC indoors at night. Warm mixed lamp and fairy light, slight sensor noise in the shadows, natural skin, no cinematic grade, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
```

### Rejected takes

_None recorded. If you rejected a take here, write why on this line._

## C03 — Pinning the curtain up

Warm cream stucco wall with dark bronze gutter and downpipe, flat frontal camera, black strands on the wall and a black tangle on the snow at the foot of the stool.

**Status** CLIP · #3 
**Frame** `v25_c03_g1.png` 
**Clip** `v25_c03_g1.mp4` 
**Settings** gpt_image_2 · 2k · medium · 1520×2688 · 9:16 · seedance 2.5 · 1080p · 4s

**References passed**

- @Image 1 · v24 C3 g3 (job) — framing and black wire - the first frame in the series that carries both the corrected flat frontal camera and the black cord. Never point C3 at a v20-v23 install frame; those all have white wire.
- @Image 2 · v25 C2 (job) — the woman only.

### Image prompt

```text
Same shot as the FIRST attached image - copy its camera, framing and staging EXACTLY. Daytime, overcast winter light, snow on the ground. A woman stands on a black folding step stool, seen from BEHIND, facing the house wall, both arms raised in front of her at the top of the wall, her hands up near the gutter line as she fixes the LED curtain to it. The big bundle of unlit LED curtain strands is heaped on the snow at the foot of the stool.

THE CAMERA ANGLE IS FLAT AND FRONTAL, exactly as in the first image: the wall faces the camera almost square-on and fills the frame, the vertical lines of the siding run straight up and down. The wall is NOT turned away at an angle, NOT receding steeply into the distance, NO strong oblique perspective, NO wide-angle corner view.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand hanging down the wall is a thin BLACK cord with small DARK unlit bulbs on it. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - take her from the SECOND attached image: the same early-thirties East Asian woman with fair warm-toned skin and straight black shoulder-blade-length hair with a blunt fringe. Outdoors she wears a deep teal parka with a faux-fur hood trim, grey jeans and brown boots.

A COMPLETELY NEW HOUSE AND BACKGROUND - take these from this text only, NOT from the first attached image: the wall she is working on is WARM CREAM STUCCO with a dark bronze gutter, dark bronze fascia and a dark bronze downpipe running down the right side. A low dark-stained wooden fence runs along the right of the frame. A bare white birch tree stands beyond the left corner of the house. A red-brick neighbour house is visible at the far right edge. Do NOT copy the slate-blue board-and-batten siding, the white trim, the brick garden wall or the hedge from the first image.

Real iPhone photo, tack-sharp, candid UGC, no text overlay, no watermark.
```

### Video prompt

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same overcast winter day, same WARM CREAM STUCCO wall filling the frame, same dark bronze gutter and dark bronze fascia along the roof edge, same dark bronze downpipe and low dark-stained wooden fence at the right, same red-brick neighbour house at the far right edge, same bare white birch beyond the left corner, same snow on the ground, same black folding step stool, same woman seen from behind in the deep teal parka with the faux-fur hood trim, grey jeans and brown boots, standing on the stool with both arms raised pinning the gathered fistful of unlit net up under the gutter, same LED net already hung flat across the wall to her left, same loose tangled coil of curtain heaped on the snow at the foot of the stool.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she reaches at the speed an arm really reaches, she shakes the net out at the speed a heavy tangled net really swings, she shifts her weight at the speed a body really balances on a step stool. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in four seconds — one slow shake, one slow reach, one slow sideways press. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still mid-reach as the clip ends than that any part of it looks fast-forwarded.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH. Portrait, exactly the framing and the angle of the reference image, flat and frontal to the wall, looking slightly up at it. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT. The wall, the dark bronze gutter, the wooden fence and the stool stay exactly the same size in frame from the first frame to the last, and the camera never swings round to an oblique or corner-on view of the wall.

MOVEMENT RULE: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole four seconds — weight shifting on the stool, shoulders rolling, ribs breathing, the faux-fur hood trim stirring, the teal parka creasing and rustling, the strands swaying on after every touch. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses, and no limb ever travels faster than a real arm travels.

ACTION TIMELINE (4 seconds, one continuous take, no cuts) — ONLY TWO THINGS HAPPEN, AND BOTH ARE SLOW:
0.0-2.0s — she lifts the gathered bundle in her right hand and shakes it out ONCE, slowly and heavily. The shake takes well over a full second of screen time: her arm swings out and down, the tangled net lets go in stages rather than all at once, and a long sheet of black strands falls open down the cream stucco and swings for a moment before it settles. The loose coil on the snow drags and shifts with it.
2.0-4.0s — still up on the stool, she stretches both arms high and presses the header wire up under the lip of the dark bronze gutter, her thumbs working slowly along it, then walks her hands a short way sideways to her RIGHT along the roofline, onto the bare stretch of wall beyond the strands she has already hung, pressing and tucking as she goes, her torso twisting and her heels lifting and dropping on the tread. She is STILL tucking when the clip ends. The curtain sways gently against the stucco and is still settling on the last frame.
THAT IS THE WHOLE CLIP. She does NOT step down off the stool, does NOT step back, does NOT plant her hands on her hips and does NOT tilt her head back to look at her work. There is no time for any of that at real speed, and cramming it in is exactly what would force the footage to look sped up. She stays on the stool from the first frame to the last.

THE LED CURTAIN IS BLACK — CRITICAL. The wire is BLACK, not white and not clear. Every vertical strand hanging down the wall is a thin BLACK cord and the unlit bulbs on it are small and DARK. Against the warm cream stucco the strands read as thin dark lines, clearly visible the whole four seconds. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire appears at any moment.

HARD RULES: the curtain is COMPLETELY OFF the entire time — not one bulb lights, no glow, no colour, no animation on the wall. The wall never gains windows, doors or new features, the dark bronze gutter and downpipe never move and the wooden fence never changes. The strands are separate vertical strands obeying gravity, sagging slightly, with an uneven wavy bottom hem — never a flat sheet, never a panel, never a screen. The loose coil rests in the snow with real contact shadows. Her face is never shown; she stays turned away from camera throughout. No other people enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor winter ambience, thin plastic strands rattling and clicking against stucco, a step-stool creak, boots on a metal tread, boots compressing snow, one quiet effortful breath. No voice.

LOOK: real iPhone UGC. Flat overcast winter daylight, slightly cool white balance, mild sensor noise, natural skin, no cinematic grade, no lens flare, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
```

### Rejected takes

_None recorded. If you rejected a take here, write why on this line._

## C04 — Phone POV, wall dead-on

Same cream stucco wall at night, camera square to it, black curtain already mounted, phone held up at the bottom centre with the scene grid glowing.

**Status** CLIP · #4 
**Frame** `v25_c04_g1.png` 
**Clip** `v25_c04_g3.mp4` 
**Settings** gpt_image_2 · 2k · medium · 1520×2688 · 9:16 · seedance 2.5 · 1080p · 4s 
**Take note** take 3 · reindeer looked photoreal, animation was flat

**References passed**

- @Image 1 · v24 C4 g3 (job) — framing, the mounted black curtain and the lit app screen.
- @Image 2 · v25 C3 (job) — the house - it must read as literally the same wall, now at night.

### Image prompt

```text
Same shot as the FIRST attached image - copy its camera, framing and staging EXACTLY. Night.

THE CAMERA ANGLE IS DEAD-ON SQUARE TO THE WALL, exactly as in the first image: the wall faces the camera flat and fills the frame, its vertical lines run straight up and down. The wall is NOT turned away at an angle, NOT receding into the distance, NO strong oblique perspective, NO corner view.

TWO THINGS THAT MUST BE PRESENT, exactly as in the first image - do not omit either:
1. The LED CURTAIN IS ALREADY MOUNTED ON THE WALL, hanging in evenly spaced vertical see-through strands from the gutter line down across the wall, with slight natural sag and an uneven bottom hem.
2. At the BOTTOM CENTRE of the frame, a hand holds a smartphone up toward the wall, screen facing the camera and BRIGHTLY LIT, showing a real phone app UI: a dark blue app screen with a grid of small square scene thumbnails and a large round play button - the screen glows and lights the hand.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand is a thin BLACK cord with small DARK unlit bulbs on it, no glow. The strands still read clearly as thin dark vertical lines against the wall, caught by the street lamp from the left and the porch light from the right so they stay visible, not invisible. No white wire, no clear wire, no silver wire anywhere.

THE HOUSE - take it from the SECOND attached image: the SAME wall, the same WARM CREAM STUCCO, the same dark bronze gutter, dark bronze fascia and dark bronze downpipe on the right, the same low dark-stained wooden fence at the right, the same bare white birch tree beyond the left corner, the same red-brick neighbour house at the far right edge. It must read as literally the same house, now at night.

Lighting: a street lamp glow from the left and a warm porch light from the right, snow on the ground catching the light. Real iPhone night photo, tack-sharp, candid UGC, no text overlay, no watermark.
```

### Video prompt

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same WARM CREAM STUCCO wall of the house seen dead-on and flat, filling the frame, with the UNLIT LED curtain hanging in thin black vertical strands across it, same dark bronze gutter along the top and dark bronze downpipe at the right, same dark-stained wooden fence at the right, same snow in the foreground, same hand coming up from the bottom holding a phone up in the lower part of frame, same app screen showing a dark blue grid of small colourful scene tiles with a BIG ROUND BLUE PLAY BUTTON at the bottom of the screen.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, handheld micro-shake only. The camera stays DEAD-ON SQUARE to the wall the whole four seconds — it never swings round to an oblique angle, never turns to a corner view, never tilts up. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY. The wall and the phone stay exactly the same size in frame throughout.

THE SINGLE MOST IMPORTANT THING IN THIS CLIP IS THE SYNC. The thumb presses the big round PLAY button, and ON THAT VERY SAME FRAME the wall lights up. Not a frame early, not a frame late, no gap, no delay, no anticipation, no lag. The press and the light are ONE event. And the instant the button is pressed the hand immediately drops away out of the bottom of frame — it does not linger, does not hold the phone up to admire the wall, does not stay in shot for even half a second after the press.

THE PHONE PART IS SHORT. THE LIT PART IS MOST OF THE CLIP. The phone is finished and gone by 1.3s. From 1.3s to the very last frame — nearly THREE FULL SECONDS — there is nothing in the foreground and the wall is lit and animating hard. The animation must NOT be squeezed into the last second and must NOT be a slow, sparse, gentle thing.

HOW THE PICTURE IN THE LIGHTS IS DRAWN — READ THIS BEFORE ANYTHING ELSE. It is FLAT CARTOON LIGHT ART built out of individual glowing bulbs, like a chunky neon shop sign or a big pixel sprite. Thick simple outlines, flat blocks of colour, big silly cartoon face. It is NOT a photograph. It is NOT a realistic person or animal. It is NOT 3D, NOT rendered, NOT shaded, NOT textured, NOT furry, NOT lifelike, and NOT a video projected onto the wall. If it could be mistaken for a photo of something real, it is wrong. Think cheap funny Christmas light display, not fine art.

ACTION TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.8s — A SHORT SCROLL, NOT A LONG ONE. The thumb comes in from the bottom and gives the grid of scene tiles ONE small flick: the tiles slide up by roughly ONE ROW only, a single fresh row of new scene thumbnails comes into view from the bottom, the list overshoots slightly and settles back with a small bounce. That is the entire scroll. NO long scroll, NO repeated flicks, NO second flick, NO rows racing past, NO scrolling through the whole list. One tile in the grid keeps its bright highlight ring the whole time — the scene is already chosen.
0.8-1.0s — the thumb slides straight down to the BIG ROUND BLUE PLAY BUTTON at the bottom of the app screen and comes to rest on it.
1.0s — THE THUMB PRESSES PLAY. On that exact frame the button visibly depresses and flashes, AND the entire wall SNAPS ON at full brightness in the very same single frame. NO fade, NO dissolve, NO ramp, NO brightness curve, NO bulbs lighting one by one, NO sweep across the wall, NO pause between the press and the light. One frame dark, the next frame fully lit at maximum brightness.

THE ARTWORK THAT APPEARS — SANTA LOSES HIS TROUSERS. One full-height cartoon SANTA drawn in bulbs, standing facing the camera in the middle of the lit area. His broad black belt has POPPED OPEN and swings loose, and his big red trousers have dropped straight down and are bunched around his black boots. Underneath he is wearing enormous baggy long underpants in red and white candy stripes with little white hearts on them. Both his white-gloved hands grab at the fallen waistband, his eyes are two huge white circles, his mouth is a big round O, his cheeks are two bright pink dots and his white beard is flying sideways. His red sack has been dropped and lies tipped over at his feet with a couple of coloured presents rolling out. Down at the bottom left a small GREEN ELF is doubled over laughing, pointing straight up at him with one arm, hat flopping. Colours: bright red, white, black, green, pink and gold. A ring of gold stars pops around Santa's head.

1.0-1.3s — the hand drops straight down and out of the bottom of frame fast and NEVER returns. The phone, the hand, the fingers and the sleeve are completely gone from frame by 1.3s and no part of them reappears at any point.
1.3-4.0s — THE REST OF THE CLIP IS THE LIT WALL ALONE, and it is relentless. See the movement block below.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. From the moment the wall snaps on, SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least NINE separate changes between 1.3s and the last frame — and at every single instant AT LEAST TWO things are changing at once: Santa's whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no pause, no settle, no gentle drifting. Every beat is a clearly DIFFERENT WHOLE-BODY pose — arms, legs, head and body all in a new position — the figure fully redrawing between beats like an animated light-bulb sign. If two consecutive beats look similar, it is wrong.
1.3s — it lands out of the snap-on already mid-move: Santa bent forward at the waist, both hands snatching down at the fallen trousers, knees knocked together, while the gold stars around his head flash on and the elf's laughing mouth flips wide open.
1.6s — he hauls the trousers UP to his knees with both arms straight up above his head from the effort, chest thrown out, and a bright chase of colour runs across the candy stripes of his underpants from left to right.
1.9s — the trousers drop straight back down to his boots, Santa's arms fly out wide to both sides in a huge shrug, head thrown back, and every gold star twinkles out and back in a rolling wave.
2.2s — he hops on one boot with the other leg kicked high and bent, tangled in the trousers, both hands flung forward for balance, and the elf jumps up and down twice, flashing bright green each time.
2.5s — he spins a quarter turn so he is side-on, one hand clapped over his backside, the other pointing away off frame, and the whole picture flashes brighter row by row from the boots upward.
2.8s — he spins back square to camera with both hands slapped over his
```

### Rejected takes

_None recorded. If you rejected a take here, write why on this line._

## C05 — Walkway approach

Forest-green clapboard two-storey with cream trim, a red-nosed reindeer in profile with snowflakes falling around it, fieldstone wall and a straight lit path.

**Status** CLIP · #5 
**Frame** `v25_c05_g1.png` 
**Clip** `v25_c05_g2.mp4` 
**Settings** gpt_image_2 · 2k · medium · 1520×2688 · 9:16 · seedance 2.5 · 1080p · 4s

**References passed**

- @Image 1 · v24 C5 (job) — framing - camera, crop, night street and the scale of the lit curtain.

### Image prompt

```text
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a deep forest-green clapboard two-storey with cream trim, cream window frames and a cream porch rail, instead of the navy-blue one with white trim.

2. A DIFFERENT PICTURE IN THE LIGHTS: a REINDEER with big spreading antlers, warm golden-brown body and a glowing red nose, standing in profile with its head turned to the camera, with white snowflakes falling around it.

3. Different foreground: a low grey fieldstone wall running along the left instead of the white picket fence, and a straight snowy path lined with small warm-white ground lights instead of the curved one.

THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark house wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.

Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.
```

### Video prompt

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same DEEP FOREST-GREEN CLAPBOARD two-storey house with cream trim, cream window frames and a cream porch rail, same low grey fieldstone wall running along the left, same straight shovelled snowy path lined with small warm-white ground lights, same snow-dusted shrubs, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing a big REINDEER with wide spreading antlers, a warm golden-brown body and a glowing red nose, standing in profile with its head turned toward the camera, with white snowflakes falling around it.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the fieldstone wall, the shrubs, the little ground lights and the snow banks at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit reindeer sits inside the curtain rectangle with a wide band of dark unlit wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The reindeer is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark wall between the highest lit point of the artwork — the tips of the antlers — and the top edge of the curtain, and the same clear margin at the bottom and at both sides. No antler tip, no hoof, no tail and no snowflake ever touches or crosses the edge of the curtain, and nothing lit ever appears on the cream trim, the porch, the roof, the sky or the neighbouring houses. If a pose would raise the antlers or widen the body past that margin, THE POSE IS DRAWN SMALLER AND LOWER — the artwork is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: twisting, crouching, leaning, stamping, bucking low, flashing and chasing — never stretching upward, never rearing. It also stays ON THE SPOT and centred; it never walks or slides sideways across the curtain. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail and does not gain size.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. The animation is already ON, already mid-move and already running at full speed in the very first frame — there is NO still opening frame, NO pause, NO switch-on — and it is STILL running hard in the last frame. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST TWO things are changing at once: the reindeer's whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no settle, no gentle drifting. Every pose is a clearly different WHOLE-BODY pose, the figure fully redrawing between beats like an animated light-bulb sign:
0.0s — it lands out of the first frame already mid-move, head dropped low and swung hard to one side so the antlers sweep sideways and DOWN, front knees bent, while the red nose fires to double brightness.
0.3s — it swings the head and antlers hard to the other side, shoulders dipping with it, and every snowflake around it shifts down a row.
0.6s — it lifts one front hoof and paws forward and LOW, chest dropping, ears pricked flat forward, and a bright chase of colour runs down its whole body from head to tail.
0.9s — it drops into a deep crouch on all fours, legs folded, body low and compact, and the red nose pulses three quick beats.
1.2s — it twists its whole body to one side, hind quarters swinging out, tail flicking up short, and every snowflake twinkles out and back in a rolling wave from left to right.
1.5s — it twists hard the other way, the antlers raking sideways across the frame, and the golden-brown body flashes brighter row by row from the hooves upward.
1.8s — it kicks both back legs out behind it in a small low buck, head tucked down between the shoulders, and the snowflakes flash on and off in alternating pairs.
2.1s — it stamps one front hoof down twice fast, head turned square to camera, ears flicking back, and the red nose strobes with each stamp.
2.4s — it shakes its whole head side to side fast, the antlers blurring left-right-left, body held low and square, and a chase of colour runs UP from the hooves to the antler tips.
2.7s — it bows, front legs folded under, chest almost to the ground, antlers angled down and forward, and every snowflake around it swaps colour white to pale blue.
3.0s — it pops back up square, shoulders shimmying left-right-left, and the outline of the whole body flashes brighter one bulb row at a time.
3.3s — it kicks one hind leg out low to the side, the other planted, head swung across its body, and the red nose flares to maximum.
3.6s — it bounces on the spot twice, all four legs compressing and springing, the whole figure squashing and stretching, and the snowflakes twinkle out and back in a rolling wave the other way.
3.9s — it lands square on all four hooves, head turned proudly to camera, antlers spread wide but held level, and the whole picture — body, antlers, nose and every snowflake — flashes to maximum brightness twice in quick succession for the final beat.
E
```

### Rejected takes

_None recorded. If you rejected a take here, write why on this line._

## C06 — Crowd at the garage

Red brick house with a white double garage door, a decorated tree with a gold star and presents in the bulbs, birch at the right and a snowy hedge at the left.

**Status** CLIP · #6 
**Frame** `v25_c06_g1.png` 
**Clip** `v25_c06_g3.mp4` 
**Settings** gpt_image_2 · 2k · medium · 1520×2688 · 9:16 · seedance 2.5 · 1080p · 4s

**References passed**

- @Image 1 · v24 C6 (job) — framing and the crowd of onlookers in silhouette at the bottom.

### Image prompt

```text
Same shot as the attached reference - same camera, same framing, same crowd of onlookers in silhouette at the bottom, same big lit LED curtain filling the garage wall. Change only these things:

1. A DIFFERENT HOUSE: warm red brick with a white double garage door, instead of the grey stucco with the charcoal door.

2. A DIFFERENT PICTURE IN THE LIGHTS: a big decorated CHRISTMAS TREE in green with round red and gold baubles on it and a bright gold star on top, with a few wrapped presents at its base.

3. A tall bare birch tree at the right edge and a snow-covered hedge running along the left edge, instead of the spruces and the pickup truck.

THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark garage wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.

Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.
```

### Video prompt

```text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same WARM RED BRICK house, same WHITE double garage door, same driveway throwing coloured light back, same tall bare birch tree at the right edge and same snow-covered hedge running along the left edge, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing one big decorated CHRISTMAS TREE in green with round red and gold baubles on it, a bright gold star on top and a few wrapped presents at its base.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit tree sits inside the curtain rectangle with a wide band of dark unlit garage door above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The tree is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark door between the highest lit point of the artwork — the tip of the gold star — and the top edge of the curtain, and the same clear margin at the bottom below the presents and at both sides beyond the widest branches. No branch tip, no point of the star, no bauble, no corner of a present and no elf ever touches or crosses the edge of the curtain, and nothing lit ever appears on the red brick, the gables, the roof, the sky, the birch tree or the hedge. If a beat would raise the star or widen the branches past that margin, THE ARTWORK IS DRAWN SMALLER AND LOWER — it is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: leaning, swaying, squashing, twisting, flashing and chasing — never stretching upward. The tree also stays ON THE SPOT and centred; it never slides sideways across the curtain. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

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

THE LIGHT PICTURE IS A LITTLE CARTOON THAT PLAYS OUT, NOT A TREE THAT SITS THERE FLASHING. There are TWO layers of movement running at the same time for the whole four seconds, and BOTH are big, obvious, travelling movements that read clearly even from the bottom of the driveway:
LAYER ONE — THE TREE ITSELF MOVES ITS WHOLE BODY. It is a dancing tree, not a decorated post. It bends, leans, squashes, springs and twists as one solid silhouette, the whole green shape visibly redrawing between beats. Every lean is a BIG lean — the trunk bowing well over to one side, the branch tiers stacking over on themselves, the gold star swinging out sideways over the branches below. Every squash is a BIG squash — the whole silhouette dropping and fanning wide, then springing back. These are not small wobbles: between one beat and the next, the tree's outline is unmistakably a different shape.
LAYER TWO — ELVES WALK IN FROM BOTH SIDES CARRYING PRESENTS. Small chunky ELF figures, lit in bright green and red with pointed hats and curled-toe boots, march IN ALONG THE BOTTOM OF THE CURTAIN from the left edge and from the right edge, each one carrying a wrapped present held out in front of it in both arms. They walk with a big bouncy stomping stride, knees lifting high, hats bobbing with every step — the walk cycle drawn by whole bulbs switching, so they visibly stomp rather than glide. They cross the dark band of unlit door toward the base of the tree, set their present down on the growing pile at its foot, wave both arms over their heads in celebration, and turn and march back out the way they came. A new elf enters roughly every half second, alternating sides, so at any instant there are elves walking in, elves setting down, and elves marching out — the bottom of the picture is never empty and never still, and the pile of presents at the base of the tree GROWS bigger and wider across the four seconds as more are stacked on.
ELF CONTAINMENT: the elves are SMALL — no taller than the bottom tier of branches — and they stay in the BOTTOM BAND of the curtain the whole time. They enter from just INSIDE the left and right edges of the curtain and they walk out to just INSIDE those same edges — they never touch the edge, never cross it, never appear on the brick, the hedge, the birch or the driveway. They stay below the tree's lowest branches at all times and never climb, never jump high, never get in front of the star. The growing present pile spreads SIDEWAYS along the bottom band, never upward into the branches, and it always keeps the clear dark margin below it and at both sides.

THE ANIMATION IS RELENTLESS FROM FRAME ONE. THE BIGGEST MISTAKE WOULD BE A QUIET START. At 0.0s the artwork is already mid-cycle, already loud, already changing, and two elves are already mid-stride inside the frame — the picture does NOT switch on, does NOT hold still, does NOT ease in, and there is NOTHING calm about the first half second. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST THREE things are changing at once: the whole-body shape of the tree, an elf travelling across the bottom band, and a lighting effect somewhere else in the picture. There is no held frame, no pause, no settle:
0.0s — the clip opens mid-action: the tree is already bowed hard over to the LEFT, star swung out sideways, AND one elf is already halfway in from the left edge mid-stomp with a present in its arms while a second elf is just stepping in from the right edge, AND a bright chase of colour is already running down the tree from the star toward the base.
0.3s — the tree springs upright and squashes down wide at the base; the left elf reaches the foot of the tree and sets its present down with a bend of the knees; every red bau
```

### Rejected takes

_None recorded. If you rejected a take here, write why on this line._

## C07 — Drive-by from the car

Out through the car side window, pale grey stone gable with white trim, a full-height waving elf in a green tunic with candy canes around him.

**Status** CLIP · #7 
**Frame** `v25_c07_g1.png` 
**Clip** `v25_c07_g1.mp4` 
**Settings** gpt_image_2 · 2k · medium · 1520×2688 · 9:16 · seedance 2.5 · 1080p · 4s

**References passed**

- @Image 1 · v24 C7 (job) — framing - the car-window POV, the wet road and the gable filled edge to edge.

### Image prompt

```text
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a pale grey stone gable with white trim and white window frames, instead of the white board-and-batten one with black trim.

2. A DIFFERENT PICTURE IN THE LIGHTS: a full-height ELF in a green tunic and green pointed hat with a red belt and curled red-and-white striped shoes, one hand raised in a wave, with small red and white candy canes scattered around him.

3. A different parked car at the kerb - a dark red hatchback instead of the silver estate - and a snow-covered garden bench at the right edge instead of the mailbox.

THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark gable wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.

Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.
```

### Video prompt

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same view shot from inside a moving car through the open passenger side window with the dark window frame framing the bottom-left corner, same wet reflective road throwing long smeared coloured reflections, same snowy verge, same street lamp, same row of neighbouring houses glowing down the street, same DARK RED HATCHBACK parked at the kerb, same snow-covered garden bench at the right edge, same lit LED curtain on the PALE GREY STONE gable wall with white trim showing a full-height ELF in a green tunic and a green pointed hat with a red belt and curled red-and-white striped shoes, one hand raised in a wave, with small red and white candy canes scattered around him.

CAMERA — HANDHELD VERTICAL PHONE VIDEO SHOT OUT OF A MOVING CAR SIDE WINDOW AT NIGHT. THE CAR IS DRIVING FORWARD and closing in on the house, so the gable wall grows steadily and continuously LARGER across the four seconds and NEVER recedes. Real vehicle motion: the road surface and the snow verge flow past the bottom of frame at speed, roadside objects sweep past with strong parallax, the frame rocks gently with the suspension. As the car advances the operator slowly pans right to hold the lit wall in frame. THIS IS DRIVING, NOT ZOOMING: no focal length change, no digital zoom, no gimbal glide, no drone move.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove and no device anywhere in the foreground. Only the car's own dark window frame, exactly as in the reference image, sits at the bottom-left.

MOVEMENT — THE ELF MUST NOT STAND STILL. He stays on the spot the whole four seconds but is never a static standing figure for even one beat. This is the most important instruction in this prompt: a CLEARLY DIFFERENT WHOLE-BODY POSE EVERY HALF SECOND, the figure fully redrawing between beats like an animated light-bulb sign.
0.0-0.5s — his raised hand swings down and across his body while the other arm comes up instead, the long point of his green hat whipping over to the opposite side.
0.5-1.0s — he bends both knees deep and hops on the spot, both arms straight out sideways, his curled striped shoes kicking up, the red belt flashing brighter.
1.0-1.5s — he lands and leans hard to one side, one leg kicked straight out, both hands on his hips and his grin stretched wide.
1.5-2.0s — he spins on the spot with his arms tucked in tight, the green tunic flaring out, and the candy canes around him swap over and change colour as he turns.
2.0-2.5s — he drops into a low crouch, both hands on the ground in front of him, the point of his hat hanging forward past his face.
2.5-3.0s — he springs straight back up and throws both arms over his head, and every candy cane around him twinkles out and back in a rolling wave from left to right.
3.0-3.5s — he kicks one striped shoe high in front of him, one arm windmilling to keep his balance, eyes wide and mouth round.
3.5-4.0s — he plants both shoes, straightens up tall and throws both arms out wide in a big proud finishing pose, the hat bobbing and the whole green tunic flashing brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. The coloured reflections on the wet road shift and streak with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the pale grey stone gable wall". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the wall behind it: its stone courses, its white trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No shoe, no arm, no point of his hat and no candy cane ever crosses the roof edge or the corner of the wall — his raised arms and his kicking legs always keep a clear margin of dark wall inside the rectangle. He also never walks sideways across the curtain; he stays ON THE SPOT and stays centred. Nothing spills onto the roof, the white trim, the sky, the verge, the parked dark red hatchback or the neighbouring houses. As the car gets closer the bulb grid simply becomes coarser and the individual bulbs bigger and more countable — the artwork does not gain detail.

HARD RULES: no people and no other vehicles enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Tyres on wet road, a low engine hum, cold air rushing past the open window, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night from a car. Noisy shadows, blown highlights around the bulbs, slight rolling-shutter wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
```

### Rejected takes

_None recorded. If you rejected a take here, write why on this line._

---

## Frame generation log (from `image_prompts.md`)


Same six shots as v20 – v24. Clip numbering kept (clip_2 … clip_7) — **C1 / the hook is skipped**.
Changed vs. v24: the woman, the install house, the showcase houses, the backgrounds, the lit artwork.
One generation per shot.

Model `gpt_image_2` · `resolution: "2k"` · `quality: "medium"` · `aspect_ratio: "9:16"` · `use_unlim: false` · output 1520×2688
Workspace: **Oneofone1**

---

#### The v25 look

**Woman** — early-thirties East Asian woman, fair warm-toned skin, straight black hair to the shoulder blades with a blunt fringe.
Indoors: cream cable-knit jumper + light-wash jeans. Outdoors: deep teal parka with faux-fur hood trim + grey jeans + brown boots.

**Living room (C2)** — warm walnut floor, charcoal-grey linen sofa, cream and rust cushions, chunky cream knit throw, sage-green painted wall, brass arc floor lamp, real green tree with multicolour lights and gold baubles at the right.

**Install wall (C3 / C4)** — warm cream stucco, dark bronze gutter / fascia / downpipe, low dark-stained wooden fence at the right, bare white birch beyond the left corner, red-brick neighbour house at the right edge. C3 day, C4 the same wall at night.

**Showcase houses** — C5 deep forest-green clapboard two-storey with cream trim · C6 warm red brick with a white double garage door · C7 pale grey stone gable with white trim.

**Lit artwork** — C5 reindeer with big antlers and a red nose, falling snowflakes · C6 decorated green Christmas tree with red and gold baubles, gold star, presents at the base · C7 full-height elf in a green tunic and pointed hat waving, candy canes scattered around.

---

#### References used

| Ref | Owns | media / job |
|---|---|---|
| `video_20_assets/clip_2/starting_frames/v20_c02_g1.png` | **C2 geometry** — sofa in front of her | `05989e1b-228c-432a-be58-a51cfbfa19ad` |
| v24 C2 job | C2 camera height (shoulder height) | `22ca36a7-739f-42f9-ad11-a81c09882666` |
| v24 C3 g3 job | C3 flat frontal framing **+ black wire** | `fa0d894f-68c0-4335-a769-b02161a6be90` |
| v24 C4 g3 job | C4 dead-on framing + mounted black curtain + lit app screen | `b22ec2ca-0015-4769-8227-98d4ddee5813` |
| v24 C5 job | C5 framing | `2636adf4-aa20-49e0-91f0-5071fcd803e0` |
| v24 C6 job | C6 framing | `d1f5ffc7-609c-4403-a131-14555bc9639b` |
| v24 C7 job | C7 framing | `862a6e66-770c-4033-b92b-676d15c2ad48` |

The v24 g3 frames are used for C3/C4 rather than the older v23 ones because they are the first in the series with the **black** wire and the corrected flat frontal camera. Never point C3/C4 at a v20–v23 install frame — those all have white wire.

#### Continuity chain

`C2 job → C3` (locks the woman) · `C3 job → C4` (locks the house, now at night)

---

#### C2 — box over the sofa

Refs: **1 = v20_c02_g1** (geometry) · **2 = v24 C2** (camera height only)

> Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.
>
> THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.
>
> She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. Wood floor visible at the bottom left.
>
> CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.
>
> A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: an early-thirties East Asian woman with fair warm-toned skin and straight black hair falling to her shoulder blades with a blunt fringe, wearing a cream cable-knit jumper and light-wash jeans. The room has a warm walnut floor, a charcoal-grey linen sofa with cream and rust cushions and a chunky cream knit throw, a sage-green painted wall, a brass arc floor lamp, and a real green Christmas tree with multicolour lights and gold baubles at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.
>
> Real iPhone photo, tack-sharp, candid UGC, no text overlay, no watermark.

#### C3 — mounting the curtain, day

Refs: **1 = v24 C3 g3** (framing + black wire) · **2 = v25 C2 job** (the woman)

> Same shot as the FIRST attached image - copy its camera, framing and staging EXACTLY. Daytime, overcast winter light, snow on the ground. A woman stands on a black folding step stool, seen from BEHIND, facing the house wall, both arms raised in front of her at the top of the wall, her hands up near the gutter line as she fixes the LED curtain to it. The big bundle of unlit LED curtain strands is heaped on the snow at the foot of the stool.
>
> THE CAMERA ANGLE IS FLAT AND FRONTAL, exactly as in the first image: the wall faces the camera almost square-on and fills the frame, the vertical lines of the siding run straight up and down. The wall is NOT turned away at an angle, NOT receding steeply into the distance, NO strong oblique perspective, NO wide-angle corner view.
>
> THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand hanging down the wall is a thin BLACK cord with small DARK unlit bulbs on it. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.
>
> THE WOMAN - take her from the SECOND attached image: the same early-thirties East Asian woman with fair warm-toned skin and straight black shoulder-blade-length hair with a blunt fringe. Outdoors she wears a deep teal parka with a faux-fur hood trim, grey jeans and brown boots.
>
> A COMPLETELY NEW HOUSE AND BACKGROUND - take these from this text only, NOT from the first attached image: the wall she is working on is WARM CREAM STUCCO with a dark bronze gutter, dark bronze fascia and a dark bronze downpipe running down the right side. A low dark-stained wooden fence runs along the right of the frame. A bare white birch tree stands beyond the left corner of the house. A red-brick neighbour house is visible at the far right edge. Do NOT copy the slate-blue board-and-batten siding, the white trim, the brick garden wall or the hedge from the first image.
>
> Real iPhone photo, tack-sharp, candid UGC, no text overlay, no watermark.

#### C4 — same wall at night, phone app

Refs: **1 = v24 C4 g3** (framing + mounted black curtain + lit app screen) · **2 = v25 C3 job** (the house)

> Same shot as the FIRST attached image - copy its camera, framing and staging EXACTLY. Night.
>
> THE CAMERA ANGLE IS DEAD-ON SQUARE TO THE WALL, exactly as in the first image: the wall faces the camera flat and fills the frame, its vertical lines run straight up and down. The wall is NOT turned away at an angle, NOT receding into the distance, NO strong oblique perspective, NO corner view.
>
> TWO THINGS THAT MUST BE PRESENT, exactly as in the first image - do not omit either:
> 1. The LED CURTAIN IS ALREADY MOUNTED ON THE WALL, hanging in evenly spaced vertical see-through strands from the gutter line down across the wall, with slight natural sag and an uneven bottom hem.
> 2. At the BOTTOM CENTRE of the frame, a hand holds a smartphone up toward the wall, screen facing the camera and BRIGHTLY LIT, showing a real phone app UI: a dark blue app screen with a grid of small square scene thumbnails and a large round play button - the screen glows and lights the hand.
>
> THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand is a thin BLACK cord with small DARK unlit bulbs on it, no glow. The strands still read clearly as thin dark vertical lines against the wall, caught by the street lamp from the left and the porch light from the right so they stay visible, not invisible. No white wire, no clear wire, no silver wire anywhere.
>
> THE HOUSE - take it from the SECOND attached image: the SAME wall, the same WARM CREAM STUCCO, the same dark bronze gutter, dark bronze fascia and dark bronze downpipe on the right, the same low dark-stained wooden fence at the right, the same bare white birch tree beyond the left corner, the same red-brick neighbour house at the far right edge. It must read as literally the same house, now at night.
>
> Lighting: a street lamp glow from the left and a warm porch light from the right, snow on the ground catching the light. Real iPhone night photo, tack-sharp, candid UGC, no text overlay, no watermark.

#### C5 — lit facade, reindeer

Ref: **v24 C5**

> Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:
>
> 1. A DIFFERENT HOUSE: a deep forest-green clapboard two-storey with cream trim, cream window frames and a cream porch rail, instead of the navy-blue one with white trim.
>
> 2. A DIFFERENT PICTURE IN THE LIGHTS: a REINDEER with big spreading antlers, warm golden-brown body and a glowing red nose, standing in profile with its head turned to the camera, with white snowflakes falling around it.
>
> 3. Different foreground: a low grey fieldstone wall running along the left instead of the white picket fence, and a straight snowy path lined with small warm-white ground lights instead of the curved one.
>
> THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark house wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.
>
> Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.

#### C6 — garage door + crowd, Christmas tree

Ref: **v24 C6**

> Same shot as the attached reference - same camera, same framing, same crowd of onlookers in silhouette at the bottom, same big lit LED curtain filling the garage wall. Change only these things:
>
> 1. A DIFFERENT HOUSE: warm red brick with a white double garage door, instead of the grey stucco with the charcoal door.
>
> 2. A DIFFERENT PICTURE IN THE LIGHTS: a big decorated CHRISTMAS TREE in green with round red and gold baubles on it and a bright gold star on top, with a few wrapped presents at its base.
>
> 3. A tall bare birch tree at the right edge and a snow-covered hedge running along the left edge, instead of the spruces and the pickup truck.
>
> THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark garage wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.
>
> Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.

#### C7 — car-window POV, elf on the gable

Ref: **v24 C7**

> Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:
>
> 1. A DIFFERENT HOUSE: a pale grey stone gable with white trim and white window frames, instead of the white board-and-batten one with black trim.
>
> 2. A DIFFERENT PICTURE IN THE LIGHTS: a full-height ELF in a green tunic and green pointed hat with a red belt and curled red-and-white striped shoes, one hand raised in a wave, with small red and white candy canes scattered around him.
>
> 3. A different parked car at the kerb - a dark red hatchback instead of the silver estate - and a snow-covered garden bench at the right edge instead of the mailbox.
>
> THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark gable wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.
>
> Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.

---

#### Generated set

| Shot | File | index | job_id |
|---|---|---|---|
| C2 | `clip_2/starting_frames/v25_c02_g1.png` | 250201 | `b02d8e1d-3688-4df4-8d86-3e77f092bfee` |
| C3 | `clip_3/starting_frames/v25_c03_g1.png` | 250301 | `f21c1741-d9db-4fae-98f8-1bfd2861a089` |
| C4 | `clip_4/starting_frames/v25_c04_g1.png` | 250401 | `2d686989-64a6-4bce-b0b9-728bf6c0f07a` |
| C5 | `clip_5/starting_frames/v25_c05_g1.png` | 250501 | `f21070fe-78e7-492b-a6fb-4f54af191c0b` |
| C6 | `clip_6/starting_frames/v25_c06_g1.png` | 250601 | `e1721c55-2092-4ba2-ad2e-171f98333bf2` |
| C7 | `clip_7/starting_frames/v25_c07_g1.png` | 250701 | `d76217c3-1d6a-4c92-9d4a-ff7378c7e496` |

#### Notes on this set

- C3 and C4 are the literally same cream stucco wall with dark bronze trim, flat frontal camera, **black** strands — day then night. Chaining off the v24 g3 frames carried both corrections through first time.
- C5 / C6 / C7 all read as see-through strands over a dark wall, not an LED panel.
- **C2 to check**: the sofa is in front of her and the camera height is right, but the frame sits slightly tighter than v24 and the tree is further right — the box and the empty seat cushions still read clearly.
- **C4 to check**: the hand holding the phone is lighter-skinned than usual for a UGC shot but consistent with the v24 frame it was built from.

---

#### C1 — hook (added 2026-09-14)

`clip_1/starting_frames/v25_c01_g1.png` · job `8ff914fc-b7c2-4011-aab8-60a68671f5f9` · gpt_image_2 · 2k · medium · 9:16
Reference: Daniel's "Christmas Decor in 1965" screenshot (media `e65739f1-8f6b-4a44-a02f-51c3e6884026`),
attached for ONE thing only — wide silver duct-tape bands spiralling down the tree with figures taped
flat onto the branches. Its room, staircase, ladder and woman explicitly excluded.

Brief: night living room, ugly tree wrapped in spiralling duct tape with deflated inflatable Santa /
snowman / reindeer / penguin taped to it, cords trailing to an orange extension lead. Man stands in the
left foreground, three-quarters rear view, cut by the left edge, feet flat, fists clenched, jaw set —
deliberately the STILL moment BEFORE the kick, since the kick happens in the video.

##### C1 g2 — `v25_c01_g1` revision

`clip_1/starting_frames/v25_c01_g1.png` · job `4c43a835-efbf-42b7-a636-5595f9c73bca` · chained off the g1 job
One change only: a slightly lower tilt so there is ~1/10 frame of clean empty ceiling above the star for
the caption. Explicit negatives against zooming out or shrinking the tree and the man.

---

#### C1 VIDEO — v25_c01_g1.mp4 (2026-09-14)

- Job: `78400d24-c63e-499d-a7f5-eb1d2a9d0124`
- Model `seedance_2_5`, `mode omni_reference`, 720p, 9:16, 5s, audio on, `declined_preset_id 24bae836-2c4a-48e0-89b6-49fcc0b21612`
- Start frame: `clip_1/starting_frames/v25_c01_g1.png` (job `4c43a835-efbf-42b7-a636-5595f9c73bca`) as `start_image`
- Output: `clip_1/clips/v25_c01_g1.mp4` — 720x1280, 5.04s, audio present

Brief from Daniel: held iPhone, no zooms. Man very angry and pissed off, yelling; he kicks the Christmas
tree hard with his foot and the tree falls.

Same prompt skeleton as V24 (locked-handheld CAMERA block, timed TIMELINE bands, AUDIO block, realism tail,
no-operator-visible negative). Shouted line verbatim: "I'M DONE WITH THIS! DONE!". Written dry — natural
room sound only, no music, no score (Daniel adds music in CapCut).

---

## Clip generation log (from `clip_jobs.md`)


Model `seedance_2_5` · `mode: "omni_reference"` · `resolution: "1080p"` · `aspect_ratio: "9:16"` · `generate_audio: true` · `use_unlim: false` · `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`
Output 1080×1920. Workspace: **Oneofone1**. Generated 2026-09-14.

One generation per shot. Prompts live in `video_prompts/v25_cNN.txt`.

---

| Shot | Duration | Start frame | Prompt | Job id | Result |
|---|---|---|---|---|---|
| C2 — box over the sofa | 5.05s | `v25_c02_g1.png` | `v25_c02.txt` | `78e0e105-1751-482c-8e4d-6afc2b34950a` | `clip_2/clips/v25_c02_g1.mp4` |
| C3 — pinning the curtain up | 4.05s | `v25_c03_g1.png` | `v25_c03.txt` | `9336af2d-a452-4c74-877b-34c7db8e1c56` | `clip_3/clips/v25_c03_g1.mp4` |
| C4 — phone POV, wall dead-on | 4.05s | `v25_c04_g1.png` | `v25_c04.txt` | `ebfb9906-113a-41c6-8c80-cff682dadd4b` | `clip_4/clips/v25_c04_g1.mp4` |
| C5 — walkway approach | 4.05s | `v25_c05_g1.png` | `v25_c05.txt` | `0ec6ab46-21f4-4999-bb83-dc92b25faabe` | `clip_5/clips/v25_c05_g1.mp4` |
| C6 — crowd at the garage | 4.05s | `v25_c06_g1.png` | `v25_c06.txt` | `3cd7fadc-0af5-4b81-85cb-e488515adc03` | `clip_6/clips/v25_c06_g1.mp4` |
| C7 — drive-by from the car | 4.05s | `v25_c07_g1.png` | `v25_c07.txt` | `ca957a4d-0727-4c53-9830-5cfa3ca3db01` | `clip_7/clips/v25_c07_g1.mp4` |

Board copies of all six clips are mirrored to `all_clips/v25_cNN.mp4`.

All six submitted in one `generate_video_batch` call, all six completed first time. No refusals.

---

#### Reference media passed

Every shot passed its own start frame as `medias[]` role `start_image`.

C2 additionally carried two product references, this time submitted with role `image_references`
directly rather than `image` — the submission came back clean with **no `adjustments` coercion block**,
confirming `image_references` is the correct schema key for this model:

- `ffaa8801-8e71-43f0-ae24-461104cf30f2` — closed box packshot (`product_images/box_nowindow/box_nowindow_g5.png`)
- `f01fecfe-9cbe-44a5-a617-63193a1108b0` — open box interior (`product_images/box_nowindow/box_interior_g5.png`)

---

#### Start-frame media ids

| Frame | Media id |
|---|---|
| `v25_c02_g1.png` | `0f36ae95-10dc-481c-bb3b-6f37a5e8a425` |
| `v25_c03_g1.png` | `71244106-f4cd-45d5-9186-cd7f19d1e0c1` |
| `v25_c04_g1.png` | `e69045a5-1251-48f2-8f98-e5a645e7170d` |
| `v25_c05_g1.png` | `1de11ee7-7fc1-45da-93bd-8a7c1bbe8686` |
| `v25_c06_g1.png` | `08a7266c-db88-43f4-9fdf-c0e113c88607` |
| `v25_c07_g1.png` | `88972a61-8191-49a8-963d-f5b102126df8` |

---

#### C4 timeline — rebalanced

The v24 C4 clip put the scroll and the tap in the front 1.6s and left the lit artwork barely over a second,
so the animation read as if it only started in the last beat. The v25 C4 prompt splits the clip in half
instead: **one short flick of the scene grid** (roughly one row, not a long scroll), tap at 1.5–1.8s,
wall snaps on at 1.8s, hand out of frame by 2.0s, and then a **full two seconds** of the lit wall animating
with five pose beats at 2.2 / 2.6 / 3.0 / 3.4 / 3.8s. Same structure in `v26_c04.txt`, and `v24_c04.txt`
was rewritten to match and regenerated.

C4's snap-on artwork always matches the C5 artwork for the same ad, so the viewer sees the scene they
picked in the app light up and then sees it again on the walk-up. For v25 that artwork is the **reindeer**.

---

#### C5 and C6 redo — the artwork was inflating inside the curtain

Daniel: *"C5 — the animation gets out of the frame of where the lights are placed, when the reindeer is moving
it's breaking the house frame. C6 — also gets out of the frame a little and the animation is extremely boring
with very few movement and nothing happens in the animation in the beginning of the clip."*

Pulling frame 0 and frame 60 out of `v25_c05_g1.mp4` showed the actual mechanism: **the curtain rectangle is not
growing — the figure inside it is scaling up.** At frame 0 the reindeer sits well inside the rectangle; by frame 60
the antlers touch and cross the top edge. The old wording (*"the animation stays inside the curtain"*) constrained
the rectangle, not the figure, which is why it never held.

The replacement block locks **size**, not position:

> THE ARTWORK NEVER CHANGES SIZE… the same number of bulbs tall and the same number of bulbs wide in the final
> frame as in the first frame… ALWAYS a clear band of at least six unlit bulb rows between the highest lit point
> and the top edge… If a pose would raise the antlers past that margin, THE POSE IS DRAWN SMALLER AND LOWER.

And because containment and "more motion" pull against each other, the prompt resolves it explicitly:
*"BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS."* Every rearing,
antlers-high or arms-overhead pose was rewritten as a low, wide or squashing one.

The "boring" complaint traced to the same structural cause on every clip: eight beats at 0.5s with a single layer
moving. Both prompts now run **fourteen beats at 0.3s with two layers moving at once** — the figure's whole-body
pose AND a lighting effect somewhere else in the picture. For C6 the first beat is written as an explicitly loud
one (*"THE BIGGEST MISTAKE WOULD BE A QUIET START… the clip opens mid-flash"*) to answer the "nothing happens at
the beginning" note.

| take | job |
| --- | --- |
| `v25_c05_g2.mp4` | `9d77ce32-705a-480a-82d4-7d1fc673d6ce` |
| `v25_c06_g2.mp4` | `2f582714-bba6-4b2c-afeb-2d0ea091e481` |

Original takes kept alongside as `_g1.mp4`.

---

#### C4 and C6 redo — the approved sync structure, and motion that travels

Daniel: *"C4 for video 24 came out good in terms of syncing, do the same for video 25 and 26, but for video 25
and 26 I want much better animations with a lot more motion and more interesting. C6 — there is almost no motion
in the animation, try something like the christmas tree moving and some elves coming from the sides with more
presents."*

**C4** was rebuilt on `v24_c04.txt`, which Daniel signed off on, keeping its sync block verbatim — the press and
the light are ONE event, and the hand drops out of frame immediately rather than lingering. The phone is finished
and gone by 1.3s so roughly three of the four seconds are the lit wall alone, and the artwork gets a ten-beat
timeline instead of the old sparse one. Artwork stays the **reindeer**, matching C5.

**C6** needed a different fix. The previous round already went to fourteen beats at 0.3s and Daniel still read it
as motionless — because in a wide crowd shot the artwork is small in frame, so pose flicker *inside* it doesn't
register at that viewing distance. Subdividing time further was never going to work. What reads at distance is
something that **travels across the picture**, so the prompt now runs two layers:

> LAYER ONE — THE TREE ITSELF MOVES ITS WHOLE BODY. It is a dancing tree, not a decorated post… between one beat
> and the next, the tree's outline is unmistakably a different shape.
> LAYER TWO — ELVES WALK IN FROM BOTH SIDES CARRYING PRESENTS… A new elf enters roughly every half second,
> alternating sides… and the pile of presents at the base of the tree GROWS bigger and wider across the four seconds.

An ELF CONTAINMENT paragraph keeps them no taller than the bottom tier of branches, inside the curtain edges and
out of the main artwork's band, so the new layer can't reintroduce the frame-breaking problem. Every beat now
changes **at least three things at once**.

| take | job |
| --- | --- |
| `v25_c04_g2.mp4` | `5b87bddc-fa90-41c8-9745-aa19de930aa9` |
| `v25_c06_g3.mp4` | `a0472685-6417-4a3e-af15-466d0f77b18b` |

Earlier takes kept alongside.

#### C4 take 3 — Santa loses his trousers

Daniel: *"C4 from video 25 — you need to remake it, that animation is completly trash and at first the raindeer
looks too realistic. It must be something funny, controversial, something with santa I want."*

Checked against a contact sheet of `v25_c04_g2.mp4` first: the stag rendered **photoreal**, the pose barely
changed between beats, and the artwork **inflated and then shrank**. Three fixes, and nothing else touched — the
camera, sync, phone-timing and 0.0–1.0s blocks Daniel already signed off on are carried over verbatim.

1. **An anti-realism paragraph placed before the timeline**, so it is read before the subject is described —
   flat cartoon light art built out of individual bulbs, like a chunky neon shop sign; *not* a photograph, not
   3D, not shaded, not furry, not lifelike. *"Think cheap funny Christmas light display, not fine art."*
2. **A subject that cannot render photoreal.** Santa's belt pops, his red trousers drop round his boots and he
   is left in enormous candy-striped long underpants with little white hearts, beard flying, sack tipped over,
   while a green elf at the bottom left doubles over laughing and points at him.
3. **Nine whole-body beats at 0.3s**, each pairing a pose change with a lighting effect, plus the explicit rule
   *"If two consecutive beats look similar, it is wrong."*

The size-lock paragraph was also found **truncated mid-word** in the old prompt file (it stopped at "never
inflates, ne"), which plausibly explains the inflation bug it was supposed to prevent. It is now complete.

| take | job |
| --- | --- |
| `v25_c04_g3.mp4` | `840228cd-c35

---

## Prompt-file versions not on the board

These are the prompts as they sit in `video_prompts/`. Where a shot above shows a different text, this is a different pass at the same shot - usually a later rewrite - so both are kept.

### `v25_c04.txt`

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same WARM CREAM STUCCO wall of the house seen dead-on and flat, filling the frame, with the UNLIT LED curtain hanging in thin black vertical strands across it, same dark bronze gutter along the top and dark bronze downpipe at the right, same dark-stained wooden fence at the right, same snow in the foreground, same hand coming up from the bottom holding a phone up in the lower part of frame, same app screen showing a dark blue grid of small colourful scene tiles with a BIG ROUND BLUE PLAY BUTTON at the bottom of the screen.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, handheld micro-shake only. The camera stays DEAD-ON SQUARE to the wall the whole four seconds — it never swings round to an oblique angle, never turns to a corner view, never tilts up. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY. The wall and the phone stay exactly the same size in frame throughout.

THE SINGLE MOST IMPORTANT THING IN THIS CLIP IS THE SYNC. The thumb presses the big round PLAY button, and ON THAT VERY SAME FRAME the wall lights up. Not a frame early, not a frame late, no gap, no delay, no anticipation, no lag. The press and the light are ONE event. And the instant the button is pressed the hand immediately drops away out of the bottom of frame — it does not linger, does not hold the phone up to admire the wall, does not stay in shot for even half a second after the press.

THE PHONE PART IS SHORT. THE LIT PART IS MOST OF THE CLIP. The phone is finished and gone by 1.3s. From 1.3s to the very last frame — nearly THREE FULL SECONDS — there is nothing in the foreground and the wall is lit and animating hard. The animation must NOT be squeezed into the last second and must NOT be a slow, sparse, gentle thing.

HOW THE PICTURE IN THE LIGHTS IS DRAWN — READ THIS BEFORE ANYTHING ELSE. It is FLAT CARTOON LIGHT ART built out of individual glowing bulbs, like a chunky neon shop sign or a big pixel sprite. Thick simple outlines, flat blocks of colour, big silly cartoon face. It is NOT a photograph. It is NOT a realistic person or animal. It is NOT 3D, NOT rendered, NOT shaded, NOT textured, NOT furry, NOT lifelike, and NOT a video projected onto the wall. If it could be mistaken for a photo of something real, it is wrong. Think cheap funny Christmas light display, not fine art.

ACTION TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.8s — A SHORT SCROLL, NOT A LONG ONE. The thumb comes in from the bottom and gives the grid of scene tiles ONE small flick: the tiles slide up by roughly ONE ROW only, a single fresh row of new scene thumbnails comes into view from the bottom, the list overshoots slightly and settles back with a small bounce. That is the entire scroll. NO long scroll, NO repeated flicks, NO second flick, NO rows racing past, NO scrolling through the whole list. One tile in the grid keeps its bright highlight ring the whole time — the scene is already chosen.
0.8-1.0s — the thumb slides straight down to the BIG ROUND BLUE PLAY BUTTON at the bottom of the app screen and comes to rest on it.
1.0s — THE THUMB PRESSES PLAY. On that exact frame the button visibly depresses and flashes, AND the entire wall SNAPS ON at full brightness in the very same single frame. NO fade, NO dissolve, NO ramp, NO brightness curve, NO bulbs lighting one by one, NO sweep across the wall, NO pause between the press and the light. One frame dark, the next frame fully lit at maximum brightness.

THE ARTWORK THAT APPEARS — SANTA LOSES HIS TROUSERS. One full-height cartoon SANTA drawn in bulbs, standing facing the camera in the middle of the lit area. His broad black belt has POPPED OPEN and swings loose, and his big red trousers have dropped straight down and are bunched around his black boots. Underneath he is wearing enormous baggy long underpants in red and white candy stripes with little white hearts on them. Both his white-gloved hands grab at the fallen waistband, his eyes are two huge white circles, his mouth is a big round O, his cheeks are two bright pink dots and his white beard is flying sideways. His red sack has been dropped and lies tipped over at his feet with a couple of coloured presents rolling out. Down at the bottom left a small GREEN ELF is doubled over laughing, pointing straight up at him with one arm, hat flopping. Colours: bright red, white, black, green, pink and gold. A ring of gold stars pops around Santa's head.

1.0-1.3s — the hand drops straight down and out of the bottom of frame fast and NEVER returns. The phone, the hand, the fingers and the sleeve are completely gone from frame by 1.3s and no part of them reappears at any point.
1.3-4.0s — THE REST OF THE CLIP IS THE LIT WALL ALONE, and it is relentless. See the movement block below.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. From the moment the wall snaps on, SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least NINE separate changes between 1.3s and the last frame — and at every single instant AT LEAST TWO things are changing at once: Santa's whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no pause, no settle, no gentle drifting. Every beat is a clearly DIFFERENT WHOLE-BODY pose — arms, legs, head and body all in a new position — the figure fully redrawing between beats like an animated light-bulb sign. If two consecutive beats look similar, it is wrong.
1.3s — it lands out of the snap-on already mid-move: Santa bent forward at the waist, both hands snatching down at the fallen trousers, knees knocked together, while the gold stars around his head flash on and the elf's laughing mouth flips wide open.
1.6s — he hauls the trousers UP to his knees with both arms straight up above his head from the effort, chest thrown out, and a bright chase of colour runs across the candy stripes of his underpants from left to right.
1.9s — the trousers drop straight back down to his boots, Santa's arms fly out wide to both sides in a huge shrug, head thrown back, and every gold star twinkles out and back in a rolling wave.
2.2s — he hops on one boot with the other leg kicked high and bent, tangled in the trousers, both hands flung forward for balance, and the elf jumps up and down twice, flashing bright green each time.
2.5s — he spins a quarter turn so he is side-on, one hand clapped over his backside, the other pointing away off frame, and the whole picture flashes brighter row by row from the boots upward.
2.8s — he spins back square to camera with both hands slapped over his face in shame, fingers spread, legs crossed tight, and the stripes on the underpants flash alternately red and white.
3.1s — he crouches right down to grab the trousers with both hands, bottom out behind him, beard hanging forward past his knees, and a chase of colour runs UP from the boots to the tip of his hat.
3.4s — he springs upright with both fists punched high in triumph, trousers finally at his waist, one leg kicked out to the side, and the gold stars strobe with the punch.
3.7s — the belt pops open again and the trousers drop for the last time, Santa's head snapping down to look at them, shoulders hunched, hands out flat in disbelief, while the elf rolls over backwards laughing and the presents on the ground flash colour.
3.9s — he turns square to camera and throws both arms out wide in a big shameless shrug with a huge grin, trousers still round his boots, and the whole picture — Santa, the underpants, the elf, the presents and every gold star — flashes to maximum brightness twice in quick succession for the final beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade, never a realistic animation curve. Coloured light spills and shifts across the snow below with every change.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. When the wall snaps on, the lit picture sits inside the curtain rectangle with a wide band of dark unlit wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from 1.0s to the last frame. Santa is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the frame he first appears. He NEVER scales up, never grows, never inflates, never creeps outward and never drifts across the wall. The dark unlit band around the picture is the same width in every single frame. Nothing lit ever spreads onto the stucco outside the curtain, onto the gutter, onto the fence or into the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights or anywhere in the frame.

THE CURTAIN — CRITICAL: it stays a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the cream stucco wall behind is plainly visible through those gaps, especially in the unlit band around the picture. The bulbs are small round points of light strung along thin cords.

Real iPhone night video, handheld, tack-sharp, candid UGC. No text overlay, no watermark, no captions, no logo.
```

### `v25_c05.txt`

```text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same DEEP FOREST-GREEN CLAPBOARD two-storey house with cream trim, cream window frames and a cream porch rail, same low grey fieldstone wall running along the left, same straight shovelled snowy path lined with small warm-white ground lights, same snow-dusted shrubs, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing a big REINDEER with wide spreading antlers, a warm golden-brown body and a glowing red nose, standing in profile with its head turned toward the camera, with white snowflakes falling around it.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the fieldstone wall, the shrubs, the little ground lights and the snow banks at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit reindeer sits inside the curtain rectangle with a wide band of dark unlit wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The reindeer is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark wall between the highest lit point of the artwork — the tips of the antlers — and the top edge of the curtain, and the same clear margin at the bottom and at both sides. No antler tip, no hoof, no tail and no snowflake ever touches or crosses the edge of the curtain, and nothing lit ever appears on the cream trim, the porch, the roof, the sky or the neighbouring houses. If a pose would raise the antlers or widen the body past that margin, THE POSE IS DRAWN SMALLER AND LOWER — the artwork is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: twisting, crouching, leaning, stamping, bucking low, flashing and chasing — never stretching upward, never rearing. It also stays ON THE SPOT and centred; it never walks or slides sideways across the curtain. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail and does not gain size.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. The animation is already ON, already mid-move and already running at full speed in the very first frame — there is NO still opening frame, NO pause, NO switch-on — and it is STILL running hard in the last frame. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST TWO things are changing at once: the reindeer's whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no settle, no gentle drifting. Every pose is a clearly different WHOLE-BODY pose, the figure fully redrawing between beats like an animated light-bulb sign:
0.0s — it lands out of the first frame already mid-move, head dropped low and swung hard to one side so the antlers sweep sideways and DOWN, front knees bent, while the red nose fires to double brightness.
0.3s — it swings the head and antlers hard to the other side, shoulders dipping with it, and every snowflake around it shifts down a row.
0.6s — it lifts one front hoof and paws forward and LOW, chest dropping, ears pricked flat forward, and a bright chase of colour runs down its whole body from head to tail.
0.9s — it drops into a deep crouch on all fours, legs folded, body low and compact, and the red nose pulses three quick beats.
1.2s — it twists its whole body to one side, hind quarters swinging out, tail flicking up short, and every snowflake twinkles out and back in a rolling wave from left to right.
1.5s — it twists hard the other way, the antlers raking sideways across the frame, and the golden-brown body flashes brighter row by row from the hooves upward.
1.8s — it kicks both back legs out behind it in a small low buck, head tucked down between the shoulders, and the snowflakes flash on and off in alternating pairs.
2.1s — it stamps one front hoof down twice fast, head turned square to camera, ears flicking back, and the red nose strobes with each stamp.
2.4s — it shakes its whole head side to side fast, the antlers blurring left-right-left, body held low and square, and a chase of colour runs UP from the hooves to the antler tips.
2.7s — it bows, front legs folded under, chest almost to the ground, antlers angled down and forward, and every snowflake around it swaps colour white to pale blue.
3.0s — it pops back up square, shoulders shimmying left-right-left, and the outline of the whole body flashes brighter one bulb row at a time.
3.3s — it kicks one hind leg out low to the side, the other planted, head swung across its body, and the red nose flares to maximum.
3.6s — it bounces on the spot twice, all four legs compressing and springing, the whole figure squashing and stretching, and the snowflakes twinkle out and back in a rolling wave the other way.
3.9s — it lands square on all four hooves, head turned proudly to camera, antlers spread wide but held level, and the whole picture — body, antlers, nose and every snowflake — flashes to maximum brightness twice in quick succession for the final beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. Coloured light spills and shifts across the snow below with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the front facade wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

HARD RULES: no people, no cars, no pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
```

### `v25_c06.txt`

```text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same WARM RED BRICK house, same WHITE double garage door, same driveway throwing coloured light back, same tall bare birch tree at the right edge and same snow-covered hedge running along the left edge, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing one big decorated CHRISTMAS TREE in green with round red and gold baubles on it, a bright gold star on top and a few wrapped presents at its base.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit tree sits inside the curtain rectangle with a wide band of dark unlit garage door above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The tree is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark door between the highest lit point of the artwork — the tip of the gold star — and the top edge of the curtain, and the same clear margin at the bottom below the presents and at both sides beyond the widest branches. No branch tip, no point of the star, no bauble, no corner of a present and no elf ever touches or crosses the edge of the curtain, and nothing lit ever appears on the red brick, the gables, the roof, the sky, the birch tree or the hedge. If a beat would raise the star or widen the branches past that margin, THE ARTWORK IS DRAWN SMALLER AND LOWER — it is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: leaning, swaying, squashing, twisting, flashing and chasing — never stretching upward. The tree also stays ON THE SPOT and centred; it never slides sideways across the curtain. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

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

THE LIGHT PICTURE IS A LITTLE CARTOON THAT PLAYS OUT, NOT A TREE THAT SITS THERE FLASHING. There are TWO layers of movement running at the same time for the whole four seconds, and BOTH are big, obvious, travelling movements that read clearly even from the bottom of the driveway:
LAYER ONE — THE TREE ITSELF MOVES ITS WHOLE BODY. It is a dancing tree, not a decorated post. It bends, leans, squashes, springs and twists as one solid silhouette, the whole green shape visibly redrawing between beats. Every lean is a BIG lean — the trunk bowing well over to one side, the branch tiers stacking over on themselves, the gold star swinging out sideways over the branches below. Every squash is a BIG squash — the whole silhouette dropping and fanning wide, then springing back. These are not small wobbles: between one beat and the next, the tree's outline is unmistakably a different shape.
LAYER TWO — ELVES WALK IN FROM BOTH SIDES CARRYING PRESENTS. Small chunky ELF figures, lit in bright green and red with pointed hats and curled-toe boots, march IN ALONG THE BOTTOM OF THE CURTAIN from the left edge and from the right edge, each one carrying a wrapped present held out in front of it in both arms. They walk with a big bouncy stomping stride, knees lifting high, hats bobbing with every step — the walk cycle drawn by whole bulbs switching, so they visibly stomp rather than glide. They cross the dark band of unlit door toward the base of the tree, set their present down on the growing pile at its foot, wave both arms over their heads in celebration, and turn and march back out the way they came. A new elf enters roughly every half second, alternating sides, so at any instant there are elves walking in, elves setting down, and elves marching out — the bottom of the picture is never empty and never still, and the pile of presents at the base of the tree GROWS bigger and wider across the four seconds as more are stacked on.
ELF CONTAINMENT: the elves are SMALL — no taller than the bottom tier of branches — and they stay in the BOTTOM BAND of the curtain the whole time. They enter from just INSIDE the left and right edges of the curtain and they walk out to just INSIDE those same edges — they never touch the edge, never cross it, never appear on the brick, the hedge, the birch or the driveway. They stay below the tree's lowest branches at all times and never climb, never jump high, never get in front of the star. The growing present pile spreads SIDEWAYS along the bottom band, never upward into the branches, and it always keeps the clear dark margin below it and at both sides.

THE ANIMATION IS RELENTLESS FROM FRAME ONE. THE BIGGEST MISTAKE WOULD BE A QUIET START. At 0.0s the artwork is already mid-cycle, already loud, already changing, and two elves are already mid-stride inside the frame — the picture does NOT switch on, does NOT hold still, does NOT ease in, and there is NOTHING calm about the first half second. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST THREE things are changing at once: the whole-body shape of the tree, an elf travelling across the bottom band, and a lighting effect somewhere else in the picture. There is no held frame, no pause, no settle:
0.0s — the clip opens mid-action: the tree is already bowed hard over to the LEFT, star swung out sideways, AND one elf is already halfway in from the left edge mid-stomp with a present in its arms while a second elf is just stepping in from the right edge, AND a bright chase of colour is already running down the tree from the star toward the base.
0.3s — the tree springs upright and squashes down wide at the base; the left elf reaches the foot of the tree and sets its present down with a bend of the knees; every red bauble swaps to gold and every gold bauble swaps to red, row by row down the tree.
0.6s — the tree bows hard over to the RIGHT, branch tiers stacking over, and the elf that just delivered throws both arms over its head, spins on the spot and starts marching back out to the left; a third elf enters from the right edge.
0.9s — the tree shimmies left-right-left fast; the gold star spins on the spot with its points stretching and shortening; the two elves on the bottom band cross paths in opposite directions, one in, one out.
1.2s — the tree squats deep, the whole silhouette compressing and fanning wide, then springs back; every bauble twinkles out and back in a rolling wave from left to right; the right elf sets down its present and the pile at the base gets visibly wider.
1.5s — the tree leans forward and nods twice like it is bowing; a chase of light runs DOWN the tree from the star to the presents one branch row at a time; a fourth elf stomps in from the left edge with a bigger present held high against its chest.
1.8s — the tree twists to one side, branches raking sideways; the present pile at the base bounces on the spot one after another; two elves wave both arms together and every bauble strobes twice fast.
2.1s — the tree twists hard the other way, baubles swinging out wide with the movement; an elf at the right hops twice on the spot before setting its present down; the star drops to half brightness then snaps back to full.
2.4s — the tree bows hard LEFT again, deeper than before; a chase of colour runs UP from the present pile to the star; a fifth elf enters from the right edge and two elves march out to the left, all three in stride at once.
2.7s — the tree bounces on the spot twice, squashing and stretching at the base with each bounce; every branch row swaps colour green to warm gold and back, row by row; the elves on the bottom band stomp in time with the bounces.
3.0s — the tree leans hard RIGHT and holds the lean while shivering; the star flares with a big ring of short spokes; every bauble and every present in the pile flashes in alternating pairs; a sixth elf stomps in from the left.
3.3s — the tree snaps upright and shimmies fast; a chase of light runs all the way around the outer edge of the silhouette; three elves at the base jump on the spot together, arms up.
3.6s — the tree squats wide one last time and springs back; the present pile strobes in sequence left to right then right to left; the last elves turn and march back out toward both edges.
3.9s — the tree lands square and centred, and the whole picture — tree, every bauble, the star, the whole grown pile of presents and every elf still in frame — flashes together to maximum brightness twice in quick succession for the final beat.
Every change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing, never a crossfade. The elves are drawn as chunky blocky bulb figures with no facial detail. The coloured reflections on the driveway shift and ripple with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the white garage door behind it: its horizontal panel seams, its rim of trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

HARD RULES: nobody turns around, no face is shown toward camera. No new real people walk into frame — the only new figures anywhere in the shot are the ELVES made of light inside the curtain. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
```

---

## Board metadata (archived from board.meta.json, 2026-09-18)

**Final cut order** - the order the shots appear in the edit,
which is not always the order the cards sit in on the board.

```
Final cut C01 → C02 → C03 → C04 → C05 → C06 → C07
```

**Stats trimmed off the lane panel**

| field | value |
|---|---|
| Stage | Final cut |
| Frames | gpt_image_2 · 2k · medium |

**Shot notes**

- `c01` - Generate the still beat, not the action — the action belongs to the video. The frame is deliberately the moment BEFORE the kick: feet flat, fists clenched, jaw set. Putting the kick in the start frame gives the clip nothing left to do.


## File traceability — verified 2026-09-21

This inventory accounts for local media. It does **not** certify that every historical take has a full prompt. Recovered records below supplement the original shot sections; they do not change the selected take. Image and clip take numbers are independent. A matching stem is not evidence that a clip used that image.

| Local file (relative to this archive) | Evidence / status |
|---|---|
| `clips/upscaled/v25_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v25_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v25_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v25_c04_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v25_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v25_c06_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/upscaled/v25_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c01_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c02_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c03_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c04_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c04_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c04_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c05_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c05_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c06_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c06_g2.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c06_g3.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `clips/v25_c07_g1.mp4` | Mentioned in the pre-repair archive (possibly via a shared stem); retained as historical evidence, not independently certified as a complete take record. |
| `starting_frames/v25_c01_g1.png` | Embedded PNG `hf-job-id`: `8ff914fc-b7c2-4011-aab8-60a68671f5f9`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v25_c01_g2.png` | Embedded PNG `hf-job-id`: `4c43a835-efbf-42b7-a636-5595f9c73bca`. Exact service prompt and returned parameters recovered below. |
| `starting_frames/v25_c02_g1.png` | Embedded PNG `hf-job-id`: `b02d8e1d-3688-4df4-8d86-3e77f092bfee`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v25_c03_g1.png` | Embedded PNG `hf-job-id`: `f21c1741-d9db-4fae-98f8-1bfd2861a089`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v25_c04_g1.png` | Embedded PNG `hf-job-id`: `2d686989-64a6-4bce-b0b9-728bf6c0f07a`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v25_c05_g1.png` | Embedded PNG `hf-job-id`: `f21070fe-78e7-492b-a6fb-4f54af191c0b`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v25_c06_g1.png` | Embedded PNG `hf-job-id`: `e1721c55-2092-4ba2-ad2e-171f98333bf2`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |
| `starting_frames/v25_c07_g1.png` | Embedded PNG `hf-job-id`: `d76217c3-1d6a-4c92-9d4a-ff7378c7e496`. Existing archive mention retained; this ID comes from the file, not an inferred UUID. |

### Recovered take — `starting_frames/v25_c01_g2.png`

**Evidence:** PNG embedded `hf-job-id` matched the Higgsfield service record retrieved on 2026-09-21. Job `4c43a835-efbf-42b7-a636-5595f9c73bca`; model `gpt_image_2`; service status `completed`. Selection/rejection outcome and reason are unknown unless explicitly recorded in the historical section.

#### Image prompt — exact service text

```text
@Image 1 is a photograph. Reproduce it EXACTLY - the same living room, the same tall artificial tree wrapped in spiralling silver duct-tape bands, the same deflated inflatable Santa, snowman, reindeer and penguin taped flat to the branches in exactly the same positions, the same lopsided foil star on top, the same cords trailing to the orange extension leads, the same plastic storage tub, tape roll, scissors and air pump on the floor, the same beige sofa, the same framed photos, the same lamp, the same curtains, the same warm night lighting, and the same man in the grey marl sweatshirt and dark jeans standing in the left foreground with his back three-quarters to the camera, feet flat, fists clenched, looking up at the tree - in exactly the same position and at exactly the same size in the frame.

CHANGE ONE THING ONLY: ADD A LITTLE MORE EMPTY SPACE AT THE TOP OF THE FRAME. Tilt the camera down very slightly so there is a clean band of plain empty ceiling and bare wall above the star at the top of the picture - a little more headroom than in @Image 1, about one tenth of the frame height of clean empty space, so a text caption can sit there. JUST A LITTLE - do not zoom out, do not move the camera back, do not shrink the tree or the man, do not add anything into that space. The tree top and star must still be high in the frame, just with a small clean gap above them.

Everything else identical.

IMAGE QUALITY - CRITICAL: a real photo taken on a recent iPhone. Extremely high quality, hyper realistic, tack-sharp across the whole frame, clean natural warm indoor lighting. Absolutely no blur, no softness, no smearing, no heavy noise, no shallow-depth-of-field bokeh, no cinematic colour grade, no vignette, no haze, no bloom, no motion blur, no CGI polish. Real amateur phone photo, natural noise. No text overlay, no captions, no watermark, no logos.
```

#### Settings and attached references — exact returned parameters

```json
{
  "aspect_ratio": "9:16",
  "medias": [
    {
      "role": "image",
      "data": {
        "id": "8ff914fc-b7c2-4011-aab8-60a68671f5f9",
        "type": "image_job",
        "url": "https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_160430_8ff914fc-b7c2-4011-aab8-60a68671f5f9.png"
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

- C01: the board showed `v25_c01_g1.png` as the start frame, but the clip in the cut was animated from `v25_c01_g2.png` (the Higgsfield start image). Card corrected.
- C04: the board did not show the exact clip prompt of `v25_c04_g3.mp4`; it now does.
- C05: the board did not show the exact clip prompt of `v25_c05_g2.mp4`; it now does.
- C06: the board did not show the exact clip prompt of `v25_c06_g3.mp4`; it now does.

### C01 — Kicking the taped-up tree

**In the cut:** `starting_frames/v25_c01_g2.png` → `clips/v25_c01_g1.mp4`

#### Image prompt — `starting_frames/v25_c01_g2.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `4c43a835-efbf-42b7-a636-5595f9c73bca`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_163244_4c43a835-efbf-42b7-a636-5595f9c73bca.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_25_assets/starting_frames/v25_c01_g1.png` · Higgsfield media `8ff914fc-b7c2-4011-aab8-60a68671f5f9`

````text
@Image 1 is a photograph. Reproduce it EXACTLY - the same living room, the same tall artificial tree wrapped in spiralling silver duct-tape bands, the same deflated inflatable Santa, snowman, reindeer and penguin taped flat to the branches in exactly the same positions, the same lopsided foil star on top, the same cords trailing to the orange extension leads, the same plastic storage tub, tape roll, scissors and air pump on the floor, the same beige sofa, the same framed photos, the same lamp, the same curtains, the same warm night lighting, and the same man in the grey marl sweatshirt and dark jeans standing in the left foreground with his back three-quarters to the camera, feet flat, fists clenched, looking up at the tree - in exactly the same position and at exactly the same size in the frame.

CHANGE ONE THING ONLY: ADD A LITTLE MORE EMPTY SPACE AT THE TOP OF THE FRAME. Tilt the camera down very slightly so there is a clean band of plain empty ceiling and bare wall above the star at the top of the picture - a little more headroom than in @Image 1, about one tenth of the frame height of clean empty space, so a text caption can sit there. JUST A LITTLE - do not zoom out, do not move the camera back, do not shrink the tree or the man, do not add anything into that space. The tree top and star must still be high in the frame, just with a small clean gap above them.

Everything else identical.

IMAGE QUALITY - CRITICAL: a real photo taken on a recent iPhone. Extremely high quality, hyper realistic, tack-sharp across the whole frame, clean natural warm indoor lighting. Absolutely no blur, no softness, no smearing, no heavy noise, no shallow-depth-of-field bokeh, no cinematic colour grade, no vignette, no haze, no bloom, no motion blur, no CGI polish. Real amateur phone photo, natural noise. No text overlay, no captions, no watermark, no logos.
````

#### Video prompt — `clips/v25_c01_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 720p · 5 s · 9:16 · audio on
**Job** - `78400d24-c63e-499d-a7f5-eb1d2a9d0124`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_175052_78400d24-c63e-499d-a7f5-eb1d2a9d0124.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v25_c01_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c01_g2.png` · Higgsfield media `4c43a835-efbf-42b7-a636-5595f9c73bca`

````text
The attached start frame is frame one. Animate it exactly as it is: the same ugly-decorated living room, the same Christmas tree with plush and inflatable decorations duct-taped to its branches and wide tape bands spiralling down it, the same man standing in front of the tree, the same lamps and lighting, the same clothes, the same everything.

CAMERA: locked handheld. The camera does not move to a new position at any point — no zoom in, no zoom out, no push, no pull, no pan, no tilt, no orbit, no rack focus. The only movement is a tiny natural handheld micro-shake, as if someone is standing still holding a phone. The framing at 5.0s is the same framing as at 0.0s. NOTHING of the camera operator is visible — no phone, no screen, no hand, no fingers, no arm, no sleeve, no device, no object in the foreground or along any edge at any moment.

TIMELINE (5 seconds):
0.0-0.8s — The man is rigid with rage. His fists clench tighter, his shoulders rise, his head tips back and he yells at the tree, his whole upper body shaking.
0.8-1.6s — He takes one hard step toward the tree, weight shifting onto his left foot, right arm swinging back, still shouting.
1.6-2.3s — THE KICK. He drives his right foot hard into the lower trunk of the tree — one single violent kick, boot connecting with the taped branches, the impact snapping his leg straight.
2.3-3.3s — The tree goes over. It tips away from him, the taped plush and inflatable decorations tearing loose and flying off, tape strips fluttering, baubles bouncing, the trunk swinging down through the frame.
3.3-5.0s — The tree crashes onto the floor with a heavy thud and a spray of needles and ornaments. The man stands over it, chest heaving, both arms flung out to the sides, still yelling down at the wreck.

AUDIO: natural room sound only — the thud of the kick, branches snapping, tape tearing, ornaments bouncing on the floor, the heavy crash of the tree. The man shouts furiously: "I'M DONE WITH THIS! DONE!" No music, no score, no background song, no narration.

Hyper-realistic amateur iPhone video, extremely high quality, real weight and physics on the tree and the flying decorations, natural indoor lighting, natural motion blur, no slow motion, no text, no watermark, no logo.
````

**Other takes of C01 on disk (1)**

#### Image prompt — `starting_frames/v25_c01_g1.png`

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `8ff914fc-b7c2-4011-aab8-60a68671f5f9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_160430_8ff914fc-b7c2-4011-aab8-60a68671f5f9.png (same byte size as the local file)
**References, in submission order**
- @Image 1: uploaded file, not on the drive · Higgsfield media `e65739f1-8f6b-4a44-a02f-51c3e6884026`

````text
USE THE ATTACHED REFERENCE PHOTOGRAPH for ONE THING ONLY: how the decorations are attached to the Christmas tree. In the reference, long WIDE STRIPS OF SILVER TAPE are wrapped around the tree in big diagonal bands that spiral all the way down it, and soft Christmas figures are stuck flat onto the branches with that tape. Copy that exact taping idea. Ignore the reference's room, its staircase, its ladder, its woman and its text overlay.

A real candid photograph taken on a recent iPhone, vertical 9:16, inside an ordinary American family living room at night, lamps on, warm indoor light.

CAMERA AND FRAMING: camera standing on the living-room floor about four metres from the tree, held at chest height, level, tilted slightly up so the whole tree fits. The tree stands slightly right of centre and runs almost the full height of the frame, its crooked top near the top of the picture. The TOP SIXTH OF THE FRAME IS CLEAN EMPTY PLAIN CEILING AND BARE WALL with nothing in it. The bottom of the frame shows the rug and the floor around the tree base.

THE TREE - THE JOKE: a tall artificial green Christmas tree, thin and patchy with obvious gaps and a visibly bent crooked top. Wrapped around it, exactly like the reference, are WIDE BANDS OF SILVER DUCT TAPE spiralling diagonally down the whole tree from top to bottom, six or seven bands, each one slightly wonky, the cut ends frayed and peeling away from the branches. TAPED FLAT ONTO THE TREE with more strips of that silver duct tape are small Christmas AIR-BLOWN INFLATABLE figures, switched off and DEFLATED so they hang limp, wrinkled and creased against the branches: a deflated Santa taped at chest height with his hat flopped over his face and his empty legs dangling down; a slumped inflatable snowman taped lower down, leaning badly off vertical; a limp reindeer taped near the top with one antler folded completely flat; a crumpled penguin taped upside down on the left side. Their fabric is sun-faded, dirty and streaked, with grey duct-tape repair patches. Their black power cords dangle loose off the branches and trail down into a tangled knot of orange extension leads on the floor.

Also on the tree: one sad strand of old multicolour bulb lights slung round in an uneven droop with several bulbs dead or missing, a handful of mismatched cracked baubles, clumps of limp grey tinsel, and a battered lopsided foil star jammed on the crooked top.

THE ROOM: a lived-in family living room - oatmeal carpet with a worn rug, a beige fabric sofa on the left with mismatched cushions, a cream painted wall behind, a framed family photo, a table lamp with a warm glow, a radiator, heavy curtains closed over a window on the right. On the floor by the tree: an open plastic storage tub of tangled decorations, a half-used roll of silver duct tape, scissors, and a small electric air pump with its hose coiled beside it.

THE MAN: a man in his late thirties stands on the floor in the left foreground, IN FRONT OF THE TREE and slightly to the side of it, turned three-quarters away from the camera so we mostly see his back and the side of his face, looking UP at the taped-up tree. He wears a grey marl sweatshirt, dark jeans and white socks. He is STANDING STILL with BOTH FEET FLAT ON THE FLOOR, weight even, arms hanging down at his sides with his fists clenched, shoulders tight, jaw set, quietly furious. He is NOT kicking, NOT swinging, NOT mid-motion, NOT off balance - this is the still, tense moment just BEFORE anything happens. He is cut off by the left edge of the frame at the shoulder and stands large in the foreground, roughly a third of the frame width, his head around a third of the way down from the top.

This is the grim, embarrassing BEFORE shot in a before-and-after gag - genuinely tacky, cheap and ugly, shot completely straight like a real phone snapshot.

IMAGE QUALITY - CRITICAL: a real photo taken on a recent iPhone. Extremely high quality, hyper realistic, tack-sharp across the whole frame, crisp tape edges, crisp wrinkled vinyl fabric, crisp carpet and fabric texture, clean natural warm indoor lighting with no muddy shadows. Absolutely no blur, no softness, no smearing, no heavy noise, no shallow-depth-of-field bokeh, no cinematic colour grade, no vignette, no haze, no bloom, no motion blur, no CGI polish, no illustration. Real amateur phone photo, natural noise. No text overlay, no captions, no watermark, no logos.
````

### C02 — Box over the sofa

**In the cut:** `starting_frames/v25_c02_g1.png` → `clips/v25_c02_g1.mp4`

#### Image prompt — `starting_frames/v25_c02_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `b02d8e1d-3688-4df4-8d86-3e77f092bfee`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260913_223635_b02d8e1d-3688-4df4-8d86-3e77f092bfee.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_20_assets/starting_frames/v20_c02_g5.png` · Higgsfield media `05989e1b-228c-432a-be58-a51cfbfa19ad`
- @Image 2: `content/video_24_assets/starting_frames/v24_c02_g1.png` · Higgsfield media `22ca36a7-739f-42f9-ad11-a81c09882666`

````text
Reproduce the FIRST attached image's camera, framing and sofa placement EXACTLY. Copy the composition from it, do not reinvent it.

THE SOFA IS IN FRONT OF HER, NOT BESIDE HER. It sits ahead of her and runs diagonally away from the bottom-right foreground into the depth of the frame, so its long EMPTY seat cushions face up and are fully visible in the open space directly in front of her body, just beyond the box. She is facing the sofa. The sofa is NOT at her left, NOT behind her, and NOT running flat across the frame.

She stands at the LEFT EDGE of the frame, cut by it, seen from behind over her left shoulder, holding the big LED CURTAIN LIGHTS box out in front of her chest with both hands, the printed front of the box facing the camera and filling the middle of the frame - same box size and same position as in the first image. Wood floor visible at the bottom left.

CAMERA HEIGHT - take it from the SECOND attached image: the camera is at her SHOULDER HEIGHT, tilted down only very slightly. Not above her head, not a top-down shot.

A COMPLETELY NEW WOMAN AND A COMPLETELY NEW ROOM - take these from this text only, NOT from either attached image: an early-thirties East Asian woman with fair warm-toned skin and straight black hair falling to her shoulder blades with a blunt fringe, wearing a cream cable-knit jumper and light-wash jeans. The room has a warm walnut floor, a charcoal-grey linen sofa with cream and rust cushions and a chunky cream knit throw, a sage-green painted wall, a brass arc floor lamp, and a real green Christmas tree with multicolour lights and gold baubles at the right. Do NOT copy the hair, the skin tone, the clothing, the sofa colour, the wall or the tree from either attached image.

Real iPhone photo, tack-sharp, candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v25_c02_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 5 s · 9:16 · audio on
**Job** - `78e0e105-1751-482c-8e4d-6afc2b34950a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_123640_78e0e105-1751-482c-8e4d-6afc2b34950a.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v25_c02_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c02_g1.png` · Higgsfield media `0f36ae95-10dc-481c-bb3b-6f37a5e8a425`
- image ref 1: `product_images/box_nowindow/box_nowindow_g5.png` · Higgsfield media `ffaa8801-8e71-43f0-ae24-461104cf30f2`
- image ref 2: `product_images/box_nowindow/box_interior_g5.png` · Higgsfield media `f01fecfe-9cbe-44a5-a617-63193a1108b0`

````text
TWO SCENES IN ONE CLIP, JOINED BY ONE HARD CUT AT EXACTLY 2.5s. No dissolve, no fade, no whip pan, no transition effect — a straight in-camera cut, exactly like a creator cutting two takes together.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she walks at a walking pace, she kneels at the speed a body really kneels, the lid swings open at the speed heavy cardboard really swings. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in five seconds — one slow lowering, one slow kneel, one slow lid. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still settling as the clip ends than that any part of it looks fast-forwarded.

REFERENCE IMAGES. Reference image 1 is the first frame of scene 1 — start there, unchanged, and it owns the room, the woman, the camera angle and the geometry. Reference image 2 is the CLOSED PRODUCT BOX: the artwork on the box in this video must match it exactly. Reference image 3 is the OPEN BOX INTERIOR: what she reveals in scene 2 must match it exactly.

THE WOMAN — she is exactly the woman in reference image 1 and never changes: an early-thirties East Asian woman with fair warm-toned skin and straight black hair falling to her shoulder blades with a blunt fringe, in a cream cable-knit jumper and light-wash jeans. Same hair, same fringe, same skin, same clothes, first frame to last.

BOX SPEC — TRUE IN EVERY FRAME. A matte black rigid retail box, 55 cm wide x 42 cm tall x 10 cm deep. It is BIG — much wider than the span of two outstretched hands; each of her hands covers less than a quarter of the box width, and laid on the sofa seat it spans most of one cushion. Front panel top to bottom: a large white condensed uppercase headline LED CURTAIN LIGHTS; a warm gold subline Create Your Own Magic; a red diagonal BEST SELLER ribbon flag in the top-right corner; one large photographic panel with a thin gold hairline border showing a night house facade with a glowing pixel LED Christmas tree on the garage door; a bottom row of five small gold line icons with white captions. NO transparent window, NO clear plastic panel, NO die-cut cutout, NO product visible through the front, NO glowing lights showing through the cardboard. The box is closed and sealed until the moment she opens it in scene 2.

SCENE 1 — 0.0 to 2.5s. CAMERA: HELD IPHONE, LOCKED FOCAL LENGTH, portrait, a friend filming from just behind her left shoulder at HER SHOULDER HEIGHT, tilted down only very slightly — exactly where reference image 1 was taken. NOT above her head, NOT a top-down shot. NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO DOLLY. Handheld micro-shake only. She is at the LEFT EDGE of frame, partly cut off by it; the charcoal-grey linen sofa is directly IN FRONT of her, running diagonally away into depth and filling the right and bottom-right of frame, its empty seat cushions facing up. The room behind her — the warm walnut floor, the sage-green painted wall, the brass arc floor lamp, the cream and rust cushions, the chunky cream knit throw and the real green Christmas tree with multicolour lights and gold baubles at the right — stays exactly as it is and never changes.
THE WHOLE POINT OF SCENE 1: she carries the box round in front of the sofa, sets it flat on the seat cushion AND drops to her knees IN THE SAME CONTINUOUS MOTION. These are not two separate steps — the box going down and her body going down are one move.
0.0-0.9s — one unhurried step forward and to her right, her shoulders turning, the heavy box swinging slowly out in front of her; her straight black hair swings across her back and settles, her cream sleeve creases with the weight.
0.9-1.8s — she steps in front of the sofa and leans forward from the hips, lowering the box steadily toward the empty charcoal-grey linen seat cushion, arms extending, knees already bending underneath her. This lowering is SLOW and heavy — the box is big and awkward and she is being careful with it.
1.8-2.5s — the box settles flat and printed-side-up on the cushion with a soft compression of the linen, her hands still on it, and in the same continuous motion her knees come down onto the warm walnut floor one after the other, her weight settling and her back rounding forward; she tucks a strand of hair behind one ear and plants both palms flat on the box lid, chest rising with one excited breath.

HARD CUT AT 2.5s.

SCENE 2 — 2.5 to 5.0s. Direct continuation, same room, same second, same woman, same cream cable-knit jumper, same box in exactly the same place on the same charcoal-grey cushion. The camera has moved about 30 degrees round to her side — a slightly more side-on three-quarter angle, a little lower, closer to the level of the sofa seat, so we now see the lid edge in profile and read the pivot clearly. Still HELD IPHONE, LOCKED FOCAL LENGTH, handheld micro-shake only, NO ZOOM.
LID MECHANISM, GEOMETRICALLY. The box is a magnetic-closure flip-top. The hinge runs along the TOP LONG EDGE of the box — the far edge away from her, at the back. The lid pivots UP and BACK on that hinge, rotating away from her and toward the back of the sofa, keeping its printed front face turned toward the camera as it rises. The inside of the lid is matte black. The lid is NEVER lifted off, NEVER removed, NEVER carried aside, NEVER set down, NEVER folded flat instantly, NEVER slid out like a drawer.
2.5-3.1s — she hooks her fingertips under the near front edge of the lid; a small snap as the magnets release and the front edge lifts a centimetre, a thin black shadow line opening slowly across the whole 55 cm width.
3.1-4.3s — she pivots the big printed lid UP and BACK on its hinge in ONE slow continuous arc with real cardboard weight, her elbows rising and her shoulders lifting with the effort, until it stands roughly vertical. This arc takes well over a full second of screen time — it travels heavily and never flips or snaps open.
4.3-5.0s — the interior is revealed exactly as reference image 3: the neatly folded BLACK LED mesh curtain lying in its tray, the coiled black lead and the small accessory items beside it, all against a matte black interior. She reaches in with both hands and touches the folded black mesh, fingers spreading it slightly, then lifts her chin, looks off toward the tree and breaks into a big open-mouthed grin, eyebrows up.

MOVEMENT RULE FOR BOTH SCENES: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole clip — weight shifting, chest breathing, hair and sleeves swinging and settling, the cushion compressing under the box — and her face keeps changing, eyes, eyebrows and mouth reading differently moment to moment. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses.

HARD RULES: exactly ONE cut, at 2.5s. The box never changes size, never changes artwork, never gains a window or a cutout. The curtain inside the box is BLACK cord with small dark bulbs — never white wire, never clear wire, never silver wire. Nobody else enters frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Quiet warm living-room ambience, the soft thump of a heavy box on a cushion, knees on the floor, the click of magnets releasing, stiff cardboard flexing, plastic mesh rustling, one small delighted exhale.

LOOK: real iPhone UGC indoors at night. Warm mixed lamp and fairy light, slight sensor noise in the shadows, natural skin, no cinematic grade, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
````

### C03 — Pinning the curtain up

**In the cut:** `starting_frames/v25_c03_g1.png` → `clips/v25_c03_g1.mp4`

#### Image prompt — `starting_frames/v25_c03_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `f21c1741-d9db-4fae-98f8-1bfd2861a089`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260913_223737_f21c1741-d9db-4fae-98f8-1bfd2861a089.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_24_assets/starting_frames/v24_c03_g3.png` · Higgsfield media `fa0d894f-68c0-4335-a769-b02161a6be90`
- @Image 2: `content/video_25_assets/starting_frames/v25_c02_g1.png` · Higgsfield media `b02d8e1d-3688-4df4-8d86-3e77f092bfee`

````text
Same shot as the FIRST attached image - copy its camera, framing and staging EXACTLY. Daytime, overcast winter light, snow on the ground. A woman stands on a black folding step stool, seen from BEHIND, facing the house wall, both arms raised in front of her at the top of the wall, her hands up near the gutter line as she fixes the LED curtain to it. The big bundle of unlit LED curtain strands is heaped on the snow at the foot of the stool.

THE CAMERA ANGLE IS FLAT AND FRONTAL, exactly as in the first image: the wall faces the camera almost square-on and fills the frame, the vertical lines of the siding run straight up and down. The wall is NOT turned away at an angle, NOT receding steeply into the distance, NO strong oblique perspective, NO wide-angle corner view.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand hanging down the wall is a thin BLACK cord with small DARK unlit bulbs on it. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire anywhere. The lights are OFF, no glow.

THE WOMAN - take her from the SECOND attached image: the same early-thirties East Asian woman with fair warm-toned skin and straight black shoulder-blade-length hair with a blunt fringe. Outdoors she wears a deep teal parka with a faux-fur hood trim, grey jeans and brown boots.

A COMPLETELY NEW HOUSE AND BACKGROUND - take these from this text only, NOT from the first attached image: the wall she is working on is WARM CREAM STUCCO with a dark bronze gutter, dark bronze fascia and a dark bronze downpipe running down the right side. A low dark-stained wooden fence runs along the right of the frame. A bare white birch tree stands beyond the left corner of the house. A red-brick neighbour house is visible at the far right edge. Do NOT copy the slate-blue board-and-batten siding, the white trim, the brick garden wall or the hedge from the first image.

Real iPhone photo, tack-sharp, candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v25_c03_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `9336af2d-a452-4c74-877b-34c7db8e1c56`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_123641_9336af2d-a452-4c74-877b-34c7db8e1c56.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v25_c03_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c03_g1.png` · Higgsfield media `71244106-f4cd-45d5-9186-cd7f19d1e0c1`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same overcast winter day, same WARM CREAM STUCCO wall filling the frame, same dark bronze gutter and dark bronze fascia along the roof edge, same dark bronze downpipe and low dark-stained wooden fence at the right, same red-brick neighbour house at the far right edge, same bare white birch beyond the left corner, same snow on the ground, same black folding step stool, same woman seen from behind in the deep teal parka with the faux-fur hood trim, grey jeans and brown boots, standing on the stool with both arms raised pinning the gathered fistful of unlit net up under the gutter, same LED net already hung flat across the wall to her left, same loose tangled coil of curtain heaped on the snow at the foot of the stool.

REAL TIME — NORMAL 1x SPEED. THIS IS THE MOST IMPORTANT RULE IN THIS PROMPT. This is one real-time phone video played back at ordinary speed. Everything happens at the pace a real person actually moves: she reaches at the speed an arm really reaches, she shakes the net out at the speed a heavy tangled net really swings, she shifts her weight at the speed a body really balances on a step stool. ABSOLUTELY NO fast motion, NO sped-up playback, NO double speed, NO under-cranking, NO time-lapse, NO hyperlapse, NO sudden jump in tempo, NO frantic twitchy limbs, NO snapping instantly from one pose to the next, NO scrubbing through the action. There is DELIBERATELY very little to do in four seconds — one slow shake, one slow reach, one slow sideways press. If the action does not fit comfortably, SLOW THE ACTION DOWN; never speed the footage up. It is far better that she is still mid-reach as the clip ends than that any part of it looks fast-forwarded.

CAMERA — HELD IPHONE, LOCKED FOCAL LENGTH. Portrait, exactly the framing and the angle of the reference image, flat and frontal to the wall, looking slightly up at it. Handheld micro-shake only — a few pixels of organic drift. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY, NO CRANE, NO ORBIT. The wall, the dark bronze gutter, the wooden fence and the stool stay exactly the same size in frame from the first frame to the last, and the camera never swings round to an oblique or corner-on view of the wall.

MOVEMENT RULE: she is never frozen and never hurried. Her body is in continuous unhurried motion the whole four seconds — weight shifting on the stool, shoulders rolling, ribs breathing, the faux-fur hood trim stirring, the teal parka creasing and rustling, the strands swaying on after every touch. But every change FLOWS smoothly into the next at natural human speed. She never snaps, never jitters, never stutters between poses, and no limb ever travels faster than a real arm travels.

ACTION TIMELINE (4 seconds, one continuous take, no cuts) — ONLY TWO THINGS HAPPEN, AND BOTH ARE SLOW:
0.0-2.0s — she lifts the gathered bundle in her right hand and shakes it out ONCE, slowly and heavily. The shake takes well over a full second of screen time: her arm swings out and down, the tangled net lets go in stages rather than all at once, and a long sheet of black strands falls open down the cream stucco and swings for a moment before it settles. The loose coil on the snow drags and shifts with it.
2.0-4.0s — still up on the stool, she stretches both arms high and presses the header wire up under the lip of the dark bronze gutter, her thumbs working slowly along it, then walks her hands a short way sideways to her RIGHT along the roofline, onto the bare stretch of wall beyond the strands she has already hung, pressing and tucking as she goes, her torso twisting and her heels lifting and dropping on the tread. She is STILL tucking when the clip ends. The curtain sways gently against the stucco and is still settling on the last frame.
THAT IS THE WHOLE CLIP. She does NOT step down off the stool, does NOT step back, does NOT plant her hands on her hips and does NOT tilt her head back to look at her work. There is no time for any of that at real speed, and cramming it in is exactly what would force the footage to look sped up. She stays on the stool from the first frame to the last.

THE LED CURTAIN IS BLACK — CRITICAL. The wire is BLACK, not white and not clear. Every vertical strand hanging down the wall is a thin BLACK cord and the unlit bulbs on it are small and DARK. Against the warm cream stucco the strands read as thin dark lines, clearly visible the whole four seconds. The heaped bundle on the snow is a tangle of BLACK cord, clearly dark against the white snow. No white wire, no clear wire, no silver wire appears at any moment.

HARD RULES: the curtain is COMPLETELY OFF the entire time — not one bulb lights, no glow, no colour, no animation on the wall. The wall never gains windows, doors or new features, the dark bronze gutter and downpipe never move and the wooden fence never changes. The strands are separate vertical strands obeying gravity, sagging slightly, with an uneven wavy bottom hem — never a flat sheet, never a panel, never a screen. The loose coil rests in the snow with real contact shadows. Her face is never shown; she stays turned away from camera throughout. No other people enter frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO CAPTIONS, NO SUBTITLES, NO WATERMARK anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor winter ambience, thin plastic strands rattling and clicking against stucco, a step-stool creak, boots on a metal tread, boots compressing snow, one quiet effortful breath. No voice.

LOOK: real iPhone UGC. Flat overcast winter daylight, slightly cool white balance, mild sensor noise, natural skin, no cinematic grade, no lens flare, no slow motion, no speed ramp, no fast motion. The whole clip plays at normal 1x speed from first frame to last.
````

### C04 — Phone POV, wall dead-on

**In the cut:** `starting_frames/v25_c04_g1.png` → `clips/v25_c04_g3.mp4`

#### Image prompt — `starting_frames/v25_c04_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `2d686989-64a6-4bce-b0b9-728bf6c0f07a`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260913_223834_2d686989-64a6-4bce-b0b9-728bf6c0f07a.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_24_assets/starting_frames/v24_c04_g3.png` · Higgsfield media `b22ec2ca-0015-4769-8227-98d4ddee5813`
- @Image 2: `content/video_25_assets/starting_frames/v25_c03_g1.png` · Higgsfield media `f21c1741-d9db-4fae-98f8-1bfd2861a089`

````text
Same shot as the FIRST attached image - copy its camera, framing and staging EXACTLY. Night.

THE CAMERA ANGLE IS DEAD-ON SQUARE TO THE WALL, exactly as in the first image: the wall faces the camera flat and fills the frame, its vertical lines run straight up and down. The wall is NOT turned away at an angle, NOT receding into the distance, NO strong oblique perspective, NO corner view.

TWO THINGS THAT MUST BE PRESENT, exactly as in the first image - do not omit either:
1. The LED CURTAIN IS ALREADY MOUNTED ON THE WALL, hanging in evenly spaced vertical see-through strands from the gutter line down across the wall, with slight natural sag and an uneven bottom hem.
2. At the BOTTOM CENTRE of the frame, a hand holds a smartphone up toward the wall, screen facing the camera and BRIGHTLY LIT, showing a real phone app UI: a dark blue app screen with a grid of small square scene thumbnails and a large round play button - the screen glows and lights the hand.

THE LED CURTAIN IS BLACK - CRITICAL: the wire is BLACK, not white and not clear. Every vertical strand is a thin BLACK cord with small DARK unlit bulbs on it, no glow. The strands still read clearly as thin dark vertical lines against the wall, caught by the street lamp from the left and the porch light from the right so they stay visible, not invisible. No white wire, no clear wire, no silver wire anywhere.

THE HOUSE - take it from the SECOND attached image: the SAME wall, the same WARM CREAM STUCCO, the same dark bronze gutter, dark bronze fascia and dark bronze downpipe on the right, the same low dark-stained wooden fence at the right, the same bare white birch tree beyond the left corner, the same red-brick neighbour house at the far right edge. It must read as literally the same house, now at night.

Lighting: a street lamp glow from the left and a warm porch light from the right, snow on the ground catching the light. Real iPhone night photo, tack-sharp, candid UGC, no text overlay, no watermark.
````

#### Video prompt — `clips/v25_c04_g3.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `840228cd-c359-4f24-8ae9-51382c2b37d0`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_154326_840228cd-c359-4f24-8ae9-51382c2b37d0.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v25_c04_g3.mp4` (1440×2560)
**Attached, in submission order**
- image ref 1: `content/video_25_assets/starting_frames/v25_c04_g1.png` · Higgsfield media `e69045a5-1251-48f2-8f98-e5a645e7170d`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same WARM CREAM STUCCO wall of the house seen dead-on and flat, filling the frame, with the UNLIT LED curtain hanging in thin black vertical strands across it, same dark bronze gutter along the top and dark bronze downpipe at the right, same dark-stained wooden fence at the right, same snow in the foreground, same hand coming up from the bottom holding a phone up in the lower part of frame, same app screen showing a dark blue grid of small colourful scene tiles with a BIG ROUND BLUE PLAY BUTTON at the bottom of the screen.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, handheld micro-shake only. The camera stays DEAD-ON SQUARE to the wall the whole four seconds — it never swings round to an oblique angle, never turns to a corner view, never tilts up. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY. The wall and the phone stay exactly the same size in frame throughout.

THE SINGLE MOST IMPORTANT THING IN THIS CLIP IS THE SYNC. The thumb presses the big round PLAY button, and ON THAT VERY SAME FRAME the wall lights up. Not a frame early, not a frame late, no gap, no delay, no anticipation, no lag. The press and the light are ONE event. And the instant the button is pressed the hand immediately drops away out of the bottom of frame — it does not linger, does not hold the phone up to admire the wall, does not stay in shot for even half a second after the press.

THE PHONE PART IS SHORT. THE LIT PART IS MOST OF THE CLIP. The phone is finished and gone by 1.3s. From 1.3s to the very last frame — nearly THREE FULL SECONDS — there is nothing in the foreground and the wall is lit and animating hard. The animation must NOT be squeezed into the last second and must NOT be a slow, sparse, gentle thing.

HOW THE PICTURE IN THE LIGHTS IS DRAWN — READ THIS BEFORE ANYTHING ELSE. It is FLAT CARTOON LIGHT ART built out of individual glowing bulbs, like a chunky neon shop sign or a big pixel sprite. Thick simple outlines, flat blocks of colour, big silly cartoon face. It is NOT a photograph. It is NOT a realistic person or animal. It is NOT 3D, NOT rendered, NOT shaded, NOT textured, NOT furry, NOT lifelike, and NOT a video projected onto the wall. If it could be mistaken for a photo of something real, it is wrong. Think cheap funny Christmas light display, not fine art.

ACTION TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.8s — A SHORT SCROLL, NOT A LONG ONE. The thumb comes in from the bottom and gives the grid of scene tiles ONE small flick: the tiles slide up by roughly ONE ROW only, a single fresh row of new scene thumbnails comes into view from the bottom, the list overshoots slightly and settles back with a small bounce. That is the entire scroll. NO long scroll, NO repeated flicks, NO second flick, NO rows racing past, NO scrolling through the whole list. One tile in the grid keeps its bright highlight ring the whole time — the scene is already chosen.
0.8-1.0s — the thumb slides straight down to the BIG ROUND BLUE PLAY BUTTON at the bottom of the app screen and comes to rest on it.
1.0s — THE THUMB PRESSES PLAY. On that exact frame the button visibly depresses and flashes, AND the entire wall SNAPS ON at full brightness in the very same single frame. NO fade, NO dissolve, NO ramp, NO brightness curve, NO bulbs lighting one by one, NO sweep across the wall, NO pause between the press and the light. One frame dark, the next frame fully lit at maximum brightness.

THE ARTWORK THAT APPEARS — SANTA LOSES HIS TROUSERS. One full-height cartoon SANTA drawn in bulbs, standing facing the camera in the middle of the lit area. His broad black belt has POPPED OPEN and swings loose, and his big red trousers have dropped straight down and are bunched around his black boots. Underneath he is wearing enormous baggy long underpants in red and white candy stripes with little white hearts on them. Both his white-gloved hands grab at the fallen waistband, his eyes are two huge white circles, his mouth is a big round O, his cheeks are two bright pink dots and his white beard is flying sideways. His red sack has been dropped and lies tipped over at his feet with a couple of coloured presents rolling out. Down at the bottom left a small GREEN ELF is doubled over laughing, pointing straight up at him with one arm, hat flopping. Colours: bright red, white, black, green, pink and gold. A ring of gold stars pops around Santa's head.

1.0-1.3s — the hand drops straight down and out of the bottom of frame fast and NEVER returns. The phone, the hand, the fingers and the sleeve are completely gone from frame by 1.3s and no part of them reappears at any point.
1.3-4.0s — THE REST OF THE CLIP IS THE LIT WALL ALONE, and it is relentless. See the movement block below.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. From the moment the wall snaps on, SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least NINE separate changes between 1.3s and the last frame — and at every single instant AT LEAST TWO things are changing at once: Santa's whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no pause, no settle, no gentle drifting. Every beat is a clearly DIFFERENT WHOLE-BODY pose — arms, legs, head and body all in a new position — the figure fully redrawing between beats like an animated light-bulb sign. If two consecutive beats look similar, it is wrong.
1.3s — it lands out of the snap-on already mid-move: Santa bent forward at the waist, both hands snatching down at the fallen trousers, knees knocked together, while the gold stars around his head flash on and the elf's laughing mouth flips wide open.
1.6s — he hauls the trousers UP to his knees with both arms straight up above his head from the effort, chest thrown out, and a bright chase of colour runs across the candy stripes of his underpants from left to right.
1.9s — the trousers drop straight back down to his boots, Santa's arms fly out wide to both sides in a huge shrug, head thrown back, and every gold star twinkles out and back in a rolling wave.
2.2s — he hops on one boot with the other leg kicked high and bent, tangled in the trousers, both hands flung forward for balance, and the elf jumps up and down twice, flashing bright green each time.
2.5s — he spins a quarter turn so he is side-on, one hand clapped over his backside, the other pointing away off frame, and the whole picture flashes brighter row by row from the boots upward.
2.8s — he spins back square to camera with both hands slapped over his face in shame, fingers spread, legs crossed tight, and the stripes on the underpants flash alternately red and white.
3.1s — he crouches right down to grab the trousers with both hands, bottom out behind him, beard hanging forward past his knees, and a chase of colour runs UP from the boots to the tip of his hat.
3.4s — he springs upright with both fists punched high in triumph, trousers finally at his waist, one leg kicked out to the side, and the gold stars strobe with the punch.
3.7s — the belt pops open again and the trousers drop for the last time, Santa's head snapping down to look at them, shoulders hunched, hands out flat in disbelief, while the elf rolls over backwards laughing and the presents on the ground flash colour.
3.9s — he turns square to camera and throws both arms out wide in a big shameless shrug with a huge grin, trousers still round his boots, and the whole picture — Santa, the underpants, the elf, the presents and every gold star — flashes to maximum brightness twice in quick succession for the final beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade, never a realistic animation curve. Coloured light spills and shifts across the snow below with every change.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. When the wall snaps on, the lit picture sits inside the curtain rectangle with a wide band of dark unlit wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from 1.0s to the last frame. Santa is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the frame he first appears. He NEVER scales up, never grows, never inflates, never creeps outward and never drifts across the wall. The dark unlit band around the picture is the same width in every single frame. Nothing lit ever spreads onto the stucco outside the curtain, onto the gutter, onto the fence or into the sky.

ABSOLUTELY NO TEXT: no letters, no words, no numbers, no speech bubbles, no signs and no writing of any kind anywhere in the lights or anywhere in the frame.

THE CURTAIN — CRITICAL: it stays a curtain of SEPARATE HANGING VERTICAL LIGHT STRANDS, NOT a solid LED video panel, NOT a flat screen and NOT a continuous mesh. There are clear DARK GAPS between the strands and the cream stucco wall behind is plainly visible through those gaps, especially in the unlit band around the picture. The bulbs are small round points of light strung along thin cords.

Real iPhone night video, handheld, tack-sharp, candid UGC. No text overlay, no watermark, no captions, no logo.
````

**Other takes of C04 on disk (2)**

#### Video prompt — `clips/v25_c04_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `ebfb9906-113a-41c6-8c80-cff682dadd4b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_123642_ebfb9906-113a-41c6-8c80-cff682dadd4b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c04_g1.png` · Higgsfield media `e69045a5-1251-48f2-8f98-e5a645e7170d`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same WARM CREAM STUCCO wall of the house seen dead-on and flat, filling the frame, with the UNLIT LED curtain hanging in thin black vertical strands across it, same dark bronze gutter along the top and dark bronze downpipe at the right, same dark-stained wooden fence at the right, same snow in the foreground, same hand coming up from the bottom holding a phone up in the lower part of frame, same app screen showing a dark blue grid of small colourful scene tiles.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, handheld micro-shake only. The camera stays DEAD-ON SQUARE to the wall the whole four seconds — it never swings round to an oblique angle, never turns to a corner view, never tilts up. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY. The wall and the phone stay exactly the same size in frame throughout.

THE CLIP IS SPLIT IN HALF, AND THE LIT HALF IS THE BIG ONE. The first half is a SHORT phone interaction. The second half — a FULL TWO SECONDS, from 2.0s to the very last frame — is the wall lit and the artwork animating. The lit half is never shorter than the dark half, and the animation must NOT be squeezed into the last second.

ACTION TIMELINE (4 seconds, one continuous take, no cuts):
0.0-1.5s — A SHORT SCROLL, NOT A LONG ONE. The thumb comes in from the bottom and gives the grid of scene tiles ONE small flick: the tiles slide up by roughly ONE ROW only, a single fresh row of new scene thumbnails comes into view from the bottom, the list overshoots slightly and settles back with a small bounce. That is the entire scroll. NO long scroll, NO repeated flicks, NO second flick, NO rows racing past, NO scrolling through the whole list. The thumb then just rests on the screen and the phone tilts a few degrees as the hand adjusts its grip.
1.5-1.8s — the thumb reaches out and TAPS one tile. The tapped tile flashes and takes a bright highlight ring.
1.8s — ON THAT EXACT FRAME the entire wall SNAPS ON at full brightness in a single frame. NO fade, NO dissolve, NO ramp, NO brightness curve, NO bulbs lighting one by one, NO sweep across the wall. One frame dark, the next frame fully lit at maximum brightness. THE ARTWORK THAT APPEARS: a big REINDEER with wide spreading antlers, a warm golden-brown body and a glowing red nose, standing in profile with its head turned toward the camera, with white snowflakes scattered and falling around it. Colours are warm golden-brown, white, red and pale blue against the dark unlit wall.
1.8-2.0s — the hand lowers straight down out of the bottom of frame quickly and NEVER returns. The phone is completely gone from frame by 2.0s.
2.0-4.0s — THE WHOLE BACK HALF OF THE CLIP IS THE LIT WALL. The frame holds on the glowing wall with nothing in the foreground and the artwork ANIMATES CONTINUOUSLY from 2.0s to the last frame, a clearly different whole-body pose roughly every four-tenths of a second: at 2.2s the reindeer tosses its head up and back so the big antlers swing, and the red nose flashes to double brightness; at 2.6s it lifts one front hoof high and paws the air, its body tipping with it; at 3.0s it lowers its head right down and swings the antlers wide to the other side, ears flicking; at 3.4s it springs up with both front hooves off the ground, tail flicking, while every snowflake around it shifts down a row; at 3.8s it plants all four hooves, straightens up tall with the antlers spread at full width and every snowflake twinkles out and back at once while the red nose pulses. Every pose change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — the figure fully redraws between beats, chunky and instantaneous, never smooth morphing. Coloured light spills and shifts across the snow below with each change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the warm cream stucco wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical BLACK wires hung side by side from a header cable pinned under the roof edge, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin BLACK wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

HARD RULES: the lit artwork is hard-cropped at all four edges of the curtain — it never grows, shrinks, shifts or warps, and nothing spills onto the roof, the dark bronze gutter, the sky or the neighbouring house. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video. Nobody walks into frame.

AUDIO: natural room sound only — no music, no score, no background song. Quiet cold suburban night ambience, a faint distant car, one soft UI tap, a faint electrical buzz as the wall comes on. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, slight motion blur in the highlights, natural phone screen glow on the fingers, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

#### Video prompt — `clips/v25_c04_g2.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `5b87bddc-fa90-41c8-9745-aa19de930aa9`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_144520_5b87bddc-fa90-41c8-9745-aa19de930aa9.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c04_g1.png` · Higgsfield media `e69045a5-1251-48f2-8f98-e5a645e7170d`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same WARM CREAM STUCCO wall of the house seen dead-on and flat, filling the frame, with the UNLIT LED curtain hanging in thin black vertical strands across it, same dark bronze gutter along the top and dark bronze downpipe at the right, same dark-stained wooden fence at the right, same snow in the foreground, same hand coming up from the bottom holding a phone up in the lower part of frame, same app screen showing a dark blue grid of small colourful scene tiles with a BIG ROUND BLUE PLAY BUTTON at the bottom of the screen.

CAMERA — HELD IPHONE, LOCKED FRAMING. Portrait, handheld micro-shake only. The camera stays DEAD-ON SQUARE to the wall the whole four seconds — it never swings round to an oblique angle, never turns to a corner view, never tilts up. ABSOLUTELY NO ZOOM IN, NO ZOOM OUT, NO PUSH IN, NO PULL BACK, NO DOLLY. The wall and the phone stay exactly the same size in frame throughout.

THE SINGLE MOST IMPORTANT THING IN THIS CLIP IS THE SYNC. The thumb presses the big round PLAY button, and ON THAT VERY SAME FRAME the wall lights up. Not a frame early, not a frame late, no gap, no delay, no anticipation, no lag. The press and the light are ONE event. And the instant the button is pressed the hand immediately drops away out of the bottom of frame — it does not linger, does not hold the phone up to admire the wall, does not stay in shot for even half a second after the press.

THE PHONE PART IS SHORT. THE LIT PART IS MOST OF THE CLIP. The phone is finished and gone by 1.3s. From 1.3s to the very last frame — nearly THREE FULL SECONDS — there is nothing in the foreground and the wall is lit and animating hard. The animation must NOT be squeezed into the last second and must NOT be a slow, sparse, gentle thing.

ACTION TIMELINE (4 seconds, one continuous take, no cuts):
0.0-0.8s — A SHORT SCROLL, NOT A LONG ONE. The thumb comes in from the bottom and gives the grid of scene tiles ONE small flick: the tiles slide up by roughly ONE ROW only, a single fresh row of new scene thumbnails comes into view from the bottom, the list overshoots slightly and settles back with a small bounce. That is the entire scroll. NO long scroll, NO repeated flicks, NO second flick, NO rows racing past, NO scrolling through the whole list. One tile in the grid keeps its bright highlight ring the whole time — the scene is already chosen.
0.8-1.0s — the thumb slides straight down to the BIG ROUND BLUE PLAY BUTTON at the bottom of the app screen and comes to rest on it.
1.0s — THE THUMB PRESSES PLAY. On that exact frame the button visibly depresses and flashes, AND the entire wall SNAPS ON at full brightness in the very same single frame. NO fade, NO dissolve, NO ramp, NO brightness curve, NO bulbs lighting one by one, NO sweep across the wall, NO pause between the press and the light. One frame dark, the next frame fully lit at maximum brightness.
THE ARTWORK THAT APPEARS: a big REINDEER with wide spreading antlers, a warm golden-brown body and a glowing red nose, standing in profile with its head turned toward the camera, with white snowflakes scattered around it. Colours are warm golden-brown, white, red and pale blue against the dark unlit wall.
1.0-1.3s — the hand drops straight down and out of the bottom of frame fast and NEVER returns. The phone, the hand, the fingers and the sleeve are completely gone from frame by 1.3s and no part of them reappears at any point.
1.3-4.0s — THE REST OF THE CLIP IS THE LIT WALL ALONE, and it is relentless. See the movement block below.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. From the moment the wall snaps on, SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least NINE separate changes between 1.3s and the last frame — and at every single instant AT LEAST TWO things are changing at once: the reindeer's whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no pause, no settle, no gentle drifting. Every pose is a clearly different WHOLE-BODY pose, the figure fully redrawing between beats like an animated light-bulb sign.
1.3s — it lands out of the snap-on already mid-move, head dropped low and swung hard to one side so the antlers sweep sideways and DOWN, front knees bent, while the red nose fires to double brightness and the snowflakes shift down a row.
1.6s — it swings the head and antlers hard to the other side, shoulders dipping with it, and a bright chase of colour runs down its whole body from head to tail.
1.9s — it lifts one front hoof and paws forward and LOW, chest dropping, ears pricked flat forward, and every snowflake twinkles out and back in a rolling wave from left to right.
2.2s — it drops into a deep crouch on all fours, legs folded, body low and compact, and the red nose pulses three quick beats.
2.5s — it twists its whole body to one side, hind quarters swinging out, tail flicking up short, and the golden-brown body flashes brighter row by row from the hooves upward.
2.8s — it twists hard the other way, the antlers raking sideways across the frame, and the snowflakes flash on and off in alternating pairs.
3.1s — it kicks both back legs out behind it in a small low buck, head tucked down between the shoulders, and a chase of colour runs UP from the hooves to the antler tips.
3.4s — it stamps one front hoof down twice fast, head turned square to camera, ears flicking back, and the red nose strobes with each stamp.
3.7s — it shakes its whole head side to side fast, the antlers blurring left-right-left, body held low and square, and every snowflake swaps colour white to pale blue.
3.9s — it lands square on all four hooves, head turned proudly to camera, antlers spread wide but held level, and the whole picture — body, antlers, nose and every snowflake — flashes to maximum brightness twice in quick succession for the final beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. Coloured light spills and shifts across the snow below with every change.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. When the wall snaps on, the lit picture sits inside the curtain rectangle with a wide band of dark unlit wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from 1.0s to the last frame. The reindeer is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the frame it first appears. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark wall between the highest lit point of the artwork — the tips of the antlers — and the top edge of the curtain, and the same clear margin at the bottom and at both sides. No antler tip, no hoof, no tail and no snowflake ever touches or crosses the edge of the curtain, and nothing lit ever appears on the dark bronze gutter, the downpipe, the roof, the sky or the fence. If a pose would raise the antlers or widen the body past that margin, THE POSE IS DRAWN SMALLER AND LOWER — the artwork is never enlarged and the rectangle is never enlarged to fit it. IT NEVER REARS UP AND THE ANTLERS ARE NEVER THROWN HIGH. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: twisting, crouching, leaning, stamping, bucking low, flashing and chasing — never stretching upward. It also stays ON THE SPOT and centred; it never walks or slides sideways across the curtain.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the warm cream stucco wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical BLACK wires hung side by side from a header cable pinned under the roof edge, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin BLACK wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

HARD RULES: NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video. Nobody walks into frame.

AUDIO: natural room sound only — no music, no score, no background song. Quiet cold suburban night ambience, a faint distant car, one soft UI tap on the press, a faint electrical buzz as the wall comes on. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, slight motion blur in the highlights, natural phone screen glow on the fingers, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C05 — Walkway approach

**In the cut:** `starting_frames/v25_c05_g1.png` → `clips/v25_c05_g2.mp4`

#### Image prompt — `starting_frames/v25_c05_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `f21070fe-78e7-492b-a6fb-4f54af191c0b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260913_223635_f21070fe-78e7-492b-a6fb-4f54af191c0b.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_24_assets/starting_frames/v24_c05_g1.png` · Higgsfield media `2636adf4-aa20-49e0-91f0-5071fcd803e0`

````text
Same shot as the attached reference - same camera, same framing, same night-time street, same big lit LED curtain filling the house wall. Change only these things:

1. A DIFFERENT HOUSE: a deep forest-green clapboard two-storey with cream trim, cream window frames and a cream porch rail, instead of the navy-blue one with white trim.

2. A DIFFERENT PICTURE IN THE LIGHTS: a REINDEER with big spreading antlers, warm golden-brown body and a glowing red nose, standing in profile with its head turned to the camera, with white snowflakes falling around it.

3. Different foreground: a low grey fieldstone wall running along the left instead of the white picket fence, and a straight snowy path lined with small warm-white ground lights instead of the curved one.

THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark house wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.

Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v25_c05_g2.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `9d77ce32-705a-480a-82d4-7d1fc673d6ce`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_134705_9d77ce32-705a-480a-82d4-7d1fc673d6ce.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v25_c05_g2.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c05_g1.png` · Higgsfield media `1de11ee7-7fc1-45da-93bd-8a7c1bbe8686`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same DEEP FOREST-GREEN CLAPBOARD two-storey house with cream trim, cream window frames and a cream porch rail, same low grey fieldstone wall running along the left, same straight shovelled snowy path lined with small warm-white ground lights, same snow-dusted shrubs, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing a big REINDEER with wide spreading antlers, a warm golden-brown body and a glowing red nose, standing in profile with its head turned toward the camera, with white snowflakes falling around it.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the fieldstone wall, the shrubs, the little ground lights and the snow banks at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit reindeer sits inside the curtain rectangle with a wide band of dark unlit wall above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The reindeer is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark wall between the highest lit point of the artwork — the tips of the antlers — and the top edge of the curtain, and the same clear margin at the bottom and at both sides. No antler tip, no hoof, no tail and no snowflake ever touches or crosses the edge of the curtain, and nothing lit ever appears on the cream trim, the porch, the roof, the sky or the neighbouring houses. If a pose would raise the antlers or widen the body past that margin, THE POSE IS DRAWN SMALLER AND LOWER — the artwork is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: twisting, crouching, leaning, stamping, bucking low, flashing and chasing — never stretching upward, never rearing. It also stays ON THE SPOT and centred; it never walks or slides sideways across the curtain. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail and does not gain size.

MOVEMENT — RELENTLESS, AND IT NEVER STOPS. The animation is already ON, already mid-move and already running at full speed in the very first frame — there is NO still opening frame, NO pause, NO switch-on — and it is STILL running hard in the last frame. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST TWO things are changing at once: the reindeer's whole-body pose AND a lighting effect somewhere else in the picture. There is no held pose, no still frame, no settle, no gentle drifting. Every pose is a clearly different WHOLE-BODY pose, the figure fully redrawing between beats like an animated light-bulb sign:
0.0s — it lands out of the first frame already mid-move, head dropped low and swung hard to one side so the antlers sweep sideways and DOWN, front knees bent, while the red nose fires to double brightness.
0.3s — it swings the head and antlers hard to the other side, shoulders dipping with it, and every snowflake around it shifts down a row.
0.6s — it lifts one front hoof and paws forward and LOW, chest dropping, ears pricked flat forward, and a bright chase of colour runs down its whole body from head to tail.
0.9s — it drops into a deep crouch on all fours, legs folded, body low and compact, and the red nose pulses three quick beats.
1.2s — it twists its whole body to one side, hind quarters swinging out, tail flicking up short, and every snowflake twinkles out and back in a rolling wave from left to right.
1.5s — it twists hard the other way, the antlers raking sideways across the frame, and the golden-brown body flashes brighter row by row from the hooves upward.
1.8s — it kicks both back legs out behind it in a small low buck, head tucked down between the shoulders, and the snowflakes flash on and off in alternating pairs.
2.1s — it stamps one front hoof down twice fast, head turned square to camera, ears flicking back, and the red nose strobes with each stamp.
2.4s — it shakes its whole head side to side fast, the antlers blurring left-right-left, body held low and square, and a chase of colour runs UP from the hooves to the antler tips.
2.7s — it bows, front legs folded under, chest almost to the ground, antlers angled down and forward, and every snowflake around it swaps colour white to pale blue.
3.0s — it pops back up square, shoulders shimmying left-right-left, and the outline of the whole body flashes brighter one bulb row at a time.
3.3s — it kicks one hind leg out low to the side, the other planted, head swung across its body, and the red nose flares to maximum.
3.6s — it bounces on the spot twice, all four legs compressing and springing, the whole figure squashing and stretching, and the snowflakes twinkle out and back in a rolling wave the other way.
3.9s — it lands square on all four hooves, head turned proudly to camera, antlers spread wide but held level, and the whole picture — body, antlers, nose and every snowflake — flashes to maximum brightness twice in quick succession for the final beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. Coloured light spills and shifts across the snow below with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the front facade wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

HARD RULES: no people, no cars, no pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C05 on disk (1)**

#### Video prompt — `clips/v25_c05_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `0ec6ab46-21f4-4999-bb83-dc92b25faabe`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_123642_0ec6ab46-21f4-4999-bb83-dc92b25faabe.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c05_g1.png` · Higgsfield media `1de11ee7-7fc1-45da-93bd-8a7c1bbe8686`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same DEEP FOREST-GREEN CLAPBOARD two-storey house with cream trim, cream window frames and a cream porch rail, same low grey fieldstone wall running along the left, same straight shovelled snowy path lined with small warm-white ground lights, same snow-dusted shrubs, same neighbouring houses and bare trees, same lit LED curtain hanging across the front facade wall showing a big REINDEER with wide spreading antlers, a warm golden-brown body and a glowing red nose, standing in profile with its head turned toward the camera, with white snowflakes falling around it.

CAMERA — FIRST-PERSON POV. The person filming is WALKING FORWARD up the shovelled path toward the house, one continuous four-second take. THE CAMERA ITSELF IS THE PHONE, so we see ONLY what the walker sees. The house grows steadily and continuously larger and NEVER recedes. Natural bodyweight rise-and-fall with each stride, a slight left-right sway, strong parallax — the fieldstone wall, the shrubs, the little ground lights and the snow banks at the edges of frame sweep past and out of frame much faster than the house moves. THIS IS WALKING, NOT ZOOMING: no focal length change, no digital zoom, no push-in, no dolly rig smoothness, no gimbal glide, no drone move. Handheld, breathing, slightly imperfect.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove, no device and no object of any kind in the foreground or along the bottom edge at any moment. The bottom of frame shows only the snowy path ahead.

MOVEMENT — the animation on the wall is already ON and running at full speed in the very first frame and is STILL running in the last frame. A CLEARLY DIFFERENT POSE EVERY HALF SECOND, the figure fully redrawing between beats like a hand-drawn light-bulb sign:
0.0-0.5s — the reindeer tosses its head up and back so the big antlers swing high, and the red nose flashes to double brightness.
0.5-1.0s — it lifts one front hoof high and paws the air, its whole body tipping with the movement, ears pricked forward.
1.0-1.5s — it lowers its head right down toward the snow and swings the antlers wide to the other side, ears flicking back.
1.5-2.0s — it springs up with both front hooves off the ground, tail flicking, while every snowflake around it shifts down a row.
2.0-2.5s — it lands, turns its head fully to camera and the red nose pulses in three quick beats, the antlers held still and wide.
2.5-3.0s — it kicks both back legs out behind it in a small buck, head down, antlers sweeping forward.
3.0-3.5s — it rears slightly, both front hooves up together, and every snowflake around it twinkles out and back in a rolling wave.
3.5-4.0s — it plants all four hooves, straightens up tall with the antlers spread at their full width, head turned proudly to camera, and the red nose flares brightest for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the front facade wall of the house". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the garage door behind it: its seams, its trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No hoof, no antler tip and no snowflake ever crosses outside the curtain rectangle. If a pose would take the antlers or a leg out to an edge, THE POSE IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. Nothing spills onto the cream trim, the porch, the roof, the sky or the neighbouring houses. As the camera walks closer the bulb grid simply becomes coarser and the individual bulbs become bigger and more countable — the artwork does not gain detail.

HARD RULES: no people, no cars, no pets enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold quiet suburban night ambience, boots crunching rhythmically on packed snow with each stride, breath, a faint distant car, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, slight motion blur on the walk, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C06 — Crowd at the garage

**In the cut:** `starting_frames/v25_c06_g1.png` → `clips/v25_c06_g3.mp4`

#### Image prompt — `starting_frames/v25_c06_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `e1721c55-2092-4ba2-ad2e-171f98333bf2`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260913_223635_e1721c55-2092-4ba2-ad2e-171f98333bf2.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_24_assets/starting_frames/v24_c06_g1.png` · Higgsfield media `d1f5ffc7-609c-4403-a131-14555bc9639b`

````text
Same shot as the attached reference - same camera, same framing, same crowd of onlookers in silhouette at the bottom, same big lit LED curtain filling the garage wall. Change only these things:

1. A DIFFERENT HOUSE: warm red brick with a white double garage door, instead of the grey stucco with the charcoal door.

2. A DIFFERENT PICTURE IN THE LIGHTS: a big decorated CHRISTMAS TREE in green with round red and gold baubles on it and a bright gold star on top, with a few wrapped presents at its base.

3. A tall bare birch tree at the right edge and a snow-covered hedge running along the left edge, instead of the spruces and the pickup truck.

THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark garage wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.

Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v25_c06_g3.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `a0472685-6417-4a3e-af15-466d0f77b18b`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_144850_a0472685-6417-4a3e-af15-466d0f77b18b.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v25_c06_g3.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c06_g1.png` · Higgsfield media `08a7266c-db88-43f4-9fdf-c0e113c88607`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same WARM RED BRICK house, same WHITE double garage door, same driveway throwing coloured light back, same tall bare birch tree at the right edge and same snow-covered hedge running along the left edge, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing one big decorated CHRISTMAS TREE in green with round red and gold baubles on it, a bright gold star on top and a few wrapped presents at its base.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit tree sits inside the curtain rectangle with a wide band of dark unlit garage door above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The tree is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark door between the highest lit point of the artwork — the tip of the gold star — and the top edge of the curtain, and the same clear margin at the bottom below the presents and at both sides beyond the widest branches. No branch tip, no point of the star, no bauble, no corner of a present and no elf ever touches or crosses the edge of the curtain, and nothing lit ever appears on the red brick, the gables, the roof, the sky, the birch tree or the hedge. If a beat would raise the star or widen the branches past that margin, THE ARTWORK IS DRAWN SMALLER AND LOWER — it is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: leaning, swaying, squashing, twisting, flashing and chasing — never stretching upward. The tree also stays ON THE SPOT and centred; it never slides sideways across the curtain. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

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

THE LIGHT PICTURE IS A LITTLE CARTOON THAT PLAYS OUT, NOT A TREE THAT SITS THERE FLASHING. There are TWO layers of movement running at the same time for the whole four seconds, and BOTH are big, obvious, travelling movements that read clearly even from the bottom of the driveway:
LAYER ONE — THE TREE ITSELF MOVES ITS WHOLE BODY. It is a dancing tree, not a decorated post. It bends, leans, squashes, springs and twists as one solid silhouette, the whole green shape visibly redrawing between beats. Every lean is a BIG lean — the trunk bowing well over to one side, the branch tiers stacking over on themselves, the gold star swinging out sideways over the branches below. Every squash is a BIG squash — the whole silhouette dropping and fanning wide, then springing back. These are not small wobbles: between one beat and the next, the tree's outline is unmistakably a different shape.
LAYER TWO — ELVES WALK IN FROM BOTH SIDES CARRYING PRESENTS. Small chunky ELF figures, lit in bright green and red with pointed hats and curled-toe boots, march IN ALONG THE BOTTOM OF THE CURTAIN from the left edge and from the right edge, each one carrying a wrapped present held out in front of it in both arms. They walk with a big bouncy stomping stride, knees lifting high, hats bobbing with every step — the walk cycle drawn by whole bulbs switching, so they visibly stomp rather than glide. They cross the dark band of unlit door toward the base of the tree, set their present down on the growing pile at its foot, wave both arms over their heads in celebration, and turn and march back out the way they came. A new elf enters roughly every half second, alternating sides, so at any instant there are elves walking in, elves setting down, and elves marching out — the bottom of the picture is never empty and never still, and the pile of presents at the base of the tree GROWS bigger and wider across the four seconds as more are stacked on.
ELF CONTAINMENT: the elves are SMALL — no taller than the bottom tier of branches — and they stay in the BOTTOM BAND of the curtain the whole time. They enter from just INSIDE the left and right edges of the curtain and they walk out to just INSIDE those same edges — they never touch the edge, never cross it, never appear on the brick, the hedge, the birch or the driveway. They stay below the tree's lowest branches at all times and never climb, never jump high, never get in front of the star. The growing present pile spreads SIDEWAYS along the bottom band, never upward into the branches, and it always keeps the clear dark margin below it and at both sides.

THE ANIMATION IS RELENTLESS FROM FRAME ONE. THE BIGGEST MISTAKE WOULD BE A QUIET START. At 0.0s the artwork is already mid-cycle, already loud, already changing, and two elves are already mid-stride inside the frame — the picture does NOT switch on, does NOT hold still, does NOT ease in, and there is NOTHING calm about the first half second. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST THREE things are changing at once: the whole-body shape of the tree, an elf travelling across the bottom band, and a lighting effect somewhere else in the picture. There is no held frame, no pause, no settle:
0.0s — the clip opens mid-action: the tree is already bowed hard over to the LEFT, star swung out sideways, AND one elf is already halfway in from the left edge mid-stomp with a present in its arms while a second elf is just stepping in from the right edge, AND a bright chase of colour is already running down the tree from the star toward the base.
0.3s — the tree springs upright and squashes down wide at the base; the left elf reaches the foot of the tree and sets its present down with a bend of the knees; every red bauble swaps to gold and every gold bauble swaps to red, row by row down the tree.
0.6s — the tree bows hard over to the RIGHT, branch tiers stacking over, and the elf that just delivered throws both arms over its head, spins on the spot and starts marching back out to the left; a third elf enters from the right edge.
0.9s — the tree shimmies left-right-left fast; the gold star spins on the spot with its points stretching and shortening; the two elves on the bottom band cross paths in opposite directions, one in, one out.
1.2s — the tree squats deep, the whole silhouette compressing and fanning wide, then springs back; every bauble twinkles out and back in a rolling wave from left to right; the right elf sets down its present and the pile at the base gets visibly wider.
1.5s — the tree leans forward and nods twice like it is bowing; a chase of light runs DOWN the tree from the star to the presents one branch row at a time; a fourth elf stomps in from the left edge with a bigger present held high against its chest.
1.8s — the tree twists to one side, branches raking sideways; the present pile at the base bounces on the spot one after another; two elves wave both arms together and every bauble strobes twice fast.
2.1s — the tree twists hard the other way, baubles swinging out wide with the movement; an elf at the right hops twice on the spot before setting its present down; the star drops to half brightness then snaps back to full.
2.4s — the tree bows hard LEFT again, deeper than before; a chase of colour runs UP from the present pile to the star; a fifth elf enters from the right edge and two elves march out to the left, all three in stride at once.
2.7s — the tree bounces on the spot twice, squashing and stretching at the base with each bounce; every branch row swaps colour green to warm gold and back, row by row; the elves on the bottom band stomp in time with the bounces.
3.0s — the tree leans hard RIGHT and holds the lean while shivering; the star flares with a big ring of short spokes; every bauble and every present in the pile flashes in alternating pairs; a sixth elf stomps in from the left.
3.3s — the tree snaps upright and shimmies fast; a chase of light runs all the way around the outer edge of the silhouette; three elves at the base jump on the spot together, arms up.
3.6s — the tree squats wide one last time and springs back; the present pile strobes in sequence left to right then right to left; the last elves turn and march back out toward both edges.
3.9s — the tree lands square and centred, and the whole picture — tree, every bauble, the star, the whole grown pile of presents and every elf still in frame — flashes together to maximum brightness twice in quick succession for the final beat.
Every change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing, never a crossfade. The elves are drawn as chunky blocky bulb figures with no facial detail. The coloured reflections on the driveway shift and ripple with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the white garage door behind it: its horizontal panel seams, its rim of trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

HARD RULES: nobody turns around, no face is shown toward camera. No new real people walk into frame — the only new figures anywhere in the shot are the ELVES made of light inside the curtain. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

**Other takes of C06 on disk (2)**

#### Video prompt — `clips/v25_c06_g1.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `3cd7fadc-0af5-4b81-85cb-e488515adc03`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_123641_3cd7fadc-0af5-4b81-85cb-e488515adc03.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c06_g1.png` · Higgsfield media `08a7266c-db88-43f4-9fdf-c0e113c88607`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same WARM RED BRICK house, same WHITE double garage door, same driveway throwing coloured light back, same tall bare birch tree at the right edge and same snow-covered hedge running along the left edge, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing one big decorated CHRISTMAS TREE in green with round red and gold baubles on it, a bright gold star on top and a few wrapped presents at its base.

ABSOLUTE FIRST RULE — THE LIT PICTURE IS TRAPPED INSIDE THE CURTAIN RECTANGLE. In the reference image the lit LED curtain is a rectangle hanging across the white garage door only, and it stops short of the door's edges. That rectangle is FIXED for the whole four seconds: it never grows, never widens, never rises, never rescales, never warps, never drifts, and the camera never changes size on it. The tree, its star, its baubles and the presents at its base are drawn INSIDE that rectangle with a clear band of unlit dark door left all the way round — a generous margin at the top above the star, and margins at the left, right and bottom.
NOTHING LIT EVER CROSSES AN EDGE. No branch tip, no point of the star, no bauble and no corner of a present ever touches or crosses the edge of the curtain, and nothing lit ever appears on the red brick, the gables, the roof, the sky, the birch tree or the hedge. If a pose would take a branch or the star out to an edge, THE ARTWORK IS MADE SMALLER so it stays inside — the rectangle is never made bigger to fit it. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

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

THE ARTWORK IS ALREADY ANIMATING IN THE FIRST FRAME — it is mid-cycle at 0.0s, not switching on and not holding still, and it changes again at 0.2s. THE TREE IS NEVER A STILL PICTURE FOR EVEN ONE BEAT. It stays in the same place on the door and keeps its shape, but its lights and its parts change constantly: at 0.2s and again at 0.6s the gold star on top flares to double brightness and throws a ring of short spokes out around it, then drops back; at 1.0s every red bauble swaps to gold and every gold bauble swaps to red, row by row down the tree; at 1.4s the whole tree leans a few degrees to one side and back again like it is swaying, the baubles swinging with it; at 1.8s a bright chase of light runs down the tree from the star to the base, one branch row at a time; at 2.2s the wrapped presents at the base flash on one after another from left to right, each one a different colour; at 2.6s the tree leans the other way and every bauble twinkles out and back at once; at 3.0s the star spins on the spot, its points stretching and shortening; at 3.4s a second chase runs UP the tree from the presents to the star; at 3.8s the whole tree, every bauble, the star and all the presents flash together to maximum brightness for the last beat. Every change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing. The coloured reflections on the driveway shift and ripple with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the white garage door behind it: its horizontal panel seams, its rim of trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE GARAGE DOOR IS THE ONLY LIT SURFACE. The artwork is hard-cropped at all four edges of the curtain. It NEVER grows, shrinks, shifts, warps or drifts. Nothing spills onto the red brick, the gables, the roof, the sky, the birch tree or the hedge.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

#### Video prompt — `clips/v25_c06_g2.mp4`

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `2f582714-bba6-4b2c-afeb-2d0ea091e481`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_134915_2f582714-bba6-4b2c-afeb-2d0ea091e481.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c06_g1.png` · Higgsfield media `08a7266c-db88-43f4-9fdf-c0e113c88607`

````text
Wholesome neighbourhood Christmas scene, warm and jolly. Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same WARM RED BRICK house, same WHITE double garage door, same driveway throwing coloured light back, same tall bare birch tree at the right edge and same snow-covered hedge running along the left edge, same crowd of neighbours seen FROM BEHIND standing and sitting on the snow in winter coats and bobble hats, same lit LED curtain across the garage door showing one big decorated CHRISTMAS TREE in green with round red and gold baubles on it, a bright gold star on top and a few wrapped presents at its base.

ABSOLUTE RULE — THE ARTWORK NEVER CHANGES SIZE. In the reference image the lit tree sits inside the curtain rectangle with a wide band of dark unlit garage door above it, below it and at both sides. THAT EXACT SIZE AND THAT EXACT POSITION ARE LOCKED from the first frame to the last. The tree is the same number of bulbs tall and the same number of bulbs wide in the final frame as in the first frame. It NEVER scales up, never grows, never inflates, never creeps upward, never fills more of the curtain than it does at the start. There is ALWAYS a clear band of at least six unlit bulb rows of dark door between the highest lit point of the artwork — the tip of the gold star — and the top edge of the curtain, and the same clear margin at the bottom below the presents and at both sides beyond the widest branches. No branch tip, no point of the star, no bauble and no corner of a present ever touches or crosses the edge of the curtain, and nothing lit ever appears on the red brick, the gables, the roof, the sky, the birch tree or the hedge. If a beat would raise the star or widen the branches past that margin, THE ARTWORK IS DRAWN SMALLER AND LOWER — it is never enlarged and the rectangle is never enlarged to fit it. BECAUSE IT CANNOT GROW, ALL ITS ENERGY GOES SIDEWAYS, DOWNWARDS AND INTO THE BULBS: leaning, swaying, squashing, twisting, flashing and chasing — never stretching upward. The tree also stays ON THE SPOT and centred; it never slides sideways across the curtain. The garage door outside the curtain, and every surface around it, stays dark the whole four seconds.

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

THE TREE ANIMATION IS THE MAIN EVENT AND IT IS RELENTLESS FROM FRAME ONE. THE BIGGEST MISTAKE WOULD BE A QUIET START. At 0.0s the artwork is already mid-cycle, already loud, already changing — it does NOT switch on, does NOT hold still, does NOT ease in, and there is NOTHING calm about the first half second. SOMETHING CHANGES EVERY THREE TENTHS OF A SECOND — that is at least THIRTEEN separate changes across the four seconds — and at every single instant AT LEAST TWO things are changing at once: the shape or lean of the tree AND a lighting effect somewhere else in the picture. There is no held frame, no pause, no settle. The tree keeps its place and its size but its lights and its parts change constantly:
0.0s — the clip opens mid-flash: the gold star is already flaring at double brightness throwing a ring of short spokes around it, AND a bright chase of colour is already halfway down the tree from the star toward the base.
0.3s — every red bauble swaps to gold and every gold bauble swaps to red, row by row down the tree, while the whole tree leans a few degrees to one side and the baubles swing with it.
0.6s — the tree leans hard the other way and back, squashing slightly at the base, and the wrapped presents flash on one after another from left to right, each a different colour.
0.9s — the star spins on the spot, its points stretching and shortening, and the outline of the tree flashes brighter one branch row at a time from the base upward.
1.2s — every bauble twinkles out and back at once in a rolling wave from left to right, while the tree gives a quick side-to-side shimmy.
1.5s — a chase of light runs DOWN the tree from the star to the presents, one branch row at a time, and the tree squats — the whole silhouette compressing down and widening — then springs back.
1.8s — the presents at the base bounce on the spot one after another, and every bauble strobes twice fast.
2.1s — the tree twists to one side, branches raking sideways, and the star drops to half brightness then snaps back to full.
2.4s — the tree twists hard the other way and the baubles swing out wide with the movement, while a chase of colour runs UP from the presents to the star.
2.7s — the whole tree shimmies left-right-left fast, and every branch row swaps colour green to warm gold and back, row by row.
3.0s — the star flares again with a bigger ring of spokes, and every bauble and every present flashes in alternating pairs.
3.3s — the tree leans forward and back like it is nodding, the baubles bobbing, and a fast chase runs around the outer edge of the silhouette.
3.6s — the tree bounces on the spot twice, squashing and stretching at the base, and the presents strobe in sequence left to right then right to left.
3.9s — the whole picture — tree, every bauble, the star and all the presents — flashes together to maximum brightness twice in quick succession for the final beat.
Every change is rendered by bulbs switching on and off row by row across the grid like an animated light-bulb sign — chunky and instantaneous, never smooth morphing, never a crossfade. The coloured reflections on the driveway shift and ripple with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable pinned under the garage lintel, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the white garage door behind it: its horizontal panel seams, its rim of trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark garage door, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the door: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the door behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

HARD RULES: nobody turns around, no face is shown toward camera. No new people walk into frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Cold outdoor night ambience, relaxed overlapping chatter, easy natural laughter, children calling to each other, the odd loose clap, boots on wet snow, a faint electrical hum from the lights.

LOOK: real iPhone UGC at night. Noisy shadows, blown highlights around the bulbs, natural handheld wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````

### C07 — Drive-by from the car

**In the cut:** `starting_frames/v25_c07_g1.png` → `clips/v25_c07_g1.mp4`

#### Image prompt — `starting_frames/v25_c07_g1.png` — IN THE CUT

**Settings** - gpt_image_2 · 9:16 · 2k · medium · 1520×2688
**Job** - `d76217c3-1d6a-4c92-9d4a-ff7378c7e496`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260913_223635_d76217c3-1d6a-4c92-9d4a-ff7378c7e496.png (same byte size as the local file)
**References, in submission order**
- @Image 1: `content/video_24_assets/starting_frames/v24_c07_g1.png` · Higgsfield media `862a6e66-770c-4033-b92b-676d15c2ad48`

````text
Same shot as the attached reference - same camera shooting out through the car side window at night, same wet road with reflections, same big lit LED curtain filling the house gable edge to edge. Change only these things:

1. A DIFFERENT HOUSE: a pale grey stone gable with white trim and white window frames, instead of the white board-and-batten one with black trim.

2. A DIFFERENT PICTURE IN THE LIGHTS: a full-height ELF in a green tunic and green pointed hat with a red belt and curled red-and-white striped shoes, one hand raised in a wave, with small red and white candy canes scattered around him.

3. A different parked car at the kerb - a dark red hatchback instead of the silver estate - and a snow-covered garden bench at the right edge instead of the mailbox.

THE CURTAIN - CRITICAL: it is a curtain of hanging vertical see-through light strands, NOT a solid LED video panel and NOT a flat screen. You can see the dark gable wall between the strands. The strands are DENSELY spaced, with many small round bulbs closely spaced along each one, so the picture has plenty of resolution and reads as beautiful and high quality.

Real iPhone night photo, tack-sharp, candid UGC, no text, no watermark.
````

#### Video prompt — `clips/v25_c07_g1.mp4` — IN THE CUT

**Settings** - seedance_2_5 · 1080p · 4 s · 9:16 · audio on
**Job** - `ca957a4d-0727-4c53-9830-5cfa3ca3db01`
**Result** - https://d8j0ntlcm91z4.cloudfront.net/user_REMOVED/hf_20260914_123640_ca957a4d-0727-4c53-9830-5cfa3ca3db01.mp4 (byte-identical to the local file, md5 checked 2026-09-23)
**Upscaled derivative** - `clips/upscaled/v25_c07_g1.mp4` (1440×2560)
**Attached, in submission order**
- start frame: `content/video_25_assets/starting_frames/v25_c07_g1.png` · Higgsfield media `88972a61-8191-49a8-963d-f5b102126df8`

````text
Animate the reference image exactly as it is. The first frame of the video IS the reference image, unchanged — same night, same view shot from inside a moving car through the open passenger side window with the dark window frame framing the bottom-left corner, same wet reflective road throwing long smeared coloured reflections, same snowy verge, same street lamp, same row of neighbouring houses glowing down the street, same DARK RED HATCHBACK parked at the kerb, same snow-covered garden bench at the right edge, same lit LED curtain on the PALE GREY STONE gable wall with white trim showing a full-height ELF in a green tunic and a green pointed hat with a red belt and curled red-and-white striped shoes, one hand raised in a wave, with small red and white candy canes scattered around him.

CAMERA — HANDHELD VERTICAL PHONE VIDEO SHOT OUT OF A MOVING CAR SIDE WINDOW AT NIGHT. THE CAR IS DRIVING FORWARD and closing in on the house, so the gable wall grows steadily and continuously LARGER across the four seconds and NEVER recedes. Real vehicle motion: the road surface and the snow verge flow past the bottom of frame at speed, roadside objects sweep past with strong parallax, the frame rocks gently with the suspension. As the car advances the operator slowly pans right to hold the lit wall in frame. THIS IS DRIVING, NOT ZOOMING: no focal length change, no digital zoom, no gimbal glide, no drone move.

HARD NEGATIVE — NO PHONE IN SHOT. There is no phone, no screen, no hand, no fingers, no thumb, no arm, no sleeve, no glove and no device anywhere in the foreground. Only the car's own dark window frame, exactly as in the reference image, sits at the bottom-left.

MOVEMENT — THE ELF MUST NOT STAND STILL. He stays on the spot the whole four seconds but is never a static standing figure for even one beat. This is the most important instruction in this prompt: a CLEARLY DIFFERENT WHOLE-BODY POSE EVERY HALF SECOND, the figure fully redrawing between beats like an animated light-bulb sign.
0.0-0.5s — his raised hand swings down and across his body while the other arm comes up instead, the long point of his green hat whipping over to the opposite side.
0.5-1.0s — he bends both knees deep and hops on the spot, both arms straight out sideways, his curled striped shoes kicking up, the red belt flashing brighter.
1.0-1.5s — he lands and leans hard to one side, one leg kicked straight out, both hands on his hips and his grin stretched wide.
1.5-2.0s — he spins on the spot with his arms tucked in tight, the green tunic flaring out, and the candy canes around him swap over and change colour as he turns.
2.0-2.5s — he drops into a low crouch, both hands on the ground in front of him, the point of his hat hanging forward past his face.
2.5-3.0s — he springs straight back up and throws both arms over his head, and every candy cane around him twinkles out and back in a rolling wave from left to right.
3.0-3.5s — he kicks one striped shoe high in front of him, one arm windmilling to keep his balance, eyes wide and mouth round.
3.5-4.0s — he plants both shoes, straightens up tall and throws both arms out wide in a big proud finishing pose, the hat bobbing and the whole green tunic flashing brighter for the last beat.
Every pose change is rendered by bulbs switching on and off row by row across the grid — chunky and instantaneous, never smooth morphing, never a crossfade. The coloured reflections on the wet road shift and streak with every change.

CRITICAL — HOW THE LIGHTS MUST BE BUILT. SURFACE OVERRIDE: wherever the block below says "garage door", read "the pale grey stone gable wall". Everything else in the block applies exactly as written.
The picture on the garage door is NOT an LED video wall, NOT a screen, NOT a projection. It is a hanging curtain of LED string lights: many thin vertical wires hung side by side from a header cable, each wire carrying small round bulbs. Build the whole picture out of VERTICAL DOTTED LINES OF LIGHT. The horizontal gap between neighbouring strands is visibly WIDER than the vertical gap between bulbs on the same strand, so the grid is tall and rectangular — never a square pixel matrix.
The curtain is SEE-THROUGH. Through the gaps between strands you clearly read the wall behind it: its stone courses, its white trim, the faint shadows of the wires falling on it. The unlit areas are NOT a solid coloured field — they are simply dark wall, with the unlit bulbs showing as tiny dull grey dots and the thin dark wires as faint vertical lines.
Every lit bulb is a tiny point source: blown-out white core, coloured halo bleeding around it, a small soft star flare, individually countable. The artwork is extremely low resolution and blocky — chunky stepped edges, no smooth curves, no thin outlines, no small facial detail, no gradients, no anti-aliasing.
The curtain hangs a few inches proud of the wall: the strands sag slightly, each strand ends at a slightly different height so the bottom hem is uneven and wavy, a faint breeze tilts the sheet, and the glow bounces back off the wall behind it as a soft halo. Light spills onto the snow in a speckled uneven pattern, not a flat even wash.
ABSOLUTELY NO: LED video wall, TV screen, monitor, jumbotron, projector image, black backing panel, bezel or frame, dense square pixel grid, solid saturated background field, smooth clean vector artwork. Real amateur photo, natural noise, no CGI polish.

ABSOLUTE HARD RULE — THE ANIMATION STAYS INSIDE THE CURTAIN. The lit rectangle is hard-cropped at all four edges like a bezel. It NEVER grows, shrinks, shifts, warps or drifts on the wall. No shoe, no arm, no point of his hat and no candy cane ever crosses the roof edge or the corner of the wall — his raised arms and his kicking legs always keep a clear margin of dark wall inside the rectangle. He also never walks sideways across the curtain; he stays ON THE SPOT and stays centred. Nothing spills onto the roof, the white trim, the sky, the verge, the parked dark red hatchback or the neighbouring houses. As the car gets closer the bulb grid simply becomes coarser and the individual bulbs bigger and more countable — the artwork does not gain detail.

HARD RULES: no people and no other vehicles enter the frame. NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS, NO SIGNS anywhere in the light artwork, and no captions, subtitles or watermark anywhere in the video.

AUDIO: natural room sound only — no music, no score, no background song. Tyres on wet road, a low engine hum, cold air rushing past the open window, a faint electrical hum from the lights. No voice.

LOOK: real iPhone UGC at night from a car. Noisy shadows, blown highlights around the bulbs, slight rolling-shutter wobble, no cinematic grade, no lens flare, no slow motion, no speed ramp.
````
